# Mightier Than The Sword And Dwarven Plate Route

Status: researched.

Source note ID: SN-000221

## Claim

`Mightier than the Sword` should be routed from a Markarth support stop after `The Only Cure`, before the broader Reach cleanup loop. The player reads and takes Looter's Note at the Silver-Blood Inn, makes a pre-approach save, travels to Reachwind Eyrie, defeats the quest looters, leaves the optional `Chimarvamidium` skill-book copy closed, takes `The Crimson Dirks, v9` from Casival, reads and takes Casival's Note, then preserves Dwarven Plate Armor and Dwarven Plate Boots.

## Routing Relevance

The quest page identifies Looter's Note in the Silver-Blood Inn as the start, Reachwind Eyrie as the target, three looters as the approach fight, Casival as the body to loot, and Dwarven Plate Armor plus Dwarven Plate Boots as the remaining quest loot. The Creation page confirms that `Mightier than the Sword`, Looter's Note, Casival's Note, `The Crimson Dirks, v9`, Casival, looters, and the two Dwarven Plate items all belong to `Alternative Armors - Dwarven Plate`.

The route should not enter Reachwind Eyrie for this Creation before the Silver-Blood Inn note. UESP records a quest-break risk if the player already visited Reachwind Eyrie and picked up the Dwarven Plate Armor before activating the quest, and records a possible impossible state if the looters or bandit fail to spawn. The guide therefore starts the quest first, saves before the approach, and tells the player to reload if the expected marker or looters fail.

Reachwind Eyrie also contains a `Chimarvamidium` skill-book copy. The current selected Heavy Armor source for that title is the Septimus Signus's Outpost copy, so this pass explicitly leaves the Reachwind copy closed.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001581 | Skyrim:Mightier than the Sword | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mightier_than_the_Sword | 2026-05-29 | Used for Looter's Note start, Reachwind Eyrie target, looter fight, Casival body, reward pickup, quest stages, and bug caveats. |
| SRC-001582 | Skyrim:Alternative Armors - Dwarven Plate | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alternative_Armors_-_Dwarven_Plate | 2026-05-29 | Used for Creation summary, quest membership, book/note membership, NPC membership, and Dwarven Plate item membership. |
| SRC-001583 | Skyrim:Reachwind Eyrie | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Reachwind_Eyrie | 2026-05-29 | Used for Reachwind Eyrie location, landmark/clearability state, related quest, one-zone layout, and `Chimarvamidium` copy. |
| SRC-001584 | Skyrim:Looter's Note | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Looter%27s_Note | 2026-05-29 | Used for note identity, Silver-Blood Inn bar location, and quest association. |
| SRC-001585 | Skyrim:The Crimson Dirks, v9 | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Crimson_Dirks,_v9 | 2026-05-29 | Used for book identity, AE Creation association, and Casival body source. |
| SRC-001586 | Skyrim:Casival's Note | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Casival%27s_Note | 2026-05-29 | Used for note identity, Reachwind Eyrie location, and quest association. |
| SRC-001587 | Skyrim:Casival | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Casival | 2026-05-29 | Used for Casival's dead Reachwind Eyrie state and quest association. |
| SRC-001588 | Skyrim:Dwarven | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dwarven | 2026-05-29 | Used for Dwarven Plate Armor and Dwarven Plate Boots item names, heavy-armor classification, item IDs, weights, values, and armor ratings. |

## Evidence Summary

The player-facing route has a short boundary: read and take Looter's Note at the Silver-Blood Inn, search Reachwind Eyrie, then pick up the leftover loot at Casival's tower. Completing the quest requires the Dwarven Plate pieces near Casival, so the guide names both armor pieces and stores them as preserved unique AE armor rather than treating the quest as a generic location clear.

`The Crimson Dirks, v9` is not represented by a separate objective row in the current objective database, but the checklist maps it to `Mightier than the Sword`. The guide therefore instructs the player to loot the named book from Casival in the same moment as Casival's Note and the Dwarven Plate pieces.

The Looter NPC page was not available through the project fetch tool during this pass. The quest page itself still supplies the needed gameplay claim that three looters attack on arrival, so no separate NPC source is required for the route.

## Confidence and Open Questions

Confidence is high for the start trigger, Reachwind route, document handling, Crimson Dirks pickup, and Dwarven Plate reward preservation.

The retained risks are procedural. The guide uses a pre-approach save because UESP records possible missing enemy/objective spawns, and it warns against entering/picking up the armor before reading Looter's Note because UESP records a quest-completion bug in that state.

## Linked Records

OBJ-000529; OBJ-000558; OBJ-000718; OBJ-001377; OBJ-001449; OBJ-002331; CHK-QUESTS-0566; CHK-BOOKS-2452; CHK-LOCATIONS-1188; ITEM-000780; ITEM-000781; `drafts/final-guide/main-guide-v1.md`; `data/books/book-document-locations.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`; `data/items/ae-item-members.csv`.
