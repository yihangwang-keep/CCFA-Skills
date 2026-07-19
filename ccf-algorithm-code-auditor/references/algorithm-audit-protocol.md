# Algorithm Audit Protocol

Use this protocol with `ccf-algorithm-code-auditor` when invoked by
`ccf-mes-validation` or `ccf-complexity-upgrade`. It keeps the algorithm check
traceable while leaving all repairs to the invoking phase owner.

## 1. Input Bundle

Record the invoking phase owner, applicable algorithm specification, required
interfaces, algorithm code, configuration, seeds, tests, execution traces, and
acceptance criteria. Bind the report to exact versions or content digests. A
changed input requires the affected checks to run again.

## 2. Traceability Matrix

Create an internal row for each material algorithm step:

| Step | Declared meaning | Code path | Executed evidence | Result |
| --- | --- | --- | --- | --- |
| initialize/update/decide/recover/terminate | inputs and output | symbol and call path | trace, assertion, or test | pass/fail |

Also map feasibility handling, objective evaluation, randomness, resource
limits, and termination behavior. Reverse-trace code that changes a decision
or reported metric.

## 3. Semantic And Interface Checks

Verify:

- objective direction, units, aggregation, and original-objective evaluation;
- decision domains, masks, constraints, feasibility signals, and recovery;
- state/observation timing and absence of future or audit-only information;
- equation signs, indices, update order, residuals, stopping rules, and
  solution extraction;
- seed/reset behavior, numerical stability, termination, and resource limits.

For `method_role: proposed`, inspect every decision component for hidden
heuristic fallback, clipping, or manual repair. Label simple rules explicitly
when they are probes or baselines.

## 4. Execution Flow Check

Inspect the algorithm's actual execution order, state transitions, branch
conditions, updates, recovery, and termination. Report each declared algorithm
step and code path whose observed behavior contradicts the specification,
together with the relevant code and execution evidence.

Use the invoking phase's declared configuration, seeds, tolerances, metrics,
and resource limits. Record feasibility, objective values,
correctness/convergence indicators, execution trace, numerical behavior,
runtime/space, and reproducibility.

## 5. Findings And Rechecks

```yaml
finding:
  location: path:line
  observed:
  expected:
  consequence:
  required_recheck:
```

The auditor reports findings only. Return every finding to the invoking phase
owner. That owner makes a focused repair, keeps the previous check evidence,
and requests the original failed check plus all affected checks again.
