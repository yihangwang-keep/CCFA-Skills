# Phase-A Record

Keep one short, append-only record. It is a readable handoff, not a state
machine. Detailed traceability and execution evidence belong to the two audit
reports.

```yaml
phase: A
status: in_progress | accepted | blocked
problem_document:
  path:
  version:
minimum_executable_scenario_version:
mes_role: candidate | anchor
environment:
  version:
  entry_point:
environment_audit:
  status: pending | pass | needs_repair
  report_ref:
  reviewed_document_version:
  reviewed_mes_version:
  reviewed_environment_version:
algorithm:
  specification_version:
  implementation_version:
  entry_point:
algorithm_audit:
  status: pending | pass | needs_repair
  report_ref:
  reviewed_document_version:
  reviewed_mes_version:
  reviewed_environment_version:
  reviewed_algorithm_version:
rounds:
  - finding:
    changed:
    rerun:
    result:
notes: []
```

When a problem-semantic revision is needed, write a new document version and
explain why the old result no longer applies. Keep the old result; do not
overwrite it. Mark `mes_role: anchor` only after the environment and initial
algorithm audits both pass and their reviewed-version fields match the current
document, MES, environment, and algorithm.
