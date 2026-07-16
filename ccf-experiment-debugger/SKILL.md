---
name: ccf-experiment-debugger
description: "Coordinate diagnosis and minimal repair of failed environment or algorithm MVP runs using evidence from ccf-env-code-auditor and ccf-algorithm-code-auditor. Use for wrong, unstable, divergent, irreproducible, unexpectedly weak, or failed MVP results, 实验失败, MVP失败, 结果异常, 复现失败, 最小修改, 排查原因. Route confirmed environment-code, algorithm-code, algorithm-design, or scenario-design causes to the owning skill and close the loop with auditor reruns. Do not design initial experiments or fabricate success."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Experiment Debugger

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Treat failed runs, code, configurations, and unpublished results as private user data.

## Core Rule

Operate as the failure coordinator around the two implementation auditors. Do not create a third independent audit protocol. Freeze the failed run and its artifact versions, obtain or refresh environment-auditor evidence, obtain or refresh algorithm-auditor evidence, identify the first confirmed owner, apply the smallest change through that owner, and rerun every affected auditor gate.

Use this ownership order:

```text
environment implementation
-> algorithm implementation
-> algorithm design
-> scenario design
```

This order controls modification, not blame. Existing decisive evidence may identify a later owner directly, but every upstream contract on which that conclusion depends must already be accepted.

## Ordered Failure Loop

1. **Failure-authority gate:** record the failed command, first divergence, paper-scenario/MVP version, environment spec/code version, environment verdict, algorithm spec/code version, algorithm verdict, configuration, seeds, metrics, criteria, logs, and preserved outputs.
2. **Environment-auditor gate:** use `ccf-env-code-auditor` evidence to establish authority, design-contract consistency, model-to-code traceability, semantics, independent execution, optimization fidelity, and tradeoff behavior. Repair a confirmed environment-code defect through that auditor and rerun it before continuing.
3. **Algorithm-auditor gate:** after environment acceptance, use `ccf-algorithm-code-auditor` evidence to establish environment-contract consistency, algorithm-design completeness, equation-to-code traceability, semantics, reference checks, and independent MVP behavior. Repair a confirmed algorithm-code defect through that auditor and rerun it.
4. **Algorithm-design gate:** when both implementations match their specifications but the algorithm mechanism or assumptions fail the declared target, route the smallest formal mechanism change to `ccf-algorithm-designer`, then rerun `ccf-algorithm-code-auditor`.
5. **Scenario-design gate:** modify the scenario only when accepted audit evidence identifies a causal, mathematical, feasibility, complexity, or paper-to-MVP defect. Route the smallest scenario-contract change to `ccf-env-design`, rerun `ccf-env-code-auditor`, then refresh affected algorithm design and audit evidence.
6. **Closure gate:** accept the repair when the original failing case and all auditor gates invalidated by the change pass under the new authoritative versions. Otherwise record the remaining failure and continue from its confirmed owner.

Load `references/diagnostic-protocol.md` for the failure record, ownership ledger, minimal-change record, and rerun closure.

## Workflow

1. Preserve the original failed run and inventory available auditor reports.
2. Start at the earliest auditor gate whose evidence is missing, stale, or contradicted.
3. Keep one active root-cause hypothesis and change one owned contract or implementation item at a time.
4. Record the reason, owner, changed artifact/version, dependent gates, rerun command, and result.
5. Return the confirmed cause, minimal modification, refreshed auditor verdicts, and unresolved evidence.

## Output Contract

```text
Failure signature and authoritative versions:
Environment-auditor status:
Algorithm-auditor status:
Confirmed owner and evidence:
Minimal modification:
Invalidated and rerun gates:
Result after rerun:
Remaining failure or next owner:
```

## Reference

- `references/diagnostic-protocol.md`: auditor-centered failure isolation, ownership, minimal repair, and closure protocol.
