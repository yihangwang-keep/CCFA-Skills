# Ralph Phase Contract

Ralph is the small append-only repair discipline embedded in Phase A and Phase B.
It is not a runtime skill, a third audit, or a separate artifact owner.

## Shared Round

1. Read the fixed phase document, authority versions, acceptance criteria, and
   current artifact digests.
2. Select the earliest failed or stale dependency.
3. Assign one phase-owned implementation or design owner and apply one smallest delta.
4. Preserve the failure and old artifact set; mark every dependent check stale.
5. Rerun the original failure, invalidated checks, regressions, and the applicable
   fresh independent domain audit.
6. Append the round evidence to the phase record. Never replace earlier failures
   or inherit a verdict across changed artifact digests.
7. Stop only at the phase-specific scientific terminal conditions. A successful
   command, empty diff, iteration limit, or resource limit is not acceptance.

## Phase Separation

| Phase | Authority transition | Required checks | Forbidden action |
| --- | --- | --- | --- |
| `mes_validation` | complete problem document -> candidate MES/environment -> initial algorithm -> frozen accepted anchor | document contract, environment L1, one anchor-candidate L2, algorithm audit, fresh reviews | freezing the anchor before algorithm acceptance, hiding failure by weakening the problem, or starting a complexity stage |
| `complexity_upgrade` | frozen anchor + accepted algorithm + one upgrade document -> stage environment -> upgraded algorithm | stage document fidelity, stage execution, anchor regression, inherited L2, algorithm audit and regression | creating another MES, rerunning L2, changing the anchor, or modifying the algorithm before stage-environment acceptance |

Phase A may create a new candidate evidence epoch before anchor acceptance when
independent evidence establishes a document/model defect. Phase B may version its
upgrade document, but it never creates or edits an MES. A Phase-B change that
replaces the parent research identity or cannot preserve anchor regression ends
as `reframe` and requires a separate Phase A.
