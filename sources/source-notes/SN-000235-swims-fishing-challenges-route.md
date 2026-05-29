# Swims-In-Deep-Water Fishing Challenges Route

Status: researched.

Source note ID: SN-000235

## Claim

The guide should route Swims-In-Deep-Water's immediate post-`Catch of the Day` quest chain inside the controlled Riften Fishing block:

- Complete `Caught in the Rain` before Viriya's longer bounty chain progresses too far, because it awards the Argonian Fishing Rod and gives access to the Lucky Fishing Hat.
- Keep the Lucky Fishing Hat by lying to Swims-In-Deep-Water at the turn-in; this preserves the unique item and forfeits only the optional 400 gold.
- Complete `Frozen Fish` after `Caught in the Rain` and Viriya's `Crustacean Extermination`, because the quest expects the Argonian and Alik'ri Fishing Rods.
- Complete `Darkest Depths` immediately after `Frozen Fish`, using the already-cleared Broken Oar Grotto underground Fishing Supplies instead of disturbing Embershard Mine before the later `Smith 'N Slash`/Orcish Plate route.

## Routing Relevance

This closes `OBJ-000595` Darkest Depths and its direct prerequisite `OBJ-000598` Frozen Fish. It also closes the route-resolution rows for `Caught in the Rain` support documents, the `Frozen Fish` support documents, the `Darkest Depths` support documents, and the Fishing catch rows that these quests naturally require:

- `Caught in the Rain`: Catfish, Pearlfish, Pygmy Sunfish, Spadefish, `List of Rainy Weather Fish`, `Fishing Mastery, v2`, Lucky Fishing Hat, and Argonian Fishing Rod.
- `Frozen Fish`: Cod, Arctic Char, Arctic Grayling, Angler Larvae, one spare Angler Larvae for later alchemy-effect discovery if needed, `List of Arctic Fish`, and `Fishing Mastery, v3`.
- `Darkest Depths`: Direfish, Glass Catfish, Tripod Spiderfish, Vampire Fish, `List of Underground Fish`, and `Fishing Mastery, v4`.

The route should not ask the player to reload for ordinary Fishing catch variance. It should use active quest state, correct biome/weather/rod controls, already-routed support stops, and rest/resupply loops if a fishing spot depletes.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001738 | Skyrim:Caught in the Rain | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Caught_in_the_Rain | 2026-05-29 | Used for Swims-In-Deep-Water start, rainy fish list, required fish, Lucky Fishing Hat objective, Geirmund/Sarethi fishing camp, reward branch, and quest bugs. |
| SRC-001739 | Skyrim:Frozen Fish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Frozen_Fish | 2026-05-29 | Used for Caught in the Rain and Crustacean Extermination prerequisites, required arctic fish, Fishing Mastery v3, courier bypass, Dawnstar/Windhelm/Nightgate fishing guidance, and reward. |
| SRC-001740 | Skyrim:Darkest Depths | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Darkest_Depths | 2026-05-29 | Used for Swims-In-Deep-Water start, required underground fish, Fishing Mastery v4, Embershard/Broken Oar underground guidance, and 400 gold completion boundary. |
| SRC-001741 | Skyrim:List of Rainy Weather Fish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:List_of_Rainy_Weather_Fish | 2026-05-29 | Used for quest-note source, Lucky Fishing Hat location hint, and required rainy fish list. |
| SRC-001742 | Skyrim:List of Arctic Fish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:List_of_Arctic_Fish | 2026-05-29 | Used for quest-note source and required arctic fish list. |
| SRC-001743 | Skyrim:List of Underground Fish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:List_of_Underground_Fish | 2026-05-29 | Used for quest-note source and required underground fish list. |
| SRC-001744 | Skyrim:Fishing Mastery, v2 | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_Mastery,_v2 | 2026-05-29 | Used for Riften Fishery back-room shelf source after beginning Caught in the Rain. |
| SRC-001745 | Skyrim:Fishing Mastery, v3 | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_Mastery,_v3 | 2026-05-29 | Used for Riften Fishery back-room shelf source after beginning Frozen Fish. |
| SRC-001746 | Skyrim:Fishing Mastery, v4 | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_Mastery,_v4 | 2026-05-29 | Used for Riften Fishery back-room shelf source after beginning Darkest Depths. |
| SRC-001747 | Skyrim:Lucky Fishing Hat | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lucky_Fishing_Hat | 2026-05-29 | Used for unique-item status, rainstorm effect, and no-recovery warning if returned to Swims-In-Deep-Water. |
| SRC-001748 | Skyrim:Pearlfish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Pearlfish | 2026-05-29 | Used for rainy temperate lake/stream conditions and guaranteed fallback locations. |
| SRC-001749 | Skyrim:Pygmy Sunfish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Pygmy_Sunfish | 2026-05-29 | Used for rainy temperate lake conditions, Lucky Fishing Hat support, and guaranteed fallback locations. |
| SRC-001750 | Skyrim:Spadefish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Spadefish | 2026-05-29 | Used for rainy temperate stream conditions and guaranteed fallback locations. |
| SRC-001751 | Skyrim:Angler Larvae | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Angler_Larvae | 2026-05-29 | Used for freezing-water catch guidance, Dawnstar fishing spot support, and Pilgrim's Trench guaranteed spawn fallback. |
| SRC-001752 | Skyrim:Geirmund's Hall | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Geirmund%27s_Hall | 2026-05-29 | Used for the Geirmund's Hall exterior Fishing Supplies and temperate-lake fishing camp. |
| SRC-001753 | Skyrim:Broken Oar Grotto | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Broken_Oar_Grotto | 2026-05-29 | Used for Broken Oar Grotto Fishing Supplies and underground-water catch suitability after the earlier clear. |
| SRC-001692 | Skyrim:Fishing (activity) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_(activity) | 2026-05-29 | Used for Fishing Supplies mechanics, biome tables, Riften canal, Geirmund's Hall, Dawnstar, and Broken Oar Grotto fishing-spot records. |
| SRC-001713 | Skyrim:Fishing Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_Items | 2026-05-29 | Used for Lucky Fishing Hat, Argonian Fishing Rod, rod effects, fish item rows, and Fishing document membership. |

