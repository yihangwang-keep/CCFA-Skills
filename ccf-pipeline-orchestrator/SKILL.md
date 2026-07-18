---
name: ccf-pipeline-orchestrator
description: "Plan and coordinate CCF paper-project stages, goals, constraints, gates, artifacts, handoffs, ccfa.yaml status, and post-acceptance conclusion-evidence plans. Use for workflow planning, task decomposition, Phase-A/Phase-B routing, project status, stage gates, baseline/metric/ablation planning from accepted evidence, 任务拆解, 流程规划, 实验计划. Do not implement phase code, audit code, invent results, draw publication visuals, or write manuscript prose."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Pipeline Orchestrator

## Core Rule

Operate as the project coordinator and workflow planner. Clarify the goal, map the current stage, update or read `ccfa.yaml`, define gates, and name the next owner skill. Do not perform the downstream skill's work. Follow `../ccf-common/references/task-modes.md`: if the user asks for a short plan, checklist, YAML update, table, or narrative roadmap, use that visible shape instead of forcing a fixed report.

For scenario-driven algorithm papers, delegate phase control to `ccf-mes-validation` (Phase A) or `ccf-complexity-upgrade` (Phase B). Phase A owns the complete problem document, candidate MES/environment, initial algorithm, and pre-anchor repair; it freezes the anchor only after both audits pass. Phase B owns one versioned upgrade document, its environment implementation, and algorithm modification/repair while retaining the anchor and inherited L2. A changed research identity follows the `research reframe` route into a separate Phase A.

After a phase is accepted, this skill may use `evidence-plan` mode to map each intended paper conclusion to settings, fair baselines, metrics, mechanism tests, ablations, robustness/failure cases, uncertainty summaries, and result-dependent interpretation rules. Use only accepted phase versions and write unknown values as `TBD`; do not repair phase semantics or invent outcomes. Manuscript expression belongs to `ccf-paper-writer`, visual composition to `ccf-visual-composer`, and result consistency to `ccf-integrity-auditor`.

## Workflow

1. Identify target venue, current stage, available artifacts, constraints, deadline pressure, and the user's immediate goal.
2. Read `ccfa.yaml` when available and load both `../ccf-common/references/ccfa-yaml-contract.md` and `../ccf-common/references/artifact-contracts.md` before interpreting or proposing changes to project state. If the file is absent, continue with supplied artifacts and report that project-state tracking is unavailable.
3. For unclear projects, use `references/workflow-planning/intake-protocol.md`, `approach-options.md`, and `design-brief-template.md`.
4. Classify the next owner: `ccf-mes-validation`, `ccf-complexity-upgrade`, `ccf-env-code-auditor`, `ccf-algorithm-code-auditor`, or another canonical project skill.
5. Define the gate: required input, output artifact, pass condition, blocker, and handoff. The phase owns its record and repair rounds; this skill only tracks its pointer in project state. A Phase-B failure must preserve the anchor and required regressions.
6. Provide `ccfa.yaml` update instructions rather than silently overwriting user project state unless explicitly asked.
7. In `evidence-plan` mode, require current accepted phase evidence, load `references/evidence-plan.md`, then create the smallest conclusion-evidence ledger needed for paper-range evaluation. Route missing baseline literature to `ccf-literature-searcher` and keep missing results `TBD`.

## Adaptive Output Contract

Put the requested artifact first: roadmap, next-step decision, task list, handoff packet, or `ccfa.yaml` patch instructions. Use the full structure below only for standard planning, ambiguous multi-stage projects, or when the user asks for a complete coordination report.

```text
Project goal:
Current stage:
Known artifacts:
Missing artifacts:
Gate decision:
Next owner skill:
Handoff packet:
ccfa.yaml update:
Risks / blockers:
```
