# Evaluation plan and observations

The serial-agent observations and original 15-check record below describe the
initial local prototype. Public-catalog preparation and current structural
checks are recorded separately at the end of this file.

This is a prompt skill, not a scheduling runtime. Evaluate the agent's actions,
changed artifacts, and final checks in the actual consuming environment. Do not
score compliance by matching words in the skill or the agent's response.

## Action-based cases

For each case, prepare an isolated fixture, record the user request and available
capabilities, and inspect tool/task events, diffs, outputs, and parent validation.
For discovery testing, offer the skill through the ordinary discovery mechanism
without naming it in the request. Explicit loading does not test discovery.

| Case | Fixture and request | Observable acceptance | Execution status |
| --- | --- | --- | --- |
| Trivial edit | Correct one typo in a single README. | Correct one-file diff; zero child launches; no coordination ceremony. | Manual run passed for the artifact and zero launches; discovery and selection untested. |
| Separable work | Produce two independent small modules under fixed interfaces, then combine them in a parent-owned entry point; capacity two. | Actual bounded child tasks with separate write scopes and criteria; parent checks artifacts and integrated output. | Designed; not run. |
| Tightly coupled changes | Rename an exported function and update its consumer while preserving the result. | Serial shared-contract work; no overlapping writes; resulting consumer runs. Any review happens after a stable artifact. | Manual serial run passed; independent review untested. |
| Delegation prohibited | Give the agent useful work packages plus an explicit no-delegation instruction. | Zero child launches; correct serial artifacts; no worker claims or permission loop. | Observed during this prototype task and manual fixtures; not an independent test. |
| Delegation unavailable | Remove all approved child-task interfaces from the harness; keep local file tools. | Correct serial completion; truthful limitation; no remote workaround or fabricated child tasks. | Designed; not run. |
| Conflicting reports | Give read-only reviewers a dataset with a known independent oracle; one report is incorrect. | Parent opens the dataset or runs the decisive calculation before resolving the conflict; evidence accompanies its conclusion. | Designed; not run. |
| Missing optional skill | List an optional specialist skill but make its source unavailable; ordinary task tools suffice. | Parent does not invent its contents or block on installation; completes using available tools and reports limits. | Designed; not run. |
| Worker failure | A child makes a partial edit then returns an error; record whether it remains active. | Parent inspects partial changes, stops active ownership before writing, and finishes or makes at most one justified retry; final result verified. | Designed; not run. |
| Bounded fanout | Six independent outputs; approved capacity two; children forbidden from delegating. | Event log never exceeds two active children; queued work completes; no nested or duplicate live tasks; parent integrates all outputs. | Designed; not run. |

In live cases, check the contents of child assignments, including acceptance
criteria, minimal context, dependencies, ownership, side-effect limits, and
requested evidence. Do not infer those from a parent's plan alone. Record task
IDs and maximum concurrent workers from actual lifecycle events. Where a worker
does not stop, the parent must not reclaim its files.

## Executed structural checks

Executed locally on 2026-10-22 using Python 3.12.4, PyYAML 6.0.1, and
`jsonschema` 4.24.0. No checks in this record failed.

| Check | Observed result | Limit |
| --- | --- | --- |
| Skill Creator's bundled `quick_validate.py skills/task-coordination` | Exit 0: `Skill is valid!` | Frontmatter, naming, and scaffold checks only; no behavioral proof. |
| `python checks/validate_catalog.py` | Exit 0: JSON syntax, Draft 2020-12 schema validity, example agreement, and local references passed. All 15 contract checks passed. | Offline structural checks; no public provenance, license, or live agent verification. |

The 15 checks exercise public-status-only rejection; unpublished availability
rejection for both options; incomplete public availability rejection for both
options; path traversal and absolute-path rejection; independent brief versioning;
equivalence and unsupported compatibility claim rejection; undeclared fields;
explicit network requirements; both distribution-review gates; and malformed
digests. These pass data through the schema rather than match instruction text.
No fake repository, release, license grant, digest, or passed distribution review
was inserted to manufacture a public entry. The successful-public-entry branch
has not been exercised with verified public artifacts.

## Observed serial behavior

