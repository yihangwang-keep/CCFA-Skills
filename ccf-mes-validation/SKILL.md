---
name: ccf-mes-validation
description: "Own Phase A for a communication paper: accept a complete scientific-problem document, implement and audit one faithful Minimum Executable Scenario (MES), design and implement the initial algorithm, and run the repair loop until the anchor is accepted or blocked. Use for initial problem/MES/algorithm acceptance, 第一阶段MES验证, 初始Ralph闭环, or pre-anchor repair. Do not start a later complexity upgrade or plan publication experiments."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# MES Validation

## Phase Ownership

Phase A owns the complete path from an authoritative scientific-problem document
to one frozen MES anchor and an accepted initial algorithm. It designs and
implements the candidate environment and algorithm; the two code auditors remain
independent acceptance owners. Do not route design or repair through separate
environment-designer, algorithm-designer, or debugger skills.

The candidate remains a candidate through environment and algorithm audit. Set
`mes_role: anchor` only at the terminal `anchor_accepted` transition, after the
initial algorithm passes against the same artifact set. Never freeze the MES
before initial-algorithm acceptance.

## Accepted Input Document

Accept a document for implementation only when it fixes or explicitly marks
`TBD` for all of the following:

1. authority, version, source document, research identity, and intended supported
   conclusion;
2. paper scenario, abstraction boundary, task causal chain, causal bottleneck,
   focused scientific question, and central tradeoff;
3. formal optimization problem: parameters, states, decisions, objective order,
   constraints, dynamics, uncertainty, information timing, and feasibility;
4. parameter applicability range and the rule for selecting one reproducible
   candidate MES without deleting a material variable, constraint, coupling,
   information restriction, task consequence, or difficult registered case;
5. fixed MES configuration, executable entry points, deterministic seeds or
   traces, algorithm-visible interface, audit-only fields, and leakage boundary;
6. independent checker/reference path, environment implementation deliverables,
   L1 acceptance checks, one predeclared anchor-only L2 procedure and target, and
   terminal evidence required before algorithm work;
7. initial algorithm target, admissible method role, reference/oracle/bound,
   implementation interface, verification criteria, and resource limits, which
   may remain `TBD` until the environment passes.

A narrative scenario without executable parameters, information timing,
independent checks, or acceptance criteria is not implementation-ready. A
document may be revised before acceptance, but every accepted semantic revision
creates a new candidate authority version and invalidates dependent evidence.

## Phase A Ralph Loop

Follow `../ccf-common/references/ralph-phase-contract.md` and keep one append-only
record:

1. Validate and version the input document; record `document_accepted` only when
   the document contract above is complete.
2. Implement the candidate MES, environment interface, registered configuration,
   trace, and independent checker directly from that document.
3. Invoke `ccf-env-code-auditor` for design-to-code L1 and the one-time
   anchor-candidate L2. L1 failure returns to the environment implementation or,
   when the document itself is contradicted, to a new candidate document version.
4. If L2 is complete but `algorithmic_need` is not demonstrated, stop with
   `no_algorithmic_contribution`; do not tune the problem or candidate MES to
   force heuristic failure.
5. When environment evidence passes, derive and implement the initial algorithm
   against the exact formal target and visible interface. For `method_role:
   proposed`, classify every decision component and reject heuristic or hidden
   fallback mechanisms.
6. Invoke `ccf-algorithm-code-auditor` for specification-to-code fidelity,
   feasibility, independent reference evidence, complete candidate-MES execution,
   and native implementation review.
7. On failure, select the earliest failed dependency, assign one implementation
   or design owner inside this phase, apply one smallest delta, mark dependent
   evidence stale, and rerun the original failure plus both affected audits.
8. If independent evidence confirms that the pre-anchor formal problem is
   infeasible, ill-posed, informationally inconsistent, or causally incomplete,
   preserve the failed epoch and open a new candidate document/MES epoch inside
   Phase A. Never weaken material difficulty merely to obtain acceptance.
9. Only after current environment L1/L2 and initial algorithm audit all pass for
   the same authority and artifact digests, atomically set `mes_role: anchor` and
   `status: anchor_accepted`.

## Terminal Conditions

- `anchor_accepted`: complete document, environment L1, one-time L2 with
  demonstrated algorithmic need, accepted initial algorithm, current independent
  reviews, and frozen artifact digests.
- `no_algorithmic_contribution`: environment is valid but the predeclared L2 does
  not demonstrate a need for the proposed algorithmic contribution.
- `blocked`: a required input, executable path, independent checker, credible
  repair, or acceptance criterion cannot be supplied.
- `reframe`: the scientific question, task consequence, central tradeoff, or
  contribution identity must change.

Read `references/phase-a-problem-contract.md` when drafting or validating the
input document. Read `references/mes-validation-record.md` when creating the persistent record.
Phase A never starts a complexity stage and never edits an accepted anchor.
