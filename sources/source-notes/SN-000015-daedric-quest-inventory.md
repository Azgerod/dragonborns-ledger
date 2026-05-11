# Source Note: Daedric Quest Inventory

Status: needs review.

Source note ID: SN-000015

## Claim

UESP's Daedric quest table lists the base-game Daedric quest inventory, level requirements, associated Daedric Prince, artifact reward options, and pointer quest or shrine entry points.

## Routing Relevance

The guide specification requires all Daedric quests and artifact-preserving routing for Oblivion Walker. This note supports objective rows for Daedric quest inventory only; detailed choice routing and branch-save treatment remain deferred to conflict and branch passes.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000011 | Skyrim:Daedric Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Daedric_Quests | 2026-05-11 | Lists quest names, Princes, level requirements, rewards, and entry points. |
| SRC-000012 | Skyrim:Artifacts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Artifacts | 2026-05-11 | Defines artifacts and notes Daedric artifact overview. |

## Evidence Summary

UESP lists Daedric quest entries for Azura, Boethiah, Clavicus Vile, Hermaeus Mora, Hircine, Malacath, Mehrunes Dagon, Mephala, Meridia, Molag Bal, Namira, Nocturnal, Peryite, Sanguine, Sheogorath, and Vaermina. The Nocturnal entry is the Thieves Guild arc already represented by Thieves Guild quest rows, so this pass adds a separate artifact-handling row rather than duplicating those quests.

## Confidence and Open Questions

Confidence is high for inventory, level requirements, and reward names. Exact artifact-maximizing choices, alternate branches, NPC survival needs, and quest-specific bugs require later constraint-table research before routing.

## Linked Records

OBJ-000165 through OBJ-000180.
