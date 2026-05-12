# Deferred Work Audit

Status: TB-031J source-readiness pull-forward complete; TB-031K downstream refresh complete; Phase 10 deferred-work audit closed.

This file exists so deferred route-planning work is not hidden in prose handoffs. It is a coordination artifact only; it does not add gameplay requirements beyond `docs/guide-specification.md`, `docs/decisions-log.md`, and source-backed data files.

## Audit Method

The audit searches project Markdown and lightweight CSV/status metadata under `docs/`, `data/`, `drafts/`, `sources/`, and `tools/` for buried planning language such as `deferred`, `later`, `handoff`, `pending`, `unresolved`, `must decide`, `checklist mapping`, `exact`, `candidate`, `manual review`, `scope review`, `needs_review`, and `needs_validation`.

Generated CSV rows are not used as prose sources for this audit, except through `data/checklist-mapping/checklist-coverage-summary.md` and targeted owner/status scans that look for stale broad generated labels.

## Newly Explicit Phase 10 Tasks

| Task | Earliest safe point | Deferred work now made explicit | Why it must happen before dependent work |
| --- | --- | --- | --- |
| TB-031A | After TB-031 validation hardening | Complete: resolved all `scope_review_required` rows, especially the 312 broad regular-book checklist rows. | Final route and appendices should not inherit spreadsheet scope accidentally. |
| TB-031B | After TB-031 validation hardening | Complete: resolved all generic manual-review rows; 195 rows now map to existing source-backed handling and 90 checklist-only rows are typed `source_readiness_required` holds. | Warning, validation, appendix, and final guide work should not proceed with unknown checklist coverage. |
| TB-031C | After TB-031A/TB-031B | Complete: resolved checklist-driven escalation for representative radiants, branch-only rewards, option defaults, Thieves Guild 125 jobs, Volkihar conversion depth, spouse-state branch needs, Bittercup/Thirsk/Ghosts variants, Velehk/Frost/Ralis, and Battle of the Champions side coverage. | Branch/warning prose now has explicit escalation decisions instead of hidden checklist assumptions. |
| TB-031D | After checklist scope/manual/escalation decisions | Complete: `data/route-planning/route-default-decisions.md` chooses route-affecting defaults and Survival logistics choices: first safe storage, main base/home, property services, travel infrastructure, spouse, children, stewards, farm steward, Black Book power defaults, final transformation state, and representative no-journal activity/favor targets. | Route, warning, branch, and option-list work now has explicit defaults instead of hidden assumptions. |
| TB-031E | After TB-031D | Complete: `data/constraints/progression-source-selection.md` and `data/constraints/progression-source-selections.csv` choose progression source selections and grind distribution: skill-book copies/read timing, spell-tome sources, enchantment source families, alchemy source methods, merchant investment circuit rules, crafting outputs/materials, training blocks, Legendary reset distribution, Oghma timing, and allowed exploit conditions. | Progression choices now have explicit inputs for level gates, carry/storage planning, shopping loops, material routing, warnings, and final validation. |
| TB-031F | After checklist/progression reconciliation | Complete: `data/checklist-mapping/counter-coverage-plan.md` resolves checklist counters and route mechanics: Sideways, Hero of the People, Delver, Explorer, Reader, Thief, Snake Tongue, Lost Relic fillers, Fishing, cutting lumber, milling, trophy-pop fallbacks, and the six TB-031F source-readiness rows. | Counter mechanics now have source-backed route-planning rules consumed by TB-031G and continuing into TB-032, TB-033, and TB-034 instead of hidden assumptions. |
| TB-031G | After checklist/manual/counter reconciliation | Complete: `data/locations/location-route-validation.md` resolves Delver/Explorer mechanics, normal clear-trigger class, Angarvunde/Mistwatch exceptions, duplicate/secondary marker links, AE content-location handling, coordinate exception rules, separate-worldspace/manual geography rules, and the `The Chill*` checklist exclusion. | Location clear/discovery rows now have source-backed route-validation rules before warnings, validation, or final placement use them. |
| TB-031H | After TB-031A through TB-031G | Complete: `docs/source-objective-readiness-audit.md` audits source, objective, support-table, and generated-index readiness; defines source-note status semantics; removes TB-031H from generated future-owner labels; initially assigns concrete ownership for remaining checklist-only source-readiness rows. | Future tasks now have explicit owners for source-note, objective-row, support-row, and generated-index metadata; TB-031J then pulled the checklist source-readiness queue forward before warning work. |
| TB-031I | After TB-031A through TB-031H | Complete: final scan confirmed active generic deferrals are either completed, explicitly assigned to TB-032 or later, or recorded in reviewable audit/status artifacts. | Warning prose can now start without inheriting hidden checklist/default/progression/location/source-readiness work. |
| TB-031J | Before TB-032 warning placement | Complete: `data/checklist-mapping/source-readiness-resolutions.csv` and `SN-000129` pull the 78 remaining source-readiness rows forward; 75 map to main-route handling, 1 maps to BR-007 branch coverage, and 2 are explicit exclusions. | Warning, validation, appendix, and route work no longer carry an unresolved checklist source-readiness bucket that could force rework later. |
| TB-031K | After TB-031J | Complete: downstream constraint, anchor, skeleton, geography, main-prototype, branch, checklist, task-board, and handoff artifacts were refreshed to use completed TB-031 decisions. | TB-032 consumed the current planning stack without first reconciling stale future-work language. |

