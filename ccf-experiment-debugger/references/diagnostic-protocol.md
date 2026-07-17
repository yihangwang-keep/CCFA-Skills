# Auditor-Centered Failure Protocol

Use this protocol after an environment, MES, or algorithm-MVP run fails, diverges, becomes unstable, cannot be reproduced, or misses a declared criterion. Keep the full working record internal unless the user requests it.

## Failure Record

```yaml
failure_id:
expected_criterion:
observed_result:
first_divergence:
run_command:
configuration_and_seeds:
validation_contract_version:
paper_scenario_version:
formal_problem_version:
minimum_executable_scenario_version:
environment_implementation_revision:
algorithm_specification_version:
algorithm_implementation_revision:
algorithm_repair_exhaustion:
  route_id:
  algorithm_specification_version:
  exhaustion_scope: mechanism | family | credible_routes
  status: not_started | active | exhausted | superseded | closed | not_applicable
  state_history: []
  repair_refs: []
  proposed_failure_classification: algorithm_specific | model_defect | unresolved
  next_route_id:
environment_review:
  route_id:
  status: not_started | active | completed | blocked
  confirmed_classification: algorithm_specific | model_defect | unresolved
  decision: return_to_algorithm | authorize_evolution | blocked
  decision_owner: ccf-env-design
  evidence_ref:
target_evidence_if_applicable:
  target_scope: environment_l2 | formal_problem | algorithm_guarantee
  target_definition_ref:
  target_definition_owner: ccf-env-design | ccf-algorithm-designer
  evidence_items:
    - evidence_ref:
      evidence_status: current | stale | invalid | not_applicable
      evidence_owner: ccf-env-design | ccf-env-code-auditor | ccf-algorithm-designer | ccf-algorithm-code-auditor
input_artifact_set_id:
artifact_manifest: []
preserved_logs_traces_outputs: []
```

An artifact manifest records repo-relative path, role, and content digest for authority, specification, implementation, configuration, test, checker, and raw evidence files. Bind the exhaustion, target evidence, and environment review to the same route ID. Append repaired runs and route-state events; never overwrite the original failure or reuse one route's review for another route.

## Evidence Layers

| Layer | Current evidence | Decisive status | Owner |
| --- | --- | --- | --- |
| Environment L1 | design contract, code traceability, semantics, independent MES execution, current native review | pass / conditional / fail / stale / missing | `ccf-env-code-auditor` |
| Environment L2 | frozen MES, predeclared joint target, representative probes, tuning ranges and budget parity | demonstrated / not_demonstrated / contradicted / insufficient_evidence / stale | `ccf-env-code-auditor`; design target from `ccf-env-design` |
| Algorithm design | formal target, family, role, component classification, mechanism, verification plan | implementation-ready / provisional / stale / contradicted | `ccf-algorithm-designer` |
| Algorithm implementation | traceability, semantics, no-heuristic check for `proposed`, reference and MES evidence, current native review | pass / conditional / fail / stale / missing | `ccf-algorithm-code-auditor` |
| Validation contract | locked cases, probes or baselines, metrics, checker, tolerances, status, resource accounting, pass criteria | accepted / stale / contradicted / missing | criterion's design owner; auditor verifies |

Refresh the earliest missing, stale, failed, or contradicted dependency. One layer's pass cannot offset another layer's failure.

## Minimal-Change Routing

