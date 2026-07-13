---
name: ccf-experiment-designer
description: "Design CCF paper evidence packages: scenarios, simulation settings, baselines, metrics, ablations, robustness tests, result-table templates, and real-result figure/table presentation. Use for experiment design, evaluation-setting planning, baseline selection, ablation design, result tables, publication figures from supplied numbers, 设计实验, 对比实验, 消融, 结果图表. Do not invent results or perform primary communication objective/constraint/scenario design."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Experiment Designer

## Core Rule

Design experiments that test the paper's central claims. For an algorithmic contribution, require an explicit optimization or decision objective, an auditable solution process, and a theoretical or optimality reference. Do not accept or recommend a heuristic as the proposed algorithm. Heuristics may appear only as prior work or comparison baselines. Do not design an artificial win by stacking hand-written rules, simplifying away the claimed difficulty, or selecting thresholds that manufacture a gap. For communication, networking, systems, and optimization papers, structure evidence around the objective, constraints, coupling, feasibility, stress regimes, and oracle/bound comparisons. Build result tables and evidence-bound figure specs only from supplied real values or explicit placeholders. Never fabricate numbers, improvements, significance, ranks, or user-study outcomes. Publication-grade layout, palette, caption placement, and render QA belong to `ccf-visual-composer`. Follow the user's requested output shape: experiment plan, table, LaTeX table, figure spec, ablation list, or execution queue.

## Modes

- `design`: scenarios, simulation settings, baselines, metrics, ablations, robustness, efficiency, failure analysis, and execution priority.
- `result-template`: fill-in tables with `TBD` placeholders.
- `result-presentation`: result tables, figure evidence plans, chart specs, caption facts, and missing-value markers from supplied real results.

## Workflow

1. Identify target venue, paper type, central claims, available results, and whether the task is planning or presenting results.
2. Extract the storyline from the idea or draft. Use `../ccf-paper-writer/references/storyline-blueprint.md` only as a schema, not as a writing handoff.
3. Map every major claim to required evidence, reviewer question, scenario/simulation setting, baseline, metric, ablation, and robustness/failure test.
4. Clearly show what the metrics are for each claim judgment, and what evidence is needed to support the claim in the Claim-Evidence Matrix.
5. For an algorithmic paper, run the Algorithmic Contribution Gate in `references/evidence-design.md`. Reject every proposed method that contains a heuristic decision mechanism. A rule set, threshold policy, manually patched strategy, or empirical search procedure is not an admissible proposed algorithm, regardless of how it is named or whether other components are formalized.
6. Run the Scenario Integrity Gate in `references/evidence-design.md`. Require scenarios to preserve the claimed difficulty, cover credible variation, and be specified independently of the desired ranking. If the primary task is to create or judge a communication/networking optimization environment, follow CCFA handoff mode before using `ccf-experiment-env-design`.
7. If scenarios, simulation settings, objective/constraint references, or baselines are unknown, use public-safe search or hand off to `ccf-literature-searcher`; request both formulation and algorithm coverage and mark uncertainty instead of guessing.
8. Load `references/evidence-design.md` for venue-family expectations and `references/result-templates.md` for result tables.
9. For result presentation, preserve units, seeds, confidence intervals, scenario or setting names, and metric direction. Mark missing values explicitly.
10. Hand off to `ccf-visual-composer` for publication-grade figure/table layout, palettes, panel maps, captions, manuscript integration, and render QA.
11. When finishing the experiment design, check carefully that all claims are covered by the needed evidence and that experiments are logically designed. If sub-agents are available and their use is authorized, use them to verify and repair design flaws.

## Adaptive Output Contract

Return the requested artifact first. For a result table request, output the table. For a figure request, output the evidence-bound figure spec and caption facts, then name `ccf-visual-composer` as next owner for visual composition when needed. For a full experiment-design request, use this default structure:

```text
Mode:
Venue and assumptions:
Claim-evidence matrix:
Algorithmic contribution gate (when applicable):
Scenario integrity gate:
Scenario / simulation / formulation needs:
Baseline matrix:
Main experiments:
Ablations:
Robustness / failure / efficiency:
Result tables or figure specs:
Missing values:
Execution priority:
No-fabrication status:
Next CCFA owner:
```

## References

- `references/evidence-design.md`: experiment, scenario, simulation-setting, and evaluation-setting design.
- `references/result-templates.md`: fill-in result tables and presentation scaffolds.
