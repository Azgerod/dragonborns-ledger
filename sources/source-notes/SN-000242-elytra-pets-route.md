# Elytra Pets Route

Status: researched.

Source note ID: SN-000242

## Claim

The existing `Saints, Seducers, and Atronach Forge Tomes` guide section can close `My Pet Elytra (Mania)` and `My Pet Elytra (Dementia)` when it adds a pre-cage save, verifies quest completion and teleport-spell acquisition, and treats Elytra home/wait commands as conditional because the pet dialogue is source-recorded as bug-prone.

For this route:

- At the first Saints camp west of North Brittleshin Pass, clear the camp, take the Saints Bandit's Cage Key from the nearby chest, read `Note on Manic Elytra Nymph`, open the cage, speak to the Manic Elytra Nymph, accept it as a pet, and verify `Teleport Pet: Manic Elytra Nymph`.
- At the first Seducers camp near Fort Kastav, clear the camp, take the Seducers Bandit's Cage Key from the nearby chest, read `Note on Demented Elytra Nymph`, open the cage, speak to the Demented Elytra Nymph, accept it as a pet, and verify `Teleport Pet: Demented Elytra Nymph`.
- If home/wait commands appear, send each Elytra to a safe owned home. If those command options are missing, keep the pet acquisition and teleport-spell completion but do not rely on the Elytra for route-critical storage, home placement, dismissal, or branch-state control.

## Routing Relevance

This closes `OBJ-000638` `My Pet Elytra (Dementia)` and `OBJ-000639` `My Pet Elytra (Mania)`. It also validates the already routed pet rows `OBJ-000677` and `OBJ-000678`, note rows `OBJ-001473` and `OBJ-001474`, and spell checklist rows `CHK-SPELLS-0835` and `CHK-SPELLS-0838`.

The route keeps both pets inside the already planned `Balance of Power` camp progression instead of splitting the pet quests into separate detours. It also avoids promising a final home/dismissal state that may be unavailable on PS4.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001797 | Skyrim:My Pet Elytra (Dementia) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:My_Pet_Elytra_(Dementia) | 2026-05-29 | Used for Seducers camp quest location, cage objective, key/lock opening, pet acceptance, quest completion boundary, reward, and related Mania dialogue bug note. |
| SRC-001798 | Skyrim:My Pet Elytra (Mania) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:My_Pet_Elytra_(Mania) | 2026-05-29 | Used for Saints camp quest location, key source, cage opening, Manic Elytra acceptance, teleport spell reward, quest completion boundary, and Mania dialogue bug note. |
| SRC-001799 | Skyrim:Note on Demented Elytra Nymph | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Note_on_Demented_Elytra_Nymph | 2026-05-29 | Used for the note identity, quest relation, and first Seducers camp near Fort Kastav location. |
| SRC-001800 | Skyrim:Note on Manic Elytra Nymph | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Note_on_Manic_Elytra_Nymph | 2026-05-29 | Used for the note identity, quest relation, and first Saints camp near North Brittleshin Pass location. |
| SRC-001801 | Skyrim:Elytra Nymph | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Elytra_Nymph | 2026-05-29 | Used for the paired pet context, first Saints/Seducers camp locations, Mystic Venom daily harvest, and related quest list. |
| SRC-001802 | Skyrim:Demented Elytra Nymph | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Demented_Elytra_Nymph | 2026-05-29 | Used for the Demented pet's Fort Kastav camp cage, key source, carry capacity, home/city/wait commands, aura, Mystic Venom, and PS4-specific command-dialogue bug. |
| SRC-001803 | Skyrim:Manic Elytra Nymph | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Manic_Elytra_Nymph | 2026-05-29 | Used for the Manic pet's North Brittleshin camp cage, key source, carry capacity, home/city/wait commands, aura, Mystic Venom, and command-dialogue bug. |
| SRC-001804 | Skyrim:Balance of Power | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Balance_of_Power | 2026-05-29 | Used for Ri'saad start context, first Saints and Seducers camp sequence, cage/key/pet integration, and broader camp-order confirmation. |
| SRC-001805 | Skyrim:Teleport Pet (spells) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Teleport_Pet_(spells) | 2026-05-29 | Used for the two Elytra teleport spell entries and spell-awarded-at-quest-end confirmation. |

## Evidence Summary

UESP's `My Pet Elytra (Mania)` page says the quest begins by finding the Saints Bandit's Cage Key in a chest at the Saints camp west of North Brittleshin Pass, opening the cage, talking to the Manic Elytra Nymph, accepting it as a pet, and receiving `Teleport Pet: Manic Elytra Nymph` when the quest ends. The individual `Note on Manic Elytra Nymph` page places that note in the first Saints camp near North Brittleshin Pass and links it to the Mania pet quest.

UESP's `My Pet Elytra (Dementia)` page says the quest can be completed during `Balance of Power`, places the cage in the Seducers camp northwest of Windhelm, and says the cage can be opened with the key or by lockpicking. After the pet is freed, speaking to it and inviting it to come with you ends the quest. The individual `Note on Demented Elytra Nymph` page places that note in the first Seducers camp near Fort Kastav and links it to the Dementia pet quest.

The `Balance of Power` page ties both pet cages to the first Saints/Seducers camps and says each camp leader has a journal and a key to the camp's cage, with an Elytra Nymph inside that can be talked to and obtained as a pet. The `Elytra Nymph` page confirms the Manic pet is in the first Saints camp and the Demented pet is in the first Seducers camp. The `Teleport Pet (spells)` page confirms both Elytra teleport spells are awarded at the end of the corresponding `My Pet Elytra` quest.

The two individual pet pages list home, city, wait, carry, aura, Mystic Venom, and new-home dialogue behavior, but they also record command-dialogue bugs. The Demented Elytra page specifically marks the missing wait/return-home command issue for PlayStation-family platforms. The guide therefore must not require a successful home command as a completion condition on PS4. Pet acquisition, quest completion, and teleport spell learning are the stable completion checks; home/wait placement is an opportunistic cleanup command if available.

## Confidence and Open Questions

Confidence is high that the existing Saints/Seducers route is the right insertion point because both pet quests are explicitly tied to the first Saints/Seducers camp progression inside `Balance of Power`.

Confidence is high for the completion boundary: free the Elytra, accept it as a pet, and verify the corresponding teleport spell. Confidence is medium for reliable home/wait command availability on PS4 because UESP records command-dialogue bugs. The route now treats those commands as optional and does not depend on Elytra carry capacity or dismissal state.

There is no remaining open route question for `OBJ-000638` or `OBJ-000639` in the current guide. Broader Saints and Seducers item/material policy remains a separate unresolved row.

## Linked Records

OBJ-000638; OBJ-000639; OBJ-000677; OBJ-000678; OBJ-001473; OBJ-001474; CHK-SPELLS-0835; CHK-SPELLS-0838; BOOKLOC-001716; BOOKLOC-001717; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/books/book-document-locations.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
