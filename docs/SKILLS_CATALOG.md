# CCFA Skills Catalog

This is the public trigger index for the 19-skill CCFA family. `SKILL.md` remains
authoritative when another document conflicts with a runtime skill.

![Runtime catalog](../assets/ccfa-skills-catalog.svg)

## Runtime Skills

| Skill | Owner intent | Boundary |
| --- | --- | --- |
| `ccf-project-scaffolder` | Create project folders, templates, and `ccfa.yaml`. | No research content. |
| `ccf-pipeline-orchestrator` | Plan stages/gates/state or create a post-acceptance conclusion-evidence plan. | No phase implementation/audit, invented results, visuals, or manuscript prose. |
| `ccf-idea-optimizer` | Explore, rescue, and concretize rough research directions. | Does not rank multiple ideas as the main task. |
| `ccf-idea-reviewer` | Score, compare, rank, and triage ideas when judgment is explicit. | Does not brainstorm or optimize a single idea as the main task. |
| `ccf-literature-monitor` | Track recent papers, venues, labs, competitors, and novelty threats. | Does not replace deep literature search. |
| `ccf-literature-searcher` | Search prior art, formulations, settings, baselines, and opportunities. | Does not audit only existing citations. |
| `ccf-mes-validation` | Phase A: complete problem document -> minimal-but-complete MES/environment -> initial algorithm -> audit/repair -> frozen anchor. | No post-anchor upgrade or paper-range evidence plan. |
| `ccf-complexity-upgrade` | Phase B: current MES/code/results -> upgrade scenario document -> existing-environment edit/audit -> algorithm modification/audit/repair. | No new MES or unchanged-algorithm baseline. |
| `ccf-env-code-auditor` | Independently audit Phase-A/Phase-B environment code, information timing, feasibility, independent execution, and tradeoff/upgrade consistency. | Does not design, implement, repair, or judge algorithms. |
| `ccf-algorithm-code-auditor` | Independently audit initial/upgraded algorithm code, role, semantics, reference evidence, and current-scenario behavior. | Does not design, implement, or repair. |
| `ccf-visual-composer` | Compose and QA publication figures/tables, plots, palettes, captions, and manuscript integration from supplied results. | Does not design experiments or invent values. |
| `ccf-paper-to-exemplar` | Convert supplied PDFs into reusable writing exemplar cards. | Does not draft or review papers. |
| `ccf-paper-writer` | Draft, revise, polish, compress, and presentation-adapt manuscript text. | Does not perform full review, evidence audit, submission check, or rebuttal. |
| `ccf-paper-reviewer` | Review manuscripts scientifically and stylistically. | Does not rewrite or rebut. |
| `ccf-integrity-auditor` | Audit conclusion support, numbers, figures/tables, and citations. | Does not replace broad search or full review. |
| `ccf-submission-checker` | Check venue rules, LaTeX/PDF, anonymity, metadata, and artifacts. | Does not polish content. |
| `ccf-rebuttal-writer` | Write rebuttals, response letters, revision ledgers, and resubmission plans. | Not ordinary manuscript writing. |
| `ccf-common` | Maintain shared routing, terminology, source, privacy, state, and artifact contracts. | Not an ordinary research skill. |
| `ccf-skill-forger` | Maintain skills, docs, generated diagrams, validation, and releases. | Not research writing, review, or experiments. |

## Communication Phases

```text
Phase A: ccf-mes-validation
  complete scientific-problem document
    -> minimal-but-complete MES/environment implementation
    -> environment consistency audit and tradeoff sanity check
    -> initial algorithm implementation
    -> algorithm audit and focused repair
    -> freeze accepted anchor

Phase B: ccf-complexity-upgrade
  accepted MES + current code/results
    -> write upgrade scenario document
    -> modify existing environment and run consistency audit
    -> modify algorithm mechanism
    -> algorithm audit and focused repair
    -> accepted upgrade or concrete blocker
```

Phase B may add uncertainty, state, topology, load, information timing,
constraints, coupling, or robust evaluation semantics. The upgrade is a direct
extension of the existing environment; it is never another MES.

## Merged Runtime Entries

| Removed name | Current owner |
| --- | --- |
| `ccf-env-design` | Phase A initial problem/MES contract; Phase B upgrade document |
| `ccf-algorithm-designer` | Phase A initial algorithm; Phase B algorithm modification/repair |
| `ccf-experiment-debugger` | Phase-owned focused repair notes and reruns |
| `ccf-experiment-designer` | Pipeline evidence plan, writer prose, visual composer figures/tables, integrity audit |
| `ccf-workflow-planner` | `ccf-pipeline-orchestrator` |
| `ccf-paper-compressor`, `ccf-paper-presenter` | `ccf-paper-writer` |
| `ccf-writing-reviewer` | `ccf-paper-reviewer` |
| `ccf-citation-auditor` | `ccf-integrity-auditor` |
| `ccf-artifact-packager`, `ccf-venue-format-guide` | `ccf-submission-checker` |
| `ccf-resubmission-adapter` | `ccf-rebuttal-writer` |
