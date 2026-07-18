# Design-Validation Loop

Use this as the domain contract for a Ralph-style design-validation loop. Ralph here means repeated domain work recorded in one ledger; it does not invoke an external plugin or continuation runtime. This protocol determines the next valid action and scientific terminal status. A completion phrase, iteration limit, resource limit, or successful process exit never establishes acceptance.

## Frozen Research Layers And Validation Contract

| Layer | Owner | Frozen content | Allowed loop delta |
| --- | --- | --- | --- |
| `R0 research basis` | paper-scenario owner | task, scientific question, task causal chain, central tradeoff, service meaning, contribution and supported-conclusion type | none; a necessary change is `reframe` |
| `R1 formal problem` | environment design | objective, variables, constraints, dynamics, uncertainty, information pattern, feasibility, parameter range | only an accepted `formal_amendment` |
| `R2 MES and environment` | environment design and audit | frozen anchor MES, registered cases, complexity-stage ladder, execution contract, code, independent checker, L1 criteria, L2 target and probe protocol | implementation repair or complexity expansion; formal amendment only after confirmed model defect |
| `R3 algorithm and implementation` | algorithm design and audit | formal target, role, component classification, mechanism, code, reference, tests, acceptance criteria | default repair layer |

The anchor MES retains the complete R0/R1 causal and formal path and may include multiple registered cases needed to activate the joint tradeoff. Accepted authority versions are immutable. The initial anchor L2 heuristic-probe result is frozen with the anchor. After initial algorithm acceptance, complexity stages add one user-requested, method-independent difficulty dimension at a time under the same R0/R1/interface contract; they never replace the anchor or reopen L2. Documentation is part of the contract: change the owning specification before dependent code when semantics change, rather than rewriting prose afterward to legitimize current behavior.

Freeze `V0 validation contract` before the first repair. Record criterion owners, original failure, MES cases, seeds or traces, L2 probe families and tuning budgets, algorithm baselines, metrics, independent checker, tolerances, required solver status, time/resource/platform accounting, stop rule, and pass condition. Diagnostics may be added without removing a criterion. A material criterion change creates a successor validation contract and cannot make the old failure accepted.

## Fixed Loop Instruction

Repeat this instruction unchanged; store round-specific state only in the ledger:

```text
Continue the CCFA design-validation loop at <ledger-path>.
Read the frozen R0-R3 authority, validation contract, and current artifact manifests.
Preserve every original failure, anchor MES case, complexity stage, target, and pass criterion.
Work on the earliest missing, stale, failed, or contradicted dependency.
Assign one active owner and apply at most one owned delta.
Do not change the environment merely to rescue an algorithm or force initial-anchor heuristic-probe failure. For a later stage, check implementation consistency and anchor regression; do not run a new heuristic-probe need test.
After faithful algorithm repairs are exhausted, route the exhaustion evidence to
environment and formal-model review; let ccf-env-design classify the failure.
Run the original failure, every invalidated check, and the applicable fresh CCFA audit.
Require native contract-fidelity and implementation-assurance reviews on the candidate digest.
Update the ledger with evidence and record only a valid structured terminal status.
```

The fixed-instruction hash prevents drift. A completion phrase has no status semantics; only the structured ledger can record a terminal decision.

## Persistent Internal Ledger

```yaml
loop_id:
scope: environment | algorithm | joint
phase: anchor_acceptance | complexity_upgrade
stage_request_id:
status: active | accepted | no-algorithmic-contribution | rebaseline-required | reframe | blocked
fixed_instruction_hash:
authority_versions:
  paper_scenario:
  formal_problem:
  minimum_executable_scenario_version:
  mes_role: anchor | candidate | legacy_successor
  mes_freeze_epoch:
  complexity_stage_id:
  parent_complexity_stage_id:
  environment_implementation:
  algorithm_specification:
  algorithm_implementation:
validation_contract:
  version:
  artifact_paths: []
  locked_failures: []
  registered_mes_cases: []
  l2_targets_probes_tuning_budgets: []
  metrics_checkers_tolerances: []
  time_resource_platform_rules: []
  pass_conditions: []
accepted_artifact_set_id:
rounds: []
current_round:
  number:
  route_id:
  owner:
  active_failure:
  single_delta:
  round_input_artifact_set_id:
  candidate_artifact_set_id:
  changed_paths: []
  invalidated_checks: []
  validation_evidence: []
  domain_audit:
  native_review_id:
  review_axis_status:
terminal_review_ids:
  environment:
  algorithm:
environment_l1:
environment_l2_algorithmic_need:
l2_scope: anchor_only | inherited_for_complexity_stage
algorithm_no_heuristic_gate:
algorithm_no_heuristic_gate_status:
active_route_id:
route_records:
  - route_id:
    algorithm_specification_version:
    exhaustion_scope: mechanism | family | credible_routes
    status: not_started | active | exhausted | superseded | closed | not_applicable
    state_history: []
    repair_refs: []
    proposed_failure_classification: algorithm_specific | model_defect | unresolved
    target_evidence_if_applicable:
      target_scope: environment_l2 | formal_problem | algorithm_guarantee
      target_definition_ref:
      target_definition_owner: ccf-env-design | ccf-algorithm-designer
      evidence_items:
        - evidence_ref:
          evidence_status: current | stale | invalid | not_applicable
          evidence_owner: ccf-env-design | ccf-env-code-auditor | ccf-algorithm-designer | ccf-algorithm-code-auditor
    environment_review:
      route_id:
      status: not_started | active | completed | blocked
      confirmed_classification: algorithm_specific | model_defect | unresolved
      decision: return_to_algorithm | authorize_evolution | blocked
      decision_owner: ccf-env-design
      evidence_ref:
    next_route_id:
evolution_proposal:
  source_route_id:
validation_change_request:
  status: not_started | proposed | accepted | rejected | blocked
  owner:
  independent_measurement_or_semantic_defect_evidence:
  non_simplification:
    status: pass | fail | unresolved
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
  decision_evidence:
supported_conclusion:
conclusion_applicability_range:
remaining_limitations: []
terminal_reason:
```

