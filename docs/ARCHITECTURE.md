# CCFA Architecture

CCFA routes by the user's current research object. Runtime skills are user-visible
owners, not every internal design or repair role.

## Research Flow

```text
scaffold -> plan -> idea -> literature
  -> Phase A: complete problem document -> minimal-but-complete MES/environment
       -> independent environment audit and tradeoff sanity check
       -> initial algorithm -> independent algorithm audit/repair
       -> frozen accepted anchor
  -> Phase B: accepted MES + current code/results -> upgrade scenario document
       -> direct existing-environment modification -> independent environment audit
       -> algorithm modification/repair -> independent algorithm audit
       -> accepted upgrade
  -> evidence plan -> visuals -> manuscript -> review -> integrity
  -> submission -> rebuttal
```

## Communication Ownership

| Object | Owner | Independent checker |
| --- | --- | --- |
| Initial scientific-problem document, minimal-but-complete MES/environment, initial algorithm, pre-anchor repair, anchor freeze | `ccf-mes-validation` | `ccf-env-code-auditor`, `ccf-algorithm-code-auditor` |
| Upgrade scenario document from current code/results, direct environment modification/audit, algorithm modification/repair | `ccf-complexity-upgrade` | `ccf-env-code-auditor`, `ccf-algorithm-code-auditor` |
| Paper-range conclusion-evidence plan after acceptance | `ccf-pipeline-orchestrator` evidence-plan mode | `ccf-integrity-auditor` later checks supplied results/conclusions |
| Publication figures/tables from supplied real values | `ccf-visual-composer` | `ccf-integrity-auditor` checks numeric/text consistency |

Design and repair remain inside the active phase so users do not route among
environment designer, algorithm designer, and debugger skills. Auditors remain
separate because the implementation owner cannot independently accept its own
artifact set.

## Phase Rules

Phase A accepts a complete document only when it specifies the causal problem,
formal model, applicability range, minimal-but-complete MES derivation,
information boundary, executable configuration, independent checks, and
initial-algorithm target. The MES becomes an anchor only after both environment
and initial-algorithm evidence pass.

Phase B begins from that accepted MES, its current implementation, and existing
results. Its upgrade document may add scale, topology, uncertainty, coupling,
state, information timing, constraints, or robust evaluation semantics. It
directly modifies and audits the existing environment before changing the
algorithm. It does not require an unchanged-algorithm baseline; run a MES
compatibility regression only when shared code or the interface could affect
the frozen anchor.

## Ralph Repair

Each phase keeps one append-only record. A round starts from concrete failure
evidence, makes one focused document/environment/algorithm change, preserves the
old result, and reruns the failed and affected checks with fresh independent
audits. Command success or a loop limit is never scientific acceptance.

## Artifact State

`ccfa.yaml` is a routing spine. Scenario-driven projects use:

```text
phase-a/             Phase-A document, MES/algorithm versions, rounds, anchor evidence
phase-b/             upgrade documents, existing-environment/algorithm deltas, audits, rounds
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
