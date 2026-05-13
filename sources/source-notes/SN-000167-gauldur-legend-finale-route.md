# SN-000167 - Gauldur Legend Finale Route

## Scope

Supports the v1 guide section `Gauldur Legend Finale`.

This pass completes the remaining `Forbidden Legend` work after Folgunthur/Mikrul and Saarthal/Jyrik have already been routed. The route handles Geirmund's Hall, Sigdis Gauldurson, the Gauldur Blackbow, Reachwater Rock, the Emerald Dragon Claw, `Ancient Edict`, the final ghost fight, The Gauldur Amulet, and the quest-completion/Sideways tracking boundary.

## Sources

| Source ID | Title | Tier | URL | Date | Use |
| --- | --- | --- | --- | --- | --- |
| SRC-001053 | Skyrim:Forbidden Legend | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Forbidden_Legend | 2026-05-13 | Remaining quest order, Geirmund/Reachwater sequence, final reforge, Gauldur rewards, Sideways qualifier context, and level-36 linked-dungeon warning already satisfied by current route state. |
| SRC-001054 | Skyrim:Geirmund's Hall | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Geirmund%27s_Hall | 2026-05-13 | Geirmund's Hall location, clearable state, sinkhole route, pillar solution, Geirmund's key, Sigdis encounter, Gauldur Blackbow, `Writ of Sealing (Sigdis)`, and `Words and Philosophy` copy. |
| SRC-001055 | Skyrim:Reachwater Rock | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Reachwater_Rock | 2026-05-13 | Reachwater Rock access, Emerald Dragon Claw and `Ancient Edict`, puzzle doors, final Gauldur chamber, clearable state, and fishing-source audit. |
| SRC-001056 | Skyrim:Gauldur Blackbow | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Gauldur_Blackbow | 2026-05-13 | Gauldur Blackbow source, level-36 maximum tier, and linked-dungeon spawn behavior. |
| SRC-001057 | Skyrim:The Gauldur Amulet | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Gauldur_Amulet | 2026-05-13 | Final amulet acquisition from combining fragments and preservation as unique gear. |
| SRC-001058 | Skyrim:Circlet of Waterbreathing | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Circlet_of_Waterbreathing | 2026-05-13 | Confirms Circlet of Waterbreathing belongs to Dawnguard `Touching the Sky`, not this underwater Gauldur route. |
| SRC-001059 | Skyrim:Words and Philosophy | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Words_and_Philosophy | 2026-05-13 | Skill-book source list, including Geirmund's Hall and Apocrypha/The Winds of Change copies. |
| SRC-001060 | Skyrim:Ancient Edict | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ancient_Edict | 2026-05-13 | `Ancient Edict` source at Reachwater Rock and relation to `Forbidden Legend`. |
| SRC-001061 | Skyrim:Geirmund's Epitaph | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Geirmund%27s_Epitaph | 2026-05-13 | `Geirmund's Epitaph` source in Geirmund's Hall and relation to `Forbidden Legend`. |
| SRC-001062 | Skyrim:Writ of Sealing (Sigdis) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Writ_of_Sealing_(Sigdis) | 2026-05-13 | `Writ of Sealing (Sigdis)` source in Geirmund's Hall and relation to `Forbidden Legend`. |
| SN-000155 | Potema, Shield, Folgunthur, and Bone Wolf route | Project note | sources/source-notes/SN-000155-potema-shield-bone-wolf-route.md | 2026-05-13 | Prior Folgunthur/Mikrul state, `Lost Legends`, Ivory Dragon Claw, Gauldur Blackblade, and Mikrul fragment completion. |
| SN-000162 | Winterhold College opening route | Project note | sources/source-notes/SN-000162-winterhold-college-opening-route.md | 2026-05-13 | Prior Saarthal/Jyrik state, Jyrik fragment, Staff of Jyrik, and Writ of Sealing (Jyrik). |
| SN-000166 | Labyrinthian and Eye of Magnus route | Project note | sources/source-notes/SN-000166-labyrinthian-eye-of-magnus-route.md | 2026-05-13 | Current state after the College main quest: College services restored, Arch-Mage state active, and College side content still staged. |

## Route Decisions

Geirmund's Hall and Reachwater Rock are routed now because both earlier `Forbidden Legend` linked dungeons are already complete and the old level-36 linked-dungeon gate is already satisfied. Holding the remaining Gauldur dungeons after the College crisis would create a stale theme bucket rather than protecting a live constraint.

The route starts from the restored College state rather than interrupting `Revealing the Unseen`, `Containment`, `The Staff of Magnus`, or `The Eye of Magnus`. That keeps the active College crisis intact while still completing `Forbidden Legend` before the later College side-content and level-46 main-quest work.

Geirmund's Hall is routed as a full clear. The guide includes the source-backed pillar solution, Lord Geirmund's key, the hidden drawbridge lever, the Sigdis identification cue, `Geirmund's Epitaph`, `Writ of Sealing (Sigdis)`, the final fragment, and the Gauldur Blackbow. The Gauldur Blackbow is preserved as unique leveled gear and is not used as an Absorb Magicka disenchant source.

