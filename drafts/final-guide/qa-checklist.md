# QA Checklist

Status: Phase 15 coverage, order/delayed-task, constraint, branch/spoiler, simulated-playtest, and final-risk QA checkpoint complete; result: Fail.
Generated: 2026-05-28.

Scope: coverage accounting, TB-038 order/delayed-task closeout, TB-039 trophy/leveled/cell-entry constraint QA, TB-040 Survival Mode/Legendary difficulty QA, TB-041 branch/spoiler QA, TB-042 simulated playtest QA, and TB-043 unresolved-risk summary. This pass checks whether objective rows, checklist rows, delayed tasks, trophy dependencies, leveled reward gates, cell-entry risks, Survival logistics, Legendary progression constraints, branch-save/reload handling, spoiler discipline, section execution, route handoffs, and known route-resolution risks are represented by current guide prose, branch handling, option/default handling, explicit exclusions, reference appendix support, or explicit unresolved route-resolution state.

No broad gameplay research was performed. TB-040 uses the existing Survival, progression, geography, guide, and coverage artifacts. TB-041 uses the branch decision matrix, branch audit, current guide prose, and coverage artifacts. TB-042 is a document-level simulated playtest, not a live PS4 run. TB-043 summarizes explicit unresolved risks without resolving or accepting them.

## Result Summary

| Check | Status | Evidence |
| --- | --- | --- |
| Objective final accounting | Pass | 2789 objective rows classified; status total 2789; expected total 2789. |
| Checklist row accounting | Pass | 3697 coverage-matrix rows and 3697 checklist-audit rows; recommended_action: none: 3697. |
| Focused COV audit artifacts | Pass | All generated audits use only allowed no-action states. |
| Appendix unresolved register | Pass | 342 Appendix I unresolved rows; expected 342. |
| Appendix headings | Pass | All expected Appendix A through I headings appear once. |
| Placeholder phrase scan | Pass | 0 banned placeholder hits in main-guide-v1.md. |
| Coverage ledger COV summaries | Pass | 19 COV summary rows found in main-guide-v1-coverage.csv. |
| TB-039 trophy/leveled/cell QA | Pass with explicit route-resolution rows | 1191 audit rows; recommended_action: none: 1131, none_existing_route_resolution: 60. |
| TB-040 Survival/Legendary QA | Pass with explicit route-resolution rows | 201 audit rows; recommended_action: none: 200, none_existing_route_resolution: 1. |
| TB-041 branch/spoiler QA | Pass | 118 audit rows; recommended_action: none: 118. |
| TB-042 simulated playtest QA | Pass with explicit route-resolution rows | 95 audit rows; recommended_action: none: 94, none_existing_route_resolution: 1. |
| TB-043 unresolved-risk report | Pass with known unresolved risks | 342 risk-register rows; severity: high: 110, medium: 87, low: 145. |

## Objective Final Status

| Final status | Count | QA note |
| --- | --- | --- |
| placed_in_main_guide | 2374 | Non-branch, non-option, non-excluded, non-unresolved objective rows represented in the self-contained guide or promoted guide reference surfaces. |
| branch_handled | 43 | Canonical branch_route objective rows handled by branch-first/reload guide blocks after unresolved rows are counted separately. |
| option_default_handled | 11 | Canonical option_list objective rows represented by route defaults and option/default guide surfaces. |
| excluded | 19 | Objective rows with canonical excluded placement or explicit guide/coverage exclusion after unresolved rows are counted separately. |
| unresolved | 342 | Objective rows with explicit NEEDS ROUTE RESOLUTION coverage, including unresolved branch or appendix rows. |
| total_classified_objective_rows | 2789 | Matches objective_rows_processed. |

## Checklist Audit Status

| Audit status | Count |
| --- | --- |
| covered_by_internal_checklist_coverage | 2223 |
| covered_by_mapped_objective_internal_coverage | 1474 |

## Focused Audit Artifacts

| Audit | Rows | Summary rows | Recommended actions | QA result |
| --- | --- | --- | --- | --- |
| Objective ID audit | 2789 | 2789 | none: 2789 | Pass |
| Checklist ID audit | 3697 | 3697 | none: 3697 | Pass |
| Branch audit | 76 | 76 | none: 76 | Pass |
| Option/default audit | 75 | 75 | none: 75 | Pass |
| Explicit exclusion audit | 322 | 322 | none: 322 | Pass |
| Appendix/reference audit | 107 | 107 | none: 107 | Pass |
| Location audit | 919 | 919 | none: 913, none_existing_route_resolution: 6 | Pass with explicit route-resolution rows |
| Book/document audit | 1780 | 1780 | none: 1567, none_existing_route_resolution: 213 | Pass with explicit route-resolution rows |
| Collectible audit | 249 | 249 | none: 222, none_existing_route_resolution: 27 | Pass with explicit route-resolution rows |
| Crafting/progression audit | 1498 | 1498 | none: 1399, none_existing_route_resolution: 99 | Pass with explicit route-resolution rows |
| Radiant/counter audit | 234 | 234 | none: 181, none_existing_route_resolution: 53 | Pass with explicit route-resolution rows |

