# Deferred Work Audit

Status: active Phase 10 audit.

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
| TB-031F | After checklist/progression reconciliation | Resolve checklist counters and route mechanics: Sideways, Hero of the People, Delver, Explorer, Reader, Thief, Snake Tongue, Lost Relic fillers, Fishing, cutting lumber, milling, and trophy-pop fallbacks. | Counter mechanics affect whether route steps must be inserted before final guide drafting and final QA. |
| TB-031G | After checklist/manual/counter reconciliation | Resolve location access, clear-trigger, and geography validation: exact clear triggers, discovery/clearance mechanics, duplicate-marker and primary-location links, path/access/entrance checks, separate-worldspace/manual geography rows, and location rows marked `needs_research` or manual validation. | The route cannot safely place location clears, Delver/Explorer work, or route warnings from corridor counts alone. |
| TB-031H | After TB-031A through TB-031G | Audit source, objective, support-table, and generated-index readiness after those tasks have touched checklist/source rows: source notes still marked `Status: needs review`, objective/support-table status fields, stale owner references in older notes/rows, generated owner labels, unknown/audit-only support rows, and broad `later`/`manual validation` ownership text. | Future tasks should not have to rediscover whether a source note, objective row, support row, or generated row is review-ready before trusting it; TB-031A through TB-031G must still source-check the rows they change. |
| TB-031I | After TB-031A through TB-031H | Re-scan deferral language and close this audit before TB-032. | Warning prose should not start while route-affecting checklist/default/progression/location/source-readiness work is still hidden in older documents. |

## Second-Pass Findings

| Finding | Evidence pattern | Explicit owner |
| --- | --- | --- |
| Location rows are corridor-ready but not route-step-ready. | Planning docs still warn that straight-line geography is not pathfinding, and `data/locations/location-catalog.csv` still carries `needs_research`, inherited-clear-state, duplicate-marker, and exact-clear-trigger work. | TB-031G |
| Source-note readiness is ambiguous. | Many source notes still say `Status: needs review` even when their downstream task is marked done, making it unclear whether the note is draft-only, reviewed, or intentionally unresolved. | TB-031H |
| Generated indexes can preserve stale broad owners. | Route-planning generators previously emitted broad `TB-030` owners for trophy/checklist/progression rows after TB-030 was already complete. | TB-031H |
| Objective/support-table readiness is also ambiguous. | `data/objectives/objectives.csv` and several support tables intentionally carry `needs_review`, `needs_validation`, `source_listed_candidate`, `option_list`, `safe_storage_status`, or other non-final readiness markers that can affect later trust in the row. | TB-031H |
| Older source notes and rows can contain stale owner references. | Some historical notes still refer to now-complete tasks such as TB-013, TB-014, TB-016, TB-019, TB-020, or TB-030 for work that now resolves through TB-031C through TB-031H, TB-032, or TB-033. | TB-031H/TB-031I |

## Already Explicit Later Work

| Existing task | Covered deferred work |
| --- | --- |
| TB-032 | Exact warning and hard-save prose for leveled rewards, cell-entry locks, NPC risks, trophy actions, bug-prone steps, and branch save/reload points. |
| TB-033 | Constraint validation, branch verification, final skill-state validation, trophy/reward safety, Survival support, and all-perks/all-skills satisfaction checks. |
| TB-034 | Minimal route prototype after warnings and validation. |
| TB-035 | Black-box guide expansion after route prototype validation. |
| TB-036 | Appendices/reference tables after checklist/manual/scope review and guide drafting. |
| TB-037 through TB-043 | Final coverage, order, trophy, Survival, branch, playtest, and unresolved-risk QA passes. |

## Current Audit Rule

Before TB-032 starts, TB-031I must verify that every remaining generic handoff to `TB-030`, `later`, `final route`, `checklist mapping`, `route validation`, `manual validation`, `source_listed_candidate`, `needs_validation`, or `needs review` has one of these states:

* completed in TB-031A through TB-031H;
* explicitly assigned to TB-032 or later with a reason it cannot be resolved earlier;
* recorded as an unresolved risk in a reviewable artifact.
