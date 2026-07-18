# Environment Code Audit Protocol

Use this protocol in the same order as ccf-env-code-auditor/SKILL.md on the
current paper-scenario, formal-problem, parameter-range, frozen anchor
minimum executable scenario (MES), and declared complexity-stage versions. The
Layer-2 heuristic-probe contract is anchor-only; a complexity-stage audit uses
Layer-1 consistency and anchor regression instead. Load
../../ccf-common/references/implementation-review-protocol.md for the native
two-axis implementation review.

## Evidence Status

- declared: present only in a specification, equation, comment, name, or configuration;
- wired: reaches an executable path but lacks independent behavioral evidence;
- verified: execution plus an independent check demonstrates the specified behavior;
- contradicted: code or execution conflicts with the authoritative design;
- untestable: missing definitions, entry points, dependencies, or observables prevent verification;
- stale: the artifact digest or authority version no longer matches the evidence.

## 0. Native Environment Review Profile

The domain-contract-fidelity reviewer checks Layer 1 only: environment
code-to-design contract fidelity. Its frozen input bundle records the authority
versions, anchor MES version, complexity-stage version when active, environment implementation digests, configuration,
declared commands, and raw evidence.
The reviewer must trace both directions:

~~~text
scenario/problem item -> code symbol -> executed path -> independently observed behavior
code behavior -> authorized problem item or necessary implementation detail
~~~

It checks the paper scenario, formal problem, MES construction, objective,
constraints, state/action/observation/transition timing, units and indices,
feasibility/resource accounting, information availability, parameter range,
causal bottleneck, optimization fidelity, and central tradeoff. It does not
judge proposed algorithm performance or redesign the scenario. Layer 2 is not
delegated to this reviewer; the environment auditor coordinates the controlled
anchor-only heuristic sweep below.

The implementation-assurance reviewer uses the shared minimum assurance list:
independent accounting and checkers, original-failure detectability,
reproducibility, seed/reset/configuration isolation, error and solver-status
handling, numerical/resource safety, and absence of hidden information,
clipping, or fallback paths. Both reviewers are fresh and read-only. Missing
review capability or an unbound artifact digest is not a pass.

## 1. Authority And Design Contract

Record the paper-scenario, formal-optimization-problem, parameter-applicability
range, frozen anchor MES, complexity-stage, equation, environment-code, entry-point, configuration, seed,
unit, time-index, information-pattern, and artifact-set versions. Resolve
conflicts before drawing executable conclusions.

Confirm that the design artifact contains the scenario background, task causal
chain, causal bottleneck, scientific question, central tradeoff, supported
conclusion and applicability boundary, formal optimization problem,
problem-to-cause traceability, complexity evidence, paper-to-MES relation, and
decision-time information contract.

## 2. Traceability Matrix

Create one row per atomic item:

| ID | Problem/equation item | Meaning, unit, domain, time scale | Code symbol | Executed path | Independent check | Status | Consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Cover parameters, exogenous state, decision-time observations, decisions,
objective terms, constraints, transitions, randomness, initialization,
termination, metrics, MES settings, and audit-only diagnostics. Reverse-trace
every code path that changes state, objective, feasibility, decisions,
termination, information, or metrics. Keep the complete matrix in the internal
evidence ledger unless the user requests the full audit.

## 3. Semantic Correctness

Verify:

- minimize/maximize direction, signs, normalization, aggregation, discounting, and terminal terms;
- inequality/equality direction, tolerances, units, index sets, residuals, enforcement, and feasibility meaning;
- pre/post-decision timing, simultaneous/sequential updates, conservation, terminal transitions, and horizon indexing;
- observation timing, decision domains, masks, audit-only information, and absence of future-state leakage;
- random distributions, correlation, truncation, seed/reset behavior, configuration precedence, and metrics.

Recompute objective components, constraint residuals, resources, and state
conservation independently from traces.

## 4. Independent MES Execution

Run:

