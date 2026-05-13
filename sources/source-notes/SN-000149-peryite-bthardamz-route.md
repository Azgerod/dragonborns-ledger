# SN-000149 - Peryite And Bthardamz Route

Status: route-writing source note for TB-035-MR-021.

## Scope

This note supports the v1 guide section `Peryite's Shrine And Bthardamz`. The section reshapes the old `Daedric Matrix` scaffold into the Daedric quest that naturally belongs after the first Aetherium Reach leg: `The Only Cure`, Shrine to Peryite, Bthardamz, Afflicted's Note, and Spellbreaker. Other Daedric quests remain assigned to later geography, level, branch, or follower-state bundles.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000011 | Skyrim:Daedric Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Daedric_Quests | 2026-05-11 | Daedric quest inventory, Daedric Influence, Oblivion Walker artifact accounting, and non-qualifying artifact caveats. |
| SRC-000012 | Skyrim:Artifacts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Artifacts | 2026-05-11 | Base artifact inventory and Spellbreaker as a Daedric artifact. |
| SRC-000726 | Skyrim:The Only Cure | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Only_Cure | 2026-05-13 | Level gate, Kesh start path, required offering ingredients, ingredient update workaround, Kesh incense bug, Bthardamz objective, Orchendor, and Spellbreaker reward. |
| SRC-000727 | Skyrim:Shrine to Peryite | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shrine_to_Peryite | 2026-05-13 | Shrine marker, Kesh, shrine table contents, The Buying Game placement, unused cooking pot, and unmarked nearby loot audit. |
| SRC-000728 | Skyrim:Bthardamz | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bthardamz | 2026-05-13 | Bthardamz zones, Afflicted's Note, Biography of the Wolf Queen, Orchendor, Reality & Other Falsehoods, elevator key, and clear-tag/body bugs. |
| SRC-000729 | Skyrim:Reachwater Rock | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Reachwater_Rock | 2026-05-13 | Remote river rowboat containing a Flawless Ruby and Reachwater Rock entry boundary. |
| SRC-000730 | Skyrim:Karthwasten | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Karthwasten | 2026-05-13 | Fenn's Gulch Mine smelter area and loose silver ingots. |
| SRC-000731 | Skyrim:Silver | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Silver | 2026-05-13 | Silver Ingot creation/acquisition and Moth gro-Bagol selling Silver Ingots at all levels. |
| SRC-000732 | Skyrim:Vampire Dust | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Vampire_Dust | 2026-05-13 | Vampire Dust drops from all vampires and The Only Cure requirement. |
| SRC-000733 | Skyrim:Deathbell | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Deathbell | 2026-05-13 | Deathbell ingredient, The Only Cure requirement, and later alchemy-effect/ingredient context. |
| SRC-000734 | Skyrim:Grave Concoctions | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Grave_Concoctions | 2026-05-13 | Falkreath alchemy shop and purchasable Deathbell samples. |

## Route Decisions

`The Only Cure` is routed immediately after Deep Folk Crossing because the player is already in the northern Reach and the section can resolve Shrine to Peryite, Bthardamz, and Spellbreaker without colliding with late Thieves, Sky Haven, or Aetherium boundaries. The level-12 Kesh gate should be satisfied long before this point in the expanded route.

The offering is made deterministic by retrospective inventory staging. The guide now buys one Deathbell from Grave Concoctions during the Falkreath/Dengeir pass and saves one Vampire Dust from Bloodlet Throne. The current Peryite section then sources the remaining two ingredients in the Reach: the Flawless Ruby from the remote rowboat north of Reachwater Rock and the Silver Ingot from Karthwasten/Fenn's Gulch, with Moth gro-Bagol as a non-random fallback if the loose ingot is owned on the player's save. The route does not ask the player to depend on random apothecary stock or random mining gems.

The rowboat Flawless Ruby is used without entering Reachwater Rock. Reachwater Rock remains protected for the later level-36 `Forbidden Legend`-linked route; the player-facing guide includes a short local warning because it sends the player near the cave entrance area for a different purpose.

The Shrine to Peryite route records the discoverable shrine marker, speaks to Kesh, and uses the source-listed item-objective workaround when the player already has the four ingredients. The guide explicitly avoids talking to Kesh while he mixes the incense because the quest source records a stage-update bug in that window. `The Buying Game` is left closed because the selected progression copy is the later Bards College copy and Kesh owns the shrine-table items.

Bthardamz is routed as a quest-location completion rather than a reliable map-clear objective. UESP records Bthardamz as not normally showing a cleared state because Orchendor is not tagged as a boss, even though the route can complete `The Only Cure` by killing him. The player-facing guide therefore marks Bthardamz only after Orchendor is dead and the elevator exit is used, and it tells the player not to wait for a map clear tag. The Orchendor body/key bug is covered with the source-listed leave-and-reenter workaround.

Afflicted's Note is placed in this section because it is a single-support quest document in Bthardamz. The local skill-book copies are audited but not routed as reads: `Biography of the Wolf Queen` in Bthardamz Dwelling is a duplicate of the selected Blue Palace source, `Reality & Other Falsehoods` on Orchendor is a duplicate of the selected Snow-Shod Farm source, `The Buying Game` at the shrine is a duplicate of the selected Bards College source, and nearby unmarked `Incident at Necrom`/`The Art of War Magic`/Reachwater `Death Blow of Abernanit` candidates are not coherent reads in this pass.

The old broad Daedric matrix is not forced into this single Reach section. Clavicus Vile belongs with a Falkreath/Haemar/Rimerock or Haafingar loop, Meridia with Statue to Meridia/Kilkreath and the Haafingar coast, Sanguine with the actual Sam Guevenne inn state and Eastmarch/Morvunskar path, Mephala with a Whiterun/Balgruuf visit after level 20, Malacath with the Orc/Forgemaster/Largashbur bundle, Boethiah with level 30 and Knifepoint/follower sacrifice planning, Azura and Hermaeus Mora with northern/College routing, Mehrunes Dagon with Dawnstar and Razor-piece geography, and Vaermina with the later Dawnstar/Nightcaller Temple section.

## Coverage Notes

This pass directly places `The Only Cure`, `Find Kesh at the Peryite Shrine`, Shrine to Peryite discovery, Bthardamz discovery/completion, Afflicted's Note, and Spellbreaker. Oblivion Walker advances from 4 of 15 to 5 of 15 qualifying artifacts.

Held Daedric rows are deliberately mapped to later route bundles rather than left in a vague player-facing matrix. No TB-035-MR-021 `NEEDS ROUTE RESOLUTION` notes remain.
