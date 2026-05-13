# SN-000157 - Dark Brotherhood Fork And Sanctuary Door

Status: route-writing source note for TB-035-MR-029.

## Scope

This note supports the v1 guide section `Cicero, Aventus, And The Sanctuary Door`. The section routes `Delayed Burial`, Loreius Farm, `Innocence Lost`, the Mysterious Note handoff, `HS-DB-ABANDONED-SHACK`, the branch-only `Destroy the Dark Brotherhood!` outcome, the main-route `With Friends Like These...` commitment, Abandoned Shack discovery, Meeko's Shack, Meeko, Dark Brotherhood Sanctuary discovery, first-entry Sanctuary collectibles, and the `Sanctuary` quest handoff to Nazir's first contracts.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000885 | Skyrim:Delayed Burial | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Delayed_Burial | 2026-05-13 | Cicero/Loreius sequence, help-versus-report outcomes, quest failure window, and horse bug note. |
| SRC-000886 | Skyrim:Loreius Farm | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Loreius_Farm | 2026-05-13 | Farm location, local audit, and crop-sale absence. |
| SRC-000887 | Skyrim:Innocence Lost | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Innocence_Lost | 2026-05-13 | Aventus start, Grelod kill, Aventus reward, courier follow-up, and orphanage state notes. |
| SRC-000888 | Skyrim:Aretino Residence | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Aretino_Residence | 2026-05-13 | Aretino Residence layout, `A Hypothetical Treachery`, and `A Kiss, Sweet Mother`. |
| SRC-000889 | Skyrim:Honorhall Orphanage | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Honorhall_Orphanage | 2026-05-13 | Honorhall layout, Grelod route, and `Purloined Shadows` local copy. |
| SRC-000890 | Skyrim:With Friends Like These... | 2 - UESP | https://en.uesp.net/wiki/Skyrim:With_Friends_Like_These... | 2026-05-13 | Mysterious Note, sleep trigger, Abandoned Shack choice, main join route, reward set, and bugs. |
| SRC-000891 | Skyrim:Abandoned Shack | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Abandoned_Shack | 2026-05-13 | Shack layout, captive hoods, key/map-marker behavior, and nearby `Sacred Witness` copy. |
| SRC-000892 | Skyrim:Destroy the Dark Brotherhood! | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Destroy_the_Dark_Brotherhood! | 2026-05-13 | Destroy branch sequence, Commander Maro, Sanctuary assault, reward, consequences, and bug notes. |
| SRC-000893 | Skyrim:Dark Brotherhood Sanctuary | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dark_Brotherhood_Sanctuary | 2026-05-13 | Sanctuary access, shrouded clothing shelf, Stone of Barenziah, word wall, and container caveats. |
| SRC-000894 | Skyrim:Sanctuary | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Sanctuary | 2026-05-13 | First Sanctuary quest, local collectibles, Nazir first contracts, and Narfi dependency note. |
| SRC-000895 | Skyrim:Meeko's Shack | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Meeko%27s_Shack | 2026-05-13 | Meeko's Shack route, `A Dance in Fire, v6`, and Meeko's return behavior. |
| SRC-000896 | Skyrim:Meeko | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Meeko | 2026-05-13 | Meeko follower availability and fragility notes. |
| SRC-000897 | Skyrim:Execution Hood | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Execution_Hood | 2026-05-13 | Execution Hood item identity and quest relation. |
| SRC-000898 | Skyrim:No Stone Unturned | 2 - UESP | https://en.uesp.net/wiki/Skyrim:No_Stone_Unturned | 2026-05-13 | Dark Brotherhood Sanctuary Stone generation and gem collection caveats. |
| SN-000156 | Haafingar Caves, Volskygge, And Night Hunter Route | Project source note | sources/source-notes/SN-000156-haafingar-caves-volskygge-night-hunter-route.md | 2026-05-13 | Prior hold reasons for Meeko and `The Dainty Sload`. |
| NPC dependencies | Project constraint table | data/constraints/npc-dependencies.md | 2026-05-13 | Erikur vulnerability boundary before `Bound Until Death`. |
| Quest conflicts and hard saves | Project constraint table | data/constraints/quest-conflicts-hard-saves.md | 2026-05-13 | `HS-DB-ABANDONED-SHACK`, `Delayed Burial` window, and join-versus-destroy branch policy. |

## Route Decisions

The Erikur-sensitive `The Dainty Sload` work is not pulled into this section. The project NPC dependency table makes Erikur protection mandatory before any Dark Brotherhood step that makes him vulnerable, specifically `Bound Until Death`; the Abandoned Shack and first Sanctuary entry do not yet create that state. The next Dark Brotherhood main-route pass must still resolve `The Dainty Sload` before the wedding assassination.

