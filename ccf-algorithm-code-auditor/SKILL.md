---
name: ccf-algorithm-code-auditor
description: "Check whether a communication algorithm faithfully implements its specification, executes as declared, and produces a solution for the stated scientific problem. Use inside ccf-mes-validation or ccf-complexity-upgrade. Report findings to the invoking phase owner; do not design or repair the algorithm."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# Algorithm Code Auditor

## Boundary

Audit the algorithm implementation against its formal specification, declared
interfaces, scientific problem, and available execution evidence. Decide
whether the code faithfully implements the declared method, whether its actual
execution follows that method, and whether its result is a solution to the
stated problem. The invoking `ccf-mes-validation` or
`ccf-complexity-upgrade` owner makes all repairs.

## Core Rule

Use bidirectional evidence:

```text
formal step -> code symbol -> executed path -> observed result
executed behavior -> declared step or necessary implementation detail
```

Use the problem and environment documents only to identify the applicable
algorithm specification and required interfaces. Do not independently repeat
the environment audit.

## Ordered Checks

1. **Formula-to-code check:** confirm that the formal equations and declared
   algorithm steps are represented faithfully in the implementation.
2. **Implementation check:** confirm that the code correctly implements the
   algorithm and produces the kind of solution required by the scientific
   problem.
3. **Execution-flow check:** confirm from actual execution evidence that the
   implemented process and returned result follow the declared algorithm.

## Review And Handoff

Return every finding to the invoking phase owner. The phase owner repairs the
algorithm and requests another audit of the affected behavior. Return a concise
verdict and explain each material divergence with its location, reason, and
supporting evidence. The auditor does not modify the code or select a
replacement method.

Read `references/algorithm-audit-protocol.md` for the audit procedure.
