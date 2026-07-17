---
name: ccf-env-design
description: "Design or audit communication-domain paper scenarios, formal optimization problems, parameter applicability ranges, and scenario MVPs. Use for task causal chains, central tradeoffs, objectives, constraints, information patterns, feasibility meaning, complexity balance, 场景设计, 目标函数与约束, MVP核验. Do not design algorithms, validate environment code, invent results, or replace literature search."
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

The environment owns the problem semantics. Start from the communication task, identify the task causal chain and its causal bottleneck, state one focused scientific question and central tradeoff, and then define the formal optimization problem: variables, objective, constraints, dynamics, uncertainty, information pattern, and feasibility meaning. Every retained component must be attributable to that same problem.

Define the paper scenario and its parameter applicability range before deriving the scenario MVP. The scenario MVP fixes only the parameters needed for one reproducible end-to-end case. It must preserve the task causal chain, formal objective, material constraints, coupled decisions, information pattern, feasibility meaning, and central tradeoff.

The target venue may raise the required causal grounding, formal completeness, verification rigor, and evidence coverage. It is not a scientific reason to add variables, constraints, mechanisms, or difficult settings that do not follow from the task.

## Modes

- `design`: construct the paper scenario, formal optimization problem, parameter applicability range, and scenario MVP.
- `audit`: judge causal validity, complexity balance, applicability, and paper-scenario-to-MVP consistency.
- `repair`: revise a confirmed environment-design defect, version the change, and invalidate dependent evidence.
- `amendment-review`: decide whether algorithm-stage evidence justifies changing the environment contract.
- `handoff-spec`: produce the environment specification for code audit and algorithm design.

## Ordered Design Gates

1. **Scenario-background gate:** define the communication context, actors, task or service need, why communication matters, and the abstraction boundary.
2. **Task-causal-chain gate:** state the concrete failure or lost value, affected entities, observed consequence, causal bottleneck, and chain from communication conditions and decisions to the task outcome.
3. **Scientific-question gate:** state one focused research question, central tradeoff, supported conclusion, and applicability boundary.
4. **Formal-problem gate:** define parameters, decision and state variables, objective, hard and soft constraints, information available at decision time, dynamics, uncertainty, and feasibility meaning.
5. **Problem-traceability gate:** map every objective term, variable, constraint, dynamic, uncertainty source, and coupling to the task causal chain or scientific question.
6. **Coupling-and-complexity gate:** identify the causal bottleneck, binding constraints, and coupled decisions; use tuned static, greedy, domain, and decoupled rules to confirm that the central tradeoff is active and attributable.
7. **Paper-to-MVP gate:** define the parameter applicability range, derive the scenario MVP, list fixed parameters, and verify that the formal problem and central tradeoff are preserved.
8. **Algorithm-information gate:** specify decision-time observations, timing, decision interface, feasibility signals, objective components, trace diagnostics, units, seeds, unavailable information, and audit-only information.
9. **Handoff-readiness gate:** record authoritative versions, unresolved items, expected environment checks, the exact problem the algorithm must solve, `environment-valid`, algorithmic-need evidence, and interface completeness. Reserve `joint-ready` for downstream algorithm acceptance.

Resolve a failed earlier gate before relying on later mathematical, implementation, or readiness conclusions.

## Environment Authority And Amendments

Algorithm failure is diagnostic evidence, not permission to rewrite the objective, constraints, information pattern, feasibility meaning, or parameter applicability range. Algorithms may use an internal reformulation or surrogate, but final feasibility and performance remain defined by the authoritative environment contract.

An algorithm-stage change to that contract requires an evidence-backed environment amendment request. Review it against all five tests:

1. **Algorithm independence:** the defect remains under another credible solution method.
2. **Causal necessity:** task or communication evidence requires the change.
3. **Research-identity preservation:** the task or service outcome, scientific question, task causal chain, central tradeoff, and intended contribution type remain the same. A material formal-problem change that preserves them starts a rebaselined R1 version; changing any of them requires reframing.
4. **Information honesty:** the change does not expose future, hidden, or audit-only information at decision time.
5. **Method neutrality:** the change repairs the problem rather than favoring one method or restoring a preferred ranking.

An accepted R1 amendment creates a new environment version and ends the current evidence epoch as `rebaseline-required`; an R0 research-identity change ends it as `reframe`. Invalidate affected MVP, algorithm, baseline, and experimental evidence. Record the reason, changed items, preserved invariants, affected gates, and required reruns.

Do not approve an environment amendment by weakening the locked validation case, seed set, feasibility checker, tolerance, solver status, time or resource budget, comparison rule, or success criterion. A justified material change to that validation contract ends the current epoch and must be owned, versioned, and rebaselined independently of the failing algorithm.

## Readiness States

- `environment-valid`: the paper scenario, task causal chain, formal optimization problem, parameter applicability range, and scenario MVP relation are coherent, attributable, feasible as defined, and sufficiently supported. This status does not establish the need for a new algorithm.
- `algorithmic-need`: report `demonstrated`, `not demonstrated`, or `contradicted` from exact/reference and tuned-simple-rule evidence.
- `interface-complete`: report whether decision-time information and audit-only diagnostics are sufficient and correctly separated for algorithm work.
- `joint-ready`: downstream-only. It additionally requires an accepted algorithm contract and implementation audit against this exact environment version.

An environment can be valid while algorithmic need is not demonstrated or contradicted. Report `modeling-only` or stop the algorithmic route instead of changing the problem merely to make an algorithm pass.

## Workflow

1. Inventory the research direction, target domain, task driver, authoritative scenario/code artifacts, requested mode, and target venue level.
2. Run the Ordered Design Gates internally and maintain versioned evidence for each decision.
3. Use literature evidence when domain ranges, formulation choices, or strongest simple rules require external support; keep unknown values `TBD`.
4. For deeper environment design, locate the earliest unsupported causal bottleneck relative to the target venue. Extend only the necessary causal chain, model term, constraint, or applicability dimension; avoid objective inflation, version the revised scenario MVP, and declare the evidence invalidated by the change.
5. Hand the specification and scenario MVP to `ccf-env-code-auditor`. Hand the accepted formal problem to `ccf-algorithm-designer` only after environment acceptance, an adequate interface, and evidence that the algorithmic route remains justified. The downstream algorithm audit decides `joint-ready`.

## Internal Decision Record

Keep gate-by-gate decisions and evidence in an internal ledger unless the user requests a full audit:

```yaml
gate:
status: pass / conditional / fail / not_applicable
authority_version:
evidence_refs: []
decisive_finding:
supported_conclusion:
applicability_boundary:
owner:
invalidated_gates: []
required_reruns: []
```

Do not expose candidate-by-candidate deliberation or an exhaustive gate transcript by default.

## User-Visible Output

Return the requested artifact first. Then report only the decision-relevant projection:

```text
Verdict and readiness: design verdict; environment-valid; algorithmic-need; interface-complete
Supported conclusion and applicability:
Decisive evidence or contradiction:
Material change, unresolved blocker, and handoff:
```

Expand the task causal chain, formal problem, traceability matrix, gate ledger, or amendment record only when requested or when needed to explain a blocking decision.

## Conditional References

- Load `references/communication-env-gates.md` for a full design, audit, repair, amendment review, or when an inline gate cannot be decided from available evidence.
- Load `references/env-spec-template.md` only when producing or validating a `handoff-spec` or a persistent environment contract.
