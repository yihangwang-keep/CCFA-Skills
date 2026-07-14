---
name: ccf-experiment-env-design
description: "Design and audit non-toy communication, wireless, networking, UAV, edge, IoT, vehicular, satellite, and mission-coupled optimization environments. Use for scenario problem/cause analysis, plan reasonableness, objective and constraint design, complexity balance, tunable-rule tests, joint-optimization necessity, 场景问题与原因, 计划合理性, 目标函数, 约束建模, tradeoff审查, 启发式调参检查, 联合优化, and judging whether later algorithmic complexity is justified. Do not design result tables, invent results, or replace literature search."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Experiment Env Design

## Core Rule

Create or audit the research environment before designing algorithms or result tables. The primary purpose is to prevent later algorithmic complexity from being added to a scenario that a tunable rule already solves. First identify the scenario's actual problem and causal mechanism. Then judge whether the plan's objective, variables, constraints, information pattern, dynamics, uncertainty, and coupling correctly represent that problem. As a simple audit hint, an effective scenario should make a heuristic improve one side of the intended tradeoff only by clearly sacrificing the other. If a tuned heuristic handles both sides well, investigate whether coupling is inactive, constraints are loose, dynamics do not matter, or the tested range misses the real conflict. Keep complexity balanced and repair only causes justified by the scenario, not by adding artificial difficulty.

This skill must answer explicitly: what problem exists, why it exists, whether the plan models it reasonably, whether tunable rules already resolve it, whether any complexity is inactive or artificial, and whether later algorithmic work is justified.

## Modes

- `audit`: judge an existing scenario or trace for realism, nontriviality, joint-optimization necessity, and paper value.
- `design`: construct a communication optimization environment from a rough task or research idea, centered on objective, variables, constraints, and explainable abstraction.
- `repair`: upgrade a toy or under-specified scenario into a stronger environment without fabricating results.
- `handoff-spec`: produce an environment specification for `ccf-experiment-designer`, algorithm implementation, or simulation.

## Mandatory Gates

Run these gates before recommending downstream algorithm or experiment work:

1. **Problem-and-cause gate:** state the concrete scenario problem, affected entities or task, observed consequence, and causal chain showing why communication decisions create the problem.
2. **Plan-reasonableness gate:** verify that the planned objective, decision variables, constraints, information pattern, time scale, dynamics, uncertainty, and coupling correspond to the stated causes rather than being added only to create difficulty.
3. **Scenario-background gate:** state who communicates, why communication affects the task, and what abstraction boundary is used.
4. **Scientific-question gate:** state one focused scientific question or tradeoff, such as latency-reliability, energy-freshness, trajectory-connectivity, fairness-efficiency, or robustness-efficiency.
5. **Mathematical-model gate:** define decision variables, objective function, constraints, information pattern, and feasibility conditions at the abstraction level needed for the scientific question.
6. **Constraint-coupling gate:** identify the constraints that bind in credible ranges and the coupled decisions that make separate optimization lose feasibility or value.
7. **Tunable-rule gate:** test whether static rules, greedy heuristics, nearest/max-SINR choices, fixed allocation, fixed route/trajectory, threshold policies, or a decoupled pipeline already solve the modeled setting after reasonable tuning. The intended signal is that improving one side requires a visible loss on the other. If a rule handles both sides well, find which real coupling, binding constraint, dynamic effect, uncertainty, or parameter regime is absent or inactive.
8. **Complexity-balance gate:** reject both insufficient structure and decorative complexity. Every retained component must have a scenario-based reason and a demonstrated effect on feasibility, the preferred decision, or the central tradeoff.

Load `references/communication-env-gates.md` for detailed gate criteria and `references/env-spec-template.md` before producing a reusable environment specification.

## Workflow

1. Identify target venue family, communication domain, task driver, available artifacts, simulation code, traces, and the user's decision goal.
2. If the user asks about current prior art, common formulations, communication abstractions, objective functions, constraints, or strongest baselines, follow CCFA handoff mode before using `ccf-literature-searcher`; if searching directly, use public keywords and primary sources.
3. Normalize the environment into problem, causes, scenario background, plan assumptions, scientific question, mathematical model, objective function, decision variables, constraints, shortcut tests, and observables.
4. Run the Mandatory Gates in order. Do not assess implementation readiness until the problem-and-cause and plan-reasonableness gates pass. For each failed gate, identify the concrete cause and label the repair as `correct-causal-model`, `remove-decorative-complexity`, `activate-binding-constraint`, `restore-coupling`, `add-decision-relevant-dynamics`, `tighten-formulation`, `narrow-claim`, or `needs-literature`.
5. Define the optimization problem at environment level: objective function or vector objective, decision variables, state/action if online, constraints, feasibility checks, tractability class, and what information is known when decisions are made. Do not invent the final algorithm.
6. Use fixed/static rules, greedy or myopic rules, domain rules, decoupled decisions, and low-dimensional parameter tuning to judge whether later algorithmic complexity is justified. A valid tradeoff should force these rules to sacrifice one side when improving the other. If they handle both sides well, repair the scenario only after identifying the missing or inactive real cause.
7. Produce either an audit verdict, a repaired scenario, or a handoff-ready environment spec. If the user asked for algorithm design, stop at the environment boundary and name what the algorithm must solve.
8. Hand off to `ccf-experiment-designer` only after the environment passes the non-toy and auditability gates; use `ccf-idea-optimizer` when the core research question itself needs reshaping.

## Adaptive Output Contract

Return the requested artifact first. Keep the default audit concise:

```text
Verdict:
Scenario problem and causes:
Plan reasonableness:
Tunable-rule finding:
Complexity-balance finding:
Required changes:
```

Do not emit a gate-by-gate report, full checklist, baseline catalog, handoff section, or repeated formulation summary unless the user asks for it. For a requested reusable environment spec, use `references/env-spec-template.md` and keep unknown values marked `TBD`.

## References

- `references/communication-env-gates.md`: use for communication-specific realism, non-toy, coupling, and publication-worthiness gates.
- `references/env-spec-template.md`: use when writing a handoff-ready environment specification for algorithms, simulations, or experiment design.
