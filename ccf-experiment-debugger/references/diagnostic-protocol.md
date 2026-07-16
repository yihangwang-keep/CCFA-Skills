# Auditor-Centered Failure Protocol

Use this protocol after an environment or algorithm MVP run fails, diverges, becomes unstable, cannot be reproduced, or misses its declared criteria.

## Failure Record

```text
Expected criterion:
Observed result and first divergence:
Run command and configuration:
Paper scenario and MVP version:
Environment spec/code version and audit verdict:
Algorithm spec/code version and audit verdict:
Metrics, tolerances, seeds, hardware, and dependencies:
Logs, traces, checkpoints, and preserved outputs:
```

## Auditor Evidence Ledger

| Layer | Required current evidence | Status | Decisive finding | Owner |
| --- | --- | --- | --- | --- |
| Environment authority/design contract | accepted scenario, MVP, equations, information contract | accepted / stale / contradicted / missing |  | `ccf-env-design` or `ccf-env-code-auditor` |
| Environment implementation | traceability, semantics, independent MVP execution, fidelity, tradeoff | pass / conditional / fail / missing |  | `ccf-env-code-auditor` |
| Algorithm authority/design contract | formal target, family, mechanism, MVP, verification plan | accepted / stale / contradicted / missing |  | `ccf-algorithm-designer` or `ccf-algorithm-code-auditor` |
| Algorithm implementation | traceability, semantics, reference evidence, independent MVP execution | pass / conditional / fail / missing |  | `ccf-algorithm-code-auditor` |

Do not infer a downstream cause from stale or failed upstream contracts. Refresh the earliest dependent auditor evidence first.

## Minimal-Change Routing

| Confirmed cause | Owning action | Required rerun |
| --- | --- | --- |
| Environment code contradicts accepted scenario/model | repair the smallest responsible environment path | affected `ccf-env-code-auditor` gates, then algorithm audit if inputs/behavior changed |
| Algorithm code contradicts accepted algorithm spec | repair the smallest responsible algorithm path | affected `ccf-algorithm-code-auditor` gates |
| Algorithm implementation matches spec but mechanism misses its formal target | revise the smallest mechanism or assumption in `ccf-algorithm-designer` | complete algorithm audit under the new spec |
| Scenario contract or MVP is causally, mathematically, or feasibly invalid | revise the smallest scenario item in `ccf-env-design` and derive the MVP again | complete environment audit, then affected algorithm design/audit |

## Change Record

```text
Confirmed cause and evidence:
Owner:
Smallest changed item:
Old and new artifact versions:
Why this change addresses the cause:
Auditor gates invalidated:
Rerun commands and seeds:
Outcome:
```

## Closure

The loop closes when:

1. the failure is reproducible or its nondeterminism is characterized;
2. current environment and algorithm auditor evidence establishes the owner;
3. one minimal owned change is applied and versioned;
4. the original failing case passes its declared criteria;
5. every auditor gate invalidated by the change passes;
6. remaining limitations and unresolved evidence are recorded.
