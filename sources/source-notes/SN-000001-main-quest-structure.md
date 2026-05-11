# Main Quest Structure

Status: needs review.

Source note ID: SN-000001

## Claim

The base-game Skyrim main quest is a defined main-quest sequence with seventeen required quests and two optional quests. The required sequence begins with `Unbound` and ends with `Dragonslayer`; the optional quests listed with the sequence are `Season Unending` and `Paarthurnax`.

## Routing Relevance

The objective database needs a first pass of main-quest rows before route construction. These rows establish the required main-quest objective inventory and flag the two optional main-quest entries for later Civil War and Paarthurnax/Blades conflict handling.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000001 | Skyrim:Main Quest | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Main_Quest | 2026-05-11 | Used for the main-quest count, required/optional distinction, and ordered quest names. |

## Evidence Summary

UESP's main quest page identifies the questline as having seventeen required quests and two optional quests. It presents the ordered list of required quests from `Unbound` through `Dragonslayer` and nests `Season Unending` and `Paarthurnax` as optional entries during the late main-quest sequence.

## Confidence and Open Questions

Confidence is high for the existence and order of the main-quest rows. This note does not resolve route timing, Civil War interactions, Season Unending handling, Paarthurnax branch handling, bug risks, Survival Mode routing, or quest-specific start/completion mechanics.

## Linked Records

Objective IDs `OBJ-000001` through `OBJ-000019`.
