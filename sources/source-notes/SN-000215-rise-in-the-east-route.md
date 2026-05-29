# SN-000215 - Rise In The East Route

Status: researched.

Source note ID: SN-000215

## Claim

`Rise in the East` can be closed as a controlled Windhelm-Dawnstar-Japhet bundle after the Diplomatic Immunity/Malborn follow-up. The route starts with Orthus Endario at the Windhelm East Empire Company office, steals and reads `Suvaris Atheron's Logbook`, identifies Haldyn through Stig Salt-Plank in Dawnstar, acquires `Blood Horker Orders`, sails with Adelaisa Vendicci to Japhet's Folly, kills Haldyn, returns through Adelaisa, reports to Orthus, and records Adelaisa as an available non-default follower/steward option.

## Routing Relevance

TB-038R carried `OBJ-000204` and `CHK-QUESTS-0226` as unresolved after an earlier Windhelm section staged the quest for a later East Empire/Japhet bundle. The same unresolved bundle also left `OBJ-001271`, `CHK-BOOKS-2424`, and `OBJ-001107` open. The Windhelm follow-up after `Diplomatic Immunity` already starts at Windhelm with no hard dependency on a follower and has enough route maturity for a northern island combat detour, so it is the cleanest point to close the bundle before the guide moves deeper into Eastmarch roads.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001536 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rise_in_the_East | 2026-05-28 | Quest giver, suggested level, logbook theft, Stig routes, Japhet assault sequence, reward, follower unlock, and quest bugs. |
| SRC-001537 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Japhet%27s_Folly | 2026-05-28 | Quest-only access, tower route, Haldyn/key escape path, bombardment state, containers, follower disappearance, and return/fast-travel bugs. |
| SRC-001538 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Blood_Horker_Orders | 2026-05-28 | Quest-document identity and Stig Salt-Plank carrier source. |
| SRC-001539 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Suvaris_Atheron%27s_Logbook | 2026-05-28 | Quest-document identity and Clan Shatter-Shield Office location next to the business ledger. |
| SRC-001540 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Adelaisa_Vendicci | 2026-05-28 | Adelaisa quest role, postquest follower availability, steward eligibility, and level range. |

## Evidence Summary

UESP lists `Rise in the East` as a side quest given by Orthus Endario, with Windhelm, Dawnstar, and Japhet's Folly as route locations. The quest starts in the Windhelm East Empire Company office, which is unlocked from 4am to 8pm. Orthus sends the player to steal `Suvaris Atheron's Logbook` from the Clan Shatter-Shield Office; the quest page notes a daytime unlocked-door option and a nighttime lock/key option.

The logbook points to Stig Salt-Plank at Windpeak Inn in Dawnstar. UESP records several ways to get the Japhet's Folly lead: bribing Stig, challenging him to a brawl, pickpocketing `Blood Horker Orders`, or killing him and taking the note. UESP states that attacking or killing Stig does not create a bounty or retaliation from the crew. The guide uses a hard save and a deterministic no-bounty kill/loot path for the note only after securing the quest lead, avoiding a required pickpocket check.

UESP states that Japhet's Folly can only be visited during this quest. The route must enter through the Sea Cave, kill Haldyn, loot the Japhet's Folly Key, exit through the tower path after the bombardment begins, report to Adelaisa at the docks, and use her dialogue to return to the mainland. After reporting to Orthus, the reward is leveled gold and Adelaisa becomes available as a follower.

UESP records several bug risks: do not fast travel back to Japhet's Folly after completion because the island is its own worldspace; reentering from the Sea Cave after bombardment can trap the player; pirates can get stuck under the bridge during the escape stage; Orthus/Adelaisa scene state can stall; and followers can disappear at Japhet's Folly. The guide therefore uses `HARD SAVE: HS-RISE-IN-THE-EAST`, sends away any follower/pet before boarding, avoids storing anything on the island, does not reenter the Sea Cave after Haldyn, confirms every pirate around the docks is dead before speaking to Adelaisa, and warns never to return to Japhet's Folly after completion.

## Route Decision

Insert the quest after Malborn is escorted out of Windhelm in `Windhelm Follow-Up and Eastmarch Roads`. This keeps the route based from Windhelm, resolves the earlier staged Shatter-Shield office logbook before the later Dark Brotherhood/Nilsine visit, closes Dawnstar's Stig/document step before the broader northern route, and makes Japhet's Folly a deliberate one-time island trip with a hard save.

Close `OBJ-000204`, `CHK-QUESTS-0226`, `OBJ-001271`, `CHK-BOOKS-2424`, and `OBJ-001107` in coverage and TB-038R/COV-001R repair data.

## Confidence and Open Questions

Confidence is high for the normal quest route. Residual risk remains for rare Orthus/Adelaisa scene stalls and pirate pathing during the bombardment; the route mitigates those with a prequest hard save, no follower, explicit dock sweep, and no return to the island after the quest.

## Linked Records

`OBJ-000204`; `CHK-QUESTS-0226`; `OBJ-001271`; `CHK-BOOKS-2424`; `OBJ-001107`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`; `data/guide-coverage/main-guide-v1-order-delayed-task-repair.csv`.
