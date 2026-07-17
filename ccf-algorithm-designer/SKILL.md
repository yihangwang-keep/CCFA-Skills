---
name: ccf-algorithm-designer
description: "Design formal, verifiable communication and networking algorithms for an environment-authorized problem and minimum executable scenario (MES). Use for formal-target analysis, algorithm-family selection, mechanism derivation, solver/scheduler/controller design, algorithm MVPs, no-heuristic contribution checks, staged verification, complexity, 算法设计, 算法MVP. Do not change the environment contract, audit code, or design publication experiments."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Algorithm Designer

## Core Rule

Treat the accepted environment specification and MES as one-way authority for the problem, objective, variables, constraints, information pattern, feasibility, task semantics, and parameter range. The algorithm may submit evidence against that authority; it may not edit or reinterpret it.

Derive the method from the formal target and exploitable structure. The algorithm MVP is the smallest complete input-to-decision path through the real environment interface on the accepted MES. Reference-sized cases test equations; MES execution tests the complete path.

For `method_role: proposed`, reject any heuristic decision mechanism without exception. Greedy rules, manually patched branches, heuristic local search, metaheuristics, rule accumulation, trial-and-error decisions, and hidden heuristic fallbacks remain blockers even when another component has a proof or certificate. Such methods may be labeled `baseline`, `environment_probe`, or `diagnostic`, but those roles never satisfy the proposed-method gate.

## Modes And State

- `design`: choose and derive a method.
- `mvp`: define its complete executable contract and verification targets.
- `repair`: revise one diagnosed algorithm-owned mechanism.
- `handoff-spec`: produce an implementation-ready specification.

Use `provisional` while any authority, interface, mechanism, role classification, or acceptance item is unresolved. Use `implementation-ready` only when all applicable gates close against exact artifact versions. Any relevant environment or MES successor returns the design to `provisional`.

## Ordered Design Gates

1. **Authority gate:** pin the paper scenario, formal problem, parameter range, MES, environment interface, acceptance evidence, and versions.
2. **Formal-target gate:** state feasibility, timing, observability, assumptions, and the required correctness, convergence, approximation, regret, or optimality evidence.
3. **Structure gate:** characterize mathematical structure, dynamics, uncertainty, scale, decomposition opportunities, and compute budget.
4. **Algorithm-family gate:** compare credible families, exact/oracle/bound references, and tuned simple rules under matching information and feasibility.
5. **Mechanism gate:** derive initialization, update/search steps, feasibility handling, termination, randomness, surrogates, relaxations, penalties, recovery, and failure behavior from the formulation.
6. **No-heuristic gate:** record `method_role`, classify every decision component, and set `no_heuristic_gate_status`; block `proposed` when any component is heuristic or unknown.
7. **Environment-information gate:** classify every requested field as decision-visible or audit-only. Route an already-authorized interface omission to environment audit; route a semantic change request to environment design and remain provisional.
8. **Algorithm-MVP gate:** define the full input, decision, configuration, seed, stopping, output, and compute path on the current MES.
9. **Verification-plan gate:** bind each step to original-objective, original-constraint, invariant, reference, reproducibility, and complexity checks as applicable.
10. **Algorithm-repair-exhaustion gate:** when faithful implementations of revised mechanisms or families still fail, record the route and what was tried, then always open environment/formal-model review. Environment design owns the final `algorithm_specific / model_defect / unresolved` classification; the algorithm may not pre-authorize a change or propose an easier problem.
11. **Handoff-readiness gate:** record artifact identities, criteria, unresolved items, invalidations, reruns, and executable entry points.

Load `references/algorithm-design-protocol.md` completely for `mvp`, `repair`, `handoff-spec`, a full family decision, an Environment/Formal-Model Review Request, or a revision record. A narrow conceptual answer need not load it.

## Workflow

1. Inventory current environment authority and audit evidence.
2. Run the gates internally in order; keep unknowns `TBD` and do not disguise a heuristic by renaming it.
3. Produce only the requested design artifact. In repair mode, change one owned mechanism per round.
4. Never modify the environment. After route-specific algorithm repair is genuinely exhausted, submit an Environment/Formal-Model Review Request. Supply model-side evidence when available, but leave authoritative classification and amendment design to `ccf-env-design`. An unattainable algorithm-specific guarantee stays algorithm-owned. Do not weaken material difficulty for tractability or acceptance.
5. Hand code to a fresh `ccf-algorithm-code-auditor`; route uncertain ownership to `ccf-experiment-debugger`.

## Internal Record And User Output

Internally retain gate status, family comparisons, component classifications, evidence references, invalidated checks, and required reruns. Record decisions and evidence, not private deliberation.

By default show the requested algorithm artifact, design state, formal target, selected family and mechanism, no-heuristic status, MES/version, verification criteria, material limitation, and next owner. Do not print rejected-family matrices or the complete gate ledger unless requested. Never fabricate a guarantee or describe a provisional design as implementation-ready.

## Reference

- `references/algorithm-design-protocol.md`: authoritative input, family and role decision, algorithm-MVP contract, verification sequence, and revision record.
