# Phase-B Record

Keep one readable, append-only record for the upgrade. It describes the work
in order; it does not encode a large phase state machine.

```yaml
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
algorithm:
  version:
  changed_files: []
failures:
  - audit: environment | algorithm
    location:
    reason:
notes: []
```

Keep the parent scenario version as the starting-point reference. For a failed
environment or algorithm check, record only its location and reason in
`failures`. If the research question itself changes, record the reason and start
a separate scenario document instead of mutating this record.
