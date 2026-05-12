# Source Note: Book Document Reconciliation

Status: needs review.

Source note ID: SN-000057

## Claim

The current book/document source indexes have been reconciled against the objective database. The reconciliation found three additional obtainable AE quest-related documents that were present in `Category:Skyrim-Creation Club-Books` but absent from the normal `Skyrim:Creation Club Books` index: Letter from Shogarz gro-Batul, Orders (Orcish Scaled), and Skorvild's Journal.

The follow-up placeholder and duplicate-copy reconciliation found no remaining aggregate placeholder objective rows, no duplicate normalized `book_document` objective names, and no `book_document` objective row without at least one acquisition/location row. Duplicate physical copies and alternate acquisition paths remain route candidates only.

## Routing Relevance

The specification requires quest/AE books and checklist-tracked unique books, while excluding every copy of every book and generic notes by default. This reconciliation confirms source-index coverage and duplicate-copy handling before route placement. It also records which buckets are intentionally deferred because they require either the external checklist or later non-book objective passes.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000182 | Skyrim:Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Books | 2026-05-11 | Overall book-category scope. |
| SRC-000183 | Skyrim:Skill Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skill_Books | 2026-05-11 | Skill-book title count and duplicate-copy handling. |
| SRC-000184 | Category:Skyrim-Books-Spell Tomes | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Books-Spell_Tomes | 2026-05-11 | Spell-tome page inventory. |
| SRC-000186 | Category:Skyrim-Quest Books | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Quest_Books | 2026-05-11 | Base/general quest-book category inventory. |
| SRC-000187 | Skyrim:Notes | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Notes | 2026-05-11 | Normal-note reconciliation. |
| SRC-000188 | Skyrim:Creation Club Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Creation_Club_Books | 2026-05-11 | AE normal-book index. |
| SRC-000199 | Category:Skyrim-Creation Club-Books-Spell Tomes | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Creation_Club-Books-Spell_Tomes | 2026-05-11 | AE spell-tome exclusion from AE document rows. |
| SRC-000208 | Category:Skyrim-Dragonborn-Quest Books | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Dragonborn-Quest_Books | 2026-05-11 | Dragonborn quest-book category inventory. |
| SRC-000209 | Category:Skyrim-Creation Club-Books | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Creation_Club-Books | 2026-05-11 | AE category cross-check. |
| SRC-000210 | Skyrim:Letter from Shogarz gro-Batul | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Letter_from_Shogarz_gro-Batul | 2026-05-11 | Category-only Headman's Cleaver quest-linked note. |
| SRC-000211 | Skyrim:Orders (Orcish Scaled) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Orders_(Orcish_Scaled) | 2026-05-11 | Category-only Orcish Scaled quest-related note. |
| SRC-000212 | Skyrim:Skorvild's Journal | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skorvild%27s_Journal | 2026-05-11 | Category-only The Cause quest-linked journal. |

## Evidence Summary

The reconciled book/document objective set now contains title-level rows for 90 skill books, 154 accessible spell tomes, 7 Black Books, 4 unique book/scroll artifacts, 261 base/DLC quest-book titles, and 219 AE book/document titles.

The UESP quest-book category and Dragonborn quest-book category contain 500 category members. Three were missing or non-book category entries, 274 are now covered by existing title rows, and 223 AE Creation pages were handled by the AE document pass and this reconciliation. No base/DLC quest-book category gaps remain.

The UESP Notes page contains 265 normal-note entries. After removing titles already covered by quest-book categories and existing book-document rows, 125 non-category notes remain deferred because they lack explicit `quest` or `questrel` linkage on their member pages.

The UESP Creation Club Books normal-book index contains 323 rows. Of those, 216 obtainable quest/action documents are covered, four unavailable pre-Anniversary courier notes are excluded, and 103 unlinked generic/system documents remain deferred until checklist reconciliation.

The broader UESP Creation Club book category contains 53 members not present in the normal-book index. Forty-three are AE spell-tome pages already covered by the spell-tome table. Seven are aggregate or unlinked compilation pages whose member titles are either already covered or deferred. Three category-only quest-linked documents were missing and are now added by this reconciliation.

The local table reconciliation now has 735 `book_document` objective rows and 1,797 acquisition/location rows across the three book tables: 474 skill-book copy rows, 716 spell-tome acquisition rows, and 607 Black Book, quest-book, unique-book, and AE-document acquisition rows. Every `book_document` title row has acquisition/location coverage. The 215 title rows with more than one acquisition candidate are intentional duplicate-copy or alternate-source cases, not separate completion objectives.

Aggregate and series markers are handled at member-title level where in scope. Fishing Mastery has member rows for volumes 1-5, The Crimson Dirks has source-linked member rows for volumes 2-7, and Thoron's Journal has member rows for volumes 1-3. Log of Elberon the Great and any unlinked/generic series members remain deferred unless checklist mapping or later source work makes them in scope.

## Confidence and Open Questions

Confidence is high for source-index coverage across UESP book categories and index pages as of 2026-05-11. Confidence is lower for checklist-only unique books because the external completion checklist is not yet present in the repository.

Open questions include whether the checklist tracks any generic normal-note or AE system-document titles that are not quest-linked, whether any deferred aggregate or series member titles should be promoted during checklist mapping, and whether provisional no-location rows can be resolved from associated quest pages during later constraint and route validation.

## Linked Records

OBJ-001552 through OBJ-001554.

BOOKLOC-001795 through BOOKLOC-001797 in `data/books/book-document-locations.csv`.

`data/books/book-document-reconciliation.md`.
