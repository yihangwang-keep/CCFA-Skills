---
name: ccf-experiment-env-code-auditor
description: "Audit a communication scenario's problem and plan before checking the complete environment code implementation. Use for plan reasonableness, formulation-to-code traceability, objective/constraint/state/action checks, simulator semantics, feasibility, invariants, and checking whether the scenario forces tuned heuristics to sacrifice one tradeoff side when improving the other, 场景问题与原因, 计划合理性, 场景代码审查, 数学模型与代码一致性, tradeoff检查, 目标函数与约束实现核验. Review only the current scenario plan, code, and execution evidence."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Experiment Env Code Auditor

## Core Rule

Audit in this order: identify the scenario problem and its causes; decide whether the plan reasonably models them without triviality or decorative complexity; only then verify the currently implemented target scenario code. Use its actual entity count, horizon, topology, partition/merge structure, workload, uncertainty, resource settings, and coupled decisions for every executable conclusion. As a simple hint, an effective implementation should force a heuristic to sacrifice one side of the intended tradeoff when improving the other. If a tuned heuristic handles both sides well, investigate which real scenario mechanism is absent, inactive, or implemented incorrectly.

Establish this bidirectional evidence chain:

```text
planned model item -> code symbol -> executed path -> observed behavior
code behavior -> planned model item or necessary implementation detail
```

Names, comments, configuration fields, and code presence are not correctness evidence. Require an executed path and a full-scenario behavioral check. Treat the plan, code, configuration, traces, and audit findings as private user data.

## Modes

- `static-trace`: map every planned model item to code and find unexplained code behavior.
- `executable-audit`: run the current complete scenario and verify its implemented semantics.
- `repair`: patch confirmed scenario-code defects when authorized and rerun the complete scenario.
- `acceptance-gate`: return whether the implemented scenario passes code-model consistency and tunable-rule tradeoff checks.

## Mandatory Gates

1. **Problem-and-cause gate:** state the implemented scenario's concrete problem, affected entities or task, observed consequence, and causal chain from communication conditions and decisions to that consequence.
2. **Plan-reasonableness gate:** verify that every planned objective term, variable, constraint, dynamic, uncertainty source, and coupling corresponds to the stated causes. Fail before code acceptance when the plan is causally unsupported or overloaded with inactive components.
3. **Authority:** identify the authoritative plan/equation version, code revision, entry point, configuration, seed handling, units, time indexing, and information pattern. Mark conflicts or missing definitions.
4. **Traceability:** map parameters, exogenous state, observations, decision variables/actions, objective terms, constraints, transitions, randomness, initialization, termination, and metrics. Classify each row as `implemented-correctly`, `present-but-wrong`, `missing`, `dead-code`, or `untestable`.
5. **Semantic correctness:** verify objective direction and aggregation, constraint direction and enforcement, units, indexing, update order, action domains, state/observation separation, random-process semantics, and reported metrics.
6. **Complete-scenario execution:** run deterministic replay, independent objective and constraint calculations, trace-wide invariants, controlled parameter/action interventions, boundary configurations, repeated seeds, and full-load checks on the current target scenario.
7. **Optimization fidelity:** verify that code preserves the planned decision space and coupling. Reject ignored or overwritten actions, leaked future information, hard-coded decisions, clipping or penalties that change the planned constraints, inactive objective terms, and constraints that cannot bind.
8. **Tunable-rule gate:** run representative fixed, domain-rule, greedy/myopic, decoupled, low-dimensional tuned, and random-feasible policies on the same complete scenario. Give them the same observations, feasibility rules, seeds, and declared tuning budget. Expect improvement on one tradeoff side to require a visible loss on the other. If a rule handles both sides well, check for inactive coupling, nonbinding constraints, ineffective dynamics/uncertainty, an easy parameter regime, or incorrect code.
9. **Environment acceptance:** pass only when the plan is reasonable, every material model item is traceable and behaviorally verified, scenario execution is reproducible, feasibility is independently observable, retained complexity affects decisions, planned coupling is active, and tuned rules do not already handle the intended tradeoff well.

Load `references/audit-protocol.md` before running the gates. Keep its matrices and checklists internal unless the user explicitly requests detailed evidence.

## Workflow

1. Inventory the authoritative model plan, scenario code, configuration files, entry points, existing tests, run commands, seeds, and generated traces.
2. Check the scenario problem, causal chain, plan assumptions, and why each planned component is necessary. If the plan is unreasonable, state the problem and cause before inspecting implementation fidelity.
3. Normalize a reasonable plan into atomic model items with symbol, meaning, unit, domain, time scale, equation, dependencies, and expected code behavior. Mark unspecified semantics as `untestable`; do not infer them from code.
4. Trace each item through configuration parsing, initialization, observation construction, action handling, transition, objective/reward, constraint handling, termination, and reporting. Reverse-trace every behavior that changes state, objective, feasibility, actions, or metrics.
5. Execute the current complete scenario with the actual configuration, seeds, and structural dimensions, then compare expected and observed behavior.
6. Independently recompute objective terms, resource accounting, state conservation, and constraint residuals from the produced full trace rather than trusting the environment's own summaries.
7. Run controlled interventions while retaining the current scenario structure. Change one parameter or action policy at a time and verify the expected effect on executed paths, states, objectives, constraints, and terminal outcomes.
8. Run the tunable-rule policy set under the same complete scenario and fair tuning/evaluation controls. If a rule handles both tradeoff sides well, find the scenario or implementation reason before accepting the environment.
9. Classify findings as `blocker`, `major`, `minor`, or `note`. If repair is authorized, patch only confirmed code defects, add a complete-scenario regression, and rerun every affected gate.
10. Return `pass`, `conditional`, or `fail`. Missing behavioral evidence is `not demonstrated`, not a pass; use `incorrect` only for a contradiction or failed check.

## Output Contract

Lead with actionable findings and cite `file:line` plus decisive execution evidence. Keep the default output to:

```text
Verdict: pass / conditional / fail
Scenario problem and causes:
Plan reasonableness:
Code implementation finding:
Tunable-rule finding:
Required fixes:
```

Do not emit detailed matrices or execution tables unless the user requests them. Mention unresolved items only when they change the verdict.

## References

- `references/audit-protocol.md`: load for the traceability schema, complete-scenario execution checks, and heuristic protocol.
