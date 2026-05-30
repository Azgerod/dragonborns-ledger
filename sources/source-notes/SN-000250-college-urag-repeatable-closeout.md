# SN-000250 - College Urag Repeatable Closeout

Status: targeted TB-044 route-resolution source note.

## Scope

This note closes the Urag gro-Shub College repeatable bucket for `OBJ-000127` Fetch me that Book! and `OBJ-000128` Shalidor's Insights. It also resolves the related random-target document rows that were still marked as route-resolution risks because they are possible radiant targets rather than deterministic route pickups.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000004 | Skyrim:College of Winterhold (faction) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:College_of_Winterhold_(faction) | 2026-05-30 | College repeatable quest inventory and Urag as the giver for Fetch me that Book! and Shalidor's Insights. |
| SRC-001066 | Skyrim:Fetch me that Book! | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fetch_me_that_Book! | 2026-05-30 | Urag start, random book title list, boss-chest target behavior, over-140 dungeon target pool, pre-found book bug, Katariah/no-marker caveat, and Urag note caveat. |
| SRC-001067 | Skyrim:Shalidor's Insights | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shalidor%27s_Insights | 2026-05-30 | Urag start, boss-chest target behavior, over-140 dungeon target pool, 24-hour translation wait, random reward, gated target examples, inaccessible-target bugs, and reward behavior. |

## Route Decisions

Both Urag repeatables should be completed late, after the all-perks audit and after the main faction, Dark Brotherhood, Companions, Dragonborn, Dawnguard, and major dungeon gates have been opened. UESP records very large random target pools for both quests. Shalidor's Insights can choose locations gated by other quest progress, including Rebel's Cairn, Snow Veil Sanctum, The Katariah, Ysgramor's Tomb, and Nchardak. Placing the Urag block after the route has already opened those known gates is safer than forcing it during the first College pass.

The route should not manipulate ordinary random assignment. The player should ask Urag for Fetch me that Book!, follow the actual marker, retrieve the assigned book from the boss chest, return directly, then repeat the same isolated-job pattern for Shalidor's Insights. This follows the project rule for random assignments: complete the actual target and do not reshape the route around a preferred dungeon.

A hard save before accepting the Urag jobs is justified only as blocked-target recovery. UESP records several failure modes: a pre-found Fetch me that Book! copy can leave the quest pointing to an empty chest, Katariah-related target selection can leave no reachable marker until the proper Dark Brotherhood state, and Shalidor's Insights can choose inaccessible or bugged targets such as High Gate Ruins after Vokun is already defeated. The guide therefore creates `HS-COLLEGE-URAG-REPEATABLES`, but tells the player not to reload for convenience.

For Shalidor's Insights, the route accepts whatever reward Urag gives after the translation wait. UESP notes that the reward can be three identical scrolls or a one-point magic skill increase and that save/reload can force a preferred reward, but the project does not need reward manipulation here: by the routed placement, all skills and perks are already complete.

## Random-Target Document Resolution

The possible Fetch me that Book! titles are not independent required deterministic pickups in this route pass. They are conditionally represented by the actual assigned quest title: if Urag assigns one of those titles, the player retrieves that book from the active boss-chest marker and turns it in. Unassigned titles are not separately required merely because they exist in Urag's random list.

This resolves the COV-001R route-resolution rows for the remaining Fetch me that Book! possible-target document titles: `OBJ-001097`, `OBJ-001119`, `OBJ-001120`, `OBJ-001189`, `OBJ-001237`, `OBJ-001280`, `OBJ-001287`, and `OBJ-001289`. It also resolves `OBJ-001261` Shalidor's Insights (book), because that book is the quest object retrieved from the active Shalidor's Insights boss chest rather than a fixed-world collectible.

`Urag's Note` is not a separate preserved-document requirement. UESP records that Urag may not give a note even when he says he will, while the journal still updates and the quest proceeds normally. The player-facing route therefore relies on the journal marker and does not ask the player to preserve or verify Urag's note.

## Coverage Summary

This pass places one representative Fetch me that Book! completion and one representative Shalidor's Insights completion. It closes `CHK-QUESTS-0029`, `CHK-QUESTS-0031`, and `CHK-BOOKS-2423` through the same late Urag block. It also converts the related possible-target document rows from unresolved deterministic-pickup gaps into conditional random-target coverage.

## Linked Records

OBJ-000127; OBJ-000128; OBJ-001097; OBJ-001119; OBJ-001120; OBJ-001189; OBJ-001237; OBJ-001261; OBJ-001280; OBJ-001287; OBJ-001289; CHK-QUESTS-0029; CHK-QUESTS-0031; CHK-BOOKS-2423; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/constraints/radiant-boundaries.md`; `data/books/book-document-locations.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
