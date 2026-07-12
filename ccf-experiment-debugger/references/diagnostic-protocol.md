# Failed Experiment Diagnostic Protocol

Use this protocol when an experiment crashes, diverges, cannot be reproduced, produces implausible metrics, or underperforms the stated expectation.

## Failure Record

Record before changing anything:

```text
Expected behavior and evidence for that expectation:
Observed behavior:
First failing step or metric:
Run command and configuration:
Code revision and environment:
Dataset/scenario version:
Seeds and hardware:
Relevant logs and artifacts:
```

Preserve the original run. Change one factor at a time and keep a ledger of hypothesis, test, result, and conclusion.

## Gate 1: Code Implementation

Reproduce first. Prefer a deterministic minimal case and compare the last known-good run when available.

Check:

- entry point, configuration precedence, defaults, command-line overrides, and unused parameters;
- data loading, splits, ordering, leakage, normalization, units, shapes, masks, padding, and empty samples;
- objective sign, loss reduction, reward/penalty direction, gradient flow, update order, detach operations, clipping, and stopping conditions;
- state transitions, constraint enforcement, action bounds, indexing, off-by-one errors, and terminal handling;
- metric implementation, numerator/denominator, aggregation level, direction, evaluation mode, and baseline protocol;
- initialization, seeds, nondeterministic kernels, precision, device placement, dependencies, checkpoint loading, caches, and stale result files;
- a hand-computed toy case, assertion, invariant, unit test, or comparison with a trusted implementation.

Pass this gate only when the failure is reproducible and the relevant code path has positive checks, not merely because no exception was raised. If a defect is found, fix it and rerun before considering algorithm changes.

## Gate 2: Algorithm Design

Enter only after Gate 1 passes or a code fix fails to resolve the experiment.

Check:

- the implemented objective, variables, constraints, assumptions, and update rules match the stated formulation;
- the scenario lies within the algorithm's stated assumptions;
- feasibility, constraint residuals, convergence/correctness conditions, termination, and numerical stability;
- exact enumeration or solver on small instances, oracle behavior, certified lower/upper bounds, relaxation gaps, or the stated theoretical reference;
- one mechanism at a time through diagnostic ablation without changing evaluation rules;
- whether the expected result was supported by theory, prior evidence under a matching protocol, or only an unsupported expectation.

Do not introduce heuristic decisions, rule stacking, post-hoc patches, or threshold selection. An algorithm change must state the diagnosed mechanism, the formal change, and a falsifiable test. Rerun the same scenario and baseline protocol before accepting it.

## Gate 3: Scenario Definition

Enter only after Gates 1 and 2 pass or their fixes fail under controlled reruns.

Check:

- feasibility and consistency of scenario parameters and constraints;
- whether scale, dynamics, uncertainty, coupling, resource scarcity, or other difficulty matches the research claim;
- whether the generator, data distribution, workload, units, and boundary cases match domain evidence;
- train/validation/test separation, seed coverage, sampling bias, hidden filtering, and scenario-version drift;
- whether a simple rule solves the scenario, indicating that the motivating difficulty was removed;
- whether thresholds or ranges were selected after observing method rankings.

Modify a scenario only to correct an evidenced mismatch or invalid assumption. State the external reason, preserve the original result, version the change, and rerun all methods with equal tuning budgets. Never modify a scenario to manufacture a performance gap.

## ResearchWiki And Web Search

Use ResearchWiki first when a relevant local knowledge base is available. Locate it through a user-provided `/ResearchWiki`, `$RESEARCHWIKI_ROOT`, or a project-local `skills/ResearchWiki`; read its `SKILL.md`, then query problem, algorithm, experiment-pattern, effect-evidence, and reviewer-risk pages. Follow page sources and evidence status.

Use the public web when ResearchWiki has no relevant coverage or current implementation details are needed. Prefer official library documentation, upstream source code and issue trackers, primary papers, author repositories, and benchmark specifications. Search with public error text, API names, algorithm names, and public problem descriptions; do not expose private code or results.

For every retrieved candidate, record:

```text
Source and access date:
Claim or proposed mechanism:
Match to the local version and assumptions:
Local confirming test:
Outcome: confirmed / rejected / unresolved
```

Do not adopt a retrieved fix solely because it worked elsewhere.

## Completion Gate

A diagnosis is complete only when:

1. the failure is reproducible or its nondeterminism is characterized;
2. the cause is isolated by a controlled test;
3. the minimal fix is applied without changing unrelated factors;
4. the original failing case passes after the fix;
5. at least one regression, invariant, or repeated-seed check passes;
6. the result is reported honestly if it still does not meet the original expectation.
