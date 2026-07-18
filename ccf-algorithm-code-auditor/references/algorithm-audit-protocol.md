# Algorithm Code Audit Protocol

Use this protocol in the same order as ccf-algorithm-code-auditor/SKILL.md to
verify an algorithm path on the accepted environment, frozen anchor, and any
declared complexity stage. Load
../../ccf-common/references/implementation-review-protocol.md for the native
two-axis implementation review.

Run the audit from authoritative artifacts and raw execution evidence. A prior
design, implementation, or repair verdict is an input to verify, not proof. The
environment authorizes the formal problem; this audit must not change it.

## Evidence Status

- declared: present only in the formal target, algorithm specification, comment, or configuration;
- wired: reaches code but lacks independent behavioral evidence;
- verified: execution plus an independent check demonstrates the declared behavior;
- contradicted: code or execution conflicts with the authoritative algorithm design;
- untestable: required definitions, entry points, observables, or dependencies are missing;
- stale: the artifact digest or authority version no longer matches the evidence.

## 0. Native Algorithm Review Profile

The domain-contract-fidelity reviewer checks the accepted environment contract and
algorithm specification against the candidate implementation. Its frozen bundle
records the environment version, anchor MES version, active complexity stage,
algorithm specification, method
role, mechanism classification, artifact digests, configuration, commands, and
raw evidence. It traces:

~~~text
formal target/algorithm step -> code symbol -> executed path -> independent check
executed behavior -> authorized algorithm step or necessary implementation detail
~~~

It checks inputs, visible information, decisions, every update/search step,
feasibility, surrogate/relaxation, recovery, original-objective and
original-constraint evaluation, termination, extraction, failure behavior,
reference scope, and complete MES behavior. It does not redesign the
environment or choose a different algorithm family.

The implementation-assurance reviewer checks independent reference and checker
paths, original-failure detectability, reproducibility, seed/reset/configuration
isolation, error and solver-status handling, numerical/resource safety, and
absence of hidden information, clipping, or fallback. Both reviewers are fresh,
read-only, and independent. Missing reviewer capability or an unbound artifact
digest blocks acceptance.

## 1. Authority, Environment, And Design Contracts

Record the paper problem, paper parameter range, MES, environment version and
verdict, interface version, algorithm specification/state, method role,
mechanism classification, artifact set, configuration, dependencies, seeds,
metrics, evidence locations, and acceptance-criteria versions.

Confirm that the environment interface matches the algorithm's inputs, outputs,
domains, feasibility signals, information timing, and task-causal semantics.
Confirm that audit-only diagnostics, actual future realizations, exact
decisions, and hidden state do not enter the algorithm-visible path.

Confirm that the algorithm design is implementation-ready and specifies the
formal target, problem structure, family decision, derived mechanism, MES path,
termination, complexity target, original-problem evaluation semantics, and
verification plan. An unresolved material TBD, stale environment version,
provisional design, or missing role/classification blocks acceptance.

## 2. Traceability Matrix

| ID | Formal target / algorithm step | Preconditions and semantics | Code symbol | Executed path | Independent check | Status | Consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Cover initialization, preprocessing, inputs, decisions, every update/search step,
feasibility handling, surrogate or relaxation, recovery, original-objective
evaluation, original-constraint checks, randomness, termination, solution
extraction, metrics, complexity accounting, and role-specific fallback paths.
Reverse-trace every behavior that changes them. Keep the complete matrix in the
working evidence record; show only rows that support material findings unless
the user requests the full matrix.

## 3. Semantic Correctness

- Recompute one update/search step outside the implementation.
- Verify signs, normalization, gradients, dual variables, projections, relaxations, sampling, and update order as applicable.
- Verify stopping conditions against the declared residual, convergence, iteration, or budget target.
- Test invariants and feasibility after initialization, required intermediate steps, and final solution extraction.
- Verify shapes, units, indices, action domains, masks, observations, and decision-time information.
- Verify that surrogate, relaxed, penalized, or decomposed computation does not silently replace the accepted objective or constraints.
- Verify recovery under the original feasible set, independent original-constraint residuals, final original-objective evaluation, and declared failure behavior without clipping, hard-coded paths, or undeclared fallback.

## 4. Proposed-Method Eligibility

Read method_role and mechanism_classification from the authoritative algorithm
artifact before interpreting the code.

Record `no_heuristic_gate` as `required`, `not_applicable`, or `unresolved`, and
record its independent outcome as `no_heuristic_gate_status: pass | blocker |
unresolved | stale | not_applicable`. Only a current `pass` satisfies a proposed
method's eligibility requirement.

For method_role proposed, any heuristic decision mechanism is a blocker,
including rule-of-thumb, greedy or heuristic local search, metaheuristic,
manual patch, trial-and-error decision, or a hidden heuristic fallback/clipping
path. A wrapper, formal proof, certificate, or non-heuristic module elsewhere
does not erase a heuristic decision path. Emit finding
ALG-CONTRACT-NH-001 with severity blocker and fail the domain-contract-fidelity
axis. Do not downgrade it to a minor implementation issue.