`Delayed Burial` is routed before `Innocence Lost` and before any Abandoned Shack choice because UESP records that entering the Dark Brotherhood Sanctuary or starting `Destroy the Dark Brotherhood!` fails the quest. The guide chooses the Cicero-friendly outcome because it preserves Vantus and Curwe, avoids the farm murder consequence, and aligns with the later join route. Loreius Farm is recorded as a location discovery at the same stop; its crop fields and interior are not routed because UESP records no crop-sale service there, and the house contents are ordinary food/loot rather than checklist objectives.

The lost caravan east of Loreius Farm and `Seedy Guard's Note` are audited but not routed. The note starts an AE Creation chain that is not otherwise ready in this section; a short detour just to start a later Creation route would split the related objective bundle.

`Innocence Lost` is routed in one Windhelm-Riften-Windhelm loop: speak to Aventus, kill Grelod, return to Aventus, and preserve the Aretino Family Heirloom. The guide asks for a save before the Aventus turn-in and waits for the Mysterious Note before sleeping because UESP records both the courier note and the possibility that sleeping can start the shack sequence before the note is delivered. The note is a tracked document row, so the route preserves the courier handoff rather than skipping it.

The Aretino Residence copy of `A Hypothetical Treachery` remains closed even though the route enters the house. The current source-selection table names that copy as the provisional representative, but reading a loose skill book now would consume the skill increase before Scholar's Insight. It remains a staged skill-book row for the later reading window unless the selection table is revised.

`HS-DB-ABANDONED-SHACK` is made after the player wakes in the shack and before speaking to Astrid or attacking anyone. The branch route kills Astrid, reports through a city guard and Commander Maro, completes `Destroy the Dark Brotherhood!`, records only the branch outcome, and reloads. Main-continuity Sanctuary collectibles are collected after the reload on the join route instead of being duplicated on the branch save.

On the main route, the guide kills Vasha as a deterministic captive choice, loots one Execution Hood, then speaks to Astrid. The captive choice is not treated as a content branch because UESP makes the quest outcome independent of which captive dies; choosing one target simply keeps the black-box guide deterministic.

Meeko's Shack is routed immediately after leaving the Abandoned Shack because it was deliberately held from the Haafingar cave sweep for this marsh/pet bundle. The guide discovers the shack, records Meeko as available, and leaves `A Dance in Fire, v6` closed because the selected copy for that title is still the Dainty Sload copy.

The first Dark Brotherhood Sanctuary entry is expanded beyond the old fork scaffold because it completes `With Friends Like These...`, unlocks the Dark Brotherhood trophy, and places several checklist objectives in one room: the Shrouded Armor reward set, shrouded clothing set, Sanctuary Stone of Barenziah, Dark Brotherhood Sanctuary map marker, and Marked for Death: Lun word wall. The guide also completes the `Sanctuary` quest by accepting Nazir's first contracts.

`Sithis`, `Sacred Witness`, and the Sanctuary duplicate of `Lost Legends` are not read here. `Sithis` and `Sacred Witness` are skill books before the Scholar's Insight window, and the guide already read `Lost Legends` from the Blue Palace before Folgunthur. The guide warns only at the exact shelf/room being used for nearby shrouded clothing so the player does not accidentally open the books while collecting routed gear.

The Sanctuary is not used as long-term artifact storage. UESP records non-respawning containers, but also records later Sanctuary-destruction and post-`To Kill an Empire` storage caveats. The guide keeps artifact storage with approved owned homes and route-controlled storage.

## Coverage Notes

This pass directly places `Delayed Burial`, Loreius Farm, `Innocence Lost`, Aretino Family Heirloom, Mysterious Note (DB), `HS-DB-ABANDONED-SHACK`, branch-only `Destroy the Dark Brotherhood!`, `With Friends Like These...`, the Dark Brotherhood join trophy, Execution Hood, Abandoned Shack, Meeko's Shack, Meeko, Dark Brotherhood Sanctuary, Shrouded Armor, Shrouded Boots, Shrouded Cowl, Shrouded Gloves, shrouded clothing pieces, the Sanctuary Stone of Barenziah, Marked for Death: Lun, and `Sanctuary`.

Held or staged rows are mapped in coverage rather than expanded as player-facing lists: `The Dainty Sload` and Erikur before `Bound Until Death`, `Seedy Guard's Note` and the Sunder & Wraithguard Creation chain, `A Hypothetical Treachery`, `Purloined Shadows`, `Sacred Witness`, `A Dance in Fire, v6`, `Sithis`, duplicate `Lost Legends`, main-route Blade of Woe, Sanctuary safe-storage, Babette/Nazir training services, and the first Nazir contract targets.

No TB-035-MR-029 `NEEDS ROUTE RESOLUTION` notes remain.
