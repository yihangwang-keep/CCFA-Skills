---
name: ccf-experiment-debugger
description: "Coordinate evidence-led diagnosis, minimal repair, and repeated design-validation loops for communication environment or algorithm MVP failures. Use for Ralph loop, Ralph-loop, design-validation cycles, environment-algorithm revision, wrong, unstable, divergent, irreproducible, unexpectedly weak, or failed MVP results, 设计-验证-修改循环, 实验失败, MVP失败, 结果异常, 复现失败, 最小修改, 排查原因. Preserve the ordered environment-code, algorithm-code, algorithm-design, scenario-design ownership path and close every invalidated check. Do not design initial paper experiments or fabricate success."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Experiment Debugger

## Core Rule

Coordinate repair around `ccf-env-code-auditor` and `ccf-algorithm-code-auditor`; do not create a third audit protocol. Freeze the failed run and authoritative versions, locate the first confirmed owner, change one owned item, and rerun every invalidated check.

Use this ownership order:

```text
environment implementation
-> algorithm implementation
-> algorithm design
-> scenario design
```

The order controls modification, not blame. Decisive current evidence may identify a later owner directly, but every upstream contract on which that conclusion depends must already be accepted. Algorithm failure alone never authorizes a change to the paper scenario or formal optimization problem.

## Modes

- `diagnose`: isolate one failed or weak run, apply one minimal repair through its owner, and close affected checks.
- `design-validation-loop`: repeat design, implementation, MVP validation, independent audit, and minimal repair against one fixed loop instruction and persistent ledger until a valid terminal status is recorded.

For `diagnose`, load `references/diagnostic-protocol.md`. For `design-validation-loop`, load both debugger references and `../ccf-common/references/communication-research-terms.md`.

## Ordered Failure Gates

1. **Failure authority:** preserve the command, first divergence, paper-scenario and scenario-MVP versions, environment specification/code verdict, algorithm specification/code verdict, validation-contract version, configuration, seeds, criteria, logs, and outputs.
2. **Environment implementation:** use current `ccf-env-code-auditor` evidence to check authority, paper-problem consistency, equation-to-code traceability, semantics, independent execution, optimization fidelity, and central-tradeoff behavior. Repair a confirmed environment-code defect and rerun this auditor before continuing.
3. **Algorithm implementation:** after environment acceptance, use current `ccf-algorithm-code-auditor` evidence to check environment-contract consistency, design completeness, equation-to-code traceability, semantics, reference checks, and independent MVP behavior. Repair a confirmed algorithm-code defect and rerun this auditor.
4. **Algorithm design:** when both implementations match their accepted specifications but the mechanism or assumptions miss the formal target, route one formal change to `ccf-algorithm-designer`, then refresh implementation and algorithm-auditor evidence.
5. **Scenario design:** change the environment contract only when accepted evidence establishes a causal, mathematical, feasibility, complexity-balance, paper-scenario-to-MVP, or information-pattern defect. Route an environment amendment to `ccf-env-design`; after acceptance, rerun the complete affected environment, algorithm, and result chain.
6. **Closure:** apply the scope-specific terminal rules and accept only when the original failing case and every check invalidated by the delta pass under the same authoritative and validation-contract versions.

## Loop Discipline

1. Keep the paper scenario, formal problem, scenario MVP, environment, algorithm, fixed points, and the validation contract defined in `references/design-validation-loop.md` versioned in the ledger. Lock that contract before the first repair.
2. Start at the earliest missing, stale, failed, or contradicted check. Keep one owner, one active cause, and one delta per round.
3. For repository changes, work on a dedicated branch or worktree, record the round base before editing, and commit the single delta as a checkpoint. Invoke the existing `$code-review` skill in a fresh review agent against that fixed point and the frozen specification. Keep its Standards and Spec axes unchanged; do not reproduce them here.
4. Reuse `$diagnosing-bugs` for a hard implementation defect, `$tdd` when the requested repair is test-first, and `$research` when an environment amendment needs external task, physical, protocol, or service evidence. Keep their protocols in their owning skills.
5. Do not remove a failed case or relax the validation contract to obtain a pass. A material validation change needs its owning design skill, independent audit, a new contract version, and a terminal restart decision.
6. After any repair, mark dependent evidence stale before rerunning it. A verdict applies only to the exact artifact versions, validation contract, and reviewed `HEAD` recorded with it.
7. End only with `accepted`, `no-algorithmic-contribution`, `rebaseline-required`, `reframe`, or `blocked`. Apply their precedence rules; a loop limit or completion phrase is not acceptance evidence.

## Visible Output

Keep gate matrices, candidate comparisons, ownership history, and the complete ledger internal unless the user requests an audit record. Return the requested repaired artifact or diagnosis first, followed only by:

```text
Current status and authoritative versions:
Confirmed cause and decisive evidence:
Changed item and owner:
Checks invalidated and refreshed:
Supported conclusion or remaining blocker:
```

Never print empty headings or routine pass details.

## References

- `references/diagnostic-protocol.md`: failure record, owner selection, minimal delta, invalidation, and closure.
- `references/design-validation-loop.md`: frozen research layers, fixed loop instruction, persistent ledger, environment amendment, independent review, and terminal statuses.
- `../ccf-common/references/communication-research-terms.md`: communication research identity, environment authority, and amendment semantics used by the loop.
