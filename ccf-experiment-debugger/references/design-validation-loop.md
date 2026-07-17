# Design-Validation Loop

Use this as the domain protocol for a Ralph-style continuation loop. The continuation mechanism repeats one fixed prompt; this file and the persistent ledger determine the next valid action and whether the work is complete. Never treat a completion marker, iteration limit, or successful command exit as scientific acceptance.

## Contents

- Frozen research layers, validation contract, and fixed loop instruction
- Persistent ledger and one-round protocol
- Environment amendment, validation change, and invalidation rules
- Scope-specific terminal statuses, precedence, and user-visible projection

## Freeze Four Research Layers And One Validation Contract

Record these layers before the first round:

| Layer | Authority | Contents | Loop permission |
| --- | --- | --- | --- |
| `R0 research basis` | paper-scenario owner | communication task, central scientific question, task causal chain, central tradeoff, non-negotiable service meaning, intended contribution and paper-conclusion type | frozen; a necessary change ends as `reframe` |
| `R1 formal problem` | environment design | objective, decision variables, material constraints, dynamics, uncertainty, information pattern, feasibility meaning, parameter applicability range | amend only through the environment request below |
| `R2 scenario MVP and environment` | environment design and audit | fixed parameter instance derived from R1, environment specification/code, independent checker, feasibility certificate, validation criteria | repair implementation or justified parameter defects without changing R0/R1 semantics |
| `R3 algorithm and implementation` | algorithm design and audit | formal target, mechanism, required information, implementation, exact/oracle/bound reference, tests, runtime and acceptance criteria | default repair layer |

The scenario MVP may reduce first-round parameter coverage only. It must retain the objective, decision variables, material constraints, decision coupling, information pattern, feasibility meaning, task causal chain, and causal bottleneck of R1.

Treat design documents, formal specifications, code, configurations, and executable evidence as one versioned contract. A documentation delta is a first-class loop change: revise the owning design artifact before dependent code when semantics change, and never rewrite documentation after the fact merely to legitimize current behavior.

Freeze a separate `V0 validation contract` before the first round. For every criterion, record its owning design skill, artifact version, original failing case, scenario cases and parameter settings, seeds, baselines, metrics, independent checker, tolerances, required solver status, time/resource budget, hardware and software accounting, stop rule, and pass condition. `ccf-env-design` owns scenario, feasibility, service, information, and parameter criteria; `ccf-algorithm-designer` owns algorithm correctness, convergence, approximation, and execution-budget criteria. Their code auditors verify the criteria and results but may not relax them.

The validation contract is not an algorithm configuration. Adding diagnostics may not remove or weaken a locked criterion. A material criterion change creates `V1` and cannot produce `accepted` in the current epoch.

## Fixed Loop Prompt

Create a dedicated loop branch or worktree, the ledger path, and fixed points before starting. Repeat this prompt unchanged; put round-specific state only in the ledger:

```text
Continue the CCFA design-validation loop recorded at <ledger-path>.
Read the authoritative R0-R3 artifacts and current evidence from that ledger.
Read the locked validation contract and preserve every original failure and pass criterion.
Work only on the earliest missing, stale, failed, or contradicted check.
Assign one active owner and apply at most one owned delta in this round.
Preserve the ordered owner path: environment implementation, algorithm implementation,
algorithm design, scenario design. Do not change R0 or R1 to rescue one algorithm.
Run the original failure, all invalidated domain checks, and the required independent reviews.
Update the ledger with exact artifact versions, commands, evidence, and one current status.
Emit the terminal marker only after the ledger records one valid terminal status.
```

Use a neutral host marker such as `<promise>CCFA TERMINAL STATUS RECORDED</promise>`. The marker stops continuation; the ledger entry supplies the actual result.

## Persistent Internal Ledger

