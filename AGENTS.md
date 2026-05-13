# AGENTS.md

## Project

This repository contains the specification and development materials for a Skyrim Anniversary Edition PS4 Legendary "true 100%" route.

The goal is not a normal hand-holding walkthrough. The final guide should be a linear black-box itinerary: go here, do this quest/objective, collect this checklist item, stop here, return later, hard save here, etc.

## Canonical Documents

Read `docs/guide-specification.md` before doing any task. It is the canonical project specification unless a task explicitly says otherwise.

Use the other project documents as supporting documents:

* `docs/development-plan.md` contains the extracted development plan.
* `docs/source-standards.md` records the sourcing rules for gameplay research.
* `docs/decisions-log.md` records resolved user decisions and should stay consistent with the specification.
* `docs/task-board.md`, if present, tracks current coordination notes and next work.
* `docs/session-handoff.md`, if present, records the current restart point for a new session.

## Session Restart Workflow

At the start of a new session, read:

1. `AGENTS.md`;
2. `docs/guide-specification.md`;
3. `docs/development-plan.md`;
4. `docs/source-standards.md`;
5. `docs/decisions-log.md`;
6. `docs/task-board.md`;
7. `docs/session-handoff.md`, if present.

Then run `git status --short` before editing. This repository may contain many uncommitted files from the current staged buildout; do not revert or clean them unless the user explicitly asks.

Use the `docs/task-board.md` Current Next Step as the default continuation point unless the user gives a newer instruction. If a handoff document and the task board disagree, inspect both and update the stale document before proceeding.

## Task Prompt Handling

The user may provide prompts beginning with "Task:" that were generated outside this repo. Treat those prompts as guiding briefs, not rigid scripts.

When a task prompt fits the current state and project documents, follow it. When it is stale, redundant, underspecified, or points in a direction that would weaken the project structure, do the better repo-aware version instead and briefly note the adjustment. Do not add requirements beyond the specification unless the user explicitly decides them.

After completing a staged task, update `docs/task-board.md` when the status or next unblocked task changes.

## Source Standards

For gameplay research, follow `docs/source-standards.md`.

Every factual gameplay claim that affects routing must include a citation in the relevant source notes. Do not research gameplay for infrastructure-only tasks.

Do not rely on memory for:

- AE Creation start triggers.
- leveled item thresholds.
- quest conflicts.
- PS4 trophy behavior.
- bug risks.
- cell-entry locking.
- missable rewards.

## Output style

Prefer structured Markdown tables and concise notes.

Do not write the final guide prematurely. Build the guide in layers:

1. objective database;
2. constraint tables;
3. route skeleton;
4. survival-mode geography pass;
5. flexible objective insertion;
6. skill/perk/grind plan;
7. branch routes;
8. checklist synchronization;
9. warning layer;
10. final black-box guide.

## Main Guide Expansion Standard

`drafts/final-guide/main-guide-v0.md` is a scaffold, not an acceptable final main-guide draft. Before treating TB-035 as complete, expand it into a self-contained `drafts/final-guide/main-guide-v1.md`.

The v1 guide must explicitly represent every row in `data/objectives/objectives.csv` and every checklist-relevant row already mapped in `data/checklist-mapping/coverage-matrix.csv`. A reader must not need to consult the objective spreadsheet, route-planning CSVs, support tables, source notes, or an external appendix to know what objective to do, where to do it, when to stop, what to collect, what to save/reload, or what checklist row to mark.

Do not use broad category placeholders as guide instructions. Phrases such as "route local objectives," "collect local books," "finish remaining checklist," "as needed," "selected sources," "support rows," "route locations," "spell sources," and similar shorthand must be replaced with explicit objective-level instructions or be immediately followed by the full list of objective names and actions covered.

At minimum, break the v1 work into one implementation pass per `MR-###` section, and split any large MR section further by quest chain, location corridor, support table, or checklist category when needed. Follow `docs/main-guide-v1-expansion-plan.md` as the active work breakdown. Do not move on to TB-036 appendices/reference tables until the v1 self-contained guide expansion is complete or the user explicitly re-scopes the sequence.

If existing project data is insufficient to route a row, write a specific `NEEDS ROUTE RESOLUTION:` note in the guide with the objective/checklist ID, objective name, exact missing fact, and inputs already checked. Do not hide unresolved rows under category language.

## Completion policy

The high-level user-resolved scope is summarized below. If this summary and `docs/guide-specification.md` diverge, update the summary to match the specification rather than creating a second rule set.

- Survival Mode on.
- Legendary difficulty.
- PS4 trophies preserved.
- Base game, official DLC, and official AE Creation Club bundle only.
- All perks required.
- Civil War main route: Imperial.
- Dawnguard main route: Dawnguard.
- Dark Brotherhood main route: join.
- Paarthurnax main route: preserve him.
- Books: skill books, spell tomes, Black Books, quest/AE books, and checklist-tracked unique books only.
- Radiants: required radiants plus one representative completion of each meaningful radiant type.
- Unique items should be preserved; do not disenchant unique items merely to learn enchantments.
- Preserve a gradually increasing difficulty curve rather than rushing overpowered gear.

## Branch policy

Fully route only branches with substantial alternate content, rewards, trophies, faction experiences, or completionist significance.

At a branch point:

1. create a named hard save;
2. play the alternate branch first;
3. include only branch-exclusive content;
4. reload the hard save;
5. continue the canonical main route.

Do not branch isolated preference choices. For spouse, children, stewards, house decoration, and similar choices, list options and recommend a default.

## Done means

For any deliverable:

- The file is internally consistent.
- Gameplay factual claims are cited.
- Uncertainties are marked.
- Assumptions are explicit.
- The output does not prematurely overfit the final route.
- The deliverable is small enough to review.
