# Communication Research Contract Terms

Use these terms across the communication environment, algorithm, audit, repair, and experiment-design skills. They describe the research object itself rather than a particular implementation technique.

## Canonical Terms

- **Paper scenario:** the communication task, actors, physical/network conditions, task consequences, and abstraction boundary studied by the paper.
- **Formal optimization problem:** the decision variables, objective, constraints, dynamics, uncertainty, information pattern, and feasibility meaning derived from the paper scenario.
- **Parameter applicability range:** the method-independent range of physical, communication, task, load, deadline, topology, and uncertainty settings for which the formal problem and final conclusions are intended to hold.
- **Minimum Executable Scenario (MES):** the smallest end-to-end scenario package for one accepted paper-scenario and formal-problem version. It preserves the complete task causal chain, objective, material constraints, decision coupling, information pattern, feasibility meaning, and central tradeoff, and binds them to executable entry points, registered configurations, interfaces, seeds or traces, an independent checker, and acceptance criteria. It may contain more than one registered case when those cases are necessary to activate the tradeoff. "Minimum" means causally and auditably complete, not the fewest entities or easiest instance.
- **MES anchor and complexity ladder:** the first accepted MES is the immutable anchor for algorithm validation. Its L2 heuristic-probe/algorithmic-need test is run once for the anchor. After L1/L2 and the initial algorithm pass, increase scale, load, topology, uncertainty, coupling, or other method-independent complexity through explicitly recorded complexity stages under the same formal-problem and MES interface. A complexity stage is evidence expansion, not a redesigned or successor MES; it checks implementation consistency, anchor regression, and the current algorithm, while failures route to algorithm diagnosis and repair.
- **MES lineage:** accepted MES artifacts are immutable evidence. New complexity stages point to the anchor and record their delta without creating a successor MES. A formal semantic change creates a new formal-problem version and requires a fresh candidate MES/evidence epoch; a changed research identity creates a new paper-scenario lineage. Legacy `scenario_extension` records remain readable but are not the default route for new complexity work.
- **Task causal chain:** the path from exogenous conditions and communication decisions through network behavior to task or service consequences. A physical network event such as reconnection, contact, or successful transmission is not automatically task recovery; trace it through application state, dependencies, completion, and acknowledgement semantics.
- **Central tradeoff:** the attributable conflict among task value, communication resources, feasibility, delay, reliability, freshness, energy, or another domain quantity that the optimization must resolve.
- **Information pattern:** what is available at each decision time, when it becomes available, and what remains unavailable, future, or audit-only.
- **Feasibility meaning:** the task, physical, protocol, resource, safety, or service conditions that make a decision admissible.
- **Causal bottleneck:** the scarce resource, binding constraint, dependent event, or coupled decision through which communication affects the task outcome.
- **Supported conclusion:** a paper conclusion whose stated applicability range is no broader than the supplied analysis, proof, execution, or experimental evidence.
- **Conclusion applicability range:** the scenario versions, parameter range, assumptions, information pattern, and operating conditions under which a supported conclusion may be used.
- **Environment-valid:** the paper scenario, formal problem, parameter range, frozen anchor MES, active complexity stage (when applicable), and environment implementation consistently represent the intended communication problem.
- **Joint-ready:** an environment-valid problem also has an accepted algorithm contract, executable verification path, and sufficient evidence to proceed to paper-range experiment design.

Environment design defines the L1 acceptance and L2 probe contracts and may issue a design verdict. Environment-code audit executes those contracts and owns `environment-valid`, `algorithmic_need`, and interface-completeness results. Neither issues `joint-ready`; that downstream state requires a current accepted algorithm specification and implementation audit against the same environment version.

## Environment And Algorithm Authority

The environment owns the paper scenario, formal optimization problem, parameter applicability range, MES lineage, information pattern, and feasibility meaning. The algorithm consumes a versioned environment contract. It may challenge that contract with evidence, but it must not directly change the objective, constraints, task semantics, information pattern, or MES.

An algorithm-originated environment or mathematical-model amendment must establish:

1. algorithm-code and algorithm-design repair have been exhausted for the current versions, with a repair ledger; when available, another credible solver, reference, bound, or probe reproduces the defect, or formal evidence independently establishes an infeasible/ill-posed authoritative problem, invalid environment-target evidence, information mismatch, or missing causal semantics. An unattainable algorithm-specific guarantee remains algorithm-owned;
2. the amendment follows from the task causal chain, physical model, protocol, standard, trace, or service requirement;
3. the task or service outcome, scientific question, task causal chain, central tradeoff, and intended contribution type are preserved; a material R1 change that preserves this research identity starts a rebaselined problem version, while a change to the identity is a reframe;
4. no future, global, exact-solution, or audit-only information becomes algorithm-visible without a justified change to the information pattern;
5. the amendment improves the problem definition independently of the proposed algorithm's ranking;
6. the successor does not simplify the research problem for tractability, ranking, or acceptance by deleting or weakening a material objective term, constraint, coupling, dynamic, uncertainty, information restriction, difficult registered case, target, feasibility rule, or resource limit; exposing future/audit-only information; or replacing the authoritative objective with an algorithm surrogate. An item independently proven inconsistent with the paper scenario may be corrected or replaced only when the intended causal difficulty and central tradeoff remain intact and all dependent evidence is rebaselined.

