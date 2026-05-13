# SN-000181 - Volkihar Finale Branch Continuation

Status: active source note for TB-035-MR-048A.

## Scope

This note supports the v1 guide section `Volkihar Finale Branch Continuation`. The section loads `HS-DG-BLOODLINE`, replays the required Volkihar main-quest spine on a temporary branch, completes Volkihar-side `Kindred Judgment`, completes `Destroying the Dawnguard`, then reloads canonical Dawnguard continuity.

## Sources

| Source ID | Source | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000026 | Skyrim:Volkihar Vampire Clan | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Volkihar_Vampire_Clan | 2026-05-13 | Volkihar membership path, faction quest inventory, and post-finale `Destroying the Dawnguard` availability. |
| SRC-000412 | Skyrim:Destroying the Dawnguard | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Destroying_the_Dawnguard | 2026-05-13 | Quest giver possibilities, Fort Dawnguard leader kill list, and turn-in boundary. |
| SRC-001169 | Skyrim:The Bloodstone Chalice | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Bloodstone_Chalice | 2026-05-13 | Required Volkihar branch opening quest replay from `HS-DG-BLOODLINE`. |
| SRC-001170 | Skyrim:Prophet (Vampire) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Prophet_(Vampire) | 2026-05-13 | Required vampire-side Prophet replay from `HS-DG-BLOODLINE`. |
| SRC-001241 | Skyrim:Kindred Judgment | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Kindred_Judgment | 2026-05-13 | Vampire-side finale path, Harkon confrontation, and post-finale Volkihar outcome. |
| SRC-001242 | Skyrim:Volkihar Keep | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Volkihar_Keep | 2026-05-13 | Volkihar-side castle ownership, courtyard repair through Garan, and branch-only home/service outcome. |

## Route Decisions

The continuation begins by making `HS-DG-MAIN-RETURN` on the already completed canonical Dawnguard save. This protects the completed Dawnguard-side `Kindred Judgment`, Fort Dawnguard survival, Serana transformation setup, and all canonical Soul Cairn/Forgotten Vale acquisitions before loading the older `HS-DG-BLOODLINE` fork.

The branch must replay the required Volkihar main quest spine from `HS-DG-BLOODLINE` because that is the clean faction-choice save. The guide routes only the required replay: `The Bloodstone Chalice`, vampire-side `Prophet`, the shared main quest path through `Touching the Sky`, Volkihar-side `Kindred Judgment`, then `Destroying the Dawnguard`. Optional Volkihar side assignments already recorded in MR-045 are not repeated unless a post-finale work request must be completed to cycle to `Destroying the Dawnguard`.

Shared Dawnguard worldspace content is not counted again on this branch. The branch may temporarily pass through Castle Volkihar courtyard, Soul Cairn, Ancestor Glade, Darkfall, and Forgotten Vale, but canonical Jiub/Arvak/Reaper/spell-tome/paragon/Unknown Book/ingredient/sun-shot coverage already lives on the Dawnguard main save.

`Destroying the Dawnguard` is treated as the branch target. The UESP page names the eight required Fort Dawnguard NPCs and separately notes that Bran, Sceolang, and exterior Dawnguard members are not required. The guide therefore names the eight required kills and avoids turning optional exterior combat into a completion target.

The branch records Castle Volkihar ownership and the free courtyard repair as Volkihar-side outcome evidence, but those outcomes are not canonical route state after the reload. Main continuity returns to the Dawnguard-aligned save where Fort Dawnguard remains intact and Serana remains uncured for transformation routing.

## Deferrals

Volkihar side radiants beyond the minimum assignment cycling needed to obtain `Destroying the Dawnguard` remain unexpanded here. MR-045 already covers the required representative Volkihar radiant types, rings, amulets, Ancient Power turn-ins, `New Allegiances`, and `The Gift`.

Death hound follower options CuSith and Garmr remain option-list rows, not canonical follower defaults. Recruiting them on this temporary branch would not survive the reload.

Castle Volkihar services, storage, and merchant use are not promoted to main-route logistics. They are useful only on the temporary Volkihar branch and disappear when `HS-DG-MAIN-RETURN` is reloaded.

No new unresolved `NEEDS ROUTE RESOLUTION` rows were introduced by this pass.

## Linked Records

HS-DG-BLOODLINE; HS-DG-MAIN-RETURN; OBJ-000356; OBJ-000357; OBJ-000360; OBJ-000361; OBJ-000358; OBJ-000359; OBJ-000362; OBJ-000363; OBJ-000364; OBJ-000378; CHK-QUESTS-0489; CHK-QUESTS-0490.
