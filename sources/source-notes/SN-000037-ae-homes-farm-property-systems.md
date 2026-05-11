# Source Note: AE Homes, Farm, and Property Systems

Status: needs review.

Source note ID: SN-000037

## Claim

The official AE Creation Club bundle adds eight player-home/property records plus the Goldenhills Plantation farm property and farm-management system that need objective-database coverage separate from the AE quest rows.

## Routing Relevance

The specification requires all AE homes, the farm, relevant upgrades/furnishings, safe storage implications, and Survival Mode geography value to be accounted for. These property rows let later routing and constraint passes decide acquisition timing, economy gates, storage use, family movement, farm-steward choices, farmhand choices, construction material planning, and bug mitigations without treating the source-list data as final route instructions.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000063 | Skyrim:Houses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Houses | 2026-05-11 | Lists Creation Club houses and summarizes acquisition, furnishings, storage, crafting, family-support, and farm notes. |
| SRC-000064 | Skyrim:Bloodchill Cavern | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bloodchill_Cavern | 2026-05-11 | Bloodchill Manor place details and crafting/storage context. |
| SRC-000065 | Skyrim:Dead Man's Dread (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dead_Man%27s_Dread_(place) | 2026-05-11 | Dead Man's Dread ship place details and crafting/storage context. |
| SRC-000066 | Skyrim:Gallows Hall (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Gallows_Hall_(place) | 2026-05-11 | Gallows Hall place details and special necromancy systems. |
| SRC-000067 | Skyrim:Goldenhills Plantation | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Goldenhills_Plantation | 2026-05-11 | Goldenhills Plantation ownership and farm-place details. |
| SRC-000068 | Skyrim:Hendraheim (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hendraheim_(place) | 2026-05-11 | Hendraheim place details and crafting/storage context. |
| SRC-000069 | Skyrim:Myrwatch (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Myrwatch_(place) | 2026-05-11 | Myrwatch place details and crafting/storage context. |
| SRC-000070 | Skyrim:Nchuanthumz | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Nchuanthumz | 2026-05-11 | Nchuanthumz Dwarven Home place details and crafting/storage context. |
| SRC-000071 | Skyrim:Shadowfoot Sanctum (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shadowfoot_Sanctum_(place) | 2026-05-11 | Shadowfoot Sanctum place details and crafting/storage context. |
| SRC-000072 | Skyrim:Tundra Homestead (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Tundra_Homestead_(place) | 2026-05-11 | Tundra Homestead place details and crafting/storage context. |
| SRC-000073 | Skyrim:Farming | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Farming | 2026-05-11 | Farming Creation overview and farmstead management scope. |
| SRC-000074 | Skyrim:Farming Construction | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Farming_Construction | 2026-05-11 | Goldenhills Plantation construction options and farm upgrades. |
| SRC-000075 | Skyrim:A Farmer's Life For Me | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_Farmer%27s_Life_For_Me | 2026-05-11 | Goldenhills Plantation farm-setup loop, steward/farmhands, livestock, income, and pantry output. |
| SRC-000076 | Skyrim:The Unquiet Dead | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Unquiet_Dead | 2026-05-11 | Goldenhills Plantation ownership quest, key reward, next-quest trigger, and bug notes. |

## Evidence Summary

UESP's Houses page groups Creation Club homes separately and identifies Bloodchill Manor, Dead Man's Dread, Gallows Hall, Goldenhills Plantation, Hendraheim, Myrwatch, Nchuanthumz, Shadowfoot Sanctum, and Tundra Homestead as Creation Club housing or farm property content. It summarizes how each is earned or purchased and notes that these homes are furnished or function as player housing.

The individual place pages confirm region/location details and house/farm type. Goldenhills Plantation requires additional treatment because Farming adds a management system, not just a static home: the farm can be claimed through The Unquiet Dead, then developed through A Farmer's Life For Me with crops, a steward, farmhands, animal pens, livestock, income, and pantry production. Farming Construction lists farm upgrade categories that need later material planning and upgrade policy.

## Confidence and Open Questions

Confidence is high that these are the AE property/farm rows needed at source-list level. Exact route placement, family-move decisions, safe-storage policy, display-audit handling, farm steward/farmhand defaults, complete farm upgrade policy, construction material planning, and The Unquiet Dead bug mitigation remain deferred.

## Linked Records

OBJ-000659 through OBJ-000668.
