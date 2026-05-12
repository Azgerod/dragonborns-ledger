# Source Note: AE Ingredient, Consumable, Material, and Broad Item Member Expansion

Status: needs review.

Source note ID: SN-000070

## Claim

The current AE ingredient, consumable, food, material, curio, fishing, Survival Mode, Nix-Hound, Saints and Seducers, and Forgotten Seasons parent rows can be expanded into source-listed member coverage using the relevant UESP Creation item pages.

## Routing Relevance

The specification requires AE items, ingredients, alchemy-effect discovery, Survival Mode-relevant consumables, practical crafting knowledge, and checklist synchronization. Member-level coverage is needed before route planning can decide which items are required acquisitions, which are crafting/alchemy validation targets, which are already covered by spell-tome rows, and which source-listed items should be excluded as unobtainable.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000104 | Skyrim:Plague of the Dead Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Plague_of_the_Dead_Items | 2026-05-12 | Mort Flesh and associated source-listed Plague item rows. |
| SRC-000106 | Skyrim:Rare Curios Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rare_Curios_Items | 2026-05-12 | Ammunition, food, ingredient, and miscellaneous item sections. |
| SRC-000107 | Skyrim:Saints & Seducers Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Saints_%26_Seducers_Items | 2026-05-12 | Apparel, weapons, ingredients, scrolls, poison, soul gem, key, miscellaneous, and spell-tome sections. |
| SRC-000108 | Skyrim:Fishing Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_Items | 2026-05-12 | Apparel, weapons, food, ingredients, keys, and miscellaneous Fishing item sections. |
| SRC-000109 | Skyrim:Forgotten Seasons Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Forgotten_Seasons_Items | 2026-05-12 | Food, ingredient, key, miscellaneous, and utility-weapon sections used for the current parent row. |
| SRC-000110 | Skyrim:Survival Mode Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Survival_Mode_Items | 2026-05-12 | Survival Mode food item section. |
| SRC-000111 | Skyrim:Nix-Hound Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Nix-Hound_Items | 2026-05-12 | Nix-Hound food and spell-tome item sections. |

## Evidence Summary

The relevant UESP item pages list the finite item members associated with each parent Creation. This pass records 284 item-member rows in `data/items/ae-item-members.csv`: 69 ingredient rows, 60 weapon rows, 47 food rows, 27 apparel rows, 21 miscellaneous item rows, 17 unique apparel rows, 17 raw-food rows, 6 ammunition rows, 6 spell-tome rows cross-linked to existing spell-tome objective IDs, 5 scroll rows, 4 key rows, 2 unique weapon rows, and one row each for poison, soul gem, and beverage coverage.

## Confidence and Open Questions

Confidence is high for source-listed membership. Exact route acquisition choices, fishing conditions, alchemy-effect discovery order, Survival Mode food policy, crafting recipes, vendor/restock behavior, checklist mapping, and whether any broad item members deserve separate objective rows remain deferred.

Rows source-marked as unobtainable are retained with `route_treatment=excluded_unobtainable` for audit rather than route placement.

## Linked Records

`OBJ-000697` through `OBJ-000703`, `data/items/ae-item-members.csv`.
