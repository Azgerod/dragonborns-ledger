# Appendices v0

Status: TB-036 draft generated from current guide and coverage artifacts.

These appendices are reference and verification material for `main-guide-v1.md`. The main guide remains the execution source. If a table here exposes a missing route instruction, fix the guide and coverage tracker rather than treating this appendix as the only instruction.

## Appendix A - Coverage Snapshot

Final objective status totals:

| Metric | Count | Notes |
| --- | --- | --- |
| objective_rows_processed | 2789 | All rows from data/objectives/objectives.csv were classified. |
| placed_in_main_guide | 2577 | Non-branch, non-option, non-excluded, non-unresolved objective rows represented in the self-contained guide or promoted guide reference surfaces. |
| branch_handled | 43 | Canonical branch_route objective rows handled by branch-first/reload guide blocks after unresolved rows are counted separately. |
| option_default_handled | 11 | Canonical option_list objective rows represented by route defaults and option/default guide surfaces. |
| excluded | 19 | Objective rows with canonical excluded placement or explicit guide/coverage exclusion after unresolved rows are counted separately. |
| unresolved | 139 | Objective rows with explicit NEEDS ROUTE RESOLUTION coverage, including unresolved branch or appendix rows. |
| total_classified_objective_rows | 2789 | Should equal objective_rows_processed. |

Raw objective route-placement counts before final-status priority rules:

| Route placement | Count | Notes |
| --- | --- | --- |
| appendix | 27 | Raw route_placement count from data/objectives/objectives.csv before final-status priority rules. |
| branch_route | 43 | Raw route_placement count from data/objectives/objectives.csv before final-status priority rules. |
| excluded | 15 | Raw route_placement count from data/objectives/objectives.csv before final-status priority rules. |
| main_route | 2693 | Raw route_placement count from data/objectives/objectives.csv before final-status priority rules. |
| option_list | 11 | Raw route_placement count from data/objectives/objectives.csv before final-status priority rules. |

Generated audit artifacts:

| Artifact | Rows | Recommended-action counts |
| --- | --- | --- |
| main-guide-v1-appendix-audit.csv | 107 | none: 107 |
| main-guide-v1-book-document-audit.csv | 1780 | none: 1693, none_existing_route_resolution: 87 |
| main-guide-v1-branch-audit.csv | 76 | none: 76 |
| main-guide-v1-checklist-id-audit.csv | 3697 | none: 3697 |
| main-guide-v1-collectible-audit.csv | 249 | none: 227, none_existing_route_resolution: 22 |
| main-guide-v1-crafting-progression-audit.csv | 1498 | none: 1404, none_existing_route_resolution: 94 |
| main-guide-v1-exclusion-audit.csv | 320 | none: 320 |
| main-guide-v1-location-audit.csv | 919 | none: 915, none_existing_route_resolution: 4 |
| main-guide-v1-objective-id-audit.csv | 2789 | none: 2789 |
| main-guide-v1-option-default-audit.csv | 75 | none: 75 |
| main-guide-v1-radiant-counter-audit.csv | 234 | none: 189, none_existing_route_resolution: 45 |

## Appendix B - Guide Section Index

| Line | Level | Heading |
| --- | --- | --- |
| 7 | Part | Guide Conventions |
| 27 | Part | Route Start and Global Setup |
| 29 | Section | Setup and Save Baseline |
| 52 | Part | Early Warm-Core Stabilization |
| 54 | Section | Helgen, Riverwood, and First Survival Loop |
| 74 | Section | First Day in Whiterun |
| 100 | Section | Bleak Falls Barrow and First Dragon |
| 121 | Section | Saadia, First Horse, Falkreath Mead, and Western Road Support |
| 140 | Section | Rising Dead Early Activation |
| 149 | Section | Guardian Stones Cache and Whiterun Farm Loop |
| 165 | Section | Halted Stream and Silent Moons Level Gate |
| 200 | Section | Goldenhills Farm and Rorikstead |
| 233 | Part | Companions, Falkreath, and Southern Warm Expansion |
| 235 | Section | Companions Entry |
| 262 | Section | Beast Blood and the Silver Hand |
| 282 | Section | Falkreath Land, Lakeview Foundation, and Glenmoril Coven |
| 312 | Section | Southern Warm Corridor |
| 350 | Section | Hircine and Bloated Man's Grotto |
| 371 | Part | Riften, Thieves Setup, and Southeast Support |
| 373 | Section | First Riften Visit and Guild Doorway |
| 415 | Section | Goldenglow, Honningbrew, Solitude, and Snow Veil |
| 470 | Section | Riften Thaneship, Frost, and Rift Roads |
| 547 | Section | Nightingale Armor Readiness Check |
| 557 | Part | Reach, Markarth, Aetherium, and Peryite |
| 559 | Section | Markarth, Nchuand-Zel, and Old Hroldan |
| 598 | Section | Markarth Prison, Daedric Rites, and Reach Redoubts |
| 649 | Section | Arkngthamz and the First Aetherium Shards |
| 664 | Section | Peryite's Shrine and Bthardamz |
| 688 | Section | Whiterun Mephala Interlude |
| 700 | Part | Windhelm, Main Quest Staging, and Eastmarch |
| 702 | Section | Windhelm Murder Investigation and White Phial |
| 734 | Section | High Hrothgar, Ustengrav, Morthal, and the Embassy |
| 788 | Section | Windhelm Follow-Up and Eastmarch Roads |
| 866 | Part | Solitude, Bards, Shield Gate, and Dark Brotherhood |
| 868 | Section | Solitude Coast, Dragon Bridge, Wild Horse, and Wolfskull |
| 899 | Section | Bards College, Lost Library, and Instrument Roads |
| 939 | Section | Potema, Shield of Solitude, and Bone Wolf |
| 963 | Section | Haafingar Caves, Volskygge, and Night Hunter |
| 990 | Section | Cicero, Aventus, and the Sanctuary Door |
| 1010 | Section | First Brotherhood Contracts and Muiri's Revenge |
| 1031 | Section | Whispers, Solitude Jobs, Nazir Contracts, and the Wedding Assassination |
| 1088 | Section | Security, Shadowmere, and the Brotherhood Endgame |
| 1166 | Part | Pale, Winterhold, College, and Level-36 Locks |
| 1168 | Section | Dawnstar, Vaermina, and Cold-Weather Setup |
| 1194 | Section | Winterhold, College Entry, and Saarthal |
| 1236 | Section | The Black Star and Ilinalta's Deep |
| 1247 | Section | Dawnstar, Pale Blade, and Heljarchen |
| 1304 | Section | Fellglow Keep and Good Intentions |
| 1326 | Section | Mzulft and the Winterhold Crisis |
| 1348 | Section | Labyrinthian and the Eye of Magnus |
| 1373 | Section | Gauldur Legend Finale |
| 1392 | Section | College Errands, Arniel, Septimus, and Aetherium |
| 1419 | Part | Level 46 Reward Loop, Civil War, and Late Main Quest |
| 1421 | Section | Karthspire, Sky Haven, and Dragonbane |
| 1441 | Section | Nightingale Rewards and the Skeleton Key |
| 1471 | Section | Viriya Fishing, Bronze Water, and Wave Breaker |
| 1505 | Section | Guild Restoration and Amulet of Articulation |
| 1544 | Section | Whiterun Property, Western Caves, Gray-Mane Rescue, and Onmund |
| 1569 | Section | Civil War Stormcloak Branch |
| 1590 | Section | Imperial Civil War |
| 1620 | Section | Gildergreen Renewal After the War |
| 1632 | Section | Blades Research, Blackreach, and the Fallen |
| 1697 | Section | Paarthurnax and Blades Branch |
| 1707 | Part | Dawnguard, Aetherium, and Transformation Coverage |
| 1709 | Section | Dawnguard Fork and Volkihar Branch |
| 1735 | Section | Fort Dawnguard Recruits, Prophet, and Lost Relics |
| 1780 | Section | Dawnguard Worldspaces |
| 1852 | Section | Volkihar Finale Branch Continuation |
| 1874 | Section | Companions Finale, Totems, and Beast-Blood Preservation |
| 1904 | Part | Solstheim and Dragonborn Spine |
| 1906 | Section | Solstheim Entry, Raven Rock Core, and Frostmoon Rings |
| 1956 | Section | Post-Frostmoon Vampire Lord Window |
| 1970 | Section | Temple of Miraak, Skaal, and Stalhrim |
| 2000 | Section | Vahlok's Tomb, Riekling Roads, and Thirsk |
| 2028 | Section | Tel Mithryn, Nchardak, and Kagrumez |
| 2072 | Section | Kolbjorn Excavation and Raven Rock West |
| 2106 | Section | Fahlbtharz, Deathbrand, and Karstaag |
| 2125 | Section | Ghosts of the Tribunal and Trueflame |
| 2151 | Section | Bittercup, the Pit, and Fortunate Son |
| 2173 | Section | Miraak Finale, Lost Knowledge, and Last Black Books |
| 2198 | Section | Vampire Lord Mastery and Rising at Dawn Closeout |
| 2211 | Part | Main Quest Finale, High-Risk AE, and Black Book Defaults |
| 2213 | Section | World-Eater's Eyrie and Dragonslayer |
| 2233 | Section | High-Risk AE Routes and Separate Worldspaces |
| 2265 | Section | Saints, Seducers, and Atronach Forge Tomes |
| 2292 | Section | Black Book Defaults and Progression Switches |
| 2304 | Section | Legends Lost and Sightless Vault |
| 2318 | Part | Final Counters, Progression, and Reconciliation |
| 2320 | Section | Late Location Reconciliation |
| 2324 | Section | Collectible Reconciliation |
| 2344 | Section | Books, Spells, and Documents |
| 2520 | Section | Crafting, Enchanting, Alchemy, and Investments |
| 2853 | Section | Level 78 and Level 80 Gates |
| 2885 | Section | All-Perks Loop |
| 2991 | Section | Late Hold Bounty Representatives |
| 3006 | Section | Urag's Late College Repeatables |
| 3014 | Section | The Gray Cowl of Nocturnal |
| 3034 | Section | Homes, Household, Services, Pets, and Mounts |
| 3085 | Section | Master Criminal Trophy Branch |
| 3108 | Section | Final Reconciliation |

## Appendix C - Named Hard-Save Reference

This table mirrors the current hard-save register for quick review. The guide route still controls when each save is made and reloaded.

