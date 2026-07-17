# CCFA Native Implementation Review Protocol

Use this protocol from ccf-env-code-auditor or
ccf-algorithm-code-auditor whenever an executable audit, repair
verification, debugger-round closure, or terminal acceptance requires an
implementation review. It defines the review mechanism only. The environment
and algorithm audit protocols remain authoritative for their respective
research semantics.

## Purpose And Boundaries

The auditor is the review coordinator and owns the final domain verdict. It
starts two independent, fresh, read-only reviewers in parallel:

1. domain-contract-fidelity: checks the environment or algorithm contract
   supplied by the invoking auditor;
2. implementation-assurance: checks whether the implementation and its
   evidence can be trusted, reproduced, and maintained.

The reviewers report findings; they do not edit code, specifications, tests,
configuration, or evidence. An actor that changed the candidate artifact set
cannot review that same set. A repair is followed by a new artifact set and a
new reviewer pair. The protocol is version-control agnostic and has no external
review-skill dependency.

## Review Inputs

Before spawning reviewers, the coordinator freezes an auditable artifact set.
The set must include the applicable authority and specification artifacts, the
current minimum executable scenario (MES), implementation and configuration
files, test/checker entry points, the validation-contract version, the original
failure when one exists, and references to raw execution evidence.

Every included file is identified by a content digest, not by a timestamp or a
mutable path alone. Canonically sort manifest entries by normalized
repo-relative path, role, and digest, then deterministically serialize them
together with every review-determining context field shown below. Set
`artifact_set_id` to the SHA-256 of that canonical review envelope. Raw evidence,
the validation contract, invoking domain profile, this shared review protocol,
and any repository standards must be digested inputs, so a change to review
semantics makes the old review stale even when code is unchanged:

~~~yaml
artifact_set_id: sha256:<canonical-review-envelope-digest>
artifact_set_kind: input | candidate | accepted
manifest:
  - path:
    role: authority | specification | implementation | configuration | test | evidence | validation_contract | domain_profile | review_protocol | repository_standard
    digest: sha256:<content-digest>
authority_versions: []
minimum_executable_scenario_version:
validation_contract_version:
validation_contract_ref:
validation_contract_digest:
domain_profile_ref:
domain_profile_digest:
review_protocol_ref:
review_protocol_digest:
repository_standard_refs_and_digests: []
changed_paths: []
original_failure_ref:
original_failure_digest:
coordinator_id:
implementer_ids: []
declared_read_only_commands: []
~~~

The coordinator recomputes the canonical review-envelope digest before dispatch, synthesis,
and acceptance. It verifies that every digest is present and the candidate has
not changed. A missing digest, missing
authority, unavailable required input, or an unbound command makes the review
`not_run`. When a reviewer runs against a valid bundle but decisive evidence is
incomplete, that axis is `conditional`. The coordinator must not replace either
reviewer with self-review to obtain a pass.

## Fresh Reviewer Dispatch

Dispatch both reviewers from the same frozen input bundle, but do not include
the other reviewer's prompt or report. Do not include an implementer's private
repair rationale or a prior pass as proof. Reviewers may inspect source and
run only declared non-destructive commands; they must not edit, format, install
dependencies, alter seeds, relax criteria, or delete a failing case.

### Domain-contract reviewer

Use the exact versioned domain profile supplied by the invoking environment or
algorithm auditor. The shared protocol does not copy those domain gates or own
their scientific decisions. Record `domain_profile_ref` in the frozen bundle,
apply every required gate in that profile, and report contradictions without
redesigning the environment or algorithm. The environment profile serves L1;
the environment auditor separately owns L2 execution and `algorithmic_need`.

### Implementation-assurance reviewer

Check implementation risks that can invalidate domain evidence:

- independent checkers, reference solvers, and accounting do not reuse the
  production calculation path;
- the original failure and controlled regressions can actually fail, and
  assertions observe the intended quantity;
- configuration precedence, seed/reset behavior, state isolation, and raw
  evidence are reproducible;
- error paths, solver statuses, numerical stability, termination, and resource
  limits are explicit;
- no silent clipping, hidden fallback, future/audit-only information leak, or
  result-only success path can manufacture a pass;
- changed behavior has a coherent owner and does not scatter one semantic
  change across unrelated implementations.

Repository-specific standards may add findings. If no standards source is
available, record that limitation and use this minimum assurance list; do not
invent repository rules.

### Reviewer prompt contract

Each fresh reviewer receives a prompt equivalent to:

