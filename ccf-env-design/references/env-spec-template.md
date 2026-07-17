# Communication Optimization Problem Specification

Use this specification for a persistent environment contract or handoff. Define the paper scenario, formal optimization problem, and parameter applicability range before deriving the Minimum Executable Scenario (MES).

## Contents

- Versioned communication-optimization specification schema
- Required relations among the paper scenario, formal problem, parameter range, MES, executable evidence, evolution lineage, and readiness states

```yaml
problem_name:
target_domain:

authority:
  paper_scenario_version:
  formal_optimization_problem_version:
  parameter_applicability_range_version:
  minimum_executable_scenario_version:
  parent_mes_version:
  environment_implementation_revision:
  validation_contract_version:
  evidence_epoch:

supported_conclusion:
  conclusion:
  applicability_boundary:

readiness:
  design_verdict: paper-worthy / salvageable / modeling-only / toy / needs-literature
  latest_environment_audit_ref:
  downstream_joint_ready: not_evaluated

scenario_background:
  communication_context:
  communicating_entities:
  task_or_service_need:
  why_communication_matters:
  abstraction_logic:
  abstraction_boundary:

task_causal_chain:
  concrete_problem:
  affected_entities_or_task:
  observed_consequence:
  exogenous_conditions:
  communication_cause:
  decision_to_network_effect:
  network_to_task_effect:
  causal_bottleneck:
  supporting_domain_evidence:

focused_scientific_question:
  question:
  why_it_matters:
  central_tradeoff:
  modeling_necessity:

formal_optimization_problem:
  sets_and_indices:
  parameters_and_units:
  state_variables_if_online:
  exogenous_variables:
  decision_variables_and_domains:
  system_dynamics:
  communication_model:
  optimization_target:
  optimization_direction: minimize / maximize / lexicographic / vector
  objective_function:
  objective_terms:
  hard_constraints:
  soft_constraints:
  information_available_at_decision_time:
  unavailable_or_future_information:
  feasibility_meaning:
  independently_computable_residuals:

problem_to_cause_traceability:
  objective_to_task_mapping:
  variable_to_task_mapping:
  constraint_to_task_mapping:
  dynamics_and_uncertainty_role:
  active_coupling:
  inactive_or_missing_components:

parameter_applicability_range:
  supported_dimensions_and_ranges:
  generation_or_construction_rule:
  boundary_cases:
  excluded_cases:
  range_evidence:
  complexity_balance:

two_layer_environment_contract:
  l1_design_contract:
    required_traceability:
    independent_checks:
    acceptance_criteria:
  l2_method_independent_probe_contract:
    frozen_mes_version:
    method_independent_construction: yes / no / conditional
    predeclared_joint_tradeoff_or_optimization_target:
    target_basis_and_units:
    target_attainability_evidence:
    feasible_reference_or_bound:
    representative_environment_probes:
    tuning_protocol_and_search_budget:
    matched_information_feasibility_and_resource_budget:
    interpretation_rule:

minimum_executable_scenario:
  id:
  status: candidate / accepted / superseded
  parent_version:
  code_entrypoint:
  registered_configurations_or_construction:
  fixed_parameter_values:
  selection_reason:
  state_observation_action_contract:
  trace_and_seed_contract:
  termination_contract:
  independent_checker:
  acceptance_criteria:
  preserved_task_causal_chain:
  preserved_objective:
  preserved_material_constraints:
  preserved_decision_coupling:
  preserved_information_pattern:
  preserved_feasibility_meaning:
  preserved_central_tradeoff:

algorithm_required_environment_information:
  decision_time_observations:
  decisions:
  decision_timing:
  objective_components_or_cost_signal:
  constraint_and_feasibility_signals:
  decision_bounds_or_masks:
  transition_timing:
  termination_and_truncation:
  shapes_units_and_ranges:
  randomness_and_seed_behavior:
  unavailable_information:
  audit_only_diagnostics:

scenario_evolution_proposal_if_any:
  proposal_id:
  originating_evidence:
  source_authority_versions:
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
    repair_refs:
    proposed_failure_classification: algorithm_specific / model_defect / unresolved
  environment_review_if_applicable:
    route_id:
    status: not_started / active / completed / blocked
    confirmed_classification: algorithm_specific / model_defect / unresolved
    decision: return_to_algorithm / authorize_evolution / blocked
    decision_owner: ccf-env-design
    evidence_ref:
  credible_methods_checked:
  change_class: implementation_repair / evidence_expansion / scenario_extension / formal_amendment / research_reframe
  proposed_minimal_change:
  preserved_research_invariants:
  changed_contract_items:
  objective_and_feasible_set_impact:
  information_pattern_impact:
  method_independence_evidence:
  causal_necessity_evidence:
  research_identity_impact:
  information_honesty:
  method_neutrality:
  non_simplification:
    status: pass / fail / unresolved
    preserved_material_invariants:
    unjustified_removed_or_weakened_items:
    corrected_model_items_and_independent_evidence:
    predecessor_regression_anchors:
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
  proposed_successor_versions:
  acceptance_criteria:
  invalidated_artifacts:
  required_reruns:
  decision: proposed / accepted / rejected

handoff:
  ready_for_environment_code_audit: yes / no
  l1_contract_complete: yes / no
  l2_probe_contract_complete: yes / no
  downstream_joint_ready: not_evaluated
  exact_problem_for_algorithm:
  unresolved_questions:
  next_owner:
```