```yaml
loop_id:
scope: environment | algorithm | joint
status: active | accepted | no-algorithmic-contribution | rebaseline-required | reframe | blocked
fixed_prompt_hash:
loop_base_sha:
specification_paths: []
validation_contract:
  version:
  artifact_paths: []
  criterion_owners: []
  locked_cases: []
  locked_seeds: []
  locked_baselines: []
  metrics_and_tolerances: []
  checker_and_solver_requirements: []
  time_resource_and_platform_accounting: []
  stop_and_pass_conditions: []
R0:
  version:
  artifact_paths: []
  frozen_items: []
R1:
  version:
  artifact_paths: []
  frozen_items: []
R2:
  version:
  artifact_paths: []
  acceptance_criteria: []
  environment_audit:
R3:
  version:
  artifact_paths: []
  acceptance_criteria: []
  algorithm_audit:
current_round:
current_owner:
active_failure:
single_delta:
invalidated_checks: []
validation_commands: []
validation_evidence: []
round_base_sha:
checkpoint_head:
code_review:
final_review:
environment_amendment:
validation_change_request:
supported_conclusion:
conclusion_applicability_range:
remaining_limitations: []
terminal_reason:
```

Store only auditable decisions and evidence: version identifiers, statuses, decisive findings, file references, commands, residuals, metrics, and required actions. Do not place unpublished results in public systems.

## One Round

1. Read the ledger and verify that the fixed prompt, R0-R3 versions, V0 validation contract, and current `HEAD` match the recorded state.
2. Select the earliest stale or failed dependency using the ordered failure protocol.
3. Name one owner and one smallest delta. Never modify environment semantics and algorithm behavior in the same round.
4. Run the original failure under the locked validation contract first, then the checks invalidated by the delta. Preserve failed outputs and do not substitute an easier case, seed, tolerance, platform accounting rule, or pass condition.
5. Obtain a fresh applicable CCFA auditor verdict against the current artifacts. The auditor reviews; the owner performs repairs.
6. Commit the single round delta as a checkpoint on the dedicated loop branch. Launch a fresh review agent with: `Use $code-review to review changes since <round-base-sha>; specification: <R0-R3 and V0 artifact paths>.` Record its reviewed `HEAD` and result; do not copy or alter the skill's Standards/Spec protocol.
7. Update invalidation, evidence, version, and status fields. Continue only from the earliest remaining non-current check.

After all domain criteria pass, launch another fresh review agent with: `Use $code-review to review changes since <loop-base-sha>; specification: <R0-R3 and V0 artifact paths>.` Acceptance requires its reviewed `HEAD` to equal the final `HEAD`.

## Environment Amendment Request

Algorithm failure is evidence about the algorithm until an environment defect is established independently. Submit this request before changing R1 or an R2 item that changes problem semantics:

```yaml
observed_failure:
algorithm_families_or_simple_rules_checked:
why_algorithm_only_repair_is_insufficient:
independent_environment_defect:
task_physical_protocol_or_service_basis:
proposed_minimal_change:
objective_and_feasible_set_impact:
information_pattern_impact:
R0_items_preserved:
method_independence_check:
invalidated_artifacts_and_results: []
required_reruns: []
requested_terminal_status: rebaseline-required | reframe
```

Use the environment-authority checks loaded directly by `SKILL.md`. Reject the request when another credible solver or properly tuned simple rule solves the accepted problem and only the current algorithm fails. Accepting a material amendment creates a new problem or scenario-MVP version; never compare old and new objective values as if they came from one unchanged problem.

## Validation Contract Changes

Do not edit V0 in place. A requested change must record:

```yaml
criterion_owner:
observed_failure:
old_criterion_and_basis:
proposed_criterion_and_external_basis:
why_this_is_not_method_rescue:
cases_seeds_metrics_or_platforms_affected: []
paper_conclusion_and_applicability_impact:
invalidated_artifacts_and_results: []
required_reruns: []
requested_terminal_status: rebaseline-required | reframe
```

- Repairing test or measurement code so that it enforces unchanged V0 semantics is an implementation repair; rerun the original V0 case and every affected check.
- Adding a diagnostic or stricter case may continue only when every V0 criterion remains binding and the addition cannot turn an existing failure into a pass.
- Removing a case, changing seeds to avoid failure, widening a tolerance, accepting a weaker solver status, changing comparison fairness, or relaxing time/resource accounting is method rescue unless independent task, physical, protocol, service, or measurement evidence establishes otherwise.
- An independently justified material V0 change that preserves R0 starts a new validation epoch as `rebaseline-required`. If it changes the research identity, task/service meaning, intended contribution type, or conclusion applicability semantics, end as `reframe`.