Every artifact set contains repo-relative path, role, and content digest. Append
each closed round to `rounds`; `current_round` is only the active projection and
must not overwrite history. `route_records` is append-only by route ID: retain
each route's `state_history`, target evidence, proposed classification, and
environment review, and move only `active_route_id` when another route opens.
Never copy or inherit one route's confirmed classification or review into
another route. A Git identifier may be optional provenance, but it is never
required for identity, review, or acceptance. Store auditable decisions and
evidence, not hidden reasoning or unpublished results in public systems.

## One Round

1. Verify the fixed-instruction hash, authority tuple, validation contract, and round-input manifest.
2. Select the earliest stale or failed dependency. In Phase A, L1 environment fidelity precedes the one-time L2 heuristic resistance and initial algorithm acceptance. In Phase B, stage L1 consistency and anchor regression precede algorithm-upgrade acceptance; L2 is inherited.
3. Name one owner and one smallest delta. Do not mix environment authority and algorithm behavior changes. Preserve algorithm revisions separately; when credible repairs are exhausted at a named complexity stage, close their round and open a model-review round without replacing the anchor.
4. Create the candidate artifact set and mark every dependent audit, review, and result stale when its content digest changed.
5. Run the original failure and the anchor regression under the locked validation contract, then all invalidated checks. Preserve failures; do not substitute an easier MES case, seed, target, tolerance, or budget; choosing favorable seeds to avoid failure is prohibited. Do not add an L2 heuristic sweep for a Phase-B stage.
6. Obtain the applicable fresh environment or algorithm auditor verdict. For environment scope, keep L1 contract fidelity separate from L2 algorithmic-need evidence.
7. The auditor launches two fresh, read-only reviewers under the shared native implementation-review protocol. The repairer cannot be a reviewer. Both reports bind to the candidate digest; their statuses remain separate and cannot offset each other.
8. Append the closed round to history and open a new `current_round` only when all required evidence is current. If a second cause appears, open a new round rather than expanding the current delta.
9. Before a terminal decision, obtain a fresh native review with `purpose: terminal_acceptance`; a `round_closure` review cannot be promoted merely because no files changed.

No round requires a branch, worktree, commit, `HEAD`, or an external generic workflow. The loop owns no publication experiment design and performs no unrelated refactor.

## Environment And Validation Changes

Classify environment deltas before editing:

- `implementation_repair`: same formal problem and MES; new implementation revision.
- `evidence_expansion`: same authority; new experimental coverage only.
- `complexity_expansion`: same formal problem, parameter semantics, interface, and frozen anchor MES; record one method-independent complexity stage and keep anchor regression cases.
- `scenario_extension`: legacy/exception parent-linked successor MES only with explicit environment-owner justification; not the normal post-acceptance route.
- `formal_amendment`: new formal problem, MES, and evidence epoch.
- `research_reframe`: new paper-scenario lineage.

`invalidation` is a consequence, not a sixth class. An algorithm request must be method-independent, causally necessary, information-honest, and neutral to method ranking. An adequately tuned heuristic reaching the initial anchor L2 target is evidence that algorithmic need is not demonstrated, not permission to add difficulty. A later complexity-stage heuristic result is only comparison evidence and does not reopen L2. Use the environment's scenario-evolution contract for proposal fields and impact rules.

