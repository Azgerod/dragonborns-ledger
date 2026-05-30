# Unresolved Risk Report

Status: TB-043 unresolved-risk report and final QA summary complete; result: Final QA complete with known unresolved route-resolution risks.
Generated: 2026-05-30.

Scope: summarizes explicit `NEEDS ROUTE RESOLUTION` objective rows already carried by `main-guide-v1.md`, the internal coverage ledger, appendices, and Phase 15 QA artifacts. This pass does not resolve gameplay facts, accept risk, or perform broad gameplay research.

## Result Summary

| Check | Result |
| --- | --- |
| Unresolved objective rows | 166 |
| High-severity rows | 51 |
| Medium-severity rows | 56 |
| Low-severity rows | 59 |
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
| book_document | 59 | low: 59 | Book and document source-location routing | Final Reconciliation route-resolution register (52), TB-038R delayed-task carryforward (6) |
| collectible | 5 | medium: 5 | Finite collectible and Fishing route policy | Collectible/Fishing reconciliation (5) |
| crafting_unlock | 12 | medium: 12 | Crafting, alchemy, and progression routing | Final Reconciliation route-resolution register (8), TB-038R delayed-task carryforward (4) |
| location | 2 | medium: 2 | Location route validation | Retrospective redistributed regional sections; no player-facing Location Counter Sweep dump (1), Final Reconciliation route-resolution register (1) |
| misc_objective | 34 | medium: 34 | Hold favor and miscellaneous-objective routing | TB-038R delayed-task carryforward (27), Final Reconciliation route-resolution register (7) |
| npc_relationship | 2 | medium: 2 | Relationship and household option routing | TB-038R delayed-task carryforward (2) |
| radiant | 7 | high: 7 | Radiant and counter assignment routing | Final Reconciliation route-resolution register (4), TB-038R delayed-task carryforward (3) |
| spell_power | 8 | high: 8 | Spell, shout, and power routing | TB-038R delayed-task carryforward (8) |
| trophy | 7 | high: 7 | Trophy and counter verification | TB-038R delayed-task carryforward (5), Collectible/Fishing reconciliation (1) |
| unique_item | 29 | high: 29 | Unique item/member route routing | Final Reconciliation route-resolution register (21), TB-038R delayed-task carryforward (7) |

## Route Surface Summary

| Route or QA surface | Rows |
| --- | --- |
| Final Reconciliation route-resolution register | 95 |
| TB-038R delayed-task carryforward | 62 |
| Collectible/Fishing reconciliation | 7 |
| Retrospective redistributed regional sections; no player-facing Location Counter Sweep dump | 1 |
| Books/spells/documents reconciliation | 1 |

## Follow-Up Priority

| Priority | Rows | Recommended next action |
| --- | --- | --- |
| 1. High-severity route-resolution rows | 51 | Resolve category by category, starting with quest/trophy/radiant/unique-item rows that affect completion proof or branch/final continuity. |
| 2. Medium-severity system and finite-set rows | 56 | Resolve Fishing/collectible, crafting/alchemy, location, relationship, and hold-favor rows after high-severity routing is stable. |
| 3. Low-severity book/document rows | 59 | Run a dedicated book/document source-location reconciliation pass for deterministic pickup paths or explicit data exclusions. |

## Risk Owners

| Likely owner | Rows |
| --- | --- |
| Book and document source-location routing | 59 |
| Hold favor and miscellaneous-objective routing | 34 |
| Unique item/member route routing | 29 |
| Crafting, alchemy, and progression routing | 12 |
| Spell, shout, and power routing | 8 |
| Radiant and counter assignment routing | 7 |
| Trophy and counter verification | 7 |
| Finite collectible and Fishing route policy | 5 |
| Location route validation | 2 |
| Relationship and household option routing | 2 |
| AE Creation item-member policy | 1 |

## Prior QA Closure

The final-risk report relies on the generated QA artifacts as current state. No broad gameplay research was performed.

| QA artifact | Rows | Recommended actions |
| --- | --- | --- |
| TB-038/TB-038R order and delayed-task QA | 3083 | none: 2804, none_existing_route_resolution: 251, none_local_save: 28 |
| TB-039 trophy, leveled-item, and cell-entry QA | 1191 | none: 1131, none_existing_route_resolution: 60 |
| TB-040 Survival Mode and Legendary difficulty QA | 204 | none: 203, none_existing_route_resolution: 1 |
| TB-041 branch and spoiler QA | 119 | none: 119 |
| TB-042 simulated playtest QA | 98 | none: 97, none_existing_route_resolution: 1 |

## Review Notes

The guide should not be treated as fully closed while these 166 explicit route-resolution rows remain. They are visible risk inventory, not hidden coverage gaps.

A follow-up route-resolution phase should work from the row-level register, source-check only the selected bucket, update the relevant source notes and coverage rows, then regenerate the affected audits and this report.
