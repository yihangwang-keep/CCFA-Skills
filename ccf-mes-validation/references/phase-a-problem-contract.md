# Phase-A Problem Document

Use this outline to make a paper/scenario document ready for implementation.
Keep the paper's terminology and equations. The document is the authority;
code should not silently fill in a missing scientific rule.

## 1. Research Identity

- document name, version, source, and status;
- intended contribution and the supported paper conclusion;
- what is inside and outside the paper's scope.

## 2. Scenario And Causality

- actors, communication task, physical/task conditions, and abstraction boundary;
- the causal chain from communication decisions to task or service outcomes;
- causal bottleneck, scientific question, and central tradeoff;
- why the retained decisions must be optimized together.

## 3. Formal Problem

- sets, parameters, units, states, exogenous inputs, and decisions;
- objective direction and ordering;
- material constraints, dynamics, uncertainty, termination, and feasibility;
- what is visible at each decision time and what is audit-only.

## 4. MES: Minimal But Complete

State explicitly that MES reduces the problem's scale, not its scientific
content. Give:

- the full parameter range and the rule used to choose the first fixed case;
- the fixed MES configuration, seed or trace, and executable entry point;
- a preservation table for the question, tradeoff, objective, decisions,
  constraints, coupling, information timing, feasibility, and task consequence;
- the reason the chosen scale is enough to activate the central tradeoff.

Do not call a case an MES when a removed object could change the preferred
decision or make the core question disappear.

## 5. Environment Interface And Evidence

- algorithm-visible observations and actions, with units and reveal times;
- audit-only and reference fields, plus the leakage boundary;
- independent replay/checker for state, objective, constraints, feasibility,
  invariants, and task consequences;
- environment implementation files and the checks the environment auditor will
  run;
- a small, predeclared sanity check showing that the central tradeoff is active.

## 6. Initial Algorithm

- exact formal target and accepted environment/interface version;
- method role and the intended mechanism;
- initialization, updates/search, feasibility handling, termination, outputs,
  and how a failure will be diagnosed;
- exact/oracle/bound/reference scope, resource limits, and acceptance criteria;
- the algorithm implementation entry point and independent audit requested.

The algorithm section may be completed after the environment is implemented,
but the problem and MES semantics must be fixed before coding begins.
