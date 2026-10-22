---
name: task-coordination
description: Coordinate tasks with independently useful work packages or a consequential independent review, selecting relevant available skills and delegating bounded work when permitted. Use without requiring the user to request subagents; skip trivial edits and tightly coupled sequential work.
license: MIT
metadata:
  maturity: experimental
---

# Task coordination

Experimental draft: automatic discovery and live delegation have not yet been
independently exercised. Preserve this status when sharing the draft.

Keep one parent responsible for the requested outcome, constraints, shared
contracts, integration, verification, and final response.

## Choose a useful split

Identify the acceptance criteria, dependencies, and shared files before splitting
work. Delegate only when a concrete output can be checked independently and the
benefit exceeds the coordination cost. Independent review can qualify even when
implementation must stay serial. Handle trivial edits directly; keep coupled
changes serial until a stable contract makes a split useful.

Inspect the available skill descriptions; read the relevant instructions before
using or assigning them. Choose by task fit, not by a fixed roster. No particular
skill is required. If an optional skill is missing, use the available tools and
state any resulting limitation. If a required capability is missing, complete
unblocked work and identify the dependency.

## Request bounded delegation

This skill explicitly requests bounded delegation when the split above is useful
and the environment permits it. Where applicable skill instructions authorize
delegation, proceed without a redundant per-task permission question. A user or
higher-priority prohibition wins. This request does not expand permission to
access data, change files, spend money, publish, or use external services.

Use the environment's supported child-task mechanism. Inherit the parent's model
and settings unless the task or environment calls for another choice. Bound
active workers to available capacity and a small task-specific budget; if capacity
is unknown, start at most one child. Queue useful remaining work. Default each
child to no further delegation. Use a serial fallback when child tools are absent,
prohibited, or add no useful independence; report actual execution honestly.

Give each child:

- A concrete output and acceptance criteria, with the minimum relevant context.
- Dependencies, shared interfaces, and relevant skill instructions or accessible
  references; do not assume the child inherits the conversation.
- Exclusive file ownership, or an explicit read-only scope, plus side-effect
  limits. Never assign concurrent writes to the same files. Give shared-file
  integration to the parent or wait for the current owner to finish.
- The expected evidence: changed artifacts, checks run and their outcomes,
  assumptions, and unresolved issues. Require a clear failure report rather than
  a claim of success when blocked.

## Integrate and verify

Track actual child tasks and their status using the supported mechanism. Avoid
launching a duplicate while an earlier task may still be running. If a worker
fails, inspect its partial output, reclaim ownership only after it has stopped,
then finish locally or make one bounded retry justified by new information.
Cancel obsolete work when the outcome no longer needs it.

Check outputs against the original acceptance criteria and shared contracts.
Resolve conflicting reports by inspecting artifacts or running the smallest
decisive check; agreement or majority vote is not evidence. Integrate changes and
verify the combined result yourself. Report what was delivered, the checks
actually run, and remaining limits; never describe proposed workers as executed.
