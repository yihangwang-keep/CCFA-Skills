# Communication Research Contract Terms

Use these terms across the communication environment, algorithm, audit, repair, and experiment-design skills. They describe the research object itself rather than a particular implementation technique.

## Canonical Terms

- **Paper scenario:** the communication task, actors, physical/network conditions, task consequences, and abstraction boundary studied by the paper.
- **Formal optimization problem:** the decision variables, objective, constraints, dynamics, uncertainty, information pattern, and feasibility meaning derived from the paper scenario.
- **Parameter applicability range:** the method-independent range of physical, communication, task, load, deadline, topology, and uncertainty settings for which the formal problem and final conclusions are intended to hold.
- **Scenario MVP:** the first complete, reproducible instance obtained by fixing parameters of the formal problem. It may reduce coverage but must not remove the objective, material constraints, decision coupling, information pattern, feasibility meaning, or task causal chain.
- **Task causal chain:** the path from exogenous conditions and communication decisions through network behavior to task or service consequences. A physical network event such as reconnection, contact, or successful transmission is not automatically task recovery; trace it through application state, dependencies, completion, and acknowledgement semantics.
- **Central tradeoff:** the attributable conflict among task value, communication resources, feasibility, delay, reliability, freshness, energy, or another domain quantity that the optimization must resolve.
- **Information pattern:** what is available at each decision time, when it becomes available, and what remains unavailable, future, or audit-only.
- **Feasibility meaning:** the task, physical, protocol, resource, safety, or service conditions that make a decision admissible.
- **Causal bottleneck:** the scarce resource, binding constraint, dependent event, or coupled decision through which communication affects the task outcome.
- **Supported conclusion:** a paper conclusion whose stated applicability range is no broader than the supplied analysis, proof, execution, or experimental evidence.
- **Conclusion applicability range:** the scenario versions, parameter range, assumptions, information pattern, and operating conditions under which a supported conclusion may be used.
- **Environment-valid:** the paper scenario, formal problem, parameter range, scenario MVP, and environment implementation consistently represent the intended communication problem.
- **Joint-ready:** an environment-valid problem also has an accepted algorithm contract, executable verification path, and sufficient evidence to proceed to paper-range experiment design.

Environment design and environment-code audit may issue `environment-valid`, plus separate findings on algorithmic need and interface completeness. They do not issue `joint-ready`; that downstream state requires a current accepted algorithm specification and implementation audit against the same environment version.

## Environment And Algorithm Authority

The environment owns the paper scenario, formal optimization problem, parameter applicability range, scenario MVP, information pattern, and feasibility meaning. The algorithm consumes a versioned environment contract. It may challenge that contract with evidence, but it must not directly change the objective, constraints, task semantics, or information pattern.

An algorithm-originated environment amendment must establish:

1. the same defect remains when the current algorithm is replaced by another credible solver or rule;
2. the amendment follows from the task causal chain, physical model, protocol, standard, trace, or service requirement;
3. the task or service outcome, scientific question, task causal chain, central tradeoff, and intended contribution type are preserved; a material R1 change that preserves this research identity starts a rebaselined problem version, while a change to the identity is a reframe;
4. no future, global, exact-solution, or audit-only information becomes algorithm-visible without a justified change to the information pattern;
5. the amendment improves the problem definition independently of the proposed algorithm's ranking.

Changing a formula or interface to enforce an already declared feasibility or information meaning is a contract correction. Changing what counts as feasible, what is available at decision time, the objective semantics, or the material feasible set is a new R1 problem version even when the research identity is preserved. Neither kind of change may inherit current algorithm, baseline, or result evidence without the declared reruns.

## Terminology Boundaries

- Use **paper conclusion**, **supported conclusion**, **conclusion applicability range**, or **statement** instead of `claim` in runtime skills and project contracts.
- In communication skills, `model` means a physical, mathematical, channel, traffic, mobility, queueing, protocol, or optimization model.
- Use **objective**, **cost**, **utility**, **constraint residual**, or **feasibility signal** instead of `reward` unless the accepted algorithm is explicitly formulated with that term.
- Use **scenario**, **trace**, **configuration**, **parameter setting**, or **operating regime** instead of training- or dataset-oriented language unless those objects are genuinely part of the user's problem.
- Do not introduce learning, training, prediction, or generalization terminology merely because an algorithm is being designed. Use it only when the accepted formal problem and selected algorithm require it.
- Runtime terms such as reviewer, tool, or sub-agent describe execution roles only. Do not use them as substitutes for communicating entities, decision makers, controllers, or network nodes in the paper scenario.

## Evidence Wording

Internal protocols may keep complete gate matrices, candidate comparisons, and evidence ledgers. User-visible output should lead with the requested artifact and expose only the supported conclusion, decisive evidence, material limitation, version change, required rerun, or user decision that affects the result.
