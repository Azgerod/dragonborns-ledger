# SN-000175 - Paarthurnax Branch Route

Status: route-writing source note for TB-035-MR-044.

## Scope

This note supports the v1 guide section `Paarthurnax And Blades Branch`. The section is a compact branch-only route from the post-`The Fallen` state: hard save, kill Paarthurnax, report to the Blades, record the branch consequence, reload, and preserve Paarthurnax on canonical continuity.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000358 | Skyrim:Paarthurnax (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Paarthurnax_(quest) | 2026-05-12 | Paarthurnax quest initiation/completion, kill-or-spare consequences, Blades/Greybeards support split, and branch outcome. |
| SRC-000173 | Skyrim:Paarthurnax (dragon) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Paarthurnax_(dragon) | 2026-05-11 | Paarthurnax as the meditation source and preservation target. |
| SRC-001146 | Skyrim:Rebuilding the Blades | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rebuilding_the_Blades | 2026-05-13 | Prior completion of Blades recruitment and the Paarthurnax-active lockout for Esbern's dragon-lair handoff. |
| SRC-001147 | Skyrim:Dragon Hunting | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon_Hunting | 2026-05-13 | Prior representative Blades dragon hunt and reason not to add a second branch-only random hunt. |
| SRC-001148 | Skyrim:Dragon Research | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon_Research | 2026-05-13 | Prior Dragon Infusion completion before the Paarthurnax lockout. |

## Route Decisions

The canonical route still preserves Paarthurnax. The branch exists only to record the optional main-quest outcome where Paarthurnax is killed and Blades support is restored. `HS-MQ-PAARTHURNAX` remains the hard-save boundary from `data/constraints/quest-conflicts-hard-saves.md`.

The guide places the branch after `The Fallen`, before Odahviing is released to Skuldafn. At this point the Civil War is complete, `Season Unending` has been bypassed, the Blades recruit/research window has already been handled, and the player has a clean main-route state to return to.

The branch tells the player to kill Paarthurnax, return to Sky Haven Temple, and tell Delphine that Paarthurnax is dead. UESP records that after killing Paarthurnax, Blades dialogue/support returns, while Greybeards hospitality, Arngeir's word-wall guidance, and future Paarthurnax meditation changes are lost. Existing meditation bonuses are not removed; they simply cannot be changed on that branch.

The guide does not duplicate `Rebuilding the Blades`, Blades `Dragon Hunting`, or `Dragon Research` in the branch. TB-035-MR-043 moved those rows onto main continuity before the Paarthurnax lockout, because the route wants Dragon Infusion without permanently killing Paarthurnax. Starting another Blades dragon hunt on the temporary branch would add random target travel that disappears on reload and is unnecessary for row-level coverage.

The nearby-objective audit found no safe same-branch additions. Throat of the World discovery, the main Paarthurnax meditation default, Sky Haven Temple discovery, Sky Haven equipment, and `Remanada` are already handled on main continuity. `Mace Etiquette` remains staged for the later Scholar's Insight window, and ordinary word-wall/shout work should not be performed on a branch that will be reloaded.

## Coverage Summary

This pass places `Paarthurnax`, `HS-MQ-PAARTHURNAX`, the branch-only restored-Blades outcome, and the reload back to Paarthurnax-preserved main continuity. It also represents `The Words of Power` / Arngeir support as preserved on main continuity rather than consumed by the branch.

Rows not duplicated here because they were completed in TB-035-MR-043: `Rebuilding the Blades`, one representative Blades `Dragon Hunting`, `Dragon Research`, and Dragon Infusion.

No new unresolved `NEEDS ROUTE RESOLUTION` rows were introduced by this pass.

## Linked Records

OBJ-000019; OBJ-000317; OBJ-000805; OBJ-000806; OBJ-002785; OBJ-002786; CHK-QUESTS-0015; CHK-QUESTS-0055; CHK-QUESTS-0057; CHK-QUESTS-0058; CHK-PERKS-3690.
