# Algorithm Code Audit Protocol

Use this protocol in the same order as `ccf-algorithm-code-auditor/SKILL.md` to verify an algorithm MVP on the accepted environment MVP.

## Evidence Status

- `declared`: present only in the formal target, algorithm spec, comment, or configuration;
- `wired`: reaches code but lacks independent behavioral evidence;
- `verified`: execution plus an independent check demonstrates the declared behavior;
- `contradicted`: code or execution conflicts with the authoritative algorithm design;
- `untestable`: required definitions, entry points, observables, or dependencies are missing.

## 1. Authority, Environment, And Design Contracts

Record the paper problem, scenario MVP, environment version/verdict, algorithm spec/code, configuration, dependencies, seeds, metrics, and acceptance-criteria versions.

Confirm that the environment interface matches the algorithm's inputs, outputs, domains, feasibility signals, and information timing. Confirm that the algorithm design specifies the formal target, problem structure, family decision, derived mechanism, MVP path, termination, complexity target, and verification plan.

## 2. Traceability Matrix

| ID | Formal target / algorithm step | Preconditions and semantics | Code symbol | Executed path | Independent check | Status | Consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Cover initialization, preprocessing, inputs, decisions, every update/search step, feasibility handling, objective evaluation, randomness, termination, checkpoints, solution extraction, metrics, and complexity accounting. Reverse-trace every behavior that changes them.

## 3. Semantic Correctness

- Recompute one update/search step outside the implementation.
- Verify signs, normalization, gradients, dual variables, projections, relaxations, sampling, and update order as applicable.
- Verify stopping conditions against the declared residual, convergence, iteration, or budget target.
- Test invariants and feasibility after initialization, intermediate steps where required, and final solution extraction.
- Verify shapes, units, indices, action domains, masks, observations, and decision-time information.

## 4. Reference Evidence

Compare hand-computable cases with expected objectives, decisions, and residuals. When feasible, enumerate or solve small instances exactly and report the optimality or feasibility gap. For bounds, relaxations, theorems, or analytical references, state precisely what is certified and under which assumptions.

## 5. Independent MVP Execution

Run the complete algorithm MVP through the accepted environment interface on the scenario MVP. Use predeclared cases, seeds, tolerances, budgets, metrics, and success criteria. Record feasibility, residuals, correctness/convergence indicators, numerical behavior, runtime/space, reproducibility, and objective values.

## 6. Verdict

- `pass`: authority and contracts are consistent; material algorithm steps, reference behavior, and independent MVP criteria are verified.
- `conditional`: no contradiction is found, but decisive reference, seed, complexity, or execution evidence is incomplete.
- `fail`: algorithm design and code contradict, the environment contract is invalid, semantics/feasibility fail, reference evidence contradicts the implementation, or MVP criteria are missed.

Attach each finding to the earliest failed gate, exact code location, decisive evidence, minimal repair, and required reruns.
