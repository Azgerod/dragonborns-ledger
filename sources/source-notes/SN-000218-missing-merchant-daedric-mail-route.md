# SN-000218 - Missing Merchant Daedric Mail Route

Status: researched.

Source note ID: SN-000218

## Claim

`Missing Merchant` can be safely routed from the Windhelm follow-up block by taking the Candlehearth Hall innkeeper start, clearing Traitor's Post, collecting the quest documents and Ring of Masser, then buying the Daedric Mail armor set from Ma'dran for 5,000 gold instead of trading away the unique ring.

## Routing Relevance

TB-044 carried `OBJ-000553` and `OBJ-000713` as high-severity route-resolution rows because the guide only had package-level Alternative Armors - Daedric Mail coverage and no quest-page route, reward choice, or preservation state. The same source cluster left `Letter from Edward`, `Missing Merchant`, `Erwan's Journal`, and `The Crimson Dirks, v5` unresolved as AE document rows.

The existing Windhelm follow-up already starts from Candlehearth Hall and then routes Eastmarch roads, so the innkeeper start and Traitor's Post can be handled there before the broader Eastmarch support chain continues. The later Winterhold coast sweep no longer needs to clear Traitor's Post or take `Treasure Map VII`.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001552 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Missing_Merchant | 2026-05-29 | Quest giver, Windhelm and Traitor's Post route, Erwan/Gunther/Ma'dran progression, armor purchase or ring-trade choice, reward, and quest stages. |
| SRC-001553 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alternative_Armors_-_Daedric_Mail | 2026-05-29 | Creation summary, Candlehearth start note, content member list, and Daedric Mail package contents. |
| SRC-001554 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Traitor%27s_Post | 2026-05-29 | Traitor's Post location east of Windhelm, clearable state, bandit occupants, bear-trap warning, and Treasure Map VII chest. |
| SRC-001555 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ma%27dran | 2026-05-29 | Ma'dran caravan route between Windhelm and Solitude and `Missing Merchant` quest dialogue, including the 5,000-gold purchase option. |
| SRC-001556 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Erwan | 2026-05-29 | Erwan's Traitor's Post role, hostile state, journal and Letter from Edward inventory, and required journal reading. |
| SRC-001557 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Gunther | 2026-05-29 | Gunther's corpse placement, Ring of Masser, and The Crimson Dirks, v5 inventory. |
| SRC-001558 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Erwan%27s_Journal | 2026-05-29 | Erwan's Journal identity and quest text supporting the Ma'dran/Ring of Masser progression. |
| SRC-001559 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Letter_from_Edward | 2026-05-29 | Letter from Edward identity and `Missing Merchant` quest association. |
| SRC-001560 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Missing_Merchant_(note) | 2026-05-29 | Missing Merchant note identity, quest association, and courier or Candlehearth Hall innkeeper acquisition. |
| SRC-001561 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Crimson_Dirks,_v5 | 2026-05-29 | The Crimson Dirks, v5 identity and Gunther quest-related source. |
| SRC-001562 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Daedric | 2026-05-29 | Daedric Mail armor-piece stats, three-piece set behavior, and no Daedric Mail helmet. |
| SRC-001563 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ring_of_Masser | 2026-05-29 | Ring of Masser identity, Gunther source, exchange-or-keep choice, enchantment, and no-disenchant state. |

## Evidence Summary

UESP lists `Missing Merchant` as the Alternative Armors - Daedric Mail quest. The quest can start by speaking to the Candlehearth Hall innkeeper for work or by receiving the note from a courier. The route chooses the innkeeper start because the guide is already at Candlehearth Hall for nearby AE quest starts. The quest sends the player to Traitor's Post, east of Windhelm, where Erwan and her bandits are hostile.

The quest page directs the player to kill Erwan, obtain and read `Erwan's Journal`, recover the Ring of Masser from Gunther's corpse, and track down Ma'dran. Erwan's NPC page confirms she carries her journal and `Letter from Edward`. Gunther's NPC page confirms the Ring of Masser and `The Crimson Dirks, v5` are on his corpse. The note page confirms `Missing Merchant` is the Candlehearth/courier start document.

Ma'dran's page places his caravan outside Windhelm or Solitude or traveling between them, and his quest dialogue includes a 5,000-gold purchase option. The quest page says the Ring of Masser can be traded for the armor or the player can pay 5,000 gold. Because the project preserves unique items, the route keeps the Ring of Masser and buys the Daedric Mail set. The Daedric page identifies the armor set as Daedric Mail, Daedric Mail Boots, and Daedric Mail Gauntlets, with no Daedric Mail helmet.

Traitor's Post is clearable and also contains `Treasure Map VII` in a novice-locked chest, so the guide takes it during this quest pass and removes the stale later Traitor's Post pickup from the Winterhold coast sweep.

## Route Decision

Insert the full route in `Windhelm Follow-Up and Eastmarch Roads` after the `Rise in the East` turn-in and before the existing Candlehearth AE book starts. The guide keeps 5,000 gold liquid, asks the Candlehearth innkeeper for work, reads/takes `Missing Merchant`, reads/takes the adjacent AE quest books, clears Traitor's Post, reads/takes `Erwan's Journal`, `Letter from Edward`, and `The Crimson Dirks, v5`, takes the Ring of Masser and `Treasure Map VII`, then follows the active marker to Ma'dran and buys the Daedric Mail set for 5,000 gold.

This closes `OBJ-000553`, `CHK-QUESTS-0649`, `OBJ-000713`, `ITEM-000765`, `ITEM-000766`, `ITEM-000767`, `ITEM-000768`, `OBJ-001432`, `OBJ-001462`, `OBJ-001523`, `CHK-BOOKS-2448`, and `CHK-BOOKS-2464`.

## Confidence and Open Questions

Confidence is high for the quest route, document pickups, and reward choice. The only live-route variable is Ma'dran's exact position when the player reaches the caravan stage, so the guide follows the active quest marker rather than assuming he is standing at Windhelm Stables. The route requires 5,000 gold; the guide now states that liquid-gold requirement before accepting the quest.

## Linked Records

`OBJ-000553`; `OBJ-000713`; `OBJ-001432`; `OBJ-001462`; `OBJ-001523`; `CHK-QUESTS-0649`; `CHK-BOOKS-2448`; `CHK-BOOKS-2464`; `ITEM-000765`; `ITEM-000766`; `ITEM-000767`; `ITEM-000768`; `BOOKLOC-001675`; `BOOKLOC-001705`; `BOOKLOC-001766`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`.
