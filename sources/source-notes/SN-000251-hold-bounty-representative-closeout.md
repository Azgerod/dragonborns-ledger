# SN-000251 - Hold Bounty Representative Closeout

Status: targeted TB-044 route-resolution source note.

## Scope

This note closes the base-game hold bounty representative bucket for `OBJ-000332` Bounty: Bandit Boss, `OBJ-000333` Bounty: Dragon, `OBJ-000334` Bounty: Forsworn, and `OBJ-000335` Bounty: Giant. It also closes the related bounty-letter document rows: `OBJ-001110` Bounty (bandits), `OBJ-001111` Bounty (dragon), `OBJ-001112` Bounty (forsworn), and `OBJ-001113` Bounty (giant).

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000021 | Skyrim:Bounty Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty_Quests | 2026-05-30 | Bounty giver model, bounty-letter handoff, one-active-per-type limit, separate-hold active limit, reward values, type gates, and bug caveats. |
| SRC-001856 | Skyrim:Bounty: Bandit Boss | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty:_Bandit_Boss | 2026-05-30 | Bandit-boss bounty giver, hold target pools, marked-leader boundary, turn-in objective, and already-cleared dungeon bug. |
| SRC-001857 | Skyrim:Bounty: Dragon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty:_Dragon | 2026-05-30 | Dragon bounty prerequisite, hold target pools, lair completion boundary, dragon-soul caveat, Mount Anthor bug, and turn-in objective. |
| SRC-001858 | Skyrim:Bounty: Forsworn | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty:_Forsworn | 2026-05-30 | Reach-only Forsworn bounty giver, target pool, Igmund turn-in, and Igmund-jarl dependency. |
| SRC-000974 | Skyrim:Bounty: Giant | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty:_Giant | 2026-05-30 | Giant bounty level gate, target pools, marked-giant boundary, turn-in objective, Skald journal caveat, and cleared-camp respawn behavior. |
| SRC-001859 | Skyrim:Bounty (bandits) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty_(bandits) | 2026-05-30 | Bandit bounty letter identity, quest relation, giver source, and alias-driven target text. |
| SRC-001860 | Skyrim:Bounty (dragon) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty_(dragon) | 2026-05-30 | Dragon bounty letter identity, quest relation, giver source, and alias-driven target text. |
| SRC-001861 | Skyrim:Bounty (forsworn) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty_(forsworn) | 2026-05-30 | Forsworn bounty letter identity, quest relation, giver source, Reach limitation note, and alias-driven target text. |
| SRC-001862 | Skyrim:Bounty (giant) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty_(giant) | 2026-05-30 | Giant bounty letter identity, quest relation, giver source, and alias-driven target text. |

## Route Decisions

The guide should keep the one-completion representative boundary from `SN-000113`: one bandit boss bounty, one dragon bounty, one Forsworn bounty, and one giant bounty. Further ordinary hold bounties are optional support only unless a later named route explicitly uses one.

The giant representative is already routed by Skald's Pale bounty in `Dawnstar, Pale Blade, And Heljarchen`. That route is level-safe, uses Skald's active marker across the Pale giant-camp loop, turns the bounty in before Pale thaneship and Heljarchen Hall, and is supported by `SN-000163`. This pass only tightens that route by making the bounty-letter read explicit; it should not add a second generic giant bounty.

The remaining bandit, dragon, and Forsworn representatives belong in a late post-all-perks hold-bounty block. By that point the character has completed Dragon Rising, is well above the level-20 giant gate, has stable Survival support, and can survive any ordinary bandit, dragon-lair, or Reach-redoubt target the active marker selects. Placing these after the all-perks audit also separates the dragon bounty from the level-78 Legendary Dragon trophy route: if the bounty dragon does not release a soul because the lair had already been cleared, the bounty can still be completed without depending on that soul for Dragon Hunter, Legend, or any other trophy counter.

The late block uses named preferred holds to keep the guide concrete without pretending the radiant target is fixed:

| Representative type | Preferred start | Active-marker policy |
| --- | --- | --- |
| Bandit boss | Whiterun innkeeper or steward | Accept the bandit letter, read it, kill the marked bandit leader at the active Whiterun-hold target, and turn in to the current Jarl or steward. |
| Dragon | Riften innkeeper or steward | Accept the dragon letter, read it, kill the active Rift dragon-lair target, wait briefly for any soul absorption, loot normally, and turn in to the current Jarl or steward. |
| Forsworn | Markarth innkeeper or Raerek | Accept the Reach Forsworn letter, read it, kill the active redoubt leader, and turn in to Igmund or the current steward. Keep this random bounty distinct from Igmund's non-repeatable thaneship favor. |

If the game offers a different still-needed representative type than the row the player was trying to start, the guide can complete that actual accepted type and then continue the remaining list. This follows the active assignment rather than reloading for a preferred target. If a giver has no bounty dialogue, the player should move to the backup innkeeper or steward in the same hold, then to another eligible hold with a source-listed target pool.

Hard-save recovery is justified only for source-listed broken states: a bandit boss in a previously cleared location that does not repopulate, a dragon lair where the target does not spawn or points incorrectly, a non-respawning/inaccessible target that prevents quest completion, or an unexpected post-Civil-War turn-in problem. The hard save is not for shopping shorter dungeons, easier targets, better rewards, or dragon subtypes. The guide should also avoid using Winterhold/Mount Anthor as the planned dragon-bounty source because the individual dragon-bounty page records a Mount Anthor spawn/marker bug.

## Bounty-Letter Document Resolution

UESP's bounty-letter pages identify the four letter titles as quest-related notes given by an innkeeper or steward, with alias-driven hold, Jarl, steward, and target text. The route therefore reads the letter immediately when each representative bounty is accepted. Duplicate bounty letters are not required after the representative type is complete.

`Bounty (giant)` is represented by Skald's Pale bounty letter in the earlier Pale route. `Bounty (bandits)`, `Bounty (dragon)`, and `Bounty (forsworn)` are represented by the late hold-bounty block. Because the letters are generated quest documents, their target text depends on the active assignment; the guide should not list one fixed dungeon, redoubt, or lair as the only acceptable document state.

## Coverage Summary

This pass closes the four representative bounty-type rows and their four source-listed bounty-letter rows. It records active-marker handling, no convenience rerolling, the Skald giant-bounty reuse, the dragon-soul caveat, and bug-recovery save use.

## Linked Records

OBJ-000332; OBJ-000333; OBJ-000334; OBJ-000335; OBJ-001110; OBJ-001111; OBJ-001112; OBJ-001113; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/constraints/radiant-boundaries.md`; `data/books/book-document-locations.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
