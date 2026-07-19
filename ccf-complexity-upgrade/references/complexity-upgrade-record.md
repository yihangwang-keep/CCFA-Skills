# Phase-B Record

Keep one readable, append-only record for the upgrade. It describes the work
in order; it does not encode a large phase state machine.

```yaml
status: in_progress | accepted | blocked
parent:
  scenario_document:
  scenario_version:
  environment_version:
  algorithm_version:
upgrade_document:
  path:
  version:
  motivation:
environment:
  version:
  changed_files: []
environment_audit:
  status: pending | pass | needs_repair
  report_ref:
  reviewed_upgrade_document_version:
  reviewed_environment_version:
algorithm:
  version:
  changed_files: []
algorithm_audit:
  status: pending | pass | needs_repair
  report_ref:
  reviewed_upgrade_document_version:
  reviewed_environment_version:
  reviewed_algorithm_version:
rounds:
  - finding:
    owner: environment | algorithm
    changed:
    rerun:
    result:
notes: []
```

Keep the parent scenario version as the starting-point reference. If the
research question itself changes, record the reason and start a separate
scenario document instead of mutating this record. Mark the upgrade `accepted`
only when both audit reports reference the current upgrade document,
environment, and algorithm versions.
