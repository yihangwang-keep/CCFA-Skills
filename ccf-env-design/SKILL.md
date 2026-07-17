---
name: ccf-env-design
description: "Design, audit, and evolve communication-domain paper scenarios, formal optimization problems, parameter applicability ranges, and Minimum Executable Scenario (MES) versions. Use for task causal chains, central tradeoffs, objectives, constraints, information patterns, feasibility meaning, complexity balance, 最小可执行场景, 场景演化, 目标函数与约束. Do not design algorithms, validate environment code, invent results, or replace literature search."
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

Define the paper scenario and its parameter applicability range before deriving a **Minimum Executable Scenario (MES; 最小可执行场景)**. An MES is the smallest versioned scenario package that executes the complete causal and formal path end to end. It may contain one or more registered configurations when needed for reproducibility or an active tradeoff, and it must bind an entry point, interface, trace or seed controls, independent checks, and acceptance criteria. Minimum means causally complete and auditable, not numerically smallest or easier than the paper problem.

The first accepted MES is the executable validation baseline, not the final scene. Evidence from environment code, algorithm attempts, audits, and experiments may drive successive MES or formal-model versions. Each accepted paper-scenario, formal-problem, and MES version remains immutable; classify the proposed change and invalidation set before creating its successor.

The target venue may raise the required causal grounding, formal completeness, verification rigor, and evidence coverage. It is not a scientific reason to add variables, constraints, mechanisms, or difficult settings that do not follow from the task.

## Modes

- `design`: construct the paper scenario, formal optimization problem, parameter applicability range, and MES.
- `audit`: judge causal validity, complexity balance, applicability, and paper-scenario-to-MES consistency.
- `evolve`: classify new code, audit, or experiment evidence and decide whether it calls for evidence expansion, a successor MES, a formal amendment, or research reframing.
- `amendment-review`: decide whether evidence justifies changing the formal environment contract.
- `handoff-spec`: produce the environment specification for code audit and algorithm design.

## Ordered Design Gates

1. **Scenario-background gate:** define the communication context, actors, task or service need, why communication matters, and the abstraction boundary.
2. **Task-causal-chain gate:** state the concrete failure or lost value, affected entities, observed consequence, causal bottleneck, and chain from communication conditions and decisions to the task outcome.
3. **Scientific-question gate:** state one focused research question, central tradeoff, supported conclusion, and applicability boundary.
4. **Formal-problem gate:** define parameters, decision and state variables, objective, hard and soft constraints, information available at decision time, dynamics, uncertainty, and feasibility meaning.
5. **Problem-traceability gate:** map every objective term, variable, constraint, dynamic, uncertainty source, and coupling to the task causal chain or scientific question.
6. **Coupling-and-complexity gate:** identify the causal bottleneck, binding constraints, and coupled decisions; verify that the intended joint tradeoff is active and attributable.
7. **Paper-to-MES gate:** define the parameter applicability range, derive the smallest complete executable package, register its configurations and execution contract, and verify that the formal problem and central tradeoff are preserved.
8. **L1 audit-contract gate:** define the bidirectional design-to-code traceability, independent checks, and acceptance criteria by which `ccf-env-code-auditor` will decide whether implementation matches the frozen environment design.
9. **L2 probe-contract gate:** before outcomes are known, define an independently justified and attainable joint-tradeoff or optimization target, representative probe coverage, tuning/search budgets, matched information and feasibility rules, and the interpretation rule. `ccf-env-code-auditor` owns execution and `algorithmic_need` judgment.
10. **Evolution-and-version gate:** bind parent and current versions, classify any proposed delta before editing, and record preserved invariants, invalidated evidence, and required reruns.
11. **Algorithm-to-model escalation gate:** when algorithm code is faithful but documented algorithm-design repairs still cannot pass, review the exhaustion evidence. Distinguish an algorithm-specific failure from a formal-model defect, and accept only a causally justified, non-simplifying environment or mathematical-model change.
12. **Algorithm-information gate:** specify decision-time observations, timing, decision interface, feasibility signals, objective components, trace diagnostics, units, seeds, unavailable information, and audit-only information.
13. **Handoff-readiness gate:** record authoritative versions, unresolved items, expected environment checks, the exact problem the algorithm must solve, `environment-valid`, algorithmic-need evidence, and interface completeness. Reserve `joint-ready` for downstream algorithm acceptance.

Resolve a failed earlier gate before relying on later mathematical, implementation, or readiness conclusions.

