---
name: ccf-env-code-auditor
description: "Audit communication paper scenarios, formal optimization problems, scenario MVPs, and environment code. Use for authority, design-to-code traceability, objective/constraint/state/decision semantics, information patterns, feasibility, invariants, causal bottlenecks, parameter applicability, 场景代码审查, 数学模型与代码一致性, MVP核验. Do not design algorithms, judge algorithm performance, or replace scenario design."
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

- **Use:** the primary object is the paper-scenario contract, formal optimization problem, parameter applicability range, scenario MVP, environment implementation, executed behavior, or decision-time information interface.
- **Route elsewhere:** scenario formulation and semantic amendments belong to `ccf-env-design`; algorithm mechanism and performance belong to the algorithm skills.

## Core Rule

Audit every environment version with the same ordered protocol. Establish bidirectional evidence:

```text
scenario/problem item -> code symbol -> executed path -> independently observed behavior
code behavior -> authorized problem item or necessary implementation detail
```

Code presence, names, comments, and configuration fields are declarations, not behavioral evidence. Use the complete scenario MVP for acceptance; use small controlled cases only for isolated semantic checks. Reapply the protocol after any code change, information-interface change, or accepted environment amendment.

The environment remains the authority for objective, constraints, information pattern, feasibility meaning, and applicability. Audit evidence may justify an amendment request, but this skill does not silently rewrite those semantics to make an algorithm pass.

## Modes

- `static-trace`: map the paper scenario and formal optimization problem into code.
- `executable-audit`: verify the complete scenario MVP through execution.
- `repair`: patch a confirmed environment-code defect and rerun affected checks.
- `acceptance-gate`: return the environment verdict, readiness state, and handoff evidence.

## Ordered Audit Gates

1. **Authority gate:** identify paper-scenario, formal-problem, parameter-range, scenario-MVP, equation, code, entry-point, configuration, seed, unit, time-index, and information-pattern versions; resolve conflicts before continuing.
2. **Design-contract gate:** verify that the task causal chain, causal bottleneck, scientific question, supported conclusion and applicability, formal problem, paper-to-MVP relation, complexity rationale, and information contract are complete and internally consistent.
3. **Traceability gate:** map parameters, exogenous state, decision-time observations, decisions, objective terms, constraints, transitions, randomness, initialization, termination, metrics, and audit-only diagnostics; reverse-trace behavior that affects them.
4. **Semantic-correctness gate:** verify objective direction and aggregation, constraint direction and enforcement, feasibility meaning, units, indexing, update order, decision domains, state/observation separation, information timing, randomness, and metrics.
5. **Independent-execution gate:** run deterministic replay, independent objective/constraint/resource accounting, trace-wide invariants, controlled interventions, boundary configurations, repeated seeds, and full-load checks on the complete scenario MVP.
6. **Optimization-fidelity gate:** verify that decisions remain effective, the planned decision space and coupling are preserved, objective terms vary as designed, constraints can bind, and feasibility is independently observable.
7. **Tradeoff gate:** run representative fixed, domain, greedy/myopic, decoupled, tuned, and random-feasible rules with equal information and declared tuning controls; verify the causal bottleneck and intended central tradeoff across the supported parameter range.
8. **Acceptance gate:** issue `pass`, `conditional`, or `fail`, then separately determine `environment-valid`, algorithmic-need evidence, and interface completeness from the combined design, trace, semantic, execution, optimization, and tradeoff evidence. Do not issue `joint-ready` before algorithm acceptance.

Missing evidence is `not demonstrated`; contradiction or failed behavior is `incorrect`. Stop executable conclusions when authority or design-contract evidence is unresolved.

## Workflow

1. Inventory the authoritative design, scenario MVP, code, tests, commands, configurations, seeds, and traces.
2. Run the Ordered Audit Gates in sequence and attach each finding to the earliest failed gate.
3. Classify findings as `blocker`, `major`, `minor`, or `note` with `file:line` and decisive execution evidence.
4. When repair is authorized, patch the smallest confirmed environment-code defect, add a regression, and rerun every invalidated gate.
5. If evidence points to problem semantics rather than code, return an evidence-backed amendment request to `ccf-env-design`; do not edit the contract here.
6. Return current `environment-valid`, algorithmic-need, and interface evidence to `ccf-algorithm-designer`; return a modeling-only or invalid result to the scenario owner, or failure evidence to `ccf-experiment-debugger`.
7. Only at a debugger checkpoint or when the user explicitly requests repository-diff review, hand off the fixed point and accepted specification to a fresh `$code-review` agent. Do not invoke it for a domain-only audit.

## Internal Evidence Ledger

Keep the traceability matrix and gate evidence internal unless a full audit is requested:

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

Do not expose exhaustive traces, discarded hypotheses, or step-by-step deliberation by default.

## User-Visible Output

Lead with findings when the user requests a review; otherwise return the requested artifact first. Default to this compact projection:

```text
Verdict and readiness: pass / conditional / fail; environment-valid; algorithmic-need; interface-complete
Supported conclusion and applicability:
Decisive design-to-code or execution evidence:
Minimal fix, invalidated checks, and required reruns:
Next owner:
```

Expand authority tables, traceability matrices, semantic checks, or amendment evidence only when requested or necessary to support a blocker.

## Conditional Reference

Load `references/audit-protocol.md` for an executable audit, repair, acceptance gate, full static trace, or any disputed semantic/readiness decision. A simple routing or status answer does not require it.
