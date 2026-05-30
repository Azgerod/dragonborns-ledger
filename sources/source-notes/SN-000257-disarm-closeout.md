# SN-000257 - Disarm Closeout

Status: targeted TB-044 route-resolution source note.

## Scope

This note closes `OBJ-000770` Disarm by tying all three words to routed guide passes: Snow Veil Sanctum during `Speaking With Silence`, Eldersblood Peak during the Hjaalmarch/Pale cold-pass sweep, and Silverdrift Lair during `The Gray Cowl of Nocturnal`.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-001872 | Skyrim:Disarm | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Disarm | 2026-05-30 | Word identities, translations, word-wall locations, Snow Veil quest-lock note, and Disarm unique-weapon loss caveat. |
| SRC-001873 | Skyrim:Eldersblood Peak | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Eldersblood_Peak | 2026-05-30 | Dragon-lair identity, clearable state, Dragon Rising enemy state, Disarm word wall, boss chest, and word-wall bug. |
| SRC-000626 | Skyrim:Speaking With Silence | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Speaking_With_Silence | 2026-05-30 | Mercer-locked Snow Veil entry, Disarm word-wall chamber, Gallus journal handoff, and follower/Mercer bug cautions. |
| SRC-000627 | Skyrim:Snow Veil Sanctum | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Snow_Veil_Sanctum | 2026-05-30 | Quest-locked ruin state, no-normal-clear caveat, Model Ship room, Disarm word wall, and boss chest. |
| SRC-001855 | Skyrim:Silverdrift Lair | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Silverdrift_Lair | 2026-05-30 | Clearable state, Gray Cowl relation, Disarm word wall, boss chest, and Silverdrift bug cautions. |

## Route Decisions

UESP maps Disarm to Zun at Eldersblood Peak, Haal at Silverdrift Lair, and Viik at Snow Veil Sanctum. Snow Veil is quest locked, but the existing Thieves Guild route already starts `Speaking With Silence`, keeps followers away from Mercer's door path, enters the ruin, takes the Model Ship, and reaches the final chamber. This pass changes the guide wording from a generic Snow Veil Disarm word to Disarm: Viik.

Eldersblood Peak was already named in the Hjaalmarch marsh and cold-pass sweep, but only as a generic clear. This pass expands it into the actual closure: make a rotating manual save, defeat the dragon and any remaining troll threat, let soul absorption settle, learn Disarm: Zun, confirm the word was granted, loot the boss chest, and clear the lair. The save/confirmation exists because the source records a confirmed word-wall bug.

Silverdrift Lair was already routed late through `The Gray Cowl of Nocturnal`, after the earlier Pale sweep leaves it unentered. The existing Gray Cowl route already makes a rotating save before the word-wall room and confirms the Disarm word before accepting the save. This pass changes the guide wording to Disarm: Haal and closes the full three-word shout aggregate.

Snow Veil's source-listed no-clear behavior remains a deliberate clear exception, not an unresolved row. Silverdrift remains held until the Gray Cowl route because its quest chest, key corpse, document, sword, and word wall are best handled in one controlled pass.

Unlocking or using Disarm still depends on the route's dragon-soul pool. This note closes word acquisition and checklist representation, not dragon-soul spending.

## Coverage Summary

This pass closes `OBJ-000770` and checklist rows `CHK-DRAGON-SHOUTS-0904`, `CHK-DRAGON-SHOUTS-0905`, and `CHK-DRAGON-SHOUTS-0906`. It also validates the related location rows `OBJ-002030`, `OBJ-002149`, and `OBJ-002156`; checklist rows `CHK-LOCATIONS-1047`, `CHK-LOCATIONS-1224`, and `CHK-LOCATIONS-1231`; and the TB-038R guide-level unresolved row for Disarm.

## Linked Records

OBJ-000770; OBJ-002030; OBJ-002149; OBJ-002156; CHK-DRAGON-SHOUTS-0904; CHK-DRAGON-SHOUTS-0905; CHK-DRAGON-SHOUTS-0906; CHK-LOCATIONS-1047; CHK-LOCATIONS-1224; CHK-LOCATIONS-1231; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/locations/location-catalog.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
