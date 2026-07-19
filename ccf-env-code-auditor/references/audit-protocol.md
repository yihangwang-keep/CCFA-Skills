# Environment Audit Protocol

Use this protocol with `ccf-env-code-auditor`. It records evidence, not a
workflow state machine.

## 1. Define The Audit Scope

Before auditing, clearly identify the exact scientific problem,
mathematical formulation, environment implementation, configuration that will be examined.

The audit report must correspond to a specific version of the problem
definition and implementation. A changed document or implementation needs a fresh audit.

## 2. Check Scientific Formulation to Implementation

For every important element in the scientific formulation,
identify its corresponding implementation and information flow.

The purpose is not to document every line of code, but to confirm that the implemented mechanism preserves the intended scientific formulation.


## 3. Scientific-Problem Fidelity Checks

Check whether the implementation exposes the documented scientific question,
core problem, causal bottleneck, and competing objectives/constraints. Confirm
that state/action timing, feasibility meaning, and information visibility are
consistent with that problem. Report any hidden assumption or shortcut that
removes the intended tradeoff.

## 4. Lightweight Tradeoff Probes

Do not run a complete algorithm or scenario as audit evidence. Instead, use
small, predeclared and reproducible probes such as:

- a simple heuristic with parameter sweep that favors one objective or constraint;
- a second heuristic that favors the competing objective or constraint;
- a random policy;

Evaluate each probe with the environment's declared objective and constraints.
The evidence should show that generic choices do not trivially achieve both
competing goals, that actions affect the documented causal path, and that the
environment code makes the tradeoff observable. These probes validate the
scientific scenario; they are not proposed-algorithm performance evidence.

## 5. Finding And Repair Handoff

For every material finding record:

```yaml
finding:
  audit: environment
  location: path:line
  reason:
```

Return the reason without editing. The responsible owner handles any repair and
requests this audit again when needed.
