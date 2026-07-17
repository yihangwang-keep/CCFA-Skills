# Communication-Paper Evidence Design

Use this file after applicable environment and algorithm MVP evidence has been accepted. Design paper-range experiments without fabricating results or repairing upstream design inside the experiment plan.

## Contents

- Evidence principle, accepted inputs, and conclusion ledger
- Communication evidence and algorithmic-contribution gate
- Scenario integrity, baselines, metrics, and mechanism tests
- Robustness, version boundaries, evidence artifacts, and minimum package

## Evidence Principle

Start from the intended paper conclusion and its applicability range, not from a table. Every experiment must answer a decisive question:

- Does the method solve the stated formal optimization problem while satisfying its feasibility meaning?
- Does the proposed mechanism address the named causal bottleneck or central tradeoff?
- Are comparisons fair under the same information, constraints, tolerance, tuning budget, and resource accounting?
- Does the conclusion remain supported across its declared parameter applicability range?
- What fails, where is the boundary, and why?
- Can another researcher reproduce and independently check the result?
- Is the evidence sufficient for the target venue and paper type?

Record before execution what result would support, narrow, contradict, or leave each conclusion unresolved.

## Accepted Inputs

Use only version-compatible accepted artifacts:

```yaml
paper_scenario_version:
formal_problem_version:
parameter_applicability_range_version:
minimum_executable_scenario_version:
parent_mes_version:
environment_code_version:
environment_contract_fidelity_verdict:
algorithmic_need: demonstrated | not_demonstrated | contradicted | insufficient_evidence | stale
algorithm_specification_version:
algorithm_code_version:
algorithm_audit_verdict:
method_role:
no_heuristic_gate:
no_heuristic_gate_status:
exact_or_oracle_bound_reference:
independent_checker:
known_limitations_and_exclusions: []
```

For non-algorithmic work, mark algorithm fields `not applicable` with a reason. A conditional verdict supports only the settings explicitly accepted by its auditor. A same-semantics MES successor preserves earlier evidence only for the parent authority tuple; rerun every method and conclusion item affected by successor cases or behavior. If a formal amendment changes the problem semantics, do not reuse earlier method rankings, objective values, or conclusion scope without complete rebaselining.

## Conclusion-Evidence Ledger

Keep this ledger internal unless the user requests it:

```text
Paper conclusion:
Conclusion applicability range:
Decisive question:
Authoritative versions:
Required setting and comparison:
Metrics and feasibility checks:
Mechanism or intervention:
Robustness and failure boundary:
Support / narrow / contradict / unresolved rule:
Result: TBD
```

An experiment belongs in the plan only if it changes at least one conclusion status, applicability boundary, mechanism interpretation, or reproducibility judgment.

## Communication And Networking Evidence

Cover only dimensions that exist in the accepted paper scenario and formal problem:

- objective, decision variables, material constraints, and feasibility meaning;
- channel, topology, mobility, interference, bandwidth, power, energy, queue, latency, reliability, freshness, and task dependencies when applicable;
- uncertainty and information timing only when they change available decisions;
- routing, scheduling, association, allocation, placement, trajectory, or control coupling actually present in the formulation;
- exact/oracle/bound comparison on tractable instances;
- nominal, resource-tight, strongly coupled, boundary, and failure regimes inside the parameter applicability range;
- end-to-end task or service consequences, not only solver-internal quantities;
- execution time, memory, signaling, and other operational costs needed by the intended conclusion.

Do not add unrelated mechanisms or operating dimensions merely to make the experiment package look broader.

## Upstream Algorithmic-Contribution Record

For an algorithmic paper, require current, version-compatible acceptance records for the formal target, implementation-ready solution process, verification criteria, qualifying theory or exact/oracle/bound reference, `method_role: proposed`, component classification, `no_heuristic_gate: required`, and `no_heuristic_gate_status: pass`. Experiment design checks only presence, status, scope, and version compatibility; it does not derive the algorithm, classify components, or repeat code audit.

If the accepted record reports any heuristic decision mechanism in the proposed method, stop the experiment branch and return it to `ccf-algorithm-designer` or `ccf-algorithm-code-auditor`. Missing, conditional, or stale evidence also returns to its owner. Heuristic methods remain permitted under explicit environment-probe, baseline, reference, or diagnostic roles.

## Scenario Integrity And Upstream L2 Evidence

Freeze scenario generation before inspecting comparative outcomes.

