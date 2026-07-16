---
name: ccf-algorithm-designer
description: "Design formal, verifiable algorithms for an accepted paper problem and scenario minimum viable version (MVP). Use for optimization-target analysis, algorithm-family selection, mechanism derivation, decomposition, solver/controller/policy design, algorithm MVPs, staged verification targets, complexity analysis, 算法设计, 算法MVP, 最小可行版本. Do not redesign the scenario, audit implementation code, or design publication experiments."
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

Design the algorithm from an accepted formal problem and scenario MVP. First establish the solution target and exploitable mathematical structure, then select an algorithm family, derive its mechanism, define the algorithm MVP, and attach a falsifiable verification target to every implementation step.

The algorithm MVP is the smallest complete path through the accepted environment interface that solves the scenario MVP. Small reference cases verify individual equations; end-to-end acceptance uses the complete scenario MVP. When evidence motivates a change, update the algorithm specification and rerun its dependent checks.

## Modes

- `design`: select and derive the algorithm.
- `mvp`: specify the smallest complete implementation and verification targets.
- `repair`: revise a diagnosed algorithm mechanism and update dependent checks.
- `handoff-spec`: produce an implementation-ready algorithm specification.

## Ordered Design Gates

1. **Authority gate:** identify the accepted paper problem, scenario MVP, environment version, objective, constraints, decision variables, information pattern, and environment verdict.
2. **Formal-target gate:** state the solution target, feasibility semantics, online/offline timing, observability, assumptions, and required correctness, convergence, approximation, regret, or optimality evidence.
3. **Structure gate:** characterize convexity/nonconvexity, combinatorial structure, decomposition opportunities, dynamics, uncertainty, scale, and computational budget.
4. **Algorithm-family gate:** compare credible families against the formal target, assumptions, information availability, complexity, and verification reference; record the selection reason.
5. **Mechanism gate:** derive initialization, update/search steps, feasibility handling, termination, randomness, and each component's role from the formulation.
6. **Environment-information gate:** state any additional observations, masks, residuals, objective components, or traces needed; send environment changes through `ccf-env-code-auditor` before implementation acceptance.
7. **Algorithm-MVP gate:** define the complete input-to-decision path, configuration, seed behavior, stopping rule, output, and computational target on the scenario MVP.
8. **Verification-plan gate:** define hand-computable, exact/oracle/bound, objective, constraint-residual, invariant, one-step, convergence/correctness, reproducibility, and complexity checks as applicable.
9. **Handoff-readiness gate:** record authoritative artifact versions, acceptance criteria, unresolved assumptions, and the implementation/audit commands or entry points.

Load `references/algorithm-design-protocol.md` before producing an algorithm MVP specification.

## Workflow

1. Inventory the accepted environment specification, environment-audit evidence, and available algorithm artifacts.
2. Run the Ordered Design Gates in sequence. Resolve authority, formal-target, or environment-information gaps before treating the algorithm MVP as implementation-ready.
3. Use literature evidence when current algorithm families, assumptions, or references determine the selection.
4. Produce the algorithm specification, MVP, and verification plan with unknowns marked `TBD`.
5. Hand implementation evidence to `ccf-algorithm-code-auditor`; send uncertain failures to `ccf-experiment-debugger`.

## Adaptive Output Contract

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

Do not fabricate convergence, optimality, runtime, or performance evidence.

## Reference

- `references/algorithm-design-protocol.md`: algorithm-family decision, MVP contract, verification sequence, and revision record.