| Hard-save name | Place immediately before | Main continuity after branch/audit | Warning-layer note |
| --- | --- | --- | --- |
| `HS-CW-BEFORE-FACTION-OATH` | Civil War faction oath/commitment. | Reload and join Imperial. | Keep separate hard saves before Season Unending or any hold handoff that could skip War Hero. |
| `HS-DG-BLOODLINE` | Lord Harkon's faction choice in `Bloodline`. | Reload and refuse the gift for Dawnguard. | Volkihar branch must verify spouse state for `The Gift` or mark it conditional. |
| `HS-DG-MAIN-RETURN` | Loading `HS-DG-BLOODLINE` for the delayed Volkihar finale branch continuation. | Reload after completing Volkihar-side `Kindred Judgment` and `Destroying the Dawnguard`. | Protects the completed canonical Dawnguard save, Fort Dawnguard survival, and Serana transformation setup while replaying the older faction fork. |
| `HS-DB-ABANDONED-SHACK` | Abandoned Shack commitment. | Reload and join the Dark Brotherhood. | Complete or intentionally skip `Delayed Burial` before commitment. |
| `HS-MQ-PAARTHURNAX` | Killing Paarthurnax. | Reload with Paarthurnax alive. | Blades rebuilding and dragon hunt are branch-only checklist rows. |
| `HS-DRAGONBORN-THIRSK-CHOICE` | Thirsk Mead Hall side choice. | Reload and complete Nord-side `Retaking Thirsk`. | Save again before hall assault and let objective state settle. |
| `HS-AE-GHOSTS-TEMPLE` | Ghosts heretic join/infiltrate versus destruction commitment. | Reload and keep join/infiltrate continuity. | Destroy branch records altered Temple state and lost armory-key/Skull Crusher access. |
| `HS-AE-GHOSTS-PROPAGANDA` | Choosing Her Word Against Theirs propaganda recipients. | Reload and distribute letters to Raven Rock civilians, including Geldis Sadri, for the restored Ashfall services. | Reclamation Priest branch records the priest attack state and `Reclamation Priest's Journal (AE)`. |
| `HS-AE-BITTERCUP-ALTAR` | Bittercup altar path choice. | Reload after Power and Nothing audits; continue Fortune. | Main route keeps Fortune for Master Transmute coverage. |
| `HS-DRAGONBORN-MIRAAK-FINALE` | Reading `Black Book: Waking Dreams` for the level-60 Miraak finale. | Continue after max-tier Miraak equipment is acquired, the Waking Dreams perk-reset service is available, and the Tree Stone/Root of Power state is established. | Protects the level-60 Miraak corpse reward gate and the nonreturnable pre-finale Waking Dreams chapters; not a branch save. |
| `HS-MQ-SKULDAFN` | Releasing Odahviing for the one-way flight to Skuldafn. | Continue after Skuldafn, Sovngarde, `Dragonslayer`, Nahkriin, Diamond Claw, Storm Call: Qo, and Call of Valor are complete. | Protects the one-way Skuldafn/Sovngarde expedition and its missable main-quest finale rewards; not a branch save. |
| `HS-KONAHRIK-MASK-SHRINE` | Equipping the Wooden Mask in the Labyrinthian mask building with all eight base-game dragon priest masks. | Continue after Konahrik is acquired, all eight placed masks are retrieved, the Wooden Mask is still in inventory, and the player has returned to the present-day room. | Protects the mask-tempering loss caveat and the source-listed horseback crash risk; not a branch save. |
| `HS-LEVEL78-LEGENDARY-DRAGON` | Starting the level 78 Legendary Dragon hunt from Jorrvaskr. | Continue after a dragon named Legendary Dragon is killed, `Legend` is observed, and the player returns to owned storage. | Protects the Dawnguard `Legend` trophy check and late dragon encounter bugs; not a reroll save for random assignment or dragon subtype. |
| `HS-EBONY-WARRIOR-CITY` | Entering a major city at level 80 to trigger the Ebony Warrior challenge. | Continue after the challenge dialogue starts `The Ebony Warrior`, the player leaves the city, and the Last Vigil duel prep is complete. | Protects the level-80 challenge trigger and rare approach/dialogue issues; not a branch save. |
| `HS-EBONY-WARRIOR-LAST-VIGIL` | Attacking the Ebony Warrior at Last Vigil. | Continue after `The Ebony Warrior` completes, no unwanted Whiterun bounty remains, and the full body loot is preserved. | Protects Disarm/unique-weapon loss, cliff danger, and possible crime or quest-stat bugs; not a branch save. |
| `HS-BOW-OF-SHADOWS` | Asking the Whiterun steward for `In the Shadows` work during the level-8 Whiterun/Silent Moons pass. | Continue after `In the Shadows` completes, `Bow of Shadows` is looted and preserved, and the steward reward is received. | Protects the PS4-relevant no-assassin spawn risk, Jarl-occupied scene timing, and Bow of Shadows reward state; not a branch save. |
| `HS-DAWNFANG-GUARDIAN-VAULT` | Following the Ghostly Apparition from the Ratway Skritch room into the Guardian Vault. | Continue after `A Soul Divided` is complete, Dawnfang/Duskfang is looted and preserved, `Verrick's Note` has started `Bloodthirst`, and all four Sellonus documents are in invent... | Protects the Guardian Vault crash/spawn bugs, the `Verrick's Note` quest-start bug, the conditional Faldar's Tooth note chain, and Dawnfang/Duskfang reward state; not a branch s... |
| `HS-CHRYSAMERE-FORELHOST` | Approaching Forelhost before speaking to Captain Valmir or starting `Siege on the Dragon Cult`. | Continue after the Lost Paladin is killed, Chrysamere is looted and preserved, and Storm Call: Strun is learned from the battlements word wall. | Protects the Lost Paladin spawn conflict with `Siege on the Dragon Cult`, the unprotected Paladin early-kill risk, and the Chrysamere reward state; not a branch save. |
| `HS-SHADOWREND-ATRONACH` | Touching Shadowrend at the black geyser pool northeast of The Atronach Stone. | Continue after `[player]'s Shadow` is defeated, `Through a Glass, Darkly` completes, Shadowrend is looted and preserved, and no permanent Marked for Death armor-rating damage is... | Protects the player/follower state from the source-listed Shadow Marked for Death armor-rating bug and the Shadowrend reward/form state; not a branch save. |
| `HS-DIVINE-CRUSADER-FOUR-SKULL` | Clearing Four Skull Lookout for `Relics of the Crusader`. | Continue after Remy, Viparth, Eigorn, and Oren are defeated, Viparth's Journal is read/taken, and all twelve Divine Crusader relics are acquired without equipping them. | Protects named bandit/relic acquisition and keeps the relic pickup separate from the later clean-continuity pilgrimage; not a branch save. |
| `HS-DIVINE-CRUSADER-PILGRIMAGE` | Equipping a stored Divine Crusader relic during final reconciliation to start `The Pilgrim's Path`. | Continue after all nine shrines are visited without new infamy actions, `The Pilgrim's Path` completes, and all Divine Crusader relics are returned to owned storage. | Protects the shrine-progress state and the source-listed infamy/restart loop; not a branch save. |
| `HS-AE-THE-CAUSE-RIELLE` | Entering Rielle Crypt during `The Cause`. | Continue after Janus' Journal, all four shards, the Great Welkynd Stone, Norion, Staff of Ehlno Ede, Rielle Key, and Vigilant Enforcer's Journal are handled. | Protects the bug-sensitive Rielle Crypt order and one-way gate closure risk; not a branch save. |
| `HS-AE-THE-CAUSE-DEADLANDS` | Entering Red Scar Cavern before the Vonos/Deadlands chain. | Continue after Vonos, Vonos' Journal, `The Cause`, `The Consequences`, Torment, Scourge, Daedric Gauntlets of Negation, Summon Daedric Horse, and Deadlands ingredients are handled. | Protects the high-risk Red Scar/Deadlands expedition and separate-worldspace reward sweep; not a branch save. |
| `HS-DAEDRIC-BLACK-STAR` | Final Black Star reward choice. | Reload and keep The Black Star. | Azura's Star/Aranea is reward-branch coverage. |
| `HS-DAEDRIC-CLAVICUS` | Final Barbas choice. | Reload, spare Barbas, and take Masque. | Rueful Axe does not carry Oblivion Walker-safe main continuity. |
| `HS-DAEDRIC-HIRCINE-GROTTO` | Hircine outcome after Bolar/grotto state is protected if needed. | Reload and keep Ring of Hircine. | Savior's Hide is reward branch; dual-artifact path is appendix/audit only. |
| `HS-DAEDRIC-MEHRUNES-SHRINE` | Silus shrine decision. | Reload and kill Silus/reforge Mehrunes' Razor. | Spare-Silus outcome is non-artifact branch coverage only. |
| `HS-DAEDRIC-NAMIRA-FEAST` | Verulus/Namira feast outcome. | Reload and complete Ring of Namira path. | Save-Verulus/kill-Eola outcomes are branch-only. |
| `HS-DAEDRIC-VAERMINA-SKULL` | Erandur final choice. | Reload and take Skull of Corruption. | Erandur follower outcome is branch-only. |
| `HS-AETHERIUM-FORGE` | Forging the single Aetherial item. | Audit Staff and Shield, then reload and craft Crown. | Lost to the Ages trophy is separate from the kept reward. |
| `HS-TG-ARTICULATION-REWARD` | Brynjolf's Guild Master reward conversation for the Amulet of Articulation. | Reload until the selected strongest version is awarded, or record an explicit final-route tradeoff if accepting a random version. | Random reward version, not a level or cell-entry lock. |
| `HS-FISHING-NO-CONTEST` | Going to the Morthal contest spot after wagering with Brutius. | Continue after Brutius and both bandits are dead, exactly one `Brutius's Journal` copy has been read, and Warlock's Ring is fished up. | Protects the source-listed raised-ambusher and duplicate-journal progression bugs; not a preferred contest-target reroll. |
| `HS-FISHING-BRONZE-WATER` | Returning to Bronze Water Cave's exterior after Viriya gives `Bounty: Dwarven Investigation`. | Continue after `Beneath Bronze Waters` completes, the Dwarven Fishing Rod is preserved, the two enchanted Irkngthand axes are preserved, and the exterior mechanism state is reso... | Protects the premature Bronze Water Cave Dwemer spider ambush bug and the Dwarven mechanism/reward state; not a branch save. |
| `HS-FISHING-WAVE-BREAKER` | Approaching the Dawnstar fishing shack for `Wave Breaker` before Imperial Civil War changes Dawnstar. | Continue after the Emperor Crab Guardian Spirit is defeated, Viriya is safe, and Skald pays the Dawnstar reward. | Protects Viriya/guard battle state and the source-listed Dawnstar Imperial-control report-to-Jarl bug; not a branch save. |
| `HS-SOLITUDE-SHIELD-LEVEL40` | Falk's final `The Wolf Queen Awakened` reward handoff at level 40+. | Continue after max-tier Shield of Solitude and Bone Wolf courier follow-up are confirmed. | Protects the level-40 Shield reward and the follow-up courier document for `Let Sleeping Wolves Lie`; not a branch save. |
| `HS-WINDHELM-BLOOD-ON-THE-ICE` | First active Windhelm graveyard investigation for `Blood on the Ice`. | Continue after the direct-Wuunferth solution and Calixto kill. | Protect Hjerim entry, evidence handling, Strange Amulet sale, and Wuunferth accusation state; keep until the quest is complete. |
| `HS-FALKREATH-LAND-JOB` | Asking Siddgeir for the Falkreath `Kill the Bandit Leader` target. | Continue if the target is safe now, or park only the Cracked Tusk Keep target for the later Mehrunes route. Reload if Siddgeir assigns Knifepoint Ridge. | Protects the source-backed Knifepoint conflict: clearing Knifepoint before Boethiah can break `Boethiah's Calling`, while Boethiah's active champion state can break the Jarl bou... |
| `HS-SKAAL-STALHRIM-SCENE` | Returning to Skaal Village after freeing the Wind Stone. | Continue after Storn completes `The Fate of the Skaal` and Deor/Fanari finish the Baldor conversation that starts `A New Source of Stalhrim`. | Protects Deor/Fanari scene integrity and the downstream stalhrim crafting unlock. |
| `HS-SKAAL-ABANDONED-LODGE` | Entering the Abandoned Lodge combat/rescue segment of `A New Source of Stalhrim`. | Continue after Baldor is present, rescued, and the map objective points to Northshore Landing. | Protects the Stalhrim Source Map handoff, Baldor rescue, and stalhrim crafting unlock chain. |
| `HS-ALL-PERKS-START` | Starting the late all-perks loop after level-gate content and progression setup are complete. | Continue after level 252+, all 251 normal perk ranks, all 18 skills restored to 100 after final Legendary reset, and all master ritual spell gates are complete. | Protects the high-impact Legendary reset loop, final perk allocation, and post-reset combat viability; not a branch save. |
| `HS-OGHMA-INFINIUM-USE` | Reading Oghma Infinium for the late skill-gap path. | Continue only after the chosen path's expected below-100 skills increase and Oghma is removed in the accepted final state. | Protects the one-time skill-gain choice and documented skill-gain failure risk; not a branch save. |
| `HS-GRAY-COWL-START` | Starting the late `The Gray Cowl of Nocturnal` route after the all-perks audit. | Continue after the thief/beggar start, Bolli strongbox, Solitude deed route, Silverdrift Lair, Gray Cowl reward, and owned-storage unload are complete. | Protects the Riften thief body/start state, Silverdrift hold-unentered policy, reward handoff, cowl guard-hostility warning, and late route baseline; not a branch save. |
| `HS-GRAY-COWL-GISLI` | Starting the Gisli deed handling during `The Gray Cowl of Nocturnal`. | Branch first for the pickpocket-only `Stranger's Final Instructions` variant, then reload and keep the Erikur's House forged-deed path on main continuity. | Protects the source-listed final-instructions variant split and keeps branch-exclusive document coverage out of final continuity. |
| `HS-HOMES-SERVICES-START` | Starting the late homes, household, services, pets, and mounts pass from Tundra Homestead. | Continue after property purchases, household moves, pet checks, and mount checks in the section are complete. | Protects the large gold spend, owned-storage baseline, household move state, and final property-service audit; not a branch save. |
| `HS-VLINDREL-PURCHASE` | Speaking to Raerek for Vlindrel Hall purchase after Igmund's property prerequisites are complete. | Continue after Vlindrel Hall is purchased, furnished, Thane of the Reach is accepted, and Argis is available. | Protects the Reach property purchase state, especially the source-listed steward/purchase caveats and the post-Cidhna Igmund route. |
| `HS-FORGOTTEN-SEASONS-RUNOFF` | Entering Runoff Caverns for `Forgotten Seasons`, `The Dwarven Horse`, and `The Dwarven Crown`. | Continue after all four seasonal wings, Turn of the Seasons, the Dwarven Crown, and the Dwarven Horse are complete. | Protects a long separate dungeon bundle with multiple quest rewards, route-critical parts, and Creation reward state. |
| `HS-LEGENDS-LOST` | Starting the late `Legends Lost` route from New Gnisis Cornerclub. | Continue after all five caravan notes are read/taken, the Attunement Crystal is used, Sightless Pit and Sightless Vault are cleared in one pass, the Messenger is defeated, and b... | Protects the source-listed note-order bugs, one-way Sightless Pit route, Attunement Crystal loss risk, and one-artifact Messenger/vault state. |
| `HS-BLOODCHILL-DINNER` | Entering Bloodchill Cavern for `Guests for Dinner`. | Continue after the mortal-route feast fight, reward handoff, ownership state, and access checks are complete. | Protects Bloodchill ownership and the source-listed Bloodchill door/key/spouse-state caveats; not a branch save. |
| `HS-LAKEVIEW-RAYYA-STEWARD` | Assigning Rayya as the permanent Lakeview Manor steward if she was not already assigned. | Continue after Rayya is steward and Lakeview carriage, bard, horse, livestock, exterior, and furnishing orders are placed. | Protects the default Hearthfire steward/service assignment and paid furnishing state; not a branch save. |
| `HS-WINDSTAD-VALDIMAR-STEWARD` | Assigning Valdimar as the permanent Windstad Manor steward. | Continue after Valdimar is steward and Windstad carriage, bard, horse, livestock, exterior, and furnishing orders are placed. | Protects the default Hearthfire steward/service assignment and paid furnishing state; not a branch save. |
| `HS-HELJARCHEN-GREGOR-STEWARD` | Assigning Gregor as the permanent Heljarchen Hall steward. | Continue after Gregor is steward and Heljarchen carriage, bard, horse, livestock, exterior, and furnishing orders are placed. | Protects the default Hearthfire steward/service assignment and paid furnishing state; not a branch save. |
| `HS-TUNDRA-HOUSEHOLD` | Moving spouse and children into Tundra Homestead. | Continue after Ysolda, Lucia, and Sofie have arrived at Tundra Homestead and child-pet defaults are preserved. | Protects the final household default and adoption move state; not a branch save. |
| `HS-TROPHY-MASTER-CRIMINAL` | Deliberate all-holds bounty escalation. | Reload after trophy pop. | Use controlled nonessential crime escalation, avoid killing quest-critical NPCs, verify 1000 bounty in all nine holds and trophy pop. |
| `HS-FINAL-RECONCILIATION-START` | Starting the final route-state audit after the Master Criminal branch has been reloaded. | Continue after branch-return, progression, unique-item, property, book, spell, crafting, collectible, and unresolved-risk checks pass. | Protects the accepted clean continuity before final QA; not a branch save. |
| `HS-FINAL-CLEAN-CONTINUITY` | Completing the final route-state audit. | Use this save as the accepted end-state for cross-cutting coverage QA. | Protects the post-reconciliation clean route state and separates final QA from earlier branch saves. |
| `HS-RIFT-FROST-LETRUSH` | Frost handoff/outcome. | Keep Frost on the main save. | Alternate Louis/Maven handling remains optional unless TB-034/TB-037 find a final coverage gap. |
| `HS-TEL-MITHRYN-RESEARCH-RADIANTS` | Asking Neloth for the `Azra's Staffs` research assignment after `Old Friends` is complete. | Continue after `Azra's Staffs`, `Experimental Subject (B)`, `Wind and Sand`, and `Whirlwind Cloak` vendor/restock handling are routed or explicitly carried to the Books, Spells,... | Protects randomized Neloth research assignments and the source-listed inaccessible-dungeon bug; not a normal reroll save for preferred target selection. |
| `HS-DRAGONBORN-A-NEW-DEBT` | Mogrul's first post-`Reluctant Steward` debt confrontation in Raven Rock. | Continue after `Mogrul's Orders` is looted/read from the debt collectors and Mogrul is paid the full 1,000 gold. | Protects Mogrul/Slitter hostility, the debt-collector document state, and the safe payment path; not a branch save. |
| `HS-DRAGONBORN-KOLBJORN-FUND-1` through `HS-DRAGONBORN-KOLBJORN-FUND-4` | Each `Unearthed` payment to Ralis Sedarys. | Continue after each funded phase and wait for the next courier letter. | Protects phase progression, Ralis journal handling, and Ahzidal relic availability. |
| `HS-DRAGONBORN-KOLBJORN-RETURN-1` through `HS-DRAGONBORN-KOLBJORN-RETURN-4` | Each Kolbjorn Barrow re-entry after a Ralis courier letter. | Continue after the phase's draugr/relic/journal objectives are complete. | Protects second-visit door state, phase-available relics, the Cyclone word wall, and final Black Book handling. |
| `HS-DRAGONBORN-UNEARTHED-RALIS` | Ralis final outcome. | Spare Ralis on the main save. | Kill outcome remains optional unless TB-034/TB-037 find a final coverage gap. |
| `HS-COLLEGE-VELEHK-SAIN` | Velehk Sain outcome. | Release Velehk for hidden treasure path. | Kill outcome remains optional note. |
| `HS-AE-CIVIL-WAR-CHAMPIONS` | Battle of the Champions side/outcome if separated. | Keep Imperial-aligned handling. | TB-033 validated prototype-level handling; TB-034/TB-037 verify both equipment-set availability before final checklist closure. |

## Appendix D - Branch Reference

Branch rows are branch-experienced unless the guide states they resolve on main continuity before the branch lockout.

| Source | Row ID | Name | Branch | Hard save | Guide location | Audit status |
| --- | --- | --- | --- | --- | --- | --- |
| branch_checklist | CHK-QUESTS-0015 | Paarthurnax (optional) | BR-004 Paarthurnax / Blades | HS-MQ-PAARTHURNAX | Paarthurnax And Blades Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0055 | Rebuilding the Blades | BR-004 Paarthurnax / Blades | HS-MQ-PAARTHURNAX | Blades Research Blackreach And The Fallen \| Main Quest Staging Before Sky Haven \| Paarthurnax And Blades Branch | branch_checklist_resolved_by_main_continuity |
| branch_checklist | CHK-QUESTS-0057 | Dragon Hunting | BR-004 Paarthurnax / Blades | HS-MQ-PAARTHURNAX | Blades Research Blackreach And The Fallen \| Paarthurnax And Blades Branch | branch_checklist_resolved_by_main_continuity |
| branch_checklist | CHK-QUESTS-0099 | Destroy the Dark Brotherhood! | BR-003 Destroy the Dark Brotherhood | HS-DB-ABANDONED-SHACK | Cicero Aventus And The Sanctuary Door | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0133 | Joining the Stormcloaks | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0141 | Liberation of Skyrim | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0143 | Rescue from Fort Neugrad | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0157 | The Battle for Fort Kastav | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_checklist_conditionally_not_applicable |
| branch_checklist | CHK-QUESTS-0159 | The Battle for Fort Hraggstad | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0160 | Battle for Solitude | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0474 | The Bloodstone Chalice | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0481 | Amulets of Night Power | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0483 | Ancient Power | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0485 | Culling the Beast | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0487 | Deceiving the Herd | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0489 | Destroying the Dawnguard | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch \| Volkihar Finale Branch Continuation | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0491 | The Gift | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0492 | The Hunt | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0494 | New Allegiances | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0496 | Protecting the Bloodline | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0498 | Rings of Blood Magic | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0541 | The Chief of Thirsk Hall | BR-006 Thirsk Riekling | HS-DRAGONBORN-THIRSK-CHOICE | Vahlok's Tomb, Riekling Roads, And Thirsk | branch_checklist_covered |
| branch_checklist | CHK-QUESTS-0582 | The Pit | BR-008A Bittercup Power | HS-AE-BITTERCUP-ALTAR | Bittercup, The Pit, And Fortunate Son | branch_checklist_covered |
| branch_checklist | CHK-UNIQUE-GEAR-1561 | Azura's Star | BR-009 Azura's Star | HS-DAEDRIC-BLACK-STAR | The Black Star and Ilinalta's Deep | branch_checklist_covered |
| branch_checklist | CHK-UNIQUE-GEAR-1669 | Savior's Hide | BR-011 Savior's Hide | HS-DAEDRIC-HIRCINE-GROTTO | Hircine And Bloated Man's Grotto | branch_checklist_covered |
| branch_checklist | CHK-UNIQUE-GEAR-1697 | The Rueful Axe | BR-010 Rueful Axe | HS-DAEDRIC-CLAVICUS | Haafingar Caves, Volskygge, And Night Hunter | branch_checklist_covered |
| branch_checklist | CHK-UNIQUE-GEAR-1724 | Aetherial Shield | BR-015 Aetherial Shield | HS-AETHERIUM-FORGE | Arkngthamz And The First Aetherium Shards \| College Errands Arniel Septimus And Aetherium | branch_checklist_covered |
| branch_checklist | CHK-UNIQUE-GEAR-1725 | Aetherial Staff | BR-015 Aetherial Staff | HS-AETHERIUM-FORGE | Arkngthamz And The First Aetherium Shards \| College Errands Arniel Septimus And Aetherium | branch_checklist_covered |
| branch_checklist | CHK-UNIQUE-GEAR-1727 | Amulet of Bats | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-UNIQUE-GEAR-1728 | Amulet of The Gargoyle | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-UNIQUE-GEAR-1741 | Ring of The Beast | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-UNIQUE-GEAR-1742 | Ring of the Erudite | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_checklist_covered |
| branch_checklist | CHK-BOOKS-2512 | Reclamation Priest's Journal (AE) | BR-007 Ghosts destroy-heretics | HS-AE-GHOSTS-PROPAGANDA \| HS-AE-GHOSTS-TEMPLE | Ghosts Of The Tribunal And Trueflame | branch_checklist_covered |
| branch_objective | OBJ-000019 | Paarthurnax | BR-004 Paarthurnax / Blades | HS-MQ-PAARTHURNAX | Paarthurnax And Blades Branch | branch_objective_covered |
| branch_objective | OBJ-000067 | Destroy the Dark Brotherhood! | BR-003 Destroy the Dark Brotherhood | HS-DB-ABANDONED-SHACK | Cicero Aventus And The Sanctuary Door | branch_objective_covered |
| branch_objective | OBJ-000087 | Joining the Stormcloaks | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000088 | The Jagged Crown (Stormcloaks) | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000089 | Message to Whiterun (Stormcloaks) | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000090 | Battle for Whiterun (Stormcloaks) | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000091 | Liberation of Skyrim | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000092 | Rescue from Fort Neugrad | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000093 | Compelling Tribute (Stormcloaks) | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000094 | The Battle for Fort Sungard (Stormcloaks) | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000095 | A False Front (Stormcloaks) | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000096 | The Battle for Fort Snowhawk (Stormcloaks) | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000097 | The Battle for Fort Dunstad (Stormcloaks) | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_conditionally_not_applicable |
| branch_objective | OBJ-000098 | The Battle for Fort Kastav | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_conditionally_not_applicable |
| branch_objective | OBJ-000099 | The Battle for Fort Greenwall (Stormcloaks) | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_conditionally_not_applicable |
| branch_objective | OBJ-000100 | The Battle for Fort Hraggstad | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000101 | Battle for Solitude | BR-001 Stormcloak Civil War | HS-CW-BEFORE-FACTION-OATH | Civil War Stormcloak Branch | branch_objective_covered |
| branch_objective | OBJ-000356 | The Bloodstone Chalice | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch \| Volkihar Finale Branch Continuation | branch_objective_covered |
| branch_objective | OBJ-000357 | Prophet (Vampire) | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch \| Volkihar Finale Branch Continuation | branch_objective_covered |
| branch_objective | OBJ-000374 | Amulets of Night Power | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-000375 | Ancient Power | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-000376 | Culling the Beast | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-000377 | Deceiving the Herd | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-000378 | Destroying the Dawnguard | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch \| Volkihar Finale Branch Continuation | branch_objective_covered |
| branch_objective | OBJ-000379 | The Gift | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-000380 | The Hunt | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-000381 | New Allegiances | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-000382 | Protecting the Bloodline | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-000383 | Rings of Blood Magic | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-000454 | The Chief of Thirsk Hall | BR-006 Thirsk Riekling | HS-DRAGONBORN-THIRSK-CHOICE | Vahlok's Tomb, Riekling Roads, And Thirsk | branch_objective_covered |
| branch_objective | OBJ-000574 | The Pit | BR-008A Bittercup Power | HS-AE-BITTERCUP-ALTAR | Bittercup, The Pit, And Fortunate Son | branch_objective_covered |
| branch_objective | OBJ-001555 | Artifact: The Rueful Axe | BR-010 Rueful Axe | HS-DAEDRIC-CLAVICUS | Retrospective redistributed regional sections; no player-facing Location Counter Sweep dump | branch_objective_covered |
| branch_objective | OBJ-001565 | Artifact: Aetherial Staff | BR-015 Aetherial Staff | HS-AETHERIUM-FORGE | Arkngthamz And The First Aetherium Shards \| College Errands Arniel Septimus And Aetherium \| Mzulft And The Winterhold Crisis | branch_objective_covered |
| branch_objective | OBJ-001581 | Artifact: Savior's Hide | BR-011 Savior's Hide | HS-DAEDRIC-HIRCINE-GROTTO | Hircine And Bloated Man's Grotto | branch_objective_covered |
| branch_objective | OBJ-001585 | Artifact: Aetherial Shield | BR-015 Aetherial Shield | HS-AETHERIUM-FORGE | Arkngthamz And The First Aetherium Shards \| College Errands Arniel Septimus And Aetherium \| Mzulft And The Winterhold Crisis | branch_objective_covered |
| branch_objective | OBJ-001612 | Artifact: Azura's Star | BR-009 Azura's Star | HS-DAEDRIC-BLACK-STAR | The Black Star and Ilinalta's Deep | branch_objective_covered |
| branch_objective | OBJ-001716 | Unique Item: Amulet of Bats | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-001717 | Unique Item: Amulet of The Gargoyle | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-001736 | Unique Item: Ring of The Beast | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-001737 | Unique Item: Ring of the Erudite | BR-002 Volkihar | HS-DG-BLOODLINE | Dawnguard Fork And Volkihar Branch | branch_objective_covered |
| branch_objective | OBJ-002777 | Master Criminal Trophy Set | BR-005 Master Criminal Trophy | HS-TROPHY-MASTER-CRIMINAL | Master Criminal Trophy Branch | branch_objective_covered |
| branch_objective | OBJ-002785 | Rebuilding the Blades | BR-004 Paarthurnax / Blades | HS-MQ-PAARTHURNAX | Blades Research Blackreach And The Fallen \| Karthspire Sky Haven And Dragonbane \| Main Quest Staging Before Sky Haven \| Paarthurnax And Blades Branch | branch_objective_resolved_by_main_continuity |
| branch_objective | OBJ-002786 | Dragon Hunting | BR-004 Paarthurnax / Blades | HS-MQ-PAARTHURNAX | Blades Research Blackreach And The Fallen \| Karthspire Sky Haven And Dragonbane \| Paarthurnax And Blades Branch | branch_objective_resolved_by_main_continuity |

## Appendix E - Option and Default Reference

These rows summarize option-list/default coverage. They do not require the player to branch isolated preference choices.

| Checklist ID | Entry | Category | Option type or objective | Guide location | Audit status |
| --- | --- | --- | --- | --- | --- |
| CHK-QUESTS-0380 | The Bonds of Matrimony | quest | Marriage Completion and Spouse Selection Options | Dawnguard Fork And Volkihar Branch | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2610 | Adelaisa Vendicci | follower_option | permanent_follower_candidate \| personal_steward_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2611 | Aela the Huntress | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Companions Finale, Totems, And Beast-Blood Preservation | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2612 | Agmaer | follower_option | permanent_follower_candidate \| personal_steward_candidate | Fort Dawnguard Recruits Prophet And Lost Relics | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2613 | Ahtar | follower_option | permanent_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2614 | Annekke Crag-Jumper | follower_option | permanent_follower_candidate \| personal_steward_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2615 | Aranea Ienith | follower_option | permanent_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2616 | Argis the Bulwark | follower_option | permanent_follower_candidate \| spouse_candidate | Markarth Nchuand-Zel And Old Hroldan \| TB-038R order and delayed-task repair register | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2617 | Armored Frost Troll | follower_option | animal_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2618 | Armored Troll | follower_option | animal_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2619 | Athis | follower_option | permanent_follower_candidate \| spouse_candidate | Companions Finale, Totems, And Beast-Blood Preservation | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2620 | Beleval | follower_option | permanent_follower_candidate \| personal_steward_candidate | Fort Dawnguard Recruits Prophet And Lost Relics | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2621 | Belrand | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2622 | Benor | follower_option | permanent_follower_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2623 | Borgakh the Steel Heart | follower_option | permanent_follower_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2624 | Bran | follower_option | animal_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2625 | Brelyna Maryon | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Winterhold, College Entry, And Saarthal | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2626 | Calder | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Imperial Civil War \| Windhelm Murder Investigation And White Phial | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2627 | Celann | follower_option | permanent_follower_candidate \| personal_steward_candidate | Fort Dawnguard Recruits Prophet And Lost Relics | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2628 | Cicero | follower_option | permanent_follower_candidate | Security, Shadowmere, And The Brotherhood Endgame | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2629 | Cosnach | follower_option | permanent_follower_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2630 | CuSith | follower_option | animal_follower_candidate | Volkihar Finale Branch Continuation | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2631 | Dark Brotherhood Initiate (female) | follower_option | permanent_follower_candidate | Security, Shadowmere, And The Brotherhood Endgame | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2632 | Dark Brotherhood Initiate (male) | follower_option | permanent_follower_candidate | Security, Shadowmere, And The Brotherhood Endgame | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2633 | Derkeethus | follower_option | permanent_follower_candidate \| spouse_candidate | Riften Thaneship Frost And Rift Roads \| Windhelm Follow-Up And Eastmarch Roads | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2634 | Durak | follower_option | permanent_follower_candidate \| personal_steward_candidate | Fort Dawnguard Recruits Prophet And Lost Relics | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2635 | Eola | follower_option | permanent_follower_candidate \| personal_steward_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2636 | Erandur | follower_option | permanent_follower_candidate | Dawnstar, Vaermina, And Cold-Weather Setup | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2637 | Erik the Slayer | follower_option | permanent_follower_candidate \| personal_steward_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2638 | Faendal | follower_option | permanent_follower_candidate \| personal_steward_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2639 | Farkas | follower_option | permanent_follower_candidate \| spouse_candidate | Companions Finale, Totems, And Beast-Blood Preservation | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2640 | Frea | follower_option | permanent_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2641 | Garmr | follower_option | animal_follower_candidate | Volkihar Finale Branch Continuation | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2642 | Ghorbash the Iron Hand | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2643 | Golldir | follower_option | permanent_follower_candidate \| personal_steward_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2644 | Gregor | follower_option | permanent_follower_candidate \| spouse_candidate | Dawnstar, Pale Blade, And Heljarchen | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2645 | Illia | follower_option | permanent_follower_candidate \| personal_steward_candidate | Riften Thaneship Frost And Rift Roads | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2646 | Ingjard | follower_option | permanent_follower_candidate \| personal_steward_candidate | Fort Dawnguard Recruits Prophet And Lost Relics | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2647 | Iona | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Riften Thaneship Frost And Rift Roads | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2648 | J'zargo | follower_option | permanent_follower_candidate | Winterhold, College Entry, And Saarthal | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2649 | Jenassa | follower_option | permanent_follower_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2650 | Jordis the Sword-Maiden | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2651 | Kharjo | follower_option | permanent_follower_candidate | Dawnstar, Pale Blade, And Heljarchen \| TB-038R order and delayed-task repair register | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2652 | Lob | follower_option | permanent_follower_candidate \| personal_steward_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2653 | Lydia | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2654 | Marcurio | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2655 | Meeko | follower_option | animal_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2656 | Mjoll the Lioness | follower_option | permanent_follower_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2657 | Njada Stonearm | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Companions Finale, Totems, And Beast-Blood Preservation | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2658 | Ogol | follower_option | permanent_follower_candidate \| personal_steward_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2659 | Onmund | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | College Errands Arniel Septimus And Aetherium \| Fellglow Keep And Good Intentions \| Whiterun Property Western Caves Gray-Mane Rescue And Onmund \| Winterhold, College Entry, And... | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2660 | Ralis Sedarys | follower_option | permanent_follower_candidate | Kolbjorn Excavation And Raven Rock West | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2661 | Rayya | follower_option | permanent_follower_candidate \| spouse_candidate | Dawnstar, Vaermina, and Cold-Weather Setup \| Falkreath Land Lakeview Foundation And Glenmoril Coven | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2662 | Ria | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Companions Finale, Totems, And Beast-Blood Preservation | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2663 | Riekling Warrior | follower_option | animal_follower_candidate | Vahlok's Tomb, Riekling Roads, And Thirsk | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2664 | Roggi Knot-Beard | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2665 | Sceolang | follower_option | animal_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2666 | Serana | follower_option | permanent_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2667 | Steadfast Dwarven Sphere | follower_option | animal_follower_candidate | Tel Mithryn, Nchardak, And Kagrumez | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2668 | Steadfast Dwarven Spider | follower_option | animal_follower_candidate | Tel Mithryn, Nchardak, And Kagrumez | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2669 | Stenvar | follower_option | permanent_follower_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2670 | Stray Dog | follower_option | animal_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2671 | Sven | follower_option | permanent_follower_candidate \| personal_steward_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2672 | Talvas Fathryon | follower_option | permanent_follower_candidate \| personal_steward_candidate | Tel Mithryn, Nchardak, And Kagrumez | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2673 | Teldryn Sero | follower_option | permanent_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2674 | Torvar | follower_option | permanent_follower_candidate \| spouse_candidate | Companions Finale, Totems, And Beast-Blood Preservation | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2675 | Ugor | follower_option | permanent_follower_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2676 | Uthgerd the Unbroken | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2677 | Valdimar | follower_option | permanent_follower_candidate \| spouse_candidate | High Hrothgar Ustengrav Morthal And The Embassy | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2678 | Vigilance | follower_option | animal_follower_candidate | Markarth Nchuand-Zel And Old Hroldan | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2679 | Vilkas | follower_option | permanent_follower_candidate \| personal_steward_candidate \| spouse_candidate | Companions Finale, Totems, And Beast-Blood Preservation | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2680 | Vorstag | follower_option | permanent_follower_candidate \| spouse_candidate | Homes Household Services Pets And Mounts | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2681 | Arvak | follower_option | unique_mount | Dawnguard Worldspaces | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2682 | Frost | follower_option | unique_mount | Riften Thaneship Frost And Rift Roads | option_row_covered |
| CHK-RECRUITABLE-FOLLOWERS-2683 | Shadowmere | follower_option | unique_mount | Security, Shadowmere, And The Brotherhood Endgame | option_row_covered |

## Appendix F - Exclusion Reference

The exclusion audit covers all explicit exclusions. Broad regular-book exclusions are summarized here; non-book or objective-linked exclusions are listed below.

Exclusion audit rows by category:

| Category | Rows |
| --- | --- |
| book_document | 1 |
| enchantment | 4 |
| general_book | 309 |
| location | 1 |
| merchant_investment | 1 |
| quest | 3 |
| skill_book | 1 |

Notable non-book or objective-linked exclusions:

| Checklist ID | Entry | Category | Objective ID | Reason | Guide location |
| --- | --- | --- | --- | --- | --- |
| CHK-QUESTS-0045 | Rejoining the College | quest | OBJ-000125 | Failure-state College repeatable placeholder; routing or exclusion deferred to TB-018 | Internal exclusion coverage |
| CHK-QUESTS-0102 | Honor Thy Family | quest | OBJ-000161 | Failure-state Dark Brotherhood radiant placeholder; routing or exclusion deferred to TB-018 | Internal exclusion coverage |
| CHK-QUESTS-0118 | Reparations | quest | OBJ-000142 | TB-044 classifies Reparations as a Thieves Guild failure-state repair quest; the guide uses an avoid/reload policy and treats Vex's payment as recovery only. | First Riften Visit And Guild Doorway |
| CHK-ENCHANTING-EFFECTS-0690 | Fortify Unarmed | enchantment | OBJ-002498 | Excluded audit row from TB-009C; optional destructive branch handling would require an explicit later user decision. | First Riften Visit And Guild Doorway |
| CHK-ENCHANTING-EFFECTS-0706 | Fiery Soul Trap | enchantment | OBJ-002522 | Excluded audit row from TB-009C; optional destructive branch handling would require an explicit later user decision. | Crafting, Enchanting, Alchemy, and Investments |
| CHK-ENCHANTING-EFFECTS-0709 | Huntsman's Prowess | enchantment | OBJ-002523 | Excluded audit row from TB-009C; optional destructive branch handling would require an explicit later user decision. | Crafting, Enchanting, Alchemy, and Investments \| Halted Stream And Silent Moons Level Gate |
| CHK-ENCHANTING-EFFECTS-0714 | Smithing Expertise | enchantment | OBJ-002525 | Excluded audit row from TB-009C; optional destructive branch handling would require an explicit later user decision. | Crafting, Enchanting, Alchemy, and Investments |
| CHK-LOCATIONS-1258 | The Chill* | location |  | TB-031G excludes The Chill from required location coverage because UESP identifies it as unmarked in official Skyrim; the map marker is an Unofficial Skyrim Patch addition outsi... | Internal exclusion coverage |
| CHK-MERCHANTS-1517 | Elrindir | merchant_investment |  | Source table marks investment as bugged without the Unofficial Patch; do not route under official PS4 AE policy. | Internal exclusion coverage |
| CHK-BOOKS-1814 | A Kiss, Sweet Mother | book_document |  | TB-031J excludes this from required book coverage because UESP lists it as a regular List 2 book with multiple copies rather than a skill book quest book AE book spell tome Blac... | Cicero Aventus And The Sanctuary Door |
| CHK-BOOKS-2055 | Pension of the Ancestor Moth | skill_book |  | TB-031J excludes this from skill-book coverage because UESP lists it as a regular List 2 book with no skill-book effect. | Internal exclusion coverage |

## Appendix G - Previous Appendix-Only Rows

These are checklist rows that used to be appendix-only. TB-035-COV-006 verified they are represented in `main-guide-v1.md`; this table is a reviewer index.

| Checklist ID | Entry | Category | Raw group | Guide location | Audit status |
| --- | --- | --- | --- | --- | --- |
| CHK-QUESTS-0388 | The Words of Power | quest | High Hrothgar | Main Quest Staging Before Sky Haven | appendix_row_covered |
| CHK-QUESTS-0534 | Skaal Village Dialogue | quest | Skaal Village Quests | Bittercup, The Pit, And Fortunate Son \| Miraak Finale, Lost Knowledge, And Last Black Books \| Temple Of Miraak, Skaal, And Stalhrim | appendix_row_covered |
| CHK-LOCATIONS-1074 | Giant's Grove | location | Grove | Retrospective redistributed regional sections; no player-facing Location Counter Sweep dump \| TB-038R order and delayed-task repair register | appendix_row_covered |
| CHK-LOCATIONS-1251 | Sundered Towers | location | Nordic Tower | Retrospective redistributed regional sections; no player-facing Location Counter Sweep dump \| TB-038R order and delayed-task repair register | appendix_row_covered |
| CHK-LOCATIONS-1400 | Gallows Hall | location | Player Housing | Windhelm Follow-Up And Eastmarch Roads | appendix_row_covered_by_mapped_objective |
| CHK-LOCATIONS-1402 | Mythic Dawn Camp | location | Camp | High-Risk AE Routes and Separate Worldspaces | appendix_row_covered |
| CHK-LOCATIONS-1403 | Nchuanthumz | location | Player Housing | Homes Household Services Pets And Mounts | appendix_row_covered |
| CHK-LOCATIONS-1405 | Rielle | location | Ayeleid Ruin | High-Risk AE Routes and Separate Worldspaces | appendix_row_covered |
| CHK-LOCATIONS-1413 | The Guardian Vault | location | Ruin | First Riften Visit And Guild Doorway | appendix_row_covered |
| CHK-LOCATIONS-1414 | Blackbone Isle Grotto | location | Cave | Homes Household Services Pets And Mounts | appendix_row_covered_by_mapped_objective |
| CHK-LOCATIONS-1415 | Dead Man's Dread | location | Ship | Homes Household Services Pets And Mounts | appendix_row_covered |
| CHK-LOCATIONS-1417 | Solitude Sewers | location | Root Tunnels | Saints, Seducers, and Atronach Forge Tomes | appendix_row_covered_by_mapped_objective |
| CHK-MERCHANTS-1421 | Madena | merchant_reference | Dawnstar | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1422 | Thoring | merchant_reference | Dawnstar | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1423 | Hadring | merchant_reference | Dawnstar - Nightgate Inn | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1424 | Valga Vinicia | merchant_reference | Falkreath | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1425 | Zaria | merchant_reference | Falkreath | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1427 | Lod | merchant_reference | Falkreath | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1428 | Babette | merchant_reference | Falkreath | Cicero Aventus And The Sanctuary Door \| TB-038R order and delayed-task repair register | appendix_row_covered |
| CHK-MERCHANTS-1430 | Ghorza gra-Bagol* | merchant_reference | Markarth | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1431 | Endon | merchant_reference | Markarth | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1432 | Anton Virane | merchant_reference | Markarth | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1435 | Hogni Red-Arm | merchant_reference | Markarth | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1436 | Kerah | merchant_reference | Markarth | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1437 | Kleppr | merchant_reference | Markarth | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1439 | Gharol | merchant_reference | Markarth - Dushnikh Yal | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1440 | Murbul | merchant_reference | Markarth - Dushnikh Yal | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1441 | Sharamph | merchant_reference | Markarth - Mor Khazgur | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1442 | Shuftharz | merchant_reference | Markarth - Mor Khazgur | Fort Dawnguard Recruits Prophet And Lost Relics | appendix_row_covered |
| CHK-MERCHANTS-1443 | Eydis | merchant_reference | Markarth - Old Hroldan Inn | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1444 | Falion | merchant_reference | Morthal | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1445 | Jonna | merchant_reference | Morthal | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1447 | Imperial Quartermaster | merchant_reference | Most Imperial camps | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1448 | Stormcloak Quartermaster | merchant_reference | Most Stormcloak camps | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1449 | Hunter | merchant_reference | Randomly anywhere in the wilderness | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1450 | Skooma Dealer | merchant_reference | Randomly anywhere in the wilderness | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1451 | Peddler | merchant_reference | Randomly anywhere in the wilderness (being attacked by bandits or Forsworn) | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1452 | Ungrien | merchant_reference | Riften | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1455 | Brand-Shei | merchant_reference | Riften | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1456 | Grelka | merchant_reference | Riften | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1457 | Madesi | merchant_reference | Riften | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1458 | Marise Aravel | merchant_reference | Riften | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1460 | Keerava | merchant_reference | Riften | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1461 | Arnskar Ember-Master | merchant_reference | Riften | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1462 | Herluin Lothaire | merchant_reference | Riften | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1463 | Syndus | merchant_reference | Riften | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1464 | Tonilia | merchant_reference | Riften | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1465 | Vanryth Gatharian | merchant_reference | Riften | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1466 | Vekel the Man | merchant_reference | Riften | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1469 | Gunmar | merchant_reference | Riften - Fort Dawnguard | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1470 | Sorine Jurard | merchant_reference | Riften - Fort Dawnguard | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1471 | Wilhelm | merchant_reference | Riften - Ivarstead | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1472 | Filnjar | merchant_reference | Riften - Shor's Stone | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1473 | Angeline Morrard* | merchant_reference | Solitude | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1476 | Fihada* | merchant_reference | Solitude | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1477 | Addvar | merchant_reference | Solitude | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1478 | Evette San | merchant_reference | Solitude | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1479 | Jala | merchant_reference | Solitude | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1482 | Corpulus Vinius | merchant_reference | Solitude | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1483 | Gulum-Ei | merchant_reference | Solitude | Goldenglow Honningbrew Solitude And Snow Veil | appendix_row_covered |
| CHK-MERCHANTS-1484 | Faida | merchant_reference | Solitude - Dragon Bridge | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1485 | Feran Sadri | merchant_reference | Solitude - Volkihar Keep | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1486 | Hestla | merchant_reference | Solitude - Volkihar Keep | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1487 | Ronthil | merchant_reference | Solitude - Volkihar Keep | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1488 | Halbarn Iron-Fur | merchant_reference | Solstheim - Bujold's Retreat | Vahlok's Tomb, Riekling Roads, And Thirsk | appendix_row_covered |
| CHK-MERCHANTS-1489 | Falas Selvayn | merchant_reference | Solstheim - Ramshackle Trading Post | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1490 | Fethis Alor | merchant_reference | Solstheim - Raven Rock | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1492 | Garyn Ienth | merchant_reference | Solstheim - Raven Rock | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1493 | Milore Ienth | merchant_reference | Solstheim - Raven Rock | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1494 | Geldis Sadri | merchant_reference | Solstheim - Raven Rock | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1495 | Baldor Iron-Shaper | merchant_reference | Solstheim - Skaal Village | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1496 | Edla | merchant_reference | Solstheim - Skaal Village | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1497 | Neloth | merchant_reference | Solstheim - Tel Mithryn | Tel Mithryn, Nchardak, And Kagrumez | appendix_row_covered |
| CHK-MERCHANTS-1498 | Revus Sarvani | merchant_reference | Solstheim - Tel Mithryn | Tel Mithryn, Nchardak, And Kagrumez | appendix_row_covered |
| CHK-MERCHANTS-1499 | Talvas Fathryon | merchant_reference | Solstheim - Tel Mithryn | Tel Mithryn, Nchardak, And Kagrumez | appendix_row_covered |
| CHK-MERCHANTS-1500 | Elynea Mothren | merchant_reference | Solstheim - Tel Mithryn | Tel Mithryn, Nchardak, And Kagrumez | appendix_row_covered |
| CHK-MERCHANTS-1502 | Zaynabi | merchant_reference | Traveling - Dawnstar or Riften | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1503 | Atahbah | merchant_reference | Traveling - Markarth or Whiterun | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1506 | Ma'jhad | merchant_reference | Traveling - Solitude or Windhelm | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1510 | Mallus Maccius | merchant_reference | Whiterun | Goldenglow Honningbrew Solitude And Snow Veil | appendix_row_covered |
| CHK-MERCHANTS-1511 | Sabjorn | merchant_reference | Whiterun | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1512 | Anoriath* | merchant_reference | Whiterun | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1513 | Carlotta Valentia | merchant_reference | Whiterun | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1514 | Fralia Gray-Mane | merchant_reference | Whiterun | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1515 | Eorlund Gray-Mane | merchant_reference | Whiterun | Companions Entry | appendix_row_covered |
| CHK-MERCHANTS-1516 | Hulda | merchant_reference | Whiterun | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1522 | Orgnar | merchant_reference | Whiterun - Riverrun | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1523 | Mralki | merchant_reference | Whiterun - Rorikstead | Goldenhills Farm And Rorikstead | appendix_row_covered |
| CHK-MERCHANTS-1525 | Elda Early-Dawn | merchant_reference | Windhelm | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1526 | Aval Atheron | merchant_reference | Windhelm | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1527 | Hillevi Cruel-Sea | merchant_reference | Windhelm | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1528 | Niranye | merchant_reference | Windhelm | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1529 | Ambarys Rendar | merchant_reference | Windhelm | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1530 | Niranye | merchant_reference | Windhelm | Guild Restoration And Amulet Of Articulation | appendix_row_covered |
| CHK-MERCHANTS-1534 | Iddra | merchant_reference | Windhelm - Kynesgrove | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1535 | Bolar | merchant_reference | Windhelm - Narzulbur | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1536 | Dushnamub | merchant_reference | Windhelm - Narzulbur | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1538 | Dagur | merchant_reference | Winterhold | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1539 | Nelacar | merchant_reference | Winterhold | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1540 | Enthir | merchant_reference | Winterhold - Mage's College | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1541 | Enthir | merchant_reference | Winterhold - Mage's College | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1542 | Tolfdir | merchant_reference | Winterhold - Mage's College | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1543 | Colette Marence | merchant_reference | Winterhold - Mage's College | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1544 | Drevis Neloren | merchant_reference | Winterhold - Mage's College | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1545 | Faralda | merchant_reference | Winterhold - Mage's College | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1546 | Phinis Gestor | merchant_reference | Winterhold - Mage's College | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |
| CHK-MERCHANTS-1547 | Urag gro-Shub | merchant_reference | Winterhold - Mage's College | Final Reconciliation route and merchant reference surfaces | appendix_row_covered |

## Appendix H - Objective-Level Exclusions

These are objective rows classified as excluded by the final coverage summary.

| Objective ID | Objective | Category | Subcategory | Route placement | Guide location |
| --- | --- | --- | --- | --- | --- |
| OBJ-000125 | Rejoining the College | radiant | college_repeatable | excluded | Internal exclusion coverage |
| OBJ-000142 | Reparations | quest | thieves_guild_other | excluded | First Riften Visit And Guild Doorway |
| OBJ-000161 | Honor Thy Family | radiant | dark_brotherhood_radiant | excluded | Internal exclusion coverage |
| OBJ-000207 | Delayed Burial | quest | town_side_quest | excluded | Cicero Aventus And The Sanctuary Door |
| OBJ-000412 | Bandit Attack | radiant | hearthfire_property_defense | excluded | Homes Household Services Pets And Mounts |
| OBJ-001354 | Bounty - Restless Spirits | book_document | ae_book_title | main_route | Goldenhills Farm And Rorikstead |
| OBJ-001420 | Hooded Skeleton | book_document | ae_book_title | main_route | Windhelm Follow-Up And Eastmarch Roads |
| OBJ-001442 | Letter to Naara | book_document | ae_book_title | main_route | Windhelm Follow-Up And Eastmarch Roads |
| OBJ-002063 | Clear Hall of the Vigilant | location | clearable_location | main_route | Dawnstar, Pale Blade, And Heljarchen \| Retrospective redistributed regional sections; no player-facing Location Counter Sweep dump |
| OBJ-002498 | Learn Enchantment: Fortify Unarmed | crafting_unlock | enchantment_learning_excluded | excluded | Crafting, Enchanting, Alchemy, and Investments \| First Riften Visit And Guild Doorway |
| OBJ-002521 | Learn Weapon Enchantment: Briarheart Geis | crafting_unlock | enchantment_learning_excluded | excluded | Crafting, Enchanting, Alchemy, and Investments |
| OBJ-002522 | Learn Weapon Enchantment: Fiery Soul Trap | crafting_unlock | enchantment_learning_excluded | excluded | Crafting, Enchanting, Alchemy, and Investments |
| OBJ-002523 | Learn Weapon Enchantment: Huntsman's Prowess | crafting_unlock | enchantment_learning_excluded | excluded | Crafting, Enchanting, Alchemy, and Investments \| Halted Stream And Silent Moons Level Gate |
| OBJ-002525 | Learn Weapon Enchantment: Smithing Expertise | crafting_unlock | enchantment_learning_excluded | excluded | Crafting, Enchanting, Alchemy, and Investments |
| OBJ-002768 | Child Game: Hide and Seek | misc_objective | optional_activity_excluded | excluded | Internal exclusion coverage |
| OBJ-002769 | Child Game: Tag, You're It! | misc_objective | optional_activity_excluded | excluded | Internal exclusion coverage |
| OBJ-002770 | Inheritance Random Courier Event | misc_objective | random_event_excluded | excluded | Internal exclusion coverage |
| OBJ-002771 | Revenge, Hired Thugs Random Event | misc_objective | random_event_excluded | excluded | Internal exclusion coverage |
| OBJ-002772 | Steal, Thugs Hunt Player Random Event | misc_objective | random_event_excluded | excluded | Internal exclusion coverage |

## Appendix I - Unresolved Route-Resolution Register

These 248 objective rows have explicit `NEEDS ROUTE RESOLUTION` coverage. They are not silent appendix-only coverage; the guide and coverage tracker carry the missing-fact notes.

Unresolved rows by category:

| Category | Count | Notes |
| --- | --- | --- |
| ae_creation | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| book_document | 45 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| collectible | 5 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| crafting_unlock | 12 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| location | 2 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective | 33 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| npc_relationship | 2 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| spell_power | 3 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| trophy | 7 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| unique_item | 29 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |

Unresolved rows by subcategory:

| Subcategory | Count | Notes |
| --- | --- | --- |
| ae_creation:ae_item_consumable_set | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| book_document:ae_book_title | 9 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| book_document:quest_book_title | 36 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| collectible:fishing_special_catch_member | 3 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| collectible:fishing_species_member | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| collectible:fishing_species_set | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| crafting_unlock:ae_ammunition_set | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| crafting_unlock:ae_equipment_crafting_set | 2 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| crafting_unlock:ae_ingredient_material_set | 3 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| crafting_unlock:ae_staff_set | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| crafting_unlock:ae_weapon_crafting_set | 2 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| crafting_unlock:alchemy_ingredient_effect_discovery | 3 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| location:clearable_location | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| location:content_location | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:dragonborn_other_misc | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:dragonborn_raven_rock_misc | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:dungeon_misc_quest | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:eastmarch_misc | 2 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:haafingar_misc | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:hjaalmarch_misc | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:non_journal_quest | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:pale_misc | 2 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:reach_misc | 7 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:rift_misc | 9 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:tutorial_misc | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:whiterun_misc | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| misc_objective:windhelm_misc | 5 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| npc_relationship:housecarl_set | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| npc_relationship:thaneship | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| spell_power:dragon_shout | 2 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| spell_power:standing_stone_choice_set | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| trophy:dragonborn_trophy | 2 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| trophy:general_trophy | 3 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| trophy:misc_objective_trophy | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| trophy:side_quest_trophy | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| unique_item:ae_unique_equipment_parent_set | 3 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| unique_item:unique_armor | 3 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| unique_item:unique_clothing | 7 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| unique_item:unique_jewelry | 5 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| unique_item:unique_misc_item | 1 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |
| unique_item:unique_weapon | 10 | Objective rows classified unresolved by explicit NEEDS ROUTE RESOLUTION coverage. |

Full unresolved objective index:

| Objective ID | Objective | Category | Subcategory | Route placement | Guide location |
| --- | --- | --- | --- | --- | --- |
| OBJ-000219 | Sideways Trophy Set | trophy | side_quest_trophy | main_route | Bards College Lost Library And Instrument Roads \| Blades Research Blackreach And The Fallen \| Bleak Falls Barrow And First Dragon \| Cicero Aventus And The Sanctuary Door \| Dawns... |
| OBJ-000220 | Hero of the People Trophy Set | trophy | misc_objective_trophy | main_route | Dawnstar, Pale Blade, And Heljarchen \| Falkreath Land Lakeview Foundation And Glenmoril Coven \| First Day In Whiterun \| First Riften Visit And Guild Doorway \| Goldenglow Honning... |
| OBJ-000223 | Kill the Bandit Leader (Annekke Crag-Jumper) | misc_objective | eastmarch_misc | main_route | Riften Thaneship Frost And Rift Roads \| TB-038R order and delayed-task repair register \| Windhelm Follow-Up And Eastmarch Roads |
| OBJ-000226 | Dungeon Delving (Roggi's Ancestral Shield) | misc_objective | eastmarch_misc | main_route | Main Quest Staging Before Sky Haven \| TB-038R order and delayed-task repair register \| Windhelm Follow-Up And Eastmarch Roads |
| OBJ-000230 | Kill the Bandit Leader (Brunwulf Free-Winter) | misc_objective | windhelm_misc | main_route | TB-038R order and delayed-task repair register \| Windhelm Follow-Up And Eastmarch Roads \| Windhelm Murder Investigation And White Phial |
| OBJ-000232 | Harsh Master | misc_objective | windhelm_misc | main_route | TB-038R order and delayed-task repair register \| Windhelm Follow-Up And Eastmarch Roads \| Windhelm Murder Investigation And White Phial |
| OBJ-000234 | Dungeon Delving (Queen Freydis's Sword) | misc_objective | windhelm_misc | main_route | TB-038R order and delayed-task repair register \| Windhelm Follow-Up And Eastmarch Roads \| Windhelm Murder Investigation And White Phial |
| OBJ-000237 | Dungeon Delving (Shahvee's Amulet) | misc_objective | windhelm_misc | main_route | TB-038R order and delayed-task repair register \| Windhelm Follow-Up And Eastmarch Roads \| Windhelm Murder Investigation And White Phial |
| OBJ-000239 | Rare Gifts (Torbjorn Shatter-Shield) | misc_objective | windhelm_misc | main_route | First Brotherhood Contracts And Muiri's Revenge \| TB-038R order and delayed-task repair register \| Windhelm Follow-Up And Eastmarch Roads \| Windhelm Murder Investigation And Whi... |
| OBJ-000249 | Rare Gifts (Captain Aldis) | misc_objective | haafingar_misc | main_route | Solitude Coast Wild Horse And Wolfskull \| TB-038R order and delayed-task repair register |
| OBJ-000262 | Rare Gifts (Lami) | misc_objective | hjaalmarch_misc | main_route | High Hrothgar Ustengrav Morthal And The Embassy \| TB-038R order and delayed-task repair register |
| OBJ-000264 | Salty Sea-Dogs | misc_objective | pale_misc | main_route | Dawnstar, Pale Blade, And Heljarchen \| Dawnstar, Vaermina, And Cold-Weather Setup \| TB-038R order and delayed-task repair register |
| OBJ-000265 | Dungeon Delving (Ring of Pure Mixtures) | misc_objective | pale_misc | main_route | Dawnstar, Vaermina, And Cold-Weather Setup \| TB-038R order and delayed-task repair register |
| OBJ-000269 | Gharol's Message | misc_objective | reach_misc | main_route | Final Reconciliation open route-resolution items |
| OBJ-000270 | Kolskeggr Mine | misc_objective | reach_misc | main_route | Markarth Nchuand-Zel And Old Hroldan \| Markarth Prison Daedric Rites And Reach Redoubts \| TB-038R order and delayed-task repair register |
| OBJ-000273 | Sanuarach Mine | misc_objective | reach_misc | main_route | Markarth Prison Daedric Rites And Reach Redoubts \| Peryite's Shrine And Bthardamz \| TB-038R order and delayed-task repair register |
| OBJ-000280 | Buy Dwarven artifact | misc_objective | reach_misc | main_route | Final Reconciliation open route-resolution items |
| OBJ-000282 | Skilled Apprenticeship | misc_objective | reach_misc | main_route | Final Reconciliation open route-resolution items |
| OBJ-000284 | Dungeon Delving (Hrolfdir's Shield) | misc_objective | reach_misc | main_route | Markarth Nchuand-Zel And Old Hroldan \| TB-038R order and delayed-task repair register |
| OBJ-000285 | Coated in Blood | misc_objective | reach_misc | main_route | Markarth Nchuand-Zel And Old Hroldan \| Markarth Prison Daedric Rites And Reach Redoubts \| TB-038R order and delayed-task repair register |
| OBJ-000287 | Smooth Jazbay | misc_objective | rift_misc | main_route | Riften Thaneship Frost And Rift Roads \| TB-038R order and delayed-task repair register |
| OBJ-000295 | Ringmaker | misc_objective | rift_misc | main_route | First Riften Visit And Guild Doorway \| TB-038R order and delayed-task repair register |
| OBJ-000296 | Few and Far Between | misc_objective | rift_misc | main_route | First Riften Visit And Guild Doorway \| Riften Thaneship Frost And Rift Roads \| TB-038R order and delayed-task repair register |
| OBJ-000300 | Distant Memories | misc_objective | rift_misc | main_route | First Riften Visit And Guild Doorway \| Riften Thaneship Frost And Rift Roads \| TB-038R order and delayed-task repair register |
| OBJ-000305 | Ice Cold | misc_objective | rift_misc | main_route | First Riften Visit And Guild Doorway \| TB-038R order and delayed-task repair register |
| OBJ-000308 | Hunt and Gather | misc_objective | rift_misc | main_route | First Riften Visit And Guild Doorway \| Riften Thaneship Frost And Rift Roads \| TB-038R order and delayed-task repair register \| Windhelm Murder Investigation And White Phial |
| OBJ-000312 | Spread the Love | misc_objective | rift_misc | main_route | Markarth Nchuand-Zel And Old Hroldan \| Riften Thaneship Frost And Rift Roads \| TB-038R order and delayed-task repair register |
| OBJ-000313 | Sealing the Deal | misc_objective | rift_misc | main_route | First Riften Visit And Guild Doorway \| TB-038R order and delayed-task repair register |
| OBJ-000314 | Stoking the Flames | misc_objective | rift_misc | main_route | Dawnstar, Vaermina, And Cold-Weather Setup \| First Riften Visit And Guild Doorway \| TB-038R order and delayed-task repair register |
| OBJ-000320 | Dungeon Delving (Amren's Family Sword) | misc_objective | whiterun_misc | main_route | First Day In Whiterun \| Halted Stream And Silent Moons Level Gate \| TB-038R order and delayed-task repair register |
| OBJ-000345 | Sleeping Tree Cave | misc_objective | dungeon_misc_quest | main_route | Final Reconciliation open route-resolution items |
| OBJ-000350 | Enchanting Tutorial | misc_objective | tutorial_misc | main_route | Final Reconciliation open route-resolution items |
| OBJ-000428 | Fetch the Netch | misc_objective | dragonborn_raven_rock_misc | main_route | Solstheim Entry, Raven Rock Core, And Frostmoon Rings \| TB-038R order and delayed-task repair register |
| OBJ-000469 | Sell Stalhrim Armor and Weapons to Ancarion | misc_objective | dragonborn_other_misc | main_route | TB-038R order and delayed-task repair register \| Temple Of Miraak, Skaal, And Stalhrim |
| OBJ-000476 | Stalhrim Crafter Trophy Set | trophy | dragonborn_trophy | main_route | TB-038R order and delayed-task repair register \| Temple Of Miraak, Skaal, And Stalhrim |
| OBJ-000477 | Dragonrider Trophy Set | trophy | dragonborn_trophy | main_route | Collectible Reconciliation \| Final Reconciliation \| Miraak Finale, Lost Knowledge, And Last Black Books |
| OBJ-000696 | Staves Creation Staff Set | crafting_unlock | ae_staff_set | main_route | Final Reconciliation open route-resolution items |
| OBJ-000697 | Rare Curios Ammunition, Ingredient, and Curio Set | crafting_unlock | ae_ingredient_material_set | main_route | Final Reconciliation open route-resolution items |
| OBJ-000698 | Saints and Seducers Item, Material, and Curio Set | crafting_unlock | ae_ingredient_material_set | main_route | Final Reconciliation open route-resolution items |
| OBJ-000699 | Plague of the Dead Mort Flesh Ingredient Set | crafting_unlock | ae_ingredient_material_set | main_route | Rising Dead Early Activation \| TB-038R order and delayed-task repair register |
| OBJ-000703 | Nix-Hound Food and Spell Tome Item Set | ae_creation | ae_item_consumable_set | main_route | Final Reconciliation open route-resolution items |
| OBJ-000704 | Adventurer's Backpack Equipment Set | crafting_unlock | ae_equipment_crafting_set | main_route | Final Reconciliation open route-resolution items |
| OBJ-000706 | Arcane Archer Ammunition, Spell Tome, and Miscellaneous Item Set | crafting_unlock | ae_ammunition_set | main_route | Final Reconciliation open route-resolution items |
| OBJ-000707 | Expanded Crossbow Pack Weapon and Crafting Set | crafting_unlock | ae_weapon_crafting_set | main_route | Final Reconciliation route-resolution list \| Potema Shield Of Solitude And Bone Wolf |
| OBJ-000708 | Elite Crossbows Weapon and Crafting Set | crafting_unlock | ae_weapon_crafting_set | main_route | Final Reconciliation route-resolution list \| Haafingar Caves Volskygge And Night Hunter |
| OBJ-000710 | Fearsome Fists Brawler Gauntlet Set | crafting_unlock | ae_equipment_crafting_set | main_route | Final Reconciliation open route-resolution items |
| OBJ-000738 | Dead Man's Dread Equipment Parent Set | unique_item | ae_unique_equipment_parent_set | main_route | Final Reconciliation open route-resolution items |
| OBJ-000757 | Pets of Skyrim Pet Equipment Parent Set | unique_item | ae_unique_equipment_parent_set | main_route | Final Reconciliation open route-resolution items |
| OBJ-000758 | Wild Horses Map and Saddle Parent Set | unique_item | ae_unique_equipment_parent_set | main_route | Solitude Coast Wild Horse And Wolfskull \| TB-038R order and delayed-task repair register |
| OBJ-000771 | Dismay | spell_power | dragon_shout | main_route | Labyrinthian And The Eye Of Magnus \| Riften Thaneship Frost And Rift Roads \| TB-038R order and delayed-task repair register |
| OBJ-000776 | Fire Breath | spell_power | dragon_shout | main_route | Blades Research Blackreach And The Fallen \| Companions Entry \| TB-038R order and delayed-task repair register |
| OBJ-000788 | Standing Stone Power and Ability Choice Set | spell_power | standing_stone_choice_set | main_route | Helgen Riverwood And First Survival Loop \| TB-038R order and delayed-task repair register |
| OBJ-001090 | Alchemist's Note | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001098 | Argonian Ceremony | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001109 | Boethiah's Proving | book_document | quest_book_title | main_route | Bards College Lost Library And Instrument Roads \| Markarth Nchuand-Zel And Old Hroldan \| TB-038R order and delayed-task repair register |
| OBJ-001121 | Contract (Murder) | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001122 | Contract (Theft) | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001139 | Faralda's Notes | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001154 | Habd's Death Letter | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001164 | Incriminating Letter (Anuriel) | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001166 | Incriminating Letter (DG) | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001188 | The Legend of Red Eagle | book_document | quest_book_title | main_route | Bards College Lost Library And Instrument Roads \| Companions Entry \| Markarth Prison Daedric Rites And Reach Redoubts \| Security, Shadowmere, And The Brotherhood Endgame \| TB-03... |
| OBJ-001190 | Letter from a Friend | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001191 | Letter from Calcemo | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001194 | Letter from Jarl (Jarl's Name) | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001195 | Letter from Jarl (Jarl's Name) of (Jarl's City) | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001202 | Letter of Inheritance | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001204 | Letter to Golldir | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001205 | Letter to Salma | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001209 | Lymdrenn Tenvanni's Journal | book_document | quest_book_title | main_route | First Riften Visit And Guild Doorway \| TB-038R order and delayed-task repair register |
| OBJ-001230 | Note (Mistwatch) | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001231 | Note from Agna | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001234 | Note to Thomas | book_document | quest_book_title | main_route | Bleak Falls Barrow And First Dragon \| TB-038R order and delayed-task repair register |
| OBJ-001245 | Purchase Agreement (Sarthis Idren) | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001251 | Repair Supplies | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001252 | Request for Help! | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001253 | Request from | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001256 | Runil's Journal | book_document | quest_book_title | main_route | Bards College Lost Library And Instrument Roads \| Hircine And Bloated Man's Grotto \| TB-038R order and delayed-task repair register |
| OBJ-001258 | A Scrawled Note | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items \| The Black Star and Ilinalta's Deep |
| OBJ-001285 | Venarus Vulpin's Journal | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001286 | Venarus Vulpin's Research | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001288 | The Warmth of Mara | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001291 | WIKill04RewardLetter | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001292 | WIKill04ThanksLetter | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001299 | Ysolda's Message | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001321 | Letter to Imperial City | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001325 | Note from Mogrul | book_document | quest_book_title | main_route | Bittercup, The Pit, And Fortunate Son \| Black Book Defaults and Progression Switches \| Books, Spells, and Documents \| Fahlbtharz, Deathbrand, And Karstaag \| Final Reconciliation... |
| OBJ-001331 | Scribbles of a Madman | book_document | quest_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001346 | Assembly Line Constructs | book_document | ae_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001385 | Dinner Menu | book_document | ae_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001386 | Ehlhiel's Journal | book_document | ae_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001393 | Eydvina's Note | book_document | ae_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001455 | Manufactory Repair Parts | book_document | ae_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001459 | Mercenary's Note | book_document | ae_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001490 | Please Read Aloud | book_document | ae_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001492 | Possible Vampire Cave | book_document | ae_book_title | main_route | Final Reconciliation open route-resolution items |
| OBJ-001529 | The Restless (book) | book_document | ae_book_title | main_route | Goldenglow Honningbrew Solitude And Snow Veil \| TB-038R order and delayed-task repair register |
| OBJ-001617 | Unique Item: Drainblood Battleaxe | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001621 | Unique Item: Bow of the Hunt | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001622 | Unique Item: Drainspell Bow | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001625 | Unique Item: Glass Bow of the Stag Prince | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001627 | Unique Item: Blade of Sacrifice | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001630 | Unique Item: Borvir's Dagger | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001633 | Unique Item: Rundi's Dagger | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001634 | Unique Item: Shiv | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001642 | Unique Item: Drainheart Sword | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001653 | Unique Item: Trollsbane | unique_item | unique_weapon | main_route | Final Reconciliation open route-resolution items |
| OBJ-001680 | Unique Item: Ironhand Gauntlets | unique_item | unique_armor | main_route | Final Reconciliation open route-resolution items |
| OBJ-001699 | Unique Item: Torturer's Hood | unique_item | unique_armor | main_route | Final Reconciliation open route-resolution items |
| OBJ-001701 | Unique Item: Ulfric's Bracers | unique_item | unique_armor | main_route | Final Reconciliation open route-resolution items |
| OBJ-001704 | Unique Item: Cicero's Boots | unique_item | unique_clothing | main_route | Security, Shadowmere, And The Brotherhood Endgame \| TB-038R order and delayed-task repair register |
| OBJ-001705 | Unique Item: Cicero's Clothes | unique_item | unique_clothing | main_route | Security, Shadowmere, And The Brotherhood Endgame \| TB-038R order and delayed-task repair register |
| OBJ-001706 | Unique Item: Cicero's Gloves | unique_item | unique_clothing | main_route | Security, Shadowmere, And The Brotherhood Endgame \| TB-038R order and delayed-task repair register |
| OBJ-001707 | Unique Item: Cicero's Hat | unique_item | unique_clothing | main_route | Security, Shadowmere, And The Brotherhood Endgame \| TB-038R order and delayed-task repair register |
| OBJ-001708 | Unique Item: Mythic Dawn Robes | unique_item | unique_clothing | main_route | Final Reconciliation open route-resolution items |
| OBJ-001714 | Unique Item: Ulfric's Boots | unique_item | unique_clothing | main_route | Final Reconciliation open route-resolution items |
| OBJ-001715 | Unique Item: Ulfric's Clothes | unique_item | unique_clothing | main_route | Final Reconciliation open route-resolution items |
| OBJ-001718 | Unique Item: Charmed Necklace | unique_item | unique_jewelry | main_route | Goldenglow Honningbrew Solitude And Snow Veil \| TB-038R order and delayed-task repair register |
| OBJ-001724 | Unique Item: Skaal Amulet | unique_item | unique_jewelry | main_route | TB-038R order and delayed-task repair register \| Temple Of Miraak, Skaal, And Stalhrim |
| OBJ-001725 | Unique Item: Yisra's Necklace | unique_item | unique_jewelry | main_route | Final Reconciliation open route-resolution items |
| OBJ-001729 | Unique Item: The Bond of Matrimony | unique_item | unique_jewelry | main_route | Final Reconciliation open route-resolution items |
| OBJ-001731 | Unique Item: Ilas-Tei's Ring | unique_item | unique_jewelry | main_route | Final Reconciliation open route-resolution items |
| OBJ-001744 | Unique Item: Balbus's Fork | unique_item | unique_misc_item | main_route | Collectible Reconciliation \| Final Reconciliation \| Security, Shadowmere, And The Brotherhood Endgame |
| OBJ-001893 | Collectible Set: Fishing Species and Special Catches | collectible | fishing_species_set | main_route | Collectible Reconciliation \| Final Reconciliation |
| OBJ-001907 | Fishing Catch: Juvenile Mudcrab | collectible | fishing_species_member | main_route | Collectible Reconciliation \| Final Reconciliation |
| OBJ-001916 | Fishing Catch: Emperor Crab Guardian Spirit | collectible | fishing_special_catch_member | main_route | Collectible Reconciliation \| Final Reconciliation |
| OBJ-001917 | Fishing Catch: Fangtusk | collectible | fishing_special_catch_member | main_route | Collectible Reconciliation \| Final Reconciliation |
| OBJ-001918 | Fishing Catch: Snippy | collectible | fishing_special_catch_member | main_route | Collectible Reconciliation \| Final Reconciliation |
| OBJ-001935 | Thane of Winterhold | npc_relationship | thaneship | main_route | Bards College Lost Library And Instrument Roads \| TB-038R order and delayed-task repair register \| Winterhold, College Entry, And Saarthal |
| OBJ-001936 | Player Housecarl Set | npc_relationship | housecarl_set | main_route | Bleak Falls Barrow And First Dragon \| TB-038R order and delayed-task repair register |
| OBJ-002169 | Clear Swindler's Den | location | clearable_location | main_route | Retrospective redistributed regional sections; no player-facing Location Counter Sweep dump \| Saadia First Horse And Western Road Support |
| OBJ-002423 | Validate AE Location Coverage: Sightless Vault | location | content_location | appendix | Final Reconciliation open route-resolution items |
| OBJ-002663 | Discover Alchemy Effects: Glassfish | crafting_unlock | alchemy_ingredient_effect_discovery | main_route | Crafting, Enchanting, Alchemy, and Investments \| TB-038R order and delayed-task repair register |
| OBJ-002666 | Discover Alchemy Effects: Goldfish | crafting_unlock | alchemy_ingredient_effect_discovery | main_route | Crafting, Enchanting, Alchemy, and Investments \| TB-038R order and delayed-task repair register |
| OBJ-002676 | Discover Alchemy Effects: Juvenile Mudcrab | crafting_unlock | alchemy_ingredient_effect_discovery | main_route | Crafting, Enchanting, Alchemy, and Investments \| First Riften Visit And Guild Doorway \| TB-038R order and delayed-task repair register |
| OBJ-002759 | Rannveig's Fast Non-Journal Quest | misc_objective | non_journal_quest | main_route | Final Reconciliation open route-resolution items |
| OBJ-002773 | Thief Trophy Set | trophy | general_trophy | main_route | Final Reconciliation open route-resolution items |
| OBJ-002774 | Snake Tongue Trophy Set | trophy | general_trophy | main_route | First Day In Whiterun \| First Riften Visit And Guild Doorway \| TB-038R order and delayed-task repair register |
| OBJ-002779 | Dragon Hunter Trophy Set | trophy | general_trophy | main_route | Bleak Falls Barrow And First Dragon \| Collectible Reconciliation \| TB-038R order and delayed-task repair register \| World-Eater's Eyrie and Dragonslayer |
