# Ralph Repair Loop

Ralph is a small, repeatable repair habit used by both phase skills. It is not
another state machine or audit owner.

## Every Round

1. Read the current document, code, and the concrete failure evidence.
2. Find the first check that is actually failing.
3. Make one focused change in the correct place: document, environment, or
   algorithm.
4. Keep the old evidence and write down what changed.
5. Rerun the failing check and the checks affected by that change.
6. Continue until the required audits pass or a missing input/resource makes
   further work impossible.

Do not hide a failure by deleting the central tradeoff, loosening a material
constraint, exposing future information, or changing the target after seeing
the result.

## The Two Phases

```text
Phase A: paper problem document
  -> minimal-but-complete MES/environment
  -> environment audit
  -> initial algorithm
  -> algorithm audit and repair
  -> freeze the accepted MES and algorithm

Phase B: current scenario + current code/results
  -> write an upgrade scenario document
  -> modify the existing environment
  -> environment audit
  -> modify and repair the algorithm
  -> algorithm audit and repair
```

Phase A may revise its problem document before the anchor is accepted when
evidence proves that the stated problem is infeasible, ill-posed, or missing a
causal requirement. Phase B may revise its own upgrade document when an
environment audit or algorithm diagnosis provides independent evidence of a
document/environment defect, then update and re-audit the existing environment;
it keeps the correction in the same upgrade document.
