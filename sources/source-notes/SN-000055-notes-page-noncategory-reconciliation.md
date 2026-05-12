# Source Note: Notes Page Non-Category Reconciliation

Status: needs review.

Source note ID: SN-000055

## Claim

No new base-game or official DLC book/document objective rows are added from the `Skyrim:Notes` entries that are outside the existing quest-book category inventory. The remaining entries do not have explicit UESP `quest` or `questrel` linkage on their `Game Book` pages and should not be promoted into required quest-book objectives without checklist evidence.

## Routing Relevance

The guide specification includes quest books and checklist-tracked unique books, but it does not require every generic note. This reconciliation prevents generic environmental notes, random encounter documents, home-system letters, and unobtainable/generated note pages from expanding the completion scope beyond the specification. If the external completion checklist later tracks one of these titles directly, TB-007B4d can add it with checklist-specific rationale.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000187 | Skyrim:Notes | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Notes | 2026-05-11 | Notes-page index and member-page `Game Book` fields. |
| SRC-000186 | Category:Skyrim-Quest Books | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Quest_Books | 2026-05-11 | Used to identify notes/books already covered by the quest-book category pass. |
| SRC-000208 | Category:Skyrim-Dragonborn-Quest Books | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Dragonborn-Quest_Books | 2026-05-11 | Used to identify Dragonborn quest documents already covered by the quest-book category pass. |

## Evidence Summary

The UESP Notes page listed 265 normal-note entries. After removing titles already covered by UESP quest-book categories or existing book-document rows, 125 entries remained for this reconciliation. Their source-content split was 82 base game, 23 Dragonborn, 12 Dawnguard, 6 Hearthfire, and 2 missing/generated pages.

The remaining 125 entries had no `quest` or `questrel` field on their fetched member pages. They fall into non-required buckets for the current book-document scope: generic environmental or faction notes, property/system documents already better represented by property or relationship objectives, random/generated encounter documents, unobtainable or missing/generated pages, and separate collectible/crafting-index material such as treasure-related notes.

Representative excluded or deferred examples include property documents such as Breezehome Furnishings and homestead charters, random/generated encounter documents such as Bounty (player) and Treasure Hunter's Note, environmental/faction notes such as A Warning and No Word Yet, and unobtainable/generated entries such as Anonymous Letter (Imperial), Anonymous Letter (Stormcloaks), and the WIKill04 letter pages.

## Confidence and Open Questions

Confidence is high that the remaining Notes-page entries are not source-listed quest books under UESP's current category and member-page structure. Confidence is lower for checklist-specific unique-note coverage because the project does not yet have the external completion checklist. Checklist reconciliation may later promote specific unique notes if the spreadsheet tracks them directly.

Open questions include whether the final checklist tracks any non-category normal notes, whether property-system documents should receive checklist cues through property rows rather than book-document rows, and whether treasure-map or recipe-related notes should be handled in collectible and crafting passes instead of this book-document pass.

## Linked Records

No new objective rows.

TB-007B4b2.
