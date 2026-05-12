# Source and Objective Readiness Audit

Status: TB-031H complete.

This is a coordination audit only. It does not add gameplay facts or replace `docs/source-standards.md`; any future row-level gameplay correction still needs a source check and citation in the row's source note.

## Scope

TB-031H reviewed readiness labels after TB-031A through TB-031G resolved checklist scope, manual review, escalation, defaults, progression source selection, counter mechanics, and location route validation.

Checked surfaces:

* `sources/source-notes/README.md` and all `sources/source-notes/SN-*.md`
* `data/objectives/objectives.csv`
* support CSVs under `data/books/`, `data/items/`, `data/locations/`, `data/npc/`, `data/properties/`, and `data/skills/`
* `data/route-planning/objective-constraints.csv`
* `data/route-planning/objective-route-index.csv`
* `data/route-planning/prototype-objective-block-map.csv`
* `data/checklist-mapping/coverage-matrix.csv`
* current checklist, progression, counter, location, branch, and route-default planning notes

No broad gameplay research was performed.

## Readiness Scan

| Surface | TB-031H finding | Treatment |
| --- | --- | --- |
| Source notes | 97 notes still say `Status: needs review.`; 30 use `researched` variants; 1 is `complete.` | Do not mass-rename old notes. `sources/source-notes/README.md` now defines `needs review` as historical/source-list input, not a hidden blocker or validation state. Future tasks source-check concrete rows before changing route facts. |
| Objective rows | All 2,789 rows still have `research_status=needs_review`; validation is `not_started` for 2,769 and `needs_review` for 20. | Leave unchanged. These are database-wide inventory/QA labels, not final-route blockers. TB-033 remains the final validation owner; TB-034/TB-035 consume objective rows only after inspecting citations and constraints. |
| Generated prototype map | Pre-audit rows still named TB-031H as an owner for dependency/support placement. | `tools/build_prototype_objective_block_map.py` now assigns unresolved dependency/support rows to named downstream owners such as TB-034, TB-035, TB-033, or existing TB-031E/TB-031F buckets. Regenerated CSV has 0 `TB-031H` `deferred_to` values. |
| Checklist coverage matrix | 78 `source_readiness_required` rows remained after TB-031G. | These are now assigned to TB-036: 43 book/document rows, 34 unique-gear rows, and 1 skill-book row. Regenerated matrix has 0 TB-031H owner labels. |
| Progression source-selection rows | Investment rows for bugged or unknown merchants still mentioned TB-031H/TB-033. | Generator now assigns those rows to TB-033 investment validation only. |
| Property support rows | 52 rows retain `safe_storage_status=needs_validation_later`; 7 Goldenhills notes named TB-031H/TB-035. | Goldenhills notes now say TB-031H audited ownership and TB-035 owns option/final-guide validation. Other property rows remain specific TB-032/TB-034/TB-035/TB-033 work depending on warning, placement, option, or validation use. |
| Book and spell support rows | Many rows remain `source_listed_candidate` because they are candidate sources, not chosen route steps. | Leave as candidate data. TB-031E chose progression source policy; TB-034/TB-036/TB-037 will consume the tables for route placement, appendices, and final checklist verification. |
| Location support rows | `location-catalog.csv` has no remaining `needs_research` access rows; `route_status=source_listed_candidate` remains normal for 437 locations. | Leave as candidate geography data. TB-031G resolved access/clear/discovery mechanics; TB-032 places warnings and TB-034 places final route steps. |
| Merchant investment support rows | 33 available, 13 bugged/unofficial-patch-only, 4 `unknown_needs_validation`. | Available rows remain in the investment circuit; bugged/unknown rows are not required route investments unless TB-033 validates official PS4 AE availability. |

## Explicit Remaining Owners

| Remaining queue | Rows or scope | Owner | Reason it is not resolved in TB-031H |
| --- | ---: | --- | --- |
| Checklist-only book/document source-readiness holds | 43 | TB-036 | Requires appendix/reference-table source validation and possible promotion/exclusion against final guide coverage. |
| Checklist-only unique-gear source-readiness holds | 34 | TB-036 | Requires unique-item appendix/source validation before final inclusion; TB-031H only assigns ownership. |
| Checklist-only skill-book source-readiness hold | 1 | TB-036 | Requires title/source spelling validation in the appendix/reference layer. |
| Objective-wide validation status | 2,789 objectives | TB-033 | Final validation depends on warning placement, route ordering, branches, counters, rewards, and Survival support. |
| Dependency anchors with no route candidate data | 409 prototype-map rows now assigned mainly to TB-034 | TB-034 | These are route-placement rows, not hidden source-readiness rows. They follow parent quests/dependencies during minimal route prototyping. |
| Property/storage validation | 52 `needs_validation_later` property-detail rows | TB-032/TB-034/TB-035/TB-033 by use | Warning timing, route placement, option presentation, and final storage validation are separate downstream tasks. |
| Unknown/bugged merchant investments | 17 non-routed investment rows | TB-033 | Official PS4 AE availability or bug behavior must be validated before any route requirement. |

## Actions Taken

| Artifact | Change |
| --- | --- |
| `sources/source-notes/README.md` | Added source-note status semantics and a TB-031H audit pointer. |
| `tools/build_prototype_objective_block_map.py` | Removed TB-031H from future generated owner labels; unresolved dependency/support rows now point to TB-034/TB-035 or existing specific owners. |
| `tools/build_checklist_coverage.py` | Reassigned remaining checklist source-readiness categories to TB-036/TB-037/TB-033 downstream owners and removed TB-031H as a future owner. |
| `tools/build_progression_source_selection.py` | Removed TB-031H from unavailable-investment validation timing. |
| `data/properties/property-details.csv` | Reassigned Goldenhills child-room/display-room validation wording to TB-035 after TB-031H audit. |
| Planning Markdown | Updated checklist, branch, route-default, progression, counter, location, route-planning, and source-note text that still described TB-031H as a future validator. |
| Generated CSVs | Regenerated route-planning, progression-source-selection, route-planning SQLite, and checklist coverage outputs. |

## Post-Audit Checks

| Check | Result |
| --- | --- |
| `prototype-objective-block-map.csv` rows naming TB-031H in `deferred_to` | 0 |
| `coverage-matrix.csv` rows naming TB-031H in `guide_location` or `deferred_to` | 0 |
| `progression-source-selections.csv` rows naming TB-031H in `route_timing` | 0 |
| Remaining `source_readiness_required` rows | 78, all explicitly assigned to TB-036 |

## Residual Risk

No unresolved TB-031H blocker remains. The remaining risk is ordinary downstream validation risk: TB-036 may promote or exclude checklist-only book/unique-gear rows, TB-033 may reject a progression or investment assumption, and TB-034/TB-035 may need to adjust placement or option presentation after warnings and validation are available.

