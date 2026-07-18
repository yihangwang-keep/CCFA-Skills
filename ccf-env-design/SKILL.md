---
name: ccf-env-design
description: "Design, audit, and evolve communication-domain paper scenarios, formal optimization problems, parameter applicability ranges, a complete Minimum Executable Scenario (MES) anchor, and its method-independent complexity ladder. Use for task causal chains, central tradeoffs, objectives, constraints, information patterns, feasibility meaning, complexity balance, 最小可执行场景, 场景演化, 复杂度拓展, 目标函数与约束. Do not design algorithms, validate environment code, invent results, or replace literature search."
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

Define the paper scenario and its parameter applicability range before deriving a **Minimum Executable Scenario (MES; 最小可执行场景)**. An MES is the smallest versioned scenario package that executes the complete causal and formal path end to end. Minimum means the paper's minimum scale with complete scientific semantics, not the minimum scientific problem, the fewest entities, or the easiest instance.

The first accepted MES is the frozen anchor for the rest of the normal workflow. It must already contain the core tradeoff and complete causal chain. Run the heuristic-probe L2 and establish `algorithmic_need` once for this anchor. After the anchor algorithm path is accepted, a user-requested scenario upgrade is a new complexity stage under the same formal problem, parameter range, and interface; do not rerun L2 or redesign/replace the MES to rescue an algorithm. A failed complexity stage is an algorithm diagnosis and repair input. Only an independently established infeasible or ill-posed authoritative problem can open a formal amendment, which starts a new candidate-MES/evidence epoch as an exception while preserving the old anchor as history.

Before the anchor is accepted, an L1/L2 contradiction or proof that the candidate formal problem is infeasible, ill-posed, or missing a causal requirement sends the work back to problem design: revise the formal problem and candidate MES together until the complete core tradeoff is executable. The no-redesign rule begins at anchor acceptance.

The target venue may raise the required causal grounding, formal completeness, verification rigor, and evidence coverage. It is not a scientific reason to add variables, constraints, mechanisms, or difficult settings that do not follow from the task.

## Modes

- `design`: construct the paper scenario, formal optimization problem, parameter applicability range, and MES.
- `audit`: judge causal validity, complexity balance, applicability, and paper-scenario-to-MES consistency.
- `evolve`: classify new code, audit, or experiment evidence and decide whether it is evidence/complexity expansion, implementation repair, formal amendment, or research reframing. A post-acceptance complexity stage does not create a successor MES.
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
9. **L2 probe-contract gate:** before outcomes are known, define an independently justified and attainable joint-tradeoff or optimization target, representative probe coverage, tuning/search budgets, matched information and feasibility rules, and the interpretation rule for the initial anchor MES only. `ccf-env-code-auditor` owns this one-time execution and `algorithmic_need` judgment.
10. **MES-freeze-and-complexity-ladder gate:** once the candidate MES and initial algorithm path pass, record `mes_role: anchor`, freeze its version, accept a user-requested stage delta, and define the stage's implementation-consistency, anchor-regression, and algorithm-acceptance rules. A stage is evidence expansion, not a successor MES, and does not rerun L2.
11. **Evolution-and-version gate:** bind authority, anchor MES, complexity-stage, implementation, and evidence versions; classify any proposed delta before editing; and record preserved invariants, invalidated evidence, and required reruns.
12. **Algorithm-to-model escalation gate:** when a complexity-stage failure remains after faithful code and documented algorithm-design repairs, review the exhaustion evidence. Distinguish an algorithm-specific failure from a formal-model defect. Only the latter can authorize a causally justified, non-simplifying formal amendment and new candidate MES.
13. **Algorithm-information gate:** specify decision-time observations, timing, decision interface, feasibility signals, objective components, trace diagnostics, units, seeds, unavailable information, and audit-only information.
14. **Handoff-readiness gate:** record authoritative versions, unresolved items, expected environment checks, the exact problem the algorithm must solve, `environment-valid`, algorithmic-need evidence, and interface completeness. Reserve `joint-ready` for downstream algorithm acceptance.

Resolve a failed earlier gate before relying on later mathematical, implementation, or readiness conclusions.

## Two-Phase Operating Model

**Phase A: anchor and initial algorithm.** Environment design defines the paper problem and complete MES. Environment code audit closes L1 and runs the one-time anchor L2 heuristic-probe contract. Algorithm design and algorithm code audit then accept the initial non-heuristic algorithm path on the anchor. If the initial algorithm fails, the repair loop upgrades code/mechanism/family against the anchor; it does not rerun a valid L2 or redesign the MES.

**Phase B: user-requested complexity upgrade.** A user or project owner supplies one method-independent stage delta. Environment design records the stage without changing the MES. Environment code audit checks the stage implementation against the same contract and reruns anchor regressions. Algorithm code/design then runs and, if needed, repairs the algorithm. The stage loop does not rerun anchor L2 or redesign the MES.

