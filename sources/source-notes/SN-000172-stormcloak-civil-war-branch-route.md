# SN-000172 - Stormcloak Civil War Branch Route

Status: route-writing source note for TB-035-MR-041.

## Scope

This note supports the v1 guide section `Civil War Stormcloak Branch`. The section plays the Stormcloak Civil War from a pre-faction hard save, records branch-exclusive quest outcomes, protects the no-Season-Unending War Hero path, captures General Tullius' Armor as branch-experienced, and then reloads for the canonical Imperial route.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000008 | Skyrim:Stormcloaks | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Stormcloaks | 2026-05-11 | Stormcloak quest inventory, titles, and Season Unending variability. |
| SRC-000009 | Skyrim:Civil War | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Civil_War | 2026-05-11 | Civil War side structure, side-switch boundary, Season Unending interaction, War Hero/Hero of Skyrim context, and Captain Aldis consequence context. |
| SRC-000010 | Skyrim:Season Unending | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Season_Unending | 2026-05-11 | Treaty-state risk and War Hero skip rationale. |
| SRC-000147 | Skyrim:Lord's Mail Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lord%27s_Mail_Items | 2026-05-12 | Castle Dour Lord's Mail note context and reason to hold AE quest-starting material off the temporary branch. |
| SRC-000376 | Skyrim:Battle of the Champions | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Battle_of_the_Champions | 2026-05-12 | Civil War Champions faction alignment context. |
| SRC-001112 | Skyrim:Joining the Stormcloaks | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Joining_the_Stormcloaks | 2026-05-13 | Ice wraith test, Stormcloak oath, starting gear, and Unblooded title. |
| SRC-001113 | Skyrim:The Jagged Crown (Stormcloaks) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Jagged_Crown_(Stormcloaks) | 2026-05-13 | Korvanjund route, Ebony Claw puzzle, hidden gate, Jagged Crown handoff, and side-switch risk. |
| SRC-001114 | Skyrim:Message to Whiterun (Stormcloaks) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Message_to_Whiterun_(Stormcloaks) | 2026-05-13 | Ulfric axe delivery and returned-axe handoff. |
| SRC-001115 | Skyrim:Battle for Whiterun (Stormcloaks) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Battle_for_Whiterun_(Stormcloaks) | 2026-05-13 | Whiterun assault objectives, drawbridge, Balgruuf surrender, and Ulfric report. |
| SRC-001116 | Skyrim:Liberation of Skyrim | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Liberation_of_Skyrim | 2026-05-13 | Required no-treaty Stormcloak hold sequence and treaty-only hold variants. |
| SRC-001117 | Skyrim:Rescue from Fort Neugrad | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rescue_from_Fort_Neugrad | 2026-05-13 | Falkreath liberation route, lake-side prison entry, prisoner rescue, and fort capture. |
| SRC-001118 | Skyrim:Compelling Tribute (Stormcloaks) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Compelling_Tribute_(Stormcloaks) | 2026-05-13 | Raerek blackmail, Amulet of Talos evidence, and caravan ambush route. |
| SRC-001119 | Skyrim:The Battle for Fort Sungard (Stormcloaks) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Battle_for_Fort_Sungard_(Stormcloaks) | 2026-05-13 | No-treaty Stormcloak War Hero fort and fort battle completion. |
| SRC-001120 | Skyrim:A False Front (Stormcloaks) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_False_Front_(Stormcloaks) | 2026-05-13 | Courier interception, forged documents, Morthal delivery, and moving-target isolation. |
| SRC-001121 | Skyrim:The Battle for Fort Snowhawk (Stormcloaks) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Battle_for_Fort_Snowhawk_(Stormcloaks) | 2026-05-13 | Fort Snowhawk battle, Stormblade title, and Stormcloak Officer Armor reward. |
| SRC-001122 | Skyrim:The Battle for Fort Hraggstad | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Battle_for_Fort_Hraggstad | 2026-05-13 | Haafingar fort battle before the Solitude assault. |
| SRC-001123 | Skyrim:Battle for Solitude | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Battle_for_Solitude | 2026-05-13 | Final assault, Castle Dour confrontation, Rikke/Tullius deaths, and branch completion boundary. |
| SRC-001124 | Skyrim:General Tullius | 2 - UESP | https://en.uesp.net/wiki/Skyrim:General_Tullius | 2026-05-13 | General Tullius essential state and death availability during Battle for Solitude. |
| SRC-001125 | Skyrim:General Tullius' Armor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:General_Tullius%27_Armor | 2026-05-13 | Unique armor identity and branch-only acquisition context. |

