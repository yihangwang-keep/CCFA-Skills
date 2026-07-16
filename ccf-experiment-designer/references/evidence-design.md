# Evidence Design

Use this file to design CCF-A evidence packages without fabricating results.

## Evidence Principle

Start from the claim, not the table. Each experiment should answer one of these reviewer questions:

- Does the method solve the stated problem?
- Why does the mechanism work?
- Is the comparison fair and current?
- Does the result generalize across settings?
- What fails, when, and why?
- Can the work be reproduced or audited?
- Does the evidence match the venue's expectations?

## Venue-Family Evidence

AI/ML:

- Strong close baselines, simple baselines, ablations, seeds/statistics, compute, hyperparameters, robustness, scaling, and diagnostic analysis.

CV/multimedia/graphics:

- Visual comparison, qualitative failure cases, per-category or hard-case analysis, fair image/video settings, user or perceptual studies when needed.

NLP:

- Data quality, annotation agreement, leakage checks, automatic and human evaluation validity, error taxonomy, ethics, and task assumptions.

DB/KDD/IR:

- Realistic operating regime, scale, latency, throughput, memory, ranking metrics, indexing or pipeline cost, ablations, and deployment constraints.

Systems/networks/architecture/storage:

- Real bottleneck, implementation detail, end-to-end results, component-level measurements, sensitivity, overhead, operating-regime variation, operational boundaries.

Communication/wireless/networking optimization:

- Clear optimization target object, objective function, decision variables, channel and mobility assumptions, interference, bandwidth/power/energy constraints, queue/latency/reliability/AoI when relevant, uncertainty that changes decisions, coupled decisions, simple rule baselines, decoupled baselines, oracle or bound references, scenario simplicity, algorithm explainability, and stress regimes.

Security/crypto:

- Threat model, attacker capabilities, adaptive attacks, bypass tests, guarantees, false positives/negatives, disclosure, ethics, and assumptions.

HCI/CSCW/UbiComp:

- Research questions, participants, procedure, tasks, measures, statistics, qualitative coding, triangulation, ethics, and claim scope.

SE/PL/FM:

- Real programs, case suites, formal statements, proof sketches, soundness/completeness tradeoffs, threats to validity, usability where relevant.

Theory:

- Formal model, theorem statement, proof roadmap, examples, lower/upper-bound relationship, relation to barriers and open problems.

## Baseline Matrix

Use this before proposing experiments:

```text
Baseline:
Why included:
Source / citation needed:
Implementation source:
Fairness constraints:
Expected metric:
Can run? yes / no / unknown
If missing, reason:
```

Baseline categories:

- Closest prior method.
- Current strong method.
- Simple sanity baseline.
- Ablated version of the user's method.
- Human, oracle, random, heuristic, or classical baseline when meaningful.
- Deployed or default system baseline for systems/HCI/security tasks.

## Algorithmic Contribution Gate

Apply this gate when the claimed contribution is an algorithm, optimizer, scheduler, controller, planner, policy, or solver. Record `not applicable` with a reason for non-algorithmic work.

1. **Formal target:** state the objective or decision criterion, decision variables, constraints, assumptions, and single- or multi-objective tradeoff. A metric used only after execution is not automatically an optimization objective.
2. **Auditable solution process:** specify initialization, update or search steps, termination condition, feasibility handling, randomness, hyperparameters, and computational complexity. Another researcher should be able to trace how an input becomes a solution.
3. **Verification:** test feasibility and constraint satisfaction on every run. Add convergence, correctness, invariant, residual, or reproducibility checks appropriate to the solver.
4. **Optimality or theory reference:** use an exact solver, exhaustive search on small instances, oracle, certified lower/upper bound, relaxation, proven approximation ratio, convergence theorem with a stated solution target, regret bound, or domain-specific analytical reference. State the optimality gap and what the reference does or does not certify.
5. **No-heuristic rule:** the proposed algorithm must contain no heuristic decision mechanism. Reject rule-of-thumb, greedy heuristic, heuristic local search, metaheuristic, manually patched, and empirical trial-and-error procedures without exception. Adding a proof, certificate, formal wrapper, learned component, or non-heuristic module elsewhere does not make a method containing a heuristic mechanism admissible. Heuristics may be retained only as prior-work or comparison baselines and must be labeled as such.
6. **Mechanism over rule accumulation:** every rule or component must follow from the formulation, enforce a real constraint, or test a named mechanism. Remove decorative rules whose only purpose is improving the reported score.

