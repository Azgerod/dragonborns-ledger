# AE Item Member Reconciliation

Status: TB-007G1 and TB-007G2 complete; covered by TB-007G4 aggregate reconciliation; downstream route and checklist validation pending.

This file summarizes `data/items/ae-item-members.csv`. It is not route prose and does not make final route-order decisions.

## Scope

TB-007G1 expands parent rows `OBJ-000693` through `OBJ-000712` into member-level coverage for AE magic, ingredients, consumables, crafting systems, and practical equipment.

TB-007G2 expands parent rows `OBJ-000713` through `OBJ-000759` into member-level coverage for AE Alternative Armor, unique/named equipment, pet equipment, mount equipment, source-listed reward items, and related cross-links.

The table records source-listed members from UESP item pages and keeps parent objective rows as the route/checklist-facing completion units until later passes decide which members need their own objective rows.

## Current Coverage

| Coverage group | Source note | Parent rows | Item-member rows | Treatment |
| --- | --- | --- | ---: | --- |
| AE magic, staves, and crafting-station cross-references | `SN-000069` | `OBJ-000693` through `OBJ-000696`; `OBJ-000711` through `OBJ-000712` | 382 | Spell tomes cross-link existing spell-tome objectives; staff and apparel members remain source-listed item members. |
| AE ingredients, consumables, materials, and broad item sets | `SN-000070` | `OBJ-000697` through `OBJ-000703` | 284 | Ingredients, food, fishing items, Saints and Seducers items, Survival Mode food, and related members are retained for route/checklist validation. |
| AE practical equipment and crafting sets | `SN-000071` | `OBJ-000704` through `OBJ-000710` | 98 | Backpacks, camping supplies, arrows, crossbows, Nordic Jewelry, and brawler gauntlets are retained for crafting and power-curve validation. |
| AE Alternative Armor member sets | `SN-000072` | `OBJ-000713` through `OBJ-000727` | 82 | Armor pieces, source-listed keys, named weapons, and unobtainable/internal audit rows are retained for route/checklist validation. |
| AE unique, named, pet-equipment, mount-equipment, and reward sets | `SN-000073` | `OBJ-000728` through `OBJ-000759` | 319 | Unique/named equipment, keys, quest items, related consumables/ingredients, and spell-tome cross-links are retained for route/checklist validation. |
| Total | `SN-000069` through `SN-000073` | `OBJ-000693` through `OBJ-000759` | 1165 | Parent-set rows now have member-level table coverage through TB-007G2. |

## Route Treatment Counts

| Route treatment | Count | Meaning |
| --- | ---: | --- |
| `source_listed_member` | 1090 | Member remains eligible for route/checklist consideration. |
| `already_tracked_in_spell_tome_table` | 45 | Member is already represented by a spell-tome objective row and acquisition table. |
| `crafting_system_cross_reference` | 6 | Row identifies a station-linked craftable system rather than a separate pickup objective. |
| `excluded_unobtainable` | 21 | Source marks member as unobtainable; retained for audit and exclusion validation. |
| `excluded_template_or_internal` | 3 | Source-listed template/internal rows retained for audit but not route placement. |

## Category Counts

| Item category | Count |
| --- | ---: |
| `apparel` | 346 |
| `staff` | 318 |
| `weapon` | 126 |
| `ingredient` | 78 |
| `misc_item` | 77 |
| `food` | 52 |
| `spell_tome` | 45 |
| `key` | 25 |
| `unique_apparel` | 24 |
| `raw_food` | 17 |
| `ammunition` | 13 |
| `unique_weapon` | 9 |
| `jewelry` | 6 |
| `crafting_station` | 6 |
| `scroll` | 5 |
| `document_item` | 5 |
| `potion` | 4 |
| `quest_item` | 3 |
| `apparel_template` | 2 |
| `poison` | 2 |
| `beverage` | 1 |
| `soul_gem` | 1 |

## Follow-Up Boundaries

| Boundary | Current treatment | Later action |
| --- | --- | --- |
| Spell tomes | Cross-linked to existing spell-tome objective IDs. | Route placement chooses acquisition source and timing from `data/books/spell-tomes-locations.csv`. |
| Ingredients and food | Source-listed members retained in item table. | TB-009/TB-020 handle alchemy-effect discovery, cooking/crafting usefulness, and Survival Mode food policy. |
| Crafting systems and equipment | Members retained without final crafting timing. | Later progression and route passes decide when to craft, buy, loot, or ignore duplicates. |
| Alternative Armor and named equipment | Source-listed members retained without final route timing or preservation policy. | TB-012/TB-020 should validate level gates, difficulty spikes, unique preservation, and power-curve timing before route insertion. |
| Pets, mounts, and follower-carried gear | Pet/mount equipment and related source-listed rows retained here; relationship/pet/mount rows remain in the objective database. | Later route and checklist passes should decide what to buy/equip/preserve and how to handle follower-carried gear such as Gogh's carried items. |
| Unobtainable/template rows | Retained with exclusion treatments. | TB-007G4 and checklist mapping should verify they remain excluded unless external checklist treatment requires a note. |
| Books and notes on item pages | Not duplicated in this table. | Book/document tables own individual book/note location and checklist expansion, including one-copy-per-title acquisition planning. |

## Result

TB-007G1 and TB-007G2 close member-level coverage for `OBJ-000693` through `OBJ-000759`. TB-007G4 reconciles the remaining broad parent/set rows in `data/objectives/aggregate-reconciliation.md`; acquisition choices, exclusions, route timing, and checklist mapping remain downstream validation work.
