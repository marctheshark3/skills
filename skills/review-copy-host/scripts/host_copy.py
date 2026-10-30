#!/usr/bin/env python3
"""Host one approved HTML copy; authorization is the caller's responsibility."""
import argparse
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import select
import shutil
import signal
import stat
import subprocess
import sys
import time


def process_stat(pid):
    try:
        fields = Path(f'/proc/{pid}/stat').read_text().rsplit(')', 1)[1].split()
    except FileNotFoundError:
        return None
    return {'state': fields[0], 'startTime': fields[19]}


def record_process(process, argv):
    info = process_stat(process.pid)
    if info is None:
        raise RuntimeError('Started process exited before its identity was recorded')
    return {'pid': process.pid, 'argv': argv, 'startTime': info['startTime'],
            'bootId': Path('/proc/sys/kernel/random/boot_id').read_text().strip()}


def owned_pidfd(process):
    """Pin a process lifetime before inspecting or signaling its numeric PID."""
    try:
        descriptor = os.pidfd_open(process['pid'])
    except ProcessLookupError:
        return None
    try:
        if select.select([descriptor], [], [], 0)[0]:
            os.close(descriptor)
            return None
        info = process_stat(process['pid'])
        if info is None or info['state'] in ('Z', 'X'):
            os.close(descriptor)
            return None
        actual = Path(f"/proc/{process['pid']}/cmdline").read_bytes().split(b'\0')[:-1]
        boot = Path('/proc/sys/kernel/random/boot_id').read_text().strip()
        if (info['startTime'] != process.get('startTime') or boot != process.get('bootId')
                or actual != [item.encode() for item in process['argv']]):
            if select.select([descriptor], [], [], 0)[0]:
                os.close(descriptor)
                return None
            raise RuntimeError('Process identity mismatch; no process was stopped')
        return descriptor
    except FileNotFoundError:
        os.close(descriptor)
        return None
    except BaseException:
        os.close(descriptor)
        raise


def terminate_pidfd(descriptor):
    try:
        signal.pidfd_send_signal(descriptor, signal.SIGTERM)
    except ProcessLookupError:
        return
    if not select.select([descriptor], [], [], 6)[0]:
        raise RuntimeError('Owned process is still stopping; do not claim removal yet')


def executable(value, name):
    binary = shutil.which(value)
    if not binary:
        raise RuntimeError(f'Existing {name} executable is required; installation needs separate authorization')
    return str(Path(binary).resolve())


def prerequisites(args):
    if sys.version_info < (3, 10):
        raise RuntimeError('Python 3.10 or newer is required')
    if (sys.platform != 'linux' or not hasattr(os, 'pidfd_open')
            or not hasattr(signal, 'pidfd_send_signal')):
        raise RuntimeError('Linux with /proc and Python pidfd support is required')
    try:
        descriptor = os.pidfd_open(os.getpid())
        os.close(descriptor)
    except OSError as error:
        raise RuntimeError('Linux process file descriptors are unavailable') from error
    executable('git', 'Git')
    node = executable(args.node, 'Node 22+')
    version = subprocess.run([node, '--version'], capture_output=True, text=True,
                             check=True, timeout=5).stdout.strip()
    match = re.fullmatch(r'v(\d+)\.\d+\.\d+.*', version)
    if not match or int(match.group(1)) < 22:
        raise RuntimeError('Node 22 or newer is required; choose an existing executable')
    tunnel = None if args.local_only else executable(args.cloudflared, 'cloudflared')
    return node, tunnel

def digest(body):
    return hashlib.sha256(body).hexdigest()

def atomic(path, body):
    temp = path.with_name(path.name + '.next')
    with open(temp, 'wb') as stream:
        os.chmod(temp, 0o600)
        stream.write(body)
    os.replace(temp, path)

def save(path, value):
    atomic(path, (json.dumps(value, indent=2) + '\n').encode())

def load(path):
    return json.loads(path.read_text())

