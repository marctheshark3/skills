# Public source verification

Reviewed on 2026-10-22. This curated inventory covers 19 skill packages in 7 public, non-fork repositories. It is not an exhaustive account inventory.

Pinned source and license/rights files were read through GitHub and independently matched against unauthenticated source-archive downloads. SHA-256 values identify the archive bytes observed on this date; they are integrity records, not upstream signatures. Archive contents were read without executing skills, installers, or hardware commands. Public access and package integrity do not establish behavior in a consuming agent.

## Archive observations

| Repository | Commit | Bytes | Observed archive SHA-256 |
| --- | --- | ---: | --- |
| [marctheshark3/option-flow](https://github.com/marctheshark3/option-flow) | [05dd4a3f71](https://github.com/marctheshark3/option-flow/commit/05dd4a3f71ff46a07f1c172e9aca5e1f1f8865c1) | 44830 | `e2d6c5580eae588a772f53385e9b9b8457715a88cf137d74175fd732ce678fd4` |
| [marctheshark3/reasoning-lenses](https://github.com/marctheshark3/reasoning-lenses) | [1f81db850a](https://github.com/marctheshark3/reasoning-lenses/commit/1f81db850ae5943229cb1749416fec8c26fe39fc) | 13136 | `de61812dd869bb16389dab5888e896f70ac313e715a8b1ade8779bfe4b70fb08` |
| [marctheshark3/spatial-tools](https://github.com/marctheshark3/spatial-tools) | [2b1733d23b](https://github.com/marctheshark3/spatial-tools/commit/2b1733d23b2c55fd1659a331e70ffd0234bab335) | 673170 | `2ed1e79ef83226e32b1b81b6f723ed91dcd8c6a832841bfbb7f685a0ad89ee0e` |
| [marctheshark3/system-observatory](https://github.com/marctheshark3/system-observatory) | [1e46479a87](https://github.com/marctheshark3/system-observatory/commit/1e46479a8730b78656c0c1874fa676c3eac4d53c) | 158529 | `d464bf6aec015efbea6007ba7bb3977b6b2549a1915bdfbac30da5990a78335e` |
| [marctheshark3/rage-fieldbook](https://github.com/marctheshark3/rage-fieldbook) | [779606a3f2](https://github.com/marctheshark3/rage-fieldbook/commit/779606a3f24588740078a5976d5ad985e9a644cb) | 130556 | `2ebb5f8b35def96e4ada54ac9b1f36b534076210f8bf008861f1d7e5e832345c` |
| [marctheshark3/captain-skills](https://github.com/marctheshark3/captain-skills) | [b624b57877](https://github.com/marctheshark3/captain-skills/commit/b624b57877a9652496b20842b4e3af27b0aee598) | 155143 | `233fef8dd6d5728777eb4793b435f647ab2963d6604bdccdd531a4b32c38d1b3` |
| [marctheshark3/agent-body-protocol](https://github.com/marctheshark3/agent-body-protocol) | [f30bf69f3a](https://github.com/marctheshark3/agent-body-protocol/commit/f30bf69f3af2ec2d24c3728dda308eadfdf1e597) | 24205514 | `988909edbf19bb7fee57ea25d85436526b6d6e7f93884e58ec1e75436f2e4917` |

A repository archive contains the full repository. Its digest does not identify a standalone skill-only ZIP. Preserve the applicable license, notices, and supporting files when selecting a skill. The reference-only entry below exposes no catalog download option.

## agent-body

Express coding-agent lifecycle events through restrained Autonomous Lamp body language.

Pinned package: [skills/agent-body](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/skills/agent-body/SKILL.md). Git blob: `5e38b5cabd662ef3df5040e122aede8c9a4aec7f`.

Reuse license: [MIT](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/LICENSE). The license file was matched to Git blob `52de5b3ea4421e19471b113c215f1952591ffb85`.

Runtime and tools:

- Python >=3.10
- agent-body-protocol 0.1.0 repository/runtime (agent-body CLI or PYTHONPATH=. module invocation)
- Compatible Agent Skills host
- Local Autonomous OS HAL and Lamp or simulator for physical/visual effects

Network: Real dispatch uses loopback HTTP(S) HAL only; output can be recorded without hardware/network.

Installation notes:

- Install the runtime separately; copying SKILL.md alone does not provide agent-body.
- External led-control, scene, emotion, and claude-buddy names describe separate workflow boundaries and are not bundled in this repository.
- Camera/computer control requires the source's separate consent and paired-companion conditions.
- Each source skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- The Lamp/HAL runtime is a separate integration, not supplied by installing a skill directory.

No consuming-agent or hardware behavior was tested by this catalog.

## build-scribe

Save approved sanitized troubleshooting steps following an explicitly consented Agent Body help session.

Pinned package: [skills/build-scribe](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/skills/build-scribe/SKILL.md). Git blob: `ec0bcb9fa21a3be0f84dc56257577166e6e61747`.

Reuse license: [MIT](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/LICENSE). The license file was matched to Git blob `52de5b3ea4421e19471b113c215f1952591ffb85`.

Runtime and tools:

- Agent with authorized local file-writing capability
- An approved reusable procedure from a resolved help session

Network: No fixed network or executable runtime dependency.

Installation notes:

- Instruction-only skill; use after explicit consent and approval of the procedure.
- It excludes secrets, personal identifiers, private host/IP details, raw screenshots and unapproved copied output; uncertain sanitization means no save.
- Each source skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.

No consuming-agent or hardware behavior was tested by this catalog.

## captain-order

Create a four-line, gradeable coding order before implementation.

Pinned package: [skills/captain-order](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/skills/captain-order/SKILL.md). Git blob: `cfd76a110ee0ad94b2cf5a49d893296269eaf039`.

Reuse license: [MIT](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/LICENSE). The license file was matched to Git blob `e5ef047e58312d946de6e22aa2c6dc28a5a78b59`.

Runtime and tools:

- Compatible Agent Skills host; documented for OpenCode
- Git and the target project's existing commands/tests as applicable

Network: No fixed network dependency; depends on the user's project.

Installation notes:

- The source's preferred host is OpenCode; install.sh defaults to ~/.config/opencode/skills and requires a new session.
- The source installer installs all seven skills; --copy recursively removes an existing same-name destination before copying. Inspect it and preserve existing installations.
- Each skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- Workflow intentionally separates advice, implementation, checking, cutting, and review into fresh sessions. Inherited-context subagents do not satisfy its fresh-session requirement.
- Target project ownership, an external order/check, and human acceptance requirements differ by skill.

No consuming-agent or hardware behavior was tested by this catalog.

## cut-bloat

Reduce an excessive diff through deletion within named behavior requirements.

Pinned package: [skills/cut-bloat](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/skills/cut-bloat/SKILL.md). Git blob: `a3ad90b3d184243449d4fa4f86f54a3f9ee378b2`.

Reuse license: [MIT](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/LICENSE). The license file was matched to Git blob `e5ef047e58312d946de6e22aa2c6dc28a5a78b59`.

Runtime and tools:

- Compatible Agent Skills host; documented for OpenCode
- Git and the target project's existing commands/tests as applicable

Network: No fixed network dependency; depends on the user's project.

Installation notes:

- The source's preferred host is OpenCode; install.sh defaults to ~/.config/opencode/skills and requires a new session.
- The source installer installs all seven skills; --copy recursively removes an existing same-name destination before copying. Inspect it and preserve existing installations.
- Each skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- Workflow intentionally separates advice, implementation, checking, cutting, and review into fresh sessions. Inherited-context subagents do not satisfy its fresh-session requirement.
- Target project ownership, an external order/check, and human acceptance requirements differ by skill.

No consuming-agent or hardware behavior was tested by this catalog.

## hatch

Request the Lamp's named wake-up/hop then look-at-user sequence through HAL.

Pinned package: [skills/hatch](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/skills/hatch/SKILL.md). Git blob: `e9ffd99437431c9ca56ed09da3ff4d3f827f6094`.

Reuse license: [MIT](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/LICENSE). The license file was matched to Git blob `52de5b3ea4421e19471b113c215f1952591ffb85`.

Runtime and tools:

- Python >=3.10
- agent-body-protocol 0.1.0 repository/runtime (agent-body CLI or PYTHONPATH=. module invocation)
- Repository mapper module on PYTHONPATH or installed package
- Autonomous OS HAL and Lamp or simulator for movement

Network: The documented live effect uses loopback HAL HTTP; omitted --hal produces markers without live movement.

Installation notes:

- Command examples use PYTHONPATH=. from the repository; skill folder alone does not supply mapper.
- Simulation is explicit; Qi mode refuses hatch. Raw joint control is outside this skill.
- Each source skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- The Lamp/HAL runtime is a separate integration, not supplied by installing a skill directory.

No consuming-agent or hardware behavior was tested by this catalog.

## look-follow-dance

Request named look, follow, dance, hatch, or stop Lamp behaviors through HAL.

Pinned package: [skills/look-follow-dance](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/skills/look-follow-dance/SKILL.md). Git blob: `0e9aee98c91387bf96bb965352ef43572dfb2db4`.

Reuse license: [MIT](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/LICENSE). The license file was matched to Git blob `52de5b3ea4421e19471b113c215f1952591ffb85`.

Runtime and tools:

- Python >=3.10
- agent-body-protocol 0.1.0 repository/runtime (agent-body CLI or PYTHONPATH=. module invocation)
- Repository mapper module on PYTHONPATH or installed package
- Autonomous OS HAL and Lamp or simulator
- Working camera/person tracking for follow

Network: The documented live effect uses loopback HAL HTTP.

Installation notes:

- Command examples use PYTHONPATH=. from the repository; skill folder alone does not supply mapper.
- Source warns follow needs a camera and can fail in the official simulator.
- This provides named behaviors; it does not expose raw joint control.
- Each source skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- The Lamp/HAL runtime is a separate integration, not supplied by installing a skill directory.

No consuming-agent or hardware behavior was tested by this catalog.

## make-grade

Implement an existing coding order within its explicit checks and change budget.

Pinned package: [skills/make-grade](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/skills/make-grade/SKILL.md). Git blob: `304d94347ac30b563af4bd0f8e4db43bcab26ebb`.

Reuse license: [MIT](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/LICENSE). The license file was matched to Git blob `e5ef047e58312d946de6e22aa2c6dc28a5a78b59`.

Runtime and tools:

- Compatible Agent Skills host; documented for OpenCode
- Git and the target project's existing commands/tests as applicable

Network: No fixed network dependency; depends on the user's project.

Installation notes:

- The source's preferred host is OpenCode; install.sh defaults to ~/.config/opencode/skills and requires a new session.
- The source installer installs all seven skills; --copy recursively removes an existing same-name destination before copying. Inspect it and preserve existing installations.
- Each skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- Workflow intentionally separates advice, implementation, checking, cutting, and review into fresh sessions. Inherited-context subagents do not satisfy its fresh-session requirement.
- Target project ownership, an external order/check, and human acceptance requirements differ by skill.

No consuming-agent or hardware behavior was tested by this catalog.

## make-pass

Make one existing failing behavior check pass with a narrowly scoped change.

Pinned package: [skills/make-pass](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/skills/make-pass/SKILL.md). Git blob: `1f7a1858202557759cfcfbb5ce101a2202bad76e`.

Reuse license: [MIT](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/LICENSE). The license file was matched to Git blob `e5ef047e58312d946de6e22aa2c6dc28a5a78b59`.

Runtime and tools:

- Compatible Agent Skills host; documented for OpenCode
- Git and the target project's existing commands/tests as applicable

Network: No fixed network dependency; depends on the user's project.

Installation notes:

- The source's preferred host is OpenCode; install.sh defaults to ~/.config/opencode/skills and requires a new session.
- The source installer installs all seven skills; --copy recursively removes an existing same-name destination before copying. Inspect it and preserve existing installations.
- Each skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- Workflow intentionally separates advice, implementation, checking, cutting, and review into fresh sessions. Inherited-context subagents do not satisfy its fresh-session requirement.
- Target project ownership, an external order/check, and human acceptance requirements differ by skill.

No consuming-agent or hardware behavior was tested by this catalog.

## miss-check

Turn one reported wrong behavior into one failing check without changing product code.

Pinned package: [skills/miss-check](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/skills/miss-check/SKILL.md). Git blob: `d2f4818477663a0ac44bf49254b7098e46355114`.

Reuse license: [MIT](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/LICENSE). The license file was matched to Git blob `e5ef047e58312d946de6e22aa2c6dc28a5a78b59`.

Runtime and tools:

- Compatible Agent Skills host; documented for OpenCode
- Git and the target project's existing commands/tests as applicable

Network: No fixed network dependency; depends on the user's project.

Installation notes:

- The source's preferred host is OpenCode; install.sh defaults to ~/.config/opencode/skills and requires a new session.
- The source installer installs all seven skills; --copy recursively removes an existing same-name destination before copying. Inspect it and preserve existing installations.
- Each skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- Workflow intentionally separates advice, implementation, checking, cutting, and review into fresh sessions. Inherited-context subagents do not satisfy its fresh-session requirement.
- Target project ownership, an external order/check, and human acceptance requirements differ by skill.

No consuming-agent or hardware behavior was tested by this catalog.

## miss-hunt

Find three behavioral misses and encode failing checks in a fresh session without fixes.

Pinned package: [skills/miss-hunt](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/skills/miss-hunt/SKILL.md). Git blob: `cd6b404b20d9bf392892176a8f49ed68a7464a64`.

Reuse license: [MIT](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/LICENSE). The license file was matched to Git blob `e5ef047e58312d946de6e22aa2c6dc28a5a78b59`.

Runtime and tools:

- Compatible Agent Skills host; documented for OpenCode
- Git and the target project's existing commands/tests as applicable

Network: No fixed network dependency; depends on the user's project.

Installation notes:

- The source's preferred host is OpenCode; install.sh defaults to ~/.config/opencode/skills and requires a new session.
- The source installer installs all seven skills; --copy recursively removes an existing same-name destination before copying. Inspect it and preserve existing installations.
- Each skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- Workflow intentionally separates advice, implementation, checking, cutting, and review into fresh sessions. Inherited-context subagents do not satisfy its fresh-session requirement.
- Target project ownership, an external order/check, and human acceptance requirements differ by skill.

No consuming-agent or hardware behavior was tested by this catalog.

## motion-aim

Aim the Lamp toward a named HAL direction without raw joint control.

Pinned package: [skills/motion-aim](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/skills/motion-aim/SKILL.md). Git blob: `8fc65062e50f16cca55686ab44e30fc5ac22b2ba`.

Reuse license: [MIT](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/LICENSE). The license file was matched to Git blob `52de5b3ea4421e19471b113c215f1952591ffb85`.

Runtime and tools:

- Python >=3.10
- agent-body-protocol 0.1.0 repository/runtime (agent-body CLI or PYTHONPATH=. module invocation)
- agent-body CLI
- A marker consumer or local HAL for live aim

Network: The shown --record example requires no network; real aim dispatch uses loopback HAL HTTP.

Installation notes:

- Install the runtime separately; copying SKILL.md alone does not provide agent-body.
- The shown --record command records requested markers and does not establish that a physical Lamp moved.
- Learned aim is a reserved optional slot; no weights/training are supplied or required.
- Each source skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- The Lamp/HAL runtime is a separate integration, not supplied by installing a skill directory.

No consuming-agent or hardware behavior was tested by this catalog.

## navigator

Advise on the next bounded coding workflow and provide a fresh-session handoff.

Pinned package: [skills/navigator](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/skills/navigator/SKILL.md). Git blob: `2a43137b33d88d884c776e9e32187440e1c3344c`.

Reuse license: [MIT](https://github.com/marctheshark3/captain-skills/blob/b624b57877a9652496b20842b4e3af27b0aee598/LICENSE). The license file was matched to Git blob `e5ef047e58312d946de6e22aa2c6dc28a5a78b59`.

Runtime and tools:

- Compatible Agent Skills host; documented for OpenCode
- Git and the target project's existing commands/tests as applicable

Network: No fixed network dependency; depends on the user's project.

Installation notes:

- The source's preferred host is OpenCode; install.sh defaults to ~/.config/opencode/skills and requires a new session.
- The source installer installs all seven skills; --copy recursively removes an existing same-name destination before copying. Inspect it and preserve existing installations.
- Each skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- Workflow intentionally separates advice, implementation, checking, cutting, and review into fresh sessions. Inherited-context subagents do not satisfy its fresh-session requirement.
- Target project ownership, an external order/check, and human acceptance requirements differ by skill.

No consuming-agent or hardware behavior was tested by this catalog.

## option-flow

Find and resolve bottlenecks in code, tools, and development feedback.

Pinned package: [skills/option-flow](https://github.com/marctheshark3/option-flow/blob/05dd4a3f71ff46a07f1c172e9aca5e1f1f8865c1/skills/option-flow/SKILL.md). Git blob: `0ec657cd7b91fac5cf44e977fb5c15aff8de6046`.

Reuse license: [MIT](https://github.com/marctheshark3/option-flow/blob/05dd4a3f71ff46a07f1c172e9aca5e1f1f8865c1/skills/option-flow/LICENSE). The license file was matched to Git blob `e5ef047e58312d946de6e22aa2c6dc28a5a78b59`.

Runtime and tools:

- Agent with access to the code/workflow being investigated

Network: No fixed network or external service dependency.

Installation notes:

- Install the entire skills/option-flow directory, preserving references, agents metadata, and LICENSE.

No consuming-agent or hardware behavior was tested by this catalog.

## rage-fieldbook

Maintain and validate The Rage Fieldbook's chapters, walkthroughs, notes, and research.

Pinned package: [.agents/skills/rage-fieldbook](https://github.com/marctheshark3/rage-fieldbook/blob/779606a3f24588740078a5976d5ad985e9a644cb/.agents/skills/rage-fieldbook/SKILL.md). Git blob: `7a13643f845a6603d461dc28ed2e1273b2d498d7`.

Reference only: the pinned [rights statement](https://github.com/marctheshark3/rage-fieldbook/blob/779606a3f24588740078a5976d5ad985e9a644cb/RIGHTS.md) selects no blanket reuse license. Download/install and recreation options are unavailable in this catalog.

Runtime and tools:

- Python >=3.11 for the book build
- Markdown==3.11.1 from repository requirements.txt
- The complete Rage Fieldbook checkout
- Git
- Browser/preview for changed reader navigation

Network: Primary-source research can require network access; book reader has no remote fonts/analytics/browser dependencies.

Installation notes:

- This is a repository-specific maintenance skill, not a standalone general writing skill.
- Paths resolve against the Fieldbook checkout; scripts, book.json, public-files.txt, templates, and publication rules are required.
- No blanket reuse license is granted in RIGHTS.md. Expose only a source/reference link in the catalog; download/install and recreation adoption remain unavailable.

No consuming-agent or hardware behavior was tested by this catalog.

## reasoning-lenses

Assess proposals and decisions through faithful interpretation, challenge, and useful next tests.

Pinned package: [skills/reasoning-lenses](https://github.com/marctheshark3/reasoning-lenses/blob/1f81db850ae5943229cb1749416fec8c26fe39fc/skills/reasoning-lenses/SKILL.md). Git blob: `82fb720134bd0ac2975c0eceb31816860ae1ba35`.

Reuse license: [MIT](https://github.com/marctheshark3/reasoning-lenses/blob/1f81db850ae5943229cb1749416fec8c26fe39fc/skills/reasoning-lenses/LICENSE). The license file was matched to Git blob `74281b10bc256cc6d61803fcfb662d673daf1244`.

Runtime and tools:

- Agent capable of reading SKILL.md; source access/browsing only when the task needs verification

Network: No fixed executable or external service dependency.

Installation notes:

- Install the complete skills/reasoning-lenses directory; other hosts may require discovery configuration.

No consuming-agent or hardware behavior was tested by this catalog.

## spatial-reasoning

Check practical 2D fit, distance, overlap, clearance, and bounded routes using explicit geometry.

Pinned package: [skills/spatial-reasoning](https://github.com/marctheshark3/spatial-tools/blob/2b1733d23b2c55fd1659a331e70ffd0234bab335/skills/spatial-reasoning/SKILL.md). Git blob: `6f7c3503dc1d7c8ed393d593b93c4262531da6db`.

Reuse license: [Apache-2.0](https://github.com/marctheshark3/spatial-tools/blob/2b1733d23b2c55fd1659a331e70ffd0234bab335/skills/spatial-reasoning/LICENSE). The license file was matched to Git blob `d645695673349e3947e8e5ae42332d0ac3164cd7`.

Runtime and tools:

- Python >=3.10
- spatial-tools 0.1.0 runtime from this repository
- Shapely >=2.1.2,<3; GEOS backend
- uv for the documented locked environment setup; pip installation is also documented
- NumPy is a transitive Shapely dependency; runtime dependency notices must be reviewed separately.
- spatial-tools executable on PATH or this repository's .venv/bin/spatial-tools
- Explicit coordinates and a version-1 scene request

Network: Dependency installation may need package indexes or an approved mirror. The skill launcher does not install packages or make network calls.

Installation notes:

- The skill directory is not a self-contained geometry runtime.
- Documented installation clones the full repository, runs uv sync --locked, and symlinks the skill. A copied skill requires an installed spatial-tools command on PATH.
- Python wheel installation does not install the skill.
- Preserve LICENSE and NOTICE. Runtime dependencies retain their own licenses; THIRD_PARTY_NOTICES.md identifies Shapely BSD-3-Clause and GEOS LGPL.
- The install helper refuses existing skill destinations; reload skill discovery after installation.

No consuming-agent or hardware behavior was tested by this catalog.

## system-observatory

Explain system intent, architecture, behavior, and design through interactive evidence-backed reports.

Pinned package: [skills/system-observatory](https://github.com/marctheshark3/system-observatory/blob/1e46479a8730b78656c0c1874fa676c3eac4d53c/skills/system-observatory/SKILL.md). Git blob: `963648379391fcff51468148153f9b0bab75f84d`.

Reuse license: [MIT](https://github.com/marctheshark3/system-observatory/blob/1e46479a8730b78656c0c1874fa676c3eac4d53c/skills/system-observatory/LICENSE). The license file was matched to Git blob `7c549f1ed5e06c97d1011c40f17eae3b9dc6cb67`.

Runtime and tools:

- Python >=3.10 for packaged helpers
- Git for source snapshots and example fixtures
- Browser or HTML preview for generated standalone reports

Network: Generated reports need no server API, remote fonts, or CDN. Investigated projects can have their own setup/network requirements.

Installation notes:

- Install the full skill directory, including scripts, references, assets and LICENSE, or the source's self-contained ZIP.
- Preserve all renderer assets; SKILL.md alone is incomplete.
- Remove or disable an old codebase-observatory installation through its manager to avoid duplicate names.
- Optional development/browser tests use Playwright and Chromium; these are not runtime requirements.

No consuming-agent or hardware behavior was tested by this catalog.

## tool-flow

Audit agent tool-call histories and experiments to reduce rework and slow feedback.

Pinned package: [skills/tool-flow](https://github.com/marctheshark3/option-flow/blob/05dd4a3f71ff46a07f1c172e9aca5e1f1f8865c1/skills/tool-flow/SKILL.md). Git blob: `ea9d18d3235c1cbec5cd402f32f3ee541536df7f`.

Reuse license: [MIT](https://github.com/marctheshark3/option-flow/blob/05dd4a3f71ff46a07f1c172e9aca5e1f1f8865c1/skills/tool-flow/LICENSE). The license file was matched to Git blob `e5ef047e58312d946de6e22aa2c6dc28a5a78b59`.

Runtime and tools:

- Python >=3.10 for optional standard-library analyzer
- Explicit supported JSONL logs or T3 activity export for deterministic analysis; app thread-read tools are preferred when available

Network: Optional analyzer performs no network calls and does not replay logged commands.

Installation notes:

- Install independently from skills/tool-flow; Option Flow is optional.
- Keep analyzer and both references; output paths must be fresh.

No consuming-agent or hardware behavior was tested by this catalog.

## work-light

Emit temporary neutral work-light markers during an explicitly consented help session, then restore lighting.

Pinned package: [skills/work-light](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/skills/work-light/SKILL.md). Git blob: `333c0f4dfa7a1b77f3a9a1e23f23e1b1e8aaabaa`.

Reuse license: [MIT](https://github.com/marctheshark3/agent-body-protocol/blob/f30bf69f3af2ec2d24c3728dda308eadfdf1e597/LICENSE). The license file was matched to Git blob `52de5b3ea4421e19471b113c215f1952591ffb85`.

Runtime and tools:

- A host/companion that interprets the documented HW LED markers
- Lamp HAL or equivalent marker-dispatch integration for the actual light

Network: The skill itself emits markers; physical effects require the host's local HAL integration.

Installation notes:

- No standalone executable is included; literal HW markers need an integration that dispatches them.
- Consent to lighting does not grant screen inspection, camera, or computer-control access.
- Each source skill directory contains only SKILL.md; retain repository-root LICENSE when extracting or redistributing.
- The Lamp/HAL runtime is a separate integration, not supplied by installing a skill directory.

No consuming-agent or hardware behavior was tested by this catalog.
