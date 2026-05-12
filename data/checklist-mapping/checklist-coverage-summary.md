# Checklist Coverage Summary

Status: TB-031A scope review complete.

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
| Main-route prototype block | 2,874 | Matched to an objective or support row currently assigned to main-route prototype handling. Final guide step numbers remain later work. |
| Explicit exclusion | 319 | Source-backed exclusion or current-scope exclusion with justification. Includes 312 broad regular-book rows resolved by TB-031A. |
| Manual review | 287 | No reliable current objective/support-table match. Resolve before final checklist synchronization. |
| Appendix-only checklist | 107 | Tracked outside the current main-route prototype as appendix/reference coverage. |
| Option-list note | 74 | Matched to option/default recommendation surfaces rather than routed branches. |
| Branch-route prototype | 36 | Matched to TB-029 branch prototype coverage. |

## Status Counts

| Status | Rows |
| --- | ---: |
| `mapped_to_route_prototype` | 2,874 |
| `excluded_with_justification` | 319 |
| `manual_review_required` | 287 |
| `mapped_to_appendix` | 107 |
| `mapped_to_option_list` | 74 |
| `mapped_to_branch_prototype` | 36 |

## Resolved Scope Buckets

| Bucket | Rows | TB-031A treatment |
| --- | ---: | --- |
| General books | 312 | Explicitly excluded from required route and required appendix coverage under the project's book/document scope. These rows are auditable with `match_source=book_scope_review`. |

## Remaining Review Buckets

| Bucket | Rows | TB-030 interpretation |
| --- | ---: | --- |
| Quest rows | 119 | Mostly checklist sub-objectives, radiant/activity rows, or item-style rows whose source-list objective granularity differs from the route database. |
| Book/document rows | 49 | Mostly checklist-specific AE or document titles not currently matched to the source-backed book tables. |
| Perk rows | 47 | Mostly transformation perks, quest perks, or abbreviated perk names that need final validation against the separate all-perks/transformation policy. |
| Unique item rows | 36 | Checklist gear names needing source-backed reconciliation against current objective or item-member rows. |
| Collectible item rows | 16 | Miscellaneous quest/collectible objects needing explicit route/checklist treatment. |
| Spell rows | 12 | Mostly pet teleport or quest spell naming gaps needing source reconciliation. |
| Alchemy rows | 4 | `Kesh Fiber` effect rows from the spreadsheet need PS4 AE/source-scope validation before inclusion. |
| Other one-off rows | 3 | One enchantment, one location, and one follower-option naming/source mismatch. |

## Handoffs

| Owner | Handoff |
| --- | --- |
| TB-031 | Complete: `tools/validate_coverage.py` now validates row uniqueness, allowed mapping/status/match values, format checks, blank-field rules by status, and required review/exclusion/branch fields. |
| TB-031A | Complete: all 312 `scope_review_required` broad regular-book rows are explicit exclusions with justification and `match_source=book_scope_review`; no `scope_review_required` rows remain. |
| TB-031B | Resolve all `manual_review_required` rows against source-backed objectives/support tables; add or correct objective/support/source-note rows only where research proves the checklist item is in scope. |
| TB-031C | Resolve checklist-driven escalation decisions for representative radiants, branch-only rewards, option-list defaults, Thieves Guild 125 jobs, Volkihar `New Allegiances`, `The Gift`, Bittercup/Thirsk/Ghosts variants, Velehk/Frost/Ralis, and Battle of the Champions side coverage. |
| TB-031D | Resolve route-affecting defaults and Survival logistics choices before warning/final-route prose depends on them. |
| TB-031E | Resolve exact progression source selections, training/reset/grind distribution, crafting outputs, and allowed exploit conditions. |
| TB-031F | Resolve checklist/trophy counter mechanics and route actions for counters and activity systems. |
| TB-031G | Resolve location access, clear-trigger, discovery/clearance, duplicate-marker, separate-worldspace, and manual geography validation before route/warning prose depends on corridor data. |
| TB-031H | Audit source-note, objective-row, support-table, generated-index readiness, stale owner labels, unknown/audit-only support rows, and broad `later`/`manual validation` ownership text after TB-031A through TB-031G have touched checklist/source rows. |
| TB-031I | Re-scan deferred-work language and close `docs/deferred-work-audit.md` before warning-layer work starts. |
| TB-032 | Warning placement should proceed only after TB-031I so warnings use resolved checklist, default, progression, counter, branch, location, and source-readiness decisions. |
| TB-033 | Validate that branch/checklist mappings still preserve canonical continuity and trophy/reward constraints. |
| TB-036/TB-037 | Verify appendix and final checklist coverage after TB-031A/B/C and final guide drafting. |
