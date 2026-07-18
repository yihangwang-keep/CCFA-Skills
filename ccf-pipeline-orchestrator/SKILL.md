---
name: ccf-pipeline-orchestrator
description: "Plan and coordinate CCF paper-project stages, goals, constraints, success criteria, gates, artifacts, handoffs, and ccfa.yaml status across the CCFA family. Use for workflow planning, task decomposition, paper-scenario-to-MES workflow, project status, stage gates, next-skill routing, 任务拆解, 流程规划. Do not perform downstream research work itself."
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

For scenario-driven algorithm papers, use two phases with repair loops in both. Phase A defines the paper scenario, formal problem, parameter range, and candidate MES containing the core tradeoff; establishes environment L1 and the one-time anchor L2 algorithmic-need result; freezes the accepted MES as anchor; then designs and audits the initial non-heuristic algorithm MVP. If the initial algorithm fails, repair its code/mechanism/family against the anchor without rerunning valid L2 or redesigning MES. Phase B begins only when a user/project owner requests one complexity upgrade: record the stage delta, audit its implementation consistency and anchor regression, run the current algorithm, and repair/upgrade the algorithm when it fails. Phase B inherits the anchor L2 result and never reruns heuristic probes or redesigns MES. After accepted stage evidence, `ccf-experiment-designer` plans paper-range usage evidence. Route exhausted algorithm work to a classified, non-simplifying environment review. Only an authoritative model defect may trigger a formal amendment, new candidate MES, new evidence epoch, and full rebaseline: it fully rebaselines environment, algorithm, baseline, and experiment evidence. A changed research identity follows the `research reframe` route.

## Workflow

1. Identify target venue, current stage, available artifacts, constraints, deadline pressure, and the user's immediate goal.
2. Read `ccfa.yaml` when available and load both `../ccf-common/references/ccfa-yaml-contract.md` and `../ccf-common/references/artifact-contracts.md` before interpreting or proposing changes to project state. If the file is absent, continue with supplied artifacts and report that project-state tracking is unavailable.
3. For unclear projects, use `references/workflow-planning/intake-protocol.md`, `approach-options.md`, and `design-brief-template.md`.
4. Classify the next owner: `ccf-project-scaffolder`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-env-design`, `ccf-env-code-auditor`, `ccf-algorithm-designer`, `ccf-algorithm-code-auditor`, `ccf-experiment-designer`, `ccf-experiment-debugger`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, or `ccf-rebuttal-writer`.
5. Define the gate: required input, output artifact, pass condition, blocker, and handoff. For Phase-A gates, include paper-scenario, formal-problem, anchor MES, one-time L2, implementation, validation-contract, and initial algorithm versions. For Phase-B gates, include `stage_request_id`, user-requested delta, anchor MES, stage implementation, anchor regression, inherited `algorithmic_need`, and algorithm-upgrade version; explicitly set `l2_heuristic_probe_rerun: no`. A complexity-stage failure must name the algorithm owner and anchor regression reruns; it must not silently replace the MES.
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
