---
name: ccf-experiment-debugger
description: "Coordinate evidence-led diagnosis, minimal repair, and Ralph-style design-validation loops for failed communication environment, MES, or algorithm-MVP evidence. Use for Ralph loop, design-validation cycles, environment-algorithm revision, wrong, unstable, divergent, irreproducible, unexpectedly weak, 实验失败, 设计-验证-修改循环, 最小修改. Preserve ownership, artifact identity, native independent review, and invalidated checks. Do not design initial experiments or fabricate success."
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

Coordinate existing owners and auditors; do not create a third domain audit. Freeze the failed evidence and current artifact set, find the earliest confirmed owner, apply one owned delta, and rerun the original failure plus every invalidated check.

Use this repair order:

```text
environment implementation -> algorithm implementation -> algorithm design -> scenario design
```

```text
algorithm route exhausted -> ccf-env-design environment/formal-model review
  -> algorithm_specific: close/supersede route; open a new route only if credible
  -> model_defect: authorize a non-simplifying formal-problem/MES successor
  -> unresolved: block without changing the environment
```

The order controls permission, not blame. One weak algorithm result stays algorithm-side. When environment L1 and algorithm-code fidelity are current but documented algorithm mechanism/family repairs still cannot pass, the debugger must open an environment/formal-model review. Only a confirmed model defect may change the authority, and the successor may complete or correct the model but never simplify the research problem.

## Modes

- `diagnose`: isolate and close one failure with the smallest owned repair.
- `design-validation-loop`: repeat design, execution, validation, audit, independent review, and one-delta repair against one fixed instruction and persistent ledger.

Load `references/diagnostic-protocol.md` for `diagnose`. Load both debugger references for a loop.

## Ordered Failure Gates

1. **Failure authority:** preserve the command, first divergence, authority versions, MES, implementation revisions, validation contract, configuration, seeds or traces, logs, and outputs in a digested artifact set.
2. **Environment L1:** require current `ccf-env-code-auditor` evidence that code is faithful to the environment design contract. Repair confirmed implementation defects before downstream reasoning.
3. **Environment L2:** require a frozen, method-independent MES and adequately tuned, budget-matched heuristic probes. If a probe reaches the predeclared joint target, keep any valid L1 verdict but set `algorithmic_need: not_demonstrated` and stop the algorithm-contribution route; never change the MES to force probe failure.
4. **Algorithm implementation:** after L1 and L2 acceptance, require current algorithm traceability, semantics, reference evidence, no-heuristic verification for `method_role: proposed`, and complete MES execution.
5. **Algorithm design:** when implementation matches its contract but the mechanism misses the formal target, route one mechanism or family revision to `ccf-algorithm-designer`. Preserve each failed revision; when credible algorithm repair is exhausted, create a repair-exhaustion record rather than accumulating patches.
6. **Environment and mathematical model:** an exhaustion record triggers `ccf-env-design` review. Accept a change only when evidence classifies a model defect, then version the corrected formal problem and successor MES. Reject weakening done for tractability or acceptance. A scenario-inconsistent item may be corrected only on independent evidence and must retain the causal difficulty and central tradeoff.
7. **Closure:** require the original case, invalidated checks, applicable domain audit, and both CCFA-native review axes to be current for the same candidate artifact set.

## Ralph Discipline

1. Freeze the research layers and validation contract defined in `references/design-validation-loop.md`; identify inputs by paths and content digests, not by a Git branch, commit, or `HEAD`.
2. Keep one fixed loop instruction. Put round-specific state only in the ledger. Select one active owner and one delta per round.
3. After a delta, mark every dependent result and review stale before rerunning it. The applicable code auditor coordinates fresh read-only contract-fidelity and implementation-assurance reviewers using `../ccf-common/references/implementation-review-protocol.md`.
4. Do not call external debugging, TDD, research, or generic code-review workflows from this protocol. An owner may use ordinary project tools needed for its single repair, but Ralph adds no branch, worktree, commit, installation, or publication-experiment behavior.
5. Do not remove a failed case, retune validation after seeing outcomes, expose audit-only information, or modify the environment to favor a method. Environment/model revision after exhausted algorithm repair must preserve the paper scenario's causal question and all material difficulty. A material authority change creates a successor version and invalidates dependent evidence.
6. End only with a domain-valid terminal status. A completion marker, loop limit, resource limit, or successful command exit controls continuation only; it is never scientific acceptance.

`Ralph` here names this domain design-validation iteration only.

## Internal Record And User Output

Keep artifact manifests, hypotheses, reviewer reports, gate matrices, and round history internal unless the user asks for the audit trail. By default return the repaired artifact or diagnosis first, then only:

```text
Status and authoritative versions:
Confirmed cause and decisive evidence:
Changed item and owner:
Checks and review axes refreshed:
Supported conclusion or blocker:
```

## References

- `references/diagnostic-protocol.md`: failure record, owner routing, one delta, invalidation, and closure.
- `references/design-validation-loop.md`: frozen layers, Ralph ledger, round protocol, scenario evolution, validation changes, and terminal status.
- `../ccf-common/references/implementation-review-protocol.md`: native independent reviewer lifecycle and artifact-set binding.
