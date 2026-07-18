# Phase-A Scientific-Problem Contract

Use this structure when the supplied paper/idea document must become an
implementation-ready Phase-A authority. Preserve the user's domain terminology
and equations; do not replace missing semantics with generic placeholders beyond
explicit `TBD` fields.

## 1. Authority

- document ID, version, status, source artifacts, and research identity;
- intended contribution type and supported-conclusion boundary;
- objects frozen by this version and unresolved items.

## 2. Scenario And Causality

- actors, communication task, physical/task conditions, and abstraction boundary;
- task causal chain from communication decisions to task/service consequences;
- causal bottleneck, focused scientific question, and central tradeoff;
- why retained decisions must be optimized jointly and what would make the
  problem too simple or needlessly complex.

## 3. Formal Problem

- sets, parameters, state, decision variables, exogenous inputs, and units;
- objective direction and ordering;
- every material constraint, dynamics/update order, uncertainty, and termination;
- information visible at each decision time and audit-only information;
- feasibility meaning and problem-to-causal-chain traceability.

## 4. Applicability And Candidate MES

- method-independent parameter applicability range, construction rules, seeds,
  exclusions, and conclusion boundary;
- one fixed candidate-MES configuration derived directly from the same formal
  problem;
- preservation table covering scientific question, objective, decisions,
  constraints, coupling, information timing, feasibility, and causal bottleneck;
- executable entry point, manifest/configuration, trace schema, and artifact
  digests. Fixing parameters may reduce first-run coverage but cannot remove a
  material semantic object.

## 5. Environment Interface And Evidence

- algorithm-visible observations/actions with meaning, unit, index, and reveal
  time;
- audit-only fields, hidden/reference values, and leakage prohibitions;
- independent replay/checker path for state, constraints, feasibility, objective,
  invariants, and task consequences;
- environment implementation deliverables and L1 acceptance gates;
- predeclared anchor-candidate L2 probes, matched information/feasibility/tuning
  budgets, attainable target basis, and interpretation rule.

## 6. Initial Algorithm Contract

- exact formal target and accepted environment/interface versions;
- method role and decision-component classification;
- credible family comparison and selected mechanism;
- initialization, updates/search, feasibility handling, termination, recovery,
  outputs, failure behavior, and complexity target;
- exact/oracle/bound/reference scope and complete candidate-MES verification;
- implementation entry points, resource limits, acceptance criteria, and required
  independent audit.

The algorithm section may remain `TBD` until environment L1/L2 passes. The
candidate becomes a frozen anchor only after this section is implemented and its
algorithm audit passes.
