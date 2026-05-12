# Source Note: Base/DLC Quest-Book Category Inventory

Status: needs review.

Source note ID: SN-000054

## Claim

This pass tracks base-game, Dawnguard, Hearthfire, and Dragonborn quest-book category members from UESP as title-level quest-book/note objectives. Duplicate copies are location candidates, not separate completion objectives. Titles already represented by earlier Black Book, unique quest-book, or skill-book rows are not duplicated here.

## Routing Relevance

The specification requires quest books and checklist synchronization, but the final route should not require every generic lore book. UESP's quest-book categories identify documents with quest start, quest relation, or quest-document relevance, making them appropriate source-list inventory rows before route selection. The rows added in this pass are not route instructions; exact timing, branch placement, safe acquisition, ownership, missability, bug, and Survival Mode handling remain deferred.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000186 | Category:Skyrim-Quest Books | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Quest_Books | 2026-05-11 | Base/general quest-book category inventory and member pages. |
| SRC-000208 | Category:Skyrim-Dragonborn-Quest Books | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Dragonborn-Quest_Books | 2026-05-11 | Dragonborn quest-book category inventory and member pages. |
| SRC-000187 | Skyrim:Notes | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Notes | 2026-05-11 | Broad notes index used to confirm that non-category note reconciliation remains a separate pass. |

## Evidence Summary

The UESP quest-book category and Dragonborn quest-book category were fetched through the MediaWiki API on 2026-05-11, along with each member page's `Game Book` template fields. The category/member-page pass found 497 usable category member pages after excluding three missing or non-book category entries. Of those, 223 were AE Creation pages and are deferred to TB-007B4c. Twenty-two titles were already represented by earlier book-document rows, including Black Books, Ancient Falmer translated/unknown books, Oghma Infinium, Wind and Sand, and overlapping skill-book titles.

This pass added 252 new title-level objectives: 187 base-game, 25 Dawnguard, 3 Hearthfire, and 37 Dragonborn. It also added 367 source-listed acquisition/location candidate rows. Twenty-one of those acquisition rows are provisional because the individual UESP member page lists the document as quest-related but does not provide a fixed location field.

The UESP Notes page lists broad normal-note material, including generic and non-quest notes. A quick reconciliation found that many Notes-page entries are not in the quest-book categories, so non-category notes need a separate scope review before any additional rows are added.

## Confidence and Open Questions

Confidence is high that the newly added rows reflect current UESP quest-book category membership and member-page location fields as of 2026-05-11. Confidence is lower for final route inclusion and exact acquisition timing because this pass does not review every associated quest page, branch state, NPC dependency, theft state, bug, or missability note.

Open questions include which non-category Notes-page entries are quest/checklist relevant, which category-member documents are branch-only rather than main-route, which provisional documents have acquisition details on associated quest pages, and whether any generic-looking category members should later be excluded with rationale.

## Linked Records

OBJ-001084 through OBJ-001335.

BOOKLOC-001212 through BOOKLOC-001578 in `data/books/book-document-locations.csv`.
