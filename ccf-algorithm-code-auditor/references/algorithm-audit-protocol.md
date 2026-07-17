# Algorithm Code Audit Protocol

Use this protocol in the same order as `ccf-algorithm-code-auditor/SKILL.md` to verify an algorithm MVP on the accepted environment MVP.

Run the audit from the authoritative artifacts and raw execution evidence. A prior design, implementation, or repair verdict is an input to verify, not proof. The environment authorizes the formal problem; this audit must not change it.

## Evidence Status

- `declared`: present only in the formal target, algorithm spec, comment, or configuration;
- `wired`: reaches code but lacks independent behavioral evidence;
- `verified`: execution plus an independent check demonstrates the declared behavior;
- `contradicted`: code or execution conflicts with the authoritative algorithm design;
- `untestable`: required definitions, entry points, observables, or dependencies are missing.

## 1. Authority, Environment, And Design Contracts

Record the paper problem, paper parameter range, scenario MVP, environment version/verdict, interface version, algorithm specification/state, code revision, configuration, dependencies, seeds, metrics, evidence locations, and acceptance-criteria versions.

Confirm that the environment interface matches the algorithm's inputs, outputs, domains, feasibility signals, information timing, and task-causal semantics. Confirm that audit-only diagnostics, actual future realizations, exact decisions, and hidden state do not enter the algorithm-visible path.

Confirm that the algorithm design is `implementation-ready` and specifies the formal target, problem structure, family decision, derived mechanism, MVP path, termination, complexity target, original-problem evaluation semantics, and verification plan. An unresolved material `TBD`, stale environment version, or provisional design blocks acceptance.

## 2. Traceability Matrix

| ID | Formal target / algorithm step | Preconditions and semantics | Code symbol | Executed path | Independent check | Status | Consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Cover initialization, preprocessing, inputs, decisions, every update/search step, feasibility handling, surrogate or relaxation, recovery, original-objective evaluation, original-constraint checks, randomness, termination, checkpoints, solution extraction, metrics, and complexity accounting. Reverse-trace every behavior that changes them.

Keep the complete matrix in the working evidence record; show only rows that support material findings unless the user requests the full matrix.

## 3. Semantic Correctness

- Recompute one update/search step outside the implementation.
- Verify signs, normalization, gradients, dual variables, projections, relaxations, sampling, and update order as applicable.
- Verify stopping conditions against the declared residual, convergence, iteration, or budget target.
- Test invariants and feasibility after initialization, intermediate steps where required, and final solution extraction.
- Verify shapes, units, indices, action domains, masks, observations, and decision-time information.
- Verify that surrogate, relaxed, penalized, or decomposed computation does not silently replace the accepted objective or constraints.
- Verify recovery under the original feasible set, independent original-constraint residuals, final original-objective evaluation, and declared failure behavior without clipping, hard-coded paths, or undeclared fallback.

## 4. Reference Evidence

Compare hand-computable cases with expected objectives, decisions, and residuals. When feasible, enumerate or solve small instances exactly and report the optimality or feasibility gap under the accepted objective and constraints. For bounds, relaxations, theorems, or analytical references, state precisely what is certified, in which direction, and under which assumptions. Include tuned simple rules when their inability to resolve the central communication tradeoff is part of algorithm necessity.

## 5. Independent MVP Execution

Run the complete algorithm MVP through the accepted environment interface on the scenario MVP. Use predeclared cases, seeds, tolerances, budgets, metrics, and success criteria. Record feasibility, residuals, correctness/convergence indicators, numerical behavior, runtime/space, reproducibility, original objective values, and comparison conditions. A successful program exit is not acceptance evidence.

## 6. Ownership, Amendment, And Repair

Assign each failure to its earliest confirmed owner:

- algorithm code: specification-to-code, numerical, state-update, recovery, termination, or extraction defect;
- algorithm design: mechanism, assumption, feasibility method, or decision-budget mismatch with correct code;
- environment code: implementation contradicts the accepted formal environment;
- environment design: only when independent evidence identifies an unsupported constraint, inactive communication bottleneck, empty credible feasible range, objective/task mismatch, or complexity imbalance that algorithm-only repair cannot resolve.

Repair only confirmed algorithm-code defects here. For a possible environment-design defect, record the observed failure, versions, alternative algorithms and tuned simple rules checked, independent evidence, why algorithm-only repair is insufficient, minimal proposed change, impact on objective/feasible set/information pattern/task semantics, invalidated artifacts, and required reruns. Submit that Environment Amendment Request to the environment owner; do not approve or apply it in this audit.

## 7. Version Invalidation And Fresh Audit

- A formal environment, information-pattern, paper-range, or scenario-MVP change invalidates the complete algorithm audit and every dependent comparison and result.
- An interface-only environment change invalidates interface, information-timing, traceability, end-to-end, and dependent reproducibility checks.
- An algorithm-specification change invalidates all mapped code paths and downstream semantic, reference, and MVP checks.
- A code or configuration change invalidates affected traceability, semantic, reference, MVP, complexity, and reproducibility checks.

Preserve old evidence under its original versions. Rerun the original failure case and every invalidated check. The final verdict requires a fresh independent audit for which `reviewed_code_revision` and every authority version exactly match the current artifacts. A pass that repaired code is not the final independent pass.

## 8. Verdict

- `pass`: authority and contracts are consistent; material algorithm steps, reference behavior, and independent MVP criteria are verified.
- `conditional`: no contradiction is found, but decisive reference, seed, complexity, or execution evidence is incomplete.
- `fail`: algorithm design and code contradict, the environment contract is invalid, semantics/feasibility fail, reference evidence contradicts the implementation, or MVP criteria are missed.

Set `joint-ready` only for `pass` when the reviewed algorithm specification, code revision, environment version, reference evidence, and complete scenario-MVP execution are all current and mutually compatible. A conditional or stale verdict is not `joint-ready`.

Attach each finding to the earliest failed gate, exact code location, decisive evidence, minimal repair, and required reruns.

Maintain the complete evidence-status ledger and traceability matrix as working records. By default, show the user material findings, the version-bound verdict, decisive evidence, repairs/reruns, unresolved items, and next owner; provide the detailed records only on request.