| Confirmed cause | One owning action | Required refresh |
| --- | --- | --- |
| Environment code contradicts accepted design or MES | repair the smallest environment implementation path | affected L1 checks, native review, and downstream behavior that consumes the delta |
| Environment L1 passes but tuned probes meet the joint target | record `algorithmic_need: not_demonstrated` or `contradicted` | no environment repair; stop the affected algorithm-contribution route |
| Probe evidence lacks tuning, parity, or a predeclared target | repair the L2 validation evidence without changing the MES | affected probe runs and L2 decision |
| Algorithm code contradicts its accepted specification or hides a heuristic fallback | repair the smallest algorithm path | affected algorithm checks, no-heuristic classification, native review, and downstream evidence |
| Algorithm code matches its specification but mechanism misses the target | revise one mechanism in algorithm design | implementation traceability, full algorithm audit, MES evidence, and review |
| Faithful algorithm code and documented mechanism/family revisions still cannot pass | create a route-specific exhaustion record and open environment/formal-model review | preserve all failed revisions; algorithm proposes, environment owner confirms classification |
| Exhaustion review confirms a scenario or formal-model defect | submit one non-simplifying classified evolution proposal to environment design | successor environment audit and all evidence invalidated by the change class |
| Environment review confirms `algorithm_specific` | close or supersede the exhausted route | open a fresh route ID if credible routes remain; otherwise evaluate `no-algorithmic-contribution` |
| Exhaustion review is unresolved or only proposes an easier problem | keep the environment unchanged and record a blocker | missing evidence, alternative algorithm route, or reframe decision needed |
| Locked validation measurement/checker is independently inconsistent with accepted semantics | submit a non-simplifying versioned correction to its design owner | preserve the old failure, rerun affected evidence, and do not accept retroactively |
| Proposed validation change lowers cases, target, feasibility, tolerance, solver status, or resource requirement | reject it as a repair | blocked or research reframe; current contribution evidence cannot transfer |

Before changing the environment, close L1 and algorithm-code fidelity and preserve the route-specific algorithm-design repair ledger. Exhaustion always opens environment review. Test another credible solver, reference, bound, or adequately tuned heuristic when available; otherwise inspect authoritative-problem infeasibility, invalid environment-target evidence, information mismatch, causal incompleteness, or ill-posed modeling. An unattainable algorithm guarantee remains algorithm-side. Never alter environment parameters, remove hard cases, relax targets/constraints, or expose unavailable information to make either a heuristic or proposed algorithm pass.

## One-Delta Record

```yaml
round:
confirmed_cause_and_evidence:
owner:
single_changed_item:
round_input_artifact_set_id:
candidate_artifact_set_id:
changed_paths: []
validation_contract_version:
checks_marked_stale: []
rerun_commands_and_seeds: []
domain_audit_result:
native_review_id:
review_axis_status:
outcome:
```

Do not combine an environment-authority change and an algorithm change in one round. Content changes create a new candidate artifact set and make reviews of the previous digest stale.

## Invalidation

- Environment implementation repair: invalidate affected L1 execution and every algorithm check whose input, transition, objective, constraint, or residual can change.
- Algorithm implementation repair: invalidate affected traceability, semantics, role classification, reference, runtime, reproducibility, and MES checks.
- Algorithm specification change: invalidate mapped code, algorithm audit, relevant MES evidence, comparisons, and results.
- Evidence expansion under the same authority: invalidate no old authority; run all relevant methods fairly on the new settings.
- MES successor: preserve evidence for the parent; invalidate successor acceptance and affected downstream evidence until compatibility anchors and new cases rerun.
- Formal amendment: create a new evidence epoch and rebaseline environment, algorithms, baselines, and results.
- Research reframe: close the current lineage; do not transfer acceptance to the new research object.
- Validation implementation repair with unchanged semantics: rerun every affected result under the same validation-contract version.
- Material validation-semantics change: create a new validation-contract version only after an independent non-simplification check; preserve the old outcome. A change that lowers cases, target, feasibility, tolerance, solver status, or resource requirements is not a repair and cannot inherit current contribution evidence.

## Closure

Close a repair only when the original failure is reproduced or characterized; one owner and delta are recorded; the original case and every invalidated check have current evidence; applicable environment L1/L2 and algorithm gates hold; and fresh native review reports bind both axes to the candidate artifact-set digest. If fresh reviewers or digest binding are unavailable, record `insufficient_evidence`; do not substitute coordinator self-review.

Dropping the failure, choosing favorable seeds, widening tolerances, weakening feasibility or resource rules, exposing future information, or silently replacing the MES is not closure.
