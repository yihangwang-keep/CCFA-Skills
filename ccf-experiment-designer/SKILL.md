---
name: ccf-experiment-designer
description: "Design communication-paper evidence after accepted paper-scenario, environment, and applicable algorithm MVP evidence: parameter-range coverage, simulation settings, baselines, metrics, mechanism tests, robustness, result templates, and presentation plans. Use for experiment design, baseline selection, ablation design, result tables, publication figures from supplied numbers, 设计实验, 对比实验, 消融, 结果图表. Do not invent results, redo upstream environment or algorithm design, or mix evidence from incompatible versions."
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

Consume accepted upstream evidence; do not recreate environment or algorithm design inside experiment planning. Map each intended paper conclusion and its applicability range to the smallest discriminating set of settings, baselines, metrics, mechanism tests, robustness checks, and failure evidence. Keep the paper scenario, formal optimization problem, parameter applicability range, scenario MVP, objective, constraints, information pattern, and feasibility meaning version-consistent.

For an algorithmic contribution, retain the accepted gate that requires an explicit objective, an auditable solution process, a qualifying theory or optimality reference, and no heuristic decision mechanism in the proposed method. Heuristics remain comparison baselines only. Build result artifacts exclusively from supplied real values, verified matching public values, or `TBD` placeholders. Publication layout belongs to `ccf-visual-composer`.

## Modes

- `design`: conclusion coverage, settings, baselines, metrics, mechanism tests, robustness, efficiency, failure analysis, and execution priority.
- `result-template`: fill-in tables with `TBD` placeholders.
- `result-presentation`: result tables, figure evidence plans, chart specifications, caption facts, and missing-value markers from supplied results.

## Upstream Acceptance Gate

Before paper-range design, record the accepted versions of:

- paper scenario, formal optimization problem, parameter applicability range, and scenario MVP;
- environment specification/code and `ccf-env-code-auditor` verdict;
- algorithm specification/code and `ccf-algorithm-code-auditor` verdict when the paper presents an algorithmic contribution;
- exact solver, oracle, certified bound, independent checker, or other accepted reference used by the conclusions;
- unresolved limitations and the parameter settings they exclude.

If an applicable item is missing, stale, conditional outside the requested range, or version-incompatible, stop the affected experiment branch and route it to its owner. Use `ccf-experiment-debugger` for failed or inconsistent evidence. Do not repair an upstream defect by adding experiments.

## Workflow

1. Identify the target venue, paper type, intended conclusions, conclusion applicability range, accepted artifact versions, available results, and requested mode.
2. Build an internal conclusion-evidence ledger: for every major conclusion, record the decisive question, required setting, baseline, metric, mechanism test, robustness/failure test, and a result-dependent interpretation rule.
3. Apply the Algorithmic Contribution Gate in `references/evidence-design.md` only to algorithmic work. Consume the upstream acceptance record; route a failure to `ccf-algorithm-designer` or `ccf-algorithm-code-auditor`.
4. Apply the Scenario Integrity Gate. Extend the validated scenario MVP only across predeclared dimensions of the parameter applicability range. A change to the objective, decision variables, material constraints, information pattern, feasibility meaning, or task causal chain returns to environment design and requires rebaselining.
5. Choose baselines that test necessity and fairness: closest prior method, current strong method, tuned simple rule, decoupled alternative, and exact/oracle/bound reference where applicable. Give comparable methods the same information, feasibility conditions, stopping tolerance, tuning budget, and compute accounting.
6. Choose metrics that directly measure objective value, feasibility, constraint residuals, task/service consequences, central tradeoff, runtime/resource cost, and failure behavior. State direction, unit, aggregation, uncertainty summary, and decision threshold.
7. If settings, objective/constraint references, or baselines are unknown, use public-safe search or route to `ccf-literature-searcher`; record `TBD` instead of guessing.
8. Load `references/evidence-design.md` for the detailed evidence rules. Load `references/result-templates.md` only when tables or presentation scaffolds are requested.
9. Preserve units, seeds, uncertainty intervals, setting names, version identifiers, metric direction, exclusions, and failed configurations. Never combine old and new environment versions in one comparison without a valid common physical or service metric and an explicit version boundary.
10. Route publication-grade figure/table composition, captions, manuscript placement, and render QA to `ccf-visual-composer`.

## Internal Checks And Visible Output

Keep the upstream gate, full conclusion-evidence ledger, rejected experiment candidates, and routine integrity checks internal unless the user asks for an audit. The user-visible response starts with the requested plan, table, or figure specification. Add only material context:

```text
Supported conclusion and applicability range:
Authoritative versions used:
Experiments and stop/interpretation rules:
TBD results or missing evidence:
Version conflict, limitation, or next owner when material:
```

Do not emit empty sections, full gate reports, or routine no-fabrication boilerplate when the requested artifact already marks every unknown value as `TBD`.

## References

- `references/evidence-design.md`: communication experiment, scenario-range, baseline, metric, mechanism, robustness, and interpretation rules.
- `references/result-templates.md`: optional fill-in result tables and presentation scaffolds.
