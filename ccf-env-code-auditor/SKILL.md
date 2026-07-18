---
name: ccf-env-code-auditor
description: "Independently audit Phase-A candidate-MES and Phase-B complexity-stage environment implementations against their accepted documents. Use for authority, design-to-code traceability, objective/constraint/state/decision semantics, information timing, feasibility, invariants, causal bottlenecks, anchor regression, 场景代码审查, 数学模型与代码一致性, 最小可执行场景核验. Run heuristic L2 only in Phase A; do not design, implement, or repair the environment or algorithm."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Environment Code Auditor

## Invocation Boundary

- **Use:** the primary object is the paper-scenario contract, formal optimization problem, parameter applicability range, minimum executable scenario (MES), environment implementation, executed behavior, or decision-time information interface.
- **Route elsewhere:** Phase-A document/environment work belongs to `ccf-mes-validation`; Phase-B upgrade-document/environment work belongs to `ccf-complexity-upgrade`; algorithm implementation evidence belongs to `ccf-algorithm-code-auditor`.

## Core Rule

Audit every environment version with the same ordered protocol. Establish bidirectional evidence:

~~~text
scenario/problem item -> code symbol -> executed path -> independently observed behavior
code behavior -> authorized problem item or necessary implementation detail
~~~

Code presence, names, comments, and configuration fields are declarations, not behavioral evidence. In Phase A, audit the complete candidate MES and use small controlled cases only for isolated semantic checks. In Phase B, audit the accepted upgrade document and its `stage_case`, rerun the frozen-anchor regression, and do not recompute `algorithmic_need`. A Phase-B stage may add method-independent formal complexity while preserving its declared parent invariants; it never creates another MES.

A stage implementation verdict is separate from algorithm acceptance: a requested stage passes its environment gate only when its specification, code, interface, and anchor regression agree. If that gate passes but the current algorithm fails, preserve the stage as valid failed evidence and route the failure to algorithm repair. Do not turn the algorithm result into a new MES or a reason to rerun L2.

The environment remains the authority for objective, constraints, information pattern, feasibility meaning, and applicability. Audit evidence may justify an amendment request, but this skill does not silently rewrite those semantics to make an algorithm pass.

Environment acceptance has two explicit layers for the initial anchor. Layer 1 is code-to-environment-design contract fidelity. Layer 2 is heuristic tradeoff resistance: with a frozen anchor MES, identical decision-time information and feasibility handling, a predeclared tuning budget, and an independently justified attainable target, sweep representative heuristic/probe rules once and test whether they still fail to reach the intended objective or reasonable tradeoff. Record procedure completion separately from the outcome: resistance gives `algorithmic_need: demonstrated`, while a successful heuristic gives `not_demonstrated`. An impossible, unsupported, or post-selected target gives `insufficient_evidence`. Later complexity stages inherit this anchor result and do not rerun heuristic probes; they require stage L1 consistency and anchor regression. Never alter environment parameters to manufacture heuristic failure.

## Modes

- static-trace: map the paper scenario and formal optimization problem into code.
- executable-audit: verify the complete MES through execution.
- complexity-stage-audit: verify one user-requested stage, anchor regressions, and implementation consistency without rerunning L2.
- repair: coordinate an authorized environment-code repair and verify the new artifact set.
- acceptance-gate: return the environment verdict, readiness state, and handoff evidence.

## Ordered Audit Gates

1. **Authority gate:** identify paper-scenario, formal-problem, parameter-range, frozen anchor MES, complexity-stage, equation, code, entry-point, configuration, time-index, and information-pattern versions; resolve conflicts before continuing.
2. **Design-contract gate:** verify that the task causal chain, causal bottleneck, scientific question, supported conclusion and applicability, formal problem, paper-to-MES relation, complexity rationale, and information contract are complete and internally consistent.
3. **Traceability gate:** map parameters, exogenous state, decision-time observations, decisions, objective terms, constraints, transitions, randomness, initialization, termination, metrics, and audit-only diagnostics; reverse-trace behavior that affects them.
4. **Semantic-correctness gate:** verify objective direction and aggregation, constraint direction and enforcement, feasibility meaning, units, indexing, update order, decision domains, state/observation separation, information timing, randomness, and metrics.
5. **Independent-execution gate:** run deterministic replay, independent objective/constraint/resource accounting, trace-wide invariants, controlled interventions, boundary configurations, repeated seeds, and full-load checks on the complete MES.
6. **Optimization-fidelity gate:** verify that decisions remain effective, the planned decision space and coupling are preserved, objective terms vary as designed, constraints can bind, and feasibility is independently observable.
7. **Layer-2 tradeoff-resistance gate:** for initial anchor acceptance only, verify target basis and attainability, then under a frozen anchor MES and equal information, feasibility rules, seeds, cases, and predeclared tuning budget, sweep representative fixed, domain, greedy/myopic, decoupled, tuned, and random-feasible `environment_probe` or baseline roles. Record `evidence_status` separately from `algorithmic_need`; a successful heuristic gives `not_demonstrated` without invalidating Layer 1. For a complexity-stage audit, mark this gate inherited/not applicable and do not rerun the sweep.
8. **Acceptance gate:** issue pass, conditional, or fail, then separately determine Layer-1 environment-validity, Layer-2 algorithmic-need evidence, interface completeness, and current native implementation-review status. Do not issue joint-ready here.

