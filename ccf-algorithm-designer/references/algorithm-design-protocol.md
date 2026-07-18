# Algorithm Design Protocol

Use this protocol after the paper scenario and its minimum executable scenario (MES) pass environment audit and the anchor-only heuristic-probe evidence establishes the intended initial algorithmic need. If either record is incomplete, use it only to produce a provisional design. A later complexity stage inherits the anchor result and enters algorithm repair/upgrade; it does not rerun the heuristic-probe need test.

The environment authorizes the formal problem in one direction. The algorithm consumes that problem; it does not rewrite the scientific question, objective, decision variables, constraints, information pattern, feasibility meaning, task-causal semantics, paper parameter range, or MES.

## Contents

- Input authority and design state
- Formal target and algorithm-family decision
- Derived mechanism and environment-information boundary
- Method role, algorithm MVP, verification, evidence, and revision records

## Input Authority

```text
Paper scenario and formal problem:
Paper parameter range:
Minimum executable scenario and lineage:
Anchor MES freeze epoch and current complexity stage:
Environment specification and code version:
Objective, decision variables, constraints, and information pattern:
Feasibility meaning and task-causal semantics:
Environment acceptance evidence:
Unresolved assumptions:
```

The MES is the smallest causally complete, executable, independently checkable scenario package for the current paper-scenario and formal-problem version. It can include multiple registered cases needed to activate the central tradeoff. A simpler replacement problem is not an MES, and an accepted anchor MES is not edited in place. Later scale, load, topology, uncertainty, coupling, and boundary stages are run against this anchor under the same formal problem and interface; they are complexity evidence, not MES successors.

## Design State

- `provisional`: at least one authority, interface, assumption, or acceptance item that can change the mechanism remains unresolved.
- `implementation-ready`: the accepted environment version is pinned, every applicable design gate is closed, the environment interface is sufficient, and each implementation step has an executable acceptance check.

Record the state in the algorithm artifact. A later environment version never inherits the earlier implementation-ready status.

## Formal Target And Problem Structure

```text
Decision variables and domains:
Objective and solution target:
Constraints and feasibility semantics:
Information timing and observability:
Online/offline and deterministic/stochastic structure:
Convex, nonconvex, combinatorial, or decomposable structure:
Dynamics and uncertainty:
Scale and computational budget:
Required correctness, convergence, approximation, regret, or optimality evidence:
```

Complete this analysis before selecting an algorithm family.

## Algorithm-Family Decision

For each credible family, record:

```text
Candidate family:
Matching problem structure:
Required assumptions:
Solution target or guarantee:
Feasibility handling:
Information and compute requirements:
Decision: select / reject / unresolved
```

Select the least complex family that addresses the accepted formulation and evidence target.

For initial anchor design, include exact or enumerated solutions, certified bounds, and the tuned heuristic probes already used by environment audit. A proposed mechanism is justified only when the accepted problem and matched decision budget expose a limitation that those alternatives cannot resolve. For a complexity-stage upgrade, consume the fixed anchor result and compare the upgraded algorithm against the stage reference and anchor regression; do not create a new heuristic-probe need test.

## Method Role And No-Heuristic Gate

Classify the method before accepting its mechanism:

```yaml
method_role: proposed | environment_probe | baseline | reference | diagnostic
mechanism_classification:
  components: []
  contains_heuristic_decision: true | false | unknown
  classification_basis: []
heuristic_components: []
no_heuristic_gate: required | not_applicable | unresolved
no_heuristic_gate_status: pass | blocker | unresolved | stale | not_applicable
```

For `method_role: proposed`, set the gate to `required`; `no_heuristic_gate_status: pass` requires every decision component to be non-heuristic and traceable to the formal target, a valid solution procedure, or an accepted analytical result. Any greedy rule, rule-of-thumb, manually patched branch, heuristic local search, metaheuristic, empirical trial-and-error decision, rule accumulation, or hidden heuristic fallback sets `blocker`. A proof, certificate, exact subroutine, or formal wrapper elsewhere does not offset it. Non-proposed roles use `not_applicable`; unknown classification remains `unresolved`. The code auditor recomputes the status against implementation. Do not relabel the method to avoid this gate.

