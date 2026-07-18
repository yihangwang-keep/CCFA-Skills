# CCFA Architecture

CCFA routes by the user's current research object. Runtime skills are user-visible
owners, not every internal design or repair role.

## Research Flow

```text
scaffold -> plan -> idea -> literature
  -> Phase A: complete problem document -> candidate MES/environment
       -> independent environment audit + one-time L2
       -> initial algorithm -> independent algorithm audit
       -> frozen accepted anchor
  -> Phase B: one upgrade document -> stage_case environment
       -> independent stage audit + anchor regression; inherited L2
       -> run/modify/repair algorithm -> independent algorithm audit
       -> accepted stage or explicit failure
  -> evidence plan -> visuals -> manuscript -> review -> integrity
  -> submission -> rebuttal
```

## Communication Ownership

| Object | Owner | Independent checker |
| --- | --- | --- |
| Initial scientific-problem document, candidate MES/environment, initial algorithm, pre-anchor repair, anchor freeze | `ccf-mes-validation` | `ccf-env-code-auditor`, `ccf-algorithm-code-auditor` |
| Versioned complexity-upgrade document, `stage_case` environment, algorithm modification/repair, anchor regressions | `ccf-complexity-upgrade` | `ccf-env-code-auditor`, `ccf-algorithm-code-auditor` |
| Paper-range conclusion-evidence plan after acceptance | `ccf-pipeline-orchestrator` evidence-plan mode | `ccf-integrity-auditor` later checks supplied results/conclusions |
| Publication figures/tables from supplied real values | `ccf-visual-composer` | `ccf-integrity-auditor` checks numeric/text consistency |

Design and repair remain inside the active phase so users do not route among
environment designer, algorithm designer, and debugger skills. Auditors remain
separate because the implementation owner cannot independently accept its own
artifact set.

## Phase Rules

Phase A accepts a complete document only when it specifies the causal problem,
formal model, applicability range, candidate-MES derivation, information
boundary, executable configuration, independent checks, L1/L2 criteria, and
initial-algorithm target. The candidate becomes an anchor only after both
environment and initial-algorithm evidence pass.

Phase B begins from that immutable anchor and an accepted algorithm. Its upgrade
document may add scale, topology, uncertainty, coupling, state, information
timing, constraints, or robust evaluation semantics. It uses a `stage_case`, not
another MES. Environment implementation/audit happens before algorithm changes;
every algorithm candidate reruns the stage and anchor regression.

## Ralph Repair

Each phase keeps one append-only record. A round selects the earliest failed or
stale dependency, assigns one phase-owned implementation or design owner, applies
one smallest delta, preserves the old failure/artifact set, invalidates dependent
checks, and requests fresh independent audits. Command success or a loop limit is
never scientific acceptance.

## Artifact State

`ccfa.yaml` is a routing spine. Scenario-driven projects use:

```text
phase-a/             Phase-A document, candidate epochs, MES/algorithm versions, rounds, anchor terminal evidence
phase-b/             upgrade documents, stage_case versions, environment/algorithm deltas, regressions, rounds
environment-audit/   independent document-to-environment-code evidence
algorithm-audit/     independent specification-to-algorithm-code evidence
experiments/plan.*   post-acceptance conclusion-evidence plan
experiments/results.* user-supplied real results
figures/, tables/    visual-composer outputs
```

Accepted versions and failures are append-only evidence. Detailed gate ledgers,
digests, traces, and native reviews stay in their owner artifacts, not in
`ccfa.yaml`.

## Shared Governance

`ccf-common` owns routing, terminology, source/privacy policy, `ccfa.yaml`, and
artifact contracts. `ccf-skill-forger` remains the optional repository-maintenance
skill; it is not part of research execution.