For method_role baseline, reference, diagnostic, or environment_probe,
heuristics and simple rules are permitted. Verify that the role is explicit,
that the method is not presented as the proposed algorithm, and that its
information, feasibility, seed, tuning, and resource conditions are declared.

## 5. Reference Evidence

Compare hand-computable cases with expected objectives, decisions, and
residuals. When feasible, enumerate or solve small instances exactly and report
the optimality or feasibility gap under the accepted objective and constraints.
For bounds, relaxations, theorems, or analytical references, state precisely
what is certified, in which direction, and under which assumptions. Evaluate
recovered decisions under the original objective and constraints. Include
explicitly labelled tuned simple or heuristic rules only as comparison evidence;
their results do not satisfy the proposed-method no-heuristic gate.

## 6. Independent MES Execution

Run the complete algorithm path through the accepted environment interface on the
MES. Use predeclared cases, seeds, tolerances, budgets, metrics, role labels,
and success criteria. Record feasibility, residuals, correctness/convergence
indicators, numerical behavior, runtime/space, reproducibility, original
objective values, and comparison conditions. A successful program exit is not
acceptance evidence.

## 7. Ownership, Amendment, And Repair

Assign each failure to its earliest confirmed owner:

- algorithm code: specification-to-code, numerical, state-update, recovery, termination, extraction, or hidden-fallback defect;
- algorithm design: mechanism, assumption, role/classification, feasibility method, or decision-budget mismatch with correct code;
- environment code: implementation contradicts the accepted formal environment;
- environment design review: always after algorithm-code fidelity is current and the current route's documented algorithm-design repairs are exhausted; environment design then decides whether evidence identifies an inconsistent/infeasible authoritative problem, invalid environment-target witness, information mismatch, missing causal factor, objective/task mismatch, or only an algorithm-specific target failure.

Repair only confirmed algorithm-code defects through the implementation owner.
When a route-specific algorithm-design ledger is exhausted, record its route ID,
specification version, scope, failed repairs, alternative families/references/
probes checked when available, and any proposed cause. Submit a model-review
request through the debugger regardless of that proposed cause. Do not call it
an accepted amendment: only `ccf-env-design` may record the confirmed
classification and, for `model_defect`, create a non-simplifying evolution
proposal. `algorithm_specific` closes or supersedes the route; `unresolved` is
blocked. The repairer cannot review the candidate it changed.

## 8. Version Invalidation And Fresh Audit

- A `complexity_expansion` preserves the prior audit for the anchor authority tuple; run a fresh stage audit plus anchor regression and invalidate only stage-dependent comparisons or results. A legacy/exception MES successor preserves the prior audit for the parent tuple but cannot establish successor acceptance.
- A formal environment, information-pattern, paper-range, or other semantic change starts a new evidence epoch and invalidates the complete algorithm audit and every dependent comparison and result.
- An interface-only environment change invalidates interface, information-timing, traceability, end-to-end, and dependent reproducibility checks.
- An algorithm-specification, method-role, or mechanism-classification change invalidates all mapped code paths and downstream semantic, eligibility, reference, and MES checks.
- A code or configuration change invalidates affected traceability, semantic, eligibility, reference, MES, complexity, and reproducibility checks.
- A proposed-method no-heuristic classification change requires a fresh domain-contract-fidelity review; a hidden fallback discovered in an unchanged file is still a new blocker finding.

Preserve old evidence under its original versions. Rerun the original failure case
and every invalidated check. The final verdict requires a fresh native review
whose reviewers and artifact digests exactly match the current artifacts. A pass
that repaired code is not the final independent pass.

## 9. Verdict

- pass: authority and contracts are consistent; the role gate, material algorithm steps, reference behavior, native review axes, and independent MES criteria are verified;
- conditional: no contradiction is found, but decisive reference, role classification, seed, complexity, native-review, or execution evidence is incomplete;
- fail: design and code contradict, the environment contract is invalid, a proposed method violates the no-heuristic gate, semantics/feasibility fail, reference evidence contradicts the implementation, a native-review axis fails, or MES criteria are missed.

Set joint-ready only for pass when the reviewed algorithm specification,
method role/classification, artifact set, code, environment version, reference
evidence, native review, and complete MES execution are all current and mutually
compatible. A conditional, stale, not_run, or role-ambiguous verdict is not
joint-ready.

Attach each finding to the earliest failed gate, exact code location, decisive
evidence, minimal repair, and required reruns. Maintain the complete
evidence-status ledger and traceability matrix as working records. By default,
show material findings separately under domain-contract-fidelity and
implementation-assurance, the proposed-method eligibility result, the
version-bound verdict, repairs/reruns, unresolved items, and next owner.
