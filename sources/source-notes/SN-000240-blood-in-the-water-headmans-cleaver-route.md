# Blood in the Water Headman's Cleaver Route

Status: researched.

Source note ID: SN-000240

## Claim

The guide should route `Blood in the Water` from the existing Candlehearth Hall/Eastmarch support window before clearing Lost Knife Hideout.

For this route:

- Ask the Windhelm innkeeper for work until the player receives `Letter from Shogarz gro-Batul`.
- Read and take the letter to start `Blood in the Water`.
- Do not clear Lost Knife Hideout before the quest is active.
- At Lost Knife Hideout, clear Lost Knife Cave and Lost Knife Hideout as one dungeon route.
- In the arena/cage area, defeat the Darkwater Snake and the Greencap Bandits.
- Loot the Darkwater Snake for Headman's Cleaver. Read and take `Urzog's Journal` from the Darkwater Snake or the nearby arena/cage tables before leaving.
- Loot Shogarz gro-Batul's corpse for `Shogarz's Journal`; read and take it.
- Preserve Headman's Cleaver in owned storage after the quest is complete.

## Routing Relevance

This closes `OBJ-000623` `Blood in the Water`, `OBJ-000754` `Headman's Cleaver Unique Weapon`, `OBJ-001504` `Shogarz's Journal`, `OBJ-001541` `Urzog's Journal`, `OBJ-001552` `Letter from Shogarz gro-Batul`, checklist rows `CHK-QUESTS-0602`, `CHK-BOOKS-2527`, and `CHK-BOOKS-2541`, and item row `ITEM-000812`.

It also upgrades the existing Lost Knife Hideout clear from a broad Eastmarch-road dungeon clear to an active quest route. This avoids the source-listed bug risk where the letter can fail to appear if a same-camp radiant for Lost Knife Hideout was completed before receiving the letter.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001782 | Skyrim:Blood in the Water | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Blood_in_the_Water | 2026-05-29 | Used for innkeeper start, letter read, Lost Knife route, Darkwater Snake target, Headman's Cleaver reward, Shogarz/Urzog journal pickups, completion boundary, and same-camp radiant bug. |
| SRC-001783 | Skyrim:Headman's Cleaver | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Headman%27s_Cleaver | 2026-05-29 | Used for Creation package context, official summary, content membership, quest name, item, books, NPCs, and innkeeper start summary. |
| SRC-001784 | Skyrim:Headman's Cleaver (item) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Headman%27s_Cleaver_(item) | 2026-05-29 | Used for artifact identity, battleaxe stats, Blood in the Water acquisition, tempering, and preservation treatment. |
| SRC-001785 | Skyrim:Letter from Shogarz gro-Batul | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Letter_from_Shogarz_gro-Batul | 2026-05-29 | Used for letter identity, quest relation, and note text context. The individual page has no fixed location field, so the innkeeper source comes from the quest page. |
| SRC-001786 | Skyrim:Shogarz's Journal | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shogarz%27s_Journal | 2026-05-29 | Used for Shogarz's Journal source on Shogarz's corpse and quest relation. |
| SRC-001787 | Skyrim:Urzog's Journal | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Urzog%27s_Journal | 2026-05-29 | Used for Urzog's Journal source on the Darkwater Snake and quest relation. |
| SRC-001788 | Skyrim:Lost Knife Hideout | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lost_Knife_Hideout | 2026-05-29 | Used for Lost Knife Cave/Hideout structure, Eastmarch location, clearable status, related Blood in the Water quest, and route hazards. |
| SRC-001789 | Skyrim:Shogarz gro-Batul | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shogarz_gro-Batul | 2026-05-29 | Used for dead Shogarz NPC identity, Lost Knife Hideout location, carried journal, and name-prefix correction. |

## Evidence Summary

UESP's `Blood in the Water` page lists any innkeeper as giver, with Lost Knife Hideout as the quest location and Headman's Cleaver as the reward. The detailed walkthrough says an innkeeper hands the player the letter, the player reads it, then travels through Lost Knife Cave and Lost Knife Hideout to the cage/arena area. There, the Darkwater Snake carries the stolen cleaver, the quest page places `Urzog's Journal` on one of the tables, the individual journal page says the Darkwater Snake carries it, and Shogarz gro-Batul's body provides `Shogarz's Journal`.

The same quest page records the quest stages: ask an innkeeper for work, read the letter, eliminate the bandits in Lost Knife Hideout, retrieve Headman's Cleaver, and finish when the cleaver is recovered. It also records a bug where the letter may not appear after getting the quest if a radiant quest for the same bandit camp was completed before receiving the letter. The guide therefore starts `Blood in the Water` before the Lost Knife clear instead of treating Lost Knife as a generic Eastmarch dungeon.

The individual item and document pages support the title-level route: Headman's Cleaver is a battleaxe artifact acquired through `Blood in the Water`; `Shogarz's Journal` is found on Shogarz's corpse; `Urzog's Journal` is carried by the Darkwater Snake; and `Letter from Shogarz gro-Batul` is a quest note for `Blood in the Water`. The individual letter page has no fixed `loc` field, so its deterministic acquisition source is the quest-page innkeeper handoff.

## Confidence and Open Questions

Confidence is high for the innkeeper start, letter read, Lost Knife route, Darkwater Snake target, cleaver reward, Shogarz/Urzog journal pickups, and unique-item preservation treatment.

Confidence is high that the route should activate the quest before the Lost Knife clear because the quest page records a same-camp radiant bug. The guide should also continue to avoid accepting random bandit-camp radiants for Lost Knife before this route.

There is no remaining open route question for `Blood in the Water` in the current guide.

## Linked Records

OBJ-000623; OBJ-000754; OBJ-001504; OBJ-001541; OBJ-001552; OBJ-002087; CHK-QUESTS-0602; CHK-BOOKS-2527; CHK-BOOKS-2541; CHK-LOCATIONS-1131; BOOKLOC-001747; BOOKLOC-001784; BOOKLOC-001795; ITEM-000812; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/books/book-document-locations.csv`; `data/items/ae-item-members.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
