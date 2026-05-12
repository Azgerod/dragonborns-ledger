# Trophy Dependencies

Status: TB-021 reviewed.

Scope: this is a constraint table, not route prose. It records PS4 Special Edition / Anniversary Edition trophy requirements, counter dependencies, trophy-disabling setup rules, and warning handoffs. It does not replace TB-016 NPC dependency work, TB-017 bug mitigation, TB-018 radiant boundaries, TB-020 progression planning, or TB-021 consistency review.

## Setup and Global Trophy Safety

| Trophy or rule | Requirement | Dependency | Risk | Route protection | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| PS4 SE/AE trophy set | Special Edition trophy list includes base-game trophies plus Dawnguard, Hearthfire, and Dragonborn add-on trophies by default; no AE Creation Club trophies are added. | Clean PS4/PS5 Skyrim Special Edition or Anniversary Edition install. | Treating AE Creation content as separate trophy content can create false requirements. | Route all 76 PS4 trophies for 100% trophy completion; treat AE Creation content as completion scope, not trophy scope. | SN-000101 | Confirmed. |
| Trophy-safe content setup | Creation Club items bundled with Anniversary Edition are trophy-safe; other Creations/Mods disable trophies. | Official AE Creation Club bundle only. | Installing or enabling non-CC Creations/mods disables trophy progress. | Setup section must forbid non-AE Creations/mods and warn against changing content mid-run. | SN-000101 | Confirmed setup rule. |
| Mod-contaminated save recovery | Trophy progress resumes only after removing/disabling mods and loading a save from before mods were installed. | Pre-mod save. | Continuing on a modded save can silently waste trophy progress. | If a mod was ever enabled, abandon that save for the trophy route unless loading a verified pre-mod save. | SN-000101 | Confirmed setup rule. |
| PS4 trophy-pop fallback | Some PS4 trophies can occasionally fail to unlock despite in-game completion. | Recent manual save before trophy-critical actions. | No console commands on PS4 to repair failed trophy flags. | Hard save before missable, long, or one-shot trophy completions; if no trophy pops, reload and repeat the action. | SN-000101 | Warning-layer handoff. |

## Base Game Questline Trophies

