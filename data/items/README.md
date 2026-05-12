# Item Data

Status: in progress.

Item member and acquisition tables live here when a parent objective row is too broad for route placement or checklist validation.

Use this directory for source-backed member inventories such as AE equipment sets, ingredients, materials, consumables, crafting outputs, practical equipment, pet/mount equipment, and unique or named reward members.

The objective database remains authoritative for routed completion units. Tables in this directory should preserve member-level acquisition, crafting, preservation, and checklist details that would make `objectives.csv` too wide or repetitive.

Do not use this directory for final guide prose.

## Row Policy

Use one row per source-listed member when a parent objective row represents a finite item set, equipment set, crafting set, consumable set, or utility system.

Do not duplicate objective rows merely because a set has many mundane craftable or purchasable members. Use `existing_objective_id` only when a member is already represented elsewhere as a routed/checklist objective, such as a spell tome in `data/books/`.

`route_treatment` values currently used:

* `source_listed_member`: member should remain available for route/checklist consideration.
* `already_tracked_in_spell_tome_table`: member is cross-linked to the existing spell-tome objective and acquisition table.
* `crafting_system_cross_reference`: member identifies a craftable/station-linked system rather than a separate pickup objective.
* `excluded_template_or_internal`: source-listed row appears to be a template/internal item rather than a normal completion target.
* `excluded_unobtainable`: source marks the member as unobtainable; keep it visible for audit but do not route it.

## Files

* `item-members.template.csv` defines the shared header for item-member tables.
* `ae-item-members.csv` records source-listed members for TB-007G1 AE magic, ingredient, consumable, crafting, and practical-equipment parent sets and TB-007G2 AE Alternative Armor and unique-equipment parent sets.
* `ae-item-member-reconciliation.md` summarizes current AE item-member coverage and downstream validation boundaries.