- **Preserve the causal bottleneck:** simplification must not remove the scarcity, coupling, dynamics, uncertainty, information restriction, task dependency, or other difficulty that produces the central tradeoff.
- **Method-independent construction:** derive settings from physical/task ranges, standards, traces, service requirements, or a generator fixed without using the proposed method's favorable outcomes.
- **Coverage:** include credible nominal, diverse, hard, boundary, and failure settings. Report generation rules, parameter ranges, seeds, exclusions, and any after-the-fact filtering.
- **Threshold integrity:** choose thresholds from domain meaning or a predeclared development rule. Give comparable methods matched tuning budgets and report the full relevant sweep. Never choose a final setting because it maximizes the proposed method's lead.
- **Consume L2:** require a current `ccf-env-code-auditor` record containing the frozen MES, target basis and attainability, representative probes, tuning/search budgets, matched conditions, and `algorithmic_need`. Experiment design does not rerun or rejudge this gate.
- **New contradiction:** heuristic methods may still appear as paper baselines. If new, fairly tuned evidence reaches the accepted target or contradicts L2, preserve it and route it through `ccf-experiment-debugger` to the environment auditor. Do not directly rewrite `algorithmic_need`, alter environment parameters, or construct a favorable successor MES inside experiment design.
- **Controlled modification:** state the external reason, changed assumption, old and new versions, invalidated evidence, and required reruns. Keep the original result visible when the modification follows result inspection.

The experiment branch fails when the principal advantage disappears under credible variation or matched tuning while the paper still states a general algorithmic conclusion. Route the contradiction through `ccf-experiment-debugger`; do not construct a favorable replacement setting or issue a new environment verdict here.

MES acceptance establishes end-to-end correctness only for its registered cases. Conclusions about scale, load, topology, channel conditions, mobility, uncertainty, deadlines, or other ranges require explicit paper-range evidence.

## Baseline Matrix

Use these categories when applicable:

- closest prior method under a matching formal problem;
- current strong method with available reproducible implementation;
- properly tuned simple rule or fixed-priority method;
- decoupled or single-stage alternative that tests whether joint optimization is necessary;
- exact solver, exhaustive search, oracle, relaxation, or certified bound on tractable instances;
- deployed or protocol-default method when it represents the practical reference.

For each baseline record:

```text
Baseline and source:
Why it is decisive:
Formal-problem match and required adaptation:
Information and feasibility conditions:
Stopping tolerance and tuning budget:
Implementation source and version:
Expected metrics:
Can run: yes / no / unknown
Missing evidence: TBD
```

Do not compare methods under different information availability, constraint enforcement, objective definitions, termination tolerances, or resource budgets without isolating and disclosing the difference.

## Metrics And Interpretation

Use metrics only when they determine a paper conclusion or applicability boundary:

- original objective components and lexicographic priority where applicable;
- feasibility rate, violation magnitude, constraint residual, and binding frequency;
- task/service quantities such as completion, delay, reliability, freshness, energy, or fairness;
- gap to exact/oracle/bound reference and certification scope;
- runtime distribution, memory, signaling, iteration count, and failure/timeout rate;
- variation across seeds or repeated executions with an appropriate uncertainty summary.

For every metric state unit, direction, aggregation, repeated-run protocol, and interpretation threshold. Never present a surrogate or internal solver quantity as the task objective without an explicit mapping.

## Mechanism Tests

Each ablation or intervention must test one accepted mechanism:

```text
Mechanism or assumption:
Formulation source:
Removal, replacement, or controlled intervention:
Affected metric and constraint:
Expected interpretation if unchanged, improved, or degraded:
```

Useful tests include removing one mechanism, replacing it with a generic admissible alternative, disabling one coupling, varying one formulation-derived parameter, and comparing tractable instances with the exact reference. A parameter sweep is sensitivity evidence, not mechanism evidence by itself. When the method is not composed of separable mechanisms, do not invent ablations; return missing mechanism justification to algorithm design.

## Robustness, Failure, And Version Boundaries

- Expand one major parameter dimension at a time from accepted MES cases into the predeclared applicability range so failures remain attributable. This is evidence expansion, not an MES edit.
- Preserve every failed, infeasible, timed-out, and boundary setting. Distinguish solver failure from proven problem infeasibility.
- Rerun the simple-rule check and relevant exact/oracle/bound comparison at each newly covered regime.
- When the algorithm changes, rerun the MES, regressions, the current expansion level, and all affected baselines.
- When the formal problem changes, end the current comparison epoch and rebaseline every method under the new version.
- Compare different problem versions only through a genuinely common physical or service quantity, with the version change explicit.

## Scenario, Simulator, Or Trace Evidence

When the paper contributes a scenario generator, simulator, or trace, record its task definition, source or generation process, parameter applicability range, development and locked evaluation settings, metrics, baseline suite, leakage checks, difficulty coverage, expert or standards validation, license, and maintenance plan. Evaluate it as an evidence artifact; do not require an algorithmic contribution when none is intended.

## Minimum Convincing Package

For a communication optimization paper, normally require:

1. main comparison against close, strong, simple-rule, and exact/oracle/bound references where applicable;
2. mechanism evidence or a qualifying formal result;
3. parameter-range, stress, and boundary coverage;
4. feasibility, failure, and limitation analysis;
5. reproducibility details and versioned settings.

If this package cannot support the intended conclusion, narrow the conclusion and applicability range before adding weaker experiments.
