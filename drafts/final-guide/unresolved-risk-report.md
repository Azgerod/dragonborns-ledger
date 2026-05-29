# Unresolved Risk Report

Status: TB-043 unresolved-risk report and final QA summary complete; result: Final QA complete with known unresolved route-resolution risks.
Generated: 2026-05-28.

Scope: summarizes explicit `NEEDS ROUTE RESOLUTION` objective rows already carried by `main-guide-v1.md`, the internal coverage ledger, appendices, and Phase 15 QA artifacts. This pass does not resolve gameplay facts, accept risk, or perform broad gameplay research.

## Result Summary

| Check | Result |
| --- | --- |
| Unresolved objective rows | 342 |
| High-severity rows | 110 |
| Medium-severity rows | 87 |
| Low-severity rows | 145 |
| Row-level register | data/guide-coverage/main-guide-v1-unresolved-risk-register.csv |
| Summary CSV | data/guide-coverage/main-guide-v1-unresolved-risk-summary.csv |
| Prior QA repair actions | none; prior QA artifacts contain only no-action or explicit route-resolution states |

## Severity Model

Severity is a triage priority for follow-up work, not permission to skip lower-severity rows.

| Severity | Definition |
| --- | --- |
| high | Quest, trophy, radiant, spell/power, unique-item, AE Creation quest/reward, or branch-route unresolved rows that can affect completion state, reward preservation, counter/trophy proof, or branch continuity. |
| medium | Collectible, crafting/progression, location, miscellaneous objective, relationship, or ordinary AE consumable/item-set rows that need exact route placement or policy before final closure. |
| low | Book/document source-location rows, usually large inventory/data-reconciliation work rather than route-order blockers. |

## Category Summary

| Category | Rows | Severity split | Likely owner | Dominant route surfaces |
| --- | --- | --- | --- | --- |
| ae_creation | 1 | medium: 1 | AE Creation quest and reward routing | Final Reconciliation route-resolution register (1) |
| book_document | 145 | low: 145 | Book and document source-location routing | Final Reconciliation route-resolution register (112), TB-038R delayed-task carryforward (32) |
| collectible | 26 | medium: 26 | Finite collectible and Fishing route policy | Collectible/Fishing reconciliation (26) |
| crafting_unlock | 21 | medium: 21 | Crafting, alchemy, and progression routing | TB-038R delayed-task carryforward (11), Final Reconciliation route-resolution register (8) |
| location | 3 | medium: 3 | Location route validation | Final Reconciliation route-resolution register (2), Retrospective redistributed regional sections; no player-facing Location Counter Sweep dump (1) |
| misc_objective | 34 | medium: 34 | Hold favor and miscellaneous-objective routing | TB-038R delayed-task carryforward (27), Final Reconciliation route-resolution register (7) |
| npc_relationship | 2 | medium: 2 | Relationship and household option routing | TB-038R delayed-task carryforward (2) |
| quest | 41 | high: 41 | Quest route validation and insertion | Final Reconciliation route-resolution register (26), TB-038R delayed-task carryforward (15) |
| radiant | 8 | high: 8 | Radiant and counter assignment routing | TB-038R delayed-task carryforward (4), Final Reconciliation route-resolution register (4) |
| spell_power | 8 | high: 8 | Spell, shout, and power routing | TB-038R delayed-task carryforward (8) |
| trophy | 7 | high: 7 | Trophy and counter verification | TB-038R delayed-task carryforward (5), Collectible/Fishing reconciliation (1) |
| unique_item | 46 | high: 46 | Unique item/member route routing | Final Reconciliation route-resolution register (34), TB-038R delayed-task carryforward (11) |

## Route Surface Summary

| Route or QA surface | Rows |
| --- | --- |
| Final Reconciliation route-resolution register | 195 |
| TB-038R delayed-task carryforward | 115 |
| Collectible/Fishing reconciliation | 28 |
| Crafting/alchemy/investment reconciliation | 2 |
| Retrospective redistributed regional sections; no player-facing Location Counter Sweep dump | 1 |
| Books/spells/documents reconciliation | 1 |

## Follow-Up Priority

| Priority | Rows | Recommended next action |
| --- | --- | --- |
| 1. High-severity route-resolution rows | 110 | Resolve category by category, starting with quest/trophy/radiant/unique-item rows that affect completion proof or branch/final continuity. |
| 2. Medium-severity system and finite-set rows | 87 | Resolve Fishing/collectible, crafting/alchemy, location, relationship, and hold-favor rows after high-severity routing is stable. |
| 3. Low-severity book/document rows | 145 | Run a dedicated book/document source-location reconciliation pass for deterministic pickup paths or explicit data exclusions. |

## Risk Owners

| Likely owner | Rows |
| --- | --- |
| Book and document source-location routing | 145 |
| Unique item/member route routing | 46 |
| Quest route validation and insertion | 41 |
| Hold favor and miscellaneous-objective routing | 34 |
| Finite collectible and Fishing route policy | 26 |
| Crafting, alchemy, and progression routing | 21 |
| Radiant and counter assignment routing | 8 |
| Spell, shout, and power routing | 8 |
| Trophy and counter verification | 7 |
| Location route validation | 3 |
| Relationship and household option routing | 2 |
| AE Creation item-member policy | 1 |

## Prior QA Closure

The final-risk report relies on the generated QA artifacts as current state. No broad gameplay research was performed.

| QA artifact | Rows | Recommended actions |
| --- | --- | --- |
| TB-038/TB-038R order and delayed-task QA | 3098 | none: 2624, none_existing_route_resolution: 444, none_local_save: 26, review_support_delay: 4 |
| TB-039 trophy, leveled-item, and cell-entry QA | 1191 | none: 1131, none_existing_route_resolution: 60 |
| TB-040 Survival Mode and Legendary difficulty QA | 201 | none: 200, none_existing_route_resolution: 1 |
| TB-041 branch and spoiler QA | 118 | none: 118 |
| TB-042 simulated playtest QA | 95 | none: 94, none_existing_route_resolution: 1 |

## Review Notes

The guide should not be treated as fully closed while these 342 explicit route-resolution rows remain. They are visible risk inventory, not hidden coverage gaps.

A follow-up route-resolution phase should work from the row-level register, source-check only the selected bucket, update the relevant source notes and coverage rows, then regenerate the affected audits and this report.
