# Source Note: Follower, Pet, and Mount Options

Status: needs review.

Source note ID: SN-000068

## Claim

Permanent followers, animal followers, household pet options, purchasable horses, and unique mounts should be tracked as candidate lists and source-list objective sets before route placement. Unique named mounts should also have objective rows where acquisition is completion-relevant.

## Routing Relevance

The specification requires a full follower/pet/mount/housecarl/steward/spouse list, while also avoiding branch routes for isolated preference choices. The option table supports later default recommendations, NPC-dependency checks, Survival Mode logistics, and checklist synchronization; the unique-mount rows preserve completion-relevant named mounts for routing.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000248 | Skyrim:Followers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Followers | 2026-05-12 | Lists permanent humanoid followers, creature followers, animal followers, prerequisites, marriage/steward flags, and AE Creation follower rows. |
| SRC-000249 | Skyrim:Horses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Horses | 2026-05-12 | Lists purchasable horses, unique horses, Hearthfire/Goldenhills horse services, and AE horse categories. |
| SRC-000250 | Skyrim:Arvak | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Arvak | 2026-05-12 | Cross-checks Arvak as a Dawnguard summonable horse tied to the Soul Cairn horse quest. |
| SRC-000251 | Skyrim:Shadowmere | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shadowmere | 2026-05-12 | Cross-checks Shadowmere as a Dark Brotherhood unique horse received during `The Cure for Madness`. |
| SRC-000252 | Skyrim:Frost | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Frost | 2026-05-12 | Cross-checks Frost as a unique horse tied to `Promises to Keep`. |
| SRC-000033 | Skyrim:Adoption | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Adoption | 2026-05-12 | Lists household pet options for adopted children. |

## Evidence Summary

UESP's Followers page groups permanent followers by faction/category and includes creature and Creation Club follower tables. `data/npc/relationship-options.csv` records 64 permanent humanoid follower candidates and 23 animal or creature follower candidates from that page, including AE rows for full-list reconciliation with earlier AE pet/follower objective rows.

UESP's Horses page lists purchasable stable horses and identifies unique horse categories. The option table records nine purchasable/steward-bought horse options plus unique mount rows for Frost, Shadowmere, and Arvak. Individual pages for Frost, Shadowmere, and Arvak support their quest links and named-mount status. The Adoption page supports five child pet options.

## Confidence and Open Questions

Confidence is high for source-list candidate membership. Later passes must still validate which followers/pets/mounts are required route acquisitions, which are option-list recommendations, exact quest or faction prerequisites, NPC death/safety risks, follower dismissal/recruitment bugs, horse ownership behavior, Survival Mode carry/travel implications, and overlap with already entered AE pet/mount rows.

## Linked Records

OBJ-001952 through OBJ-001957 and `data/npc/relationship-options.csv`.
