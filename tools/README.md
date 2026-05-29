# tools

Validation and maintenance scripts live here.

Prefer small tools that support coverage checks, checklist mapping, source-note consistency, or other repeatable QA tasks.

Current tools:

| Tool | Purpose |
| --- | --- |
| `validate_all.py` | Runs all lightweight repository validators. |
| `validate_objectives.py` | Basic objective CSV header validation. |
| `validate_coverage.py` | Basic coverage-matrix structure validation. |
| `validate_sources.py` | Basic source workflow structure validation. |
| `validate_books.py` | Book/document location table structural validation. |
| `validate_npc_options.py` | Relationship, household role, follower, pet, and mount option table structural validation. |
| `validate_items.py` | AE item-member table structural validation. |
| `validate_properties.py` | Property detail table structural validation. |
| `validate_locations.py` | Location catalog structural validation. |
| `validate_location_coordinates.py` | Location coordinate support table structural validation. |
| `validate_location_geography.py` | Hub/corridor geography support table structural validation. |
| `build_route_planning_index.py` | Generates route-planning objective and constraint indexes from source CSVs and Markdown constraint tables. |
| `build_route_planning_database.py` | Builds an ignored local SQLite workbench from the project CSVs. |
| `validate_route_planning.py` | Route-planning index structural validation. |
| `validate_skills.py` | Skill/perk and individual perk-rank support table structural validation. |
| `validate_enchantments.py` | Enchantment-learning support table structural validation. |
| `validate_alchemy.py` | Alchemy ingredient-effect support table structural validation. |
| `validate_merchants.py` | Merchant investment support table structural validation. |
| `validate_crafting_systems.py` | Practical crafting-system support table structural validation. |
| `audit_main_guide_objective_ids.py` | Generates the TB-035-COV-001 objective representation audit for `main-guide-v1.md`. |
| `audit_main_guide_checklist_ids.py` | Generates the TB-035-COV-002 checklist representation audit for `main-guide-v1.md`. |
| `audit_main_guide_branch_coverage.py` | Generates the TB-035-COV-003 branch checklist/objective audit for `main-guide-v1.md`. |
| `audit_main_guide_option_defaults.py` | Generates the TB-035-COV-004 option/default audit for `main-guide-v1.md`. |
| `audit_main_guide_exclusions.py` | Generates the TB-035-COV-005 explicit-exclusion audit for `main-guide-v1.md`. |
| `audit_main_guide_appendix_rows.py` | Generates the TB-035-COV-006 appendix-only checklist audit for `main-guide-v1.md`. |
| `audit_main_guide_locations.py` | Generates the TB-035-COV-007 location objective/checklist audit for `main-guide-v1.md`. |
| `audit_main_guide_books_documents.py` | Generates the TB-035-COV-008 book/document objective and checklist audit for `main-guide-v1.md`. |
| `audit_main_guide_collectibles.py` | Generates the TB-035-COV-009 finite collectible objective/checklist audit for `main-guide-v1.md`. |
| `audit_main_guide_crafting_progression.py` | Generates the TB-035-COV-010 crafting/progression objective, checklist, and support-row audit for `main-guide-v1.md`. |
| `audit_main_guide_radiant_counters.py` | Generates the TB-035-COV-011 radiant/counter objective and checklist audit for `main-guide-v1.md`. |
| `check_main_guide_placeholders.py` | Checks `main-guide-v1.md` for TB-035-COV-012 banned placeholder phrases. |
| `summarize_main_guide_coverage.py` | Generates the TB-035-COV-013 final coverage summary and per-objective final-status table for `main-guide-v1.md`. |
| `build_appendices_v0.py` | Generates the TB-036 `drafts/final-guide/appendices-v0.md` reference draft from guide and coverage artifacts. |
| `build_coverage_qa_checklist.py` | Generates the Phase 15 `drafts/final-guide/qa-checklist.md` from guide, appendix, coverage, checklist, COV audit, order/delayed-task, focused constraint QA, simulated-playtest, and final-risk artifacts. |
| `audit_main_guide_order_delayed_tasks.py` | Generates the TB-038 order/delayed-task QA audit and summary CSVs for `main-guide-v1.md`. |
| `repair_main_guide_order_delayed_tasks.py` | Generates the TB-038R delayed-task repair/classification register, appends TB-038R coverage rows, and refreshes the guide's explicit route-resolution block. |
| `audit_main_guide_trophy_leveled_cell.py` | Generates the TB-039 trophy, leveled-item, and cell-entry QA audit and summary CSVs for `main-guide-v1.md`. |
| `audit_main_guide_survival_legendary.py` | Generates the TB-040 Survival Mode and Legendary difficulty QA audit and summary CSVs for `main-guide-v1.md`. |
| `audit_main_guide_branch_spoilers.py` | Generates the TB-041 branch handling and spoiler discipline QA audit and summary CSVs for `main-guide-v1.md`. |
| `audit_main_guide_playtest.py` | Generates the TB-042 simulated playtest audit, summary CSVs, and playtest notes for `main-guide-v1.md`. |
| `build_unresolved_risk_report.py` | Generates the TB-043 unresolved-risk report, row-level risk register, and summary CSVs for `main-guide-v1.md`. |
| `fetch_uesp.py` | Fetches UESP pages through the MediaWiki API with a browser User-Agent for source-note research. |