| Trophy | Requirement | Dependency | Risk | Route protection | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Unbound | Complete `Unbound`. | OBJ-000001 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| Bleak Falls Barrow | Complete `Bleak Falls Barrow`. | OBJ-000003 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| The Way of the Voice | Complete `The Way of the Voice`. | OBJ-000005 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| Diplomatic Immunity | Complete `Diplomatic Immunity`. | OBJ-000008 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| Alduin's Wall | Complete `Alduin's Wall`. | OBJ-000010 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| Elder Knowledge | Complete `Elder Knowledge`. | OBJ-000012 | Scroll routing overlaps Dawnguard but trophy is not mutually exclusive. | Complete on main route; coordinate Elder Scroll handling later. | SN-000102 | Route normally. |
| The Fallen | Complete `The Fallen`. | OBJ-000014 | Civil War state can affect route shape before this point. | Preserve Civil War/Season Unending hard saves from TB-014. | SN-000102 | Coordinate with Civil War. |
| Dragonslayer | Complete `Dragonslayer`. | OBJ-000017 | No special trophy risk beyond main quest completion. | Complete on main route. | SN-000102 | Route normally. |
| Take Up Arms | Join the Companions. | OBJ-000020 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| Blood Oath | Become a member of the Circle. | OBJ-000022 | Transformation-state decisions affect later Werewolf Mastered planning. | Do not cure lycanthropy permanently until Werewolf Mastered plan is complete. | SN-000102, SN-000105 | Coordinate with transformation plan. |
| Glory of the Dead | Complete `Glory of the Dead`. | OBJ-000025 | Curing decisions can affect Werewolf Mastered and later werewolf-only content. | Delay final cure decision until transformation trophy and completionist checks are done. | SN-000102, SN-000105 | Coordinate with transformation plan. |
| Gatekeeper | Join the College of Winterhold. | OBJ-000028 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| Revealing the Unseen | Complete `Revealing the Unseen`. | OBJ-000032 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| The Eye of Magnus | Complete `The Eye of Magnus`. | OBJ-000035 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| Taking Care of Business | Join the Thieves Guild. | OBJ-000037 | No special trophy risk. | Complete on main route. | SN-000102 | Route normally. |
| Darkness Returns | Complete `Darkness Returns`. | OBJ-000046 | Nocturnal/Skeleton Key handling does not count for Oblivion Walker. | Return Skeleton Key as normal; do not count it as a Daedric artifact. | SN-000102, SN-000104 | Route normally. |
| One with the Shadows | Return the Thieves Guild to its former glory. | OBJ-000047 | Missable if Erikur dies before `The Dainty Sload`. | Protect Erikur until the relevant Thieves Guild restoration work is complete. | SN-000102 | TB-016 NPC handoff. |
| With Friends Like These... | Join the Dark Brotherhood. | OBJ-000055 | Unavailable if the player destroys the Dark Brotherhood. | Main route must kill a captive at the Abandoned Shack; destroy path stays branch-only. | SN-000102, SN-000097 | Hard-save protected. |
| Bound Until Death | Complete `Bound Until Death`. | OBJ-000060 | Unavailable on destroy branch. Erikur becomes nonessential after this quest starts. | Complete `The Dainty Sload` dependency before risking Erikur during Dark Brotherhood progression. | SN-000102 | TB-016/TB-017 handoff. |
| Hail Sithis! | Complete `Hail Sithis!`. | OBJ-000066 | Unavailable on destroy branch. | Keep Dark Brotherhood join route on canonical save. | SN-000102, SN-000097 | Hard-save protected. |
| Taking Sides | Join the Stormcloaks or Imperial Army. | OBJ-000070 or OBJ-000087 | Faction choice is mutually exclusive in one continuity. | Canonical route joins Imperial; Stormcloak belongs to branch save. | SN-000102, SN-000097 | Canonical decided. |
| War Hero | Capture Fort Sungard or Fort Greenwall. | OBJ-000080, OBJ-000084, OBJ-000094, OBJ-000099 | Can be skipped by some `Season Unending` outcomes. | Hard save before Season Unending and any hold handoff; ensure an eligible fort battle is captured on the trophy save. | SN-000102, SN-000097 | High-priority warning. |
| Hero of Skyrim | Capture Solitude or Windhelm. | OBJ-000086 or OBJ-000101 | Faction path changes which city is captured. | Canonical Imperial route captures Windhelm; Stormcloak branch captures Solitude if branch is fully routed. | SN-000102, SN-000097 | Canonical decided. |

## Base Game Counter and System Trophies

| Trophy | Requirement | Dependency | Risk | Route protection | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Sideways | Complete 10 qualifying side quests. | OBJ-000219 plus qualifying side-quest rows. | Several journal side quests do not count; some unusual rows do count; two quests have ending-specific caveats. | Track only sourced qualifying quests; do not count `Blood on the Ice`, Black Book side quests, or `Lost to the Ages` for Sideways. | SN-000103, SN-000020 | Counter QA needed. |
| Hero of the People | Complete 50 miscellaneous objectives. | OBJ-000220 through OBJ-000350 plus later misc/favor rows. | Counts objectives, not quests; repeated or disappearing objectives can confuse manual tracking. | Route at least 50 distinct finite misc objectives rather than relying on repeated-objective behavior. | SN-000103, SN-000022 | Counter QA needed. |
| Hard Worker | Chop wood, mine ore, and cook food. | OBJ-002752, OBJ-002762, OBJ-002764, OBJ-002765 | Current rows cover representative activities, not exact stations. | Perform all three actions explicitly in the route and check the trophy before moving on. | SN-000103 | Needs station placement. |
| Thief | Pick 50 locks and 50 pockets. | OBJ-002773 plus Lockpicking/Pickpocket skill and route activity support. | Counter may lag if route does not explicitly track both halves. | Track both locks and pockets; avoid assuming normal play hits 50 pockets. | SN-000103 | Explicit tracker added. |
| Snake Tongue | Successfully persuade, bribe, and intimidate. | OBJ-002774 plus Speech checks during route. | Missing one dialogue action can defer trophy unpredictably. | Add explicit persuade/bribe/intimidate actions to route skeleton. | SN-000103 | Explicit tracker added. |
| Blessed | Select a Standing Stone blessing. | OBJ-000788 | No special trophy risk. | Activate an early standing stone on main route. | SN-000103 | Route normally. |
| Standing Stones | Find all 13 Standing Stones. | OBJ-000788 plus location/discovery rows. | Route must visit all stones, not merely choose a final power. | Track all 13 stone discoveries and final recommended power separately. | SN-000103 | Counter QA needed. |
| Citizen | Buy a house. | OBJ-002775 plus city home/property rows, especially OBJ-001920-OBJ-001925. | Property prerequisite timing can affect access. | Ensure first city-house purchase is explicit; Hearthfire land does not replace the city-house trophy check. | SN-000103 | Explicit tracker added. |
| Wanted | Escape from jail. | OBJ-002776 plus crime/jail route action. | Clean-route play may never trigger it. | Stage a controlled jail escape with a hard save or cleanup block. | SN-000103 | Explicit tracker added. |
| Married | Get married. | OBJ-001945 | Spouse choice is an option-list/default decision, not a branch. | Pick a recommended spouse later and route marriage once prerequisites are safe. | SN-000103 | Option-list default later. |
| Artificer | Make a smithed item, an enchanted item, and a potion. | OBJ-002751 plus crafting rows. | Exact crafts and materials are not selected yet. | Perform one explicit low-risk craft in each system before assuming trophy completion. | SN-000103 | TB-020 handoff. |
| Master Criminal | Have a bounty of 1000 gold in all nine holds. | OBJ-002777 plus crime route action. | Conflicts with a clean final-state preference and can disrupt NPC/services if done carelessly. | Use a named hard save and controlled crime branch or late cleanup plan; reload or clear bounties after trophy if needed. | SN-000103 | Explicit tracker added; hard-save likely. |
| Golden Touch | Have 100000 gold. | OBJ-002778 plus economy route support. | Spending on homes/materials can delay trophy. | Add an economy checkpoint before expensive final purchases or all-perks grind cleanup. | SN-000103 | Explicit tracker added. |
| Delver | Clear 50 dungeons. | OBJ-001958 through OBJ-002198. | Clear-state quirks and non-counting locations can affect manual totals. | Route more than 50 source-listed clearable locations and validate Delver counter behavior in QA. | SN-000103, SN-000077 | Counter QA needed. |
| Skill Master | Get a skill to 100. | OBJ-002465 and skill rows. | No special trophy risk; all-skills scope exceeds requirement. | All-skills plan will satisfy this; check trophy when first skill reaches 100. | SN-000103, SN-000081 | TB-020 handoff. |
| Explorer | Discover 100 locations. | Location rows OBJ-001958 through OBJ-002407. | Duplicate/secondary markers and AE markers need later route validation. | Discover at least 100 source-listed map markers and validate location counter during route QA. | SN-000103, SN-000078 | Counter QA needed. |
| Reader | Read 50 different skill books. | OBJ-000819 through OBJ-000909. | Duplicate copies do not count again; skill-book bugs can hide skill gain. | Track title-level reads, not copies; save/check before reading planned books if needed. | SN-000103 | Counter QA needed. |
| Daedric Influence | Acquire one Daedric artifact. | OBJ-000165 through OBJ-000181. | Non-artifact outcomes do not count. | First Daedric artifact route action should use an artifact-awarding outcome. | SN-000104 | Artifact-safe. |
| Oblivion Walker | Collect 15 qualifying Daedric artifacts. | OBJ-000165 through OBJ-000181. | Missable; AE artifacts, Black Books, Skeleton Key, and Daedric Quests Completed statistic are not reliable substitutes. | Choose artifact-awarding outcomes for all base-game Daedric quests; do not rely on dual Hircine unless TB-028 explicitly allows it. | SN-000104 | High-priority warning. |
| Dragon Soul | Absorb one dragon soul. | OBJ-000760 | Dragons must be enabled by main-quest progression. | Complete `Dragon Rising` route gate before expecting random dragon soul progress. | SN-000103 | Route normally. |
| Dragon Hunter | Absorb 20 dragon souls. | OBJ-002779 plus OBJ-000760. | Miraak can steal souls during parts of Dragonborn; all-shouts scope needs many souls anyway. | Track dragon souls for shout unlocks and trophy; avoid relying on stolen souls. | SN-000103, SN-000033 | Explicit tracker added. |
| Words of Power | Learn all three words of one shout. | OBJ-000761 through OBJ-000788. | No special trophy risk. | Main quest shouts or routed word walls should satisfy this naturally; verify on first three-word shout. | SN-000103 | Route normally. |
| Thu'um Master | Learn 20 shouts. | OBJ-000760 through OBJ-000788. | Requires broad word-wall/main-quest/Dragonborn shout coverage. | All-shouts scope exceeds requirement; track learned shout count before final cleanup. | SN-000103 | Counter QA needed. |
| Apprentice | Reach level 5. | OBJ-002780 plus leveling plan. | No special trophy risk. | Normal progression satisfies; no route constraint beyond trophy-enabled save. | SN-000103 | Explicit tracker added. |
| Adept | Reach level 10. | OBJ-002781 plus leveling plan. | No special trophy risk. | Normal progression satisfies; no route constraint beyond trophy-enabled save. | SN-000103 | Explicit tracker added. |
| Expert | Reach level 25. | OBJ-002782 plus leveling plan. | No special trophy risk. | Normal progression satisfies; no route constraint beyond trophy-enabled save. | SN-000103 | Explicit tracker added. |
| Master | Reach level 50. | OBJ-002783 plus leveling plan. | No special trophy risk; all-perks scope exceeds requirement. | TB-020 all-perks plan will exceed this, but trophy should be checked at level 50. | SN-000103, SN-000081 | Explicit tracker added; TB-020 handoff. |
| Platinum Trophy | Collect all other 50 base-game trophies. | All base-game trophy rows. | DLC trophies are needed for 100% but not for base platinum. | Complete all base-game trophy rows on trophy-enabled save. | SN-000101, SN-000103 | Derived trophy. |

## Dawnguard Trophies

| Trophy | Requirement | Dependency | Risk | Route protection | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Awakening | Complete `Awakening`. | OBJ-000352 | No side-specific trophy risk. | Complete on main route. | SN-000105 | Route normally. |
| Beyond Death | Complete `Beyond Death`. | OBJ-000361 | Soul Cairn travel/resource burden, but no trophy conflict. | Complete on main route; coordinate Soul Tear setup. | SN-000105 | Route normally. |
| Kindred Judgement | Complete `Kindred Judgment`. | OBJ-000364 | Auriel's Bow stops being quest-protected afterward. | Use or secure Auriel's Bow trophy action before risking the bow after finale. | SN-000105 | Warning required. |
| Lost to the Ages | Complete `Lost to the Ages`. | OBJ-000385 | Aetherial reward is mutually exclusive but trophy only needs quest completion. | Hard save at Aetherium Forge for reward choice; trophy route can use any crafted Aetherial item. | SN-000105, SN-000099 | Branch reward handoff. |
| Soul Tear | Learn all three words of Soul Tear. | OBJ-000386, OBJ-000782, OBJ-000784 | Requires summoning Durnehviir enough times after Soul Cairn access. | Route three Durnehviir summons/listening waits before marking trophy complete. | SN-000105 | Counter/action QA. |
| Auriel's Bow | Use the special power of Auriel's Bow. | OBJ-000363, OBJ-001557 | Missable if bow is lost/despawns after `Kindred Judgement`. | Hard save after acquiring bow; shoot the sun with valid special arrows before risky storage, arrest, sale, or post-finale delay. | SN-000105 | High-priority warning. |
| Werewolf Mastered | Acquire 11 werewolf perks. | OBJ-000815, OBJ-000816 | Can become inaccessible after curing lycanthropy twice; Vampire Lord conversion cures lycanthropy. | Complete werewolf perk tree before permanent cure or Vampire Lord phase that removes Beast Form. | SN-000105 | TB-031D/TB-031E transformation and grind decision; TB-033 validation. |
| Vampire Mastered | Acquire 11 Vampire Lord perks. | OBJ-000817, OBJ-000818 | Requires Vampire Lord access even on Dawnguard canonical route; may conflict with Dawnguard access until cured. | Use Serana/Harkon access deliberately, finish perk tree, then cure or restore final state according to later defaults. | SN-000105 | TB-031D/TB-031E transformation and grind decision; TB-033 validation. |
| A New You | Change your face. | OBJ-000389 | Galathil will not perform surgery while the player is a vampire or Vampire Lord. | Do face change before Vampire Lord phase or after curing vampirism. | SN-000105 | Route-order warning. |
| Legend | Defeat a Legendary Dragon. | OBJ-002784 plus high-level dragon combat. | Legendary Dragons begin appearing at level 78, so early route cannot satisfy this. | Delay until level 78+ and use a hard save before the hunt. | SN-000105, SN-000103 | Explicit tracker added; late-route gate. |

## Hearthfire Trophies

| Trophy | Requirement | Dependency | Risk | Route protection | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Proud Parent | Adopt a child. | OBJ-000409, OBJ-000410 | Adoption can fail if housing requirements are not met cleanly. | Prepare a valid child bedroom or Hearthfire child beds/containers before adoption dialogue. | SN-000105, SN-000030 | Housing warning. |
| Landowner | Buy one plot of land. | OBJ-000391 through OBJ-000397, OBJ-000403 | Falkreath land can be disrupted by Dark Brotherhood/Civil War/NPC state. | Secure at least one Hearthfire plot before risky Falkreath/Dark Brotherhood actions; track all three for Land Baron. | SN-000105, SN-000100 | Route-order warning. |
| Architect | Build three wings on one house. | OBJ-000405 and Hearthfire construction rows. | Materials and wing choices need route planning. | Build Main Hall and three wings at one homestead; exact wing defaults later. | SN-000105 | TB-020/material handoff. |
| Land Baron | Buy three plots of land. | OBJ-000404, OBJ-000395 through OBJ-000397 | Hold authority and quest prerequisites can be disrupted. | Complete all three land-permission chains before irreversible NPC/faction risks. | SN-000105, SN-000100 | Route-order warning. |
| Master Architect | Build three houses. | OBJ-000406, OBJ-000395 through OBJ-000397 | UESP construction note requires all three wings on each of the three houses for credit. | Build each Hearthfire house through all three wings; do not stop at small house/main hall. | SN-000105, SN-000030 | Material plan needed. |

## Dragonborn Trophies

| Trophy | Requirement | Dependency | Risk | Route protection | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Outlander | Arrive on Solstheim. | OBJ-000413, OBJ-000473 | No special trophy risk; Survival Mode travel matters later. | Take Windhelm boat when route opens Solstheim. | SN-000105 | Route normally. |
| The Temple of Miraak | Complete `The Temple of Miraak`. | OBJ-000414 | No trophy conflict; starts broader Black Book/Dragonborn chain. | Complete on Dragonborn route. | SN-000105 | Route normally. |
| The Path of Knowledge | Complete `The Path of Knowledge`. | OBJ-000417 | Suggested-level and Nchardak logistics affect route timing. | Delay until route level/difficulty plan permits. | SN-000105 | Route normally with level pacing. |
| At the Summit of Apocrypha | Complete `At the Summit of Apocrypha`. | OBJ-000419 | Miraak can steal dragon souls before finale; all-perks/respec value also matters. | Coordinate with dragon-soul and perk planning; complete when Bend Will and power curve are ready. | SN-000105, SN-000033 | TB-020 handoff. |
| Dragon Aspect | Learn all three words of Dragon Aspect. | OBJ-000474 plus Dragon Aspect word objectives. | Requires all three word locations. | Route all three words before leaving Dragonborn cleanup. | SN-000105 | Counter QA needed. |
| Hidden Knowledge | Learn secrets from five Black Books. | OBJ-000420, OBJ-000441, OBJ-000460-OBJ-000462, OBJ-000475 | Trophy needs five; project scope needs all seven Black Books. | Route all seven Black Books, but check trophy after fifth completed book. | SN-000105 | Counter QA needed. |
| Stalhrim Crafter | Craft one Stalhrim item. | OBJ-000436, OBJ-000476 | Missable if Deor or Fanari dies before `A New Source of Stalhrim` starts; crafting has perk/material requirements. | Protect Deor/Fanari, unlock stalhrim crafting, then craft one item after Smithing requirements are met. | SN-000105, SN-000100 | High-priority warning. |
| Dragonrider | Tame and ride five dragons. | OBJ-000418, OBJ-000477, Bend Will shout rows | Requires all three words of Bend Will; some dragons/worldspaces cannot be ridden. | After Bend Will is complete, track five successful mounts on rideable dragons. | SN-000105 | Counter/action QA. |
| Raven Rock Owner | Own a house in Raven Rock. | OBJ-000421, OBJ-000422, OBJ-000424 | Requires Raven Rock prerequisite quest chain and Severin Manor reward. | Complete `March of the Dead`, `The Final Descent`, and `Served Cold` safely. | SN-000105 | Route normally with bug pass. |
| Solstheim Explorer | Discover 30 Solstheim locations. | OBJ-000478 plus Solstheim location rows. | Needs location-counter tracking; Survival Mode geography affects route. | Track Solstheim discoveries during Dragonborn regional passes and verify count before leaving island cleanup. | SN-000105 | Counter QA needed. |
