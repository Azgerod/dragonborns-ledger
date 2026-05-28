# SN-000201 - Level 78 And Level 80 Gates Route

Status: route-writing source note for TB-035-MR-067.

## Scope

This note supports the v1 guide section `Level 78 and Level 80 Gates`. The pass converts the old scaffold into a source-backed late combat gate for the Dawnguard `Legend` trophy and Dragonborn's `The Ebony Warrior`.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000002 | Skyrim:Achievements | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Achievements | 2026-05-12 | Special Edition trophy behavior and the Dawnguard `Legend` condition. |
| SRC-000048 | Skyrim:The Ebony Warrior | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Ebony_Warrior | 2026-05-11 | Level 80 requirement, major-city challenge trigger, Last Vigil objective, reward summary, and quest bugs. |
| SRC-000385 | Skyrim:Dragon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon | 2026-05-12 | Legendary Dragon level 78 leveled-list timing, `Legend` achievement note, dragon-soul bug notes, and reliable dragon-hunt source. |
| SRC-001149 | Skyrim:Dragon Lairs | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon_Lairs | 2026-05-13 | Dragon lair list, word-wall context, respawning dragon behavior, and respawned-soul caveat. |
| SRC-001248 | Skyrim:Dragon Seekers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon_Seekers | 2026-05-13 | Post-Glory Companions radiant, random lair assignment list, and direct turn-in structure. |
| SRC-001483 | Skyrim:Last Vigil | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Last_Vigil | 2026-05-28 | Last Vigil location, Fort Greenwall path, and camp contents. |
| SRC-001484 | Skyrim:Ebony Warrior | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ebony_Warrior | 2026-05-28 | Ebony Warrior NPC equipment, loot, combat shouts, disarm risk, and crime-faction bug. |

## Route Decisions

Legendary Dragons begin appearing in leveled lists at level 78 if Dawnguard is installed. The route therefore does not ask the player to hunt one before level 78, and it does not treat a Revered Dragon, Ancient Dragon, or Serpentine Dragon as equivalent for `Legend`.

The guide uses repeatable `Dragon Seekers` assignments as the level-78 hunt source because the Dragon page identifies `Dragon Seekers` and `Dragon Hunting` as reliable repeatable dragon-fight sources with guaranteed dragon destinations. Canonical continuity preserves Paarthurnax after the Blades window, so `Dragon Hunting` is not used here. The guide sends the player directly to the assigned lair, handles only the assigned dragon, turns in, and repeats only if the dragon is not named `Legendary Dragon`. It explicitly avoids save reloads to reroll the lair or subtype.

The `Dragon Lairs` page supports lairs as renewable dragon locations, but it also records that respawned dragons can fail to give dragon souls. MR-067 therefore treats the level-78 block as a `Legend` trophy hunt and not as a guaranteed Dragon Hunter soul-count closeout.

The Ebony Warrior is held until level 80. The guide uses Whiterun as the controlled major-city trigger point, then routes the duel at Last Vigil with two hard saves: one before the city trigger and one before attacking at the duel site. The Last Vigil page supports the Rift/Fort Greenwall approach and the source-listed site; the quest page supports that the Ebony Warrior waits to be attacked.

The fight text protects unique gear because the Ebony Warrior can use Disarm and the quest page warns that a disarmed weapon can roll down the mountain. The guide tells the player to store unique melee weapons or use disposable/nonunique gear for the fight. It also has the player loot the full body inventory after the quest completes, preserving the enchanted ebony equipment, six flawless gems, Human Heart, Daedra Heart, and filled Black Soul Gem from the NPC page.

## Coverage Notes

This pass appends MR-067 coverage rows for `Legend Trophy Set`, the `Legend` trophy observation, repeatable `Dragon Seekers` support, level 78 and level 80 state gates, the two fight-readiness checks, `The Ebony Warrior`, Last Vigil reuse, and the three named hard saves.

`Dragonrider`, level 252 all-perks completion, final homes and services, Fishing, Proudspire/No Stone/Prowler's Profit, and Balbus's Fork remain with their documented later owners or route-resolution rows.