If the proposed method contains any heuristic decision mechanism, reject the proposed algorithmic route and redesign it before adding more experiments. Separately, reject it if no meaningful objective, verifiable solution process, and qualifying guarantee or optimality reference can be defined. Renaming a heuristic as a policy, framework, strategy, adaptive algorithm, hybrid method, or learned rule does not pass this gate.

For the experiment-design stage, do not recreate this upstream design work. Require and cite the accepted `ccf-algorithm-designer` specification and `ccf-algorithm-code-auditor` evidence. Missing design or implementation acceptance routes back to its owner; it is not repaired by adding more baselines or ablations.

## Scenario Integrity Gate

Define and freeze scenario generation before using outcomes to choose favorable cases.

- **Preserve the bottleneck:** simplification must not remove the uncertainty, coupling, scarcity, scale, dynamics, partial observability, strategic behavior, or other difficulty that motivates the claimed method.
- **Independent construction:** derive scenarios from real data, domain ranges, standards, or method-independent generators. Do not construct scenarios around the proposed method's rules or failure thresholds.
- **Coverage:** include realistic, diverse, hard, boundary, and failure cases. Report the sampling distribution, seeds, exclusions, and any post-hoc filtering.
- **No threshold-manufactured gap:** choose thresholds from domain meaning, training/validation data, or a preregistered rule. Apply matched tuning budgets to all tunable methods and report sweeps or sensitivity. Never select a test threshold because it maximizes the proposed method's lead.
- **Rule-baseline check:** include a simple rule-based baseline. If it solves the simplified scenario, either restore the missing difficulty, justify the scenario as a legitimate special case, or narrow the novelty claim; do not add more ad hoc rules to reclaim a lead.
- **Controlled modification:** when changing a scenario, state the external reason, the affected assumption, and whether all methods are reevaluated under the same version. Keep the original result visible when the change follows result inspection.

Fail the gate when the principal advantage disappears under credible scenario variation, matched tuning, or a simple rule baseline and the paper still claims a general algorithmic advance. Treat that outcome as evidence to revise the problem or claim, not as a reason to engineer a more favorable setting.

MVP success establishes end-to-end implementation and mechanism evidence. Map broader claims about scale, uncertainty, dynamics, or parameter ranges to explicit additional experiments before using them in the paper.

## Ablation Logic

Each ablation should test a mechanism:

```text
Component or assumption:
Why it matters:
Replacement or removal:
Metric affected:
Expected interpretation if it fails:
```

Useful ablations:

- Remove a module.
- Replace a specialized component with a generic alternative.
- Vary a key hyperparameter.
- Change scale, scenario regime, or domain.
- Test hard cases and failure cases.
- Analyze compute, memory, latency, or cost.

Threshold sweeps are sensitivity analysis, not evidence of mechanism by themselves. Fix the selection rule before test evaluation, use the same tuning budget for comparable baselines, and show the full relevant range rather than only the threshold with the largest gap.

If the algorithm method is not a combination of mechanisms, do not invent ablations. And we encourage to create a new algorithmic mechanism to support the claim, rather than just combine existing mechanisms. But we can update the existing mechanism to fit the new situation in order to support the claim.

## Scenario, Simulator, Or Dataset Design(if needed)

For a new scenario generator, simulator, trace, or dataset:

```text
Task definition:
Data source:
Annotation or generation process:
Scenario or simulator generation process:
Splits:
Metrics:
Baseline suite:
Leakage checks:
Difficulty and diversity:
Human or expert validation:
License and ethics:
Maintenance plan:
```

Trace, simulator, or scenario-generator papers should be evaluated as evidence artifacts, not only as methods. Do not score them as weak because they lack a method, and do not invent adoption claims.

## Minimum Convincing Package

For most CCF-A submissions:

1. Main comparison against close and strong baselines.
2. Mechanism ablation or proof.
3. Robustness/generalization/stress test.
4. Failure analysis or limitation study.
5. Reproducibility details.

If this package is infeasible, narrow the central claim before adding weaker experiments.
