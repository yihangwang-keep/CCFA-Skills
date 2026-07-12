---
name: ccf-experiment-debugger
description: "Diagnose and repair failed research experiments whose results are wrong, unstable, unexpectedly weak, or inconsistent with expectations. Use for experiment failure analysis, unexpected results, reproduction failures, training divergence, metric anomalies, 实验失败, 结果不符合预期, 效果异常, 复现失败, 排查实验原因. Check code implementation first, algorithm design second, and scenario definition last; use ResearchWiki or public web evidence to find candidate solutions. Do not use for initial experiment planning or fabricate successful results."
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

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep failed-experiment diagnosis separate from initial experiment design, broad literature search, idea optimization, and manuscript review.

Treat experiment code, logs, configurations, unpublished results, and failure details as private user data. Load `../ccf-common/references/privacy-and-evidence.md` before web search. Never paste private code, paths, tokens, unpublished numbers, or distinctive private text into public queries.

## Core Rule

Diagnose in this fixed order:

```text
code implementation -> algorithm design -> scenario definition
```

Do not modify the algorithm until code defects have been tested and ruled out. Do not modify the scenario until both code and algorithm causes have been tested and ruled out. Stop at the first confirmed cause, apply the smallest justified fix, and rerun a controlled comparison before continuing.

ResearchWiki and web findings are candidate explanations, not proof of the local root cause. Confirm every adopted solution against the user's code and rerun evidence. Never tune thresholds, simplify scenarios, remove hard cases, or change metrics merely to make results match expectations.

## Workflow

1. Capture the failure signature: expected behavior, observed behavior, command, code/config version, environment, seed, logs, metrics, and the earliest point of divergence. Mark missing inputs instead of guessing.
2. Load `references/diagnostic-protocol.md` and run the code gate. Reproduce the failure, reduce it to the smallest case, and inspect implementation, data, configuration, metrics, baselines, randomness, environment, and stale artifacts.
3. If a code cause is confirmed, patch only the responsible code when the user authorized a fix, add a regression check, and rerun the failing case. Do not proceed to algorithm or scenario changes unless the failure remains.
4. After the code gate passes, run the algorithm gate. Check formulation-to-code consistency, assumptions, feasibility, objective direction, convergence/correctness evidence, and exact/oracle/bound comparisons. Proposed fixes must remain non-heuristic and comply with `../ccf-experiment-designer/references/evidence-design.md`.
5. After both earlier gates pass, run the scenario gate. Check whether the scenario violates method assumptions, is infeasible, lacks the claimed difficulty, or uses an invalid generator/protocol. Change it only for an external scientific or domain reason, then rerun every method under the same version.
6. At each gate, query ResearchWiki or the public web only with the smallest safe technical description needed. Record source, proposed mechanism, applicability, and the local test that confirmed or rejected it.
7. Return the root-cause ledger and the exact rerun needed. Use `confirmed`, `probable`, `ruled out`, or `unresolved`; do not claim success before the rerun passes.

## Output Contract

```text
Failure signature:
Current diagnostic gate:
Code checks and evidence:
Algorithm checks and evidence:
Scenario checks and evidence:
ResearchWiki / web findings:
Root cause and confidence:
Minimal fix:
Regression or controlled rerun:
Result after rerun:
Unresolved risks:
```

## Reference

- `references/diagnostic-protocol.md`: Load for the ordered code, algorithm, scenario, source-search, and verification gates.