Changing a formula or interface to enforce an already declared feasibility or information meaning is a contract correction. Changing what counts as feasible, what is available at decision time, the objective semantics, or the material feasible set is a new R1 problem version even when the research identity is preserved. A documented algorithm-repair exhaustion triggers environment review, but it does not predetermine the amendment. If no causally justified, non-simplifying correction exists, keep the environment version and report the route as blocked, unsupported, or requiring a research reframe. Neither kind of change may inherit current algorithm, baseline, or result evidence without the declared reruns.

## Method Roles And Heuristics

Classify every executable decision method before using its evidence:

- **`environment_probe`:** a fixed, random-feasible, greedy, domain, or tuned simple rule used to test whether the MES activates the causal bottleneck, central tradeoff, feasibility boundary, and need for optimization. It is environment evidence, not the paper's proposed algorithm.
- **`proposed`:** the algorithmic contribution presented by the paper. Any heuristic decision mechanism in this role is a blocking failure, including a hidden fallback, manually patched branch, rule accumulation, heuristic local search, or renamed strategy. A formal wrapper or certified component elsewhere does not cure the heuristic component.
- **`baseline`:** a comparison method. Heuristic methods are allowed when labeled, properly tuned, and run under matched information, feasibility, stopping, and resource conditions.
- **`reference` or `diagnostic`:** an exact, oracle, bound, checker, or targeted diagnostic method whose certification scope is explicit.

Environment validity and proposed-algorithm admissibility are separate decisions. A heuristic probe can validate or challenge the initial MES without passing the proposed method's no-heuristic gate. It is not rerun as an algorithmic-need gate for later complexity stages. Conversely, rejecting a proposed heuristic does not by itself invalidate the environment. The algorithm designer owns role classification and the no-heuristic contract; the algorithm code auditor verifies it component by component; experiment design consumes the current acceptance record.

Use `algorithmic_need: demonstrated | not_demonstrated | contradicted | insufficient_evidence | stale` in machine-readable records. A completed, fair L2 sweep can yield either `demonstrated` or `not_demonstrated`; completion of the evidence procedure and the scientific outcome are separate fields.

- **Design-validation repair loop:** an operational loop for a failed implementation, algorithm, or accepted complexity-stage run. It preserves the failure, assigns one owner and one delta, and reruns invalidated checks; it does not design the initial problem, initial algorithm, or publication evidence.
- **Paper-range experiment design:** downstream evidence planning after anchor algorithm acceptance. It chooses settings, baselines, metrics, ablations, robustness checks, and conclusion-bound result artifacts; it consumes accepted stage contracts and does not repair environment or algorithm semantics.

Legacy `scenario MVP`, `scenario_mvp`, and `scenario_mvp_version` values may be read only as aliases for MES fields. New artifacts use `minimum_executable_scenario` and `minimum_executable_scenario_version`. If canonical and legacy values coexist and differ, report a version conflict rather than merging them.

## Terminology Boundaries

- Use **paper conclusion**, **supported conclusion**, **conclusion applicability range**, or **statement** instead of `claim` in runtime skills and project contracts.
- In communication skills, `model` means a physical, mathematical, channel, traffic, mobility, queueing, protocol, or optimization model.
- Use **objective**, **cost**, **utility**, **constraint residual**, or **feasibility signal** instead of `reward` unless the accepted algorithm is explicitly formulated with that term.
- Use **scenario**, **trace**, **configuration**, **parameter setting**, or **operating regime** instead of training- or dataset-oriented language unless those objects are genuinely part of the user's problem.
- Do not introduce learning, training, prediction, or generalization terminology merely because an algorithm is being designed. Use it only when the accepted formal problem and selected algorithm require it.
- Runtime terms such as reviewer, tool, or sub-agent describe execution roles only. Do not use them as substitutes for communicating entities, decision makers, controllers, or network nodes in the paper scenario.

## Evidence Wording

Internal protocols may keep complete gate matrices, candidate comparisons, rejected hypotheses, reviewer disagreements, artifact manifests, and evidence ledgers. These are model-working records, not a default response template. User-visible output should lead with the requested artifact and expose only the current verdict, decisive evidence, material limitation, version change, required rerun, next owner, or user decision that affects the result. Show the full internal record only when the user explicitly requests an audit trail.
