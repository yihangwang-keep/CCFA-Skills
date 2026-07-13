# Environment Specification Template

Use this template for a reusable communication optimization environment. Keep unknown values as `TBD`.

```yaml
environment_name:
target_domain:
target_venue_or_family:
paper_claim_supported:
publication_verdict: paper-worthy / salvageable / modeling-only / toy / needs-literature

task_semantics:
  external_task:
  why_communication_matters:
  task_utility:
  failure_cost:

optimization_core:
  target_object:
  objective_form:
  objective_terms:
  primary_tradeoff:
  decision_variables:
  decision_timescales:
  hard_constraints:
  soft_constraints:
  binding_constraints:
  feasibility_checks:

entities:
  transmitters:
  receivers:
  relays_or_edges:
  controllers:
  moving_agents:
  users_or_flows:

time_and_space:
  time_horizon:
  decision_epoch:
  spatial_region:
  mobility_model_or_trace:
  topology_model:

communication_model:
  spectrum:
  channel_model:
  path_loss:
  fading_or_blockage:
  interference_model:
  noise_model:
  csi_assumption:
  link_rate_or_reliability_model:

traffic_and_task_model:
  arrival_process:
  packet_or_data_units:
  deadlines:
  priorities:
  queues_or_aoi:
  mission_events:

decision_problem:
  state:
  decisions:
  objective:
  constraints:
  information_pattern:
  offline_or_online:
  tractability_note:
  explainable_algorithmic_structure:
  feasibility_checks:

joint_optimization_necessity:
  coupled_decisions:
  why_decoupling_fails:
  simple_rule_baselines:
  expected_hard_cases:

uncertainty_and_stress:
  random_variables:
  distributions_or_trace_sources:
  seeds:
  stress_cases:
  boundary_cases:

baselines_and_references_needed:
  classical_baselines:
  communication_baselines:
  decoupled_baselines:
  oracle_or_bounds:
  literature_search_queries:

evaluation_contract:
  primary_metrics:
  secondary_metrics:
  metric_direction:
  units:
  parameter_sweeps:
  reproducibility_artifacts:

toy_risks_and_repairs:
  failed_gates:
  overcomplexity_risks:
  explainability_risks:
  required_repairs:
  claim_narrowing:
  next_owner:
```

## Minimum Handoff Packet

When handing off to `ccf-experiment-designer`, include:

- the environment YAML or equivalent structured spec;
- gate verdict and failed-gate repairs;
- central claim and what evidence must test;
- baseline families and oracle/bound expectations;
- objective function, constraints, scenario abstraction level, parameter sweeps, stress cases, and reproducibility requirements;
- unresolved literature or source-basis questions.
