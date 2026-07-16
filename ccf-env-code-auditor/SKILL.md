---
name: ccf-env-code-auditor
description: "Audit a communication paper scenario, its minimum viable version (MVP), and environment code. Use for authoritative-version checks, design-to-code traceability, paper-to-MVP consistency, objective/constraint/state/action semantics, feasibility, invariants, algorithm-facing observations and diagnostics, tunable-rule behavior, 场景代码审查, 数学模型与代码一致性, MVP核验, tradeoff检查. Do not design algorithms, judge algorithm performance, or replace scenario design."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Environment Code Auditor

## Invocation Boundary

- **Use:** the primary object is the paper-scenario contract, scenario MVP, environment implementation, executed environment behavior, or algorithm-facing environment information.
- **Route elsewhere:** scenario formulation belongs to `ccf-env-design`; algorithm mechanism and performance belong to the algorithm skills.

## Core Rule

Audit every environment version with the same ordered protocol. Establish bidirectional evidence:

```text
scenario/model item -> code symbol -> executed path -> independently observed behavior
code behavior -> authorized model item or necessary implementation detail
```

Code presence, names, comments, and configuration fields are declarations, not behavioral evidence. Use the complete scenario MVP for acceptance, while small controlled cases support semantic checks. Apply this same protocol after environment fields are added for an algorithm.

## Modes

- `static-trace`: map the scenario and mathematical model into code.
- `executable-audit`: verify the complete scenario MVP through execution.
- `repair`: patch a confirmed environment-code defect and rerun affected checks.
- `acceptance-gate`: return the environment verdict and handoff evidence.

## Ordered Audit Gates

1. **Authority gate:** identify the paper-scenario spec, scenario MVP, equation version, code revision, entry point, configuration, seeds, units, time indexing, and information pattern; resolve conflicts before continuing.
2. **Design-contract gate:** verify that the accepted background, causal problem, scientific question, mathematical model, paper-to-MVP relation, complexity rationale, and algorithm-information contract are complete and internally consistent.
3. **Traceability gate:** map parameters, exogenous state, observations, algorithm-facing fields, decisions/actions, objective terms, constraints, transitions, randomness, initialization, termination, and metrics; reverse-trace behavior that affects them.
4. **Semantic-correctness gate:** verify objective direction and aggregation, constraint direction and enforcement, units, indexing, update order, action domains, state/observation separation, information timing, randomness, and metrics.
5. **Independent-execution gate:** run deterministic replay, independent objective/constraint/resource accounting, trace-wide invariants, controlled interventions, boundary configurations, repeated seeds, and full-load checks on the complete scenario MVP.
6. **Optimization-fidelity gate:** verify that actions remain effective, the planned decision space and coupling are preserved, objective terms vary as designed, constraints can bind, and feasibility is independently observable.
7. **Tradeoff gate:** run representative fixed, domain, greedy/myopic, decoupled, tuned, and random-feasible policies with equal information and declared tuning controls; verify that behavior exposes the intended scientific tradeoff.
8. **Acceptance gate:** issue `pass`, `conditional`, or `fail` from the combined design, trace, semantic, execution, optimization, and tradeoff evidence.

Load `references/audit-protocol.md` before running the gates. Keep detailed matrices internal unless requested.

## Workflow

1. Inventory the authoritative design, MVP, code, tests, commands, configurations, seeds, and traces.
2. Run the Ordered Audit Gates in sequence; stop executable conclusions when authority or design-contract evidence is unresolved.
3. Classify findings as `blocker`, `major`, `minor`, or `note` with `file:line` and decisive execution evidence.
4. When repair is authorized, patch the smallest confirmed environment-code defect, add a regression, and rerun all dependent gates.
5. Return accepted environment evidence to `ccf-algorithm-designer` or failure evidence to `ccf-experiment-debugger`.

## Output Contract

```text
Verdict: pass / conditional / fail
Authority status:
Design-contract finding:
Model-to-code findings:
Semantic and independent-execution findings:
Optimization and tradeoff findings:
Minimal environment fix and reruns:
Next owner:
```

Missing evidence is `not demonstrated`; contradictions and failed checks are `incorrect`.

## Reference

- `references/audit-protocol.md`: traceability schema, semantic checks, complete-MVP execution, and tunable-rule protocol.