## Unresolved Route-Resolution Register

The 342 unresolved objective rows are explicit `NEEDS ROUTE RESOLUTION` states, not hidden coverage gaps. The full row list is in Appendix I of `drafts/final-guide/appendices-v0.md` and in `data/guide-coverage/main-guide-v1-objective-final-status.csv`.

| Category | Unresolved rows |
| --- | --- |
| ae_creation | 1 |
| book_document | 145 |
| collectible | 26 |
| crafting_unlock | 21 |
| location | 3 |
| misc_objective | 34 |
| npc_relationship | 2 |
| quest | 41 |
| radiant | 8 |
| spell_power | 8 |
| trophy | 7 |
| unique_item | 46 |

## Appendix Checks

| Appendix heading | Count |
| --- | --- |
| ## Appendix A - Coverage Snapshot | 1 |
| ## Appendix B - Guide Section Index | 1 |
| ## Appendix C - Named Hard-Save Reference | 1 |
| ## Appendix D - Branch Reference | 1 |
| ## Appendix E - Option and Default Reference | 1 |
| ## Appendix F - Exclusion Reference | 1 |
| ## Appendix G - Previous Appendix-Only Rows | 1 |
| ## Appendix H - Objective-Level Exclusions | 1 |
| ## Appendix I - Unresolved Route-Resolution Register | 1 |

## TB-038 Order and Delayed-Task QA

Status: TB-038 order/delayed-task QA complete; TB-038R repair/classification complete; result: Fail.

No broad gameplay research was performed. TB-038R records remaining delayed-task uncertainty as explicit route-resolution state rather than hidden reader-memory debt.

| Check | Status | Evidence |
| --- | --- | --- |
| Registered hard saves | Pass with explicit route-resolution row | 61 registered saves appear in the guide; 0 known save remains tied to explicit route-resolution state. |
| Guide-local hard saves | Pass | 26 local guide saves have creation cues. |
| Branch reload cues | Pass | 8 branch markers have same-section reload cues. |
| Delayed coverage closeout | Pass with explicit route-resolution rows | 3098 audit rows; recommended_action: none: 2624, none_existing_route_resolution: 444, none_local_save: 26, review_support_delay: 4. TB-038R classified 280 findings: 217 explicit route-resolution and 63 connected to existing route/final-reference closeouts. |

## TB-039 Trophy, Leveled-Item, and Cell-Entry QA

Status: TB-039 trophy, leveled-item, and cell-entry QA complete; result: Pass with explicit route-resolution rows.

No broad gameplay research was performed. This pass audits the v1 guide against the existing `trophy-dependencies.md`, `leveled-unique-items.md`, and `cell-entry-locks.md` constraints plus current final coverage state.

| Check | Status | Evidence |
| --- | --- | --- |
| Trophy setup rules | Pass | 4 setup rows; recommended_action: none: 4. |
| Trophy dependencies | Pass with explicit route-resolution rows | 1115 constraint rows; recommended_action: none: 1056, none_existing_route_resolution: 59. |
| Leveled rewards | Pass | 24 constraint rows; recommended_action: none: 24. |
| Cell-entry and related locks | Pass with explicit route-resolution row | 48 constraint rows; recommended_action: none: 47, none_existing_route_resolution: 1. |

## TB-040 Survival Mode and Legendary Difficulty QA

Status: TB-040 Survival Mode and Legendary difficulty QA complete; result: Pass with explicit route-resolution rows.

No broad gameplay research was performed. This pass audits the v1 guide against existing Survival Mode constraints, progression policy, selected reset/training/crafting defaults, current guide logistics cues, and generated geography support data.

| Check | Status | Evidence |
| --- | --- | --- |
| Setup baseline | Pass | 8 setup rules; recommended_action: none: 8. |
| Survival constraint table | Pass with explicit route-resolution row | 29 constraint rows; recommended_action: none: 28, none_existing_route_resolution: 1. |
| Guide section logistics | Pass | 81 guide sections scanned; 80 route sections include explicit logistics cues. |
| Legendary progression constraints | Pass | 18 progression constraint rows accounted in current guide coverage. |
| Reset, training, crafting, and policy defaults | Pass | 51 progression-source rows represented. |
| Cold and transport geography support | Pass | 6 cold-risk groups and 8 transport/access groups audited. |

## TB-041 Branch and Spoiler QA

Status: TB-041 branch and spoiler QA complete; result: Pass with explicit route-resolution rows.

No broad gameplay research was performed. This pass audits current guide branch policy, the branch decision matrix, the existing branch coverage audit, guide-local branch cues, and curated spoiler-language phrases.

