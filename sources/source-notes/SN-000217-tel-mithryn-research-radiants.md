# SN-000217 - Tel Mithryn Research Radiants

Status: researched.

Source note ID: SN-000217

## Claim

Neloth's `Azra's Staffs`, `Experimental Subject (B)`, and `Wind and Sand` chain can be closed in a controlled Tel Mithryn research block after `Reluctant Steward`, `Briarheart Necropsy`, and `Old Friends` are stable. `Azra's Staffs` and `Wind and Sand` use random dungeon targets, so the guide should respect the active marker instead of manipulating RNG. The route should make one hard save before accepting the research block to protect source-listed inaccessible-target bugs, not to reroll ordinary assignments.

## Routing Relevance

TB-038R carried `OBJ-000440`, `OBJ-000452`, `OBJ-000451`, and `OBJ-001083` forward because the previous Tel Mithryn/Nchardak section deliberately left Neloth's later research work unstarted. The open risk was not geography alone; it was the interaction of Azra's random target, Experimental Subject's prerequisite chain, Wind and Sand's Destruction 40 gate, the Wind and Sand book/document row, and Whirlwind Cloak's postquest Talvas vendor unlock.

The route now handles these as one bounded research block. If Destruction is already 40, the player completes the full chain before leaving Tel Mithryn's research surface. If Destruction is below 40, the guide gives an explicit return instruction before the Books, Spells, and Documents vendor pass, so the Whirlwind Cloak purchase is not treated as available before `Wind and Sand`.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001547 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Azra%27s_Staffs | 2026-05-29 | Azra's Staffs prerequisite, random boss-container target pool, reward, repeatability, map-marker bug, and inaccessible-dungeon bug. |
| SRC-001548 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Experimental_Subject_(B) | 2026-05-29 | Experimental Subject (B) prerequisite, Neloth spell experiment, blindness/stamina effect, 250-gold reward, and black-screen bug workaround. |
| SRC-001549 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Wind_and_Sand_(quest) | 2026-05-29 | Wind and Sand prerequisites, Destruction 40 gate, radiant target pool, book retrieval, 250-gold reward, and Talvas restock unlock for Whirlwind Cloak. |
| SRC-001550 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Wind_and_Sand_(book) | 2026-05-29 | Wind and Sand book identity, item ID, quest association, value/weight, and blank fixed-location field. |
| SRC-001551 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Whirlwind_Cloak | 2026-05-29 | Whirlwind Cloak tome ID, Talvas purchase source, post-Wind-and-Sand condition, no-loot status, and spell notes. |

## Evidence Summary

UESP lists `Azra's Staffs` as a Neloth side quest with quest ID `DLC2TTR7`. Its prerequisite is after speaking to Neloth during `Reluctant Steward`, except while finding him a new steward, and not while `Briarheart Necropsy` is active. The quest sends the player to a specified dungeon to retrieve a staff made by Azra Nightwielder, then return it to Neloth for a random generic staff. The detailed walkthrough says the target is radiant and can be on Solstheim or mainland Skyrim. The notes define the eligible target categories and state that only locations with boss containers are chosen. The bugs section warns about mainland-Skyrim map-marker behavior and the possibility that the quest may choose a dungeon with a section that became inaccessible after an earlier clear.

UESP lists `Experimental Subject (B)` as a Neloth miscellaneous objective with `Azra's Staffs` as prerequisite and a 250-gold reward. The player lets Neloth cast the experimental silence spell, is blinded briefly while stamina drains, then can demand payment after the effect ends. The bug note records a possible black-screen state after the conversation and points to opening a Black Book as a workaround.

UESP lists `Wind and Sand` as a Neloth side quest with `Old Friends` and `Experimental Subject` as previous quests and Destruction 40 as a prerequisite. The quest sends the player to a radiant target to retrieve the book `Wind and Sand`; the eligible target categories are dragon lairs, dragon priest lairs, draugr crypts, Falmer hives, Forsworn camps, hagraven nests, vampire lairs, and warlock lairs. On return, Neloth gives 250 gold and Whirlwind Cloak becomes available for purchase the next time Talvas restocks. The book page confirms the title is quest-related but has no fixed location field, so the book/document row is closed through the quest retrieval rather than through an independent fixed pickup. The Whirlwind Cloak page lists Talvas Fathryon as the purchase source and conditions the tome on `Wind and Sand`.

## Route Decision

Insert a controlled Neloth research block after `Old Friends` in `Tel Mithryn, Nchardak, and Kagrumez`. Make `HARD SAVE: HS-TEL-MITHRYN-RESEARCH-RADIANTS`, accept `Azra's Staffs`, follow the assigned marker directly, retrieve the staff from the boss-container/quest-marker target, and return it to Neloth. If the target is inaccessible because of an earlier clear-state bug, reload the hard save and record that target as bug recovery. This save is not a normal target-selection reroll.

After the Azra return, accept and complete `Experimental Subject (B)` locally. Then, if Destruction is at least 40, accept and complete `Wind and Sand` using the same isolated active-marker rule. If Destruction is below 40, the player records an explicit return instruction and completes `Wind and Sand` before the later Books, Spells, and Documents vendor pass. After `Wind and Sand`, buy/read `Spell Tome: Whirlwind Cloak` from Talvas after his next restock, either immediately in Tel Mithryn or during the later vendor pass.

This closes `OBJ-000440`, `CHK-QUESTS-0549`, `OBJ-000452`, `CHK-QUESTS-0552`, `OBJ-000451`, `CHK-QUESTS-0561`, `OBJ-001083`, `CHK-BOOKS-2429`, `OBJ-001007`, `CHK-SPELLS-0783`, and `CHK-BOOKS-2382`.

## Confidence and Open Questions

Confidence is medium-high. The quest prerequisites, target pools, rewards, and vendor gate are source-backed. The remaining uncertainty is the actual random dungeon assignment in a live playthrough, so the route uses a hard save and active-marker branch rather than naming a false deterministic target. The unreachable-target case is explicitly treated as bug recovery.

## Linked Records

`OBJ-000440`; `OBJ-000451`; `OBJ-000452`; `OBJ-001083`; `OBJ-001007`; `CHK-QUESTS-0549`; `CHK-QUESTS-0552`; `CHK-QUESTS-0561`; `CHK-BOOKS-2429`; `CHK-SPELLS-0783`; `CHK-BOOKS-2382`; `BOOKLOC-001211`; `BOOKLOC-000962`; `PROGSEL-000188`; `HS-TEL-MITHRYN-RESEARCH-RADIANTS`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`; `data/guide-coverage/main-guide-v1-order-delayed-task-repair.csv`.
