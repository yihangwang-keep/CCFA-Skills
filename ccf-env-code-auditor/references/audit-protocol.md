# Environment Audit Protocol

Use this protocol with `ccf-env-code-auditor`. It records evidence, not a
workflow state machine.

## 1. Freeze The Inputs

Record the current scientific-problem document, formal equations, environment
files, configuration, entry point, probe definitions, seeds, tests, and raw
probe outputs. Bind the report to exact versions or content digests. A changed
document or implementation needs a fresh audit.

## 2. Build The Trace

Create an internal row for every material item:

| Item | Meaning and timing | Code path | Static or probe evidence | Result |
| --- | --- | --- | --- | --- |
| parameter/state/observation/action | unit and reveal time | symbol and call path | trace or probe | pass/fail |

Cover initialization, transitions, objective, constraints, feasibility,
randomness, termination, metrics, and audit-only diagnostics. Reverse-trace
every code path that changes one of these quantities.

## 3. Scientific-Problem Fidelity Checks

Check whether the implementation exposes the documented scientific question,
core problem, causal bottleneck, and competing objectives/constraints. Confirm
that state/action timing, feasibility meaning, and information visibility are
consistent with that problem. Report any hidden assumption or shortcut that
removes the intended tradeoff.

## 4. Lightweight Tradeoff Probes

Do not run a complete algorithm or scenario as audit evidence. Instead, use
small, predeclared and reproducible probes such as:

- a simple heuristic that favors one objective or constraint;
- a second heuristic that favors the competing objective or constraint;
- a seeded random policy or random feasible actions;
- a small parameter sweep over the relevant environment control.

Evaluate each probe with the environment's declared objective and constraints.
The evidence should show that generic choices do not trivially achieve both
competing goals, that actions affect the documented causal path, and that the
environment code makes the tradeoff observable. These probes validate the
scientific scenario; they are not proposed-algorithm performance evidence.

## 5. Independent Review

When explicitly required by the project, use the shared implementation-review
protocol to obtain:

- a domain-contract review of scientific-problem and document-to-code fidelity;
- an implementation-assurance review of probe reproducibility, error handling,
  and hidden information or action repair.

Both reviewers are fresh and read-only. The implementer cannot review its own
changed artifact. Report `pass`, `conditional`, `fail`, or `not_run` for each
axis and keep the reports separate.

## 6. Finding And Repair Handoff

For every material finding record:

```yaml
finding:
  location: path:line
  observed:
  expected:
  consequence:
  repair_owner: document | environment
  rerun:
```

Return findings without editing. The responsible owner decides whether to
change the document or code, keeps the old evidence, and requests this audit
again.