## Second-Pass Findings

| Finding | Evidence pattern | Explicit owner |
| --- | --- | --- |
| Location rows are corridor-ready but not route-step-ready. | TB-031G resolved clear/discovery mechanics, marker exceptions, content-location handling, and coordinate exception rules. Final path order and black-box step placement remain separate route drafting work. | TB-034, with warning triggers in TB-032 and counter validation in TB-033 |
| Source-note readiness is ambiguous. | TB-031H found 97 older source notes still marked `Status: needs review.` | Complete in TB-031H: `sources/source-notes/README.md` defines the status as historical/source-list input, not a hidden blocker or validation state. |
| Generated indexes can preserve stale broad owners. | Route-planning and checklist generators still emitted TB-031H future-owner labels before the audit. | Complete in TB-031H: regenerated route/checklist/progression outputs no longer name TB-031H as a future owner. |
| Objective/support-table readiness is also ambiguous. | `data/objectives/objectives.csv` and several support tables intentionally carry `needs_review`, `needs_validation`, `source_listed_candidate`, `option_list`, `safe_storage_status`, or other non-final readiness markers. | Complete in TB-031H: `docs/source-objective-readiness-audit.md` assigns these to TB-033, TB-034, TB-035, TB-036, or TB-037 by use. |
| Older source notes and rows can contain stale owner references. | Some historical notes still refer to now-complete tasks such as TB-013, TB-014, TB-016, TB-019, TB-020, or TB-030. | Closed in TB-031I for active coordination surfaces. Historical source notes/task-board entries remain intact unless a future concrete row edit needs a source-standard-compliant update. |

## Already Explicit Later Work

| Existing task | Covered deferred work |
| --- | --- |
| TB-032 | Complete: exact warning and hard-save trigger prose for leveled rewards, cell-entry locks, NPC risks, trophy actions, bug-prone steps, and branch save/reload points now lives in `drafts/route-prototypes/main-route-prototype-v0.md` and `data/constraints/quest-conflicts-hard-saves.md`. |
| TB-033 | Constraint validation, branch verification, final skill-state validation, trophy/reward safety, Survival support, and all-perks/all-skills satisfaction checks. |
| TB-034 | Minimal route prototype after warnings and validation. |
| TB-035 | Black-box guide expansion after route prototype validation. |
| TB-036 | Appendices/reference tables after checklist/manual/scope/source-readiness review and guide drafting; no unresolved source-readiness bucket remains for appendices. |
| TB-037 through TB-043 | Final coverage, order, trophy, Survival, branch, playtest, and unresolved-risk QA passes. |

## Final Scan Results

TB-031I scanned current coordination docs, route prototypes, branch prototypes, checklist summaries, generated owner fields, and readiness artifacts for generic handoffs to `TB-030`, `later`, `final route`, `checklist mapping`, `route validation`, `manual validation`, `source_listed_candidate`, `needs_validation`, and `needs review`.

| Scan area | Result |
| --- | --- |
| Checklist coverage generated rows | No `manual_review_required`, `scope_review_required`, `unmatched`, TB-031H future-owner labels, or `source_readiness_required` rows remain after TB-031J. |
| Prototype objective block map | No `TB-031H`, `route_anchor_or_later_pass`, `source_or_support_validation`, or `manual_route_validation` values remain in active generated ownership fields. |
| Progression source selections | No TB-031H future-owner labels remain in route timing, validation owner, or notes fields. |
| Branch/default/checklist wording | Older route-prototype language that still described branch defaults, flexible objective insertion, or checklist synchronization as unresolved was updated to point at TB-028/TB-029, TB-026, and TB-030 through TB-031I completions. |
| Remaining warning and hard-save work | TB-032 complete at trigger/register level; final step numbers and path placement remain TB-034. |
| Remaining route placement work | Explicitly assigned to TB-034, with TB-033 validation before the minimal prototype. |
| Remaining checklist appendix work | Explicitly assigned to TB-036/TB-037. Source-readiness holds are complete after TB-031J; appendices still verify/reference coverage after final guide drafting. |
| Historical source notes and task-board history | Left intact as history unless a future concrete row edit requires source-note maintenance. |

## Closed Audit Rule

After TB-031I, do not insert new generic handoffs such as `later`, `manual validation`, `source readiness`, or `needs review` into active planning artifacts unless the same row or sentence names a concrete owner task and reason.

TB-032 is complete. TB-033 may now validate the warning-layered prototype against the constraint tables; it should not reopen the completed TB-031A through TB-031J checklist/default/progression/counter/location/readiness decisions unless it finds a concrete contradiction.
