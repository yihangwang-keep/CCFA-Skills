---
name: ccf-algorithm-code-auditor
description: "Audit and repair communication and networking algorithm implementations against an accepted formal problem, frozen minimum executable scenario (MES) anchor, complexity stages, environment contract, and algorithm specification. Use for authoritative-version checks, design-to-code traceability, solver/scheduler/controller semantics, feasibility, convergence, exact/oracle/bound comparison, algorithm validation, 算法代码审查, 算法验证, 求解器实现核验. Do not redesign the environment, choose the initial algorithm, or design publication experiments."
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

- **Use:** the primary object is the algorithm specification, implementation, executed solver/scheduler/controller behavior, or algorithm acceptance evidence on the accepted minimum executable scenario (MES).
- **Route elsewhere:** environment behavior belongs to ccf-env-code-auditor; initial algorithm design belongs to ccf-algorithm-designer.

## Core Rule

Audit the implementation against an implementation-ready algorithm design, the
environment-authorized formal problem, and the frozen anchor MES through
bidirectional evidence:

~~~text
formal target/algorithm step -> code symbol -> executed path -> independent check
executed behavior -> authorized algorithm step or necessary implementation detail
~~~

The environment remains the authority for objective, decision variables,
constraints, information pattern, feasibility meaning, task-causal semantics,
paper parameter range, anchor MES, and current complexity stage. Audit algorithm code against that contract; do
not alter the environment or accept an algorithm-side reinterpretation.

Consume the initial anchor-only L2/`algorithmic_need` result from the environment auditor. For a later complexity stage, audit the upgraded algorithm on the stage and anchor regression while inheriting that result; this auditor does not rerun environment heuristic probes.

Use small cases for semantic and reference checks, then decide acceptance on the
complete MES. Bind every verdict to exact authority, specification, artifact
digests, configuration, and evidence versions. After a confirmed repair, rerun
every gate that depends on the changed behavior.

## Modes

- static-trace: map the algorithm specification into code.
- mvp-audit: verify the complete algorithm path on the MES.
- repair: coordinate an authorized algorithm-code repair and verify a new artifact set.
- acceptance-gate: return the algorithm verdict and handoff evidence.

## Ordered Audit Gates

1. **Authority gate:** identify the paper formulation, frozen anchor MES, complexity stage, environment version/verdict, algorithm specification, method role, mechanism classification, artifact set, configuration, dependencies, seeds, metrics, and acceptance criteria.
2. **Environment-contract gate:** confirm that algorithm inputs, outputs, action domains, feasibility signals, information timing, and interface version match the accepted environment contract; separate algorithm-visible information from audit-only diagnostics.
3. **Design-contract gate:** verify that the design is implementation-ready and that the formal target, assumptions, selected family, derived mechanism, MES path, termination, complexity target, original-problem evaluation semantics, verification plan, method role, and mechanism classification are complete and internally consistent.
4. **Traceability gate:** map initialization, preprocessing, decisions, every update/search step, feasibility handling, surrogate or relaxation, recovery, original-objective evaluation, original-constraint checks, randomness, termination, solution extraction, and metrics; reverse-trace behavior that changes them.
5. **Semantic-correctness gate:** independently verify equations, signs, units, indices, update order, masks, gradients where applicable, residuals, stopping rules, extracted decisions, and failure behavior without hidden fallback.
6. **Proposed-method eligibility gate:** when method_role is proposed, reject any heuristic decision mechanism, including a hidden heuristic fallback or clipping path, as a blocker. Heuristic and simple rules are permitted only for explicitly labelled baseline, reference, diagnostic, or environment-probe roles.
7. **Reference gate:** compare hand-computable or small instances with the declared exact solver, enumeration, oracle, certified bound, relaxation, theorem, or other analytical target; state the certification scope and evaluate recovered decisions under the original objective and constraints.
8. **Independent-MES gate:** run the complete algorithm path on the frozen anchor MES and, when a complexity stage is active, the new stage; verify anchor regression, feasibility, correctness/convergence evidence, numerical stability, reproducibility, original objective values, declared comparison conditions, and runtime/space against predeclared criteria.
9. **Acceptance gate:** issue pass, conditional, or fail from the combined authority, contract, trace, semantic, reference, MES, and native implementation-review evidence. Set joint-ready only when the environment is current and valid and all applicable algorithm gates are accepted under the same artifact set.

