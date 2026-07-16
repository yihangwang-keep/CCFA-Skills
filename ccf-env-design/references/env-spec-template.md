# Communication Optimization Problem Spec

Use this compact specification to define the paper scenario first and then derive its minimum executable scenario (MVP) for implementation and algorithm verification.

```yaml
problem_name:
target_domain:
paper_claim_supported:
verdict: paper-worthy / salvageable / modeling-only / toy / needs-literature

scenario_background:
  communication_context:
  communicating_entities:
  task_or_service_need:
  why_communication_matters:
  abstraction_logic:
  abstraction_boundary:

scenario_problem_and_causes:
  concrete_problem:
  affected_entities_or_task:
  observed_consequence:
  communication_cause:
  decision_causal_chain:

focused_scientific_question:
  question:
  why_it_matters:
  central_tradeoff:
  modeling_necessity:

mathematical_model:
  sets_and_indices:
  parameters:
  state_variables_if_online:
  exogenous_variables:
  decision_variables:
  system_dynamics:
  communication_model:
  constraints:
  information_available_at_decision_time:
  feasibility_conditions:

model_to_cause_traceability:
  objective_to_problem_mapping:
  variable_to_problem_mapping:
  constraint_to_problem_mapping:
  dynamics_and_uncertainty_role:
  active_coupling:
  inactive_or_missing_components:

optimization_target_and_function:
  optimization_target:
  optimization_direction: minimize / maximize / multi-objective
  objective_function:
  objective_terms:
  tradeoff_form:

paper_scenario:
  parameter_space_and_claimed_scope:
  generation_or_construction_rule:
  complexity_balance:
  tunable_rule_finding:

minimum_executable_scenario:
  id:
  code_entrypoint:
  configuration:
  entities_topology_horizon_and_workload:
  fixed_parameter_values:
  selection_reason:
  preserved_objective:
  preserved_material_constraints:
  preserved_decision_coupling:
  preserved_information_pattern:
  preserved_causal_tradeoff:

algorithm_required_environment_information:
  observations:
  actions_or_decisions:
  decision_timing:
  objective_reward_or_cost_signal:
  constraint_and_feasibility_signals:
  action_bounds_or_masks:
  transition_timing:
  termination_and_truncation:
  shapes_units_and_ranges:
  randomness_and_seed_behavior:
  unavailable_or_future_information:
  audit_only_diagnostics:

handoff:
  ready_for_environment_code_audit: yes / no
  ready_for_algorithm_design_after_audit: yes / no
  unresolved_questions:
  next_owner:
```

## Required Relation

The paper scenario is the formal research problem. Its minimum executable scenario (MVP) is the first reproducible end-to-end version. Fixing parameters in the MVP may reduce the number of cases, but it keeps the same objective, material constraints, decision variables and coupling, information pattern, feasibility semantics, and scientific causal chain.

The handoff must also state what environment information the algorithm and independent checker need. Separate algorithm-visible information from audit-only diagnostics.
