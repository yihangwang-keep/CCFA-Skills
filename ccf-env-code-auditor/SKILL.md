---
name: ccf-env-code-auditor
description: "Independently check that a communication environment implementation corresponds to its scientific-problem document, exposes the core tradeoff, and is supported by lightweight heuristic or random probes. Do not design or repair the environment or algorithm."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# Environment Code Auditor

## Boundary

Audit the environment against the current scientific-problem document and
environment contract. The document is authoritative. Decide whether the
implementation faithfully represents the stated scientific problem and keeps
its core mechanism and tradeoff observable. Report what is wrong; the
responsible owner repairs it. Algorithm behavior belongs to
`ccf-algorithm-code-auditor`.

## What To Check

Trace in both directions:

```text
document item -> code symbol -> static/probe evidence
observed behavior -> document item or necessary implementation detail
```

The audit uses one common contract for every scenario.

## Audit Modes

- `tradeoff-probe`: use simple labelled heuristics, parameter sweeps, or seeded
  random actions to probe whether the environment exposes the documented
  tradeoff.
- `repair-check`: verify a new artifact after the responsible owner makes a change.
- `acceptance-gate`: return a concise environment verdict and handoff.

## Ordered Audit Gates

1. **Scientific-problem check:** the  scientific-problem    
   itself can be reflected in the document. If the document is not scientific and cannot be implemented, report a document/design-contract finding.
2. **Document-to-code check:** map the scientific question, causal chain,
   objectives, constraints, information contract, and feasibility semantics to
   the environment code.
3. **Tradeoff check:** use heuristics, parameter sweeps,
   or seeded random actions to show that the documented competing goals remain
   observable in the environment.


## Review And Handoff

This skill is the environment audit step used by `ccf-mes-validation` and
`ccf-complexity-upgrade`. The phase owner implements the environment, this
skill audits it, and the phase owner repairs any finding. Return a concise
verdict and explain each material mismatch with its location, reason, and
supporting evidence. Do not repair or silently reinterpret the document.

Read `references/audit-protocol.md` for the audit procedure.
