# Checklist Coverage Summary

Status: TB-031H source/objective/support readiness audit complete.

Raw input: `data/checklist-mapping/raw/Skyrim Checklist.xlsx`

Generated output: `data/checklist-mapping/coverage-matrix.csv`

TB-031H audited source/objective/support-table readiness ownership and removed TB-031H from generated future-owner labels. The matrix is generated from the raw workbook plus existing objective, support-table, route-planning, branch-prototype, default, progression-selection, counter-planning, location-validation, and readiness-audit artifacts.

## Intake Counts

| Checklist tab | Rows |
| --- | ---: |
| Books | 763 |
| Learned Alchemy Effects | 732 |
| Quests | 660 |
| Locations | 452 |
| Perks | 282 |
| Unique Gear | 239 |
| Spells | 167 |
| Merchants | 129 |
| Dragon Shouts | 81 |
| Recruitable Followers | 74 |
| Collectible Items | 60 |
| Enchanting Effects | 58 |
| Total | 3,697 |

## Mapping Counts

| Mapping type | Rows | Meaning |
| --- | ---: | --- |
| Main-route prototype block | 3,085 | Matched to an objective or support row currently assigned to main-route prototype handling. Final guide step numbers remain later work. |
| Explicit exclusion | 320 | Source-backed exclusion or current-scope exclusion with justification. Includes 312 broad regular-book rows resolved by TB-031A and the TB-031G `The Chill*` official-scope exclusion. |
| Appendix-only checklist | 107 | Tracked outside the current main-route prototype as appendix/reference coverage. |
| Source-readiness hold | 78 | Checklist-only rows carried as typed source-readiness work for TB-036; not route-ready until validated, promoted, or excluded. |
| Option-list note | 75 | Matched to route-default and option-list recommendation surfaces rather than routed branches. |
| Branch-route prototype | 32 | Matched to TB-029 branch prototype coverage. |

## Status Counts

| Status | Rows |
| --- | ---: |
| `mapped_to_route_prototype` | 3,085 |
| `excluded_with_justification` | 320 |
| `mapped_to_appendix` | 107 |
| `source_readiness_required` | 78 |
| `mapped_to_option_list` | 75 |
| `mapped_to_branch_prototype` | 32 |

## Resolved Scope Buckets

| Bucket | Rows | TB-031A treatment |
| --- | ---: | --- |
| General books | 312 | Explicitly excluded from required route and required appendix coverage under the project's book/document scope. These rows are auditable with `match_source=book_scope_review`. |

## Resolved Manual-Review Bucket

| Bucket | Rows | TB-031B treatment |
| --- | ---: | --- |
| Naming/detail aliases mapped to existing source-backed rows | 195 | Existing objective, property, activity, location, quest-detail, perk, transformation, pet, book, spell, and unique-item rows now cover these checklist rows. |
| Source-readiness holds after TB-031B | 90 | Generic manual review was replaced by typed `source_readiness_required` rows with named owners and `source_note_refs=SN-000125-checklist-manual-review-reconciliation.md`. |
| TB-031E-owned progression holds resolved | 5 | `Damage Stamina` now maps to `OBJ-002515` and the four `Kesh Fiber (AE)` rows now map to `OBJ-002678`, with alias support recorded in SN-000126. |
| Source-readiness holds after TB-031E | 85 | At that checkpoint, remaining holds fed TB-031F, TB-031G, and the later readiness audit path that ultimately assigned residual rows to TB-036. |
| TB-031F-owned counter/action holds resolved | 6 | `Rebuilding the Blades` and `Dragon Hunting` now map to the Paarthurnax/Blades branch prototype; `Archery Practice`, `Scare My Enemy`, `Firebrand Wine Case`, and `Map of Dragon Burials` now map to source-backed main-route objective handling. |
| Source-readiness holds after TB-031F | 79 | At that checkpoint, remaining holds fed TB-031G and the later readiness audit path that ultimately assigned residual rows to TB-036. |
| TB-031G-owned location hold resolved | 1 | `The Chill*` is now an explicit exclusion under official PS4 AE scope because its map marker is USKP-only, not official Skyrim. |
| Source-readiness holds after TB-031G | 78 | Remaining holds entered TB-031H readiness audit. |
| TB-031H owner audit | 78 | TB-031H assigned the remaining checklist-only holds to TB-036 book/document, skill-book, or unique-gear source-readiness validation. No generated checklist row now names TB-031H as a future owner. |
| Generic manual review | 0 | `tools/validate_coverage.py` no longer allows unmatched/manual-review rows. |

## Source-Readiness Holds

| Bucket | Rows | Owner |
| --- | ---: | --- |
| Book/document rows | 43 | TB-036 book/document appendix source-readiness review. |
| Unique item rows | 34 | TB-036 unique-gear appendix source-readiness review. |
| Skill-book row | 1 | TB-036 skill-book appendix source-readiness review. |

## Handoffs

| Owner | Handoff |
| --- | --- |
| TB-031 | Complete: `tools/validate_coverage.py` now validates row uniqueness, allowed mapping/status/match values, format checks, blank-field rules by status, and required review/exclusion/branch fields. |
| TB-031A | Complete: all 312 `scope_review_required` broad regular-book rows are explicit exclusions with justification and `match_source=book_scope_review`; no `scope_review_required` rows remain. |
| TB-031B | Complete: no `manual_review_required` or `unmatched` rows remain. 195 rows were mapped to existing source-backed handling; 90 checklist-only rows are explicit `source_readiness_required` holds for named later tasks. |
| TB-031C | Complete: `checklist-escalation-decisions.md` records no all-target radiant escalation, required Thieves Guild 125-job counter coverage, canonical/default promotions, and branch-only holds. |
| TB-031D | Complete: `data/route-planning/route-default-decisions.md` records route-affecting defaults for storage, bases, property services, travel, household roles, Black Book powers, final transformation state, and representative activity/favor targets. |
| TB-031E | Complete: `data/constraints/progression-source-selection.md` and `data/constraints/progression-source-selections.csv` record selected book/tome sources, enchantment source families, alchemy source methods, investments, crafting outputs, training blocks, reset distribution, Oghma timing, and progression alias fixes. |
| TB-031F | Complete: `counter-coverage-plan.md` records route-planning counter checkpoints, Thieves Guild 125-job policy, Lost Relic filler policy, Fishing/support-action treatment, trophy-pop fallbacks, and six source-readiness row resolutions. |
| TB-031G | Complete: `location-route-validation.md` records Delver/Explorer mechanics, normal clear-trigger policy, duplicate/secondary marker handling, AE content-location treatment, coordinate/access rules, and the `The Chill*` official-scope exclusion. |
| TB-031H | Complete: `docs/source-objective-readiness-audit.md` records source-note, objective-row, support-table, generated-index readiness, stale owner label, unknown/audit-only support row, and broad `later`/`manual validation` ownership treatment after TB-031A through TB-031G. |
| TB-031I | Re-scan deferred-work language and close `docs/deferred-work-audit.md` before warning-layer work starts. |
| TB-032 | Warning placement should proceed only after TB-031I so warnings use resolved checklist, default, progression, counter, branch, location, and source-readiness decisions. |
| TB-033 | Validate that branch/checklist mappings still preserve canonical continuity and trophy/reward constraints. |
| TB-036/TB-037 | Verify appendix and final checklist coverage after TB-031A/B/C/E/F/G/H and final guide drafting. |