When environment L1 and algorithm-code fidelity pass but one route's documented mechanism or family revisions still cannot meet the formal target, bind exhaustion to `route_id`, algorithm-specification version, and scope, then set that route to `exhausted` and open `environment_review`. The algorithm/debugger may record only a proposed classification. Only `decision_owner: ccf-env-design` may set the confirmed classification, review status, and decision.

A completed `model_defect` review with `decision: authorize_evolution` may create a classified formal-problem amendment and new candidate-MES/evidence epoch. It must not silently overwrite the frozen anchor. A completed `algorithm_specific` review with `return_to_algorithm` closes or supersedes the exhausted route; if credible routes remain, append a new route record with a new `route_id` and `status: not_started`, then move `active_route_id` rather than resetting or overwriting the old record. Bind target evidence, environment review, and any evolution proposal to that route ID. If `exhaustion_scope: credible_routes`, an algorithm-specific decision supports `no-algorithmic-contribution` rather than inventing another route. An `unresolved` review is blocked. Reject any replacement that weakens material difficulty for tractability or acceptance. A model item independently proven inconsistent with the paper scenario may be corrected or replaced only when causal difficulty and the central tradeoff remain intact.

Resolve target definition and every evidence item owner before model classification using the scenario-evolution contract's legal owner combinations. A stale or invalid `environment_l2` target/attainability witness returns to environment design and environment audit. Analytical `algorithm_guarantee` evidence returns to algorithm design; implementation/execution evidence returns to algorithm code audit. Only a contradiction in the authoritative `formal_problem` target or feasibility semantics can support `model_defect`.

A validation-contract correction is allowed only when its owner independently proves a measurement/checker defect or a mismatch with already accepted scenario/formal semantics. Set `validation_change_request.status: accepted` only when `non_simplification.status: pass`, `unjustified_removed_or_weakened_items` is empty, predecessor hard-case anchors remain registered, and every structured impact field is resolved: target, tolerance, feasibility rules, solver status, time/resource budget, seed selection, objective weighting or priority, case sampling distribution, cross-case aggregation, horizon or termination, and exogenous resources or capabilities must not hide reduced difficulty. It may not drop a failure case, choose favorable seeds, widen a correctness/feasibility tolerance, lower a target, increase a time/resource budget, weaken solver status, or change weighting/aggregation merely to obtain a pass. Preserve the old failure and mark affected evidence stale. If the desired criterion change actually lowers the research requirement, reject it as a repair; it requires a research reframe and cannot inherit the current contribution evidence.

## Terminal Status Precedence

Apply this order: `reframe` -> `rebaseline-required` -> `blocked` -> scope-specific scientific decision. Do not report `accepted` when a higher-precedence condition holds.

- `scope: environment`, `accepted`: current R0-R2 and V0; initial anchor L1 passes; anchor-only L2 has a current supported result; original failure and invalidated checks close; and `terminal_review_ids.environment` names a native `terminal_acceptance` review whose two passing axes bind to the candidate artifact set. A Phase-B stage additionally requires stage L1 consistency and anchor regression. Set the algorithm review ID to `not_applicable`. For an initial algorithm-contribution handoff, L2 must be `algorithmic_need: demonstrated`.
- `scope: algorithm`, `accepted`: current accepted anchor environment with the anchor L2 result (inherited for a complexity stage); algorithm specification and code pass; `method_role: proposed` passes the no-heuristic gate; reference/MES evidence is current; and `terminal_review_ids.algorithm` names a native `terminal_acceptance` review whose two passing axes bind to the candidate artifact set. Retain the accepted environment review ID rather than replacing it.
- `scope: joint`, `accepted`: both environment and algorithm terminal review IDs are current, have `purpose: terminal_acceptance`, and satisfy their acceptance conditions against one compatible authority tuple.
- `no-algorithmic-contribution`: the current environment remains valid and adequately tuned probes meet the target, or credible non-heuristic algorithm routes are exhausted without a supportable contribution and no model defect is established. A no-heuristic violation alone routes to algorithm redesign. A confirmed `model_defect` routes to formal amendment and rebaselining, not this terminal status.
- `rebaseline-required`: an accepted `formal_amendment` or material validation-semantic change creates a new evidence epoch and candidate MES. A `complexity_expansion` stays on the frozen anchor and invalidates only the new stage and dependent downstream evidence until the anchor regression and stage rerun close. A legacy/exception `scenario_extension` requires its explicitly declared successor invalidation.
- `reframe`: R0 research identity must change.
- `blocked`: failure classification remains `unresolved`, or required evidence, execution resources, independent review capability, external authority, or a material user decision is unavailable. Record the exact unblock condition; never lower criteria.

## User-Visible Projection

Return the repaired artifact or behavior first. Then expose only status, authority versions, the decisive cause or supported conclusion, the one delta, checks and review axes refreshed, and any limitation or next owner. Keep the full ledger, candidate hypotheses, reviewer dialogue, and routine pass matrix internal unless requested.
