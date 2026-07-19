# Algorithm Audit Protocol

Use this protocol with `ccf-algorithm-code-auditor` when invoked by
`ccf-mes-validation` or `ccf-complexity-upgrade`. Its sole purpose is to check
whether the implementation faithfully executes the declared algorithm and
produces a solution for the stated scientific problem. The auditor reports
divergences; the invoking phase owner makes all repairs.

## 1. Define The Audit Scope

Bind the audit to the current scientific problem, algorithm specification,
implementation, and available execution evidence. Recheck the affected
behavior when any of them changes.

## 2. Check Algorithm Steps Against The Code

Compare the declared algorithm with the implementation and its actual behavior
as a whole. Decide whether the code correctly realizes the method, whether the
executed flow remains faithful to it, and whether the returned result is the
kind of solution required by the scientific problem.

Use code references, tests, assertions, or traces only as needed to support the
judgment and identify where a mismatch begins. Do not create a mapping table or
an exhaustive record of implementation details.

## 5. Findings And Handoff

```yaml
finding:
  audit: algorithm
  location: path:line
  reason:
```

The auditor reports the reason only and returns it to the invoking phase owner.
