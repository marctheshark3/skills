"""Local behavior regressions; dummy files, owned processes, no public tunnel."""
import argparse
import copy
import http.client
import importlib.util
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch


SOURCE = Path(__file__).resolve().parents[1] / 'skills/review-copy-host/scripts/host_copy.py'
SPEC = importlib.util.spec_from_file_location('review_copy_host', SOURCE)
host = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(host)


class ReviewCopyHost(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='review-copy-regression-', dir='/tmp')
        self.root = Path(self.temp.name)
        self.file = self.root / 'input.html'
        self.file.write_bytes(b'<!doctype html><title>first</title><p>approved first</p>')
        self.directory = self.root / 'state'
        self.node = str(Path(shutil.which('node')).resolve())
        self.children = []
        self.created = []
        spawn = host.spawn

        def retain_children(argv, directory, logfile, children):
            try:
                return spawn(argv, directory, logfile, children)
            finally:
                for child in children:
                    if child not in self.created:
                        self.created.append(child)

        self.spawn_patch = patch.object(host, 'spawn', side_effect=retain_children)
        self.spawn_patch.start()

    def tearDown(self):
        try:
            for child in reversed(self.created + self.children):
                if child.poll() is None:
                    child.terminate()
                child.wait(timeout=6)
        finally:
            self.spawn_patch.stop()
            self.temp.cleanup()

    def args(self, **changes):
        values = dict(state_dir=self.directory, file=self.file, mount='/review.html',
                      node=self.node, cloudflared='cloudflared', local_only=True)
        values.update(changes)
        return argparse.Namespace(**values)

    def start(self):
        state = host.up(self.args())
        return state

    def fetch(self, state, method='GET', target='/review.html'):
        connection = http.client.HTTPConnection('127.0.0.1', state['port'], timeout=5)
        try:
            connection.request(method, target)
            response = connection.getresponse()
            return response.status, response.read(), dict(response.getheaders())
        finally:
            connection.close()

    def assert_stopped(self, record):
        info = host.process_stat(record['pid'])
        self.assertTrue(info is None or info['state'] in ('Z', 'X'))

    def test_publication_replacement_and_shutdown_preserve_local_contract(self):
        state = self.start()
        status, body, headers = self.fetch(state)
        self.assertEqual((status, body), (200, self.file.read_bytes()))
        self.assertIn('no-store', headers['Cache-Control'])
        self.assertIn("default-src 'none'", headers['Content-Security-Policy'])
        self.assertEqual(self.directory.stat().st_mode & 0o777, 0o700)
        self.assertEqual((self.directory / 'preview.html').stat().st_mode & 0o777, 0o600)
        self.assertEqual(self.fetch(state, 'HEAD')[:2], (200, b''))
        self.assertEqual(self.fetch(state, target='/unrelated')[0], 404)
        self.assertEqual(self.fetch(state, method='POST')[0], 405)
        self.file.write_bytes(b'<!doctype html><title>second</title><p>approved second</p>')
        updated = host.replace(self.args())
        self.assertEqual(updated['server'], state['server'])
        self.assertEqual(updated['port'], state['port'])
        self.assertEqual(self.fetch(updated, target='/review.html?v=2')[:2],
                         (200, self.file.read_bytes()))
        self.assertEqual(host.down(self.args()), {'stopped': True})
        self.assert_stopped(state['server'])
        with self.assertRaises(OSError):
            self.fetch(state)

    def test_tampered_bytes_stay_rejected_during_replacement(self):
        state = self.start()
        (self.directory / 'preview.html').write_bytes(b'<p>unapproved</p>')
        self.assertEqual(self.fetch(state)[0], 503)
        self.file.write_bytes(b'<p>approved replacement</p>')
        atomic = host.atomic
        intermediate = []

        def observe_before_swap(path, body):
            if path.name == 'preview.html':
                intermediate.append(self.fetch(state)[0])
            return atomic(path, body)

        with patch.object(host, 'atomic', side_effect=observe_before_swap):
            host.replace(self.args())
        self.assertEqual(intermediate, [503])
        self.assertEqual(self.fetch(state)[:2], (200, self.file.read_bytes()))
        self.assertEqual(host.load(self.directory / 'allowed.json')['sha256'],
                         [host.digest(self.file.read_bytes())])

    def test_exited_tunnel_startup_stops_and_reaps_server(self):
        with self.assertRaises(RuntimeError):
            host.up(self.args(local_only=False, cloudflared='/usr/bin/false'))
        state = host.load(self.directory / 'state.json')
        self.assertTrue(state['startupFailed'])
        self.assertTrue(state['cleanupComplete'])
        for key in ('server', 'tunnel'):
            if key in state:
                self.assertIsNone(host.process_stat(state[key]['pid']))

    def test_interrupted_startup_stops_and_reaps_server(self):
        verify = host.verify_local

        def interrupt_after_verification(state):
            verify(state)
            raise KeyboardInterrupt

        with patch.object(host, 'verify_local', side_effect=interrupt_after_verification):
            with self.assertRaises(KeyboardInterrupt):
                host.up(self.args())
        state = host.load(self.directory / 'state.json')
        self.assertTrue(state['cleanupComplete'])
        self.assertIsNone(host.process_stat(state['server']['pid']))

    def test_initial_state_save_failure_still_stops_server(self):
        save = host.save
        injected = False

        def fail_first_state_save(path, state):
            nonlocal injected
            if path.name == 'state.json' and not injected:
                injected = True
                raise OSError('simulated state-save failure')
            return save(path, state)

        with patch.object(host, 'save', side_effect=fail_first_state_save):
            with self.assertRaisesRegex(OSError, 'simulated'):
                host.up(self.args())
        state = host.load(self.directory / 'state.json')
        self.assertTrue(state['cleanupComplete'])
        self.assertIsNone(host.process_stat(state['server']['pid']))

    def test_signal_during_spawn_cannot_lose_the_new_child(self):
        popen = subprocess.Popen
        started = []

        def interrupt_before_returning_child(*args, **kwargs):
            child = popen(*args, **kwargs)
            if not kwargs.get('start_new_session'):
                return child
            started.append(child)
            self.children.append(child)
            signal.raise_signal(signal.SIGINT)
            return child

        with patch.object(host.subprocess, 'Popen', side_effect=interrupt_before_returning_child):
            with self.assertRaises(KeyboardInterrupt):
                host.up(self.args())
        self.assertTrue(started)
        for child in started:
            self.assertIsNone(host.process_stat(child.pid))

    def test_same_command_with_different_birth_is_not_owned(self):
        argv = [sys.executable, '-c', 'import time; time.sleep(30)']
        first = subprocess.Popen(argv)
        self.children.append(first)
        record = host.record_process(first, argv)
        time.sleep(0.03)
        second = subprocess.Popen(argv)
        self.children.append(second)
        other = host.record_process(second, argv)
        self.assertNotEqual(record['startTime'], other['startTime'])
        record['pid'] = second.pid
        with self.assertRaisesRegex(RuntimeError, 'identity mismatch'):
            host.owned_pidfd(record)
        self.assertIsNone(first.poll())
        self.assertIsNone(second.poll())

    def test_mismatched_tunnel_prevents_stopping_either_process(self):
        state = self.start()
        sentinel = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)'])
        self.children.append(sentinel)
        forged = copy.deepcopy(state)
        forged['tunnel'] = dict(state['server'], pid=sentinel.pid)
        host.save(self.directory / 'state.json', forged)
        with self.assertRaisesRegex(RuntimeError, 'identity mismatch'):
            host.down(self.args())
        self.assertEqual(self.fetch(state)[0], 200)
        self.assertIsNone(sentinel.poll())

    def test_dead_tunnel_does_not_prevent_stopping_server(self):
        state = self.start()
        argv = [sys.executable, '-c', 'import time; time.sleep(0.1)']
        child = subprocess.Popen(argv)
        self.children.append(child)
        state['tunnel'] = host.record_process(child, argv)
        for _ in range(100):
            info = host.process_stat(child.pid)
            if info and info['state'] == 'Z':
                break
            time.sleep(0.01)
        else:
            self.fail('Owned test child did not exit')
        host.save(self.directory / 'state.json', state)
        self.assertEqual(host.down(self.args()), {'stopped': True})
        self.assert_stopped(state['server'])

    def test_missing_git_stops_before_process_start(self):
        empty = self.root / 'empty-path'
        empty.mkdir()
        with patch.dict(os.environ, {'PATH': str(empty)}):
            with self.assertRaisesRegex(RuntimeError, 'Git executable is required'):
                host.up(self.args())
        self.assertFalse(self.directory.exists())


if __name__ == '__main__':
    unittest.main()
