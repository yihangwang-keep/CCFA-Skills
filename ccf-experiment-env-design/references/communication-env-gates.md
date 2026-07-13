# Communication Environment Gates

Use this reference when judging or repairing communication, wireless, networking, UAV, edge, IoT, vehicular, satellite, or mission-coupled optimization environments.

## Strong Scenario Ingredients

Prefer environments where the communication task is created by an external mission, service requirement, or control objective:

- UAV or mobile robot mission data collection, search, relay, target tracking, emergency response, or map update.
- Edge/IoT sensing with age of information, event priority, battery limits, and intermittent links.
- Vehicular, rail, maritime, or satellite connectivity with mobility, handover, blockage, or intermittent coverage.
- Integrated sensing and communication, semantic/task-oriented communication, federated learning over wireless, caching/offloading, or network slicing when the task utility is explicit.
- Multi-hop, cooperative relay, multi-cell, or device-to-device scenarios where interference, routing, scheduling, and resource allocation interact.

Weak scenarios usually optimize a single scalar metric over independent users with static channels, fixed topology, no meaningful constraints, no feasibility stress, and no reason a simple rule would fail. A scenario is also weak when it is too complicated to explain, analyze, or connect to a clean algorithmic mechanism.

## Gate Criteria

### 1. Task-Communication Semantics

Pass when the scenario explains why bits are generated, why they matter, and how communication quality changes task value. Good task utilities include latency-weighted mission completion, information freshness, coverage confidence, detection quality, control stability, emergency priority, energy-limited lifetime, fairness under scarce resources, or reliability for critical flows.

Fail when the task is only "maximize throughput" without a domain reason, unless the claimed paper is narrowly about PHY/MAC/network theory and its novelty is formal.

### 2. Coupling And Joint Optimization

Before checking coupling, identify the optimization target object:

- communication metric: rate, SINR, outage, reliability, latency, AoI, energy efficiency, spectral efficiency, coverage, fairness, or queue stability;
- task metric: mission completion, sensing confidence, information value, control stability, emergency priority, or service utility;
- tradeoff form: weighted sum, constrained optimization, lexicographic objective, Pareto frontier, min-max fairness, or chance-constrained target.

Pass when the target object is mathematically clear and at least two decision layers interact through constraints or objectives:

- trajectory or placement affects channel quality, interference, and energy;
- power or bandwidth allocation changes queue delay and mission success;
- routing or relay choice affects congestion, reliability, and energy balance;
- sensing/computation/offloading changes traffic load and deadline feasibility;
- caching or compression changes backhaul load and application utility;
- handover or association changes scheduling, interference, and fairness.

Fail when the objective is vague, the target is only a post-hoc evaluation metric, the problem decomposes into independent subproblems without loss, or a sequential pipeline is as good as a joint method under all meaningful cases.

### 3. Real Constraints

Record units and ranges for all active constraints. At minimum, a strong wireless/networking environment should include several of:

- bandwidth, transmit power, interference, SINR, channel model, path loss, fading, blockage, or CSI error;
- energy budget, battery dynamics, propulsion cost, compute cost, or sleep/wake duty cycle;
- queue, traffic arrival, deadline, reliability, packet loss, retransmission, or age of information;
- topology, mobility, coverage, handover, link availability, or multi-hop reachability;
- fairness, priority, safety, mission coverage, collision avoidance, or service-level constraints.

Fail when constraints are only decorative or never bind in plausible operating ranges.

### 4. Scenario Complexity And Explainability

Use the smallest scenario that preserves the paper's core tradeoff. Prefer one crisp coupling over many loosely related constraints. A good communication optimization scenario should be complex enough that a simple rule fails, but structured enough that the later algorithm can be explained through a recognizable mechanism, such as decomposition, relaxation, dual variables, Lyapunov drift, matching, convexification, dynamic programming, game structure, graph structure, or online control.

Fail when:

- the model mixes too many objectives without saying which tradeoff is central;
- the number of entities, stages, and random factors makes the result impossible to interpret;
- every constraint is active only because of hand-picked parameters;
- the later algorithm would be a bag of case rules rather than a mechanism derived from the formulation.

### 5. Uncertainty And Dynamics

Use variation that changes the optimal decision: channel variation, mobility, bursty arrivals, failures, forecast error, CSI delay, partial observability, or non-stationary demand. Report parameter ranges and stress cases. Avoid randomness that does not change the decision structure.

Fail when all variables are static constants chosen after looking at outcomes.

### 6. Non-Toy And Anti-Shortcut Test

Add a simple rule baseline and a decoupled baseline. The environment is too weak for an algorithm paper when either one solves the central claim across realistic settings.

Typical shortcut baselines:

- nearest base station / nearest relay;
- max-SINR association;
- shortest path or minimum distance route;
- equal bandwidth or equal power;
- earliest deadline first;
- greedy offloading to the strongest edge node;
- fixed trajectory plus independent resource allocation;
- static threshold policy.

If a shortcut wins, repair by changing the claim or restoring missing difficulty. Do not add arbitrary penalties, thresholds, or hand-written exceptions whose only purpose is to make the proposed method win.

### 7. Innovation Semantics

A scenario can support a deep paper when the new problem semantics are crisp. Examples:

- a new objective object captures task value better than throughput alone;
- mission utility couples information freshness and route planning;
- communication decisions affect physical task success, not only link metrics;
- reliability, latency, and energy create an unavoidable three-way tradeoff;
- uncertainty makes online decisions fundamentally different from offline allocation;
- multi-agent interference and cooperation create nonconvex or combinatorial structure;
- a neglected operating regime exposes failure in standard communication baselines.

Weak novelty: adding one more constraint to a standard resource allocation problem without changing the mechanism, evidence, or insight.

### 8. Publication Verdict

Use these labels:

- `paper-worthy`: passes task, objective-object, decision-variable, coupling, constraint, explainability, non-toy, innovation, and auditability gates; ready for experiment design.
- `salvageable`: has a real task and at least one strong coupling, but needs repairs before algorithm design.
- `modeling-only`: valuable as a formulation or evaluation setting, but not enough for a new algorithm claim yet.
- `toy`: missing task semantics, credible constraints, uncertainty, or shortcut resistance.
- `needs-literature`: cannot judge novelty or baseline sufficiency without related-work search.

The verdict must include concrete repairs, not only criticism.
