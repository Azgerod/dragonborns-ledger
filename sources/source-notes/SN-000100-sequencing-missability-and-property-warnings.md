# Source Note: Sequencing, Missability, and Property Warnings

Status: researched.

Source note ID: SN-000100

## Claim

Some TB-014 candidates are not full branches, but still need route warnings or hard saves because sequencing can close quest windows, block property access, lose NPC-dependent services, or lock reward objects.

## Routing Relevance

These rows feed the warning layer and later NPC/bug/trophy passes. TB-014 records the constraint and handoff; TB-016 and TB-017 will decide exact NPC protection and bug-mitigation placement.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000003 | Skyrim:Companions | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Companions | 2026-05-11 | Windowed Companions radiant availability. |
| SRC-000013 | Skyrim:Bards College | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bards_College | 2026-05-11 | Bards College instrument and investigation bugs. |
| SRC-000015 | Skyrim:Tending the Flames | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Tending_the_Flames | 2026-05-11 | Bards College conflict and ordering risks. |
| SRC-000040 | Skyrim:A New Source of Stalhrim | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_New_Source_of_Stalhrim | 2026-05-11 | Skaal NPC dependency for stalhrim crafting. |
| SRC-000353 | Skyrim:Rare Gifts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rare_Gifts | 2026-05-12 | Siddgeir level-9 letter caveat and Captain Aldis Civil War risk. |
| SRC-000362 | Skyrim:Delayed Burial | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Delayed_Burial | 2026-05-12 | Dark Brotherhood side-quest availability window. |
| SRC-000368 | Skyrim:The Whispering Door | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Whispering_Door | 2026-05-12 | Hulda/Ysolda quest-start dependency. |
| SRC-000369 | Skyrim:Discerning the Transmundane | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Discerning_the_Transmundane | 2026-05-12 | Oghma Infinium outpost respawn lock and Septimus failure risk. |
| SRC-000374 | Skyrim:Kill Helvard | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Kill_Helvard | 2026-05-12 | Falkreath Jarl disposition/property bug. |
| SRC-000375 | Skyrim:Lakeview Manor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lakeview_Manor | 2026-05-12 | Falkreath land purchase prerequisites and Kill Helvard property risk. |
| SRC-000379 | Skyrim:Boethiah's Calling | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Boethiah%27s_Calling | 2026-05-12 | Nonessential follower sacrifice and inventory/faction risks. |
| SRC-000380 | Skyrim:The House of Horrors | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors | 2026-05-12 | Logrolf failure condition and locked-house bug risk. |
| SRC-000381 | Skyrim:The Cursed Tribe | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Cursed_Tribe | 2026-05-12 | Largashbur first-visit NPC death risk. |

## Evidence Summary

UESP records several windowed or sequence-sensitive cases. `Delayed Burial` fails once the Dark Brotherhood path advances too far. The Companions faction page lists three post-Silver Hand radiants that become unavailable after starting `Blood's Honor`. Bards College notes warn against starting the investigation late or collecting instruments too early. `Rare Gifts` notes that Falkreath's level-9 Jarl letter can block Siddgeir's rare-gift favor, and that Captain Aldis becomes unavailable after the Stormcloak Solitude battle. `Kill Helvard` and `Lakeview Manor` both warn that killing Helvard can block Lakeview Manor purchase under Siddgeir if the property is not secured first.

Other cases are NPC or object preservation warnings. `The Whispering Door` depends on Hulda or Ysolda for the rumor path. `A New Source of Stalhrim` depends on Deor and Fanari surviving long enough to start the quest. `Boethiah's Calling` requires sacrificing a nonessential follower and warns about follower inventory and faction side effects. `The House of Horrors` fails if Logrolf is killed while captive. `Discerning the Transmundane` can lock the Oghma Infinium behind a closed Dwemer puzzle door if the outpost cell respawns after opening the cube. `The Cursed Tribe` opens with a giant attack at Largashbur that can kill potential Orc followers before the player intervenes.

## Confidence and Open Questions

Confidence is high for the warning need. TB-016 must expand NPC dependency handling, and TB-017 must decide exact PS4/no-console mitigation wording for bugs and hard-save placement.

## Linked Records

OBJ-000109 through OBJ-000111, OBJ-000168, OBJ-000172, OBJ-000174, OBJ-000182 through OBJ-000186, OBJ-000207, OBJ-000249, OBJ-000260, OBJ-000391, OBJ-000395, OBJ-000436, OBJ-001919 through OBJ-001957.
