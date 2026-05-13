# Source Note: Markarth Prison, Daedric Rites, And Reach Redoubts Route

Status: reviewed for TB-035-MR-019 draft placement.

Source note ID: SN-000147

## Claim

The v1 guide should expand the internal `Cidhna, Molag Bal, And Namira` bucket into a Markarth prison, Daedric, Temple of Dibella, and Reach-redoubt routing block. This pass completes `The Forsworn Conspiracy`, `No One Escapes Cidhna Mine`, `The House of Horrors`, `The Taste of Death`, `The Heart of Dibella`, `Speak to Degaine`, `Lisbet's Missing Shipment`, `The Affairs of Hagravens`, and the already-started `The Ghost of Old Hroldan` target when its actual redoubt target is cleared. It also synchronizes colocated unique items, quest books, clearable locations, Daedric artifact outcomes, and branch saves.

## Routing Relevance

The previous section deliberately stopped `The Forsworn Conspiracy` at the Shrine of Talos, recorded the Old Hroldan Hjalti target, and returned to Markarth with a clean save. This section uses that state to finish the Markarth prison chain, then starts the Markarth quests whose objectives point into overlapping Forsworn target pools before any of those redoubts are cleared. The route respects the player's actual randomized Logrolf, Lisbet, and Hjalti targets instead of rerolling, and it clears each unique target once while handling every active objective there.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000019 | Skyrim:Side Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Side_Quests | 2026-05-11 | Side quest inventory and Sideways caveats, including unusual counting cases. |
| SRC-000020 | Skyrim:Miscellaneous Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Miscellaneous_Quests | 2026-05-12 | Reach miscellaneous objectives, Hero of the People context, and Forgemaster's Fingers exclusion list. |
| SRC-000179 | Skyrim:The Heart of Dibella | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Heart_of_Dibella | 2026-05-11 | Temple of Dibella start path, Broken Tower/Fjotra objective, and Agent of Dibella reward. |
| SRC-000310 | Skyrim:Liar's Retreat (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Liar%27s_Retreat_(quest) | 2026-05-12 | Non-journal quest row for retrieving The Longhammer. |
| SRC-000366 | Skyrim:The Taste of Death | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Taste_of_Death | 2026-05-12 | Eola/Verulus path, Reachcliff Cave route, branch outcome, and Ring of Namira reward. |
| SRC-000380 | Skyrim:The House of Horrors | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_House_of_Horrors | 2026-05-12 | Tyranus start, abandoned house bug caution, Logrolf target/failure state, and Mace of Molag Bal reward. |
| SRC-000394 | Skyrim:No One Escapes Cidhna Mine | 2 - UESP | https://en.uesp.net/wiki/Skyrim:No_One_Escapes_Cidhna_Mine | 2026-05-12 | Cidhna Mine route, inventory return, Old Gods/Silver-Blood Ring reward path, and bug mitigations. |
| SRC-000436 | Skyrim:Sundered Towers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Sundered_Towers | 2026-05-12 | Sundered Towers is a Red Eagle Redoubt-linked secondary location rather than an independent Delver clear. |
| SRC-000688 | Skyrim:The Forsworn Conspiracy | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Forsworn_Conspiracy | 2026-05-13 | Margret/Weylin/Thonar/Nepos investigation path, evidence notes, arrest handoff, and bug workarounds. |
| SRC-000700 | Skyrim:The Ghost of Old Hroldan | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Ghost_of_Old_Hroldan | 2026-05-13 | Randomized Hjalti's Sword target list and turn-in boundary. |
| SRC-000708 | Skyrim:Lisbet's Missing Shipment | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lisbet%27s_Missing_Shipment | 2026-05-13 | Randomized Forsworn target pool and preclear bug. |
| SRC-000709 | Skyrim:Speak to Degaine | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Speak_to_Degaine | 2026-05-13 | Degaine statue job and Temple of Dibella/Heart of Dibella interaction. |
| SRC-000711 | Skyrim:Coated in Blood | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Coated_in_Blood | 2026-05-13 | Moth gro-Bagol favor and Orc-disposition context for later routing. |
| SRC-000712 | Skyrim:Reachcliff Cave | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Reachcliff_Cave | 2026-05-13 | Reachcliff Cave route, Namira shrine/secret exit, and skill-book placement. |
| SRC-000713 | Skyrim:Interception | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Interception | 2026-05-13 | Redguard Elite start path and later Karthwasten handoff. |
| SRC-000714 | Skyrim:Sanuarach Mine (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Sanuarach_Mine_(quest) | 2026-05-13 | Karthwasten mine dispute and Orc-disposition/Forgemaster interaction context. |
| SRC-000715 | Skyrim:The Affairs of Hagravens | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Affairs_of_Hagravens | 2026-05-13 | Melka/Petra route, Eye of Melka reward, and Sideways-relevant handling. |
| SRC-000716 | Skyrim:Liar's Retreat | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Liar%27s_Retreat | 2026-05-13 | Clearable location route, The Longhammer placement, and Biography of the Wolf Queen placement. |
| SRC-000717 | Skyrim:Rebel's Cairn (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rebel%27s_Cairn_(quest) | 2026-05-13 | Red Eagle's Fury/Bane conversion and Red Eagle's Rite route. |
| SRC-000718 | Skyrim:Red Eagle Redoubt | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Red_Eagle_Redoubt | 2026-05-13 | Red Eagle Redoubt boss camp, Red Eagle trigger books, and skill-book placement. |

## Evidence Summary

`The Forsworn Conspiracy` is routed as a controlled investigation rather than a normal city-side wander. Margret's Journal, Weylin's Note, Dryston's Note, Thonar's Journal, and Nepos's Journal are all source-linked evidence objects, and the source notes enough bug risk around Thonar/Nepos states to justify saves and non-lethal/pickpocket-first handling before the arrest handoff.

`No One Escapes Cidhna Mine` is routed from a named hard save because it is a bug-prone quest with inventory return, animal/pet, and Thieves Guild special-job risks. The route dismisses pets, avoids hotkeyed item-smuggling tricks, and confirms inventory return. The guide uses the source-supported both-reward path: side with Madanach long enough to receive the Old Gods set, then kill Madanach and the escaping Forsworn before exiting so Thonar can award the Silver-Blood Family Ring. The direct kill-Madanach path is not the main route because it would forfeit the Old Gods set.

Molag Bal and Namira are included in the same Markarth block because both start in Markarth and point into Reach dungeons or Forsworn target spaces. `The House of Horrors` is started and entered immediately to avoid a known abandoned-house state issue, then Logrolf's actual target is recorded. `The Taste of Death` is staged through Verulus and Eola, then finished through a hard-save fork so the branch records the save-Verulus outcome while the main route keeps the Ring of Namira artifact for `Oblivion Walker`.

`Speak to Degaine` and `The Heart of Dibella` are bundled deliberately. The guide first completes Degaine's statue theft cleanly, then returns to the Inner Sanctum and accepts Hamal's Sybil objective. This avoids mixing an unnoticed theft objective with the forced-priestess confrontation in the wrong order.

`Lisbet's Missing Shipment`, `The House of Horrors`, and `The Ghost of Old Hroldan` can all point to overlapping Forsworn camps/redoubts. Lisbet's source lists a preclear risk, so the guide starts her quest before clearing possible targets. The route then builds a target list from Broken Tower Redoubt, Logrolf's target, Lisbet's target, and Hjalti's target, clears each unique target once, and handles every active retrieval/freeing objective there. This avoids RNG manipulation while preventing duplicated travel or accidental preclear failures.

Broken Tower Redoubt is mandatory in this pass because Fjotra is there for `The Heart of Dibella`. Conditional targets cover Bruca's Leap, Deepwood, Dragon Bridge Overlook, Druadach, Hag Rock, Red Eagle, and Serpent's Bluff. If Red Eagle Redoubt is active, the guide finishes the linked Red Eagle/Rebel's Cairn chain immediately because the trigger book, Red Eagle's Fury, Red Eagle's Rite, Rebel's Cairn, and Red Eagle's Bane are one coherent objective bundle.

Liar's Retreat is routed now because it sits in the same Reach/Karthwasten redoubt travel band and its finite non-journal quest, clearable location, and The Longhammer item all complete together. Blind Cliff Cave is routed now because `The Affairs of Hagravens` is nearby, source-listed as a dungeon miscellaneous quest with Sideways caveat coverage, and awards Eye of Melka. Reachcliff Cave is routed when Namira requires it, with the Reachcliff Secret Entrance marker handled on the same exit path.

Skill books in the routed rooms are still left closed. The current route has not reached the planned skill-book reading window, so local warnings remain only where the guide sends the player into the exact room or dungeon that contains the copy. In particular, the Cidhna copy of `Proper Lock Design` is not consumed here; a later skill-book pass must use a different planned source copy or revisit the selected source list.

## Nearby Objective Audit And Deferrals

Sanuarach Mine is not completed during the Karthwasten visit. The route only uses Karthwasten to discover the marker and speak to Enmon for Fjotra because Sanuarach is one of the quests that can block `The Forgemaster's Fingers` if completed first. Kolskeggr Mine, `Coated in Blood`, Skilled Apprenticeship, Dushnikh Yal, and the Orc stronghold route stay together for a later Orc/Forgemaster/Blood-Kin bundle.

`Interception` and Redguard Elite Armaments are held because the source starts that Creation quest from Azadi near Shor's Stone and only later sends the player to Karthwasten and Purewater Run. Merely being in Karthwasten during this section is not a clean quest start, and Purewater Run is better routed with the Redguard Elite objective path.

Reach property, Vlindrel Hall, Thane of the Reach, Argis, merchant investments, and Reach house storage remain held. The current route has no validated money plan for a Markarth home immediately after the earlier Riften property work, and investments require the later Speech/Investor state.

Sky Haven Temple and Dragonbane remain hard-held by the level 46 Dragonbane gate. The guide should not discover or enter Sky Haven while routing Reach redoubts.

## Confidence and Open Questions

Confidence is high for the Markarth investigation, Cidhna both-reward route shape, Molag Bal/Namira hard-save handling, Dibella/Degaine ordering, Lisbet preclear timing, and the overlapping-target conditional branch structure. Confidence is medium for the exact no-console recovery if Thonar's post-escape reward scene fails after the both-reward path; the guide uses a named hard save and retry language rather than falling back to a reward-losing direct-kill route. No TB-035-MR-019 `NEEDS ROUTE RESOLUTION` notes remain, but the skill-book source plan must remember that the Cidhna `Proper Lock Design` copy was deliberately left unread.

## Linked Records

OBJ-000174; OBJ-000175; OBJ-000187; OBJ-000188; OBJ-000189; OBJ-000268; OBJ-000273; OBJ-000275; OBJ-000277; OBJ-000285; OBJ-000338; OBJ-000344; OBJ-000802; OBJ-000826; OBJ-000833; OBJ-000837; OBJ-000841; OBJ-000842; OBJ-000849; OBJ-000853; OBJ-000862; OBJ-000867; OBJ-000868; OBJ-000870; OBJ-000884; OBJ-000894; OBJ-000896; OBJ-000902; OBJ-000989; OBJ-001131; OBJ-001188; OBJ-001210; OBJ-001215; OBJ-001225; OBJ-001249; OBJ-001277; OBJ-001290; OBJ-001564; OBJ-001609; OBJ-001645; OBJ-001652; OBJ-001686; OBJ-001687; OBJ-001688; OBJ-001689; OBJ-001740; OBJ-001782; OBJ-001978; OBJ-001993; OBJ-001997; OBJ-002020; OBJ-002022; OBJ-002026; OBJ-002060; OBJ-002085; OBJ-002121; OBJ-002123; OBJ-002124; OBJ-002139; OBJ-002232; OBJ-002284; OBJ-002287; OBJ-002325; OBJ-002330; OBJ-002354; OBJ-002481; OBJ-002730 through OBJ-002733; OBJ-002758; NPCOPT-000003; NPCOPT-000020; NPCOPT-000023; NPCOPT-000031; NPCOPT-000103; NPCOPT-000193.
