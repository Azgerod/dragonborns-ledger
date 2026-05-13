# SN-000166 - Labyrinthian and Eye of Magnus Route

## Scope

Supports the v1 guide section `Labyrinthian And The Eye Of Magnus`.

This pass resolves the active College crisis that began with `Containment`: `The Staff of Magnus` is active, the Torc of Labyrinthian is in inventory, College services are disrupted, and `The Eye of Magnus` follows immediately after the Staff turn-in. The route therefore clears the Labyrinthian site, obtains the Staff of Magnus, completes the Eye of Magnus, restores the College, and claims the immediate Arch-Mage rewards before returning to the remaining Gauldur and College side-content work.

## Sources

| Source ID | Title | Tier | URL | Date | Use |
| --- | --- | --- | --- | --- | --- |
| SRC-001040 | Skyrim:The Staff of Magnus | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Staff_of_Magnus | 2026-05-13 | Quest entry from Containment, Torc use, Morokei, Staff of Magnus, Estormo, and Tolfdir turn-in. |
| SRC-001041 | Skyrim:Labyrinthian | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Labyrinthian | 2026-05-13 | Exterior complex, Wooden Mask, Lost Valkygg/Shalidor's Maze relation, main ruin layout, fixed spell tomes, Ancient Helmet, Slow Time wall, and Morokei chamber. |
| SRC-001042 | Skyrim:Shalidor's Maze | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shalidor%27s_Maze | 2026-05-13 | Maze sigils, Dismay word wall, Heal Other tome, Liminal Bridges copy, dremora trial, and Diadem of the Savant. |
| SRC-001043 | Skyrim:Lost Valkygg | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lost_Valkygg | 2026-05-13 | Proper entrance route, final chamber, clear state, and Aevar Stone-Singer copy. |
| SRC-001044 | Skyrim:The Eye of Magnus | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Eye_of_Magnus | 2026-05-13 | College barrier, Eye/Ancano fight, Psijic scene, Arch-Mage state, Archmage's Robes, and quarters key. |
| SRC-001045 | Skyrim:Arch-Mage's Quarters | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Arch-Mage%27s_Quarters | 2026-05-13 | Arch-Mage quarters ownership and post-quest access. |
| SRC-001046 | Skyrim:Boots (Arch-Mage) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Boots_(Arch-Mage) | 2026-05-13 | Arch-Mage's Boots location and ownership timing. |
| SRC-001047 | Skyrim:Wooden Mask | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Wooden_Mask | 2026-05-13 | Wooden Mask placement and later shrine use. |
| SRC-001048 | Skyrim:Diadem of the Savant | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Diadem_of_the_Savant | 2026-05-13 | Diadem source and unique-item handling. |
| SRC-001049 | Skyrim:Ancient Helmet of the Unburned | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ancient_Helmet_of_the_Unburned | 2026-05-13 | Ancient Helmet source in Labyrinthian Tribune. |
| SRC-001050 | Skyrim:Morokei (item) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Morokei_(item) | 2026-05-13 | Morokei mask source and preservation. |
| SRC-001051 | Skyrim:Archmage's Robes | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Archmage%27s_Robes | 2026-05-13 | Archmage's Robes reward timing. |
| SRC-001052 | Skyrim:Equilibrium | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Equilibrium | 2026-05-13 | Equilibrium fixed tome source in Labyrinthian Chasm. |
| SN-000165 | Mzulft and Winterhold crisis route | Project note | sources/source-notes/SN-000165-mzulft-winterhold-crisis-route.md | 2026-05-13 | Current College state, Containment handoff, Torc of Labyrinthian, and staged Arniel/Onmund work. |

## Route Decisions

`The Staff of Magnus` and `The Eye of Magnus` are routed immediately because the College crisis is already active and College services remain disrupted until the Eye is resolved. The guide does not insert the Gauldur finale between `Containment` and Labyrinthian.

Lost Valkygg and Shalidor's Maze are routed while the player is already at the Labyrinthian exterior. They are safe on-site objectives, include clearable/location work and direct unique rewards, and do not require a later quest state. This avoids a shallow return trip to the same exterior. The guide uses the proper Lost Valkygg entrance rather than entering through the upper exit door.

The Wooden Mask is acquired from the exterior circular building now because it is directly on site. The actual dragon-priest-mask shrine/Konahrik use remains later because it depends on the complete mask set.

The Shalidor's Maze rewards are routed now: Dismay `Maar`, `Spell Tome: Heal Other`, and Diadem of the Savant. The `Liminal Bridges` skill book in the maze and the `Aevar Stone-Singer` skill book in Lost Valkygg are left closed because the route is preserving skill-book reads for Scholar's Insight.

`Spell Tome: Heal Other`, `Spell Tome: Steadfast Ward`, and `Spell Tome: Equilibrium` now use fixed on-route Labyrinthian-site sources in `data/constraints/progression-source-selections.csv`. This is stronger than relying on later vendor stock or a broad cleanup pass. Equilibrium is moved from the old G14 cleanup source to the active Labyrinthian Chasm route, Heal Other is moved from a vendor source to Shalidor's Maze, and Steadfast Ward is moved from a vendor source to the Labyrinthian Tribune podium.

The Ancient Helmet of the Unburned, Staff of Magnus, Morokei, Archmage's Robes, and Arch-Mage's Boots are routed at their normal acquisition points and preserved as unique gear. Arch-Mage's Boots are taken only after `The Eye of Magnus` because the quarters become free to use after the Arch-Mage promotion.

Arniel's later stages, Onmund's Request, College repeatables, master ritual spells, and spell-vendor buying remain staged for a controlled College side-content section. This is not a theme-bucket hold: the active crisis has just been resolved, several of those systems involve random targets or skill/vendor conditions, and they are better handled after the College main quest is stable.

The guide-writing convention was updated during this pass for random assignments: ordinary randomized jobs should not be forced to a preferred target. They should be isolated from the main route, routed directly to the assigned target, and returned to the route hub without building the surrounding itinerary around that target.

## Coverage Summary

This pass places `The Staff of Magnus`, `The Eye of Magnus`, Labyrinthian, Lost Valkygg, Shalidor's Maze, Wooden Mask, Dismay `Maar`, `Spell Tome: Heal Other`, Diadem of the Savant, `Spell Tome: Equilibrium`, `Spell Tome: Steadfast Ward`, Ancient Helmet of the Unburned, Slow Time `Ul`, Staff of Magnus, Morokei, Archmage's Robes, and Arch-Mage's Boots.

Rows intentionally staged with concrete reasons: `Aevar Stone-Singer`, `Liminal Bridges`, the Wooden Mask shrine use/Konahrik outcome, Arniel's later stages, Onmund's Request, College repeatables, master rituals, and spell-vendor buying.

No TB-035-MR-036 `NEEDS ROUTE RESOLUTION` rows remain.
