# Catch of the Day Route

Status: researched.

Source note ID: SN-000234

## Claim

`Catch of the Day` should be closed in the controlled Riften Fishing block that follows the Nightingale reward storage stop. The route already starts the quest during the first Riften visit by speaking to Swims-In-Deep-Water, receiving and reading `List of Fair Weather Fish`, and taking/reading `Fishing Mastery, v1` from the Riften Fishery back room. The later Riften return should finish the quest before Viriya's longer chain advances.

The guide should catch one Carp, one Glassfish, one Goldfish, and one Pogfish in clear weather, then return them to Swims-In-Deep-Water for the 200 gold reward and Riften Fishery Key. Lake Honrich at the Riften Fishery covers the temperate-lake fish; the Riften canal or another nearby temperate stream covers Pogfish.

## Routing Relevance

This closes the high-severity `OBJ-000592` route-resolution row without waiting for the broader Fishing species cleanup. It also gives precise route treatment to the related Fishing catch rows that the quest itself requires:

- Carp is routed as a fair-weather catch from a temperate lake or stream.
- Glassfish is already routed as a clear-weather Lake Honrich catch in the Viriya chain; this pass also records the earlier `Catch of the Day` catch as valid Fishing-species coverage.
- Goldfish is already routed by the Fellglow source in the Viriya chain; this pass also records the earlier `Catch of the Day` clear-weather catch as valid Fishing-species coverage.
- Pogfish is routed from a clear-weather temperate stream, using the Riften canal spot or the river route toward Ivarstead.

The guide should not ask the player to reload for fishing results. Fishing has ordinary catch variance and spot population limits, so the route uses source-backed biome/weather/location controls and tells the player to rest, resupply, and return in clear weather if a spot dries up.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001734 | Skyrim:Catch of the Day | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Catch_of_the_Day | 2026-05-29 | Used for Swims-In-Deep-Water giver, Riften Fishery start, required fair-weather fish, Fishing Mastery optional objective, Riften/Ivarstead fishing guidance, reward, key, and completion boundary. |
| SRC-001735 | Skyrim:List of Fair Weather Fish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:List_of_Fair_Weather_Fish | 2026-05-29 | Used for the quest document source and required fish list. |
| SRC-001736 | Skyrim:Fishing Mastery, v1 | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_Mastery,_v1 | 2026-05-29 | Used for the back-room Riften Fishery copy after beginning Catch of the Day. |
| SRC-001692 | Skyrim:Fishing (activity) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_(activity) | 2026-05-29 | Used for Fishing Supplies activation, biome/weather mechanics, active quest catch support, clear-weather lake/stream catch tables, Lake Honrich supplies, and Riften canal stream spot. |
| SRC-001737 | Skyrim:Riften Fishery | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Riften_Fishery | 2026-05-29 | Used for Riften Fishery dock Fishing Supplies, Fishing Rod, Lake Honrich location, and temperate-lake fishery context. |

## Evidence Summary

UESP's `Catch of the Day` page says Swims-In-Deep-Water gives the quest at Riften Fishery, hands over `List of Fair Weather Fish`, and requests Carp, Glassfish, Goldfish, and Pogfish. It says `Fishing Mastery, v1` is on a shelf in the room behind Swims and that all four requested fish can be caught in warmer Skyrim streams and lakes, including the Riften docks and the river toward Ivarstead. The quest stages close when the player gives Swims all requested fish; the listed reward state includes gold and the Riften Fishery Key.

UESP's `List of Fair Weather Fish` page matches the same four fish and identifies the note as given by Swims-In-Deep-Water when the related quest starts. UESP's `Fishing Mastery, v1` page places the book on a Riften Fishery back-room shelf after beginning `Catch of the Day`.

The Fishing activity page says Fishing requires a Fishing Rod at Fishing Supplies and that catches depend on biome, weather, rod, population, time, and active quests. Its biome tables place Glassfish and Goldfish in clear-weather temperate lakes, Pogfish in temperate streams, and Carp in clear-weather temperate lakes or streams. Its location table lists the Riften Fishery/Lake Honrich fishing supplies as a lake spot and the Riften canal spot as a stream spot. The Riften Fishery page separately confirms Fishing Supplies and a Fishing Rod at the Fishery docks on Lake Honrich.

## Confidence and Open Questions

Confidence is high for the quest start, document handling, required fish list, clear-weather biome split, Riften-area fishing locations, and turn-in boundary.

The remaining uncertainty is operational catch variance, not route structure. The guide handles that by naming source-backed spots and weather conditions while avoiding save reloads for ordinary catch luck.

## Linked Records

OBJ-000592; OBJ-001398; OBJ-001445; OBJ-001900; OBJ-001905; OBJ-001906; OBJ-001910; CHK-QUESTS-0621; CHK-BOOKS-2469; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/books/book-document-locations.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
