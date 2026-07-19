# Communication Research Contract Terms

Use these terms consistently in the communication scenario, environment,
algorithm, and audit skills. Keep the user-facing explanation simple; detailed
audit tables belong in the audit references.

## Core Terms

- **Paper scenario:** the communication task, actors, physical/network
  conditions, task consequences, and abstraction boundary studied by the paper.
- **Formal optimization problem:** decisions, objective, constraints, dynamics,
  uncertainty, information pattern, and feasibility derived from the scenario.
- **Parameter applicability range:** the method-independent settings for which
  the problem and a conclusion are intended to hold.
- **Minimum Executable Scenario (MES):** the paper's smallest end-to-end scale
  that is still complete. It keeps the causal chain, central tradeoff,
  objective, material constraints, decision coupling, information timing,
  feasibility, executable interface, and independent checks. "Minimum" refers
  to scale, not to an easier or different problem.
- **MES anchor:** the accepted Phase-A MES and its initial algorithm.
- **Task causal chain:** the path from exogenous conditions and communication
  decisions through network behavior to a task or service outcome.
- **Central tradeoff:** the attributable conflict among task value, resources,
  delay, reliability, freshness, energy, or another domain quantity that the
  optimization must resolve.
- **Information pattern:** what is visible at each decision time, when it is
  revealed, and what remains future or audit-only.
- **Feasibility meaning:** the physical, protocol, resource, safety, or service
  conditions that make a decision admissible.
- **Causal bottleneck:** the scarce resource, binding constraint, dependent
  event, or coupled decision through which communication changes the outcome.
- **Environment-valid:** the current document, formal problem, interface, and
  environment implementation agree and execute as specified.
- **Joint-ready:** the environment is valid and the current algorithm has
  passed its independent audit for the same document and interface.

## Authority And Repair

The active phase document is the authority for objectives, constraints,
information, and task semantics. Code and algorithms must follow it. A
document or environment change is justified only by independent evidence and a
causal explanation; it cannot be made merely to improve an algorithm's score.

If an algorithm fails, first inspect and repair the algorithm. If evidence shows
that the problem or environment is wrong, record a new document version, update
the environment, and rerun the affected audits. Never remove the central
tradeoff, weaken a material constraint, or expose future information to obtain
acceptance.

## Method Roles

- **`environment_probe`:** a simple rule used to check that the MES activates
  the bottleneck and tradeoff. It is environment evidence, not the proposed
  method.
- **`proposed`:** the algorithmic contribution. Its decision path must follow
  the declared mechanism and interface, without hidden fallback rules.
- **`baseline`:** a comparison method, evaluated under matched information,
  feasibility, and resource conditions.
- **`reference` / `diagnostic`:** an exact solver, oracle, bound, checker, or
  targeted test with an explicit scope.

## Phase Vocabulary

Phase A is: problem document -> MES/environment -> environment audit -> initial
algorithm -> algorithm audit and repair -> frozen anchor. Phase B is: current
scenario, implementation, and results -> upgrade scenario document -> direct
changes to the existing environment -> environment audit -> algorithm
modification and repair -> algorithm audit.

Use **supported conclusion** and **applicability range** for paper statements.
Use **objective**, **cost**, or **utility** instead of `reward` unless the
accepted problem explicitly uses that term. Use **scenario**, **trace**, and
**configuration** instead of training- or dataset-oriented language unless
those objects genuinely belong to the problem.
