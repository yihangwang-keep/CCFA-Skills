---
name: ccf-algorithm-code-auditor
description: "Check whether a communication algorithm is correctly implemented against its formal specification and required interfaces. Use for equation-to-code traceability, implementation correctness, and execution-flow verification inside ccf-mes-validation or ccf-complexity-upgrade. Report findings to the invoking phase owner; do not design or repair the algorithm."
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
interfaces, and available execution evidence. The auditor checks whether the
algorithm's operations and execution flow match the declared method and where
an observed run first diverges from that specification. The invoking
`ccf-mes-validation` or `ccf-complexity-upgrade` owner makes all repairs.

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

1. **Formula-to-code check:** map the formal equation and algorithm step to
   its implementation code.
2. **Implementation check:** verify that operations, variables, parameters match the specification.
3. **Execution-flow check:** verify that initialization, branch choices,
   updates, termination, and solution extraction execute in the declared order.

## Review And Handoff

Return every finding to the invoking phase owner. The phase owner repairs the
algorithm and requests the original failed check plus every affected check
again. The auditor does not modify code, select a replacement mechanism, or
route findings to another owner.

Return:

```text
Verdict: pass / conditional / fail
Invoking phase owner: ccf-mes-validation / ccf-complexity-upgrade
Specification and interface:
Algorithm specification and implementation:
Equation-to-code trace:
Implementation findings:
Execution-flow findings:
Required recheck:
Next owner: current phase owner
```

Read `references/algorithm-audit-protocol.md` for the detailed evidence
checklist.
