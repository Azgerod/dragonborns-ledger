# Major Faction Branch Prototypes v0

Status: TB-029 complete.

Scope: compact branch prototypes for the major faction and faction-adjacent choices resolved by TB-028. These are not final guide prose. Each branch records the hard save, alternate-only objective coverage, reload point, and later warning/checklist handoffs.

## Operating Rules

| Rule | Handling |
| --- | --- |
| Branch order | Create the named hard save, play the alternate branch first, verify branch-exclusive content, reload, then continue canonical main continuity. |
| Duplication boundary | Do not repeat objectives that belong to the canonical main route unless the alternate state changes availability, reward, trophy meaning, or warning placement. |
| Placement boundary | TB-029 does not decide exact route-block insertion. TB-032 places warnings and hard-save text; TB-033 validates branch safety. |
| Branch verification | TB-033 should verify objective completion, branch-exclusive reward/state capture, trophy behavior where relevant, reload point, and restoration of canonical continuity. |
| Canonical continuity | Imperial, Dawnguard, Dark Brotherhood join, and Paarthurnax preserved. |

## Branch Prototype Index

| Branch ID | Branch file section | Hard save | Canonical continuity | Alternate branch |
| --- | --- | --- | --- | --- |
| BR-001 | Civil War Stormcloak branch | `HS-CW-BEFORE-FACTION-OATH` | Imperial | Stormcloak Civil War route |
| BR-002 | Volkihar branch | `HS-DG-BLOODLINE` | Dawnguard | Volkihar faction route |
| BR-003 | Destroy the Dark Brotherhood branch | `HS-DB-ABANDONED-SHACK` | Join Dark Brotherhood | Destroy the Dark Brotherhood |
| BR-004 | Paarthurnax compact branch | `HS-MQ-PAARTHURNAX` | Preserve Paarthurnax | Kill Paarthurnax / restore Blades support |

## BR-001 - Civil War Stormcloak Branch

| Field | Prototype |
| --- | --- |
| Hard save | `HS-CW-BEFORE-FACTION-OATH` before irreversible faction oath/commitment. |
| Canonical resume | Reload and continue the Imperial route after the branch audit is complete. |
| Branch goal | Experience and record the Stormcloak-only Civil War sequence without carrying Stormcloak final-state consequences into the main save. |
| Source support | `SN-000097`, `SN-000100`, `SN-000102`. |

Alternate-only objective queue:

| Objective ID | Objective | Branch handling |
| --- | --- | --- |
| `OBJ-000087` | `Joining the Stormcloaks` | Join only on branch save. |
| `OBJ-000088` | `The Jagged Crown (Stormcloaks)` | Branch-only Stormcloak version. |
| `OBJ-000089` | `Message to Whiterun (Stormcloaks)` | Branch-only Stormcloak progression. |
| `OBJ-000090` | `Battle for Whiterun (Stormcloaks)` | Branch-only battle state. |
| `OBJ-000091` | `Liberation of Skyrim` | Branch umbrella for the Stormcloak campaign. |
| `OBJ-000092` | `Rescue from Fort Neugrad` | Branch-only fort objective. |
| `OBJ-000093` | `Compelling Tribute (Stormcloaks)` | Branch-only Stormcloak version. |
| `OBJ-000094` | `The Battle for Fort Sungard (Stormcloaks)` | Branch War Hero-relevant fort candidate. |
| `OBJ-000095` | `A False Front (Stormcloaks)` | Branch-only Stormcloak version. |
| `OBJ-000096` | `The Battle for Fort Snowhawk (Stormcloaks)` | Branch-only fort objective. |
| `OBJ-000097` | `The Battle for Fort Dunstad (Stormcloaks)` | Branch-only fort objective. |
| `OBJ-000098` | `The Battle for Fort Kastav` | Branch-only fort objective. |
| `OBJ-000099` | `The Battle for Fort Greenwall (Stormcloaks)` | Branch War Hero-relevant fort candidate. |
| `OBJ-000100` | `The Battle for Fort Hraggstad` | Branch-only fort objective. |
| `OBJ-000101` | `Battle for Solitude` | Branch `Hero of Skyrim` city-capture endpoint. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| War Hero | Preserve the warning that Season Unending or hold handoffs must not skip the eligible fort battle. TB-032 places the exact warning. |
| Captain Aldis | Complete Aldis-linked favor work before the Stormcloak branch reaches Solitude if final route keeps that favor. |
| Main-route duplicate risk | Do not include Imperial-side objectives in this branch prototype. |
| Reload point | After branch-exclusive Stormcloak campaign audit, reload `HS-CW-BEFORE-FACTION-OATH` and continue Imperial. |

## BR-002 - Volkihar Branch

| Field | Prototype |
| --- | --- |
| Hard save | `HS-DG-BLOODLINE` before Lord Harkon's faction choice. |
| Canonical resume | Reload and refuse Harkon's gift for the Dawnguard main route. |
| Branch goal | Experience Volkihar-only quests, finite rewards, representative radiants, and Vampire Lord/faction services without replacing the Dawnguard final continuity. |
| Source support | `SN-000097`, `SN-000105`, `SN-000114`. |

