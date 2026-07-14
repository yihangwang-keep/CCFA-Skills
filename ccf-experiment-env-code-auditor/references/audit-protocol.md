# Environment Code Audit Protocol

Use this protocol only on the currently implemented target scenario.

## Evidence Status

- `declared`: present only in the plan, equation, comment, name, or configuration;
- `wired`: reaches an executable path but lacks behavioral verification;
- `verified`: complete-scenario execution demonstrates the planned behavior;
- `contradicted`: code or execution evidence conflicts with the plan;
- `untestable`: missing definitions, dependencies, data, entry points, or observables prevent verification.

## Traceability Matrix

Create one row per atomic model item:

| ID | Plan equation/item | Meaning, unit, domain, time scale | Code location/symbol | Executed path | Complete-scenario check | Status | Consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Cover:

1. configurable parameters and constants;
2. exogenous state and stochastic processes;
3. observations and information available at decision time;
4. decision variables/actions, domains, and bounds;
5. objective terms, signs, weights, normalization, and temporal aggregation;
6. hard/soft constraints, residuals, enforcement, and violation metrics;
7. state transitions and update order;
8. initialization and terminal conditions;
9. scenario generation, acceptance, rejection, or resampling;
10. evaluation metrics and their relationship to objective/reward values.

Reverse-trace code paths that alter state, objective, feasibility, actions, termination, or metrics without a planned model counterpart. Classify each as a necessary implementation detail or model drift.

## Semantic Checks

### Objective

- Verify minimize/maximize direction, reward and penalty signs, weights, normalization, horizon aggregation, discounting, and terminal terms.
- Recompute every objective component independently from the complete execution trace.
- Intervene on one relevant parameter or action policy and confirm the expected effect while keeping the scenario structure unchanged.
- Verify that every planned term varies and can affect the preferred decision in at least one tested complete-scenario configuration.

### Constraints And Feasibility

- Verify inequality direction, equality tolerance, index sets, units, and residual definitions.
- Distinguish rejection, action masks, projection, clipping, penalties, repair rules, and termination. Treat them as equivalent only when the complete-scenario behavior matches the planned constraint.
- Recompute every residual independently from the complete trace.
- Measure feasible-run rate and constraint activity. Flag always-slack, always-violated, unreachable, or unreported constraints.

### State, Observation, And Transition

- Verify pre-action/post-action timing, simultaneous/sequential updates, queue and energy accounting, arrivals/departures, partition/merge consistency, terminal transitions, and horizon indexing.
- Verify that observations contain only the planned information and no future state or randomness.
- Verify that each action component affects only its planned transitions and is not ignored, overwritten, or forced to a constant.

### Randomness And Configuration

- Verify distribution family, parameters, correlations, truncation, seed control, reset behavior, and configuration precedence.
- Trace each configured value into the instantiated environment and executed behavior.
- Flag parsed-but-unused options, hidden defaults, hard-coded values, stale caches, and scenario-version mismatches.

## Complete-Scenario Execution

Retain the current scenario's entity count, horizon, topology, partition/merge structure, workload semantics, uncertainty model, resource limits, and coupled decision dimensions.

1. **Deterministic replay:** freeze exogenous traces and seeds; verify identical states, objectives, residuals, and terminal outcomes.
2. **Independent accounting:** recompute objectives, resource consumption, conservation relations, and constraint residuals outside the environment's reporting path.
3. **Trace-wide invariants:** check bounds, non-negativity, conservation, monotonicity, symmetry, permutation invariance where planned, and partition/merge consistency.
4. **Controlled interventions:** change one parameter or action policy and verify the expected effect without changing the scenario structure.
5. **Boundary configurations:** run the same scenario structure with planned low/high workload, weak/severe interference, loose/tight resources, and benign/adverse uncertainty settings.
6. **Repeated seeds and full load:** characterize feasibility, active constraints, objective distribution, tail behavior, numerical stability, and runtime.

Compare expected and observed behavior under the actual command, configuration, and seed. Merely completing without an exception is not evidence of correctness.

## Tunable-Rule Checks

Run these policies against the same implemented environment interface:

- fixed/static policy;
- applicable domain rule such as nearest, max-SINR, shortest path, equal allocation, earliest deadline, or strongest-node choice;
- greedy or myopic policy;
- decoupled policy over the planned decision blocks;
- low-dimensional parameter-tuned policy;
- random feasible policy as a sanity floor.

Apply these controls:

- provide identical observations and feasibility rules;
- declare tuning parameters, search ranges, budget, seeds, and stopping rule;
- separate tuning configurations from evaluation configurations;
- use the same complete scenario structure for tuning and evaluation;
- evaluate nominal, scarcity, strong-coupling, dynamic/uncertain, boundary, and full-load configurations.

As a simple qualitative check, an effective scenario should force a heuristic to sacrifice one side of the intended tradeoff when improving the other. If a tuned heuristic handles both sides well, check whether coupling is inactive, constraints do not bind, dynamics or uncertainty do not affect decisions, the parameter regime is easy, or the implementation is incorrect.

Use this decision rule:

- `pass`: planned coupling is verified in execution and credible simple policies do not handle the intended tradeoff well;
- `conditional`: model-code fidelity passes but heuristic coverage, tuning fairness, configuration coverage, or execution evidence is incomplete;
- `fail`: code contradicts the plan, material behavior is unverified, planned coupling is inactive, or a simple policy consistently handles the intended tradeoff across tested configurations.

Do not infer tunable-rule limitations from formulation labels or code complexity. Base them on executions of the current scenario.
