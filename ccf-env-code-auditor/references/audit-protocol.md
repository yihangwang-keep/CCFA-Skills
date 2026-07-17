# Environment Code Audit Protocol

Use this protocol in the same order as `ccf-env-code-auditor/SKILL.md` on the current paper-scenario, formal-problem, parameter-range, and scenario-MVP versions.

## Evidence Status

- `declared`: present only in a specification, equation, comment, name, or configuration;
- `wired`: reaches an executable path but lacks independent behavioral evidence;
- `verified`: execution plus an independent check demonstrates the specified behavior;
- `contradicted`: code or execution conflicts with the authoritative design;
- `untestable`: missing definitions, entry points, dependencies, or observables prevent verification.

## 1. Authority And Design Contract

Record the paper-scenario, formal-optimization-problem, parameter-applicability-range, scenario-MVP, equation, environment-code, entry-point, configuration, seed, unit, time-index, and information-pattern versions. Resolve conflicts before drawing executable conclusions.

Confirm that the design artifact contains the scenario background, task causal chain, causal bottleneck, scientific question, central tradeoff, supported conclusion and applicability boundary, formal optimization problem, problem-to-cause traceability, complexity evidence, paper-to-MVP relation, and decision-time information contract.

## 2. Traceability Matrix

Create one row per atomic item:

| ID | Problem/equation item | Meaning, unit, domain, time scale | Code symbol | Executed path | Independent check | Status | Consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Cover parameters, exogenous state, decision-time observations, decisions, objective terms, constraints, transitions, randomness, initialization, termination, metrics, scenario-MVP settings, and audit-only diagnostics. Reverse-trace every code path that changes state, objective, feasibility, decisions, termination, information, or metrics.

Keep this matrix in the internal evidence ledger unless the user requests the full audit.

## 3. Semantic Correctness

Verify:

- minimize/maximize direction, signs, normalization, aggregation, discounting, and terminal terms;
- inequality/equality direction, tolerances, units, index sets, residuals, enforcement, and feasibility meaning;
- pre/post-decision timing, simultaneous/sequential updates, conservation, terminal transitions, and horizon indexing;
- observation timing, decision domains, masks, audit-only information, and absence of future-state leakage;
- random distributions, correlation, truncation, seed/reset behavior, configuration precedence, and metrics.

Recompute objective components, constraint residuals, resources, and state conservation independently from traces.

## 4. Independent Scenario-MVP Execution

Run:

1. deterministic replay with frozen exogenous traces and seeds;
2. independent accounting outside the environment reporting path;
3. trace-wide bounds, non-negativity, conservation, monotonicity, symmetry, and domain invariants;
4. one-factor parameter and decision interventions with expected directional effects;
5. planned boundary configurations and repeated seeds;
6. complete scenario-MVP load with runtime and numerical-stability measurement.

Verify that the scenario MVP preserves the paper problem's task causal chain, objective, material constraints, decision coupling, information pattern, feasibility meaning, and central tradeoff. Verify that its fixed values lie inside the stated parameter applicability range and follow its construction rule.

## 5. Optimization Fidelity

Check that every decision affects its specified transition, the decision space is not overwritten, objective terms can affect preferred decisions, material constraints can bind, feasibility is reported independently, and environment-side masks, projections, or penalties match the authoritative mathematical semantics.

## 6. Causal-Bottleneck And Tunable-Rule Evidence

Run fixed/static, applicable domain, greedy/myopic, decoupled, low-dimensional tuned, and random-feasible rules through the same environment interface. Give them identical decision-time information, feasibility rules, seeds, evaluation cases, and declared tuning budgets.

Record whether improving one side of the central tradeoff creates the expected cost on the other, identify the executed causal bottleneck responsible, and test planned boundary cases in the parameter applicability range. If a tuned simple rule handles all intended outcomes, do not alter the environment to preserve algorithmic need; narrow the supported conclusion, identify a causally supported defect, or mark algorithmic need `not demonstrated` or `contradicted`.

## 7. Environment Amendment Evidence

When algorithm-stage evidence indicates a possible environment defect, record the observed failure, credible methods checked, why algorithm-only repair is insufficient, proposed minimal change, objective/feasible-set impact, information-pattern impact, preserved invariants, invalidated artifacts, and required reruns.

Route the request to `ccf-env-design` only if all five questions have supported answers:

1. **Algorithm independence:** would the defect remain under another credible solution method?
2. **Causal necessity:** does task or communication evidence require the change?
3. **Semantic preservation:** do the task outcome, scientific question, and central tradeoff remain unchanged?
4. **Information honesty:** does the decision-time interface still exclude future, hidden, and audit-only information?
5. **Method neutrality:** would the change still be justified without knowing which method benefits?

Algorithm failure alone is insufficient. If the accepted change alters objective semantics, material constraints, information pattern, feasibility meaning, or applicability, create a new environment version and invalidate all dependent MVP, algorithm, baseline, and experimental evidence.

## 8. Verdict And Readiness

- `pass`: authority and design contracts are consistent; material items, scenario-MVP behavior, optimization fidelity, causal bottleneck, and intended central tradeoff are verified.
- `conditional`: no contradiction is found, but a decisive trace, configuration, tuning, range, or execution check is incomplete.
- `fail`: design and code contradict; material behavior is unverified; the scenario MVP changes the paper problem; optimization fidelity fails; or the intended coupling and central tradeoff are inactive.

Determine readiness separately:

- `environment-valid`: the task causal chain, formal problem, applicability range, scenario-MVP relation, and implemented semantics are coherent and verified to the required level.
- `algorithmic-need`: `demonstrated`, `not demonstrated`, or `contradicted` by exact/reference and tuned-simple-rule evidence.
- `interface-complete`: the decision-time interface is sufficient for algorithm work and remains separated from audit-only evidence.
- `joint-ready`: not issued here; it requires downstream algorithm specification and implementation acceptance against this environment version.

Attach each finding to the earliest failed gate, exact code location, decisive evidence, minimal repair, invalidated gates, and required reruns. In the user-visible response, report only the requested artifact, readiness, supported conclusion and applicability, decisive evidence, and material next action unless a full ledger is requested.
