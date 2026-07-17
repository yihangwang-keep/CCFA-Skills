# Communication Environment Gates

Use these criteria in the same order as `ccf-env-design/SKILL.md` for a full communication-domain design, audit, evolution decision, or environment amendment review.

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

## 7. Parameter Applicability Range And Construction Neutrality

Define the supported parameter range, construction rule, boundary cases, and the evidence behind material values. Fix the construction independently of comparative method outcomes. The central tradeoff is active only when improving one side creates a measurable, attributable cost on the other.

## 8. Paper Scenario To Minimum Executable Scenario

Derive a **Minimum Executable Scenario (MES; 最小可执行场景)** from the paper scenario's parameter applicability range and construction rule. Record its entry point, registered configuration or configurations, interface, trace and seed controls, independent checks, acceptance criteria, and scenario-based reasons for every fixed choice.

The MES must keep the same task causal chain, scientific question, objective, material constraints, decision variables and coupling, information pattern, feasibility meaning, and central tradeoff. It is the smallest causally complete and auditable executable package for that authority version, not a different easier problem. One configuration is sufficient only when it can exercise the required end-to-end semantics and declared tradeoff.

## 9. Two-Layer Environment Contract

**L1 audit contract:** define the required bidirectional mappings and independent checks for the frozen paper scenario, formal problem, parameter range, MES, causal bottleneck, objective, material constraints, decision coupling, information pattern, feasibility meaning, and execution contract. `ccf-env-code-auditor` executes this contract and owns `environment-valid`; L1 does not establish algorithmic need.

**L2 probe contract:** before comparative outcomes, predeclare a joint-tradeoff or optimization target, its domain/formal basis, and independent evidence that the target region is feasible and attainable under the MES contract. Define representative fixed/static, domain, greedy/myopic, decoupled, low-dimensional tuned, and random-feasible `environment_probe` policies as applicable; disclose tuning ranges and search budgets; and match decision-time information, feasibility enforcement, stopping conditions, cases, and resource accounting. An impossible or unsupported target cannot establish algorithmic need.

`ccf-env-code-auditor` freezes and executes this contract. It sets `algorithmic_need: demonstrated` only when L1 passes and adequately tuned representative probes still cannot reach the independently justified attainable target. If a probe reaches it, the environment may remain `environment-valid`, but the auditor sets `not_demonstrated`. Missing target reachability, tuning, coverage, or fairness evidence is `insufficient_evidence`. Never change the MES, add unsupported difficulty, or select favorable cases merely to make a probe fail.

These probes may be heuristic because they diagnose the environment or serve as baselines. They do not authorize heuristic decision mechanisms in the paper's proposed algorithm contribution. Algorithm design owns that prohibition and algorithm audit verifies it.

## 10. Evolution, Versioning, And Invalidation

Bind the paper-scenario, formal-problem, parameter-range, MES, implementation, validation-contract, and evidence-epoch versions. Accepted authority artifacts are immutable. When code, audit, or experiment evidence motivates a change, classify it before editing as `implementation_repair`, `evidence_expansion`, `scenario_extension`, `formal_amendment`, or `research_reframe` using `scenario-evolution-contract.md`.

Record the parent version, decisive evidence, preserved research invariants, changed contract items, acceptance criteria, invalidated artifacts, and required reruns. Invalidation is a dependency consequence, not a change class. Preserve prior versions and failed evidence as historical records.

## 11. Algorithm Repair Exhaustion And Model Escalation

When environment L1 passes and algorithm code matches its specification, preserve a repair-exhaustion record covering attempted mechanism or family revisions, reference/bound evidence, unchanged failures, and why another algorithm-only delta is no longer credible. This record triggers environment and mathematical-model review; it does not automatically authorize a change.

Classify the failure:

- **algorithm-specific:** a credible admissible algorithm can solve the accepted problem, or the failure follows from the selected mechanism; keep the environment unchanged and return to algorithm design;
- **formal-model defect:** the registered problem is infeasible or ill-posed, has inconsistent information timing, omits a necessary causal factor, or otherwise fails to represent the paper scenario; create the smallest justified formal correction and successor MES;
- **unresolved hardness:** no defect or admissible algorithm route is established; record a blocker and do not simplify the problem.

