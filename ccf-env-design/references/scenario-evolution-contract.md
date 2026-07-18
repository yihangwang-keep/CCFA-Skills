# Scenario Evolution Contract

Use this contract when code, audit, or experiment evidence suggests changing an accepted paper scenario, formal optimization problem, parameter applicability range, Minimum Executable Scenario (MES), complexity stage, or executable environment. Classify the change before editing. Keep the complete ledger internal unless the user requests it or a version decision blocks progress.

## Authority Lineage

Bind every decision and evidence item to this tuple:

```yaml
paper_scenario_version:
formal_optimization_problem_version:
parameter_applicability_range_version:
minimum_executable_scenario_version:
parent_mes_version:
mes_role: candidate | anchor | legacy_successor
mes_freeze_epoch:
complexity_stage_id:
parent_complexity_stage_id:
environment_implementation_revision:
validation_contract_version:
evidence_epoch:
```

An accepted authority artifact is immutable. The first accepted MES is the anchor: after its design, L1, and L2 gates pass, its identity and complete causal package are frozen for the normal algorithm-development loop. A complexity stage cites the anchor and records its method-independent delta, evidence, preserved invariants, and acceptance criteria without creating a new MES. A formal amendment or research reframe is an exceptional authority change that starts a new candidate-MES design and evidence epoch. Superseding a version does not erase or make its evidence false; it limits that evidence to the authority tuple under which it was obtained.

The intended progression is paper scenario -> candidate MES with the complete central tradeoff -> L1/L2 acceptance and MES freeze -> complexity ladder with algorithm repair at each failed stage -> paper-range evidence. If the authoritative problem is independently shown infeasible or ill-posed, stop the ladder, revise the formal problem through an explicit amendment, and restart candidate-MES acceptance; this is not a routine algorithm upgrade. MES is the paper's minimum scale, not a minimum scientific problem.

## Change Classification

| Class | Use when | Version action | Required consequence |
| --- | --- | --- | --- |
| `implementation_repair` | Code, configuration, checker, or test contradicts the accepted contract while problem and MES semantics remain unchanged. | Keep paper-scenario, formal-problem, parameter-range, and MES versions; create a new implementation revision. | Reproduce the original failure and rerun affected environment checks plus every downstream check that consumed changed behavior. |
| `evidence_expansion` | New runs add settings already authorized by the current formal problem, construction rule, parameter range, MES interface, and validation semantics. | Keep authority versions; create new evidence records. | Run all relevant methods fairly on the added settings. Do not call an ordinary sweep a scenario upgrade. |
| `complexity_expansion` | After the anchor MES and initial algorithm are accepted, a user/project owner requests a method-independent scale, load, topology, uncertainty, coupling, or boundary increase within the accepted formal problem, construction rule, parameter range, and interface. | Keep paper-scenario, formal-problem, parameter-range, and anchor MES versions; create a complexity-stage evidence record under the current epoch. | Audit stage implementation consistency, keep the anchor as a regression case, inherit anchor `algorithmic_need`, do not rerun L2, and route any algorithm failure to code/design repair. Do not create an MES successor. |
| `scenario_extension` (legacy/exception) | Read existing successor-MES records, or use only when environment design documents that an already-authorized formal contract cannot be executed without an authority-level package change. It is not the normal post-acceptance complexity route. | Legacy records retain their parent; a new authority action must be reclassified as `formal_amendment` or `research_reframe` unless the environment owner explicitly records why the anchor contract itself is incomplete. | Preserve the anchor and all failed evidence; require explicit environment review, compatibility anchors, and the applicable rebaseline. |
| `formal_amendment` | Objective, decision variables, material constraints, dynamics, uncertainty, information pattern, feasibility meaning, parameter semantics, or formal construction semantics change while research identity remains intact. | Create new formal-problem, parameter-range when affected, and MES versions; start a new evidence epoch. | Rebaseline environment, algorithm, baseline, and experimental evidence under one common successor contract. |
| `research_reframe` | The task or service outcome, scientific question, task causal chain, central tradeoff, intended contribution type, or supported-conclusion meaning changes. | Start a new paper-scenario lineage, then define a new formal problem and MES. | End the current lineage as `reframe`; do not inherit acceptance or rankings as evidence for the new research object. |

`invalidation` is not a sixth change class. It is the dependency consequence of an accepted delta. Record what becomes stale for the successor, why, what remains valid for the prior version, and the exact reruns needed.

If a proposed complexity increase changes formal semantics, parameter meaning, or information/feasibility rules, reclassify it as `formal_amendment`; it cannot be hidden in a complexity stage. If it changes research identity, reclassify it as `research_reframe`. Names such as enhancement, upgrade, optimization, or cleanup do not override these boundaries.

