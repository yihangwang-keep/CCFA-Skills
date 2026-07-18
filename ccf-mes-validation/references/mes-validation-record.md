# Phase-A Record

Use one append-only record for a Phase-A run. Detailed traceability and review
evidence stays in the two auditor artifacts; this record stores authority,
digests, gate results, repair deltas, and the terminal transition.

```yaml
phase: mes_validation
status: active | document_accepted | environment_accepted | anchor_accepted | no_algorithmic_contribution | blocked | reframe
source_problem_document:
paper_scenario_version:
formal_problem_version:
candidate_epoch:
document_contract:
  research_identity: complete | incomplete
  causal_chain_and_tradeoff: complete | incomplete
  formal_problem: complete | incomplete
  parameter_range: complete | incomplete
  candidate_mes_derivation: complete | incomplete
  information_and_interface: complete | incomplete
  implementation_and_acceptance: complete | incomplete
minimum_executable_scenario_version:
mes_role: candidate | anchor
environment_implementation_version:
environment_l1: not_started | pass | fail | stale
environment_l2:
  scope: anchor_candidate_only
  procedure: not_started | complete | stale
  algorithmic_need: demonstrated | not_demonstrated | insufficient_evidence | stale
algorithm_specification_version:
algorithm_implementation_version:
algorithm_audit: not_started | pass | fail | stale
rounds:
  - failure_id:
    owner: phase_a_environment_implementation | phase_a_problem_contract | phase_a_algorithm_implementation | phase_a_algorithm_design
    single_delta:
    input_artifact_set_id:
    candidate_artifact_set_id:
    invalidated_checks: []
    rerun_evidence: []
    result: repaired | failed | blocked | new_candidate_epoch
terminal_evidence: []
```

`mes_role: anchor` is legal only with `status: anchor_accepted`. A semantic
problem change increments `candidate_epoch`, preserves the failed artifact set,
and returns downstream gates to `stale`; it never overwrites accepted evidence.
