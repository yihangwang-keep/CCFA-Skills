---
name: ccf-env-design
description: "Design and audit non-toy communication, wireless, networking, UAV, edge, IoT, vehicular, satellite, and mission-coupled optimization environments. Use for paper-scenario design, scenario background and causal problems, scientific questions, objective and constraint design, complexity balance, minimum viable versions (MVPs), algorithm information requirements, 场景设计, 论文场景, 最小可行版本, 目标函数, 约束建模, tradeoff审查. Do not design algorithms, validate environment code, invent results, or replace literature search."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Environment Design

## Core Rule

Design the paper scenario as a scientific and mathematical contract before algorithm work. Start from the communication task and causal problem, form one focused scientific question, and express it through decision variables, objective, constraints, information timing, dynamics, uncertainty, and feasibility semantics. Retain enough active coupling to require meaningful optimization while keeping every component attributable to the same problem.

After the paper scenario is stable, derive its minimum viable version (MVP) for the first reproducible end-to-end implementation. The MVP fixes only the parameters needed for one complete case and preserves the paper scenario's scientific question, objective, material constraints, decision coupling, information pattern, feasibility meaning, and causal tradeoff.

## Modes

- `design`: construct the paper scenario, formal optimization problem, and MVP.
- `audit`: judge an existing scenario plan for causal validity, complexity balance, and MVP consistency.
- `repair`: revise a confirmed scenario-design defect and update dependent contracts.
- `handoff-spec`: produce an environment specification for code audit and algorithm design.

## Ordered Design Gates

1. **Scenario-background gate:** define the communication context, actors, task or service need, why communication matters, and the abstraction boundary.
2. **Problem-and-cause gate:** state the concrete failure or lost value, affected entities, observed consequence, and causal chain from communication conditions and decisions to that consequence.
3. **Scientific-question gate:** state one focused research question, central tradeoff, and paper claim boundary.
4. **Mathematical-model gate:** define parameters, decision and state variables, objective, hard and soft constraints, information available at decision time, dynamics, uncertainty, and feasibility conditions.
5. **Model-traceability gate:** map every objective term, variable, constraint, dynamic, uncertainty source, and coupling to the scenario problem or scientific question.
6. **Coupling-and-complexity gate:** identify binding constraints and coupled decisions, then use tuned static, greedy, domain, and decoupled rules to confirm that the intended tradeoff is active and attributable.
7. **Paper-to-MVP gate:** derive the MVP, list fixed parameters, and verify that the formal problem and causal tradeoff are preserved.
8. **Algorithm-information gate:** specify observations and timing, decision/action interface, feasibility signals, objective components, trace diagnostics, units, seeds, and audit-only information needed for implementation and independent verification.
9. **Handoff-readiness gate:** record authoritative versions, unresolved items, expected environment checks, and the exact problem the algorithm must solve.

Load `references/communication-env-gates.md` for detailed communication-specific criteria and `references/env-spec-template.md` for a reusable specification.

## Workflow

1. Inventory the research idea, target domain, task driver, available scenario/code artifacts, and decision goal based on a specific research question.
2. Run the Ordered Design Gates in sequence. Resolve a failed earlier gate before relying on later mathematical or implementation conclusions.
3. Use literature evidence when domain ranges, formulation choices, or strongest simple rules require external support; follow CCFA handoff and privacy controls.
4. Produce the requested audit, repaired plan, or specification. Keep unknown values `TBD` and preserve version authority.
5. Hand the environment specification and MVP to `ccf-env-code-auditor`. After environment acceptance, hand the accepted problem to `ccf-algorithm-designer`.

If user ask to futher the env design, you need to find the true promblem in the current env design torwards to the vene goal and deepth the env design to the next level. And need to clearly consider the central scientific question, the new causal chain, the main tradeoff, the suggested mathematical extensions between the current scenario and the desired one, keep the objective function from inflating, the minimal viable scenario, and the scenario evidence that must be run.

## Adaptive Output Contract

```text
Verdict:
Scenario background and causal problem:
Scientific question and claim boundary:
Mathematical model:
Model-to-cause traceability:
Coupling and complexity finding:
Paper scenario to MVP:
Algorithm-required environment information:
Required changes and handoff:
```

Return the user's requested artifact first and keep internal gate detail concise unless a full audit is requested.

## References

- `references/communication-env-gates.md`: communication-specific realism, coupling, complexity, and paper-worthiness criteria.
- `references/env-spec-template.md`: paper-scenario, MVP, information-interface, and handoff schema.