Missing evidence is not demonstrated; contradictions and failed checks are incorrect. A proposed-method heuristic violation is never downgraded to a minor finding.

## Native Implementation Review

For a full static trace, MES audit, repair verification, debugger-round closure, or acceptance gate, load ../ccf-common/references/implementation-review-protocol.md. Freeze one candidate artifact set with content digests and dispatch, in parallel, fresh read-only domain-contract-fidelity and implementation-assurance reviewers. The algorithm domain profile checks environment-contract and algorithm-specification fidelity, all declared steps, feasibility/recovery, original-objective evaluation, termination/extraction, reference scope, and MES behavior. The assurance reviewer checks independent reference/checker paths, failure detectability, reproducibility, numerical/resource safety, and hidden fallback or information leakage.

The proposed-method eligibility gate is owned by this auditor's domain profile. For method_role proposed, any heuristic decision path or hidden heuristic fallback emits blocker ALG-CONTRACT-NH-001. Environment-probe/baseline/reference/diagnostic roles may use heuristics when labelled and fairly evaluated. Reviewers only report; they never repair. An implementation owner cannot review the artifact set it changed. Missing reviewer capability or missing digest is not_run/conditional and blocks acceptance; prior reports become stale after any artifact change.

## Workflow

1. Inventory authoritative specifications, current environment verdict, MES, code, tests, commands, reference tools, configurations, seeds, and raw traces with exact artifact digests.
2. Start a fresh native two-axis review from those artifacts and run the Ordered Audit Gates; do not inherit an implementer's or designer's pass status as evidence.
3. Report each finding with file:line, decisive evidence, severity, affected checks, owner, and required reruns; keep axis reports separate.
4. When repair is authorized, route one smallest confirmed algorithm-code delta to its implementation owner, preserve the old artifact set, create a new candidate digest, and rerun dependent gates. The repairer cannot sign the new review.
5. Never repair the environment or formal problem from this skill. Route environment-code defects to `ccf-env-code-auditor` and mechanism/no-heuristic failures to `ccf-algorithm-designer`. When code fidelity is current and the route-specific repair ledger is exhausted, always submit it through `ccf-experiment-debugger` for environment/formal-model review. Environment design classifies the cause; this auditor cannot require or approve an easier problem.
6. For a `complexity_expansion`, preserve the anchor audit and rerun the anchor plus the new stage; invalidate only stage-dependent comparisons and results. A legacy/exception MES successor preserves old evidence for its parent authority tuple but cannot establish successor acceptance. For a formal amendment or another semantic environment change, start a new evidence epoch, use a new candidate MES, and rebaseline the complete algorithm audit, comparisons, and results.
7. Send current joint-ready evidence to ccf-experiment-designer only after the native review axes and all algorithm gates are current and accepted.

## Working Evidence Ledger

Keep artifact manifests, traceability, method role and component classification, gate evidence, native-review axis reports, invalidations, and reruns in the internal records defined by the two references. Record evidence and verdicts, not private deliberation. A verdict applies only when all artifact digests and authority versions remain current.

## User-Visible Output

Lead with material findings, ordered by severity within each axis. Do not merge
or rerank the axes:

~~~text
Verdict: pass / conditional / fail / stale; joint-ready: yes / no
Reviewed artifact set and authority/environment versions:
Domain contract fidelity: status and findings
Implementation assurance: status and findings
Proposed-method eligibility: pass / blocker / not_applicable
Semantic, reference, and MES evidence:
Minimal algorithm-code fix, invalidated checks, and reruns:
Next owner:
~~~

Do not print the full gate ledger or traceability matrices unless requested.

## Conditional References

- references/algorithm-audit-protocol.md: traceability, executable checks, role-aware eligibility, acceptance rules, and artifact invalidation.
- ../ccf-common/references/implementation-review-protocol.md: native two-axis dispatch, read-only reviewer contract, finding schema, stale rules, and output projection.
