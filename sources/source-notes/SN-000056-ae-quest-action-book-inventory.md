# Source Note: AE Quest and Action Book Inventory

Status: needs review.

Source note ID: SN-000056

## Claim

This pass tracks obtainable Anniversary Edition Creation Club books, notes, journals, ledgers, lists, and related documents that UESP explicitly links to an AE quest or quest-related system through `quest` or `questrel` fields on the member page. It adds one title-level objective per document and one source-listed acquisition candidate per title. Duplicate copies are route candidates, not separate completion objectives.

## Routing Relevance

The specification requires all official AE Creation Club quests, systems, items, spells, ingredients, and rewards, plus quest/AE books. This source-list pass gives the AE document layer title-level coverage without drafting route prose or deciding final route timing. It also prevents generic AE flavor notes, already-covered AE spell tomes, and unavailable pre-Anniversary courier notes from being treated as required objectives by default.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000188 | Skyrim:Creation Club Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Creation_Club_Books | 2026-05-11 | Main AE normal-book index and member-page `Game Book` fields. |
| SRC-000209 | Category:Skyrim-Creation Club-Books | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Creation_Club-Books | 2026-05-11 | Category cross-check, including category-only spell-tome and aggregate pages. |
| SRC-000199 | Category:Skyrim-Creation Club-Books-Spell Tomes | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Creation_Club-Books-Spell_Tomes | 2026-05-11 | Used to confirm AE spell tomes are already covered by the spell-tome pass, not duplicated here. |

## Evidence Summary

UESP's Creation Club Books page currently lists 323 normal book/note rows. Fetching each member page's `Game Book` fields found 220 quest-linked entries. Four of those quest-linked entries are excluded from required objective rows because their location text says they are unavailable or were only obtainable before the Anniversary Edition update: Letter from Calcelmo, Notice of Sale - Dwarven Mudcrab, Notice of Sale - Nix-Hound (Geldis), and Notice of Sale - Nix-Hound (Revus).

This pass adds 216 obtainable AE quest/action document title rows and 216 acquisition candidate rows. Fourteen acquisition rows are provisional because the individual UESP member page has quest linkage but no fixed location field. The remaining 103 normal-book entries on the Creation Club Books page have no explicit `quest` or `questrel` field and are deferred to checklist reconciliation rather than assumed required.

The broader Creation Club book category contains 375 members. The 53 category members not present in the normal-book index are mainly the category page itself, aggregate pages, and AE spell-tome pages. AE spell-tome title objectives and acquisition candidates are already covered in TB-007B3 and are not duplicated here.

## Confidence and Open Questions

Confidence is high for the source-list inventory and the unavailable-note exclusions under UESP's current page structure. Final route inclusion, route timing, branch placement, courier timing, ownership/theft state, bug risk, cell-entry risk, and Survival Mode implications remain unvalidated.

Open questions include whether any of the 103 unlinked AE documents are tracked by the external checklist, whether any provisional no-location rows need associated quest-page data, and whether individual Creation package pages identify additional checklist-relevant documents that are not present on the Creation Club Books index.

## Linked Records

OBJ-001336 through OBJ-001551.

BOOKLOC-001579 through BOOKLOC-001794 in `data/books/book-document-locations.csv`.
