# ccfa.yaml Contract

`ccfa.yaml` is the shared paper-project state file. Version `0.5.0` replaces generic assertion-oriented project state with paper-scenario and supported-conclusion state.

Required top-level fields:

- `version`
- `project`
- `target_venue`
- `stage`
- `artifacts`
- `paper_conclusions`
- `experiments`
- `reviews`
- `revision_ledger`
- `submission_checks`

Only `ccf-project-scaffolder` should create it by default. `ccf-pipeline-orchestrator` may update stage and gate state. Other skills may read it and propose updates unless the user explicitly grants write permission.

## Version 0.4 Compatibility

The authoritative migration policy is machine-readable so validation does not depend on prose wording:

```json
{
  "migration": {
    "source_versions": ["0.4.x"],
    "target_version": "0.5.0",
    "legacy_field": "claims",
    "canonical_field": "paper_conclusions",
    "read_mode": "read_only_alias",
    "authorized_copy": "verbatim",
    "dual_field_merge": "stable_id",
    "same_id_same_content": "retain_once",
    "same_id_different_content": "report_conflict",
    "unkeyed_entries": "preserve_source_order",
    "remove_legacy": "after_validated_write",
    "unauthorized_write": "leave_unchanged_and_report"
  }
}
```

Readers apply the alias before treating conclusion state as absent. During an authorized migration, merge dual fields by stable ID, stop on conflicting content, preserve unkeyed entries in source order, and remove the legacy field only after the new document validates. Without authorization, use the alias for reading, leave the file unchanged, and report the migration requirement.

These compatibility rules do not authorize any skill to rewrite project state. A version update and a field rename are one explicit migration operation, not an incidental read-time cleanup.

For scenario-driven algorithm projects, register the versioned artifact roots under `artifacts.environment_design`, `artifacts.environment_audit`, `artifacts.algorithm_design`, `artifacts.algorithm_audit`, and `artifacts.experiment_debug`. Store paper-scenario, formal-problem, parameter-range, MES, implementation-revision, validation-contract, and evidence-epoch identities in the owning artifacts; keep only current pointers in project state when needed. Scenario-evolution records live below `artifacts.environment_design`, normally at `scenario-evolution/`. Detailed gate evidence, artifact manifests, native implementation reviews, and design-validation loop ledgers stay out of `ccfa.yaml`.

Artifact-local fields use `minimum_executable_scenario` and `minimum_executable_scenario_version`. Readers may interpret `scenario_mvp` and `scenario_mvp_version` as read-only aliases. A writer must not emit the legacy fields, and conflicting canonical and legacy values require an explicit migration decision.

Optional monitoring fields:

- `literature_monitor`
- `tracked_competitors`
- `watch_queries`
- `last_monitoring_report`

`ccf-literature-monitor` may propose updates to these fields after a watch run. It must not silently overwrite project state unless the user explicitly asks it to persist the monitoring summary.
