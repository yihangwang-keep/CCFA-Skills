---
name: ccf-complexity-upgrade
description: "Use for Phase B: upgrade a current scenario by writing an upgrade scenario document from the current implementation and results, modifying and auditing the existing environment, then modifying and repairing the algorithm. Use for 场景升级 and complexity-upgrade Ralph loops."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# Phase B: Deepen The Accepted Scenario

## Purpose

Phase B starts after already having accepted the scenario and its algorithm. Phase B increases the problem's complexity, exposes where the current
algorithm stops working, and improves the algorithm mechanism. It does not
replace the scenario-upgrade request with an unrelated research problem.

The environment and algorithm auditors remain independent. This skill writes
the upgrade document, changes the existing implementation, and owns the
repair loop.

## First Write An Upgrade Scenario Document

Before editing code, read the accepted current environment, algorithm, and
available experiment/results. Then write a new scenario document describing the
upgrade. If the user supplied a draft, complete it from the same evidence. The
document is the single authority for the Phase-B environment changes.

For example:

1. relation to the accepted scenario, including the 
   same scientific question and causal chain;
2. current implementation/results and the limitation they expose;
3. upgraded scenario background, the same scientific question and causal chain,
   and how the added complexity stresses the existing tradeoff;
4. semantics retained from the current scenario and the exact added complexity;
5. added state, uncertainty, information timing, actions, and transitions;
6. objective, constraints, aggregation, and feasibility;
7. algorithm-visible interface, audit-only fields, and leakage rules;
8. parameter range, fixed reproducible configurations, traces, and independent
   checkers;
9. environment implementation changes and consistency-audit evidence;
10. algorithm mechanism to change, expected failure explanation, and acceptance
    evidence.

The new document may add complexity to the setting, but it must keep the same
question and causal tradeoff and explain why this is still the same research
problem. Do not add complexity just to make an algorithm look better.

## Phase B Ralph Loop

The loop is deliberately short:

```text
accepted scenario + current code/results
  -> write upgrade scenario document
  -> modify the existing environment from that document
  -> environment consistency audit
  -> modify the algorithm mechanism
  -> algorithm consistency audit
  -> focused algorithm repair or upgrade-document/environment repair
  -> repeat the affected audit
  -> accepted upgrade
```

1. **Read the starting point.** Identify the current implementation's observed
   limitation and the exact complexity added by the upgrade document.
2. **Modify the existing environment.** Implement the document in the current
   scenario code, interfaces, traces, and independent checkers. This is a
   direct extension of the current scenario implementation.
3. **Audit the environment.** Invoke `ccf-env-code-auditor`. If the code is
   inconsistent, fix the code. If the document's semantics need correction,
   append a new version/decision to the same upgrade document, then update the
   environment and audit again.
4. **Modify the algorithm.** Once the environment is coherent, use the observed
   failure and the new causal difficulty to change the algorithm mechanism or
   implementation.
5. **Audit and repair.** Invoke `ccf-algorithm-code-auditor`. If the finding is
   algorithmic, make algorithm fixes and solve this problem correctly to the best effort.
   In the end if independent evidence shows that the added problem itself is infeasible, revise the added semantics in then upgrade document and re-design the existing environment but needn't to use easy algorithmes to verify the scenario again. 
   Record each failure and its evidence simply in order to complete the repair process.
6. **Finish the upgrade.** When the upgraded environment and algorithm both
   pass their audits for the current document, record the versions and the
   evidence. If the proposed addition no longer represents the same research
   question, stop and ask whether it should be handled as a separate scenario
   rather than silently treating it as this upgrade.

Use record fields `in_progress`, `accepted`, and `blocked`.
Describe every failure in the round notes: what was found, what changed, what
was rerun, and whether the work can continue.

Read `references/phase-b-upgrade-contract.md` when writing the document and
`references/complexity-upgrade-record.md` when recording the loop.

## Handoff

Return the upgrade scenario document, the modified environment and checker
entry points, the environment audit, the modified algorithm and algorithm
audit, and the focused repair history. Publication-range experiment planning
starts later in `ccf-pipeline-orchestrator`.
