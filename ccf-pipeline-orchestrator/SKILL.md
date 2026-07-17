---
name: ccf-pipeline-orchestrator
description: "Plan and coordinate CCF paper-project stages, goals, constraints, success criteria, gates, artifacts, handoffs, and ccfa.yaml status across the CCFA family. Use for workflow planning, task decomposition, paper-scenario-to-MVP workflow, project status, stage gates, next-skill routing, 任务拆解, 流程规划. Do not perform downstream writing, review, search, scenario design, algorithm design, experiment design, or rebuttal itself."
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

For scenario-driven algorithm papers, keep this stage order: define the paper scenario, formal optimization problem, parameter applicability range, and scenario MVP; establish `environment-valid`; use algorithm-family and reference-solver probes to expose information, feasibility, and verification gaps; freeze the joint contract; design and audit the algorithm MVP; run the `ccf-experiment-debugger` design-validation loop for versioned minimal repairs; then hand `joint-ready` MVP evidence to experiment design for evaluation across the paper's conclusion applicability range. An algorithm may submit an environment amendment request, but only `ccf-env-design` may accept a problem-contract change.

## Workflow

1. Identify target venue, current stage, available artifacts, constraints, deadline pressure, and the user's immediate goal.
2. Read `ccfa.yaml` when available and load both `../ccf-common/references/ccfa-yaml-contract.md` and `../ccf-common/references/artifact-contracts.md` before interpreting or proposing changes to project state. If the file is absent, continue with supplied artifacts and report that project-state tracking is unavailable.
3. For unclear projects, use `references/workflow-planning/intake-protocol.md`, `approach-options.md`, and `design-brief-template.md`.
4. Classify the next owner: `ccf-project-scaffolder`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-env-design`, `ccf-env-code-auditor`, `ccf-algorithm-designer`, `ccf-algorithm-code-auditor`, `ccf-experiment-designer`, `ccf-experiment-debugger`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, or `ccf-rebuttal-writer`.
5. Define the gate: required input, output artifact, pass condition, blocker, and handoff. For scenario/algorithm gates, also state the paper-scenario, formal-problem, MVP, and algorithm versions; the allowed change class; and which checks become stale after a change.
6. Provide `ccfa.yaml` update instructions rather than silently overwriting user project state unless explicitly asked.

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
