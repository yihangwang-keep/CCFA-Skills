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

For scenario-driven algorithm projects, register versioned artifact roots under `artifacts.phase_a`, `artifacts.phase_b`, `artifacts.environment_audit`, and `artifacts.algorithm_audit`. Phase A owns the problem document, MES/environment, initial algorithm, repair rounds, and accepted anchor. Phase B owns each upgrade scenario document, direct revisions to the existing environment and algorithm, audits, and repair rounds. Store only current pointers in project state; detailed contracts, digests, failures, gate evidence, and native reviews stay in their owning artifacts rather than `ccfa.yaml`.

Phase-A artifact fields use `minimum_executable_scenario`, `minimum_executable_scenario_version`, and `mes_role`. Readers may interpret `scenario_mvp` and `scenario_mvp_version` as read-only aliases, but writers do not emit them. Phase-B artifacts keep the parent scenario document/version pointer and add an `upgrade_document` version plus environment/algorithm revision pointers.

Optional monitoring fields:

- `literature_monitor`
- `tracked_competitors`
- `watch_queries`
- `last_monitoring_report`

`ccf-literature-monitor` may propose updates to these fields after a watch run. It must not silently overwrite project state unless the user explicitly asks it to persist the monitoring summary.
