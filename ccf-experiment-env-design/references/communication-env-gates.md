# Communication Environment Gates

Use this reference when judging or repairing communication, wireless, networking, UAV, edge, IoT, vehicular, satellite, or mission-coupled optimization environments.

## Strong Scenario Ingredients

Prefer environments where the communication task is created by an explainable scenario background, service requirement, or control objective:

- UAV or mobile robot mission data collection, search, relay, target tracking, emergency response, or map update.
- Edge/IoT sensing with age of information, event priority, battery limits, and intermittent links.
- Vehicular, rail, maritime, or satellite connectivity with mobility, handover, blockage, or intermittent coverage.
- Integrated sensing and communication, semantic/task-oriented communication, federated learning over wireless, caching/offloading, or network slicing when the task utility is explicit.
- Multi-hop, cooperative relay, multi-cell, or device-to-device scenarios where interference, routing, scheduling, and resource allocation interact.

Weak scenarios usually optimize a single scalar metric over independent users with static channels, fixed topology, no meaningful constraints, no feasibility stress, and no reason a simple rule would fail. A scenario is also weak when a simple heuristic rule already solves the modeled setting, or when the setting is too complicated to explain, analyze, or connect to a clean algorithmic mechanism.

## Gate Criteria

### 1. Scenario Problem And Causes

Identify the concrete problem before judging mathematical difficulty:

- what fails, becomes costly, or loses value;
- which entities, flows, users, or mission stages are affected;
- which communication condition causes the consequence;
- why the consequence cannot be removed without changing a decision;
- which evidence or domain assumption supports the causal chain.

Fail this gate when the plan starts from variables or constraints without a scenario problem, when the claimed cause cannot affect the task, or when complexity is introduced only to make optimization appear difficult.

### 2. Plan Reasonableness

Check that every planned objective term, variable, constraint, dynamic, uncertainty source, and coupling corresponds to the problem or one of its causes and can change feasibility, the preferred decision, or the central tradeoff in credible operating ranges.

The plan needs repair when it omits a causal factor needed to reproduce the problem, adds components that do not change decisions, or uses arbitrary weights or thresholds only to force difficulty.

### 3. Scenario Background And Task-Communication Semantics

A strong environment names the scenario background first: who communicates, why communication is needed, what task or service is affected, and what abstraction boundary keeps the model explainable. Good task utilities include latency-weighted mission completion, information freshness, coverage confidence, detection quality, control stability, emergency priority, energy-limited lifetime, fairness under scarce resources, or reliability for critical flows.

Throughput, delay, reliability, energy, AoI, outage, or coverage should be tied to the scenario background and the paper's scientific question.

### 4. Mathematical Model

State the mathematical model before discussing algorithms, at the abstraction level needed for the scenario:

- parameters and constants;
- decision variables and their time scale;
- state variables if decisions are online;
- objective function or vector objective;
- hard constraints and soft constraints;
- information available at decision time;
- feasibility conditions.

The optimization target object should be mathematically clear: rate, SINR, outage, reliability, latency, AoI, energy efficiency, spectral efficiency, coverage, fairness, queue stability, mission utility, or a justified tradeoff among them.

### 5. Coupling And Joint Optimization

A strong model has at least two decision layers that interact through constraints or objectives:

- trajectory or placement affects channel quality, interference, and energy;
- power or bandwidth allocation changes queue delay and mission success;
- routing or relay choice affects congestion, reliability, and energy balance;
- sensing/computation/offloading changes traffic load and deadline feasibility;
- caching or compression changes backhaul load and application utility;
- handover or association changes scheduling, interference, and fairness.

The coupled decisions should explain why a joint method is needed. If the model decomposes without loss, the paper should narrow the claim to that decomposable case or change the scientific question.

### 6. Constraint And Coupling Necessity

Check the constraints that shape the optimization decision. Typical communication constraints include:

- bandwidth, transmit power, interference, link quality, coverage, or imperfect link-state knowledge;
- energy budget, battery dynamics, propulsion cost, compute cost, or sleep/wake duty cycle;
- queue, traffic arrival, deadline, reliability, packet loss, retransmission, or age of information;
- topology, mobility, coverage, handover, link availability, or multi-hop reachability;
- fairness, priority, safety, mission coverage, collision avoidance, or service-level constraints.

Mark which constraints bind in plausible operating ranges. Constraints that never affect feasibility or the optimal decision are background assumptions, not the core of the problem.

### 7. Scenario Complexity And Explainability

Keep only components with a scenario-based role and a demonstrated effect on feasibility, the preferred decision, or the central tradeoff. A good communication optimization scenario is not dominated by a tunable rule and is not burdened by unrelated entities, objectives, constraints, or random factors.

The scenario needs repair when:

- the model mixes too many objectives without saying which tradeoff is central;
- the number of entities, stages, and random factors makes the result impossible to interpret;
- every constraint is active only because of hand-picked parameters;
- interactions cannot be attributed to the stated scenario causes;
- a more complex solver is proposed even though a tuned rule already resolves the modeled problem.

### 8. Uncertainty And Dynamics

Use variation that changes the optimal decision: link-quality variation, mobility, bursty arrivals, failures, forecast error, delayed state information, partial observability, or non-stationary demand. Report parameter ranges and stress cases. Avoid randomness that does not change the decision structure.

Use static constants only when the paper's scientific question is about the resulting deterministic structure.

### 9. Tunable-Rule Test

Test a static rule, a greedy heuristic, a domain rule, a decoupled policy, and low-dimensional parameter tuning. An effective scenario should force these rules to sacrifice one side of the intended tradeoff when improving the other.

Typical shortcut baselines:

- nearest base station / nearest relay;
- max-SINR association;
- shortest-path or shortest-distance route;
- equal bandwidth or equal power;
- earliest deadline first;
- greedy offloading to the strongest edge node;
- fixed trajectory plus independent resource allocation;
- static threshold policy.

If a tuned rule handles both sides well, investigate whether the intended coupling is inactive, constraints do not bind, dynamics or uncertainty do not change decisions, or parameter ranges avoid the real conflict. Repair the scenario only when that missing cause is justified by the scenario. Do not add arbitrary difficulty solely to make the rule fail.

### 10. Focused Scientific Question

A scenario can support a deep paper when the scientific question is crisp. Examples:

- a new objective object captures task value better than throughput alone;
- mission utility couples information freshness and route planning;
- communication decisions affect physical task success, not only link metrics;
- reliability, latency, and energy create an unavoidable three-way tradeoff;
- uncertainty makes online decisions fundamentally different from offline allocation;
- multi-agent interference and cooperation create nonconvex or combinatorial structure;
- a neglected operating regime exposes failure in standard communication baselines.

Adding one more constraint to a standard resource allocation problem is strongest when it changes the solution mechanism or exposes a previously hidden tradeoff.

### 11. Publication Verdict

Use these labels:

- `paper-worthy`: passes task, objective-object, decision-variable, coupling, constraint, explainability, non-toy, innovation, and auditability gates; ready for experiment design.
- `salvageable`: has a real task and at least one strong coupling, but needs repairs before algorithm design.
- `modeling-only`: valuable as a formulation or evaluation setting, but not enough for a new algorithm claim yet.
- `toy`: missing task semantics, credible constraints, uncertainty, or shortcut resistance.
- `needs-literature`: cannot judge novelty or baseline sufficiency without related-work search.

The verdict must include concrete repairs, not only criticism.
