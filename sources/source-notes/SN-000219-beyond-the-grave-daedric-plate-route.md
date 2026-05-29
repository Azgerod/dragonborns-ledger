# SN-000219 - Beyond the Grave Daedric Plate Route

Status: researched.

Source note ID: SN-000219

## Claim

`Beyond the Grave` should be routed as a controlled level-30 Knifepoint Ridge bundle with `Boethiah's Calling`: start from `Death of a Crimson Dirk` in Dragonsreach Dungeon, take the Falkreath graveyard clue, then enter Knifepoint Ridge only after Boethiah has opened the mine path. If Siddgeir's Falkreath bandit-leader favor assigns Knifepoint Ridge, reload `HS-FALKREATH-LAND-JOB` as bug recovery rather than trying to park and complete that bounty during Boethiah.

## Routing Relevance

TB-044 carried `OBJ-000554` and `OBJ-000714` as high-severity route-resolution rows because the guide had only held the Daedric Plate Creation for later. The same source cluster left `Bounty Hunter's Note`, `Death of a Crimson Dirk`, `Khajiit's Note`, and `The Crimson Dirks, v3` unresolved as AE document rows.

The route already reserves Knifepoint Ridge for the level-30 Boethiah route. The source check confirms that entering or clearing Knifepoint before Boethiah is risky, while the Jarl bandit-leader objective at Knifepoint can fail once Boethiah's current champion objective is active. That makes a Knifepoint assignment from Siddgeir a conflict state, not an ordinary target to park for later.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001564 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Beyond_the_Grave | 2026-05-29 | Quest start, Dragonsreach/Falkreath/Knifepoint sequence, bounty hunter target, Daedric Plate armor reward, and quest stages. |
| SRC-001565 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alternative_Armors_-_Daedric_Plate | 2026-05-29 | Creation summary, Death of a Crimson Dirk start note, content member list, and two-piece Daedric Plate package contents. |
| SRC-001566 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Death_of_a_Crimson_Dirk | 2026-05-29 | Quest-document identity and Dragonsreach Dungeon table location near the jail. |
| SRC-001567 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty_Hunter%27s_Note | 2026-05-29 | Quest-document identity and Bounty Hunter body source in Knifepoint Ridge. |
| SRC-001568 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Khajiit%27s_Note | 2026-05-29 | Quest-document identity and Falkreath Graveyard dead-Khajiit source. |
| SRC-001569 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Crimson_Dirks,_v3 | 2026-05-29 | Quest-related book identity and Dragonsreach Dungeon hallway dining-table location. |
| SRC-001570 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Knifepoint_Ridge | 2026-05-29 | Knifepoint exterior/mine layout, Boethiah mine cave-in state, clearability bugs, Siddgeir bounty conflict bug, and stuck-ramp reload risk. |
| SRC-001571 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Boethiah%27s_Calling | 2026-05-29 | Level-30 gate, sacrifice route, Knifepoint champion objective, Ebony Mail equip requirement, and Knifepoint/radiant bug warnings. |
| SRC-001572 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Daedric | 2026-05-29 | Daedric Plate armor variant identity, two-piece set composition, and armor/helmet item details. |

## Evidence Summary

UESP lists `Beyond the Grave` as the Alternative Armors - Daedric Plate quest. The quest starts in Dragonsreach Dungeon by reading `Death of a Crimson Dirk`, then sends the player to Falkreath Graveyard for `Khajiit's Note`, then to Knifepoint Ridge to defeat the bounty hunter wearing the Daedric Plate armor. The bounty hunter carries `Bounty Hunter's Note`, and the associated Creation summary lists `The Crimson Dirks, v3` as another book in the same package. The individual book pages place `Death of a Crimson Dirk` and `The Crimson Dirks, v3` in Dragonsreach Dungeon, `Khajiit's Note` by the dead Khajiit in Falkreath Graveyard, and `Bounty Hunter's Note` on the Knifepoint bounty hunter.

The Daedric page identifies Daedric Plate as a heavy-armor Creation variant consisting of Daedric Plate Armor and Daedric Plate Helmet. The quest page names the armor reward, and the Creation summary confirms the package has two armor pieces, so the guide treats both member rows as acquired and preserved when the bounty hunter is looted.

Knifepoint Ridge has unusual route constraints. The location page says the mine path is blocked by a cave-in unless `Boethiah's Calling` is active. Both the location page and the Boethiah quest page warn that clearing Knifepoint before Boethiah may prevent the quest from starting. The Knifepoint page also states that if Boethiah's champion objective is already active, the Jarl `Kill the Bandit Leader` quest at Knifepoint cannot be completed. The route therefore cannot safely solve Siddgeir's Knifepoint target by clearing it before Boethiah or by parking it until Boethiah.

## Route Decision

Keep the opening Whiterun route's existing warning: do not take `Death of a Crimson Dirk` during the first-day Whiterun pass. In the later level-30 Daedric block, first route Dragonsreach Dungeon for `Death of a Crimson Dirk` and `The Crimson Dirks, v3`, then Falkreath Graveyard for `Khajiit's Note`. Do not enter Knifepoint Ridge until `Boethiah's Calling` is active and Boethiah has sent the player there.

At Knifepoint Ridge, clear the exterior camp, kill the Daedric Plate bounty hunter, loot and preserve Daedric Plate Armor and Daedric Plate Helmet, and read/take `Bounty Hunter's Note`. Then continue into the Boethiah-opened mine path, kill Boethiah's Champion, loot the Ebony Mail, equip it from inventory when the quest stage requires it, and preserve it afterward.

For Siddgeir's Falkreath bandit-leader assignment, treat Knifepoint Ridge as a source-backed bug-conflict target. The guide uses `HS-FALKREATH-LAND-JOB` to reload and accept the next clean assignment if Siddgeir assigns Knifepoint. This is not a normal preferred-target reroll; it is a bug recovery because the source pages do not leave a safe main-route path that both preserves Boethiah and completes the Jarl bounty at Knifepoint.

This closes `OBJ-000554`, `CHK-QUESTS-0562`, `OBJ-000714`, `ITEM-000769`, `ITEM-000770`, `OBJ-001355`, `OBJ-001383`, `OBJ-001427`, `OBJ-001521`, `CHK-BOOKS-2446`, and `CHK-BOOKS-2455`.

## Confidence and Open Questions

Confidence is high for the document chain, reward handling, and Knifepoint/Boethiah conflict. The open operational caveat is live-save target assignment from Siddgeir, handled by the named bug-recovery hard save. Because PS4 has no console fallback for the documented stuck or failed bounty states, the guide should keep the reload instruction explicit.

## Linked Records

`OBJ-000554`; `OBJ-000714`; `OBJ-001355`; `OBJ-001383`; `OBJ-001427`; `OBJ-001521`; `CHK-QUESTS-0562`; `CHK-BOOKS-2446`; `CHK-BOOKS-2455`; `ITEM-000769`; `ITEM-000770`; `BOOKLOC-001598`; `BOOKLOC-001626`; `BOOKLOC-001670`; `BOOKLOC-001764`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`.
