# SN-000191 - Bittercup Branches and Fortunate Son Route

Date: 2026-05-13

Task context: TB-035-MR-058 final-guide expansion.

## Sources

| Source ID | Source | Tier | URL | Accessed | Use |
| --- | --- | --- | --- | --- | --- |
| SRC-000062 | Skyrim:A Dying Wish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_Dying_Wish | 2026-05-11 | Existing source for Bittercup start, three altar choices, path rewards, Giant's Tooth, Ironwood Soup, Rulnik, and Ironwood Fruit vendor unlock. |
| SRC-000261 | Skyrim:Bittercup Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bittercup_Items | 2026-05-12 | Existing source for Bittercup item-member list, item exclusions, Spiked Sujamma, Master Transmute, and route-resolution gaps. |
| SRC-001388 | Skyrim:Fortunate Son | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fortunate_Son | 2026-05-13 | Fortune path, Spiked Vial/Sujamma route, Cuinanthil seal, courier disguise, vault sequence, Ernanthil reward, and Master Transmute chest. |
| SRC-001389 | Skyrim:The Pit (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Pit_(quest) | 2026-05-13 | Power branch dungeon route, Prisoner's Note, Grand Champion rewards, Pit Key, Pit Fighter's Note, belongings recovery, and branch completion. |
| SRC-001390 | Skyrim:The Pit (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Pit_(place) | 2026-05-13 | The Pit location context and Falkreath Watchtower-area exit. |
| SRC-001391 | Skyrim:Roadside Ruins | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Roadside_Ruins | 2026-05-13 | Roadside Ruins clearable status, spriggan, Bittercup altar site, chest, and `Catalogue of Weapon Enchantments` copy. |
| SRC-001392 | Skyrim:Falkreath Watchtower | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Falkreath_Watchtower | 2026-05-13 | Falkreath Watchtower clearable status, necromancer, and `Liminal Bridges` copy. |
| SRC-001393 | Skyrim:Iron Tusk Cave | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Iron_Tusk_Cave | 2026-05-13 | Nothing branch cave, Ironwood Fruit harvest, spriggan fight, and Ironwood Tree source. |
| SRC-001394 | Skyrim:Dead Man's Drink | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dead_Man%27s_Drink | 2026-05-13 | Dead Man's Drink rented-room placement for `Mysterious Altar`. |
| SRC-001395 | Skyrim:Silver-Blood Inn | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Silver-Blood_Inn | 2026-05-13 | Markarth inn services and cooking-pot support for Spiked Sujamma. |
| SRC-001396 | Skyrim:The Warrens | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Warrens | 2026-05-13 | Warrens location context for Fortunate Son courier/vault route. |
| SRC-001471 | Skyrim:Skaal Village Dialogue | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skaal_Village_Dialogue | 2026-05-13 | Morwen's Bera necklace favor and Falkreath Runil delivery during the Solstheim-to-Falkreath handoff. |

## Route decisions

The canonical route keeps the Fortune path because `Fortunate Son` is the path that provides the fixed `Spell Tome: Master Transmute` source in Eslaf's room. The Power and Nothing paths remain compact hard-save branches from `HS-AE-BITTERCUP-ALTAR` because UESP ties Grand Champion's Sword/Helm to Power and Rulnik/Rulnik's Dagger/Ironwood Soup to Nothing.

The guide now starts Bittercup from Dead Man's Drink after the Solstheim Ghosts/Trueflame block. This timing is late enough that Scholar's Insight is already active, and it puts Falkreath Watchtower and Roadside Ruins on the same Falkreath route. The selected skill-book copies therefore move to `Liminal Bridges` at Falkreath Watchtower and `Catalogue of Weapon Enchantments` at Roadside Ruins.

The Power branch explicitly handles `The Pit`, `Prisoner's Note`, Grand Champion's Sword, Grand Champion's Helm, `On the Bittercup`, Pit Key, `Pit Fighter's Note`, and belongings recovery. Because the branch is discarded, it also drinks the branch-copy of the Bittercup once so the consumed/empty-cup state is experienced without consuming the main-route Bittercup.

The Nothing branch explicitly handles `Note from the Temple of Kynareth`, Harlaug's Giant's Tooth ferry, Iron Tusk Cave, Ironwood Fruit, quest Ironwood Soup, Acolyte Aldren, Rulnik Wind-Strider, Rulnik's Dagger, the Bittercup, and `On the Bittercup`. Main continuity still returns to the altar save before selecting Fortune.

The Fortune main route uses the Ernanthil-side approach because it avoids depending on a very hard Speech check, uses the Solstheim Sujamma prep already available at Raven Rock, and reaches the Fortunate Son vault naturally. The route creates Spiked Sujamma at the Silver-Blood Inn, pickpockets Cuinanthil's Family Seal, uses the courier disguise and steward letter, follows Cuinanthil to the vault, receives the Fortune reward from Ernanthil, then kills Ernanthil after the reward dialogue to acquire `Ernanthil's Journal`. The fixed Master Transmute tome is taken and read from the large chest in Eslaf's room.

The main-route Bittercup is preserved unconsumed under the project's unique-item preservation policy. The ordinary/Hot Ironwood Soup and Ironwood Fruit alchemy-effect rows remain for the later alchemy/cooking reconciliation because the Nothing branch is reloaded and the main route only unlocks later Ironwood Fruit access through Khajiit caravans.

Morwen's Bera necklace favor starts before leaving Solstheim and delivers to Runil during the Falkreath Bittercup stop. The reward turn-in waits until the next Skaal Village visit, keeping the quest split to the minimum natural mainland handoff instead of leaving it for late cleanup.

## Open questions

The Bittercup item table lists Potion of Blood, Mysterious Potion, and Ironwood Soup Elixir, but the fetched quest/place pages used for this pass did not identify a deterministic pickup action for them. Internal coverage marks those member rows for later route-resolution rather than inventing an acquisition step.

## Linked records

Objective rows: OBJ-000439, OBJ-000535, OBJ-000572, OBJ-000573, OBJ-000574, OBJ-000755, OBJ-000841, OBJ-000851, OBJ-000919, OBJ-001380, OBJ-001493, OBJ-002035, OBJ-002132, OBJ-002254, OBJ-002416, OBJ-002421, OBJ-002675.

Checklist rows: CHK-QUESTS-0534, CHK-QUESTS-0579, CHK-QUESTS-0580, CHK-QUESTS-0582, CHK-SPELLS-0843, CHK-LOCATIONS-1052, CHK-LOCATIONS-1200, CHK-BOOKS-1871, CHK-BOOKS-1999, CHK-BOOKS-2454, CHK-BOOKS-2463, CHK-BOOKS-2502, CHK-LEARNED-ALCHEMY-EFFECTS-3276 through CHK-LEARNED-ALCHEMY-EFFECTS-3279.

Files updated: `drafts/final-guide/main-guide-v1.md`, `data/guide-coverage/main-guide-v1-coverage.csv`, `data/constraints/progression-source-selections.csv`, `docs/main-guide-v1-expansion-plan.md`, `docs/task-board.md`, and `docs/session-handoff.md`.
