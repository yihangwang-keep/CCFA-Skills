# Experiment Design

Use this file when turning an optimized idea into a minimum convincing evidence package for a CCF-A submission.

For a full experiment plan, baseline search, simulation setting, evaluation setting, or result-fill table, use `ccf-experiment-designer` through the CCFA handoff mode. This file is the local lightweight evidence planner for idea optimization.

## Evidence Principle

Design experiments to answer the reviewer question, "Does the evidence test the central claim?" Do not add experiments for volume. Every experiment should defend novelty, soundness, significance, generalization, efficiency, or scope.

## Experiment Matrix

For each major claim, create:

```text
Claim:
Evidence needed:
Scenario / setting / formulation / proof / study:
Baselines:
Metrics:
Ablations:
Stress or robustness tests:
Failure analysis:
Expected reviewer concern answered:
```

## Baseline Rules

- Include the strongest close prior work when feasible.
- Separate reproduced baselines, reported numbers, and incompatible settings.
- Explain why any missing baseline cannot be run.
- Avoid unfair adaptation, extra data, or hidden tuning advantages.
- Add simple baselines that test whether the core mechanism is necessary.

## Ablation Rules

Use ablations to test mechanism, not only performance drops:

- Remove each core component.
- Replace the proposed component with a plausible generic alternative.
- Vary the key hyperparameter or threshold across a justified range; fix the selection rule before test evaluation and do not report only the value that maximizes the proposed method's lead.
- Show when the method fails.
- Include qualitative or diagnostic evidence when numeric metrics hide behavior.

## Algorithm And Scenario Integrity

For algorithmic ideas, define the objective, variables, constraints, assumptions, solver steps, termination, and feasibility or correctness checks before designing comparison tables. Require an exact solver, oracle, certified bound, relaxation, proven approximation/convergence property, or other defensible theoretical or optimality reference. Do not propose a method containing any heuristic decision mechanism, including a hybrid method with only one heuristic component. There are no proof, certificate, naming, or formal-wrapper exceptions. Heuristics may appear only as explicitly labeled baselines. If the proposed method contains a heuristic or lacks a qualifying guarantee or certificate, redesign or reject the algorithmic route before experiment planning.

Define scenarios independently of the desired result. Preserve the motivating difficulty, cover realistic and hard variations, use matched tuning budgets, and include a simple rule baseline. Do not stack rules or modify scenarios and thresholds merely to win under a chosen setting. If the rule baseline solves the setting, revise the setting or narrow the claim before expanding the experiment suite.

For communication, wireless, networking, UAV, edge, IoT, vehicular, satellite, or task-oriented communication ideas, use `ccf-env-design` through the CCFA handoff mode when the problem environment itself needs to be designed or audited. The local minimum check is: optimization target object, objective function, decision variables, channel/network model, binding constraints, uncertainty that affects decisions, coupled decisions, shortcut baseline, scenario simplicity, and explainable algorithmic structure.

## Venue-Specific Evidence

- ML/AI: ablations, seeds/statistics, data splits, robustness, compute, scaling, and diagnostic analysis.
- CV: visual comparisons, per-category or hard-case analysis, fair image/video settings, and failure cases.
- NLP: data quality, annotation agreement, leakage checks, human or automatic evaluation validity, and error taxonomy.
- DB/KDD/IR: scale, latency, memory, throughput, ranking metrics, operating-regime realism, and deployment constraints.
- Systems: end-to-end evaluation, component-level measurements, overhead, sensitivity, resource use, and operational failure cases.
- Communication/networking: objective function, decision variables, channel and mobility assumptions, interference, power/bandwidth/energy constraints, latency/reliability/AoI when relevant, fairness, online uncertainty, decoupled and rule baselines, oracle or bound, scenario simplicity, explainable mechanism, and stress tests.
- Security: threat model tests, bypass attempts, adaptive attacks, guarantees, responsible disclosure, and limitations.
- HCI: participant recruitment, tasks, measures, statistics, qualitative coding, ethics, and claim scope.
- Theory: theorem statement, proof sketch, examples, relation to known results, and limits of assumptions.

## Minimum Convincing Package

The minimum package should include:

1. Main result against close baselines.
2. Mechanism ablation or proof of why the method works.
3. Robustness, generalization, or stress test.
4. Limitation or failure analysis.
5. Reproducibility details sufficient for audit.

If this package cannot be built under the user's constraints, recommend narrowing the claim, changing venue, or pivoting the idea.
