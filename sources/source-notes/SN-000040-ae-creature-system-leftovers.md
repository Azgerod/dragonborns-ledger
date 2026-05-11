# Source Note: AE Creature System Leftovers

Status: needs review.

Source note ID: SN-000040

## Claim

Plague of the Dead adds a zombie creature system that is not simply a pet, mount, follower, or unique reward row. It needs source-list coverage for later warning, Survival Mode, and Legendary-difficulty validation.

## Routing Relevance

The project includes official AE systems, but excludes arbitrary random encounter variants. A narrow system row lets later constraint passes account for zombie night/world interactions, quest interaction, Mort Flesh, spell-tome linkage, and difficulty implications without forcing the final guide to route infinite or arbitrary zombie encounters.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000099 | Skyrim:Plague of the Dead | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Plague_of_the_Dead | 2026-05-11 | Plague of the Dead Creation overview, zombie creature type, level-5 quest start, night/world interaction context, spell tomes, and Mort Flesh. |
| SRC-000100 | Skyrim:Zombie | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Zombie | 2026-05-11 | Plague of the Dead zombie variants and creature behavior. |
| SN-000035 | AE Bundle Membership and Parent Creation Inventory | Local source note | sources/source-notes/SN-000035-ae-bundle-membership-and-parent-inventory.md | 2026-05-11 | Parent package row for Plague of the Dead. |

## Evidence Summary

UESP describes Plague of the Dead as adding a new zombie creature type, a quest, night/world-interaction appearances, Mort Flesh, and zombie-related spell tomes. Because the source describes world interactions and creature variants rather than a bounded finite set of individual completion targets, this pass records a system row rather than requiring every possible zombie encounter.

## Confidence and Open Questions

Confidence is high that Plague of the Dead needs system coverage. Exact zombie-spawn warnings, night-travel implications, level-gate handling, quest timing, and whether Mort Flesh or zombie spell tomes become separate item/spell rows remain deferred to AE start-trigger, Survival Mode, item, and spell passes.

## Linked Records

OBJ-000692.
