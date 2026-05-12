# Checklist Coverage Summary

Status: TB-031C escalation decisions complete.

Raw input: `data/checklist-mapping/raw/Skyrim Checklist.xlsx`

Generated output: `data/checklist-mapping/coverage-matrix.csv`

No new gameplay research was performed. The matrix is generated from the raw workbook plus existing objective, support-table, route-planning, and branch-prototype artifacts.

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
| Main-route prototype block | 3,076 | Matched to an objective or support row currently assigned to main-route prototype handling. Final guide step numbers remain later work. |
| Explicit exclusion | 319 | Source-backed exclusion or current-scope exclusion with justification. Includes 312 broad regular-book rows resolved by TB-031A. |
| Appendix-only checklist | 107 | Tracked outside the current main-route prototype as appendix/reference coverage. |
| Source-readiness hold | 90 | Checklist-only rows carried as typed source-readiness work for TB-031E through TB-031H/TB-036 plus TB-031F quest/counter review; not route-ready until validated, promoted, or excluded. |
| Option-list note | 75 | Matched to option/default recommendation surfaces rather than routed branches. |
| Branch-route prototype | 30 | Matched to TB-029 branch prototype coverage. |

## Status Counts

| Status | Rows |
| --- | ---: |
| `mapped_to_route_prototype` | 3,076 |
| `excluded_with_justification` | 319 |
| `mapped_to_appendix` | 107 |
| `source_readiness_required` | 90 |
| `mapped_to_option_list` | 75 |
| `mapped_to_branch_prototype` | 30 |

## Resolved Scope Buckets

| Bucket | Rows | TB-031A treatment |
| --- | ---: | --- |
| General books | 312 | Explicitly excluded from required route and required appendix coverage under the project's book/document scope. These rows are auditable with `match_source=book_scope_review`. |

## Resolved Manual-Review Bucket

| Bucket | Rows | TB-031B treatment |
| --- | ---: | --- |
| Naming/detail aliases mapped to existing source-backed rows | 195 | Existing objective, property, activity, location, quest-detail, perk, transformation, pet, book, spell, and unique-item rows now cover these checklist rows. |
| Source-readiness holds | 90 | Generic manual review is replaced by typed `source_readiness_required` rows with named owners and `source_note_refs=SN-000125-checklist-manual-review-reconciliation.md`. |
| Generic manual review | 0 | `tools/validate_coverage.py` no longer allows unmatched/manual-review rows. |

## Source-Readiness Holds

| Bucket | Rows | Owner |
| --- | ---: | --- |
| Book/document rows | 43 | TB-031H/TB-036 source-readiness review. |
| Unique item rows | 34 | TB-031H/TB-036 source-readiness review. |
| Quest rows | 4 | TB-031F/TB-031H source-readiness review after TB-031C found no immediate promotion without source validation. |
| Alchemy rows | 4 | TB-031E/TB-031H source-readiness review. |
| Collectible item rows | 2 | TB-031F/TB-031H source-readiness review. |
| Enchantment row | 1 | TB-031E/TB-031H source-readiness review. |
| Location row | 1 | TB-031G/TB-031H source-readiness review. |
| Skill-book row | 1 | TB-031H/TB-036 source-readiness review. |

## Handoffs

| Owner | Handoff |
| --- | --- |
| TB-031 | Complete: `tools/validate_coverage.py` now validates row uniqueness, allowed mapping/status/match values, format checks, blank-field rules by status, and required review/exclusion/branch fields. |
| TB-031A | Complete: all 312 `scope_review_required` broad regular-book rows are explicit exclusions with justification and `match_source=book_scope_review`; no `scope_review_required` rows remain. |
| TB-031B | Complete: no `manual_review_required` or `unmatched` rows remain. 195 rows were mapped to existing source-backed handling; 90 checklist-only rows are explicit `source_readiness_required` holds for named later tasks. |
| TB-031C | Complete: `checklist-escalation-decisions.md` records no all-target radiant escalation, required Thieves Guild 125-job counter coverage, canonical/default promotions, and branch-only holds. |
| TB-031D | Resolve route-affecting defaults and Survival logistics choices before warning/final-route prose depends on them. |
| TB-031E | Resolve exact progression source selections, training/reset/grind distribution, crafting outputs, and allowed exploit conditions. |
| TB-031F | Resolve checklist/trophy counter mechanics and route actions for counters and activity systems. |
| TB-031G | Resolve location access, clear-trigger, discovery/clearance, duplicate-marker, separate-worldspace, and manual geography validation before route/warning prose depends on corridor data. |
| TB-031H | Audit source-note, objective-row, support-table, generated-index readiness, stale owner labels, unknown/audit-only support rows, and broad `later`/`manual validation` ownership text after TB-031A through TB-031G have touched checklist/source rows. |
| TB-031I | Re-scan deferred-work language and close `docs/deferred-work-audit.md` before warning-layer work starts. |
| TB-032 | Warning placement should proceed only after TB-031I so warnings use resolved checklist, default, progression, counter, branch, location, and source-readiness decisions. |
| TB-033 | Validate that branch/checklist mappings still preserve canonical continuity and trophy/reward constraints. |
| TB-036/TB-037 | Verify appendix and final checklist coverage after TB-031A/B/C and final guide drafting. |