1. deterministic replay with frozen exogenous traces and seeds;
2. independent accounting outside the environment reporting path;
3. trace-wide bounds, non-negativity, conservation, monotonicity, symmetry, and domain invariants;
4. one-factor parameter and decision interventions with expected directional effects;
5. planned boundary configurations and repeated seeds;
6. complete MES load with runtime and numerical-stability measurement.

Verify that the MES preserves the paper problem's task causal chain,
objective, material constraints, decision coupling, information pattern,
feasibility meaning, and central tradeoff. Verify that fixed values lie inside
the stated parameter applicability range and follow its construction rule.

## 5. Optimization Fidelity

Check that every decision affects its specified transition, the decision space
is not overwritten, objective terms can affect preferred decisions, material
constraints can bind, feasibility is reported independently, and
environment-side masks, projections, or penalties match the authoritative
mathematical semantics.

## 6. Layer-2 Heuristic Tradeoff Resistance

For initial anchor acceptance, freeze the anchor MES version, evaluation cases,
decision-time information, feasibility rules, seeds, resource accounting,
tuning budget, and target before running the sweep. For a complexity-stage
audit, freeze the stage request and anchor-regression cases instead, and do not
run the heuristic sweep. Record the target's units, domain or formal basis, and
independent evidence that its objective value or central-tradeoff region is
feasible and attainable under the MES contract, such as a witness, exact
reference, certified bound, or accepted construction argument. An impossible,
unsupported, or post-selected target cannot establish algorithmic need.

Run fixed/static, applicable domain, greedy/myopic, decoupled, low-dimensional
tuned, and random-feasible rules through the same environment interface. Record
each as role environment_probe or baseline, not proposed algorithm. Sweep the
declared tuning dimensions and retain all settings, not only the best outcome.

Use identical decision-time information, feasibility rules, seeds, evaluation
cases, and resource/tuning budgets for every representative rule. The sweep
must be able to expose a rule that reaches the target; do not weaken the target
or alter environment parameters to manufacture a failure.

Record whether improving one side of the central tradeoff creates the expected
cost on the other, identify the executed causal bottleneck responsible, and test
planned boundary cases in the parameter applicability range. Mark the evidence
procedure complete only after the representative probes receive the declared
tuning and matched conditions. Set `algorithmic_need: demonstrated` only when
those probes still miss the predeclared target for a causally supported reason.
If a tuned rule reaches the target or handles all intended outcomes, retain
Layer-1 environment-validity, set `algorithmic_need: not_demonstrated`, and block
the algorithm-contribution handoff. A possible environment defect requires an
independent amendment request; never change parameters to preserve algorithmic
need.

A probe's heuristic nature is permitted in this section. The environment audit
must not label a probe as a proposed algorithm or apply the proposed-method
no-heuristic gate to it.

Record the initial, anchor-only Layer 2 result in the internal ledger:

~~~yaml
layer_2_heuristic_tradeoff_resistance:
  scope: anchor_only
  frozen_mes_version:
  complexity_stage_id:
  anchor_regression_required: true
  target:
  target_basis_and_units:
  target_attainability_evidence:
  feasible_reference_or_bound:
  tuning_budget:
  common_information_and_feasibility: true
  probe_roles: []
  sweep_settings: []
  evidence_status: complete | incomplete | invalid | stale | not_run
  algorithmic_need: demonstrated | not_demonstrated | contradicted | insufficient_evidence | stale
  evidence_refs: []
~~~

For a complexity-stage audit, do not create a new Layer-2 sweep. Record the
stage separately:

~~~yaml
complexity_stage_consistency:
  stage_id:
  anchor_mes_version:
  implementation_consistency: pass | conditional | fail
  anchor_regression: pass | conditional | fail
  inherited_anchor_algorithmic_need: demonstrated | not_demonstrated | contradicted | insufficient_evidence | stale
  l2_heuristic_probe_rerun: no
  evidence_refs: []
~~~

