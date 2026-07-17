# Communication Environment Gates

Use these criteria in the same order as `ccf-env-design/SKILL.md` for a full communication-domain design, audit, repair, or environment amendment review.

## 1. Paper Scenario And Abstraction Boundary

State who communicates, which task or service requires communication, what physical and network conditions matter, and what remains outside the optimization. Connect rate, delay, reliability, energy, age of information, outage, coverage, or other communication quantities to the task outcome. Retain only details needed to express the scientific problem.

## 2. Task Causal Chain And Causal Bottleneck

State:

- what fails, becomes costly, or loses value;
- which entities, flows, users, or mission stages are affected;
- which communication condition causes the consequence;
- which decision can change that consequence;
- which domain assumption or evidence supports the chain;
- where the causal bottleneck makes otherwise reasonable decisions compete.

A valid task causal chain runs from exogenous conditions and communication decisions through network behavior to the task outcome. The causal bottleneck is the smallest supported part of that chain that activates the central tradeoff; it is not complexity added solely to make optimization difficult.

## 3. Focused Scientific Question And Applicability

Define one scientific question and one central tradeoff, such as latency-reliability, energy-freshness, trajectory-connectivity, fairness-efficiency, robustness-efficiency, or task value versus radio cost. State the supported conclusion and its applicability boundary so later objectives and constraints answer this question rather than create unrelated difficulty.

## 4. Formal Optimization Problem

Specify:

- sets, parameters, units, and time scales;
- decision variables and domains;
- state variables and transitions for online problems;
- objective function or lexicographic/vector objective;
- hard and soft constraints;
- information available at each decision time;
- dynamics, uncertainty, and feasibility meaning.

The optimization target and every feasibility residual must be independently computable from a trace. State whether the problem is static or dynamic, deterministic or stochastic, offline or online, convex or nonconvex, combinatorial, or partially observable as applicable.

## 5. Problem-To-Cause Traceability

Map each objective term, variable, constraint, dynamic, uncertainty source, and coupling to the task causal chain or scientific question. A retained component must affect feasibility, the preferred decision, or the central tradeoff in a credible part of the parameter applicability range.

Mark decorative or inactive components for removal or repair. Mark missing causal factors whose absence prevents the environment from reproducing the stated problem.

## 6. Binding Constraints And Coupled Decisions

Identify which constraints bind in plausible settings and which decisions interact through them. Common couplings include trajectory-channel-energy, allocation-queue-deadline, route-congestion-reliability, sensing/offloading-traffic, and association-interference-fairness.

Explain the causal bottleneck and why separate optimization loses feasibility or task value. If the problem decomposes without loss, align the scientific question, supported conclusion, and algorithm scope with that structure.

## 7. Parameter Applicability Range And Tunable-Rule Test

Define the supported parameter range, construction rule, boundary cases, and the evidence behind material values. Evaluate fixed/static, domain, greedy/myopic, decoupled, low-dimensional tuned, and random-feasible rules under equal information and declared tuning controls.

The central tradeoff is active when improving one side creates a measurable, attributable cost on the other. A tuned simple rule that handles all intended outcomes points to inactive coupling, slack constraints, irrelevant dynamics or uncertainty, or an uninformative parameter setting. Repair only defects supported by the task causal chain; otherwise narrow the supported conclusion and mark algorithmic need `not demonstrated` or `contradicted`.

## 8. Paper Scenario To Scenario MVP

Derive one complete scenario MVP from the paper scenario's parameter applicability range and construction rule. Record fixed parameter values and their scenario-based reasons.

The scenario MVP must keep the same task causal chain, scientific question, objective, material constraints, decision variables and coupling, information pattern, feasibility meaning, and central tradeoff. It is the first reproducible end-to-end version of the formal optimization problem, not a different easier problem.

## 9. Algorithm Information And Auditability

Define decision-time observations, exogenous-state access, decision domains, feasibility masks or residuals, objective components, terminal signals, trace fields, units, and seed controls. Separate decision-time information from audit-only diagnostics and identify every field needed for independent recomputation. Future or hidden information remains unavailable unless the formal information pattern explicitly authorizes it.

## 10. Environment Amendment Review

An algorithm may submit evidence of an environment defect but may not directly change problem semantics. Require an amendment record containing the observed failure, methods checked, proposed minimal change, objective/feasible-set impact, information-pattern impact, preserved invariants, invalidated artifacts, and required reruns.

Accept the request only when all five tests pass:

- **algorithm independence:** the defect is not specific to the current method;
- **causal necessity:** communication or task evidence requires the change;
- **semantic preservation:** the task outcome, scientific question, and central tradeoff remain intact;
- **information honesty:** no future, hidden, or audit-only information is newly exposed;
- **method neutrality:** the environment is not tailored to favor a method or ranking.

If semantic preservation fails, treat the proposal as a new paper-scenario version or reframing. Any accepted semantic amendment invalidates all dependent environment, algorithm, baseline, and experimental evidence until rerun.

## 11. Verdict And Readiness

Keep the original design verdict and report readiness separately:

- `paper-worthy`: the paper scenario, formal problem, active coupling, complexity balance, scenario MVP, and auditability support one coherent study.
- `salvageable`: the scientific problem is meaningful but one or more design gates require a concrete repair.
- `modeling-only`: the formulation is useful, but current evidence does not establish the need for a new algorithmic contribution.
- `toy`: the task semantics, binding constraints, coupling, or central tradeoff are not active enough for the intended study.
- `needs-literature`: domain validity, formulation precedent, parameter applicability, or comparison sufficiency requires external evidence.

Readiness meanings:

- `environment-valid`: the task causal chain, formal problem, applicability range, and paper-to-MVP relation are coherent and supported.
- `algorithmic-need`: `demonstrated`, `not demonstrated`, or `contradicted` by exact/reference and tuned-simple-rule evidence.
- `interface-complete`: decision-time information and audit-only evidence are sufficient and correctly separated for algorithm work.
- `joint-ready`: reserved for downstream acceptance after the algorithm specification and implementation pass against the same environment version.

Attach each non-pass verdict to the earliest failed design gate and a specific repair. An environment may be `environment-valid` without supporting a new algorithmic contribution.
