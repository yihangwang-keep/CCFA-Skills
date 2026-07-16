# Environment Code Audit Protocol

Use this protocol in the same order as `ccf-env-code-auditor/SKILL.md` on the current paper-scenario and MVP versions.

## Evidence Status

- `declared`: present only in a plan, equation, comment, name, or configuration;
- `wired`: reaches an executable path but lacks independent behavioral evidence;
- `verified`: execution plus an independent check demonstrates the planned behavior;
- `contradicted`: code or execution conflicts with the authoritative design;
- `untestable`: missing definitions, entry points, dependencies, or observables prevent verification.

## 1. Authority And Design Contract

Record the scenario spec, MVP, equations, environment code, entry point, configuration, seed, units, time-index convention, and information pattern versions. Resolve conflicts before drawing executable conclusions.

Confirm that the design artifact contains the background, causal problem, scientific question, mathematical model, model-to-cause traceability, binding coupling, complexity evidence, paper-to-MVP relation, and algorithm-information contract.

## 2. Traceability Matrix

Create one row per atomic item:

| ID | Design/equation item | Meaning, unit, domain, time scale | Code symbol | Executed path | Independent check | Status | Consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Cover parameters, exogenous state, observations, algorithm-facing fields, decisions/actions, objective terms, constraints, transitions, randomness, initialization, termination, metrics, scenario-MVP settings, and audit-only diagnostics. Reverse-trace every code path that changes state, objective, feasibility, actions, termination, information, or metrics.

## 3. Semantic Correctness

Verify:

- minimize/maximize direction, signs, normalization, aggregation, discounting, and terminal terms;
- inequality/equality direction, tolerances, units, index sets, residuals, and enforcement;
- pre/post-action timing, simultaneous/sequential updates, conservation, terminal transitions, and horizon indexing;
- observation timing, action domains, masks, audit-only information, and absence of future-state leakage;
- random distributions, correlation, truncation, seed/reset behavior, configuration precedence, and metrics.

Recompute objective components, constraint residuals, resources, and state conservation independently from traces.

## 4. Independent MVP Execution

Run:

1. deterministic replay with frozen exogenous traces and seeds;
2. independent accounting outside the environment reporting path;
3. trace-wide bounds, non-negativity, conservation, monotonicity, symmetry, and domain invariants;
4. one-factor parameter and action interventions with expected directional effects;
5. planned boundary configurations and repeated seeds;
6. complete MVP load with runtime and numerical-stability measurement.

Verify that the scenario MVP uses the paper problem's objective, material constraints, coupling, information pattern, feasibility meaning, and causal chain.

## 5. Optimization Fidelity

Check that every action affects its planned transition, the decision space is not overwritten, objective terms can affect decisions, material constraints can bind, feasibility is reported independently, and environment-side masks/projections/penalties match the accepted mathematical semantics.

## 6. Tunable-Rule Evidence

Run fixed/static, applicable domain, greedy/myopic, decoupled, low-dimensional tuned, and random-feasible policies through the same environment interface. Give them identical observations, feasibility rules, seeds, evaluation cases, and declared tuning budgets.

Record whether improving one side of the scientific tradeoff creates the expected cost on the other and identify the executed mechanism responsible for that behavior.

## 7. Verdict

- `pass`: authority and design contracts are consistent; material items, MVP behavior, optimization fidelity, and the intended tradeoff are verified.
- `conditional`: no contradiction is found, but a decisive trace, configuration, tuning, or execution check is incomplete.
- `fail`: the design and code contradict, material behavior is unverified, the MVP changes the paper problem, optimization fidelity fails, or the intended coupling/tradeoff is inactive.

Attach each finding to the earliest failed gate, exact code location, decisive evidence, minimal repair, and required reruns.
