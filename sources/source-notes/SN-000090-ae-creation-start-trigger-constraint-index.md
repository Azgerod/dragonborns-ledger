# Source Note: AE Creation Start-Trigger Constraint Index

Status: needs review.

Source note ID: SN-000090

## Claim

The TB-011 constraint table records package-level start or acquisition triggers for all 74 official Anniversary Edition Creation Club Creations. These rows are routing constraints and discovery rules, not route instructions.

## Routing Relevance

The specification requires all official AE Creation Club content to be included without dumping it into a separate late block. The route cannot place AE quests, homes, pets, crafting systems, spells, ingredients, or unique rewards until their package start methods, broad regions, level gates, and obvious route delays are visible in one constraint table.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000054 | Bethesda support: What does Skyrim Anniversary Edition include? | 1 - Bethesda official support | https://help.bethesda.net/app/answers/detail/a_id/54327/ | 2026-05-11 | Official AE bundle scope. |
| SRC-000055 | Skyrim:Creation Club | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Creation_Club | 2026-05-12 | Official Creation Club context, 74-Creation AE set, and package-level hints. |
| SRC-000057 | Skyrim:Creation Club First Time Players | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Creation_Club_First_Time_Players | 2026-05-12 | Spoiler-light location/start table used to classify start areas. |
| SRC-000058 | Skyrim:Creation Club Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Creation_Club_Quests | 2026-05-12 | Creation Club quest inventory by package. |
| SN-000035 | AE Bundle Membership and Parent Creation Inventory | Local source note | sources/source-notes/SN-000035-ae-bundle-membership-and-parent-inventory.md | 2026-05-11 | Existing source-backed 74-package parent manifest. |
| SN-000036 | AE Creation Quest Inventory | Local source note | sources/source-notes/SN-000036-ae-creation-quest-inventory.md | 2026-05-11 | Existing source-backed AE quest child-row inventory. |

## Evidence Summary

Bethesda's support article defines Anniversary Edition as the official bundle scope used by this project. UESP's Creation Club page identifies the official Creation Club context and the AE package set, while the First Time Players and Creation Club Quests pages provide package-level discovery and quest inventory cross-checks. The existing local manifest already records all 74 package parent rows and the source-list child coverage created in Phase 1.

TB-011 reduces the broad AE objective queue into one package-level constraint row per official Creation. Child objective rows remain covered by their package row unless a later constraint pass needs a more specific quest, item, NPC, bug, cell-entry, or branch row.

## Confidence and Open Questions

Confidence is high for the 74-package scope and package-level start/acquisition hints. Confidence is medium for using broad package hints as final route placement rules; later TB-012 through TB-020 passes must still verify leveled rewards, cell locks, conflicts, bugs, NPC dependencies, Survival Mode logistics, and skill/crafting timing before route placement.

During this pass, direct UESP requests were made reliable by fetching through the MediaWiki API with a browser User-Agent, wrapped in `tools/fetch_uesp.py`. Any row whose exact trigger depends on a quest page that was not individually checked remains marked `needs_review`, not `validated`.

## Linked Records

`data/constraints/ae-creation-start-triggers.md`; `data/objectives/ae-creation-manifest.md`; OBJ-000479 through OBJ-000759; OBJ-000813; OBJ-000814; OBJ-000912; OBJ-000913; OBJ-000919; OBJ-000920; OBJ-000922; OBJ-000935 through OBJ-000937; OBJ-000942 through OBJ-000944; OBJ-000947; OBJ-000949; OBJ-000951; OBJ-000953; OBJ-000955; OBJ-000956; OBJ-000958; OBJ-000959; OBJ-000961; OBJ-000963 through OBJ-000965; OBJ-000969; OBJ-000970; OBJ-000972; OBJ-000973; OBJ-000978 through OBJ-000981; OBJ-000986; OBJ-000987; OBJ-000991; OBJ-000998; OBJ-001000; OBJ-001004; OBJ-001008; OBJ-001011; OBJ-001013 through OBJ-001016; OBJ-001031; OBJ-001033; OBJ-001336 through OBJ-001554; OBJ-001893 through OBJ-001918; OBJ-001951; OBJ-002206; OBJ-002210; OBJ-002211; OBJ-002218; OBJ-002254; OBJ-002258; OBJ-002262; OBJ-002269; OBJ-002308; OBJ-002332; OBJ-002336; OBJ-002340; OBJ-002346; OBJ-002352; OBJ-002385; OBJ-002389; OBJ-002409 through OBJ-002424; OBJ-002495; OBJ-002496; OBJ-002637 through OBJ-002710; OBJ-002712; OBJ-002716.