The environment's anchor-only heuristic-probe result establishes whether tuned simple rules meet the predeclared joint target on the initial MES. It does not certify the proposed method, and it cannot replace this component-level gate. The result is inherited, not recomputed, for later complexity stages.

## Derived Mechanism And Evaluation Semantics

For every mechanism, record its source in the formulation. For any computational replacement of the original problem, record:

```text
Original objective and constraints:
Surrogate, relaxation, penalty, decomposition, or bound:
Purpose and required assumptions:
Direction and scope of the bound, if any:
Recovery or projection into the original feasible set:
Independent residual check on the original constraints:
Final evaluation under the original objective:
Failure behavior without hidden fallback:
```

An internal objective or relaxed feasible set does not replace the environment contract. Report final decisions, feasibility, and objective values using the accepted environment semantics.

## Environment Information And Amendment Boundary

For every requested input or diagnostic, state its meaning, unit, time index, and availability time. Separate:

- algorithm-visible information authorized by the formal information pattern;
- audit-only information such as actual future realizations, exact decisions, hidden state, or checker-only statistics.

If an authorized mathematical quantity is missing only from the code interface, request an interface change and require environment-code audit. If the request would change the formal problem or expose information unavailable at decision time, do not implement it. After route-specific algorithm repair is exhausted, submit this Environment/Formal-Model Review Request to the environment owner:

```yaml
observed_failure:
authority_versions:
algorithm_repair_exhaustion:
  route_id:
  algorithm_specification_version:
  exhaustion_scope: mechanism / family / credible_routes
  status: exhausted
  repair_refs: []
  credible_methods_and_references_checked: []
  proposed_failure_classification: algorithm_specific / model_defect / unresolved
environment_l1_and_algorithm_code_fidelity_evidence:
independent_evidence:
unchanged_failures_and_reference_evidence:
why_algorithm_only_repair_is_insufficient:
target_evidence_if_applicable:
  target_scope: environment_l2 / formal_problem / algorithm_guarantee
  target_definition_ref:
  target_definition_owner: ccf-env-design / ccf-algorithm-designer
  evidence_items:
    - evidence_ref:
      evidence_status: current / stale / invalid / not_applicable
      evidence_owner: ccf-env-design / ccf-env-code-auditor / ccf-algorithm-designer / ccf-algorithm-code-auditor
proposed_model_defect_evidence:
proposed_change_if_any:
objective_and_feasible_set_impact:
information_pattern_impact:
scientific_problem_and_task_semantics_preserved:
method_neutrality:
proposed_non_simplification_evidence:
  preserved_material_invariants: []
  unjustified_removed_or_weakened_items: []
  corrected_model_items_and_independent_evidence: []
  predecessor_regression_anchors: []
  objective_weighting_or_priority_impact:
  target_impact:
  tolerance_impact:
  feasibility_rule_impact:
  solver_status_impact:
  time_or_resource_budget_impact:
  seed_selection_impact:
  case_sampling_distribution_impact:
  cross_case_aggregation_impact:
  horizon_or_termination_impact:
  exogenous_resource_or_capability_impact:
  preserved_causal_difficulty_and_tradeoff:
invalidated_artifacts:
required_reruns:
environment_review:
  route_id:
  status: not_started
  confirmed_classification:
  decision:
  decision_owner: ccf-env-design
  evidence_ref:
```

The algorithm designer cannot classify or approve the environment change. All
`proposed_*` fields are non-authoritative evidence for environment review; the
environment owner recomputes classification, change necessity, and the final
non-simplification status. A timeout or weak result from one mechanism is not
exhaustion. Once the bound route/scope is exhausted, the review is mandatory
even when model-side evidence is incomplete. Another credible method/reference
should be included when available; formal evidence may indicate an
infeasible/ill-posed authoritative problem, invalidated environment-target
witness, information mismatch, or missing causal semantics. An unattainable
algorithm guarantee remains algorithm-owned. Only a completed environment
review with `confirmed_classification: model_defect` and `decision:
authorize_evolution` may produce a classified evolution proposal.
`algorithm_specific` returns a completed route to algorithm ownership when
credible routes remain; `unresolved` is blocked. Any formal-amendment successor
must pass the environment owner's non-simplification contract and restart
algorithm design at the authority gate. A complexity stage does not restart
authority or create a new MES; it reopens algorithm repair while retaining the
anchor regression.

