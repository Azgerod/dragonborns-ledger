# Source Note: AE Unique Equipment Member Expansion

Status: needs review.

Source note ID: SN-000073

## Claim

UESP item pages and Creation content summaries identify individual source-listed members for AE unique, named, pet-equipment, mount-equipment, and reward parent rows `OBJ-000728` through `OBJ-000759`. These members are now captured in `data/items/ae-item-members.csv`.

## Routing Relevance

The specification requires all obtainable unique items, AE rewards, pets and mounts, source-listed spells, item preservation, branch handling for meaningful reward choices, and checklist synchronization. Member rows keep source-listed equipment, keys, quest items, ingredients, consumables, and exclusions visible without prematurely writing route content.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000135 | Skyrim:Divine Crusader Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Divine_Crusader_Items | 2026-05-12 | Item table used for source-listed members. |
| SRC-000136 | Skyrim:Netch Leather Armor Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Netch_Leather_Armor_Items | 2026-05-12 | Item table used for source-listed members. |
| SRC-000137 | Skyrim:Spell Knight Armor Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Spell_Knight_Armor_Items | 2026-05-12 | Item table used for source-listed members. |
| SRC-000138 | Skyrim:Vigil Enforcer Armor Set Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Vigil_Enforcer_Armor_Set_Items | 2026-05-12 | Item table used for source-listed members and exclusions. |
| SRC-000139 | Skyrim:Civil War Champions Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Civil_War_Champions_Items | 2026-05-12 | Item table used for source-listed members and branch-sensitive gear. |
| SRC-000141 | Skyrim:Saturalia Holiday Pack Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Saturalia_Holiday_Pack_Items | 2026-05-12 | Item table used for source-listed members. |
| SRC-000142 | Skyrim:Arms of Chaos Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Arms_of_Chaos_Items | 2026-05-12 | Item table used for source-listed members. |
| SRC-000143 | Skyrim:Chrysamere Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Chrysamere_Items | 2026-05-12 | Item table used for the unique weapon member. |
| SRC-000144 | Skyrim:Dawnfang & Duskfang Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dawnfang_%26_Duskfang_Items | 2026-05-12 | Item table used for weapon members. |
| SRC-000145 | Skyrim:Dead Man's Dread Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dead_Man%27s_Dread_Items | 2026-05-12 | Item table used for source-listed members. |
| SRC-000147 | Skyrim:Lord's Mail Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lord%27s_Mail_Items | 2026-05-12 | Item table used for source-listed members and item-state rows. |
| SRC-000148 | Skyrim:Ruin's Edge Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ruin%27s_Edge_Items | 2026-05-12 | Item table used for the unique weapon member. |
| SRC-000149 | Skyrim:Shadowrend Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shadowrend_Items | 2026-05-12 | Item table used for weapon-form rows. |
| SRC-000150 | Skyrim:Staff of Hasedoki Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Staff_of_Hasedoki_Items | 2026-05-12 | Item table used for the staff member. |
| SRC-000151 | Skyrim:Staff of Sheogorath Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Staff_of_Sheogorath_Items | 2026-05-12 | Item table used for weapon and quest-item members. |
| SRC-000152 | Skyrim:Stendarr's Hammer Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Stendarr%27s_Hammer_Items | 2026-05-12 | Item table used for the unique weapon member. |
| SRC-000153 | Skyrim:Sunder & Wraithguard | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Sunder_%26_Wraithguard | 2026-05-12 | Creation content summary used for source-listed members. |
| SRC-000154 | Skyrim:The Gray Cowl Returns! Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Gray_Cowl_Returns!_Items | 2026-05-12 | Item table used for source-listed members. |
| SRC-000155 | Skyrim:Umbra Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Umbra_Items | 2026-05-12 | Item table used for unique weapon and key members. |
| SRC-000158 | Skyrim:Bow of Shadows | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bow_of_Shadows | 2026-05-12 | Creation content summary used for source-listed members. |
| SRC-000160 | Skyrim:Headman's Cleaver | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Headman%27s_Cleaver | 2026-05-12 | Creation content summary used for source-listed member. |
| SRC-000162 | Skyrim:Pets of Skyrim Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Pets_of_Skyrim_Items | 2026-05-12 | Item table used for pet-equipment and related item members. |
| SRC-000163 | Skyrim:Wild Horses Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Wild_Horses_Items | 2026-05-12 | Item table used for map/member coverage. |
| SRC-000164 | Skyrim:Dwarven Armored Mudcrab Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dwarven_Armored_Mudcrab_Items | 2026-05-12 | Item table used for spell-tome cross-link coverage. |
| SRC-000256 | Skyrim:Redguard Elite Armaments Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Redguard_Elite_Armaments_Items | 2026-05-12 | Item table used for source-listed members. |
| SRC-000109 | Skyrim:Forgotten Seasons Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Forgotten_Seasons_Items | 2026-05-12 | Item table used for source-listed members and exclusions. |
| SRC-000257 | Skyrim:Ghosts of the Tribunal Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ghosts_of_the_Tribunal_Items | 2026-05-12 | Item table used for source-listed members and exclusions. |
| SRC-000258 | Skyrim:The Cause Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Cause_Items | 2026-05-12 | Item table used for source-listed members and spell-tome cross-links. |
| SRC-000259 | Skyrim:The Contest Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Contest_Items | 2026-05-12 | Item table used for reward members. |
| SRC-000260 | Skyrim:Goldbrand Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Goldbrand_Items | 2026-05-12 | Item table used for source-listed members. |
| SRC-000261 | Skyrim:Bittercup Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bittercup_Items | 2026-05-12 | Item table used for source-listed members, exclusions, and spell-tome cross-link. |
| SRC-000262 | Skyrim:Goblins | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Goblins | 2026-05-12 | Creation content summary used for source-listed members and the unobtainable Spear of Bitter Mercy audit row. |

## Evidence Summary

The expansion adds 319 unique-equipment member rows. UESP item pages are used where available; summary content lists are used for parent sets without item pages. Books and notes are not duplicated here because the book/document pass owns them. Spell-tome rows are cross-linked to existing spell-tome objectives rather than creating duplicate objectives.

## Confidence and Open Questions

Confidence is high for source-listed membership. Exact acquisition source selection, quest/outcome branches, branch-only reward treatment, unique-item preservation, carried follower gear policy, pet/mount equipment policy, checklist mapping, and route timing remain deferred.

## Linked Records

`OBJ-000728` through `OBJ-000759`; `ITEM-000847` through `ITEM-001165`.