`Words and Philosophy` is not read in Geirmund's Hall. This is a same-room skill-book candidate, but skill-book reads remain held for the Scholar's Insight window. The selected source in `data/constraints/progression-source-selections.csv` is changed from the Geirmund's Hall copy to the Apocrypha/The Winds of Change copy because that later copy is naturally aligned with the Black Book/Scholar's Insight route. The Geirmund copy therefore only needs a concise local leave-closed instruction in player prose.

The nearby `2920, Frostfall, v10` summit copy south of Geirmund's Hall and `Death Blow of Abernanit` copy west-southwest of Reachwater Rock are audited but not routed. Both are unmarked or non-dungeon same-region candidates, both have other selected sources, and the skill-book reading gate is still active.

Reachwater Rock is routed immediately after Geirmund's Hall because the player now has all three fragments and the Ivory Dragon Claw. The guide collects the Emerald Dragon Claw, reads and takes `Ancient Edict`, uses the Emerald and Ivory claw doors, fights the three brother ghosts, takes The Gauldur Amulet, completes `Forbidden Legend`, and adds it to Sideways tracking if the trophy is still open.

Fishing supplies and fishing-source data at Geirmund's Hall and Reachwater Rock are not started here. Using Fishing Supplies starts the Fishing Creation route, and the fish rows are better handled in the controlled fishing quest/counter pass rather than as random catches inside a Gauldur finale. The Circlet of Waterbreathing is also not routed here; UESP places it in the Dawnguard Inner Sanctum during `Touching the Sky`.

The guide keeps followers, pets, summons, and temporary allies dismissed through the Gauldur finale because the source pages record follower/pet/summon-sensitive risks in the water passage and final chamber. The player-facing route states the clean intended setup without adding recovery or bug-workaround prose.

## Coverage Summary

This pass places `Forbidden Legend`, Geirmund's Hall, `Geirmund's Epitaph`, `Writ of Sealing (Sigdis)`, Gauldur Blackbow, Reachwater Rock, Emerald Dragon Claw, `Ancient Edict`, and The Gauldur Amulet. It also records the Sideways-tracking boundary for `Forbidden Legend`.

Rows intentionally staged with concrete reasons: `Words and Philosophy` is moved to the late Apocrypha/The Winds of Change skill-book source; nearby `2920, Frostfall, v10` and `Death Blow of Abernanit` copies remain duplicate skill-book candidates; Fishing/Caught in the Rain and Fishing item rows remain for the controlled fishing pass; Circlet of Waterbreathing remains for Dawnguard `Touching the Sky`; College side quests, College radiants, master rituals, and spell-vendor buying remain for the next College side-content section.

No TB-035-MR-037 `NEEDS ROUTE RESOLUTION` rows remain.