## Route Decisions

The guide places `HS-CW-BEFORE-FACTION-OATH` immediately before the Stormcloak oath sequence. The branch is played first so every Stormcloak-specific quest and final Solitude outcome can be experienced without carrying Stormcloak final-state consequences into the canonical Imperial save.

The branch deliberately runs before any `Season Unending` treaty. UESP's `Liberation of Skyrim` page says the required Stormcloak hold subset depends on treaty state; on a clean no-treaty Stormcloak branch, the required line is Falkreath, the Reach, Hjaalmarch, and Haafingar. Therefore `The Battle for Fort Dunstad`, `The Battle for Fort Kastav`, and `The Battle for Fort Greenwall` are represented as treaty-state Stormcloak variants and are not routed in this branch. Fort Sungard is the branch's War Hero fort under the no-treaty sequence.

Korvanjund is visited during the branch because `The Jagged Crown` requires it, but the guide does not count Korvanjund's word wall, claw, location records, or other durable collectibles as canonical. Those states vanish on reload and should stay on the later Imperial continuity when Korvanjund is routed there.

Military camp and fort discoveries also occur transiently on the branch. They are not claimed as main-save location checklist completions because the branch reload removes them. The player-facing guide names the camps as quest destinations but leaves camp and fort location coverage to the canonical route or later location pass.

`A False Front` uses a moving courier target between Rorikstead and Dragon Bridge. The guide follows the current random-assignment convention by isolating the courier objective and returning to Galmar rather than routing nearby objectives around a courier position the route cannot predict.

General Tullius' Armor is routed in the branch because Tullius is essential before the Stormcloak final battle and the canonical Imperial route will not kill him. The guide has the player execute Tullius personally and take the armor, then record it as branch-experienced rather than as main-save preserved inventory.

`Battle of the Champions` remains out of the Stormcloak branch. Existing branch notes selected Imperial-aligned handling on the main Civil War route unless final QA proves a checklist-relevant gap, and the branch should not add AE side content that will be erased by the required reload.

`Gift of Kynareth` and `Letter to General Tullius` also remain out of the branch even though the final assault enters Castle Dour. Those are AE main-continuity quest-starting rows, not Stormcloak-exclusive branch content, and the branch reload would erase any progress.

Captain Aldis-sensitive work was already completed earlier in the main route before this branch reaches Battle for Solitude. No additional Aldis player-facing warning belongs in the branch section.

## Coverage Summary

This pass places the Stormcloak branch hard save, `Joining the Stormcloaks`, `The Jagged Crown (Stormcloaks)`, `Message to Whiterun (Stormcloaks)`, `Battle for Whiterun (Stormcloaks)`, `Liberation of Skyrim`, `Rescue from Fort Neugrad`, `Compelling Tribute (Stormcloaks)`, `The Battle for Fort Sungard (Stormcloaks)`, `A False Front (Stormcloaks)`, `The Battle for Fort Snowhawk (Stormcloaks)`, `The Battle for Fort Hraggstad`, `Battle for Solitude`, branch War Hero/Hero of Skyrim state, and General Tullius' Armor branch acquisition.

Rows intentionally not executed on the clean branch: `The Battle for Fort Dunstad (Stormcloaks)`, `The Battle for Fort Kastav`, and `The Battle for Fort Greenwall (Stormcloaks)` because they require Season Unending treaty-state changes that this route avoids to protect War Hero and keep the branch deterministic. `Gift of Kynareth` and `Letter to General Tullius` are also audited here but belong to main continuity, where the Imperial Civil War section now routes them.

No TB-035-MR-041 unresolved route rows are introduced by this pass.

## Linked Records

OBJ-000087 through OBJ-000101; OBJ-000625; OBJ-001439; OBJ-001672; CHK-QUESTS-0133; CHK-QUESTS-0135; CHK-QUESTS-0137; CHK-QUESTS-0139; CHK-QUESTS-0141; CHK-QUESTS-0143; CHK-QUESTS-0145; CHK-QUESTS-0147; CHK-QUESTS-0151; CHK-QUESTS-0153; CHK-QUESTS-0155; CHK-QUESTS-0157; CHK-QUESTS-0159; CHK-QUESTS-0160; CHK-QUESTS-0585; CHK-UNIQUE-GEAR-1604.
