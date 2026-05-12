# Source Note: Survival Travel Network and Fast-Travel Boundaries

Status: researched.

Source note ID: SN-000116

## Claim

Survival Mode disables ordinary fast travel, so the route must be built around walking, horses, carriages, ferries, player-home travel services, and the late dragon-riding exception. Fast-travel exploits should not be used as route assumptions.

## Routing Relevance

The route skeleton must cluster objectives geographically and treat travel services as infrastructure unlocks. City carriages, Hearthfire homestead carriages, ferries, horses, Dead Man's Dread, and late dragon riding can shorten otherwise bad Survival travel, but each has acquisition, origin, destination, or worldspace limits.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000415 | Skyrim:Survival Mode | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Survival_Mode | 2026-05-12 | Survival fast-travel rule, travel arrival condition warning, house-carriage tip, and fast-travel exploit bug. |
| SRC-000420 | Skyrim:Transport | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Transport | 2026-05-12 | Transport methods, carriage network, ferries, Dead Man's Dread map, and Survival fast-travel line. |
| SRC-000249 | Skyrim:Horses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Horses | 2026-05-12 | Horse purchase, unique/tamable horse categories, speed, carry, over-encumbrance, and ownership behavior. |
| SRC-000044 | Skyrim:Dragon Riding | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dragon_Riding | 2026-05-12 | Dragon riding fast-travel behavior, Bend Will requirement, worldspace limits, and Survival Mode exception. |
| SRC-000063 | Skyrim:Houses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Houses | 2026-05-12 | Player-home and homestead context for travel/base planning. |
| SRC-000065 | Skyrim:Dead Man's Dread (place) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dead_Man%27s_Dread_(place) | 2026-05-12 | Dead Man's Dread player-home travel map context. |
| SRC-000245 | Skyrim:Personal Steward | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Personal_Steward | 2026-05-12 | Steward services including Hearthfire carriage and horse services. |

## Evidence Summary

The Survival Mode page states that travel must be on foot, by horse, carriage, or boat, and warns that long carriage or boat trips can leave the player hungry, cold, and tired on arrival. It also records a fast-travel exploit bug; because the project excludes exploit-only routing unless explicitly justified, the route should not depend on that bug.

UESP's Transport page says ordinary fast travel is totally disabled in Survival Mode except while riding a dragon. Carriages connect the nine hold capitals for 20 to 50 gold, but in the plain game carriage origins are only the five major hold capitals; the smaller capitals are destinations, not origins. Hearthfire homestead carriages add no-charge service after the initial driver hire to smaller villages such as Ivarstead, Kynesgrove, Dragon Bridge, Rorikstead, and Old Hroldan Inn. Transport also records that there are no carriages on Solstheim.

Dawnguard ferrymen connect coastal cities and Icewater Jetty, and Dragonborn adds the Windhelm to Raven Rock ferryman. Dead Man's Dread adds one-way sea transport from its map after the ship is claimed, including Solitude, Dawnstar, Windhelm, and later Castle Volkihar/Icewater Jetty and Raven Rock once discovered.

Horses increase movement speed and let the player ride while over-encumbered. The Horses page lists purchasable, unique, and Creation-added tamable or summonable horses, but exact acquisition timing remains separate objective work. Dragon riding becomes a late fast-travel exception after all three words of Bend Will, but it cannot move between worldspaces such as Skyrim and Solstheim or into walled-city/interior-style destinations.

## Confidence and Open Questions

Confidence is high for transport-network boundaries. Later route passes must choose exact timing for first owned horse, Hearthfire carriage services, Dead Man's Dread, Arvak or other summonable mounts, and dragon riding. Those are route-efficiency decisions layered on top of the fixed Survival travel rules.

## Linked Records

`data/constraints/survival-mode-constraints.md`; `data/npc/relationship-options.csv`; `data/properties/property-details.csv`; OBJ-000477; OBJ-001950; OBJ-001954; mount and property objective rows.