## Evidence Summary

UESP's `Caught in the Rain` page says Swims-In-Deep-Water gives the quest at the Riften Fishery, asks for Catfish, Pearlfish, Pygmy Sunfish, Spadefish, and the Lucky Fishing Hat, and lets the player either return the hat or lie that it was not found. The Lucky Fishing Hat page marks it as a unique item and says that returning it during the quest prevents recovering it from Swims-In-Deep-Water. The route therefore keeps the hat and accepts the lower reward.

The same quest page and the Fishing activity/fish pages support the rainy-weather split: Pygmy Sunfish are rainy temperate-lake fish, Spadefish are rainy temperate-stream fish, and Pearlfish can be caught in rainy temperate lakes or streams. `List of Rainy Weather Fish` names the same required fish and the hat's west-of-Sarethi-Farm fishing camp. `Fishing Mastery, v2` is on a Riften Fishery back-room shelf after the quest begins. Geirmund's Hall and the Fishing activity location table confirm a nearby temperate-lake Fishing Supplies camp.

UESP's `Frozen Fish` page gives `Caught in the Rain` and `Crustacean Extermination` as prerequisites, says the courier letter can be bypassed by going directly to Swims-In-Deep-Water after `Crustacean Extermination`, and asks for Cod, Arctic Grayling, Arctic Char, and Angler Larvae. It names freezing-water spots near Windhelm, Dawnstar, and Nightgate Inn; the guide uses Dawnstar because the route is already working in that region and already owns the Argonian and Alik'ri rods. `List of Arctic Fish` and `Fishing Mastery, v3` match the quest support documents. Angler Larvae are also guaranteed at Pilgrim's Trench, so the guide stores one during the earlier sourced Pilgrim's Trench dive if the player follows the full route.

UESP's `Darkest Depths` page asks for Direfish, Glass Catfish, Tripod Spiderfish, and Vampire Fish, says all can be caught at underground fishing spots such as Embershard Mine and Broken Oar Grotto, and pays 400 gold when the requested fish are delivered. `List of Underground Fish` and `Fishing Mastery, v4` match the quest support documents. Broken Oar Grotto is already cleared in the guide before this Fishing block; Embershard is deliberately left undisturbed for the later `Smith 'N Slash`/Orcish Plate route, so Broken Oar is the safer underground spot here.

## Confidence and Open Questions

Confidence is high for the quest order, document sources, unique hat preservation policy, rod requirements, fish lists, and route insertion point.

The only operational uncertainty is ordinary Fishing catch variance. The guide handles that with source-backed biome/weather/rod controls and rest/resupply loops instead of save-reload manipulation.

`Fishing Legend`, `Further Study`, `Rubbish Retrieval`, `Stocking Up`, `Fishing Mastery, v5`, `List of Rare Fish`, and remaining rare/special Fishing species are still unresolved and should stay in the next TB-044 Fishing bucket.

## Linked Records

OBJ-000593; OBJ-000595; OBJ-000598; OBJ-001399; OBJ-001400; OBJ-001401; OBJ-001444; OBJ-001446; OBJ-001448; OBJ-001896; OBJ-001901; OBJ-001902; OBJ-001903; OBJ-001904; OBJ-001909; OBJ-001911; OBJ-001913; OBJ-001914; OBJ-001915; OBJ-002640; CHK-QUESTS-0622; CHK-QUESTS-0624; CHK-QUESTS-0625; CHK-BOOKS-2470; CHK-BOOKS-2471; CHK-BOOKS-2472; ITEM-000537; ITEM-000548; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/books/book-document-locations.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/items/ae-item-members.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
