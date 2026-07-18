# Phase-B Record

Use one append-only record for each user-approved complexity upgrade. A Phase-B
record points to the frozen anchor and stores a stage document and `stage_case`;
it never stores a candidate, successor, or replacement MES.

```yaml
phase: complexity_upgrade
status: active | document_accepted | environment_accepted | stage_accepted | algorithm_failed | upgrade_unsupported | blocked | reframe
stage_request_id:
upgrade_document:
upgrade_document_version:
parent_phase_a_record:
parent_formal_problem_version:
anchor_mes_version:
anchor_artifact_set_id:
base_algorithm_specification_version:
base_algorithm_implementation_version:
complexity_stage_id:
parent_complexity_stage_id:
method_independent_delta:
stage_problem_version:
stage_case_id:
stage_contract:
  inherited_semantics: []
  added_complexity: []
  forbidden_changes: []
  algorithm_visible_fields: []
  audit_only_fields: []
  environment_deliverables: []
  acceptance_gates: []
environment_implementation_version:
environment_consistency: not_started | pass | fail | stale
stage_execution: not_started | pass | fail | stale
anchor_regression: not_started | pass | fail | stale
inherited_algorithmic_need: demonstrated | not_demonstrated | insufficient_evidence | stale
algorithm_freeze: frozen_until_environment_pass | released
algorithm_specification_version:
algorithm_implementation_version:
algorithm_audit: not_started | pass | fail | stale
algorithm_anchor_regression: not_started | pass | fail | stale
rounds:
  - failure_id:
    owner: phase_b_stage_document | phase_b_environment_implementation | phase_b_algorithm_implementation | phase_b_algorithm_design
    single_delta:
    input_artifact_set_id:
    candidate_artifact_set_id:
    invalidated_checks: []
    rerun_evidence: []
    result: repaired | failed | blocked | new_stage_document_version
terminal_evidence: []
```

The only MES field is the immutable `anchor_mes_version` pointer inherited from
Phase A. A document or algorithm failure never changes that pointer.