## Algorithm MVP Contract

```yaml
algorithm_name:
algorithm_version:
authoritative_problem_version:
environment_version:
environment_interface_version:
minimum_executable_scenario_version:
parent_mes_version:
mes_role: anchor | candidate | legacy_successor
mes_freeze_epoch:
complexity_stage_id:
parent_complexity_stage_id:
design_state: provisional | implementation-ready
method_role: proposed | environment_probe | baseline | reference | diagnostic
mechanism_classification:
  components: []
  contains_heuristic_decision: true | false | unknown
  classification_basis: []
heuristic_components: []
no_heuristic_gate: required | not_applicable | unresolved
no_heuristic_gate_status: pass | blocker | unresolved | stale | not_applicable
solution_target:
assumptions:
inputs_and_information_timing:
decision_outputs:
initialization:
algorithm_mechanism:
update_or_search_steps:
feasibility_handling:
termination:
randomness_and_seed_control:
complexity_target:
environment_information_needed:
original_objective_evaluation:
original_constraint_checks:
acceptance_criteria:
```

The algorithm MVP is the first complete path through the real environment interface on the frozen anchor MES. Unit-sized cases may verify individual equations, while end-to-end acceptance uses the complete anchor. For each complexity stage, run the anchor regression and the new stage with the same information, feasibility, stopping, and resource rules; a stage failure is routed to algorithm repair before any environment review.

## Verification Sequence

| Step | Implemented scope | Required check | Pass condition | Owner |
| --- | --- | --- | --- | --- |
| 1 | Mathematical reference | hand-computable case or exact/oracle/bound | expected decision, objective, and residuals match tolerance | algorithm design |
| 2 | Environment interface | shape, unit, timing, mask, information checks | interface matches the formal information pattern | environment code |
| 3 | Feasibility path | independent original-constraint residuals and invariants | returned decisions satisfy declared constraints | algorithm code |
| 4 | Update/search step | equation-to-code comparison | implementation matches the derivation | algorithm code |
| 5 | Initial anchor algorithm MVP end to end | termination, original objective, reproducibility, anchor L2 comparison, complexity | anchor MES meets predeclared acceptance criteria and the proposed-method no-heuristic gate passes | independent algorithm audit |
| 6 | Complexity-stage algorithm upgrade | stage objective/constraints, anchor regression, reproducibility, reference comparison, complexity | requested stage and anchor regression meet the current algorithm acceptance criteria; no new L2 probe sweep is introduced | independent algorithm audit |

## Working Evidence Record

Keep family tables, gate results, evidence locations, and rerun dependencies in the working record. The default user-facing artifact contains the selected mechanism, decisive evidence, current design state, unresolved items, and implementation contract; include full tables only when requested.

## Revision Record

```text
Observed evidence:
Diagnosed owner:
Changed assumption, mechanism, interface, or MES item:
Reason for the change:
Artifact versions updated:
Verification checks to rerun:
Outcome:
```

A completed revision preserves an explicit relationship among the paper problem, frozen anchor MES, complexity-stage lineage, environment implementation, algorithm specification, and measured evidence.

Apply these invalidation rules:

- A `complexity_expansion` keeps the anchor authority tuple and creates stage evidence only; preserve and rerun the anchor regression plus the new stage, and route a failure to the algorithm repair ledger. It does not create an MES successor or transfer a stage failure into environment redesign. A legacy/exception MES successor preserves evidence for its parent tuple but cannot establish successor acceptance. A formal environment, information-pattern, paper-range, or other semantic change starts a new evidence epoch, creates a new candidate MES, and invalidates the complete dependent algorithm evidence. An implementation repair under the same anchor MES invalidates only dependent executable evidence.
- An environment-interface-only change invalidates interface, timing, end-to-end, and dependent reproducibility checks.
- An algorithm-specification change invalidates the mapped implementation paths and every downstream check that exercises them.
- A code or configuration change invalidates the affected semantic, reference, MVP, complexity, and reproducibility checks.

Preserve prior evidence as versioned history; never relabel it as evidence for the new version. Rerun the original failure case and every invalidated check, then obtain a fresh independent algorithm-code audit against the exact current versions.