## Decision Protocol

1. Preserve the originating command, configuration, seeds or traces, outputs, and current authority tuple.
2. Classify the origin as `algorithm_failure`, `domain_or_formal_evidence`, `code_or_audit_evidence`, or `experiment_evidence`, then identify whether it concerns implementation fidelity, coverage, scenario semantics, formal semantics, or research identity.
   Classify by the decisive evidence, not by which tool produced it. If the core fact is that an algorithm or its result missed a target, use `algorithm_failure` even when the observation came from code audit or an experiment. The other origins are reserved for evidence whose environment implication is independent of method ranking or failure.
3. For `algorithm_failure`, require current environment L1 and algorithm-code fidelity plus the repair-exhaustion ledger. This always opens environment/formal-model review. Use another credible method, reference, bound, or probe when available; the environment owner then classifies the failure as algorithm-specific, model-defect, or unresolved. Only `model_defect` may justify a scenario or formal change on this branch.
4. For other origins, require method-independent causal, task, physical, protocol, service, audit, or formal evidence appropriate to the proposed change. A `complexity_expansion` follows anchor and initial-algorithm acceptance, does not require prior algorithm exhaustion to open, and keeps the accepted authority; it does require a user/project-owner stage request, frozen construction rule, stage implementation contract, and anchor regression. A legacy/exception `scenario_extension` requires environment-owner review.
5. Run a non-simplification check and select exactly one change class and owner before editing. Environment implementation repair belongs to environment code ownership; experiment-only coverage belongs to experiment design; scenario extension, formal amendment, and research reframe require environment-design acceptance.
6. For a complexity stage, predeclare the stage ID, parent stage, method-independent delta, preserved anchor, acceptance criteria, and affected reruns; do not propose a successor MES. For a formal amendment or reframe, predeclare successor versions, preserved invariants, invalidation set, and required reruns.
7. Apply one owned delta. Mark dependent evidence stale before relying on new stage or successor evidence. At every complexity-stage failure, preserve the stage and route the earliest algorithm owner before considering a model review.
8. Obtain fresh environment audit evidence for the changed implementation or formal authority. Refresh algorithm and experiment evidence only against mutually compatible authority, implementation, validation, and complexity-stage versions.

Never obtain tractability or acceptance by deleting or weakening a material item, choosing favorable seeds, widening a tolerance, exposing future or audit-only information, replacing the environment objective with a solver surrogate, or tailoring the scenario to one method. An item independently proven inconsistent with the paper scenario may be corrected or replaced only when the successor preserves causal difficulty and the central tradeoff and rebaselines all dependent evidence.

A sufficiently tuned heuristic probe reaching the predeclared joint-tradeoff or optimization target does not invalidate an L1-valid environment. It means algorithmic need is not demonstrated. Do not propose a scenario extension or formal amendment merely to make that probe fail; require independent task, causal, physical, protocol, service, or formal evidence for any environment change.

## Evolution Proposal

```yaml
proposal_id:
source_authority_versions:
originating_evidence:
origin_type: algorithm_failure / domain_or_formal_evidence / code_or_audit_evidence / experiment_evidence
observed_gap_or_failure:
target_evidence_if_applicable:
  target_scope: environment_l2 / formal_problem / algorithm_guarantee
  target_definition_ref:
  target_definition_owner: ccf-env-design / ccf-algorithm-designer
  evidence_items:
    - evidence_ref:
      evidence_status: current / stale / invalid / not_applicable
      evidence_owner: ccf-env-design / ccf-env-code-auditor / ccf-algorithm-designer / ccf-algorithm-code-auditor
algorithm_repair_exhaustion_if_applicable:
  route_id:
  algorithm_specification_version:
  exhaustion_scope: mechanism / family / credible_routes
  status: exhausted
  repair_refs: []
  proposed_failure_classification: algorithm_specific / model_defect / unresolved
environment_review_if_applicable:
  route_id:
  status: not_started / active / completed / blocked
  confirmed_classification: algorithm_specific / model_defect / unresolved
  decision: return_to_algorithm / authorize_evolution / blocked
  decision_owner: ccf-env-design
  evidence_ref:
proposed_delta:
change_class: implementation_repair / evidence_expansion / complexity_expansion / scenario_extension / formal_amendment / research_reframe
owner:
mes_policy: freeze_anchor | legacy_successor_review | new_candidate_after_formal_amendment | new_lineage_after_reframe
complexity_stage:
  stage_request_id:
  requested_by:
  stage_id:
  parent_stage_id:
  anchor_mes_version:
  method_independent_delta:
  formal_problem_unchanged: true | false
  anchor_regression_required: true
  rerun_l2_heuristic_probes: false
  inherited_algorithmic_need:
  algorithm_failure_route: code | mechanism | family | formal_model | unresolved
preserved_research_invariants: []
changed_contract_items: []
method_independence_evidence:
causal_necessity_evidence:
research_identity_impact:
information_honesty:
method_neutrality:
non_simplification:
  status: pass / fail / unresolved
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
objective_and_feasible_set_impact:
information_pattern_impact:
supported_conclusion_effect:
proposed_successor_versions:
acceptance_criteria: []
invalidated_artifacts: []
required_reruns: []
decision: proposed / accepted / rejected
decision_evidence:
```

