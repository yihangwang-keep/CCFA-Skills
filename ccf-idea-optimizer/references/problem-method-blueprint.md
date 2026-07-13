# Problem And Method Blueprint

Use this file when converting a rough direction into a CCF-A-ready problem and method plan.

## Problem Sharpening

A strong problem statement should answer:

```text
What is the task or phenomenon?
Who in the venue community cares?
What gap remains after the strongest prior work?
Why is the gap hard rather than merely unattempted?
What would become possible if it were solved?
What scope boundary prevents overclaiming?
```

Good CCF-A problems tend to have at least one of these properties:

- They expose a bottleneck that strong prior work cannot handle.
- They define a new setting that changes the technical requirements.
- They reveal a mismatch between common assumptions and real use.
- They connect two areas in a way that creates a new capability or question.
- They make a hidden evaluation gap measurable.

## Method Mechanism

Translate method labels into mechanisms:

```text
Input and output:
Key representation:
Main operation:
Optimization or inference objective:
Why the mechanism should address the root challenge:
Assumptions:
Failure modes:
Alternative designs rejected:
```

If the method is a combination of known components, identify the non-obvious interaction. If no interaction exists, the idea is likely an engineering assembly and needs a sharper contribution or a stronger formulation/evidence story.

For an algorithmic contribution, additionally require:

```text
Decision variables and constraints:
Solution procedure and termination:
Feasibility / correctness / convergence check:
Exact solver, oracle, bound, relaxation, or theoretical guarantee:
Optimality gap and qualifying guarantee / certificate:
```

Do not turn a collection of hand-written rules into an alleged algorithmic novelty by adding more conditions. Do not propose any algorithm containing a heuristic decision mechanism. Greedy heuristics, heuristic local search, metaheuristics, rules of thumb, manually patched procedures, and empirical trial-and-error procedures always fail this gate. A proof, certificate, formal wrapper, learned component, or non-heuristic module elsewhere creates no exception. If no meaningful objective, verifiable solution process, and guarantee or certificate exist, independently redesign or reject the algorithmic route.

## Scenario Validity

A new or modified setting must introduce a meaningful technical requirement while retaining the difficulty that motivates the research. Specify its real-world or scientific basis, constraint ranges, scenario generator or data provenance when needed, and how it differs from prior settings.

Reject scenario engineering that makes the task trivial for a simple rule, removes the central coupling or uncertainty, encodes the proposed method's assumptions into the evaluation setting, or chooses thresholds after seeing results to create a larger gap. If a simple rule solves the setting, restore the missing difficulty or narrow the contribution to the legitimate special case. Thresholds may represent domain constraints or sensitivity variables, but their selection rule and full relevant range must be visible.

## Coherence Filter

Before presenting an optimized idea, check:

- The problem setting and method assumptions are compatible.
- The proposed evidence can actually test the central claim.
- The contribution type matches the evidence type.
- The target venue audience would care about the problem, not only the technique.
- No module requires data, supervision, deployment access, or theoretical assumptions that conflict with another module.
- The idea does not rely on mutually exclusive claims such as "training-free" and "requires large fine-tuning" unless the distinction is scoped.

## Innovation Types

Classify the strongest honest contribution:

- New problem or setting.
- New method or architecture.
- New objective, inference procedure, or theoretical result.
- New data artifact, simulator, scenario setting, or evaluation method.
- New system design or deployment insight.
- New empirical finding or diagnostic analysis.
- New synthesis that resolves a known tension.

Avoid claiming all types. Pick the top one or two and make the evidence package serve them.

## Elegance Checks

An elegant idea usually has:

- One central insight that explains the method.
- A method whose parts are necessary, not decorative.
- A simple claim that can be tested directly.
- A failure mode that is understandable.
- A result that would teach the community something even if SOTA gains are modest.
- A design that removes a bottleneck or reveals a simpler formulation, not merely a longer pipeline.

## Fatal Idea Risks

Mark these early:

- The novelty collapses under a likely close paper.
- The problem is too narrow for the target venue.
- The method is a known trick with new terminology.
- The central claim cannot be tested with available resources.
- The evidence would require a dataset, proof, or system that cannot be built in time.
- The idea depends on hidden assumptions reviewers will reject.
