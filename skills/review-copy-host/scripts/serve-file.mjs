import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { parseArgs } from 'node:util';

const { values } = parseArgs({ options: { state: { type: 'string' }, mount: { type: 'string' } } });
const directory = path.resolve(values.state);
const mount = values.mount;
const filename = path.join(directory, 'preview.html');

function send(response, status, body, head = false) {
  response.writeHead(status, {
    'Content-Type': status === 200 ? 'text/html; charset=UTF-8' : 'text/plain; charset=UTF-8',
    'Content-Length': body.length, 'Cache-Control': 'no-store, max-age=0',
    'X-Content-Type-Options': 'nosniff',
    'Content-Security-Policy': "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'",
    'Referrer-Policy': 'no-referrer', 'Connection': 'close',
  });
  response.end(head ? undefined : body);
}
const server = http.createServer({ maxHeaderSize: 8192, requestTimeout: 5000,
  headersTimeout: 5000, keepAliveTimeout: 1000 }, (request, response) => {
  if (!['GET', 'HEAD'].includes(request.method)) {
    send(response, 405, Buffer.from('method not allowed\n')); return;
  }
  if ((request.url ?? '').split('?', 1)[0] !== mount) {
    send(response, 404, Buffer.from('not found\n'), request.method === 'HEAD'); return;
  }
  let descriptor;
  try {
    descriptor = fs.openSync(filename, fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW);
    const info = fs.fstatSync(descriptor);
    if (!info.isFile() || info.size > 1048576) throw new Error('unapproved file');
    const body = fs.readFileSync(descriptor);
    const hash = crypto.createHash('sha256').update(body).digest('hex');
    const hashes = JSON.parse(fs.readFileSync(path.join(directory, 'allowed.json'), 'utf8')).sha256;
    if (!Array.isArray(hashes) || !hashes.includes(hash)) throw new Error('unapproved bytes');
    send(response, 200, body, request.method === 'HEAD');
  } catch {
    send(response, 503, Buffer.from('approved preview unavailable\n'), request.method === 'HEAD');
  } finally { if (descriptor !== undefined) fs.closeSync(descriptor); }
});
server.maxConnections = 32;
server.maxRequestsPerSocket = 1;
server.on('clientError', (_error, socket) => socket.end('HTTP/1.1 400 Bad Request\r\nConnection: close\r\n\r\n'));
server.listen(0, '127.0.0.1', () => {
  fs.writeFileSync(path.join(directory, 'listener.json'), JSON.stringify({
    pid: process.pid, port: server.address().port, host: '127.0.0.1',
  }) + '\n', { mode: 0o600 });
});
process.on('SIGTERM', () => server.close(() => process.exit(0)));
