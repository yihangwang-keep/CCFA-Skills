---
name: ccf-experiment-env-design
description: "Design and audit non-toy communication, wireless, networking, UAV, edge, IoT, vehicular, satellite, and mission-coupled optimization problem environments for CCF paper experiments. Use for experiment-env-design, communication scenario design, task-communication problem formulation, objective-function design, optimization target selection, constraint design, joint optimization necessity checks, explainable scenario abstraction, 场景设计, 通信优化问题, 目标函数, 优化对象, 约束建模, 任务通信, 联合优化, 非玩具问题, and judging whether a scenario can support a deep communication algorithm paper. Do not design result tables, invent results, or replace literature search."
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

Create or audit the research environment before designing algorithms or result tables. The environment must contain a real communication task, explicit entities, a well-defined optimization target, decision variables, channel/network dynamics, resource constraints, coupled decisions, uncertainty, and a reason simple decoupled rules are insufficient. Do not make the setting complex by stacking arbitrary rules. Prefer the smallest scenario that preserves the essential coupling and admits an interpretable algorithmic mechanism. Every modeling detail must follow from domain motivation, communication theory, an accepted system assumption, a cited source, or a declared assumption that can be stress-tested.

This skill must answer the user's key gate explicitly: whether the scenario can support a deep communication algorithm paper, whether it is currently toy-like, and what must change before later algorithms have necessity, difficulty, and paper value.

## Modes

- `audit`: judge an existing scenario or trace for realism, nontriviality, joint-optimization necessity, and paper value.
- `design`: construct a communication optimization environment from a rough task or research idea, centered on objective, variables, constraints, and explainable abstraction.
- `repair`: upgrade a toy or under-specified scenario into a stronger environment without fabricating results.
- `handoff-spec`: produce an environment specification for `ccf-experiment-designer`, algorithm implementation, or simulation.

## Mandatory Gates

Run these gates before recommending downstream algorithm or experiment work:

1. **Task-communication gate:** identify the external task or mission that creates communication demand. A scenario with only abstract throughput maximization is weak unless the paper's contribution is explicitly physical-layer, networking, or theory.
2. **Objective-object gate:** define the optimization target object first: rate, delay, reliability, energy, AoI, coverage, mission utility, fairness, stability, outage, or a justified weighted/vector objective. Reject vague "overall performance" objectives.
3. **Decision-variable gate:** state the controllable variables and their time scale, such as power, bandwidth, subchannel, association, scheduling, routing, relay selection, trajectory, sensing/computation/offloading, compression, or admission control.
4. **Constraint gate:** list hard and soft constraints: spectrum, power, energy, latency, reliability, interference, mobility, topology, buffer, computation, fairness, safety, coverage, or regulatory limits. Mark which constraints are binding and which are only background.
5. **Coupling gate:** show at least two decisions that cannot be optimized independently without losing feasibility or value, such as routing-power, bandwidth-scheduling, trajectory-link quality, sensing-communication, queue-control, or reliability-energy.
6. **Difficulty-balance gate:** keep the scenario no more complex than needed. Fail if the formulation has so many objectives, entities, stages, or random factors that the algorithm cannot be explained, analyzed, or compared cleanly.
7. **Uncertainty gate:** include only decision-relevant variation: fading, blockage, mobility, traffic bursts, task arrivals, node failures, CSI error, demand forecast error, or partial observability. Avoid decorative randomness.
8. **Non-toy gate:** fail the environment if a simple static threshold, nearest-neighbor rule, max-SINR rule, greedy scheduler, or separately optimized pipeline solves the central claim. Repair by restoring the missing coupling or constraint tension, not by adding arbitrary rules.
9. **Innovation semantics gate:** state what is new in the problem setting, not only in the future algorithm: a new objective object, neglected constraint interaction, new mission utility, new coupling structure, new robustness requirement, or a cleaner formulation of a known hard tradeoff.
10. **Auditability gate:** define inputs, outputs, variables, units, parameter ranges, assumptions, seeds if simulated, and feasibility checks so another researcher can reproduce the environment.
11. **Publication gate:** decide whether the environment is enough to support a communication algorithm paper, only a modeling/evaluation note, or not yet a paper.

Load `references/communication-env-gates.md` for detailed gate criteria and `references/env-spec-template.md` before producing a reusable environment specification.

## Workflow

1. Identify target venue family, communication domain, task driver, available artifacts, simulation code, traces, and the user's decision goal.
2. If the user asks about current prior art, common formulations, standard channel models, objective functions, constraints, or strongest baselines, follow CCFA handoff mode before using `ccf-literature-searcher`; if searching directly, use public keywords and primary sources.
3. Normalize the environment into entities, time scale, spatial model, network model, traffic/task model if needed, objective object, decision variables, constraints, uncertainty, and observables.
4. Run the Mandatory Gates. For each failed gate, label whether the fix is `add-domain-grounding`, `restore-coupling`, `add-dynamics`, `add-uncertainty`, `tighten-formulation`, `narrow-claim`, or `needs-literature`.
5. Define the optimization problem at environment level: objective function or vector objective, decision variables, state/action if online, constraints, feasibility checks, tractability class, and what information is known when decisions are made. Do not invent the final algorithm.
6. Specify baseline families that test scenario necessity: decoupled optimization, simple rules, classical solvers, standard communication methods, oracle or relaxed bounds, and domain-specific baselines.
7. Produce either an audit verdict, a repaired scenario, or a handoff-ready environment spec. If the user asked for algorithm design, stop at the environment boundary and name what the algorithm must solve.
8. Hand off to `ccf-experiment-designer` only after the environment passes the non-toy and auditability gates; use `ccf-idea-optimizer` when the core research question itself needs reshaping.

## Adaptive Output Contract

Return the requested artifact first. For the user's default question about scenario depth, use:

```text
Verdict:
Paper-depth answer:
Why this is / is not a non-toy communication problem:
Task-communication semantics:
Optimization target object:
Decision variables and constraints:
Joint optimization necessity:
Scenario abstraction and explainability:
Environment specification:
Optimization formulation sketch:
Scenario realism and source basis:
Failure modes / toy risks:
Required repairs:
Baseline and oracle requirements:
Handoff target:
Gate status:
```

For a reusable environment spec, use the schema in `references/env-spec-template.md` and keep unknown values marked `TBD` instead of filling them by invention.

## References

- `references/communication-env-gates.md`: use for communication-specific realism, non-toy, coupling, and publication-worthiness gates.
- `references/env-spec-template.md`: use when writing a handoff-ready environment specification for algorithms, simulations, or experiment design.