~~~text
Read only the frozen artifact bundle and your assigned axis profile. Work as a
read-only reviewer. Do not edit, format, install, relax criteria, remove a
failure, or infer a pass from another reviewer or an implementer's report.
Report only material findings in the required schema, with exact locations and
evidence. Return pass only when required evidence for your axis is current;
return conditional for missing decisive evidence and fail for a contradiction
or failed material check.
~~~

Before accepting either report, verify that `coordinator_id` is present, both
reviewers record `fresh: true` and `read_only: true`, both `agent_id` values are
present and distinct, and both IDs are absent from both `implementer_ids` and
`coordinator_id`. A false, unknown, or missing capability, missing identity,
same-agent two-axis review, coordinator review, or failed implementer exclusion
makes the affected review `not_run`; self-review cannot be relabeled as
independent or enter terminal acceptance.

## Finding Schema

Every material finding is independent and traceable:

~~~yaml
id:
axis: domain-contract-fidelity | implementation-assurance
severity: blocker | major | minor | note
status: open | resolved | not_applicable
location: path:line
authority_ref:
observed_evidence:
consequence:
repair_owner:
closure_condition:
invalidated_checks: []
required_reruns: []
related_ids: []
~~~

Reviewers do not score the candidate. Findings from separate axes remain
separate even when they describe related symptoms; related_ids may link them,
but one axis cannot offset another.

## Axis And Combined Status

Each reviewer returns exactly one of:

- pass: required checks for that axis are current and no material contradiction
  is present;
- conditional: no contradiction is established, but decisive evidence is
  incomplete;
- fail: a material contradiction or failed check is present;
- stale: the reviewed artifact digest no longer matches the candidate;
- not_run: the required reviewer or input capability was unavailable;
- not_applicable: the invoking audit explicitly excludes the axis.

The combined implementation-review status uses the same enum and follows this
precedence:

1. any `stale` axis makes the combined status `stale`;
2. otherwise any required `not_run` axis makes it `not_run`;
3. otherwise any applicable `fail` axis makes it `fail`;
4. otherwise any applicable `conditional` axis makes it `conditional`;
5. all applicable axes `pass` makes it `pass`;
6. only when every axis is explicitly excluded may it be `not_applicable`.

`stale` and `not_run` block acceptance and cannot be converted to pass by
coordinator self-review.

Do not average, rank, or trade findings across axes. If reviewers disagree,
preserve both reports and request targeted evidence. A domain audit verdict may
be stricter than this combined status, but never looser.

## Repair And Staleness

The auditor or debugger routes an open finding to its owner after the review
has ended. The owner may make one authorized delta, but cannot sign the review
of that delta. Before the delta, preserve the old artifact set and failure
record. After the delta:

1. create a new candidate manifest and digest;
2. mark all dependent domain and implementation-review records stale;
3. rerun the original failure and every invalidated check;
4. dispatch fresh reviewers against the new candidate set;
5. close a finding only when its closure condition and all required reruns are
   current.

An unchanged candidate may satisfy terminal acceptance using a current review
whose purpose is terminal_acceptance; a round-only report must not be reused
as a terminal review without that scope being recorded.

## Internal Record And Visible Projection

The coordinator stores the complete record internally:

~~~yaml
review_id:
purpose: executable_audit | repair_verification | round_closure | terminal_acceptance
audit_kind: environment | algorithm
input_artifact_set_id:
candidate_artifact_set_id:
coordinator_id:
implementer_ids: []
reviewer_exclusion_check: pass | fail | unknown
reviewer_distinctness_check: pass | fail | unknown
reviewer_coordinator_exclusion_check: pass | fail | unknown
reviewer_capability_check: pass | fail | unknown
reviewers:
  domain_contract_fidelity: {agent_id:, fresh: true, read_only: true, status:, report_ref:}
  implementation_assurance: {agent_id:, fresh: true, read_only: true, status:, report_ref:}
findings: []
axis_status: {}
combined_status:
reviewed_artifact_set_id:
~~~

The default user-visible projection is findings-first and keeps axes distinct:

~~~text
Verdict: pass / conditional / fail / stale / not_run / not_applicable; artifact_set_id and authority versions
Domain contract fidelity: status; material findings with path:line and evidence
Implementation assurance: status; material findings with path:line and evidence
Invalidated checks and required reruns:
Next owner or blocker:
~~~

Do not print the full trace matrix, discarded hypotheses, reviewer prompts, or
private deliberation unless a full audit record is requested.
