# Source Note: Hircine and Bloated Man's Grotto Route

Status: researched.

Source note ID: SN-000141

## Claim

The v1 guide should handle Bloated Man's Grotto in its normal state before starting `Ill Met By Moonlight`, then use `HS-DAEDRIC-HIRCINE-GROTTO` to route the Savior's Hide outcome as a reload branch and the Ring of Hircine as the canonical main-route reward. Falkreath Barracks/Jail has colocated Elven Hunter start papers and skill books, but those should remain unopened during the Sinding visit.

## Routing Relevance

This section has a hard cell-state dependency: the quest version of Bloated Man's Grotto removes Bolar's Oathblade and changes the normal clear condition. It also has a branch dependency for the two Hircine artifacts and a Survival Mode caveat because the quest version can force a late-night entry. The player must enter Falkreath Jail to speak with Sinding, so the local AE documents and skill books need an explicit hold in player-facing prose.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000348 | Skyrim:Bloated Man's Grotto | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bloated_Man%27s_Grotto | 2026-05-12 | Normal-state clear condition, Bolar's Oathblade placement, quest-state replacement, and Survival Mode time-shift note. |
| SRC-000349 | Skyrim:Bolar's Oathblade | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bolar%27s_Oathblade | 2026-05-12 | Oathblade placement and quest-state availability caveat. |
| SRC-000350 | Skyrim:Ill Met By Moonlight | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ill_Met_By_Moonlight | 2026-05-12 | Sinding start path, White Stag step, Hircine outcomes, cursed-ring behavior, bugs, and dual-reward caveat. |
| SRC-000011 | Skyrim:Daedric Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Daedric_Quests | 2026-05-11 | Daedric Influence and Oblivion Walker artifact-count rules and Hircine artifact note. |
| SRC-000571 | Skyrim:Ring of Hircine | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ring_of_Hircine | 2026-05-13 | Ring reward state, cursed-ring behavior, and restored-ring power. |
| SRC-000572 | Skyrim:Savior's Hide | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Savior%27s_Hide | 2026-05-13 | Savior's Hide artifact reward. |
| SRC-000573 | Skyrim:Once A Hunter | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Once_A_Hunter | 2026-05-13 | Elven Hunter start documents and Sunderstone-area destination. |
| SRC-000127 | Skyrim:Alternative Armors - Elven Hunter | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alternative_Armors_-_Elven_Hunter | 2026-05-12 | Elven Hunter creation summary and member list. |
| SRC-000574 | Skyrim:Falkreath Barracks | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Falkreath_Barracks | 2026-05-13 | Barracks and jail layout, Sinding trigger, local papers, and skill-book placements. |

## Evidence Summary

UESP's Bloated Man's Grotto page states that the quest version replaces the normal inhabitants, removes the shrine contents including Bolar's Oathblade and Bolar's Writ, and only gives the normal cleared state after killing the non-quest animals and spriggans. The Bolar's Oathblade page gives the same availability caveat, with the post-quest recovery path requiring Sinding to be killed and the grotto left alone long enough to reset.

UESP's `Ill Met By Moonlight` page gives the Sinding start, White Stag hunt, and the two single-artifact outcomes. Killing Sinding yields Savior's Hide and removes the cursed ring. Sparing Sinding and killing the hunters leads to the restored Ring of Hircine after leaving the grotto. The page also records the dual-reward methods, but existing branch policy keeps those appendix/audit-only rather than making them the baseline route.

For the main-route Hircine outcome, the route should avoid hitting or healing Sinding while defending him, because UESP records that striking or healing him can turn him hostile. The quest page also says Sinding should be allowed to transform and escape after the jail conversation, records possible White Stag relocation bugs, and notes that the cursed ring can force werewolf transformations outdoors. The Bloated Man's Grotto and quest pages both record the quest-entry time shift to 11pm, which can matter under Survival Mode.

The Falkreath Barracks page places Sinding in the jail and records that approaching his cell starts the conversation. The same page lists Guard Dossier: Aesrael, Guard's Bounty Letter Draft, Guard's Note, The Legendary Sancre Tor, and The Black Arts On Trial in the barracks/jail. `Once A Hunter` starts from the Aesrael papers at the barracks but sends the player to Aesrael's camp near Sunderstone Gorge, where it overlaps with later Sunderstone/AE armor routing.

## Route Placement Decision

TB-035-MR-013 keeps the Hircine work as one coherent bundle: normal Bloated Man's Grotto clear, Bolar's Oathblade, Sinding, White Stag, Hircine hard save, Savior's Hide branch, and Ring of Hircine main route. The player-facing guide warns only about the same-building Falkreath papers and skill books because the player is being sent directly into the Barracks/Jail.

`Once A Hunter`, Guard Dossier: Aesrael, Guard's Bounty Letter Draft, Guard's Note, Aesrael's Journal, The Crimson Dirks v7, and the Elven Hunter armor set stay staged for the later Sunderstone/Alternative Armors route. This avoids starting an AE quest at the jail and leaving its destination unresolved across unrelated Hircine branch work.

Broad Falkreath-pine-forest locations such as Ancient's Ascent, Evergreen Grove, Greywater Grotto, Halldir's Cairn, Ilinalta's Deep, Peak's Shade Tower, Roadside Ruins, and Shriekwind Bastion are not part of this Hircine branch bundle. They need their own southern-location route pass with their local books, shouts, quest dependencies, and Delver/Explorer accounting rather than being inserted as a large wilderness sweep inside the Hircine outcome save.

## Confidence and Open Questions

Confidence is high for the Hircine/Bloated Man's Grotto route order, branch save, item availability, and immediate Falkreath Barracks holds. No MR-013 route-resolution notes remain unresolved. Later passes still need to place the Elven Hunter/Sunderstone bundle, the Falkreath Jail selected copy of The Black Arts On Trial in the Scholar's Insight reading plan, and the broader southern Falkreath clearable-location sweep.

## Linked Records

OBJ-000169; OBJ-000181; OBJ-000519; OBJ-000560; OBJ-000720; OBJ-000863; OBJ-000907; OBJ-001338; OBJ-001409; OBJ-001410; OBJ-001414; OBJ-001525; OBJ-001581; OBJ-001608; OBJ-001641; OBJ-001980; CHK-QUESTS-0175; CHK-QUESTS-0652; CHK-LOCATIONS-0992; CHK-UNIQUE-GEAR-1572; CHK-UNIQUE-GEAR-1662; CHK-UNIQUE-GEAR-1669; CHK-BOOKS-2136; CHK-BOOKS-2174; CHK-BOOKS-2432; CHK-BOOKS-2450; CHK-BOOKS-2477.
