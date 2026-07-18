---
name: ccf-complexity-upgrade
description: "Own Phase B for an accepted communication-paper anchor: accept one versioned complexity-upgrade document, implement and audit the upgraded environment while preserving anchor regression, then modify, audit, and repair the algorithm. Use for complexity upgrade, 场景的升级, 复杂度升级Ralph闭环, robust/uncertain/scale/topology/information-pattern upgrades, or algorithm repair on an accepted anchor. Phase B never creates another MES, reruns L2, or changes the frozen anchor."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# Complexity Upgrade

## Phase Ownership

Phase B starts from one accepted Phase-A record, its immutable MES anchor, and its
accepted initial algorithm. It owns the upgrade document, stage environment
implementation, algorithm modification, and repair loop. The environment and
algorithm code auditors remain independent acceptance owners.

Phase B does not derive, name, register, or freeze another MES. A fixed minimal
configuration used to implement an upgrade is a `stage_case`, not an MES, MVP,
anchor, successor, or replacement. The accepted anchor remains an immutable
regression target even when the stage adds scale, topology, uncertainty,
coupling, state, information timing, constraints, or a method-independent robust
evaluation objective.

## Accepted Upgrade Document

Accept one user-approved upgrade document only when it records:

1. `stage_request_id`, document/version status, parent Phase-A record, frozen
   anchor and initial-algorithm digests, and the parent artifacts that must remain
   unchanged;
2. the parent scientific question and causal chain, inherited semantics, exact
   method-independent complexity delta, and why the delta is needed scientifically;
3. added or extended states, dynamics, uncertainty processes, information reveal
   timing, decisions, constraints, objectives, interfaces, and feasibility rules;
4. an explicit inherited/added/forbidden matrix proving that the upgrade extends
   rather than silently deletes or weakens the parent task semantics;
5. one reproducible `stage_case`, its configuration and range, environment
   implementation deliverables, algorithm-visible and audit-only fields, traces,
   independent checkers, and no-leakage tests;
6. stage-specific environment gates, parent anchor regression, evidence required
   before algorithm modification, and conditions that classify a failure as
   implementation, algorithm, unsupported upgrade, or research reframe;
7. a freeze rule that keeps existing algorithm files unchanged until the upgraded
   environment and independent checkers pass.

The document may introduce a versioned stage problem and richer formal objects.
It must not overwrite the Phase-A problem or state that its `stage_case` is a new
MES. If it changes the research identity, removes a parent invariant, or cannot
retain anchor regression, terminate as `reframe` and start a separate Phase A.

## Phase B Ralph Loop

Follow `../ccf-common/references/ralph-phase-contract.md`:

1. Validate and freeze the upgrade document, parent digests, stage case, gates,
   and algorithm-file freeze boundary before implementation.
2. Implement only the upgraded environment, versioned interface, traces,
   independent checker/reference paths, and stage tests. Do not modify the
   accepted algorithm during this environment subphase.
3. Invoke `ccf-env-code-auditor` to check document-to-code fidelity, causal and
   information semantics, stage execution, checker independence, and complete
   anchor regression. Inherit the Phase-A L2 result without rerunning or
   recomputing `algorithmic_need`.
4. Repair confirmed stage-document or environment-implementation defects with one
   smallest delta per round. Preserve every failed artifact set and rerun all
   invalidated stage checks plus anchor regression.
5. Only after the stage environment passes, unfreeze algorithm work. Run the
   accepted algorithm unchanged first and preserve that result as the upgrade
   baseline.
6. When the algorithm fails the accepted stage target, modify its implementation
   or mechanism while keeping the stage document, anchor, information boundary,
   cases, targets, tolerances, and resource limits fixed.
7. Invoke `ccf-algorithm-code-auditor` after each candidate algorithm delta. Rerun
   the original stage failure, stage algorithm checks, and anchor algorithm
   regression for the same artifact digests.
8. If credible algorithm repairs are exhausted, stop as `algorithm_failed` unless
   independent evidence establishes that the upgrade document itself is
   infeasible, ill-posed, causally unsupported, or informationally inconsistent.
   A document defect may create a new stage-document version, but still cannot
   create or modify an MES. A changed research identity routes to a new Phase A.

## Terminal Conditions

- `stage_accepted`: upgrade document, stage environment, all independent checkers,
  anchor regressions, upgraded algorithm, and native reviews pass for one current
  artifact set.
- `algorithm_failed`: the stage environment is valid, but the algorithm remains
  unaccepted after the recorded repair route.
- `upgrade_unsupported`: the proposed complexity delta lacks causal support or a
  feasible method-independent contract while the parent anchor remains valid.
- `blocked`: required artifacts, checker capability, execution resources, or a
  credible repair path are unavailable.
- `reframe`: the requested change replaces the parent research identity or cannot
  preserve the frozen anchor as regression evidence.

Read `references/phase-b-upgrade-contract.md` when drafting or validating the
upgrade document. Read `references/complexity-upgrade-record.md` when creating the stage record.
Publication-range evidence planning happens only after `stage_accepted` and is not
part of this Ralph loop.
