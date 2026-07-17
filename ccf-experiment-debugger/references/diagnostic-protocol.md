# Auditor-Centered Failure Protocol

Use this protocol after an environment or algorithm MVP run fails, diverges, becomes unstable, cannot be reproduced, or misses its declared criteria. Keep this working record internal unless the user asks for the audit trail.

## Failure Record

```yaml
expected_criterion:
observed_result:
first_divergence:
run_command:
configuration_and_seeds:
validation_contract_version:
paper_scenario_version:
formal_problem_version:
scenario_mvp_version:
environment_spec_code_version:
environment_audit_verdict:
algorithm_spec_code_version:
algorithm_audit_verdict:
metrics_tolerances_hardware_dependencies:
preserved_logs_traces_outputs:
```

Do not overwrite the original failure record after repair. Append a new run record with new artifact versions.

## Auditor Evidence Ledger

| Layer | Required current evidence | Status | Decisive finding | Owner |
| --- | --- | --- | --- | --- |
| Environment authority and design contract | accepted paper scenario, formal problem, parameter applicability range, scenario MVP, information pattern | accepted / stale / contradicted / missing |  | `ccf-env-design` or `ccf-env-code-auditor` |
| Environment implementation | traceability, semantics, independent MVP execution, objective/constraint fidelity, central tradeoff | pass / conditional / fail / missing |  | `ccf-env-code-auditor` |
| Algorithm authority and design contract | formal target, family, mechanism, MVP, verification plan | accepted / stale / contradicted / missing |  | `ccf-algorithm-designer` or `ccf-algorithm-code-auditor` |
| Algorithm implementation | traceability, semantics, exact/oracle/bound evidence, independent MVP execution | pass / conditional / fail / missing |  | `ccf-algorithm-code-auditor` |
| Validation contract | original failure, cases, seeds, baselines, metrics, checker, tolerances, solver status, time/resource/platform accounting, pass criteria | accepted / stale / contradicted / missing |  | criterion's owning design skill; auditor verifies |
| Repository change | reviewed diff, fixed point, specification source, reviewed `HEAD` | pass / fail / missing / not applicable |  | fresh `$code-review` agent |

Never infer a downstream cause from stale or failed upstream evidence. Refresh the earliest dependency first.

## Minimal-Change Routing

| Confirmed cause | Owning action | Required refresh |
| --- | --- | --- |
| Environment code contradicts the accepted paper scenario or formal problem | repair the smallest responsible environment path | affected environment-auditor checks; algorithm audit if inputs, semantics, or behavior changed; checkpoint `$code-review` |
| Algorithm code contradicts the accepted algorithm specification | repair the smallest responsible algorithm path | affected algorithm-auditor checks; checkpoint `$code-review` |
| Algorithm implementation matches its specification but the mechanism misses its formal target | revise one mechanism or assumption in `ccf-algorithm-designer` | implementation traceability, complete algorithm audit, relevant MVP checks, checkpoint `$code-review` |
| Paper scenario, formal problem, or scenario MVP is causally, mathematically, or feasibly invalid | submit an environment amendment to `ccf-env-design` | complete environment audit, algorithm design/audit, all dependent result evidence; close the current loop epoch when the problem version changes |
| Locked validation criterion is independently invalid | submit a versioned validation change to the criterion's owning design skill | preserve the old failed case; end as `rebaseline-required` or `reframe`; do not accept in the current epoch |

Before the last row, test whether another credible solver, exact reference, or tuned simple rule exposes the same defect. If only the current algorithm fails while a credible alternative solves the accepted problem, the owner remains algorithm design.

## One-Delta Record

```yaml
round:
confirmed_cause_and_evidence:
owner:
single_changed_item:
old_artifact_versions:
new_artifact_versions:
validation_contract_version:
why_the_delta_addresses_the_cause:
checks_marked_stale:
rerun_commands_and_seeds:
checkpoint_fixed_point:
checkpoint_head:
domain_auditor_results:
code_review_result:
outcome:
```

Do not combine an environment-contract change and an algorithm change in one round. If a change reveals a second cause, close the current delta, refresh its evidence, then open a new round.

## Invalidation Rules

- Environment implementation delta: invalidate affected environment checks and every algorithm check whose inputs, transitions, residuals, objective, constraints, or execution behavior may change.
- Algorithm implementation delta: invalidate affected algorithm traceability, semantic, reference, runtime, and regression checks.
- Algorithm specification or mechanism delta: invalidate its implementation traceability, algorithm audit, relevant MVP evidence, and downstream paper-range results.
- Scenario-MVP parameter delta within the accepted parameter applicability range: invalidate its feasibility certificate, environment execution evidence, algorithm evidence, and results for the changed setting.
- Objective, decision variable, material constraint, information pattern, feasibility meaning, task causal chain, or parameter applicability range delta: create a new formal-problem version and invalidate all downstream environment, algorithm, baseline, and result evidence.
- Test or measurement implementation delta with unchanged criteria: invalidate every affected result and rerun the original case under the same validation contract.
- Case, seed, baseline, metric, checker, tolerance, solver-status, time/resource/platform accounting, or pass-criterion delta: create a new validation-contract version, preserve the old failure, and end the current epoch as required by the design-validation protocol.

## Closure

Close one repair only when:

1. the original failure is reproduced or its nondeterminism is characterized;
2. current environment and algorithm evidence establishes one owner;
3. one owned delta is versioned;
4. the original failing case meets its criteria under the unchanged validation contract;
5. every invalidated domain check passes under the same versions;
6. when repository files changed, the fresh checkpoint `$code-review` applies to the current `HEAD`; otherwise record it as not applicable;
7. remaining limitations and unresolved evidence are recorded.

Passing a replacement case while dropping the original failure, changing seeds to avoid it, widening a tolerance, weakening a solver status or time/resource budget, relaxing a material constraint, exposing future or audit-only information, or silently removing a difficult parameter is not closure.
