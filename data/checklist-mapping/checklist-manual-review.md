# Checklist Manual Review Resolution

Status: TB-031B complete.

Input: `data/checklist-mapping/coverage-matrix.csv`

Raw checklist snapshot: `data/checklist-mapping/raw/Skyrim Checklist.xlsx`

This pass resolved every row that previously used the generic `manual_review_required` status. It did not add new gameplay facts or new objective rows merely because the checklist named an item. Rows were either mapped to existing source-backed objectives/support tables or converted into typed source-readiness holds owned by the earliest appropriate follow-up task.

## Resolution Counts

| Result | Rows | Meaning |
| --- | ---: | --- |
| Newly mapped to existing objective/support handling | 195 | Checklist naming, spelling, abbreviation, parent-objective, or detail-location gaps now map to existing source-backed rows. |
| Source-readiness hold | 90 | Checklist-only rows remain unpromoted until a named follow-up validates source scope, adds/promotes support rows, or excludes them. |
| Generic manual review | 0 | No row may remain in an untyped manual bucket after TB-031B. |

Two additional rows (`Dawnguard` and `Dragonborn`) were fixed by tightening the checklist normalizer so standalone DLC quest titles are not stripped as empty content suffixes.

## New Match Sources

| `match_source` | Rows | Treatment |
| --- | ---: | --- |
| `checklist_manual_representative_activity` | 65 | Mapped no-journal work/favor variants to existing representative activity rows; TB-031C confirmed no all-variant escalation, and TB-031F still chooses exact route actions. |
| `checklist_manual_objective_alias` | 27 | Mapped checklist wording to existing quest/objective rows. |
| `checklist_transformation_perk_parent` | 22 | Mapped Werewolf/Vampire Lord perk checklist rows to existing transformation parent rows. |
| `checklist_detail_location_alias` | 19 | Mapped checklist detail-location rows to existing location objectives. |
| `checklist_detail_quest_alias` | 19 | Mapped collectible rows whose detail named an existing quest parent. |
| `checklist_quest_perk_parent` | 9 | Mapped quest-perk checklist rows to existing permanent ability/reward rows. |
| `checklist_manual_property_alias` | 8 | Mapped house/land checklist wording to existing property rows. |
| `checklist_manual_pet_spell_parent` | 8 | Mapped pet teleport spells to existing pet-acquisition parent rows. |
| `checklist_manual_book_alias` | 7 | Mapped spelling/punctuation variants to existing book/document or skill-book rows. |
| `checklist_manual_spell_parent` | 4 | Mapped quest-granted spells to existing quest parent rows. |
| `checklist_manual_unique_item_alias` | 2 | Mapped unique-gear spelling variants to existing objective rows. |

## Source-Readiness Holds

These rows are no longer generic manual review. They are explicit `source_readiness_required` rows with `match_status=support_table_only`, `source_note_refs=SN-000125-checklist-manual-review-reconciliation.md`, and a named owner in `guide_location`.

This table records the TB-031B source-readiness buckets with current owner annotations where later TB-031 tasks have completed. For current counts, use `checklist-coverage-summary.md`; by TB-031G, the single location row (`The Chill*`) has been resolved as an explicit official-scope exclusion, and by TB-031H the remaining book/document, unique-gear, and skill-book holds are assigned to TB-036.

| Category | Rows | Owner |
| --- | ---: | --- |
| `book_document` | 43 | TB-036 book/document appendix source-readiness review after TB-031H ownership audit. |
| `unique_item` | 34 | TB-036 unique-gear appendix source-readiness review after TB-031H ownership audit. |
| `quest` | 4 | Resolved by TB-031F; any future checklist-only quest catch-all goes to TB-034/TB-037. |
| `alchemy_effect` | 4 | Resolved by TB-031E; any future checklist-only alchemy catch-all goes to TB-033/TB-037. |
| `collectible_item` | 2 | Resolved by TB-031F; any future checklist-only collectible catch-all goes to TB-033/TB-037. |
| `enchantment` | 1 | Resolved by TB-031E; any future checklist-only enchantment catch-all goes to TB-033. |
| `location` | 1 | Resolved later in TB-031G as the `The Chill*` official-scope exclusion. |
| `skill_book` | 1 | TB-036 skill-book appendix source-readiness review after TB-031H ownership audit. |

## Boundary

`source_readiness_required` does not mean the item is route-ready, appendix-ready, or in final scope. It means the raw checklist row is now visible as a typed reconciliation input, and the named task must make a source-backed decision before final checklist synchronization.

Do not use TB-032 warning prose, TB-033 validation, or final-guide drafting to silently promote these rows. Promotion requires source-standard-compliant research and either objective/support-table updates or an explicit exclusion.

Expected counts after TB-031B:

| Check | Expected |
| --- | ---: |
| `manual_review_required` rows | 0 |
| `unmatched` rows | 0 |
| `source_readiness_required` rows | 90 |
