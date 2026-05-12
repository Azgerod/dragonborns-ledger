# Source Note: AE Home and Goldenhills Farm Detail Expansion

Status: needs review.

Source note ID: SN-000076

## Claim

The property detail table now carries source-backed rows for AE player-home feature summaries, Goldenhills Plantation ownership, farm interior upgrades, farm exterior construction, livestock/services, farmhand hiring, farm income, and pantry harvest behavior.

## Routing Relevance

The specification requires all AE homes, the farm, relevant upgrades/furnishings, safe storage implications, display audits, Survival Mode geography value, and farm/property services. AE homes often provide fully furnished storage, crafting, displays, and family support. Goldenhills Plantation adds a farm-management system that affects food, income, horse travel, farm staffing, crop choices, and material planning.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000063 | Skyrim:Houses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Houses | 2026-05-12 | AE home summaries, purchase/quest acquisition, furnished status, mannequins, family support, Goldenhills upgrade costs, and livestock costs. |
| SRC-000064 | Skyrim:Bloodchill Cavern | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bloodchill_Cavern | 2026-05-12 | Bloodchill Manor place, storage/crafting/display context, and quest-resident caveats. |
| SRC-000065 | Skyrim:Dead Man's Dread (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dead_Man%27s_Dread_(place) | 2026-05-12 | Dead Man's Dread player-home conversion and one-way map travel destinations. |
| SRC-000066 | Skyrim:Gallows Hall (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Gallows_Hall_(place) | 2026-05-12 | Gallows Hall storage, crafting, display, Bone Forge, and Altar of the Revenant features. |
| SRC-000067 | Skyrim:Goldenhills Plantation | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Goldenhills_Plantation | 2026-05-12 | Goldenhills ownership, farm operations, steward/farmhand notes, pet guard note, and production context. |
| SRC-000068 | Skyrim:Hendraheim (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hendraheim_(place) | 2026-05-12 | Hendraheim place, smithing/display/storage context. |
| SRC-000069 | Skyrim:Myrwatch (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Myrwatch_(place) | 2026-05-12 | Myrwatch storage, crafting, family support, staff enchanter, and All Forge context. |
| SRC-000070 | Skyrim:Nchuanthumz | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Nchuanthumz | 2026-05-12 | Nchuanthumz restored-home facilities, beds, trophy bases, fertile soil, and crafting context. |
| SRC-000071 | Skyrim:Shadowfoot Sanctum (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shadowfoot_Sanctum_(place) | 2026-05-12 | Shadowfoot Sanctum purchase, entrances, storage, shrines, crafting stations, and family support. |
| SRC-000072 | Skyrim:Tundra Homestead (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Tundra_Homestead_(place) | 2026-05-12 | Tundra Homestead purchase, storage, crafting, garden/apiary, and family support. |
| SRC-000074 | Skyrim:Farming Construction | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Farming_Construction | 2026-05-12 | Goldenhills Farmer's Workbench exterior construction options and material requirements. |
| SRC-000075 | Skyrim:A Farmer's Life For Me | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_Farmer%27s_Life_For_Me | 2026-05-12 | Goldenhills farm setup sequence, steward, farmhand, livestock, income, pantry, notes, and bugs. |
| SRC-000245 | Skyrim:Personal Steward | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Personal_Steward | 2026-05-12 | Goldenhills steward furnishing, farmhand, horse, and livestock services. |

## Evidence Summary

UESP's Houses page lists the Creation Club homes covered by the AE bundle and identifies their acquisition method, fully furnished status where applicable, purchase costs for Shadowfoot Sanctum and Tundra Homestead, mannequins, family support where listed, and Goldenhills Plantation upgrade and livestock prices.

The individual AE property pages add facility details needed for later route analysis: storage and crafting stations, display furniture, family support, special systems such as Gallows Hall's Bone Forge and Altar of the Revenant, Myrwatch's staff enchanter and All Forge, Nchuanthumz's trophy bases and fertile soil, and Dead Man's Dread's one-way travel map.

Farming Construction lists Goldenhills Farmer's Workbench exterior construction options and materials. A Farmer's Life For Me records the setup sequence: plant 10 crops, recruit a steward, recruit farmhands, build animal pens, buy livestock, wait for farm income, collect income, and collect pantry output. The Personal Steward page cross-checks steward-priced Goldenhills interior furnishings, farmhand hiring, horse, and livestock services.

## Confidence and Open Questions

Confidence is high for source-listed AE home and Goldenhills detail rows. TB-031D selects Tundra Homestead as main base, Goldenhills as farm/food/income support, Faendal as Goldenhills steward, and generic Goldenhills farmhands. Later passes must still validate exact AE start triggers, quest difficulty, bug mitigations, safe-storage recommendations, display/checklist audits, Goldenhills crop defaults, farm-income repeatability bounds, family-home implementation, and Survival Mode route value.

## Linked Records

`data/properties/property-details.csv`, `OBJ-000659` through `OBJ-000668`, `OBJ-001951`, and `OBJ-001954`.