Do not confuse targets. If the independently supported environment L2 target becomes unattainable, mark L2 stale or invalid and return to environment audit before model amendment. If only an algorithm's promised convergence, approximation, or compute target is unattainable, ownership remains algorithm design. Only a defect in the authoritative scenario/formal problem may enter the model-amendment branch.

A permitted correction may add a missing causal state, dynamic, constraint, or uncertainty; correct inconsistent units, timing, feasibility, or objective semantics; or replace the formulation with a mathematically equivalent executable form. An item independently proven inconsistent with the paper scenario may be replaced, but the successor must preserve the intended causal difficulty and central tradeoff. It must not delete or weaken material semantics, discard difficult cases, narrow the intended range, relax feasibility/targets/budgets, expose future information, or substitute an algorithm-internal surrogate merely to obtain tractability or a pass.

## 12. Algorithm Information And Auditability

Define decision-time observations, exogenous-state access, decision domains, feasibility masks or residuals, objective components, terminal signals, trace fields, units, and seed controls. Separate decision-time information from audit-only diagnostics and identify every field needed for independent recomputation. Future or hidden information remains unavailable unless the formal information pattern explicitly authorizes it.

## 13. Environment Amendment Review

An algorithm or experiment may submit evidence of an environment defect but may not directly change problem semantics. Every proposal records its origin and appropriate evidence. An `algorithm_failure` proposal must include route-specific repair exhaustion and leaves final failure classification to environment design. Domain, audit, or experiment-originated proposals instead provide method-independent causal or formal evidence and do not require prior algorithm failure. All proposals include the classified minimal change, impacts, non-simplification check, preserved invariants, successor versions, invalidations, and reruns.

Accept the request only when all six tests pass:

- **origin evidence:** for `algorithm_failure`, environment L1, algorithm-code fidelity, and route-specific algorithm-design repairs are current so environment review can classify the cause; for other origins, the required method-independent evidence is current;
- **causal necessity:** communication or task evidence requires the change;
- **semantic preservation:** the task outcome, scientific question, and central tradeoff remain intact;
- **information honesty:** no future, hidden, or audit-only information is newly exposed;
- **method neutrality:** the environment is not tailored to favor a method or ranking;
- **non-simplification:** no material item is removed or weakened for tractability, ranking, or acceptance; any independently proven modeling error is replaced with scenario-faithful semantics that preserve causal difficulty and the central tradeoff.

If the formal semantics change while research identity remains intact, classify the proposal as `formal_amendment` and create new formal-problem and MES versions. If research identity changes, classify it as `research_reframe` and start a new paper-scenario lineage. Never rewrite an accepted version in place.

## 14. Verdict And Readiness

Keep the original design verdict and report readiness separately:

- `paper-worthy`: the paper scenario, formal problem, active coupling, complexity balance, MES, and auditability support one coherent study.
- `salvageable`: the scientific problem is meaningful but one or more design gates require a concrete repair.
- `modeling-only`: the formulation is useful, but current evidence does not establish the need for a new algorithmic contribution.
- `toy`: the task semantics, binding constraints, coupling, or central tradeoff are not active enough for the intended study.
- `needs-literature`: domain validity, formulation precedent, parameter applicability, or comparison sufficiency requires external evidence.

Readiness meanings:

- `environment-valid`: L1 establishes that the task causal chain, formal problem, applicability range, paper-to-MES relation, and executable contract are coherent and supported for the recorded versions.
- `algorithmic-need`: `demonstrated` only when L2's frozen, method-independent, sufficiently tuned, and budget-matched probes cannot reach the predeclared target; otherwise `not_demonstrated`, `contradicted`, `insufficient_evidence`, or `stale` as supported by the evidence.
- `interface-complete`: decision-time information and audit-only evidence are sufficient and correctly separated for algorithm work.
- `joint-ready`: reserved for downstream acceptance after the algorithm specification and implementation pass against the same environment version.

Attach each non-pass verdict to the earliest failed design gate and a specific repair. An environment may be `environment-valid` without supporting a new algorithmic contribution. Do not modify a valid MES merely to turn L2 into a probe failure.