def read_html(path):
    if path.is_symlink() or not stat.S_ISREG(path.stat().st_mode):
        raise RuntimeError('Expected a regular, non-symlink HTML file')
    body = path.read_bytes()
    if not body or len(body) > 1048576:
        raise RuntimeError('HTML size must be between 1 byte and 1 MiB')
    body.decode('utf8')
    return body

def private_directory(path):
    if path.is_symlink():
        raise RuntimeError('State directory must not be a symlink')
    path.mkdir(mode=0o700, parents=True, exist_ok=True)
    if subprocess.run(['git', 'rev-parse', '--git-dir'], cwd=path,
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
        raise RuntimeError('State directory must be outside Git')
    os.chmod(path, 0o700)

def spawn(argv, directory, logfile, children):
    stream = open(directory / logfile, 'ab', buffering=0)
    os.chmod(directory / logfile, 0o600)
    environment = {key: os.environ[key] for key in
                   ('PATH', 'HOME', 'LANG', 'SSL_CERT_FILE', 'SSL_CERT_DIR') if key in os.environ}
    interrupted = []
    handlers = {}
    try:
        # Defer cancellation until the child handle is retained for rollback.
        for sig in (signal.SIGINT, signal.SIGTERM):
            handlers[sig] = signal.signal(sig, lambda number, _frame: interrupted.append(number))
        process = subprocess.Popen(argv, cwd=directory, env=environment,
                                   stdin=subprocess.DEVNULL, stdout=stream,
                                   stderr=subprocess.STDOUT, start_new_session=True)
        children.append(process)
        return record_process(process, argv)
    finally:
        try:
            stream.close()
        finally:
            for sig, handler in handlers.items():
                signal.signal(sig, handler)
        if interrupted:
            raise KeyboardInterrupt

def matches(process):
    try:
        descriptor = owned_pidfd(process)
    except RuntimeError:
        return False
    if descriptor is None:
        return False
    os.close(descriptor)
    return True

def cleanup_children(children):
    """Popen owns these unreaped children, even when they exited before recording."""
    errors = []
    for child in reversed(children):
        try:
            if child.poll() is None:
                child.terminate()
            child.wait(timeout=6)
        except (OSError, subprocess.TimeoutExpired) as error:
            errors.append(str(error))
    return errors

def verify_local(state):
    connection = http.client.HTTPConnection('127.0.0.1', state['port'], timeout=5)
    try:
        connection.request('GET', state['mount'])
        response = connection.getresponse()
        body = response.read(1048577)
        if response.status != 200 or digest(body) != state['sha256']:
            raise RuntimeError('Local response does not match approved bytes')
    finally:
        connection.close()

def up(args):
    directory = args.state_dir
    node, binary = prerequisites(args)
    if directory.exists() and any(directory.iterdir()):
        raise RuntimeError('Choose a fresh, empty state directory')
    private_directory(directory)
    if (directory / 'state.json').exists():
        raise RuntimeError('Existing state: inspect it rather than duplicating or overwriting it')
    body = read_html(args.file)
    atomic(directory / 'preview.html', body)
    save(directory / 'allowed.json', {'sha256': [digest(body)]})
    mount = args.mount
    if not mount.startswith('/') or '?' in mount or '#' in mount or '..' in mount.split('/'):
        raise RuntimeError('Use a plain absolute URL path')
    script = str(Path(__file__).with_name('serve-file.mjs').resolve())
    state = {'mount': mount, 'sha256': digest(body), 'localOnly': args.local_only}
    children = []
    try:
        server = spawn([node, script, '--state', str(directory), '--mount', mount],
                       directory, 'server.log', children)
        state['server'] = server
        save(directory / 'state.json', state)
        for _ in range(100):
            if (directory / 'listener.json').exists():
                listener = load(directory / 'listener.json')
                if listener['pid'] != server['pid'] or listener['host'] != '127.0.0.1':
                    raise RuntimeError('Unexpected listener')
                state['port'] = listener['port']; break
            if not matches(server):
                raise RuntimeError('File server exited')
            time.sleep(0.05)
        else:
            raise RuntimeError('File server did not become ready')
        verify_local(state)
        if not args.local_only:
            atomic(directory / 'empty.yml', b'{}\n')
            argv = [binary, 'tunnel', '--no-autoupdate', '--config', str(directory / 'empty.yml'),
                    '--metrics', '127.0.0.1:0', '--management-diagnostics=false', '--grace-period', '3s',
                    '--url', 'http://127.0.0.1:' + str(state['port'])]
            state['tunnel'] = spawn(argv, directory, 'tunnel.log', children)
            save(directory / 'state.json', state)
            for _ in range(400):
                text = (directory / 'tunnel.log').read_text(errors='replace')
                found = re.search(r'https://[a-z0-9-]+\.trycloudflare\.com', text)
                if found:
                    state['url'] = found.group(0) + mount; break
                if not matches(state['tunnel']):
                    raise RuntimeError('Tunnel exited; inspect its private log')
                time.sleep(0.1)
            else:
                raise RuntimeError('No tunnel URL arrived within 40 seconds')
        save(directory / 'state.json', state)
        return state
    except BaseException as error:
        handlers = {sig: signal.signal(sig, signal.SIG_IGN)
                    for sig in (signal.SIGINT, signal.SIGTERM)}
        try:
            errors = cleanup_children(children)
            state['startupFailed'] = True
            state['cleanupComplete'] = not errors
            try:
                save(directory / 'state.json', state)
            except OSError as save_error:
                errors.append(str(save_error))
        finally:
            for sig, handler in handlers.items():
                signal.signal(sig, handler)
        if errors:
            raise RuntimeError('Startup failed; cleanup errors: ' + '; '.join(errors)) from error
        raise

def replace(args):
    directory = args.state_dir
    state = load(directory / 'state.json')
    if not matches(state['server']):
        raise RuntimeError('The recorded file server is not running')
    body = read_html(args.file)
    old = state['sha256']
    new = digest(body)
    save(directory / 'allowed.json', {'sha256': [old, new]})
    atomic(directory / 'preview.html', body)
    save(directory / 'allowed.json', {'sha256': [new]})
    state['sha256'] = new
    verify_local(state)
    save(directory / 'state.json', state)
    return state

def down(args):
    state = load(args.state_dir / 'state.json')
    descriptors = []
    try:
        for key in ('tunnel', 'server'):
            if key in state:
                descriptor = owned_pidfd(state[key])
                if descriptor is not None:
                    descriptors.append(descriptor)
        errors = []
        for descriptor in descriptors:
            try:
                terminate_pidfd(descriptor)
            except OSError as error:
                errors.append(str(error))
            except RuntimeError as error:
                errors.append(str(error))
        if errors:
            raise RuntimeError('Shutdown incomplete: ' + '; '.join(errors))
    finally:
        for descriptor in descriptors:
            os.close(descriptor)
    state['stopped'] = True
    save(args.state_dir / 'state.json', state)
    return {'stopped': True}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('up', 'replace', 'down', 'status'):
        command = commands.add_parser(name)
        command.add_argument('--state-dir', type=lambda value: Path(value).absolute(), required=True)
        if name in ('up', 'replace'):
            command.add_argument('--file', type=lambda value: Path(value).absolute(), required=True)
        if name == 'up':
            command.add_argument('--mount', default='/review.html')
            command.add_argument('--node', default='node')
            command.add_argument('--cloudflared', default='cloudflared')
            command.add_argument('--local-only', action='store_true')
    args = parser.parse_args()
    def interrupted(_signal, _frame):
        raise KeyboardInterrupt
    signal.signal(signal.SIGTERM, interrupted)
    try:
        result = {'up': up, 'replace': replace, 'down': down,
                  'status': lambda value: load(value.state_dir / 'state.json')}[args.command](args)
        print(json.dumps(result))
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError) as error:
        parser.exit(1, str(error) + '\n')
    except KeyboardInterrupt:
        parser.exit(130, 'Interrupted; inspect retained state before retrying\n')

if __name__ == '__main__':
    main()