Missing evidence is not demonstrated; contradiction or failed behavior is incorrect. Stop executable conclusions when authority or design-contract evidence is unresolved.

## Native Implementation Review

For an executable audit, complexity-stage audit, phase repair verification, or acceptance gate, load ../ccf-common/references/implementation-review-protocol.md. Freeze a candidate artifact set with content digests and dispatch, in parallel, fresh read-only domain-contract-fidelity and implementation-assurance reviewers. These reviewers serve Layer 1 only: they check document/formal-problem/environment-to-code fidelity, information timing, feasibility, optimization fidelity, causal bottleneck, and implementation evidence. The auditor coordinates the Phase-A L2 sweep; a Phase-B audit records only stage consistency and anchor regression.

Reviewers only report; they never repair. An implementation owner cannot review the candidate it changed. A missing reviewer capability or missing digest is not_run/conditional and blocks acceptance; the coordinator must not self-review to downgrade it. Keep both axis reports separate and do not use one axis to offset another. Any artifact change marks prior review evidence stale.

## Workflow

1. Inventory the authoritative design, anchor MES, requested complexity-stage contract when active, code, tests, commands, configurations, seeds, traces, and artifact-set digests.
2. Run Layer 1 gates and the native two-axis review in sequence; attach each finding to the earliest failed gate.
3. For initial anchor acceptance, verify that the L2 target is attainable independently of the compared heuristics, then run the frozen-anchor sweep with matched information, feasibility, cases, and tuning budget; record all settings and the outcome. For a user-requested complexity stage, skip L2, audit the stage implementation, rerun anchor regressions, and carry forward the anchor `algorithmic_need` result.
4. When repair is authorized, route one smallest confirmed environment-code delta to its implementation owner, preserve the old artifact set, create a new candidate digest, and rerun every invalidated layer and gate. The repairer cannot sign the new review.
5. Report findings without repairing them. Phase A or Phase B owns every document or implementation delta and must request a fresh audit for the new artifact set.
6. Return Phase-A environment/L2 evidence to `ccf-mes-validation`; return Phase-B stage consistency, information-interface, checker, and anchor-regression evidence to `ccf-complexity-upgrade`.

## Internal Evidence Ledger

Keep artifact manifests, traceability, gate evidence, L1 status, L2 evidence status and `algorithmic_need`, native-review axis reports, invalidations, and reruns in the internal record defined by the two references. Do not expose exhaustive traces, discarded hypotheses, reviewer prompts, or step-by-step deliberation by default.

## User-Visible Output

Lead with findings when the user requests a review; otherwise return the requested artifact first. Default to this compact projection:

~~~text
Verdict and readiness: pass / conditional / fail; environment-valid; algorithmic-need; interface-complete
Layer 1 contract fidelity: status and material path:line findings
Layer 2 heuristic tradeoff resistance: anchor-only status, frozen MES, target, budget, and outcome; inherited for complexity stages
Complexity-stage consistency: requested stage, implementation trace, anchor regression, and inherited algorithmic-need
Reviewed artifact set and authority versions:
Domain contract fidelity: status and material path:line findings
Implementation assurance: status and material path:line findings
Supported conclusion and applicability:
Invalidated checks, required reruns, and next owner:
~~~

Expand authority tables, traceability matrices, semantic checks, amendment evidence, or reviewer records only when requested or necessary to support a blocker.

## Conditional References

- references/audit-protocol.md: executable environment gates, probe-role evidence, MES acceptance, amendments, and verdict rules.
- ../ccf-common/references/implementation-review-protocol.md: native two-axis reviewer dispatch, artifact digests, finding schema, stale rules, and output projection.