For an `algorithm_failure` origin, only `environment_review.status: completed` with `decision_owner: ccf-env-design`, `confirmed_classification: model_defect`, and `decision: authorize_evolution` may authorize a scenario or formal successor. An algorithm-side proposed classification is never authoritative.

Target evidence follows its definition owner and each evidence item's owner
before classification. For `environment_l2`, `target_definition_owner` is
`ccf-env-design`; analytical/attainability evidence may be owned by
`ccf-env-design`, while executed probe evidence is owned by
`ccf-env-code-auditor`. For `formal_problem`, the definition owner is
`ccf-env-design`; evidence is owned by `ccf-env-design` or
`ccf-env-code-auditor` according to the cited artifact. For
`algorithm_guarantee`, the definition owner is `ccf-algorithm-designer`;
analytical evidence is owned by `ccf-algorithm-designer`, while implementation
or execution evidence is owned by `ccf-algorithm-code-auditor`. Record each
source separately in `evidence_items`; an unsupported owner/scope combination
is unresolved. Invalid `environment_l2` attainability returns to environment
design/audit and makes the old L2 result stale; an `algorithm_guarantee`
failure returns to algorithm design; only an authoritative `formal_problem`
contradiction may support model-defect review.

Any accepted authority successor requires `non_simplification.status: pass`, an empty `unjustified_removed_or_weakened_items`, preserved predecessor regression anchors, and explicit evidence that target, tolerance, feasibility rules, solver status, time/resource budget, seed selection, weighting/priority, case distribution, aggregation, horizon/termination, and exogenous resources or capabilities do not hide a reduction in difficulty. A corrected model item requires independent scenario/formal evidence and must preserve the causal problem and central tradeoff.

An accepted `complexity_expansion` requires a user/project-owner stage request and produces a stage specification before dependent algorithm runs are treated as evidence; it never produces a successor MES or reruns anchor L2. A legacy/exception `scenario_extension` or a `formal_amendment` produces a successor specification before dependent code is treated as authoritative. A formal amendment creates a new candidate MES and evidence epoch; the prior anchor remains historical and is not silently edited. Do not rewrite documentation after implementation merely to legitimize observed behavior.

## Evidence Compatibility

- Evidence is reusable only when its authority, implementation, validation, configuration, and metric semantics match the target conclusion. Cite the exact compatibility basis.
- Old evidence remains valid for its recorded version unless independently contradicted. Mark it `historical` or `superseded`, not silently deleted.
- Every complexity expansion must preserve the anchor MES cases as regression anchors. A scenario extension or same-lineage formal amendment must also preserve predecessor hard cases unless independent task or formal evidence proves a case invalid. A method's failure is not such evidence.
- Do not rank objective values from materially different formal-problem versions. Cross-version comparison requires a genuinely common task, physical, service, or resource quantity and an explicit version boundary.
- Preserve every failed, infeasible, timed-out, and boundary setting with its original versions.

## Heuristic Boundary

Heuristic, greedy, static, domain, tuned, decoupled, and random-feasible rules may be used as `environment_probe` policies and experiment baselines. They test whether the causal bottleneck, constraint activity, and central tradeoff are real; they are not proposed algorithm contributions.

The hard no-heuristic rule for the paper's proposed algorithm contribution belongs to `ccf-algorithm-designer`. `ccf-algorithm-code-auditor` verifies that the implementation contains no heuristic decision mechanism or hidden heuristic fallback. Environment design records the resulting algorithmic-need evidence but does not weaken, duplicate, or reinterpret that algorithm gate.

## User-Visible Projection

Return the requested specification or evolution decision first. Then expose only the current and proposed versions, selected change class, decisive evidence, preserved research identity, invalidated evidence, required reruns, and next owner. Do not print the full internal proposal or dependency ledger by default.
