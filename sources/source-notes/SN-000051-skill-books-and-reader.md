# Source Note: Skill Books and Reader Trophy

Status: needs review.

Source note ID: SN-000051

## Claim

Skyrim has 90 unique skill book titles: five for each of the 18 skills. The maximalist guide should account for reading one copy of every unique skill book title, while duplicate copies of the same title are not required. The Reader trophy requires reading 50 skill books.

## Routing Relevance

The specification includes skill books, checklist synchronization, all skills to 100, and PS4 trophies. Skill book timing matters because reading a title immediately grants its skill increase when the book is opened. This pass creates one objective row per unique skill book title plus a Reader trophy target row. It also records all source-listed copy locations in `data/books/skill-books-locations.csv` so later route placement can choose the best copy without treating duplicate copies as separate objectives.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000183 | Skyrim:Skill Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skill_Books | 2026-05-11 | Identifies 90 skill books, five per skill, mechanics, Reader trophy context, duplicate-copy behavior, location table, and bug notes. |
| SRC-000182 | Skyrim:Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Books | 2026-05-11 | Supports book-category scope and confirms skill books as a tracked book category. |
| SRC-000002 | Skyrim:Achievements | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Achievements | 2026-05-11 | Supports Reader trophy naming and trophy context. |

## Evidence Summary

UESP states that skill books permanently increase a skill by one point and that there are five different skill books for each of Skyrim's 18 skills, for 90 total unique titles. UESP's Skill Books page also provides a source-listed location table. The objective rows expose title-level coverage with generic all-location pointers, while `data/books/skill-books-locations.csv` records 474 source-listed copy locations for route-selection analysis.

## Confidence and Open Questions

Confidence is high for the 90-title inventory, the 474 source-listed copy-location rows, and the Reader trophy target. Open questions include the preferred copy for each title, whether any copy is locked behind quest or faction state, theft ownership, follower retrieval quirks, bug handling, and whether the route should delay reading certain skill books for leveling efficiency.

## Linked Records

OBJ-000819 through OBJ-000909.

`data/books/skill-books-locations.csv`.
