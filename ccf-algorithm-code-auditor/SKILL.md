---
name: ccf-algorithm-code-auditor
description: "Audit and repair communication and networking algorithm MVP implementations against an accepted formal problem, scenario MVP, environment contract, and algorithm specification. Use for authoritative-version checks, design-to-code traceability, solver/scheduler/controller semantics, feasibility, convergence, exact/oracle/bound comparison, algorithm-MVP validation, 算法代码审查, 算法验证, 求解器实现核验, MVP验证. Do not redesign the environment, choose the initial algorithm, or design publication experiments."
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

- **Use:** the primary object is the algorithm specification, implementation, executed solver/scheduler/controller behavior, or algorithm-MVP acceptance evidence.
- **Route elsewhere:** environment behavior belongs to `ccf-env-code-auditor`; initial algorithm design belongs to `ccf-algorithm-designer`.

## Core Rule

Audit the implementation against an implementation-ready algorithm design and its pinned, environment-authorized formal problem through bidirectional evidence:

```text
formal target/algorithm step -> code symbol -> executed path -> independent check
executed behavior -> authorized algorithm step or necessary implementation detail
```

The environment remains the authority for the objective, decision variables, constraints, information pattern, feasibility meaning, task-causal semantics, paper parameter range, and scenario MVP. Audit algorithm code against that contract; do not alter the environment or accept an algorithm-side reinterpretation.

Use small cases for semantic and reference checks, then decide acceptance on the complete scenario MVP. Bind every verdict to exact authority, specification, code, configuration, and evidence versions. After a confirmed repair, rerun every gate that depends on the changed behavior.

## Modes

- `static-trace`: map the algorithm specification into code.
- `mvp-audit`: verify the complete algorithm MVP.
- `repair`: patch a confirmed algorithm-code defect and rerun affected checks.
- `acceptance-gate`: return the algorithm verdict and handoff evidence.

## Ordered Audit Gates

1. **Authority gate:** identify the paper formulation, scenario MVP, environment version/verdict, algorithm specification, code revision, configuration, dependencies, seeds, metrics, and acceptance criteria.
2. **Environment-contract gate:** confirm that algorithm inputs, outputs, action domains, feasibility signals, information timing, and interface version match the accepted environment contract; separate algorithm-visible information from audit-only diagnostics.
3. **Design-contract gate:** verify that the design is `implementation-ready` and that the formal target, assumptions, selected family, derived mechanism, MVP path, termination, complexity target, original-problem evaluation semantics, and verification plan are complete and internally consistent.
4. **Traceability gate:** map initialization, preprocessing, decisions, every update/search step, feasibility handling, surrogate or relaxation, recovery, original-objective evaluation, original-constraint checks, randomness, termination, checkpoints, solution extraction, and metrics; reverse-trace behavior that changes them.
5. **Semantic-correctness gate:** independently verify equations, signs, units, indices, update order, masks, gradients where applicable, residuals, stopping rules, extracted decisions, and failure behavior without hidden fallback.
6. **Reference gate:** compare hand-computable or small instances with the declared exact solver, enumeration, oracle, certified bound, relaxation, theorem, or other analytical target; state the certification scope and evaluate recovered decisions under the original objective and constraints.
7. **Independent-MVP gate:** run the complete algorithm MVP on the scenario MVP and verify feasibility, correctness/convergence evidence, numerical stability, reproducibility, original objective values, tuned simple-rule comparisons, and runtime/space against predeclared criteria.
8. **Acceptance gate:** issue `pass`, `conditional`, or `fail` from the combined authority, contract, trace, semantic, reference, and MVP evidence. Set `joint-ready` only when the environment is current and valid and the algorithm specification, implementation, reference checks, and complete MVP are accepted under the same versions.

Read `references/algorithm-audit-protocol.md` completely for a full `static-trace`, `mvp-audit`, `repair`, or `acceptance-gate`. Do not load it for a narrow file-local question that does not request an audit verdict.

## Workflow

1. Inventory the authoritative specifications, audit verdicts, code, tests, commands, reference tools, configurations, seeds, and raw traces with exact versions.
2. Start a fresh independent audit from those artifacts. Do not inherit the implementer's or designer's pass status as evidence. Run the Ordered Audit Gates internally in sequence; stop acceptance conclusions when authority, environment, or design contracts are unresolved.
3. Report findings with `file:line`, decisive execution evidence, severity, affected checks, and required reruns.
4. When repair is authorized, patch one smallest confirmed algorithm-code defect, add a regression, and rerun dependent gates. A repair pass cannot issue the final `pass`; audit the updated revision in a fresh independent pass.
5. Never repair the environment or formal problem from this skill. Route confirmed environment-code defects to `ccf-env-code-auditor`; for a possible formal environment defect, record independent evidence and submit an Environment Amendment Request to the environment owner. Return mechanism failures to `ccf-algorithm-designer` and uncertain ownership to `ccf-experiment-debugger`.
6. Treat any accepted environment version change as a new audit epoch: invalidate the prior algorithm verdict, comparisons, and results; rerun authority, contracts, traceability, semantic, reference, and complete-MVP checks against the new version.
7. Send current `joint-ready` MVP evidence to `ccf-experiment-designer`. Only at a debugger checkpoint or when the user explicitly requests repository-diff review, hand off the fixed point and accepted specification to a fresh `$code-review` agent. Do not invoke it for a domain-only audit.

## Working Evidence Ledger

Keep the full gate record and traceability matrices internal unless the user explicitly requests them:

```yaml
authority_versions:
reviewed_code_revision:
gate:
status: declared | wired | verified | contradicted | untestable
evidence_refs: []
decisive_finding:
owner:
invalidated_checks: []
required_reruns: []
```

Record evidence and verdicts, not private deliberation.

## User-Visible Output

Lead with material findings, ordered by severity. Then give the version-bound verdict, decisive environment/design-contract status, independent execution evidence, repairs and reruns, unresolved items, and next owner. Do not print the full gate ledger or traceability matrices unless requested.

For a full audit report, use:

```text
Verdict: pass / conditional / fail; joint-ready: yes / no
Authority and environment-contract status:
Algorithm-design contract status:
Algorithm-to-code findings:
Semantic and reference findings:
Independent MVP findings:
Minimal algorithm-code fix and reruns:
Next owner:
```

Missing evidence is `not demonstrated`; contradictions and failed checks are `incorrect`. A verdict applies only when its reviewed code revision and authority versions match the current artifacts.

## Reference

- `references/algorithm-audit-protocol.md`: traceability, executable checks, acceptance rules, and revision consistency.
