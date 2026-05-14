# SN-000193 - Vampire Lord Mastery and Rising at Dawn Closeout

## Scope

Supports the v1 guide section `Vampire Lord Mastery and Rising at Dawn Closeout`.

This pass closes the canonical Vampire Lord window when all eleven perks are purchased, routes a deterministic Falion cure path, resolves the final mortal-state baseline, cures Serana as the route default after her vampire services are no longer needed, and inserts Robber's Gorge as a late Hjaalmarch bandit-camp objective that also supplies a deterministic Black Soul Gem fill opportunity.

## Sources

| Source ID | Use |
| --- | --- |
| SRC-000171 | Vampire Lord perk tree size, qualifying perk-kill methods, 165-kill full-tree requirement, Vampire Mastered boundary, form limitations, and Serana-follower Vampiric Drain interaction. |
| SRC-000172 | Normal vampirism state, cure implications, and Dawnguard acceptance context after temporary Vampire Lord use. |
| SRC-001237 | Serana post-`Kindred Judgment` Vampire Lord service, Bloodcursed arrow service, cure dialogue availability, supportive cure responses, three-day return behavior, and service loss after cure. |
| SRC-001249 | `Rising at Dawn` start boundary, filled Black Soul Gem requirement, Falion's dawn ritual window, and The Black Star exclusion. |
| SRC-001408 | Mace of Molag Bal's Soul Trap effect, used as the deterministic route source for filling a Black Soul Gem if the player does not already have one filled. |
| SRC-001409 | Robber's Gorge clearable camp route, bandit chief/key, Robbers' Cove, `The Black Arrow, v2`, `Bandit Leader's Journal`, and hidden stash location. |
| SRC-000312 | Robber's Gorge finite non-journal quest framing and hidden-stash objective. |

## Routing Decisions

The section begins with a hard perk-tree checkpoint rather than blindly curing. The route has carried Vampire Lord through multiple fresh hostile Solstheim sections, but exact perk progress depends on whether the player used Vampiric Drain or power-bite kills during combat. If the eleventh perk is not purchased yet, the guide keeps the vampire state and sends the player into the next fresh hostile route content before returning to this closeout. This protects Vampire Mastered without forcing an exploit or a disconnected 165-kill grind.

The player is cured through Falion's `Rising at Dawn` ritual because the project decision log selects a mortal final transformation state after Werewolf and Vampire Lord coverage is complete. The guide explicitly excludes The Black Star from the ritual item because UESP says Falion requires a filled Black Soul Gem and the quest will not accept The Black Star.

Robber's Gorge is inserted here instead of leaving it to final cleanup. It is safe late, it is geographically compatible with the Morthal/Falion cure trip, it contains bandits for a deterministic black-soul fill using the already-preserved Mace of Molag Bal, it closes the Robber's Gorge non-journal quest and clearable-location rows, and it supplies a post-Scholar's Insight reading of `The Black Arrow, v2`. The previous selected copy for that skill-book title was Brood Cavern; `data/constraints/progression-source-selections.csv` now selects the Robber's Gorge copy because the guide already routes the camp here.

Serana is cured as the route default only after the player is cured and after Serana's Vampire Lord and Bloodcursed-arrow services have already been used. UESP records that curing Serana removes those services, so the guide keeps her uncured until this closeout and then uses the supportive cure dialogue after the player's own cure.

The inherited Bittercup item-table rows for Potion of Blood, Ironwood Soup Elixir, and Mysterious Potion remain unresolved. This pass does not hide those rows under the vampire cure route because the current fetched sources still do not identify deterministic normal-play pickup actions for them.

## Unresolved

No new `NEEDS ROUTE RESOLUTION` rows were introduced by this pass.

Inherited unresolved rows still remain for `Filial Bonds`/Torkild, `Torkild's Letter to Wulf`, `Note from Mogrul`, Potion of Blood, Ironwood Soup Elixir, and Mysterious Potion.

## Linked Records

OBJ-000192; OBJ-000817; OBJ-000818; OBJ-000830; OBJ-002133; OBJ-002760; NPCOPT-000160; CHK-QUESTS-0271; CHK-QUESTS-0198; CHK-LOCATIONS-1201; CHK-BOOKS-2135; CHK-PERKS-3667; CHK-PERKS-3670; CHK-PERKS-3673; CHK-PERKS-3676; CHK-PERKS-3679; CHK-PERKS-3682; CHK-PERKS-3685; CHK-PERKS-3688; CHK-PERKS-3691; CHK-PERKS-3694; CHK-PERKS-3696.
