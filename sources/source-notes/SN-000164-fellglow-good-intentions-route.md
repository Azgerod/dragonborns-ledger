# SN-000164 - Fellglow Keep and Good Intentions Route

## Scope

Supports the v1 guide section `Fellglow Keep And Good Intentions`.

This pass removes the stale standalone Mage's Circlet gate. The current v1 route has already passed the level-40 Shield of Solitude gate before returning to the College, so the level-25 Mage's Circlet threshold is no longer an active player-facing checkpoint. The guide now treats Mage's Circlet as a normal preserved reward acquired while completing `Good Intentions`.

## Sources

| Source ID | Title | Tier | URL | Date | Use |
| --- | --- | --- | --- | --- | --- |
| SRC-001034 | Skyrim:Hitting the Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hitting_the_Books | 2026-05-13 | Fellglow quest sequence, Orthorn options, quest-book titles, Urag reward books, Tolfdir return, and re-entry bug. |
| SRC-001035 | Skyrim:Fellglow Keep | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fellglow_Keep | 2026-05-13 | Fellglow local books/tomes, Stone of Barenziah, Caller outcome, no-clear state during the quest, and crash risk. |
| SRC-000343 | Skyrim:Good Intentions | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Good_Intentions | 2026-05-12 | Good Intentions sequence, Mage's Circlet reward, Revealing the Unseen follow-up, Augur ordering, and bugs. |
| SRC-001036 | Skyrim:Tolfdir the Absent-Minded | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Tolfdir_the_Absent-Minded | 2026-05-13 | Alembic prerequisite, search locations, completion behavior, and repeat-dialogue bug. |
| SRC-001037 | Skyrim:Arniel's Endeavor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Arniel%27s_Endeavor | 2026-05-13 | Arniel part-one start, ten-cog requirement, Mzulft cog support, and later stage caveats. |
| SRC-001038 | Skyrim:Revealing the Unseen | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Revealing_the_Unseen | 2026-05-13 | Mzulft dependency and pre-clear bug context for the next College section. |
| SRC-000722 | Skyrim:Mzulft | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mzulft | 2026-05-13 | Mzulft access lock, Dwarven Storeroom, ten cogs, and Dwemer convectors for next-section planning. |
| SRC-000996 | Skyrim:Onmund's Request | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Onmund%27s_Request | 2026-05-13 | Random Grand Staff of Charming target, follower/marriage reward, and staff/persuasion caveats. |
| SN-000092 | Leveled quest reward thresholds and locks | Project note | sources/source-notes/SN-000092-leveled-quest-reward-thresholds-and-locks.md | 2026-05-13 | Confirms the level-25 Mage's Circlet threshold already protected by the current higher-level route state. |

## Route Decisions

`Hitting the Books` is now completed at Fellglow Keep because `Under Saarthal` already advanced the College questline to Urag's Fellglow lead. Fellglow is entered through the quest route, Orthorn is freed but sent away, and the Caller is killed so the Ritual Chamber key and clean exterior exit are secured without sacrificing Orthorn or relying on a persuasion outcome.

Fellglow is not marked clear in this pass. UESP records that the location cannot be cleared during `Hitting the Books` because the boss is disabled, and it also records a crash risk when re-entering after clearing or backtracking from the Ritual Chamber. The guide therefore tells the player to leave through the Ritual Chamber exterior path and records Fellglow's clearable-location row as staged for a later source-backed clear decision.

The Fellglow Stone of Barenziah is routed immediately because the quest path reaches the west room with the crafting stations and the stone has no reward or quest-state gate. `Spell Tome: Sparks` is also routed here: the fixed tome is in the upper circular library room on the quest path, making it better than the prior College vendor-stock default. `data/constraints/progression-source-selections.csv` now selects the Fellglow fixed source for Sparks.

The Fellglow copies of `The Doors of Oblivion` and `A Hypothetical Treachery` remain closed because they are skill books and the current route has not reached the Scholar's Insight reading window. The selected source for `The Doors of Oblivion` is moved away from Fellglow to the late Sightless Pit exterior skeleton copy because Fellglow is being visited too early and has post-quest access/crash risks. The Aretino Residence source remains the selected copy for `A Hypothetical Treachery`.

Urag's reward skill books are listed in the player guide because the player receives them here, but they are not counted as read. The guide instructs the player to keep `Daughter of the Niben`, `2920, Hearth Fire, v9`, `Response to Bero's Speech`, `Catalogue of Weapon Enchantments`, `The Black Arts On Trial`, and `Racial Phylogeny` unread until the late skill-book reading window.

Arniel's first stage is started now because UESP records it as available after `Hitting the Books`, and the next College/Dwemer route can collect the ten Dwarven Cogs naturally in Mzulft. The guide does not route a special cog trip here.

`Tolfdir the Absent-Minded` is routed now because UESP records that Tolfdir returns to the College during `Hitting the Books`, making the alembic quest available. The guide also includes the repeat-dialogue warning because selecting the quest dialogue again after completion can re-add an unfinishable objective.

`Good Intentions` is completed in sequence: speak to Tolfdir, follow Ancano only after he directs the player to the Arch-Mage's Quarters, speak to Quaranir, ask Tolfdir about the Augur before entering the Midden, speak to the Augur, and report to Savos for Mage's Circlet. This ordering protects the Good Intentions bug notes without exposing internal bug mechanics in the guide.

`Revealing the Unseen` is allowed to start after `Good Intentions`, but the guide stops before Mirabelle's Mzulft briefing. The next College section should decide whether to route Mzulft immediately or interleave another source-backed objective block, but it must preserve the Mzulft pre-clear warning.

`Onmund's Request` remains held. Starting it now can create a random Grand Staff of Charming target, including locations already routed or fragile to revisit such as Fellglow Keep. Because UESP also records staff/persuasion caveats, the safer route is to resolve Onmund in a controlled later College-side pass before any route state would make Enthir dialogue unsafe.

## Coverage Summary

This pass places `Hitting the Books`, the Fellglow Stone of Barenziah, `Spell Tome: Sparks`, the three stolen quest books, `Good Intentions`, Mage's Circlet, `Tolfdir the Absent-Minded`, and Arniel part-one start/staging.

Rows intentionally staged with concrete reasons: Fellglow Keep clear tag, the Fellglow skill-book copies, Urag's six reward skill-book reads, later Arniel stages/reward spells, `Onmund's Request`, and the Mzulft/Revealing continuation.

No TB-035-MR-034 `NEEDS ROUTE RESOLUTION` rows remain.