The old failed configuration remains in the ledger. V1 results must not be reported as if they passed V0.

## Invalidation And Epochs

- R3 implementation repair: rerun affected algorithm checks, the original failure, regressions, and checkpoint review.
- R3 mechanism change: rerun implementation traceability, complete algorithm audit, exact/oracle/bound comparison, applicable MVP settings, and checkpoint review.
- R2 environment-code repair: rerun affected environment audit and every algorithm check whose observations, actions, transitions, objective, constraints, or execution changed.
- R2 fixed-parameter change that replaces the scenario MVP: end the current epoch as `rebaseline-required`, regenerate its feasibility certificate, and rerun all methods. Retain the old failed setting in the ledger. Adding a paper-range evaluation setting without replacing the accepted MVP does not trigger this status.
- R1 change preserving R0: end the current epoch as `rebaseline-required`; derive a new scenario MVP and rerun environment, algorithm, baseline, validation-contract, and result evidence from the new fixed point.
- V0 material change preserving R0: end the current epoch as `rebaseline-required`; create V1, retain the V0 failure, and rerun every affected method under one common contract.
- R0 change, or an R1/V0 change that alters the scientific question, task causal chain, central tradeoff, task/service meaning, intended contribution type, or conclusion applicability semantics: end as `reframe`.

## Terminal Status Precedence

Choose exactly one status in this order:

1. `no-algorithmic-contribution` for `scope: algorithm` or `scope: joint` when the current environment is valid and current exact/reference or tuned-simple-rule evidence refutes algorithmic need without requiring a problem or validation-contract change. This ends the algorithm or joint loop before any later project-level contribution reframing. An environment-only loop instead records the algorithmic-need result and may still accept the environment.
2. `reframe` when progress requires an R0 research-identity change.
3. `rebaseline-required` when an independently accepted material R1, R2 scenario-MVP, or V0 change preserves R0 but invalidates the current epoch.
4. `blocked` when no earlier terminal fact applies and required evidence, authority, resources, or a user decision is unavailable.
5. `accepted` only when no earlier terminal condition applies and the scope-specific acceptance rule below passes.

Do not use `reframe` merely because algorithmic advantage is absent; use the explicit first status. Do not use `accepted` in the same epoch as a material environment or validation-contract change.

## Scope-Specific Terminal Statuses

- `accepted` for `scope: environment`: R0/R1 are current, the scenario MVP and environment implementation are accepted, `environment-valid` and interface evidence are current, the original failure and every invalidated environment check pass under unchanged V0, the environment audit passes, and final `$code-review` covers the final `HEAD` when repository files changed. Algorithm acceptance is not required.
- `accepted` for `scope: algorithm`: the current environment is valid, current, and compatible with the reviewed algorithm version; the algorithm contract and implementation are accepted; the original failure and every invalidated algorithm check pass under unchanged V0; the algorithm audit passes; and final `$code-review` covers the final `HEAD` when repository files changed.
- `accepted` for `scope: joint`: both scope-specific rules pass against mutually compatible R0-R3 and unchanged V0 versions; this is the loop form of `joint-ready`.
- `no-algorithmic-contribution`: the environment is valid, but an exact method or properly tuned simple rule already resolves the central tradeoff within the declared criteria, or the proposed mechanism has no supported algorithmic advantage. Preserve the modeling/reference result and narrow the paper conclusion.
- `rebaseline-required`: an independently justified environment or validation-contract amendment preserves R0 but materially changes R1, the scenario MVP, or V0; all affected evidence must restart under the new versions.
- `reframe`: progress requires changing R0 or another contract in a way that changes the scientific question, task causal chain, central tradeoff, task/service meaning, intended contribution type, or conclusion applicability semantics.
- `blocked`: required evidence, executable resources, external authority, or a user decision is unavailable. Record the precise unblock condition; do not lower criteria.

No terminal status may hide failed configurations, substitute an easier problem, relax a material constraint without versioning, expose future or audit-only information, or reuse stale results.

## User-Visible Projection

Return the requested artifact or repaired behavior first. Then expose only the current status, authoritative versions, one decisive cause or conclusion, the single delta, checks actually invalidated and refreshed, and any limitation or decision that changes what the user can do next. Keep the full ledger and routine pass matrix internal unless requested.
