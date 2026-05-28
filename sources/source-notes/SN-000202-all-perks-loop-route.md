# SN-000202 - All-Perks Loop Route

Status: route-writing source note for TB-035-MR-068.

## Scope

This note supports the v1 guide section `All-Perks Loop`. The pass converts the old scaffold into a player-facing late progression loop for level 252, all 18 skills at 100, all 251 normal perk ranks, bounded Legendary resets, Oghma Infinium use timing, paid training limits, and College master ritual spell gates.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000268 | Skyrim:Skills | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skills | 2026-05-12 | Eighteen skills, 180 perk nodes, 251 perk ranks, Legendary reset behavior, and level 252 all-perks note. |
| SRC-000422 | Skyrim:Leveling | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Leveling | 2026-05-12 | Character XP from skill increases, perk point on level-up, level 252 enough for all perks, and all-perks reset math. |
| SRC-000391 | Skyrim:Trainers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Trainers | 2026-05-12 | Five training sessions per character level, trainer caps, trainer identities, and training limitations. |
| SRC-000415 | Skyrim:Survival Mode | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Survival_Mode | 2026-05-12 | Survival Mode level-up sleep requirement and late-route survival constraints. |
| SRC-000418 | Skyrim:Fatigue | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fatigue | 2026-05-12 | Fatigue penalties relevant to planned rest before long crafting, travel, and level-up work. |
| SRC-000190 | Skyrim:Oghma Infinium | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Oghma_Infinium | 2026-05-11 | Skill-path choice, no increase above 100, removal after reading, and skill-gain bug note. |
| SRC-000875 | Skyrim:Alteration Ritual Spell | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alteration_Ritual_Spell | 2026-05-13 | Kahvozein's Fang, dragon heartscales, Dragonhide reward, Mass Paralysis unlock, and reset warning. |
| SRC-001070 | Skyrim:Conjuration Ritual Spell | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Conjuration_Ritual_Spell | 2026-05-13 | Unbound Dremora sequence, Sigil Stone, Flame Thrall reward, master thrall tome unlocks, and bug warnings. |
| SRC-001071 | Skyrim:Destruction Ritual Spell | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Destruction_Ritual_Spell | 2026-05-13 | Power of the Elements route, pedestal spell sequence, Fire Storm reward, and Blizzard/Lightning Storm unlocks. |
| SRC-001072 | Skyrim:Illusion Ritual Spell | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Illusion_Ritual_Spell | 2026-05-13 | Vision of the Tenth Eye, four Master Illusion Text locations, Hysteria reward, and master Illusion tome unlocks. |
| SRC-001073 | Skyrim:Restoration Ritual Spell | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Restoration_Ritual_Spell | 2026-05-13 | Augur test, Bane of the Undead reward, Guardian Circle unlock, and Colette vendor caveat. |

## Route Decisions

The guide requires the all-perks loop only after the earlier late-route gates have created safe storage, beds, crafting access, vendor access, magic access, and combat alternatives. If MR-067 sends the player into this section only to reach level 78 or level 80, the guide now states that the player should return to the prior gate with a combat-ready build before completing the full level 252 closeout.

The skill/perk target is stated as three distinct requirements: reach level 252 or higher, restore all 18 skills to 100 after the final Legendary reset, and assign all 251 normal skill perk ranks. The `Skill Master` trophy is treated separately because its trophy condition is one skill reaching 100, not the project all-skills/all-perks scope.

Legendary resets are bounded by a stop condition rather than an invented fixed count table. Existing project data intentionally defers final numeric reset counts to later validation because exact counts depend on route order, training purchases, Oghma choice, skill books, material stock, and incidental XP. MR-068 therefore uses the approved distribution: repeated resets first through Alchemy, Smithing, Enchanting, Alteration, Conjuration, and Illusion; Restoration, Sneak, and Pickpocket only after their risks are controlled; combat and armor skills only as emergency fillers; and no repeated Lockpicking or Speech baseline.

The reset-safety checklist is included because Legendary reset behavior refunds invested perks and drops a skill to 15. The guide therefore checks pending quest/vendor gates, combat dependence, Fortify Skill effects, unused perk-point counter risk, and recovery plan before every reset. It also explicitly requires final recovery to 100 for every skill after all resets.

Paid training is framed as smoothing rather than the core engine. The guide carries forward the five-sessions-per-level limit, trainer caps, and selected trainer list from the training/source-selection notes.

Oghma Infinium is held until the late gap-closing window. The guide hard-saves before reading, chooses the path with the largest below-100 gain, defaults to Magic on a tie, verifies the actual skill increases, and reloads if the documented skill-gain bug appears.

The five College master ritual quests are routed as skill-threshold gates before resetting their related skill. This prevents reset timing from blocking quest turn-in or vendor unlocks and completes the master spell/tome rows that MR-065 intentionally staged for the all-perks window.

## Coverage Notes

This pass appends MR-068 coverage rows for all-skills completion, all-perks allocation, level 252, bounded Legendary resets, Skill Master separation, the two named hard saves, underleveled return support, the MR-066 investment return, training policy, all 18 skill-100 rows, all 18 perk-tree rows, reset pool distribution, Oghma Infinium use, the five College master ritual quests, ritual support objects/books, and all master spell rewards and vendor tomes.

Final exact reset-count validation remains with the later final QA/validation tasks. Homes, household, services, pets, mounts, Master Criminal, final reconciliation, Fishing species, Proudspire/No Stone/Prowler's Profit, Dragonrider's four rides, and the unresolved one-time ingredient/branch items remain with their documented later sections or route-resolution owners.
