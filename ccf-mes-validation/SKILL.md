---
name: ccf-mes-validation
description: "Use for Phase A: turn a paper's complete scientific-problem document into one minimal-but-complete MES, implement and audit its environment, then implement and audit the initial algorithm. Use for 第一阶段 MES 验证 and the initial Ralph loop. Do not use for a post-anchor complexity upgrade."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# Phase A: Build The First MES

## Purpose

Phase A starts with the paper's scientific-problem document. It ends with one
working environment and one accepted initial algorithm. The environment and
algorithm auditors are independent reviewers; this skill implements the work
and owns the repair loop.

### What MES means

MES means **minimal but complete**. Reduce the paper problem's scale (for
example, fewer nodes, messages, or time slots), but keep the problem itself
intact. The MES must still contain:

- the paper's scientific question and task causal chain;
- the central tradeoff and its causal bottleneck;
- the objective and its ordering;
- every decision, material constraint, coupling, and feasibility rule;
- the information available at each decision time; and
- the task consequence that the communication decisions are meant to change.

If removing an object can change the preferred decision or make the tradeoff
disappear, it is not a valid MES reduction. MES is the paper's smallest
credible **scale**, not the paper's easiest or smallest **problem**. Once this
MES and its initial algorithm are accepted, freeze it. Phase B only adds
complexity on top of it; it does not redesign the MES.

## Input Document

Use the user's paper/scenario document, such as
`ideas/scenario-partition-merge-mission-consistency.md`, as the authority. It
must explain the background, causal chain, scientific question, tradeoff,
formal problem, MES scaling rule, interface, and acceptance evidence. Key
semantics must be written in the document. 

Read `references/phase-a-problem-contract.md` for the document outline before
implementation.

## Phase A Ralph Loop

Keep the loop visible and linear:

```text
paper problem document
  -> MES and environment implementation
  -> environment consistency audit
  -> initial algorithm implementation
  -> algorithm consistency audit
  -> focused repair of the algorithm or (when evidence requires it) the scenario
  -> repeat the affected audit
  -> accepted MES and its' algorithm
```

1. **Understand the document.** Write down the scientific question, causal
   chain, central tradeoff, and the exact objects that the MES must preserve.
   Completion means another reader can explain why this is the same problem at
   a smaller scale.
2. **Implement the MES and environment.** Build the
   minimal-but-complete MES and its environment code. 
3. **Run the environment audit.** Invoke `ccf-env-code-auditor`. If code and
   document disagree, fix the code. The audit must also show that the core tradeoff is active in the environment and easy algorithms can't solve the problem.
   If it is not active, return to the problem document/MES and fix the
   representation before implementing the algorithm.
4. **Implement the initial algorithm.** After the
   environment audit is clear,
   implement the algorithm for this exact formal problem. 
5. **Run the algorithm audit and repair.** Invoke
   `ccf-algorithm-code-auditor`. Repair the algorithm
   first up to best effort. Only when that evidence shows that the
   problem is infeasible, or missing a causal requirement should you
   revise the document. Under the new document version, rebuild or
   update the affected MES/environment document and complete a fresh environment audit
   before auditing the algorithm again. Never remove the tradeoff or relax a
   material rule just to make the algorithm pass.
6. **Freeze the result.** When both audits pass for the same document, MES,
   environment, and algorithm, record the versions and mark `mes_role: anchor`.
   This is the handoff to Phase B.

Each repair round should change one focused thing, preserve the old failure
evidence, and rerun the check that exposed the problem plus any check affected
by the change. Use the simple record in
`references/mes-validation-record.md`; detailed matrices stay with the
auditors.

## Handoff

Return the accepted problem document, MES configuration, environment and
algorithm entry points, audit reports, and a short repair history. If a
required input or executable path cannot be supplied, explain the concrete
blocker and leave the work open for correction. Do not start a Phase-B upgrade
from this skill.
