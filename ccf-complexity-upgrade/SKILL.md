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

Phase B starts based the already accepted the scenario and its algorithm. The main purpose is to increase the problem's complexity and improves the algorithm mechanism. It does not
replace the scenario-upgrade request with an unrelated research problem.

The environment and algorithm auditors remain independent. This skill writes
the upgrade document, changes the existing implementation, and owns the
repair loop.

## First Write An Upgrade Scenario Document

Before editing code, you should clearly know the current accepted environment, algorithm, and
available experiment/results. Then write a new scenario document describing the
upgrade idea. If the user supplied a draft, complete it from the same evidence. The
document is the single authority for the Phase-B environment changes.

For example:

1. relation to the accepted scenario, including the 
   same scientific question and causal chain;
2. current implementation/results and the limitation they expose;
3. upgraded scenario background, the same scientific question and causal chain,
   and how the added complexity stresses the existing tradeoff;
4. semantics retained from the current scenario and the exact added complexity;
5. expected changes in the environment and algorithm, including the new tradeoff problem;
6. objective, constraints and feasibility;
7. algorithm must expose audit-visible fields that capture essential execution evidence. These fields allow auditors to determine where and why an upgraded algorithm fails when evaluated in a new environment.;
8. environment implementation to change;
9. algorithm mechanism to change, expected failure explanation, and acceptance
    evidence.

The new document may add complexity to the setting, but it must keep the same
research problem with the upgraded tradeoff problems. Do not make the problem total different from the origin or add complexity just to make an algorithm look better.

## Phase B Ralph Loop

The loop is deliberately short:

```text
accepted scenario + current code/results
  -> write upgrade scenario document
  -> modify the existing environment from that document
  -> environment consistency audit in a clean session
  -> modify the algorithm mechanism
  -> algorithm consistency audit in a clean session
  -> focused algorithm repair or upgrade-document/environment repair
  -> repeat the affected audit
  -> accepted upgrade
```

1. **Read the starting point.** Identify the current implementation's observed
   limitation and the exact complexity added by the upgrade document.
2. **Modify the existing environment.** Implement the document in the current
   scenario code, interfaces, traces, and independent checkers. This is a
   direct extension of the current scenario implementation.
3. **Audit the environment.** Invoke `ccf-env-code-auditor`in a new clean, read-only
   session to review the implementation of the environment but needn't to tradeoff check to verify the scenario again. If the code is
   inconsistent, fix the code. If issues are identified in the document semantics, correct the document first, then update the environment code accordingly and perform the audit again.
4. **Modify the algorithm.** Once the environment is coherent, use the observed
   failure and the new causal difficulty to change the algorithm mechanism and 
   implementation.
5. **Audit and repair.** Invoke `ccf-algorithm-code-auditor` to review the implementation of algorithm in a new clean, read-only session. If the finding is
   algorithmic, repair it with a decision rule that applies uniformly across all states. After every algorithm repair, invoke `ccf-algorithm-code-auditor` again in a new clean, read-only session; no repair round may bypass this independent audit. Once the algorithm is frozen, rerun it across the affected scenario matrix. Do not repair the algorithm in adding a scenario-specific rule because a remaining scenario performs poorly.
   Only when that evidence shows that the added problem itself is infeasible, revise the added semantics and re-design the existing environment but needn't to tradeoff check to verify the scenario again the record this scenario failure reason briefly.
6. **Finish the upgrade.** When the upgraded environment and algorithm both
   pass their audits for the current document, record the versions and the
   evidence. If the proposed addition no longer represents the same research
   question, stop and ask whether it should be handled as a separate scenario
   rather than silently treating it as this upgrade.

When a check fails, add one short failure note with the audit scope and reason.
Do not maintain a workflow state machine for these notes.

Read `references/phase-b-upgrade-contract.md` when writing the document and
`references/complexity-upgrade-record.md` when recording the loop.

## Handoff

Return the upgrade scenario document, the modified environment and checker
entry points, the environment audit, the modified algorithm and algorithm
audit, and any short failure reasons. Publication-range experiment planning
starts later in `ccf-pipeline-orchestrator`.
