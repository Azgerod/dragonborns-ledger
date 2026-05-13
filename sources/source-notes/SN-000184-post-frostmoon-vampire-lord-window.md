# SN-000184 - Post-Frostmoon Vampire Lord Window

## Scope

Supports the v1 guide section `Post-Frostmoon Vampire Lord Window`.

This pass closes the werewolf dependency after Frostmoon Crag, opens Vampire Lord access on canonical Dawnguard continuity through Serana, starts explicit Vampire Lord perk tracking, and deliberately holds Falion's `Rising at Dawn` cure plus the final Serana cure-state choice until Vampire Mastered is actually complete.

## Sources

| Source ID | Use |
| --- | --- |
| SRC-000170 | Lycanthropy cure and replacement rules, Ring of Hircine support, werewolf perk-tree feed count, Werewolf Mastered 11-perk boundary, and the reason Beast Blood must be complete before Serana conversion. |
| SRC-000171 | Vampire Lord acquisition through Serana on a Dawnguard-compatible route, qualifying Vampire Lord perk-kill methods, 165-kill full-tree requirement, 11-perk Vampire Mastered boundary, and Serana-follower Vampiric Drain interaction. |
| SRC-000172 | Normal vampirism state context after Vampire Lord conversion and final mortal-state cure implications. |
| SRC-001237 | Serana post-`Kindred Judgment` Vampire Lord service, Serana cure dialogue and return behavior, and the reason curing Serana is held until her vampire services are no longer needed. |
| SRC-001249 | `Rising at Dawn` start boundary, Falion cure route, filled Black Soul Gem requirement, dawn ritual, and The Black Star exclusion for the cure item. |

## Routing Decisions

Frostmoon Crag and the four Majni ring purchases are complete before this section, so Beast Blood is no longer needed for Frostmoon access. The guide still requires the player to confirm all eleven werewolf perks before replacing Beast Blood, because UESP records that Serana's Vampire Lord infection cures lycanthropy and the werewolf achievement requires all eleven werewolf perks.

The section does not force an immediate 165-kill Vampire Lord grind. UESP records that the Vampire Lord tree requires eleven perks and 165 qualifying kills, with progress coming from Vampiric Drain or power-bite kills. Forcing that entire tree into one small post-Frostmoon section would require either a disconnected grind or an exploit-like route distortion. The guide instead opens the Vampire Lord window now and carries explicit perk-counter tracking into the next fresh hostile Solstheim content.

Serana is used for the canonical Dawnguard-compatible Vampire Lord conversion because Harkon's gift belongs to the reloaded Volkihar branch. After conversion, the guide dismisses Serana before perk work because UESP records that Serana following reduces the damage component of Vampire Lord Vampiric Drain, which is the main planned perk-progress method.

`Rising at Dawn` is deliberately not started in this section. The route needs the player to stay vampire/Vampire Lord until Vampire Mastered is complete. Falion's cure remains the selected final mortal-state cure path after the perk tree is done; the guide already tells the player not to use The Black Star for the ritual because UESP says Falion requires a filled Black Soul Gem and The Black Star will not work.

Serana's personal cure is held. UESP records that Serana can be asked about curing herself after Dawnguard-side `Kindred Judgment`, and that choosing supportive dialogue sends her away to be cured by Falion. The main route keeps her uncured for now because her Vampire Lord service and blood-arrow service should not be removed before the player cure and Vampire Mastered window are closed. The final cure-state choice remains a later option/default decision.

## Unresolved

No new `NEEDS ROUTE RESOLUTION` rows were introduced by this pass.

The later Vampire Lord closeout section must close the 11-perk counter, route `Rising at Dawn`, and make the final Serana cure-state recommendation after the route has accumulated enough fresh hostile content for Vampire Mastered without relying on an exploit.

## Linked Records

OBJ-000815; OBJ-000816; OBJ-000817; OBJ-000818; OBJ-000192; NPCOPT-000160; CHK-PERKS-3667; CHK-PERKS-3668; CHK-PERKS-3670; CHK-PERKS-3671; CHK-PERKS-3673; CHK-PERKS-3674; CHK-PERKS-3676; CHK-PERKS-3677; CHK-PERKS-3679; CHK-PERKS-3680; CHK-PERKS-3682; CHK-PERKS-3683; CHK-PERKS-3685; CHK-PERKS-3686; CHK-PERKS-3688; CHK-PERKS-3689; CHK-PERKS-3691; CHK-PERKS-3692; CHK-PERKS-3694; CHK-PERKS-3695; CHK-PERKS-3696; CHK-PERKS-3697; CHK-QUESTS-0271.