## Required Relations

The paper scenario defines the task and communication setting. The formal optimization problem gives that setting mathematical semantics. The parameter applicability range states where the resulting conclusion is supported. The MES is the smallest versioned package that executes the complete causal and formal path with a registered interface, reproducibility controls, independent checks, and acceptance criteria.

An MES may use one or more registered configurations. It must not remove the task causal chain, objective, material constraints, coupled decisions, information pattern, feasibility meaning, or central tradeoff merely to become smaller or easier. Separate decision-time information from audit-only diagnostics.

Accepted versions are immutable. Within-range experiment settings that do not alter the executable contract are `evidence_expansion`, not a new MES. A `scenario_extension` creates a parent-linked successor MES under the same formal semantics. A `formal_amendment` creates new formal-problem and MES versions. A `research_reframe` starts a new paper-scenario lineage. `implementation_repair` retains the MES authority version and changes only the implementation revision. Apply invalidation and evidence-reuse rules from `scenario-evolution-contract.md` before editing.

Legacy artifacts may expose `scenario_mvp` or `scenario_mvp_version`. Treat those names as read-only aliases for migration; if legacy and canonical values conflict, report the conflict instead of choosing one.

Environment design records the L1 acceptance contract and predeclares the L2 probe contract. It does not write executable verdicts into this authority artifact. `ccf-env-code-auditor` stores `environment_valid`, L2 `evidence_status`, `algorithmic_need`, interface status, and native-review results in the environment-audit artifact and may be linked through `latest_environment_audit_ref`. `algorithmic_need: demonstrated` requires tuned probes to miss an independently justified attainable target; an impossible or post-selected target yields `insufficient_evidence`. Never change the MES to force probe failure. Only downstream algorithm acceptance may set `joint-ready`.

## Recommended Persistent Artifact Headings

Use only headings applicable to the user's scenario. They are a domain-neutral organization pattern, not a requirement to introduce absent mechanisms:

1. Authority, Status, And Lineage
2. Scenario And Supported-Conclusion Boundary
3. Entities, Roles, And Construction
4. Exogenous Process And Information Pattern
5. System Models And State Dynamics
6. Objective, Constraints, And Feasibility
7. State, Observation, Action, And Trace Contract
8. Registered Execution And Evidence Matrix
9. Independent Audit Contract
10. Parameter Basis And Applicability
11. Specification-To-Implementation Traceability
12. Evolution, Invalidation, And Version History
