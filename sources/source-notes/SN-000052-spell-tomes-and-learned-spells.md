# Source Note: Spell Tomes and Learned Spells

Status: needs review.

Source note ID: SN-000052

## Claim

The guide should track one title-level objective for every accessible official Skyrim AE spell tome whose spell can be learned or whose tome is a checklist-relevant book/document. Duplicate copies and duplicate acquisition sources are route candidates only. UESP's school spell tables identify 154 accessible spell tome titles across base game, Dawnguard, Dragonborn, and AE Creation Club content. The same source data also lists purchase, fixed-location, quest-reward, pet-recruitment, crafting, and other acquisition sources. Spectral Arrow is not entered as a required objective because UESP marks it as not available in game.

## Routing Relevance

The specification includes spell tomes in book/document scope and requires all permanent spells, powers, and abilities obtainable on the main route. This pass creates one objective row per accessible spell tome title and records source-listed acquisition candidates in `data/books/spell-tomes-locations.csv` so later routing can choose deterministic, well-timed sources without treating every merchant listing or random copy as a separate completion objective.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000185 | Skyrim:Spells | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Spells | 2026-05-11 | Supports spell-tome learning mechanics, general purchase rules, random-loot rules, skill/restock thresholds, master spell-tome access, and expert-loot bug note. |
| SRC-000193 | Skyrim:Alteration Spells | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alteration_Spells | 2026-05-11 | Spell rows, tome IDs, levels, and acquisition text for Alteration spell tomes. |
| SRC-000194 | Skyrim:Conjuration Spells | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Conjuration_Spells | 2026-05-11 | Spell rows, tome IDs, levels, and acquisition text for Conjuration spell tomes. |
| SRC-000195 | Skyrim:Destruction Spells | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Destruction_Spells | 2026-05-11 | Spell rows, tome IDs, levels, and acquisition text for Destruction spell tomes. |
| SRC-000196 | Skyrim:Illusion Spells | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Illusion_Spells | 2026-05-11 | Spell rows, tome IDs, levels, and acquisition text for Illusion spell tomes. |
| SRC-000197 | Skyrim:Restoration Spells | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Restoration_Spells | 2026-05-11 | Spell rows, tome IDs, levels, and acquisition text for Restoration spell tomes. |
| SRC-000184 | Category:Skyrim-Books-Spell Tomes | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Books-Spell_Tomes | 2026-05-11 | Spell tome page inventory and Creation Club subcategory pointer. |
| SRC-000198 | Category:Skyrim-Dragonborn-Books-Spell Tomes | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Dragonborn-Books-Spell_Tomes | 2026-05-11 | Dragonborn spell-tome category reconciliation. |
| SRC-000199 | Category:Skyrim-Creation Club-Books-Spell Tomes | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Creation_Club-Books-Spell_Tomes | 2026-05-11 | AE Creation Club spell-tome category reconciliation. |

## Evidence Summary

UESP's spell tables expose spell-tome IDs and acquisition notes for each school. After excluding the single source-listed unavailable spell tome, the accessible inventory used here contains 154 titles: 92 base-game, 8 Dawnguard, 9 Dragonborn, and 45 AE Creation Club spell tomes. The acquisition table preserves source-listed purchase, found, reward, crafting, pet-recruitment, and generic random-loot sources as candidates. UESP's general spell-tome rules state that adept and expert vendor stock depends on school skill and restock/reset, master spell tomes require the relevant ritual quest, and random tome loot uses character-level thresholds; those facts are recorded as deferred routing constraints, not final route choices.

## Confidence and Open Questions

Confidence is high for the title inventory and source-listed acquisition candidates. Open questions include exact merchant stock timing after skill thresholds, price/gold planning, faction/quest access, ownership or theft status for fixed copies, cell-entry or container reset implications, Creation-specific availability on PS4 AE, and whether the route should treat starting spells or pet-granted teleport spells as already satisfied or still acquire representative tomes for checklist presentation.

## Linked Records

OBJ-000910 through OBJ-001063.

`data/books/spell-tomes-locations.csv`.