Stage environment validity and algorithm acceptance are separate gates. A consistent requested stage remains the active problem even when the current algorithm fails; that failure is preserved and repaired on the algorithm side. Only a confirmed formal-model defect may leave the frozen-anchor lineage.

Environment probes may include heuristic, greedy, static, domain, tuned, or decoupled rules when they test whether the causal bottleneck and central tradeoff are active in the initial anchor MES. They are probes or baselines, not the paper's proposed algorithm contribution. This skill fixes their one-time, anchor-only contract; it does not execute the sweep or issue its outcome. Later complexity stages do not use heuristic probes to re-decide `algorithmic_need`; they use implementation consistency, anchor regression, and the current algorithm audit. Never change the MES merely to make a probe fail. The no-heuristic requirement for a proposed algorithm is owned by `ccf-algorithm-designer` and verified by `ccf-algorithm-code-auditor`.

## Environment Authority And Evolution

Algorithm failure at a complexity stage is diagnostic evidence, not permission to redesign the MES. First close environment L1, algorithm-code fidelity, and algorithm-design repair while preserving the anchor and failed stage. If faithful implementations and documented mechanism/family revisions still cannot satisfy the current formal target, environment design must review whether the authoritative problem is infeasible, ill-posed, informationally inconsistent, causally incomplete, or mismatched to the paper scenario. A confirmed defect may require a new mathematical model, formal-problem version, and candidate MES; it may not be repaired by making the problem easier for the algorithm. Ordinary hardness, scale failure, or an unattainable algorithm-specific guarantee remains algorithm-owned.

Classify every proposed delta using `references/scenario-evolution-contract.md`: `implementation_repair`, `evidence_expansion`, `complexity_expansion`, legacy/exception `scenario_extension`, `formal_amendment`, or `research_reframe`. `invalidation` is the dependency consequence of a delta, not another change class. An implementation repair and complexity expansion keep the accepted anchor MES version; a formal amendment creates a new formal-problem and candidate MES version; a research reframe starts a new paper-scenario lineage. Do not use a successor MES as the normal response to algorithm failure.

Accept any authority change only when evidence establishes causal or formal necessity, research-identity impact, information honesty, method neutrality, and non-simplification. Additionally require algorithm-repair exhaustion when the proposal originates from algorithm failure; ordinary method-independent domain evidence, code audit, or experiment evidence does not need an algorithm failure first. Never weaken material difficulty merely to obtain a pass. An independently proven modeling error may be corrected or replaced only when the paper scenario's causal difficulty and central tradeoff remain intact. Preserve the old version and evidence; create and audit a successor only after an accepted formal amendment or research reframe, never as ordinary complexity progression.

## Readiness States

- `environment-valid`: consume the current `ccf-env-code-auditor` L1 result for the paper scenario, task causal chain, formal problem, parameter range, anchor MES or active complexity stage, and implementation. This status does not establish the need for a new algorithm.
- `algorithmic-need`: consume the one-time anchor-MES L2 result. `demonstrated` requires a complete, fair L2 evaluation in which tuned probes miss an independently justified attainable target; later complexity stages inherit this result and do not recompute it. Retain the auditor's `not_demonstrated`, `contradicted`, `insufficient_evidence`, or `stale` result until a formal amendment creates a new candidate MES.
- `interface-complete`: report whether decision-time information and audit-only diagnostics are sufficient and correctly separated for algorithm work.
- `joint-ready`: downstream-only. It additionally requires an accepted algorithm contract and implementation audit against this exact environment version.

An environment can be valid while algorithmic need is not demonstrated or contradicted. Report `modeling-only` or stop the algorithmic route instead of changing the problem merely to make an algorithm pass.

## Workflow

1. Inventory the research direction, target domain, task driver, authoritative scenario/code artifacts, requested mode, and target venue level.
2. Run the design-owned gates internally and maintain versioned evidence. For L2, freeze the probe contract and target interpretation without executing or judging the sweep.
3. Use literature evidence when domain ranges, formulation choices, or strongest simple rules require external support; keep unknown values `TBD`.
4. After the initial anchor algorithm path is accepted, receive one user-requested complexity-stage delta at a time. Record the stage contract, have `ccf-env-code-auditor` check implementation consistency and anchor regression, and hand the same formal problem to the algorithm auditor. Do not rerun L2 or change `algorithmic_need`. When the stage fails, select the earliest algorithm owner and preserve the failed stage while repairing the algorithm. If algorithm repair is exhausted or independent evidence suggests a model defect, load the evolution contract and create the smallest non-simplifying justified formal delta. Do not call ordinary complexity evidence an MES extension or change the scenario merely to improve a method's ranking.
5. Use `ccf-experiment-debugger` only to coordinate a failed stage or implementation/algorithm repair loop. Use `ccf-experiment-designer` later for paper-range usage evidence, baselines, metrics, ablations, robustness, and conclusion applicability; neither skill replaces environment or algorithm design/audit.

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
