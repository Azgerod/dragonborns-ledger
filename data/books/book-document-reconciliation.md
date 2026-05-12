# Book/Document Reconciliation

Status: placeholder and duplicate-copy reconciliation complete; checklist-specific exceptions pending.

This is not route prose. It records the current source-index coverage and table-level reconciliation for book/document objectives before route placement chooses actual copies.

## Current Coverage

| Area | Objective rows | Location/acquisition rows | Source notes | Status |
| --- | ---: | ---: | --- | --- |
| Skill book titles | 90 | 474 | `SN-000051-skill-books-and-reader.md` | Covered at all-source-listed-copy level. |
| Spell tome titles | 154 | 716 | `SN-000052-spell-tomes-and-learned-spells.md` | Covered at source-listed acquisition level. |
| Black Books | 7 | 7 | `SN-000053-black-books-and-unique-quest-books.md` | Covered at title level. |
| Unique quest books/scrolls | 4 | 5 | `SN-000053-black-books-and-unique-quest-books.md` | Oghma Infinium and three Elder Scrolls covered. |
| Base/DLC quest-book titles | 261 | 376 | `SN-000053-black-books-and-unique-quest-books.md`, `SN-000054-base-dlc-quest-book-category-inventory.md` | UESP quest-book category coverage reconciled. |
| AE quest/action documents | 219 | 219 | `SN-000056-ae-quest-action-book-inventory.md`, `SN-000057-book-document-reconciliation.md` | UESP Creation Club Books and category-only quest documents reconciled. |

Total current `book_document` objective rows: 735.

## TB-007B5 Structural Checks

| Check | Result | Treatment |
| --- | --- | --- |
| `book_document` objective rows without acquisition/location rows | 0 | Every title-level book/document objective has at least one row in a book location table. |
| Duplicate normalized `book_document` objective names | 0 | Duplicate copies are not represented as duplicate objective rows. |
| Remaining aggregate placeholder objective rows | 0 | Aggregate/source-index pages are not objective rows unless promoted to title-level member rows. |
| Title rows that have multiple acquisition candidates | 215 | Route placement will choose one safe/useful acquisition path per required title, unless the title itself must be revisited for quest/state reasons. |

| Table | Title objective rows | Acquisition/location rows | Titles with multiple candidates | Notes |
| --- | ---: | ---: | ---: | --- |
| Skill books | 90 | 474 | 90 | All duplicate copies are candidate rows only. |
| Spell tomes | 154 | 716 | 109 | Vendor, fixed-copy, reward, crafting, starting-spell, and other sources are acquisition candidates only. |
| Black Books, quest books, unique books, and AE documents | 491 | 607 | 16 | Multiple copies exist for a small subset of quest/unique titles; they remain route candidates only. |
| Total | 735 | 1,797 | 215 | No title objective currently lacks acquisition/location coverage. |

## Source-Index Results

| Source inventory | Result | Rationale |
| --- | --- | --- |
| UESP quest-book categories | No open source-index gaps. | 500 category members were checked: 3 missing/non-book entries, 274 covered by title rows, and 223 AE pages handled by the AE document pass. |
| UESP Notes page | No new rows added. | 125 normal-note entries outside quest-book coverage lacked explicit `quest` or `questrel` linkage and remain out of book scope unless the checklist tracks them. |
| UESP Creation Club Books normal index | No open source-index gaps. | 216 obtainable quest/action documents are covered, 4 unavailable pre-Anniversary courier notes are excluded, and 103 unlinked generic/system documents are deferred. |
| UESP Creation Club book category | Three gaps closed. | Category-only quest-linked pages for Letter from Shogarz gro-Batul, Orders (Orcish Scaled), and Skorvild's Journal were added in this pass. |
| AE category-only spell tomes | Covered elsewhere. | 43 category-only AE spell-tome pages are covered by the spell-tome table and are not duplicated as AE book rows. |
| Aggregate/compilation pages | Not objective rows by default. | Aggregate pages such as Fishing Mastery, The Crimson Dirks, Thoron's Journal, and Log of Elberon the Great are represented by member titles where in scope; unlinked members remain checklist-dependent. |

## Aggregate And Series Handling

| Aggregate or series marker | Current treatment | Remaining action |
| --- | --- | --- |
| Fishing Mastery | No parent objective row. Member rows exist for `Fishing Mastery, v1` through `Fishing Mastery, v5` with acquisition candidates. | Route placement chooses timing and confirms quest-state safety. |
| The Crimson Dirks | No parent objective row. Source-linked member rows exist for `The Crimson Dirks, v2` through `The Crimson Dirks, v7` with acquisition candidates. | Any additional unlinked/generic member is deferred unless checklist mapping or later source work makes it in scope. |
| Thoron's Journal | No parent objective row. Member rows exist for `Thoron's Journal - Volume 1` through `Thoron's Journal - Volume 3` with acquisition candidates. | Route placement chooses timing and confirms quest-state safety. |
| Log of Elberon the Great | No parent objective row and no member row in the current source-backed book scope. | Deferred unless checklist mapping or later source work makes it in scope. |
| Titles containing non-series set words | Treated as normal title rows when the wording is part of the title, such as `Mysterious Note (Vigil Enforcer Armor Set)`. | No aggregate action required. |

## Explicit Exclusions And Deferrals

| Bucket | Treatment | Notes |
| --- | --- | --- |
| Duplicate copies | Reconciled; not separate objectives. | Duplicate copies remain location/acquisition candidates for route selection. |
| Aggregate/source-index compilation pages | Not separate objectives by default. | In-scope member titles are represented individually; out-of-scope or unlinked members remain deferred until checklist mapping or a later expansion task. |
| Unavailable pre-Anniversary AE courier notes | Excluded from required rows. | Letter from Calcelmo, Notice of Sale - Dwarven Mudcrab, Notice of Sale - Nix-Hound (Geldis), and Notice of Sale - Nix-Hound (Revus). |
| Generic non-category notes | Deferred/excluded unless checklist-tracked. | These lack explicit quest linkage in UESP member-page fields. |
| Unlinked AE system/flavor documents | Deferred unless checklist-tracked or needed by another objective category. | Some may later belong to crafting, collectible, property, pet/mount, or checklist mapping passes. |
| Checklist-tracked unique books | Pending external checklist. | The spreadsheet is not in the repository yet, so checklist-only unique book exceptions cannot be confirmed here. They must be handled during checklist mapping or a checklist-specific reconciliation pass. |

## Follow-Up

TB-007B5 is complete. Later route placement must choose actual acquisition candidates, and checklist mapping must re-open this file if the external spreadsheet tracks a book/note title not already represented here. TB-007G should still catch any aggregate parent/set rows introduced by later collectible, item, or checklist work.