`evidence_status: complete` means the anchor-only target attainability is
supported and the predeclared sweep finished with matched information,
feasibility, cases, and budget; it does not mean that every probe failed. A
successful probe yields `complete` with `algorithmic_need: not_demonstrated`.
Use `incomplete` or `not_run` with `insufficient_evidence` when tuning or
fairness evidence is missing, `invalid` for an invalid sweep, and `stale` after
an authority or artifact change. A complexity-stage consistency record does not
change this L2 result and must not be marked invalid merely because the
algorithm performs poorly at the new stage.

## 7. Model Review And Amendment Evidence

When a route-specific algorithm repair ledger is exhausted, verify current
environment L1 and algorithm-code fidelity, bind the route ID/specification,
preserve the frozen anchor MES and failed complexity stage, attempted repairs
and references, and forward a model-review request
to `ccf-env-design`. The algorithm side may include a proposed classification,
but environment design records the authoritative `algorithm_specific`,
`model_defect`, or `unresolved` decision.

Only after the environment review completes with `confirmed_classification: model_defect`
and `decision: authorize_evolution` may it create an amendment proposal. That
proposal must answer all six questions:

1. **Authority and review:** are L1, algorithm-code fidelity, route-specific repair exhaustion, and the environment-owned `model_defect` decision current?
2. **Causal or formal necessity:** does task, communication, authoritative-problem infeasibility, invalid environment-target evidence, information, or modeling evidence require the change rather than an algorithm-specific target revision?
3. **Semantic preservation:** do the task outcome, scientific question, and central tradeoff remain unchanged?
4. **Information honesty:** does the decision-time interface still exclude future, hidden, and audit-only information?
5. **Method neutrality:** would the change still be justified without knowing which method benefits?
6. **Non-simplification:** is material difficulty preserved, with no weakening for tractability, ranking, or acceptance; and is any corrected item independently proven inconsistent with the paper scenario and replaced by semantics that retain the causal problem and central tradeoff?

One algorithm failure alone is insufficient, but a documented route exhaustion
always triggers formal environment review. `algorithm_specific` closes or
supersedes that route and returns to algorithm design when another credible route
exists; `unresolved` is blocked. If no non-simplifying model defect is confirmed,
keep the environment unchanged. If an accepted change alters
objective semantics, material constraints, information pattern, feasibility
meaning, or applicability, create a new environment version and candidate MES,
start a new evidence epoch, and invalidate all dependent algorithm, baseline,
and experimental evidence. The prior anchor remains historical; a complexity
stage never edits it.

## 8. Verdict And Readiness

- pass: initial anchor Layer 1 authority/design/code contracts and applicable native review axes are current and Layer 2 has `evidence_status: complete` under the predeclared target and budget; a complexity-stage pass instead requires stage consistency and anchor regression, while inheriting `algorithmic_need`;
- conditional: no contradiction is found, but a decisive Layer 1 trace, configuration, native review, anchor L2 target-basis/attainability/tuning/coverage item, or complexity-stage consistency/regression item is incomplete;
- fail: design and code contradict; material behavior is unverified; the MES changes the paper problem; optimization fidelity fails; the intended coupling or central tradeoff is inactive; or an applicable native-review axis fails.

Determine readiness separately:

- environment-valid: Layer 1 task causal chain, formal problem, applicability range, MES relation, and implemented semantics are coherent and verified to the required level; this status does not depend on the Layer 2 outcome;
- algorithmic-need: `demonstrated` only when the initial anchor Layer 2's properly tuned, predeclared probe sweep misses its target; later complexity stages inherit this value. Use `not_demonstrated`, `contradicted`, `insufficient_evidence`, or `stale` when supported by the current anchor record;
- interface-complete: the decision-time interface is sufficient for algorithm work and remains separated from audit-only evidence;
- native-implementation-review: pass only when both fresh applicable axes are current and pass on the same candidate artifact set;
- joint-ready: not issued here; it requires downstream algorithm specification and implementation acceptance against this environment version.

Attach each finding to the earliest failed gate, exact code location, decisive
evidence, minimal repair, invalidated gates, and required reruns. Preserve the
old artifact set when a repair creates a new candidate. In the user-visible
response, report only the requested artifact, readiness, supported conclusion
and applicability, decisive evidence, native-review axis findings, and material
next action unless a full ledger is requested.
