# Algorithm Audit Protocol

Use this protocol with `ccf-algorithm-code-auditor` when invoked by
`ccf-mes-validation` or `ccf-complexity-upgrade`. Its sole purpose is to check
whether the implementation faithfully executes the declared algorithm. The
auditor reports divergences; the invoking phase owner makes all repairs.

## 1. Define The Audit Scope

Identify the exact algorithm specification, required interfaces,
implementation, configuration, and available execution traces. Bind
the audit to those versions. Recheck affected steps when an input changes.

## 2. Check Algorithm Steps Against The Code

Compare the declared algorithm with its implementation. Confirm that every
algorithm step is present in the code and that no extra logic changes the
algorithm's meaning.

## 3. Check Implementation Correctness

This check answers two questions:

- **Is the algorithm implemented correctly?** Confirm that the code performs
  the declared algorithm steps and produces the expected results.
- **Does the algorithm solve the scientific problem?** Confirm that it uses
  the problem's required inputs and returns the kind of decision or solution
  required by the stated objective and constraints.

Report a finding when either answer is no.

## 4. Confirm The Executed Flow

Use tests, assertions, or traces to confirm that the actual execution order,
branch choices, updates, termination, and returned solution match the declared
steps. For each mismatch, report the first point where execution diverges from
the specification and cite the corresponding code and evidence.

## 5. Findings And Handoff

```yaml
finding:
  audit: algorithm
  location: path:line
  reason:
```

The auditor reports the reason only and returns it to the invoking phase owner.
