# Phase-B Complexity-Upgrade Contract

Use this structure for a user-approved stage design document after Phase A is
accepted. The document may add formal complexity, but it does not define another
MES. Replace legacy `MVP`, `MSE`, `candidate MES`, or `successor MES` names for the
stage's fixed implementation case with `stage_case`.

## 1. Authority And Parent Freeze

- upgrade document ID/version/status and `stage_request_id`;
- parent Phase-A record, frozen anchor and base-algorithm digests;
- parent files, configurations, reports, conclusions, and regressions that remain
  immutable;
- environment-ready, audit-ready, algorithm-ready, and conclusion-ready verdicts
  as separate fields.

## 2. Scientific Upgrade

- parent limitation or complexity gap;
- upgraded scientific question and causal chain;
- exact method-independent delta and causal/domain justification;
- inherited, added, removed, and forbidden semantics table;
- reason the upgrade remains in the same research lineage and preserves anchor
  regression.

## 3. Added Formal Objects

- added state, exogenous process, dynamics, uncertainty, observation/reveal
  timing, decisions, constraints, feasibility, objective, and aggregation;
- invariants inherited unchanged from Phase A;
- information pattern, nonanticipativity/causality requirements when applicable,
  and prohibited future/oracle leakage;
- conditions under which the stage is unsupported or becomes a research reframe.

## 4. Stage Case And Interface

- `stage_case_id`, fixed configuration, supported range, and out-of-range
  diagnostics;
- algorithm-visible observations/actions and audit-only fields;
- trace schema, independent replay/checkers, reference/oracle scope, leakage tests,
  and reproducibility requirements;
- explicit statement that the stage case is not an MES, anchor, or successor.

## 5. Environment Implementation And Gates

- implementation deliverables and exact files/interfaces allowed to change;
- algorithm-file freeze until the environment passes;
- document-to-code, physical/causal generation, information timing, constraint,
  action-effectiveness, independent replay, stage-feasibility, active-coupling,
  reproducibility, and coverage gates;
- complete Phase-A anchor regression and inherited L2 pointer.

## 6. Algorithm Modification And Repair

- unchanged base-algorithm run recorded before modification;
- stage-specific algorithm target, mechanism gap, permitted implementation or
  design changes, reference/bound, resource limits, and acceptance criteria;
- stage and anchor algorithm regression after every candidate delta;
- terminal classification: `stage_accepted`, `algorithm_failed`,
  `upgrade_unsupported`, `blocked`, or `reframe`.

Environment acceptance must precede algorithm modification. A failed algorithm
does not authorize changing the stage case, information boundary, target,
tolerance, resource budget, or frozen anchor.
