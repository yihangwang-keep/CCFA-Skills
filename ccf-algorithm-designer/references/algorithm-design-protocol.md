# Algorithm Design Protocol

Use this protocol after the paper scenario and its environment MVP pass environment audit.

## Input Authority

```text
Paper scenario and formal problem:
Scenario MVP:
Environment specification and code version:
Objective, constraints, and information pattern:
Environment acceptance evidence:
Unresolved assumptions:
```

The scenario MVP remains the paper problem with fixed parameters for one reproducible first implementation. Confirm that relationship from the environment specification before designing the algorithm.

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

## Algorithm MVP Contract

```yaml
algorithm_name:
algorithm_version:
authoritative_problem_version:
scenario_mvp_version:
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
```

The algorithm MVP is the first complete path through the real environment interface on the scenario MVP. Unit-sized cases may verify individual equations, while end-to-end acceptance uses the complete scenario MVP.

## Verification Sequence

| Step | Implemented scope | Required check | Pass condition | Owner |
| --- | --- | --- | --- | --- |
| 1 | Mathematical reference | hand-computable case or exact/oracle/bound | expected decision, objective, and residuals match tolerance | algorithm design |
| 2 | Environment interface | shape, unit, timing, mask, information checks | interface matches the formal information pattern | environment code |
| 3 | Feasibility path | independent constraint residuals and invariants | returned decisions satisfy declared constraints | algorithm code |
| 4 | Update/search step | equation-to-code comparison | implementation matches the derivation | algorithm code |
| 5 | Algorithm MVP end to end | termination, objective, reproducibility, complexity | scenario MVP meets predeclared acceptance criteria | algorithm audit |

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
