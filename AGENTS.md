# Maintaining the public catalog

This repository catalogs public agent skills and keeps experimental original
work separate from verified upstream packages. Preserve canonical sources,
pinned commits, applicable licenses, dependencies, and observed evidence.
Public visibility alone does not establish a reuse license or adoption readiness.

Keep catalog entries, documentation, examples, and skill packages portable and
free of private infrastructure and installation policy. Never copy another
repository's content or apply this repository's license to linked material.

Run `python3 checks/validate_catalog.py` after catalog changes. Check original
skill packages with the available Skill Creator validator. Describe behavior
as tested only when an actual consuming agent has exercised it; structural
checks and the author's manual exercises do not establish automatic discovery,
delegation behavior, or cross-model compatibility.

Publish substantive changes through a pull request with independent review.
Review the initial source before its first publication. Keep raw agent
transcripts and temporary audit downloads outside this repository.
