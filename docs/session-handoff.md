# Session Handoff

Status: updated 2026-05-12.

This file exists to make a session switch cheap. It is a coordination note only; it does not add requirements beyond `docs/guide-specification.md`.

## Current Project State

Phase 1 source-list objective setup is closed. The objective database currently has 2,772 rows, and source notes currently run through `SN-000089-activity-favor-boundary-reconciliation.md`.

Phase 2 constraint-table research is ready to begin. Route construction remains blocked until the Phase 2 consistency review task, TB-021, confirms the constraint tables.

The current next task is TB-011: research AE Creation start triggers and level gates.

## Restart Checklist

At the start of the next session:

1. Read `AGENTS.md`.
2. Read `docs/guide-specification.md`.
3. Read `docs/development-plan.md`.
4. Read `docs/source-standards.md`.
5. Read `docs/decisions-log.md`.
6. Read `docs/task-board.md`.
7. Read `data/objectives/phase-2-research-inputs.md`.
8. Run `git status --short` and preserve unrelated existing changes.

## Next Task Details

Start TB-011 from the TB-011 section of `data/objectives/phase-2-research-inputs.md`.

Primary output:

* `data/constraints/ae-creation-start-triggers.md`
* new or updated source notes under `sources/source-notes/`
* any needed source inventory rows in `sources/bibliography.md`
* task-board status updates when complete

Research rules:

* Use current online sources.
* Do not rely on memory for AE Creation start triggers, level gates, conflicts, bugs, trophy behavior, cell-entry locking, or missability.
* Mark unknowns explicitly instead of guessing.
* Do not create route content.
* Do not draft the final guide.

## Validation Before Handoff

Run at least:

```bash
python3 tools/validate_all.py
git diff --check
```

If source notes or bibliography rows are added, also run the source-workflow validator directly if `tools/validate_all.py` output is not enough to identify source issues.