| Check | Status | Evidence |
| --- | --- | --- |
| Branch policy setup | Pass | 4 policy rows; recommended_action: none: 4. |
| Branch decision matrix | Pass with explicit route-resolution row | 19 matrix rows; recommended_action: none: 19, none_existing_route_resolution: 0. |
| Existing branch audit rows | Pass with explicit route-resolution rows | 76 branch-audit rows mirrored; recommended_action: none: 76, none_existing_route_resolution: 0. |
| Guide-local branch cues | Pass | 17 branch-route cue rows; recommended_action: none: 17. |
| Spoiler discipline | Pass | 2 spoiler-language rows; recommended_action: none: 2. |

## TB-042 Simulated Playtest QA

Status: TB-042 simulated playtest QA complete; result: Pass with explicit route-resolution rows.

No broad gameplay research was performed. This document-level pass audits executable section starts, numbered route steps, route-heavy section logistics cues, prior QA repair-action state, placeholder language, and visibility of known unresolved route-resolution rows. It is not a live PS4 run.

| Check | Status | Evidence |
| --- | --- | --- |
| Player setup contract | Pass | 7 setup/player-contract rows; recommended_action: none: 7. |
| Section walkthrough | Pass | 81 route-section rows; pass_section_executable: 80, pass_non_executable_handoff_section: 1. |
| Prior QA integration | Pass | 4 prior-QA artifacts checked; recommended_action: none: 4. |
| Route-resolution visibility | Pass with explicit route-resolution row | 1 route-resolution visibility row; recommended_action: none_existing_route_resolution: 1. |
| Simulated-playtest limits | Pass | 2 scope-boundary rows; recommended_action: none: 2. |

## TB-043 Unresolved-Risk Report and Final QA Summary

Status: TB-043 unresolved-risk report and final QA summary complete; result: Pass with known unresolved risks.

No broad gameplay research was performed. This section summarizes explicit route-resolution rows already visible in the guide, coverage ledger, appendices, and QA artifacts; it does not resolve or accept those risks.

| Check | Status | Evidence |
| --- | --- | --- |
| Risk report artifact | Pass | drafts/final-guide/unresolved-risk-report.md exists. |
| Risk register row count | Pass | 342 risk-register rows; expected 342 unresolved objective rows. |
| Severity triage | Pass | high: 110, medium: 87, low: 145. |
| Category ownership | Pass | ae_creation: 1, book_document: 145, collectible: 26, crafting_unlock: 21, location: 3, misc_objective: 34, npc_relationship: 2, quest: 41, radiant: 8, spell_power: 8, trophy: 7, unique_item: 46 |

## Remaining Work Handoff

| Task | Owner scope |
| --- | --- |
| TB-044 | Resolve high-severity route-resolution risks from the TB-043 risk register. |

## Inputs

| Path | Use |
| --- | --- |
| drafts/final-guide/main-guide-v1.md | Player-facing guide checked for placeholder phrases and coverage support. |
| drafts/final-guide/appendices-v0.md | Appendix heading and unresolved-register checks. |
| data/guide-coverage/main-guide-v1-coverage.csv | COV summary row presence. |
| data/guide-coverage/main-guide-v1-final-coverage-summary.csv | Final objective, audit, and unresolved summary counts. |
| data/guide-coverage/main-guide-v1-objective-final-status.csv | Per-objective final coverage status. |
| data/checklist-mapping/coverage-matrix.csv | Checklist row source count. |
| data/guide-coverage/main-guide-v1-*-audit.csv | Generated COV audit artifacts. |
| data/guide-coverage/main-guide-v1-order-delayed-task-audit.csv | TB-038 order and delayed-task audit. |
| data/guide-coverage/main-guide-v1-order-delayed-task-repair.csv | TB-038R delayed-task repair/classification register. |
| data/guide-coverage/main-guide-v1-trophy-leveled-cell-audit.csv | TB-039 trophy, leveled-item, and cell-entry audit. |
| data/guide-coverage/main-guide-v1-survival-legendary-audit.csv | TB-040 Survival Mode and Legendary difficulty audit. |
| data/guide-coverage/main-guide-v1-branch-spoiler-audit.csv | TB-041 branch and spoiler QA audit. |
| data/guide-coverage/main-guide-v1-playtest-audit.csv | TB-042 simulated playtest audit. |
| drafts/final-guide/playtest-notes.md | TB-042 simulated playtest notes. |
| data/guide-coverage/main-guide-v1-unresolved-risk-register.csv | TB-043 row-level unresolved-risk register. |
| data/guide-coverage/main-guide-v1-unresolved-risk-summary.csv | TB-043 unresolved-risk summary counts. |
| drafts/final-guide/unresolved-risk-report.md | TB-043 unresolved-risk report. |

Regenerate with `python3 tools/build_coverage_qa_checklist.py` after refreshing coverage or audit artifacts.
