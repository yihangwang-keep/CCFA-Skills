# Result Templates

Use only the templates needed by the user's requested artifact. Keep every unknown result as `TBD`; never infer a number from an expected trend.

## Contents

- Conclusion-evidence and upstream-acceptance records
- Algorithmic-contribution and scenario-integrity gates
- Main, mechanism, robustness, and exact-reference tables
- Version-boundary, execution-priority, and provenance records

## Conclusion-Evidence Matrix

```md
| Paper conclusion | Applicability range | Decisive question | Setting and authoritative version | Baselines | Metrics and feasibility checks | Interpretation rule | Result | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | support / narrow / contradict / unresolved | TBD | planned / running / done |
```

The interpretation rule must be fixed before comparative outcomes are inspected.

## Upstream Acceptance Record

Keep this internal unless the user requests an audit or a version conflict affects the result.

```md
| Artifact | Version | Required verdict | Current verdict | Limitation or excluded range |
| --- | --- | --- | --- | --- |
| Paper scenario and formal problem |  | accepted | TBD |  |
| Scenario MVP and environment |  | accepted | TBD |  |
| Algorithm specification and implementation, when applicable |  | accepted | TBD |  |
| Exact/oracle/bound reference and independent checker |  | accepted | TBD |  |
```

## Algorithmic Contribution Gate

Use internally for algorithmic work. Show it only for an audit request or when a failed item blocks experiment design.

```md
| Item | Required record | Verification or reference | Status |
| --- | --- | --- | --- |
| Formal target | objective, variables, constraints, assumptions | accepted formulation | pass / fail / unresolved |
| Solution process | initialization, steps, termination, feasibility, complexity | accepted specification and trace | pass / fail / unresolved |
| Solver verification | residual, invariant, convergence, correctness, constraint checks | named check and tolerance | pass / fail / unresolved |
| Optimality or theory | exact solver, oracle, bound, relaxation, or qualifying guarantee | gap and certification scope | pass / fail / N/A with reason |
| No-heuristic rule | proposed method contains no heuristic decision mechanism; heuristics are comparison baselines only | component-by-component classification | pass / fail / unresolved |
```

## Scenario Integrity Gate

Keep this internal unless the user asks for the gate record or a failed item changes the conclusion scope.

```md
| Item | Scenario construction | Evidence | Status |
| --- | --- | --- | --- |
| Causal bottleneck preserved | motivating scarcity, coupling, dependency, or information restriction retained | comparison with controlled simplification | pass / fail / unresolved |
| Method-independent construction | source, ranges, generator, and seeds fixed without favorable-result selection | provenance and version | pass / fail / unresolved |
| Applicability coverage | nominal, hard, boundary, and failure settings | coverage table | pass / fail / unresolved |
| Threshold integrity | domain or predeclared selection with matched tuning budgets | full relevant sweep | pass / fail / N/A |
| Simple-rule check | properly tuned sanity rule under matching information and feasibility | result and interpretation | pass / fail / N/A with reason |
| Scenario changes | reason, old/new versions, invalidated evidence, all methods rerun | change ledger | pass / fail / unchanged |
```

## Main Comparison Table

```md
| Method | Source and version | Setting | Feasibility | Objective or task metric 1 ↑/↓ | Metric 2 ↑/↓ | Runtime/resource metric ↓ | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Proposed method | this paper |  | TBD | TBD | TBD | TBD |  |
| Baseline A | citation needed |  | TBD | TBD | TBD | TBD |  |
| Baseline B | citation needed |  | TBD | TBD | TBD | TBD |  |
```

State units, aggregation, repeated-run protocol, stopping tolerance, and whether values are directly comparable.

## Mechanism Test Table

```md
| Variant or intervention | Mechanism tested | Formulation source | Setting/version | Feasibility | Metric 1 ↑/↓ | Metric 2 ↑/↓ | Result-dependent interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Full method | complete accepted mechanism |  |  | TBD | TBD | TBD |  |
| Without or replace component A | necessity or specificity of A |  |  | TBD | TBD | TBD |  |
```

Do not create this table when the accepted method has no separable mechanism to test.

## Robustness And Failure Table

```md
| Changed dimension | Why it matters | Setting and version | Metric and feasibility check | Result | Boundary or stop condition | Conclusion effect |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | TBD |  | support / narrow / contradict / unresolved |
```

## Exact Or Bound Comparison

```md
| Instance | Proposed result | Exact/oracle/bound result | Gap | Feasible | Reference status/tolerance | Certification scope |
| --- | --- | --- | --- | --- | --- | --- |
|  | TBD | TBD | TBD | TBD | TBD |  |
```

## Version-Boundary Record

Use when an environment amendment or scenario-MVP change invalidates prior results.

```md
| Evidence item | Old version/status | New version/status | Why invalidated | Required rerun | Reusable common physical/service metric |
| --- | --- | --- | --- | --- | --- |
|  |  | TBD |  |  |  |
```

Do not place objective values from materially different formal-problem versions in one ranking.

## Execution Priority Table

```md
| Priority | Experiment | Paper conclusion tested | Cost | Dependency | Main paper/appendix | Stop or interpretation condition |
| --- | --- | --- | --- | --- | --- | --- |
| P0 |  |  | low / medium / high |  | main |  |
```

## Result Provenance Note

Include this note only when handing off a fill-in template:

```text
No experimental value has been generated by this template. Every TBD cell must be filled from an executed experiment, a paper-provided value, or a verified public result under a matching formal problem, setting, and protocol.
```