Alternate-only objective queue:

| Objective ID | Objective | Branch handling |
| --- | --- | --- |
| `OBJ-000356` | `The Bloodstone Chalice` | Volkihar branch quest. |
| `OBJ-000357` | `Prophet (Vampire)` | Volkihar branch version. |
| `OBJ-000374` | `Amulets of Night Power` | Complete once to retrieve both amulets. |
| `OBJ-000375` | `Ancient Power` | Complete successful body-part upgrades to the source-backed branch boundary. |
| `OBJ-000376` | `Culling the Beast` | One representative branch instance. |
| `OBJ-000377` | `Deceiving the Herd` | One representative branch instance. |
| `OBJ-000378` | `Destroying the Dawnguard` | Branch-only finite quest after Volkihar-side finale state. |
| `OBJ-000379` | `The Gift` | Branch-only Volkihar quest. |
| `OBJ-000380` | `The Hunt` | One representative branch instance. |
| `OBJ-000381` | `New Allegiances` | Baseline one successful conversion; TB-031C may escalate to all three named conversions. |
| `OBJ-000382` | `Protecting the Bloodline` | One representative branch instance. |
| `OBJ-000383` | `Rings of Blood Magic` | Complete once to retrieve both rings. |

Branch reward queue:

| Objective ID | Reward / item | Handling |
| --- | --- | --- |
| `OBJ-001716` | `Unique Item: Amulet of Bats` | Branch-only finite reward. |
| `OBJ-001717` | `Unique Item: Amulet of The Gargoyle` | Branch-only finite reward. |
| `OBJ-001736` | `Unique Item: Ring of The Beast` | Branch-only finite reward. |
| `OBJ-001737` | `Unique Item: Ring of the Erudite` | Branch-only finite reward. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| Conversion depth | Prototype one successful `New Allegiances` conversion; mark all-three conversion coverage as TB-031C checklist escalation only. |
| Representative radiants | `Culling the Beast`, `Deceiving the Herd`, `The Hunt`, and `Protecting the Bloodline` stay at one representative branch instance unless TB-031C checklist escalation creates named-variant or all-variant requirements. |
| Spouse-state dependency | `The Gift` requires spouse-state coordination. TB-031C/TB-032 must ensure the branch save has a valid spouse setup or explicitly mark the quest conditional. |
| Transformation planning | Vampire Lord perk-tree work is a wider progression/transformation issue and must not be silently solved inside this branch file. |
| Dawnguard final continuity | Never route `Destroying the Dawnguard` on the canonical Dawnguard save. |
| Reload point | After Volkihar branch-exclusive audit, reload `HS-DG-BLOODLINE` and continue Dawnguard. |

## BR-003 - Destroy the Dark Brotherhood Branch

| Field | Prototype |
| --- | --- |
| Hard save | `HS-DB-ABANDONED-SHACK` before the Abandoned Shack commitment. |
| Canonical resume | Reload and kill a captive to join the Dark Brotherhood. |
| Branch goal | Complete the destroy route and record the mutually exclusive outcome without losing Dark Brotherhood join-route trophies, contracts, sanctuary access, and rewards on the main save. |
| Source support | `SN-000097`, `SN-000100`, `SN-000102`. |

Alternate-only objective queue:

| Objective ID | Objective | Branch handling |
| --- | --- | --- |
| `OBJ-000067` | `Destroy the Dark Brotherhood!` | Kill Astrid and complete the destroy route only on branch save. |

Canonical-only rows to avoid duplicating in the branch:

| Objective IDs | Canonical handling |
| --- | --- |
| `OBJ-000055` through `OBJ-000066`, `OBJ-000068` | Join-route Dark Brotherhood objectives remain on the main save after reload. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| `Delayed Burial` | Complete or intentionally skip according to the main route before either Dark Brotherhood commitment. TB-032 places exact warning text. |
| Falkreath/property risk | Do not let the branch prototype replace the broader Helvard/Lakeview property warning layer. |
| Reload point | After destroy-route audit, reload `HS-DB-ABANDONED-SHACK` and continue the join route. |

## BR-004 - Paarthurnax Compact Branch

| Field | Prototype |
| --- | --- |
| Hard save | `HS-MQ-PAARTHURNAX` before killing Paarthurnax. |
| Canonical resume | Reload and preserve Paarthurnax on the main save. |
| Branch goal | Record the kill-Paarthurnax / Blades support state without losing Greybeards support in canonical continuity. |
| Source support | `SN-000097`, `SN-000112`. |

Branch-impact queue:

| Objective ID | Objective / system | Branch handling |
| --- | --- | --- |
| `OBJ-000019` | `Paarthurnax` | Complete kill outcome only on branch. |
| `OBJ-000317` | `The Words of Power` | Record support-state impact only; do not move main-route word-wall/shout support into the branch unless it is proven Blades-exclusive. |

Warnings and handoffs:

| Topic | TB-029 handling |
| --- | --- |
| Branch size | Keep compact. This is not a second main-quest route. |
| Main-route support | Preserve Greybeards support on the final save. |
| Reload point | After branch-state audit, reload `HS-MQ-PAARTHURNAX` and continue with Paarthurnax alive. |
