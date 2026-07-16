---
name: ccf-algorithm-code-auditor
description: "Audit and repair algorithm MVP implementations against an accepted formal problem, scenario MVP, environment contract, and algorithm specification. Use for authoritative-version checks, design-to-code traceability, solver/controller/policy semantics, feasibility, convergence, exact/oracle/bound comparison, algorithm-MVP validation, 算法代码审查, 算法验证, 求解器实现核验, MVP验证. Do not redesign the environment, choose the initial algorithm, or design publication experiments."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Algorithm Code Auditor

## Invocation Boundary

- **Use:** the primary object is the algorithm specification, implementation, executed solver/controller/policy behavior, or algorithm-MVP acceptance evidence.
- **Route elsewhere:** environment behavior belongs to `ccf-env-code-auditor`; initial algorithm design belongs to `ccf-algorithm-designer`.

## Core Rule

Audit the implementation against the accepted algorithm design through bidirectional evidence:

```text
formal target/algorithm step -> code symbol -> executed path -> independent check
executed behavior -> authorized algorithm step or necessary implementation detail
```

Use small cases for semantic and reference checks, then decide acceptance on the complete scenario MVP. After a confirmed repair, rerun every gate that depends on the changed behavior.

## Modes

- `static-trace`: map the algorithm specification into code.
- `mvp-audit`: verify the complete algorithm MVP.
- `repair`: patch a confirmed algorithm-code defect and rerun affected checks.
- `acceptance-gate`: return the algorithm verdict and handoff evidence.

## Ordered Audit Gates

1. **Authority gate:** identify the paper formulation, scenario MVP, environment version/verdict, algorithm specification, code revision, configuration, dependencies, seeds, metrics, and acceptance criteria.
2. **Environment-contract gate:** confirm that algorithm inputs, outputs, action domains, feasibility signals, and information timing match the accepted environment interface.
3. **Design-contract gate:** verify that the formal target, assumptions, selected family, derived mechanism, MVP path, termination, complexity target, and verification plan are complete and internally consistent.
4. **Traceability gate:** map initialization, preprocessing, decisions, every update/search step, feasibility handling, objective evaluation, randomness, termination, checkpoints, solution extraction, and metrics; reverse-trace behavior that changes them.
5. **Semantic-correctness gate:** independently verify equations, signs, units, indices, update order, masks, gradients where applicable, residuals, stopping rules, and extracted decisions.
6. **Reference gate:** compare hand-computable or small instances with the declared exact solver, enumeration, oracle, certified bound, relaxation, theorem, or other analytical target; state the certification scope.
7. **Independent-MVP gate:** run the complete algorithm MVP on the scenario MVP and verify feasibility, correctness/convergence evidence, numerical stability, reproducibility, objective values, and runtime/space against predeclared criteria.
8. **Acceptance gate:** issue `pass`, `conditional`, or `fail` from the combined authority, contract, trace, semantic, reference, and MVP evidence.

Load `references/algorithm-audit-protocol.md` before running the gates.

## Workflow

1. Inventory the authoritative specifications, audit verdicts, code, tests, commands, reference tools, configurations, seeds, and traces.
2. Run the Ordered Audit Gates in sequence; stop acceptance conclusions when authority, environment, or design contracts are unresolved.
3. Report findings with `file:line`, decisive execution evidence, severity, and affected checks.
4. When repair is authorized, patch the smallest confirmed algorithm-code defect, add a regression, and rerun dependent gates.
5. Return mechanism failures to `ccf-algorithm-designer`, environment failures to `ccf-env-code-auditor`, uncertain ownership to `ccf-experiment-debugger`, and accepted MVP evidence to `ccf-experiment-designer`.

## Output Contract

```text
Verdict: pass / conditional / fail
Authority and environment-contract status:
Algorithm-design contract status:
Algorithm-to-code findings:
Semantic and reference findings:
Independent MVP findings:
Minimal algorithm-code fix and reruns:
Next owner:
```

Missing evidence is `not demonstrated`; contradictions and failed checks are `incorrect`.

## Reference

- `references/algorithm-audit-protocol.md`: traceability, executable checks, acceptance rules, and revision consistency.
