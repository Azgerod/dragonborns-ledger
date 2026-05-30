# SN-000256 - Become Ethereal Closeout

Status: targeted TB-044 route-resolution source note.

## Scope

This note closes `OBJ-000764` Become Ethereal by tying all three words to already routed dungeon and regional passes. It also closes the linked `Coming of Age`, Ironbind Barrow, Lost Valley Redoubt, Steel Battleaxe of Fiery Souls, and `Letter to Beem-Ja` rows that naturally resolve during the same Ironbind route.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000782 | Skyrim:Become Ethereal | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Become_Ethereal | 2026-05-30 | Word identities, translations, word-wall locations, Ustengrav quest-lock note, and Paarthurnax Feim meditation caveat. |
| SRC-000769 | Skyrim:Ustengrav | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ustengrav | 2026-05-30 | Ustengrav non-clearable state, Horn quest access, and Become Ethereal word-wall route. |
| SRC-000766 | Skyrim:The Horn of Jurgen Windcaller | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Horn_of_Jurgen_Windcaller | 2026-05-30 | Main-quest route through Ustengrav, waterfall word wall, and missed-word return caveat. |
| SRC-000308 | Skyrim:Coming of Age | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Coming_of_Age | 2026-05-30 | Ironbind quest start, Salma/Beem-Ja escort, Gathrik fight, Beem-Ja betrayal, Steel Battleaxe handling, word wall, and save/bug warnings. |
| SRC-001868 | Skyrim:Ironbind Barrow | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ironbind_Barrow | 2026-05-30 | Clearable location state, occupants, Become Ethereal word wall, Steel Battleaxe placement, Gathrik chamber layout, and local bugs. |
| SRC-001869 | Skyrim:Lost Valley Redoubt | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lost_Valley_Redoubt | 2026-05-30 | Clearable location state, Forsworn/hagraven route, Briarheart ritual, Bard's Leap proximity, Become Ethereal word wall, and word-wall bug. |
| SRC-000289 | Skyrim:Steel Battleaxe of Fiery Souls | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Steel_Battleaxe_of_Fiery_Souls | 2026-05-30 | Unique-item status, Ironbind throne placement, Fiery Soul Trap source note, Salma Disarm risk, and high-level physics bug. |
| SRC-001870 | Skyrim:Letter to Beem-Ja | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Letter_to_Beem-Ja | 2026-05-30 | Quest-document identity, `Coming of Age` relation, and Beem-Ja carrier. |
| SRC-001871 | Skyrim:Letter to Salma | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Letter_to_Salma | 2026-05-30 | Quest-document identity, `Coming of Age` relation, and Salma carrier for the remaining document-policy gap. |

## Route Decisions

UESP maps Become Ethereal to Feim at Ironbind Barrow, Zii at Lost Valley Redoubt, and Gron at Ustengrav. Ustengrav remains correctly placed during `The Horn of Jurgen Windcaller`: most of the ruin is inaccessible before that quest, the waterfall word wall is on the Horn route, and the current guide already learns Become Ethereal: Gron there.

Lost Valley Redoubt is already routed in the Reach road sweep, but the guide only said to clear the location. This pass makes the word-wall action explicit: fight through to the upper aqueduct and hagraven platform, defeat the hagravens and any raised Briarheart, learn Become Ethereal: Zii, loot the boss chest, and clear the redoubt. Because the source records a confirmed Lost Valley word-wall bug, the guide adds a rotating manual save before the final climb.

Ironbind Barrow is already routed in the Pale/Nightgate pass, but the guide only said to clear it. This pass expands the route into the `Coming of Age` encounter. The guide speaks to Salma at the exterior camp, escorts Salma and Beem-Ja through the dungeon, saves before Gathrik's chamber, takes Steel Battleaxe of Fiery Souls from behind the throne before Salma can be disarmed into it, defeats Gathrik, learns Become Ethereal: Feim, loots the boss chest, kills Beem-Ja after his betrayal, loots and reads `Letter to Beem-Ja`, speaks to Salma, clears Ironbind Barrow, and preserves the battleaxe under the unique-item policy.

The Steel Battleaxe of Fiery Souls remains preserved. It is the only known source item for Fiery Soul Trap, but the project has already excluded Fiery Soul Trap from main-route learning because learning it would require destroying a unique item. This closeout therefore acquires the battleaxe as unique gear and does not change the enchantment-learning exclusion.

`Letter to Beem-Ja` closes because Beem-Ja becomes hostile and must be killed in the normal `Coming of Age` route. `Letter to Salma` does not close in this pass. The source confirms Salma carries the letter, but a safe main-continuity acquisition method is not selected here; the remaining row needs an explicit pickpocket, branch, or exclusion decision before the route can require it.

Unlocking or using Become Ethereal still depends on the route's dragon-soul pool. Paarthurnax's Feim meditation and the Eternal Spirit ability remain separate later-route concerns.

## Coverage Summary

This pass closes `OBJ-000764`, `OBJ-002756`, `OBJ-002078`, `OBJ-002090`, `OBJ-001618`, and `OBJ-001203`; checklist rows `CHK-DRAGON-SHOUTS-0892`, `CHK-DRAGON-SHOUTS-0893`, `CHK-DRAGON-SHOUTS-0894`, `CHK-QUESTS-0211`, `CHK-LOCATIONS-1111`, `CHK-LOCATIONS-1135`, and `CHK-UNIQUE-GEAR-1691`; and the guide-level unresolved rows for Become Ethereal, Coming of Age, and Letter to Beem-Ja. It leaves `OBJ-001205` Letter to Salma unresolved with a narrower source-checked policy note.

## Linked Records

OBJ-000764; OBJ-002756; OBJ-002078; OBJ-002090; OBJ-001618; OBJ-001203; OBJ-001205; CHK-DRAGON-SHOUTS-0892; CHK-DRAGON-SHOUTS-0893; CHK-DRAGON-SHOUTS-0894; CHK-QUESTS-0211; CHK-LOCATIONS-1111; CHK-LOCATIONS-1135; CHK-UNIQUE-GEAR-1691; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/locations/location-catalog.csv`; `data/books/book-document-locations.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