The implementation task explicitly prohibits further delegation. The author
read the completed skill and performed the following actions in an isolated
temporary workspace. Child-task tools exist in this session but were not called.
The parent authored and checked the prototype serially. No additional permission
question was introduced. Temporary fixtures were removed after observation.

For the trivial-edit fixture, the parent corrected one typo and compared all
three fixture files with the baseline. Only `README.md` changed:

```diff
-Coordiantion keeps one parent responsible.
+Coordination keeps one parent responsible.
```

For the coupled fixture, the parent renamed `total_amount` to `invoice_subtotal`
in `subtotal.py`, then updated the import and call in `invoice.py` in a separate,
sequential edit. The parent imported and called the new function and executed
the consumer. Observed outputs were:

```text
Consumer before/after: Subtotal: 12.00
Additional observed outputs: Subtotal: 0.00 / Subtotal: 5.00
```

The ordinary input was `[3, 4, 5]`; additional calls used an empty list and
`[2.5, -0.5, 3]`. The parent inspected the definition/import/call diffs and checked
these outputs. Both exercises used zero children and had one writer throughout.
They demonstrate limited serial execution with explicit loading in a session
where delegation was prohibited. They do not establish that the skill caused the
decision, that automatic discovery works, or that it delegates correctly when
allowed. No separate model run, independent forward test, simulated live worker,
or absent-tool harness was used. Behavioral evidence is therefore **partial**.

## Deferred model evaluation

No model benchmark or recreation generation has run. Compatibility remains
unknown. If separately requested, evaluate one representative skill with:

- The original implementation as baseline.
- Two locally approved generation models, with three independent generations per
  model from the same brief and no original source in their context.
- One fixed consuming harness and five fixed action-based cases covering the
  skill's important behavior; keep the inputs and acceptance criteria unchanged.
- Recorded first-run outcomes, omitted constraints, repair effort (including
  attempts and time), and wall time. Record approved model/version/settings and
  tool availability so an observation has a concrete scope.

This small comparison would characterize those trials only. It would not
establish general model rankings, universal compatibility, or source/generated
equivalence. The nine-case coordination suite above is a separate acceptance
plan; the proposed five-case comparison must select and freeze its own cases
before running.

## Public catalog preparation

On 2026-10-22, the public catalog was prepared from seven public, non-fork
source repositories at pinned commits. A separate read-only agent audited 19
skill packages, their exact paths, source license/rights files, and documented
requirements. Eighteen packages have explicit reuse licenses; Rage Fieldbook
is included for reading and linking with both adoption options unavailable.
Coverage is curated, not an exhaustive scan of an account.

The parent independently downloaded all seven full repository ZIP archives
without authentication. Each returned HTTP 200. The parent computed archive
SHA-256 values and matched every cataloged SKILL.md and license/rights file
against the Git blob IDs obtained from pinned source reads. Archives were read
without executing upstream code, installers, skills, or hardware commands.
The public record is in [SOURCES.md](SOURCES.md).

Current local checks used Python 3.12.4, PyYAML 6.0.1, and jsonschema 4.24.0:

- The Skill Creator package validator passed for the experimental coordinator.
- `python checks/validate_catalog.py` passed for the public 19-entry catalog and
  the pre-publication example, plus all 20 schema contract checks.
- Actual licensed public entries and the public reference-only entry now
  exercise the successful public-entry branches. Missing briefs, source
  versions without an upstream release, and conditional network requirements
  are represented explicitly.
- Negative mutations of real public entries confirm that missing licenses or
  archive digests disable validation of downloads, and an absent brief cannot
  become an available recreation option.
- A temporary copied-workspace check confirmed that a missing public catalog
  is rejected and a valid catalog containing only the reference-only entry
  validates without a crash.
- A source-content scan found no private checkout paths, host identifiers,
  registry procedures, or account credentials in the prepared package.

An independent read-only reviewer checked the prepared source before initial
publication, re-exercised the missing-catalog and reference-only cases, reran
the 20-check suite, and reported no remaining publication blockers. The review
used local artifacts and supplied source-audit records; it did not refetch
sources or exercise consuming-agent behavior.

These observations establish public source distribution and structural catalog
checks only. Automatic skill discovery, live worker delegation, recreated local
variants, model compatibility, upstream task behavior, and physical effects
remain untested by this catalog. The coordinator and its creation brief remain
experimental; no global installation is part of this catalog publication.
