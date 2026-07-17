# Algorithm Design Protocol

Use this protocol after the paper scenario and its environment MVP pass environment audit. If authority or audit evidence is incomplete, use it only to produce a provisional design.

The environment authorizes the formal problem in one direction. The algorithm consumes that problem; it does not rewrite the scientific question, objective, decision variables, constraints, information pattern, feasibility meaning, task-causal semantics, paper parameter range, or scenario MVP.

## Contents

- Input authority and design state
- Formal target and algorithm-family decision
- Derived mechanism and environment-information boundary
- Algorithm MVP, verification, evidence, and revision records

## Input Authority

```text
Paper scenario and formal problem:
Paper parameter range:
Scenario MVP:
Environment specification and code version:
Objective, decision variables, constraints, and information pattern:
Feasibility meaning and task-causal semantics:
Environment acceptance evidence:
Unresolved assumptions:
```

The scenario MVP remains the paper problem with fixed parameters for one reproducible first implementation. Confirm that it preserves the scientific problem, objective, decision variables, key constraints, information pattern, feasibility meaning, task-causal semantics, and central communication bottleneck. A simpler replacement problem is not the scenario MVP.

## Design State

- `provisional`: at least one authority, interface, assumption, or acceptance item that can change the mechanism remains unresolved.
- `implementation-ready`: the accepted environment version is pinned, every applicable design gate is closed, the environment interface is sufficient, and each implementation step has an executable acceptance check.

Record the state in the algorithm artifact. A later environment version never inherits the earlier implementation-ready status.

## Formal Target And Problem Structure

```text
Decision variables and domains:
Objective and solution target:
Constraints and feasibility semantics:
Information timing and observability:
Online/offline and deterministic/stochastic structure:
Convex, nonconvex, combinatorial, or decomposable structure:
Dynamics and uncertainty:
Scale and computational budget:
Required correctness, convergence, approximation, regret, or optimality evidence:
```

Complete this analysis before selecting an algorithm family.

## Algorithm-Family Decision

For each credible family, record:

```text
Candidate family:
Matching problem structure:
Required assumptions:
Solution target or guarantee:
Feasibility handling:
Information and compute requirements:
Decision: select / reject / unresolved
```

Select the least complex family that addresses the accepted formulation and evidence target.

Include exact or enumerated solutions, certified bounds, and tuned simple rules when applicable. A more complex mechanism is justified only when the accepted problem and measured decision budget expose a limitation that the simpler alternatives cannot resolve.

## Derived Mechanism And Evaluation Semantics

For every mechanism, record its source in the formulation. For any computational replacement of the original problem, record:

```text
Original objective and constraints:
Surrogate, relaxation, penalty, decomposition, or bound:
Purpose and required assumptions:
Direction and scope of the bound, if any:
Recovery or projection into the original feasible set:
Independent residual check on the original constraints:
Final evaluation under the original objective:
Failure behavior without hidden fallback:
```

An internal objective or relaxed feasible set does not replace the environment contract. Report final decisions, feasibility, and objective values using the accepted environment semantics.

## Environment Information And Amendment Boundary

For every requested input or diagnostic, state its meaning, unit, time index, and availability time. Separate:

- algorithm-visible information authorized by the formal information pattern;
- audit-only information such as actual future realizations, exact decisions, hidden state, or checker-only statistics.

If an authorized mathematical quantity is missing only from the code interface, request an interface change and require environment-code audit. If the request would change the formal problem or expose information unavailable at decision time, do not implement it. Submit this Environment Amendment Request to the environment owner:

```yaml
observed_failure:
authority_versions:
algorithm_families_and_simple_rules_checked:
independent_evidence:
why_algorithm_only_repair_is_insufficient:
identified_environment_defect:
proposed_minimal_change:
objective_and_feasible_set_impact:
information_pattern_impact:
scientific_problem_and_task_semantics_preserved:
method_neutrality:
invalidated_artifacts:
required_reruns:
```

The algorithm designer cannot approve or apply this request. A timeout, weak result from one algorithm, or desire for an easier solver is not independent evidence of an environment defect. If the environment owner accepts a material change, create a new environment version and restart algorithm design from the authority gate.

## Algorithm MVP Contract

```yaml
algorithm_name:
algorithm_version:
authoritative_problem_version:
environment_version:
environment_interface_version:
scenario_mvp_version:
design_state: provisional | implementation-ready
solution_target:
assumptions:
inputs_and_information_timing:
decision_outputs:
initialization:
algorithm_mechanism:
update_or_search_steps:
feasibility_handling:
termination:
randomness_and_seed_control:
complexity_target:
environment_information_needed:
original_objective_evaluation:
original_constraint_checks:
acceptance_criteria:
```

The algorithm MVP is the first complete path through the real environment interface on the scenario MVP. Unit-sized cases may verify individual equations, while end-to-end acceptance uses the complete scenario MVP.

## Verification Sequence

| Step | Implemented scope | Required check | Pass condition | Owner |
| --- | --- | --- | --- | --- |
| 1 | Mathematical reference | hand-computable case or exact/oracle/bound | expected decision, objective, and residuals match tolerance | algorithm design |
| 2 | Environment interface | shape, unit, timing, mask, information checks | interface matches the formal information pattern | environment code |
| 3 | Feasibility path | independent original-constraint residuals and invariants | returned decisions satisfy declared constraints | algorithm code |
| 4 | Update/search step | equation-to-code comparison | implementation matches the derivation | algorithm code |
| 5 | Algorithm MVP end to end | termination, original objective, reproducibility, simple-rule comparison, complexity | scenario MVP meets predeclared acceptance criteria | independent algorithm audit |

## Working Evidence Record

Keep family tables, gate results, evidence locations, and rerun dependencies in the working record. The default user-facing artifact contains the selected mechanism, decisive evidence, current design state, unresolved items, and implementation contract; include full tables only when requested.

## Revision Record

```text
Observed evidence:
Diagnosed owner:
Changed assumption, mechanism, interface, or scenario item:
Reason for the change:
Artifact versions updated:
Verification checks to rerun:
Outcome:
```

A completed revision preserves an explicit relationship among the paper problem, scenario MVP, environment implementation, algorithm specification, and measured evidence.

Apply these invalidation rules:

- A formal environment, information-pattern, paper-range, or scenario-MVP version change invalidates every dependent algorithm design state, implementation verdict, comparison, and result.
- An environment-interface-only change invalidates interface, timing, end-to-end, and dependent reproducibility checks.
- An algorithm-specification change invalidates the mapped implementation paths and every downstream check that exercises them.
- A code or configuration change invalidates the affected semantic, reference, MVP, complexity, and reproducibility checks.

Preserve prior evidence as versioned history; never relabel it as evidence for the new version. Rerun the original failure case and every invalidated check, then obtain a fresh independent algorithm-code audit against the exact current versions.
