# Communication Environment Gates

Use these criteria in the same order as `ccf-env-design/SKILL.md` when designing or repairing communication, wireless, networking, UAV, edge, IoT, vehicular, satellite, or mission-coupled environments.

## 1. Scenario Background And Abstraction Boundary

State who communicates, which task or service requires communication, what physical/network conditions matter, and what remains external to the optimization. Connect link-level objects such as rate, delay, reliability, energy, AoI, outage, or coverage to task value.

Useful task contexts include mission data collection, relay, tracking, emergency response, edge sensing, intermittent connectivity, multi-hop cooperation, offloading, caching, federated learning, and task-oriented communication. Retain only details needed to express the scientific problem.

## 2. Problem And Causal Chain

State:

- what fails, becomes costly, or loses value;
- which entities, flows, users, or mission stages are affected;
- which communication condition causes the consequence;
- which decision can change that consequence;
- which domain assumption or evidence supports the chain.

A valid causal chain reaches from exogenous conditions and communication decisions through network behavior to the task outcome.

## 3. Focused Scientific Question

Define one question and central tradeoff. Examples include latency-reliability, energy-freshness, trajectory-connectivity, fairness-efficiency, robustness-efficiency, or task value versus radio cost. State the paper-scope boundary so later objectives and constraints answer this question rather than create unrelated difficulty.

## 4. Mathematical Model

Specify:

- parameters, units, and time scales;
- decision variables and domains;
- state variables and transitions for online problems;
- objective function or lexicographic/vector objective;
- hard and soft constraints;
- information available at decision time;
- dynamics, uncertainty, and feasibility conditions.

The mathematical target should be independently computable from a trace. State whether the structure is static/dynamic, deterministic/stochastic, offline/online, convex/nonconvex, combinatorial, or partially observable as applicable.

## 5. Model-To-Cause Traceability

Map each objective term, variable, constraint, dynamic, uncertainty source, and coupling to the causal problem or scientific question. A retained component should affect feasibility, the preferred decision, or the central tradeoff in a credible setting.

Mark decorative or inactive components for removal or repair. Mark missing causal factors whose absence prevents the environment from reproducing the stated problem.

## 6. Binding Constraints And Coupled Decisions

Identify which constraints bind in plausible settings and which decisions interact through them. Common couplings include trajectory-channel-energy, allocation-queue-deadline, route-congestion-reliability, sensing/offloading-traffic, and association-interference-fairness.

Explain why separate optimization loses feasibility or value. If the problem decomposes without loss, align the paper question and algorithm scope with that structure.

## 7. Complexity Balance And Tunable-Rule Test

Evaluate fixed/static, domain, greedy/myopic, decoupled, low-dimensional tuned, and random-feasible policies under equal information and declared tuning controls. A meaningful tradeoff is active when improving one side creates a measurable cost on the other.

Use the result to locate the active scientific difficulty. A tuned rule that handles all intended outcomes points to inactive coupling, slack constraints, irrelevant dynamics/uncertainty, or an uninformative parameter setting. An environment with many unrelated objectives, actors, or random mechanisms should be reduced to one attributable problem and coherent algorithmic target.

## 8. Paper Scenario To MVP

Define the paper scenario's parameter space and construction rule, then derive its MVP for the first complete implementation. Record fixed parameter values and their scenario-based reasons.

The MVP keeps the same scientific question, objective, material constraints, decision variables and coupling, information pattern, feasibility meaning, and causal chain. It provides one reproducible end-to-end version of the paper problem.

## 9. Algorithm Information And Auditability

Define observations and timing, exogenous-state access, action domains, feasibility masks/residuals, objective components, terminal signals, trace fields, units, and seed controls. Separate algorithm-visible information from audit-only diagnostics and identify every field needed for independent recomputation.

## 10. Verdict

- `paper-worthy`: the background, causal problem, scientific question, model, active coupling, complexity balance, MVP, and auditability form one coherent research environment.
- `salvageable`: the scientific problem is meaningful but one or more design gates require a concrete repair.
- `modeling-only`: the formulation or environment is useful, but current evidence does not support a new algorithmic contribution.
- `toy`: the task semantics, binding constraints, coupling, or tradeoff are not active enough for the intended contribution.
- `needs-literature`: domain validity, formulation precedent, parameter ranges, or baseline sufficiency require external evidence.

Attach each non-pass verdict to the earliest failed design gate and a specific repair.
