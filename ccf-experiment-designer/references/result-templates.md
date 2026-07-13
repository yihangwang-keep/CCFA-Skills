# Result Templates

Use these templates to produce fill-in result tables. Keep all unknown numbers blank, `TBD`, or bracketed placeholders.

## Claim-Evidence Matrix(must)

```md
| Claim | Reviewer question | Evidence needed | Scenario / setting / formulation | Baselines | Metrics | Result placeholder | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | TBD | planned / running / done |
```
Evidence needed must answer what the evidences needed for this claim.

## Algorithmic Contribution Gate (must for algorithmic work)

```md
| Item | Required record | Verification / reference | Status |
| --- | --- | --- | --- |
| Formal target | objective, variables, constraints, assumptions | formulation review | pass / fail / unresolved |
| Solution process | initialization, steps, termination, feasibility, complexity | trace or reproducibility test | pass / fail / unresolved |
| Solver verification | residual, invariant, convergence, correctness, or constraint checks | named check and tolerance | pass / fail / unresolved |
| Optimality / theory | exact small-instance solver, oracle, bound, relaxation, or guarantee | gap or certification scope | pass / fail / N/A with reason |
| No-heuristic rule | proposed method contains no heuristic decision mechanism; heuristics are baselines only | component-by-component classification audit; no exceptions | pass / fail / unresolved |
```

## Scenario Integrity Gate (must)

```md
| Item | Scenario construction | Evidence | Status |
| --- | --- | --- | --- |
| Bottleneck preserved | motivating difficulty retained | comparison with simplified case | pass / fail / unresolved |
| Independent construction | source, generator, ranges, seeds fixed without result-based selection | construction rule or provenance | pass / fail / unresolved |
| Coverage | realistic, diverse, hard, boundary, and failure cases | coverage table | pass / fail / unresolved |
| Threshold integrity | domain/validation/preregistered selection with matched tuning budgets | full sweep or sensitivity | pass / fail / N/A |
| Simple rule baseline | non-learned/non-optimized sanity policy | result and interpretation | pass / fail / N/A with reason |
| Scenario changes | reason, version, affected assumption, all methods rerun | change ledger | pass / fail / unchanged |
```

## Main Comparison Table

```md
| Method | Source | Setting | Metric 1 ↑/↓ | Metric 2 ↑/↓ | Metric 3 ↑/↓ | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| User method | this paper |  | TBD | TBD | TBD |  |
| Baseline A | citation needed |  | TBD | TBD | TBD |  |
| Baseline B | citation needed |  | TBD | TBD | TBD |  |
```

## Ablation Table(if needed)

```md
| Variant | Component changed | Mechanism tested | Metric 1 ↑/↓ | Metric 2 ↑/↓ | Interpretation after user fills result |
| --- | --- | --- | --- | --- | --- |
| Full method | none | full mechanism | TBD | TBD |  |
| w/o component A | remove A | necessity of A | TBD | TBD |  |
| generic replacement | replace A | specificity of design | TBD | TBD |  |
```

## Robustness / Stress Test Table(if needed)

```md
| Stress condition | Why it matters | Scenario / parameter setting | Metric | User result | Failure threshold | Reviewer concern answered |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | TBD |  |  |
```

## Qualitative / Case Study Table(if needed)

```md
| Case | Selection rule | Expected observation | User-provided result | What it demonstrates | Failure or limitation |
| --- | --- | --- | --- | --- | --- |
|  | representative / hard / failure |  | TBD |  |  |
```

## Execution Priority Table(must)

```md
| Priority | Experiment | Claim defended | Cost | Dependency | Appendix/main | Stop condition |
| --- | --- | --- | --- | --- | --- | --- |
| P0 |  |  | low/medium/high |  | main |  |
```

## No-Fabrication Reminder

Use this note when returning templates:

```text
No experimental result has been generated here. All TBD cells must be filled from user-run experiments, paper-provided numbers, or verified public baseline reports under a matching formulation and setting.
```
