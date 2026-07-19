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
environment contract. The document is authoritative for objectives,
constraints, information timing, feasibility, and task meaning. Report what is
wrong; the responsible owner repairs it. Algorithm behavior belongs to
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

1. **Scientific-problem gate:** confirm the background, causal chain,
   scientific question, core difficulty, tradeoff, formal problem,
   applicability range, and information contract are complete in the code.
2. **Scientific-problem fidelity gate:** check whether the environment code
   represents the documented scientific question and core problem, preserves
   the relevant objective/constraint tension, and does not erase the intended
   tradeoff through hidden information, clipping, projection, or repair.
3. **Tradeoff-evidence gate:** use small, predeclared probes based on simple
   heuristics, parameter sweeps, or seeded random actions. The probes should
   show that generic choices do not trivially achieve both competing goals and
   that the environment makes the documented tradeoff observable.
4. **Acceptance gate:** return `pass`, `conditional`, or `fail`, with decisive
   evidence and the next owner.

## Review And Handoff

This skill is the environment audit step used by `ccf-mes-validation` and
`ccf-complexity-upgrade`. The phase owner implements the environment, this
skill audits it, and the phase owner repairs any finding. Do not repair findings
in this skill.

If the scientific-problem document contradicts itself, or cannot be
implemented consistently with the environment contract, report a
document/design-contract finding. Do not silently reinterpret or repair the
document as part of this audit.

Return a short report first:

```text
Verdict: pass / conditional / fail
Document-to-code findings:
Implementation traceability evidence:
Scientific-problem and tradeoff evidence:
Required repair and rerun:
Next owner: responsible owner
```

Read `references/audit-protocol.md` for the detailed trace and probe checklist.
