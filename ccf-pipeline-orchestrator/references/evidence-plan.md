# Post-Acceptance Evidence Plan

Use only after the applicable Phase A or Phase B artifacts and both audits are
current. This is paper-range evidence planning, not phase design or repair.

## Accepted Inputs

Record the accepted phase record, environment and algorithm versions, frozen
anchor, current upgrade scenario when applicable, applicability range, independent
reference/checker, limitations, and excluded settings. Stop an affected branch
when these versions are stale or incompatible.

## Conclusion-Evidence Ledger

For each intended paper conclusion record:

| Field | Required content |
| --- | --- |
| Conclusion and range | Exact statement, operating range, and exclusions |
| Decisive question | What evidence could support or weaken it |
| Settings | Nominal, binding, boundary, failure, and robustness cases |
| Baselines | Closest prior, strong current, tuned simple, decoupled, and exact/oracle/bound where applicable |
| Metrics | Direction, unit, aggregation, uncertainty, feasibility residual, and threshold |
| Mechanism test | Ablation, intervention, sensitivity, proof, or diagnostic tied to the proposed mechanism |
| Interpretation rule | Result-dependent support, narrowing, or rejection rule fixed before outcomes |
| Result | Real supplied value or `TBD` |

Give comparable methods the same information, feasibility rules, stopping
tolerance, tuning budget, cases, seeds, and compute accounting. Preserve failures
and exclusions. Heuristics may be baselines under a declared role; later
baseline results do not rewrite the accepted Phase-A environment or algorithm
audit evidence.

## Minimum Convincing Package

- main comparison across the accepted applicability range;
- feasibility and task/service consequences, not objective value alone;
- mechanism-specific evidence;
- robustness, boundary, failure, and efficiency evidence;
- exact/oracle/bound comparison on its declared scope;
- uncertainty intervals or deterministic coverage statement;
- explicit limitations and result-dependent conclusion boundaries.

Use `TBD` rather than invented numbers. Send supplied values and the ledger to
`ccf-visual-composer` for figures/tables, `ccf-paper-writer` for manuscript
expression, and `ccf-integrity-auditor` for conclusion/number consistency.