Environment probes may include heuristic, greedy, static, domain, tuned, or decoupled rules when they test whether the causal bottleneck and central tradeoff are active. They are probes or baselines, not the paper's proposed algorithm contribution. This skill fixes their method-independent contract; it does not execute the sweep or issue its outcome. Never change the MES merely to make a probe fail. The no-heuristic requirement for a proposed algorithm is owned by `ccf-algorithm-designer` and verified by `ccf-algorithm-code-auditor`.

## Environment Authority And Evolution

Algorithm failure is diagnostic evidence. First close environment L1, algorithm-code fidelity, and algorithm-design repair. If faithful implementations and documented mechanism/family revisions still cannot satisfy the current formal target, environment design must review whether the scenario-to-model contract is infeasible, ill-posed, informationally inconsistent, causally incomplete, or mismatched to the paper scenario. A confirmed defect may require a new mathematical model, formal-problem version, and MES; it may not be repaired by making the problem easier for the algorithm.

Classify every proposed delta using `references/scenario-evolution-contract.md`: `implementation_repair`, `evidence_expansion`, `scenario_extension`, `formal_amendment`, or `research_reframe`. `invalidation` is the dependency consequence of a delta, not another change class. An implementation repair keeps the accepted semantics and MES version; a scenario extension creates a parent-linked successor MES; a formal amendment creates a new formal-problem and MES version; a research reframe starts a new paper-scenario lineage.

Accept any authority change only when evidence establishes causal or formal necessity, research-identity impact, information honesty, method neutrality, and non-simplification. Additionally require algorithm-repair exhaustion when the proposal originates from algorithm failure; ordinary method-independent domain evidence, code audit, or experiment evidence does not need an algorithm failure first. Never weaken material difficulty merely to obtain a pass. An independently proven modeling error may be corrected or replaced only when the paper scenario's causal difficulty and central tradeoff remain intact. Preserve the old version and evidence; create, rebaseline as required, and audit a successor instead of rewriting history.

## Readiness States

- `environment-valid`: consume the current `ccf-env-code-auditor` L1 result for the paper scenario, task causal chain, formal problem, parameter range, MES, and implementation. This status does not establish the need for a new algorithm.
- `algorithmic-need`: consume the current `ccf-env-code-auditor` result. `demonstrated` requires a complete, fair L2 evaluation in which tuned probes miss an independently justified attainable target; otherwise retain the auditor's `not_demonstrated`, `contradicted`, `insufficient_evidence`, or `stale` result.
- `interface-complete`: report whether decision-time information and audit-only diagnostics are sufficient and correctly separated for algorithm work.
- `joint-ready`: downstream-only. It additionally requires an accepted algorithm contract and implementation audit against this exact environment version.

An environment can be valid while algorithmic need is not demonstrated or contradicted. Report `modeling-only` or stop the algorithmic route instead of changing the problem merely to make an algorithm pass.

## Workflow

1. Inventory the research direction, target domain, task driver, authoritative scenario/code artifacts, requested mode, and target venue level.
2. Run the design-owned gates internally and maintain versioned evidence. For L2, freeze the probe contract and target interpretation without executing or judging the sweep.
3. Use literature evidence when domain ranges, formulation choices, or strongest simple rules require external support; keep unknown values `TBD`.
4. When algorithm repair is exhausted or other evidence suggests a model change, load the evolution contract, select the earliest owning layer, and create the smallest non-simplifying justified delta. Do not call an ordinary within-range experiment an MES extension or change the scenario merely to improve a method's ranking.
5. Hand the specification and MES to `ccf-env-code-auditor`. Hand the accepted formal problem to `ccf-algorithm-designer` only after environment acceptance, an adequate interface, and `algorithmic_need: demonstrated` under L2. The downstream algorithm audit decides `joint-ready`.

## Internal Decision Record

Keep gate status, authority versions, change class, evidence references, decisive findings, conclusion boundary, owner, invalidations, and reruns in an internal ledger. Do not expose candidate-by-candidate deliberation or an exhaustive gate transcript by default.

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

- Load `references/communication-env-gates.md` for a full design, audit, evolve, amendment review, or when an inline gate cannot be decided from available evidence.
- Load `references/env-spec-template.md` only when producing or validating a `handoff-spec` or a persistent environment contract.
- Load `references/scenario-evolution-contract.md` for `evolve`, `amendment-review`, any proposal to change an accepted authority artifact, or any dispute about version lineage, evidence reuse, or invalidation.
