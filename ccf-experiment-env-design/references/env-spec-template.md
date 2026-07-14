# Communication Optimization Problem Spec

Use this compact specification when writing a handoff-ready communication optimization environment. Keep the focus on the explainable scenario background, focused scientific question, mathematical model, objective function, constraints, and non-toy shortcut test.

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
  abstraction_boundary:

scenario_problem_and_causes:
  concrete_problem:
  affected_entities_or_task:
  observed_consequence:
  communication_cause:
  decision_causal_chain:

plan_reasonableness:
  objective_to_cause_mapping:
  variable_to_cause_mapping:
  constraint_to_cause_mapping:
  dynamics_and_uncertainty_role:
  inactive_or_decorative_components:
  tunable_rule_risk:
  verdict: reasonable / repair-needed / unsupported

focused_scientific_question:
  question:
  why_it_matters:
  central_tradeoff:

mathematical_model:
  parameters:
  decision_variables:
  state_variables_if_online:
  objective_function:
  constraints:
  information_available_at_decision_time:

handoff:
  ready_for_algorithm_design: yes / no
  ready_for_experiment_design: yes / no
  unresolved_questions:
  next_owner:
```

## Required Core

Every completed spec must make the following parts explicit:

- Scenario problem and causes: what problem exists, who or what it affects, and why communication decisions cause it.
- Plan reasonableness: whether each objective term, variable, constraint, dynamic, uncertainty source, and coupling corresponds to the stated causes and changes decisions in credible ranges.
- Scenario background: who communicates, why communication matters, and which abstraction boundary keeps the scenario explainable.
- Scientific question: the single focused tradeoff the paper studies.
- Mathematical model: variables, objective function, constraints, and information pattern.
- Tunable-rule check: whether simple rules are forced to sacrifice one side when improving the other; if not, whether a real coupling, binding constraint, dynamic effect, uncertainty, or conflict regime is missing or inactive.
- Complexity balance: whether the scenario avoids both tunable-rule triviality and components that do not affect feasibility, decisions, or the central tradeoff.
