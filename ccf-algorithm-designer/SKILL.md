---
name: ccf-algorithm-designer
description: "Design formal, verifiable communication and networking algorithms for an environment-authorized paper problem and scenario minimum viable version (MVP). Use for optimization-target analysis, algorithm-family selection, mechanism derivation, decomposition, solver/scheduler/controller design, algorithm MVPs, staged verification targets, complexity analysis, 算法设计, 算法MVP, 最小可行版本. Do not change the scenario contract, audit implementation code, or design publication experiments."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Algorithm Designer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Keep algorithm design separate from environment formulation, environment-code audit, algorithm-code audit, and experiment evidence design.

Treat unpublished formulations, algorithms, code, and results as private user data.

## Core Rule

Treat the accepted environment specification as the one-way authority for the scientific problem, objective, decision variables, constraints, information pattern, feasibility meaning, task-causal semantics, paper parameter range, and scenario MVP. The algorithm may challenge that authority with evidence, but it must not edit or silently reinterpret it.

First establish the solution target and exploitable mathematical structure, then select the least complex credible algorithm family, derive every mechanism from that structure, define the algorithm MVP, and attach a falsifiable verification target to every implementation step. A surrogate objective, relaxation, penalty, decomposition, or bound may guide computation, but the accepted objective and constraints remain the final evaluation semantics.

The algorithm MVP is the smallest complete path through the accepted environment interface that solves the scenario MVP. Small reference cases verify individual equations; end-to-end acceptance uses the complete scenario MVP. When evidence motivates a change, update the algorithm specification and rerun its dependent checks.

## Modes

- `design`: select and derive the algorithm.
- `mvp`: specify the smallest complete implementation and verification targets.
- `repair`: revise a diagnosed algorithm mechanism and update dependent checks.
- `handoff-spec`: produce an implementation-ready algorithm specification.

## Design State

- `provisional`: explore structure, candidate families, or mechanisms while an authority version, environment verdict, interface, assumption, or acceptance criterion remains unresolved. Mark affected items `TBD`; do not hand the design to implementation as accepted.
- `implementation-ready`: pin an accepted environment version and interface, close every applicable design gate, define executable verification criteria, and leave no material `TBD` that changes the mechanism or evaluation semantics.

An environment version change returns every dependent algorithm design to `provisional`. Do not reuse an implementation-ready status across different objective, constraint, information-pattern, feasibility, task-causal, parameter-range, or scenario-MVP versions.

## Ordered Design Gates

1. **Authority gate:** identify the accepted paper problem, paper parameter range, scenario MVP, environment version, objective, constraints, decision variables, information pattern, feasibility meaning, task-causal semantics, and environment verdict.
2. **Formal-target gate:** state the solution target, feasibility semantics, online/offline timing, observability, assumptions, and required correctness, convergence, approximation, regret, or optimality evidence.
3. **Structure gate:** characterize convexity/nonconvexity, combinatorial structure, decomposition opportunities, dynamics, uncertainty, scale, and computational budget.
4. **Algorithm-family gate:** compare credible families and tuned simple rules against the formal target, assumptions, information availability, complexity, and exact/oracle/bound reference; record the selection reason.
5. **Mechanism gate:** derive initialization, update/search steps, feasibility handling, termination, randomness, and each component's role from the formulation. Identify every surrogate, relaxation, penalty, decomposition, recovery step, and its relationship to the original problem.
6. **Environment-information gate:** state any additional observations, masks, residuals, objective components, or traces needed, including meaning, unit, time index, and availability time. Separate algorithm-visible information from audit-only diagnostics. If the requested field is already authorized by the information pattern, route the interface addition through `ccf-env-code-auditor`; otherwise submit an Environment Amendment Request to the environment owner and keep the design provisional.
7. **Algorithm-MVP gate:** define the complete input-to-decision path, configuration, seed behavior, stopping rule, output, and computational target on the scenario MVP.
8. **Verification-plan gate:** define hand-computable, exact/oracle/bound, original-objective, original-constraint-residual, invariant, one-step, convergence/correctness, reproducibility, simple-rule, and complexity checks as applicable.
9. **Handoff-readiness gate:** record authoritative artifact versions, design state, acceptance criteria, unresolved assumptions, invalidated checks, required reruns, and the implementation/audit commands or entry points.

Read `references/algorithm-design-protocol.md` completely for `mvp`, `repair`, or `handoff-spec`, and whenever a full family decision, Environment Amendment Request, or revision ledger is required. Do not load it for a narrow conceptual answer that does not produce or revise an algorithm artifact.

## Workflow

1. Inventory the accepted environment specification, environment-audit evidence, and available algorithm artifacts with exact versions.
2. Run the Ordered Design Gates internally in sequence. Resolve authority, formal-target, or environment-information gaps before treating the algorithm MVP as implementation-ready.
3. Use literature evidence when current algorithm families, assumptions, or references determine the selection.
4. Produce the requested algorithm specification, MVP, and verification plan with unknowns marked `TBD`. In repair mode, change one owned mechanism at a time so the resulting evidence remains attributable.
5. Never modify the environment from this skill. Submit an Environment Amendment Request only when independent evidence shows that algorithm-only repair is insufficient; the environment owner decides whether a new environment version is justified.
6. Hand implementation evidence to a fresh, independent `ccf-algorithm-code-auditor`; send uncertain ownership to `ccf-experiment-debugger`.
7. If an accepted environment amendment creates a new version, close the current design epoch, invalidate dependent algorithm specifications, implementations, audits, comparisons, and results, then rerun the gates against the new authority.

## Working Evidence Ledger

Keep detailed gate decisions, family comparisons, traceability, and invalidation state in a working ledger rather than printing them by default:

```yaml
authority_versions:
design_state: provisional | implementation-ready
gate:
status: pass | conditional | fail | not_applicable
evidence_refs: []
decisive_finding:
owner:
invalidated_checks: []
required_reruns: []
```

Record verdicts and evidence references, not private deliberation.

## User-Visible Output

Return the requested algorithm artifact, the current design state, decisive supporting evidence, material unresolved items, and the next owner. Do not expose the full gate ledger, every rejected family, or detailed matrices unless the user requests a full audit or handoff record.

For an implementation-ready handoff, include:

```text
Authority and formal target:
Problem structure:
Algorithm-family decision:
Derived mechanism:
Required environment information:
Algorithm MVP:
Verification plan and acceptance criteria:
Implementation handoff:
```

Do not fabricate convergence, optimality, runtime, feasibility, or performance evidence. Do not describe a provisional design as implementation-ready.

## Reference

- `references/algorithm-design-protocol.md`: algorithm-family decision, MVP contract, verification sequence, and revision record.
