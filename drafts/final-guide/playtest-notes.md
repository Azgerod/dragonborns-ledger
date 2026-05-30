# Playtest Notes

Status: TB-042 simulated playtest complete; result: Pass with explicit route-resolution rows carried forward.
Generated: 2026-05-30.

Scope: document-level simulated playtest of `drafts/final-guide/main-guide-v1.md` as a player-facing black-box itinerary. This pass checks executable section starts, numbered route steps, route-heavy section logistics cues, previous QA repair-action state, placeholder language, and visibility of known unresolved route-resolution rows.

No broad gameplay research was performed. This is not a live PS4 run; live combat, economy, random assignment, trophy-pop, and engine-state behavior still require actual play or targeted source checks if a contradiction appears.

## Result Summary

| Check | Result |
| --- | --- |
| Audit rows | 98 |
| Recommended actions | none: 97, none_existing_route_resolution: 1 |
| Section walkthrough rows | 84 |
| Section walkthrough status | pass_non_executable_handoff_section: 1, pass_section_executable: 83 |
| Route-resolution register | 166 unresolved rows remain explicit; by category: ae_creation: 1, book_document: 59, collectible: 5, crafting_unlock: 12, location: 2, misc_objective: 34, npc_relationship: 2, radiant: 7, spell_power: 8, trophy: 7, unique_item: 29 |
| Repair actions | none |

## Area Summary

| Area | Rows |
| --- | --- |
| playtest_setup | 7 |
| previous_qa_integration | 4 |
| route_resolution_visibility | 1 |
| section_walkthrough | 84 |
| simulated_playtest_limits | 2 |

## Findings

No simulated-playtest repair actions remain. Every executable route section has numbered player steps, a clear start/continuity cue, and logistics support where the section contains travel, combat, cold, dungeon, or branch language. The one no-step section is an explicit no-standalone-sweep handoff into the named reconciliation blocks below it.

Known unresolved route-resolution rows remain explicit and are not hidden player-memory debt. TB-043 should summarize those risks rather than rerunning the route coverage audits.

## Manual Playtest Boundary

A live playtest or targeted source check is still needed for any concrete contradiction found during actual play, especially cash balance, difficulty/power curve, random target behavior, trophy-pop timing, and exact quest-state behavior.

## Inputs

| Path | Use |
| --- | --- |
| drafts/final-guide/main-guide-v1.md | Primary player-facing route walked section by section. |
| drafts/final-guide/qa-checklist.md | Prior Phase 15 QA checkpoint state. |
| drafts/final-guide/appendices-v0.md | Reference appendix and unresolved-register support. |
| data/guide-coverage/main-guide-v1-objective-final-status.csv | Explicit unresolved route-resolution count and categories. |
| data/guide-coverage/main-guide-v1-playtest-audit.csv | Generated TB-042 detailed audit rows. |
| data/guide-coverage/main-guide-v1-playtest-summary.csv | Generated TB-042 summary counts. |

Regenerate with `python3 tools/audit_main_guide_playtest.py` after guide or QA-artifact changes.
