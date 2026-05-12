# Source Note: AE Magic, Staff, and Station Member Expansion

Status: needs review.

Source note ID: SN-000069

## Claim

The current AE magic and staff parent rows can be expanded into source-listed member coverage for Arcane Accessories robes and spell tomes, Necromantic Grimoire apparel and spell tomes, Plague of the Dead zombie spell tomes, Staves Creation staff members, and Staff Enchanter Creation Club craftable-staff cross-references.

## Routing Relevance

The specification requires all AE spells, items, rewards, and practical crafting-system unlocks. Member-level coverage is needed before the route can decide which members are separate checklist targets, which are already handled by spell-tome objectives, which require crafting-station access, and which can remain parent-set verification rather than standalone route steps.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000102 | Skyrim:Arcane Accessories Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Arcane_Accessories_Items | 2026-05-12 | Robe, template, and spell-tome member sections. |
| SRC-000103 | Skyrim:Necromantic Grimoire Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Necromantic_Grimoire_Items | 2026-05-12 | Apparel, magic apparel, and spell-tome member sections. |
| SRC-000104 | Skyrim:Plague of the Dead Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Plague_of_the_Dead_Items | 2026-05-12 | Zombie spell-tome member section. |
| SRC-000105 | Skyrim:Staves Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Staves_Items | 2026-05-12 | Unenchanted and enchanted Staves Creation item sections. |
| SRC-000119 | Skyrim:Staff Enchanter | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Staff_Enchanter | 2026-05-12 | Creation Club craftable-staff table used as a station/system cross-reference. |

## Evidence Summary

UESP's Arcane Accessories and Necromantic Grimoire item pages list apparel and spell-tome members; the Plague of the Dead item page lists the zombie spell tomes; the Staves item page lists unenchanted and enchanted staff members; and the Staff Enchanter page lists Creation Club craftable-staff rows tied to Creation content.

This pass records 382 item-member rows in `data/items/ae-item-members.csv`: 315 staff rows, 33 spell-tome rows cross-linked to existing spell-tome objective IDs, 26 apparel rows, 6 crafting-station cross-reference rows, and 2 template/internal rows kept visible as exclusions.

## Confidence and Open Questions

Confidence is high for source-list membership. Exact route acquisition choices, vendor/restock behavior, crafting recipes, station access timing, checklist mapping, and whether any staff/apparel rows should become separate objective rows remain deferred.

Template/internal rows are retained in the item table with `route_treatment=excluded_template_or_internal` so they are visible during checklist and completeness review.

## Linked Records

`OBJ-000693` through `OBJ-000696`, `OBJ-000711`, `OBJ-000712`, `data/items/ae-item-members.csv`.
