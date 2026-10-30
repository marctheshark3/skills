# Review Copy Host validation

Observed on 2026-10-30 with Codex in T3 Code on Linux, Node 25.6.1 and
Python 3.14.7. An independent consuming agent explicitly loaded the package and
used isolated dummy HTML outside Git. No credentials or real review content
were supplied. This is evidence for the local workflow, with the limits below.

## Observed behavior

- `up --local-only` served the exact approved file over a loopback listener.
  Its state directory and saved HTML had modes 0700 and 0600.
- GET and a query-string GET returned the approved bytes. HEAD returned 200,
  an unrelated path returned 404, and POST returned 405.
- Responses declared HTML, disabled caching, and included a script-blocking
  content security policy.
- `replace` preserved the server PID, port and mount. Ordinary and query-string
  GETs returned only the replacement bytes.
- Changing the staged file to bytes absent from the allowlist produced 503.
- With a disposable state record pointing at an unrelated sentinel process,
  `down` rejected the command-identity mismatch and left both processes alive.
  After restoring the record, `down` stopped the owned server; the sentinel
  remained alive and the local port stopped accepting connections.

## Limits

The independent run did not start a public tunnel. It does not establish the
helper's public startup, public reachability, reviewer access,
automatic skill discovery, behavior on other models, or compatibility with
other Node, Python, cloudflared or Linux versions. The public route must be
verified with the intended reviewer in each authorized use.

Cloudflare documents Quick Tunnels as temporary development hosting, with a
different hostname after restart and no uptime guarantee. The helper keeps
the existing process running during replacement; it provides no persistent
hosting guarantee. See the [vendor documentation](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).

## Reproduce the local workflow

Create two harmless HTML inputs and choose a fresh state directory outside
Git. Using the package's `scripts/host_copy.py`, run `up --local-only`, fetch
the returned loopback port and mount, run `replace` with the second input,
fetch again, then run `down`. A public `up` is a separate operation requiring
the user's authorization and an existing cloudflared executable.

Skill Creator validation and Node syntax checking cover package structure and
syntax. They do not substitute for the behavior observations above.

## Source review and regression checks

A separate initial source review reproduced a replacement window in which
altered, previously rejected bytes became approved. It also reproduced servers
surviving failed or interrupted startup. Those cases were absent from the
earlier local workflow check.

The candidate now takes the prior hash from its approval record, retains and
reaps startup children, and defers cancellation until a new child is tracked.
Shutdown checks boot identity, start time and command line, and uses Linux
process file descriptors to bind signaling to the inspected process lifetime.
Git and Python 3.10+ are explicit prerequisites.

The standard-library regression suite exercises normal local serving and
replacement, rejection throughout a tampered-file replacement, failed tunnel
startup with an inert executable, cancellation after verification and during
spawn, initial state-save failure, different process birth with the same
command, mismatch refusal, teardown with a dead tunnel, and missing Git.
These tests use dummy HTML and loopback only; they do not validate a real
cloudflared session or simulate actual operating-system PID reuse.

Run `python3 -m unittest discover -s checks -p test_review_copy_host.py -v`
from the source repository. Independent re-review of the repaired candidate is
required before publication.

On 2026-10-30, independent re-review approved the repaired package with no
required amendments. All ten regressions passed on Python 3.10.21 and 3.14.7
with Node 25.6.1; six additional local probes passed. Those probes covered
CLI lifecycle, startup cancellation/identity-recording failure, refusal before
partial shutdown, and signaling after an owned process had exited. Public
startup, Node 22 behavior and actual operating-system PID reuse remain
unverified.
