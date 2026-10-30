---
name: review-copy-host
description: Publish, replace, and take down one temporary static HTML review copy on Linux using an existing cloudflared executable and a file-only localhost server. Use when the same public link must survive a file replacement; permanent hosting and full application deployment are separate tasks.
---

# Review Copy Host

Use existing Node 22+, Python 3.10+, Git and cloudflared executables on Linux with /proc and process file descriptors (pidfds). Local-only verification needs no cloudflared. Stop for a missing prerequisite unless installation is separately authorized. Read help/version output before using an unfamiliar version.

Resolve the example script paths from this skill's directory.

Before a public upload, establish the exact file, purpose, public visibility and how the owner can remove it. Reuse authorization already supplied for that scope. A later marker-removal overwrite needs its own approval when the task requires it. Keep preview bytes, state, logs and credentials outside Git. Review the HTML for secrets, active scripts and external dependencies before publishing it.

## Put one file up

Choose a fresh private state directory outside every Git repository. The helper copies the approved bytes there, starts a server bound to 127.0.0.1, and starts a separate anonymous Quick Tunnel. It never edits existing Tailscale or cloudflared configurations.

```sh
python3 scripts/host_copy.py up --file /absolute/review.html --state-dir /absolute/private-state --mount /review.html --cloudflared /absolute/cloudflared --node /absolute/node
```

The reply contains the generated HTTPS URL. Keep that process running through review: a restart creates a different hostname. This is temporary hosting without an uptime guarantee.

Verify the public response has status 200, text/html and the same SHA-256 as the approved file. Confirm unrelated paths return 404. The helper serves only a fixed hash-approved file, disables caching, and blocks scripts. A successful local fetch does not prove that the intended reviewer can open the URL; check with that reviewer before treating submission as accepted.

For local verification without a public tunnel, add `--local-only`.

## Replace at the same link

Prepare the replacement first and check the intended difference. When removing a marker, verify that it occurs zero times and the remaining page is unchanged. Obtain the required overwrite approval, then:

```sh
python3 scripts/host_copy.py replace --file /absolute/replacement.html --state-dir /absolute/private-state
```

This preserves the server and tunnel and atomically replaces the same local pathname. Verify the ordinary and cache-busted public URL after replacement. Do not commit preview bytes or create public version copies.

## Inspect or remove

```sh
python3 scripts/host_copy.py status --state-dir /absolute/private-state
python3 scripts/host_copy.py down --state-dir /absolute/private-state
```

Down verifies the boot, process start time and command line before stopping only the processes it created; pidfds keep signaling bound to that process lifetime. A live mismatched or reused PID is a stopping condition; do not use broad pkill commands or reset unrelated service configurations. Exited processes do not block stopping the remaining owned processes. Preserve evidence until the task permits cleanup.

See [Cloudflare's Quick Tunnel documentation](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/) for current limitations.
