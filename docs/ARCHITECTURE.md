# CCFA Architecture

CCFA is a 21-skill paper-project workflow family, not a loose collection of unrelated writing prompts. The v0.8 architecture has one owner skill per responsibility area and uses `ccfa.yaml` plus explicit artifact contracts to keep stages connected.

![Architecture](../assets/ccfa-skills-architecture.svg)

## Core Model

The family has three layers:

| Layer | Purpose | Skills |
| --- | --- | --- |
| Research production chain | Move a paper project from project setup through versioned design validation to rebuttal. | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-literature-monitor`, `ccf-literature-searcher`, `ccf-env-design`, `ccf-env-code-auditor`, `ccf-algorithm-designer`, `ccf-algorithm-code-auditor`, `ccf-experiment-debugger`, `ccf-experiment-designer`, `ccf-visual-composer`, `ccf-paper-to-exemplar`, `ccf-paper-writer`, `ccf-paper-reviewer`, `ccf-integrity-auditor`, `ccf-submission-checker`, `ccf-rebuttal-writer` |
| Shared state and policy | Keep routing, evidence, privacy, source registry, and artifact ownership consistent. | `ccf-common` |
| Family maintenance | Maintain skills, docs, generated SVGs, validation, and releases. | `ccf-skill-forger` |

The main chain is:

```text
scaffold -> orchestrate -> optimize idea -> review idea
         -> monitor recent literature -> search literature
         -> design scenario -> audit environment implementation
         -> design algorithm -> audit algorithm implementation
         -> repair failed MVP and rerun affected gates when needed
         -> design experiments -> compose visuals -> optional exemplar extraction
         -> write manuscript -> review manuscript -> audit conclusion/evidence support
         -> check submission -> rebuttal / ledger / resubmission
```

The rebuttal stage can loop back to writing, experiments, integrity audit, or submission checks. This is why rebuttal is not a dead-end output skill; it owns response structure and ledger discipline, while actual manuscript edits go back to `ccf-paper-writer`.

## Versioned Design-Validation Loop

The communication problem follows a separate Ralph-style loop before publication-range experiment design:

```text
ccf-env-design
  -> ccf-env-code-auditor                 [environment-valid]
  -> ccf-algorithm-designer
  -> ccf-algorithm-code-auditor           [joint-ready]
  -> ccf-experiment-debugger on failure
       -> one minimal change by one owning skill
       -> rerun every invalidated audit gate
       -> return to environment-valid / joint-ready
```

The environment owns the paper scenario, formal optimization problem, parameter applicability range, scenario MVP, information pattern, and feasibility meaning. Algorithm failure may produce an evidence-backed environment amendment request, but it may not silently change the objective, constraints, task semantics, information pattern, or test settings. Any accepted semantic change creates a new problem version, preserves the failed version as historical evidence, and invalidates downstream algorithm, baseline, and result evidence until affected gates are rerun.

At checkpoint commits, invoke the installed `$code-review` skill with the fixed comparison point and accepted specification. CCFA records the checkpoint and consumes its report; it does not copy or redefine the external skill's Standards/Spec review rules.

## Artifact State

`ccfa.yaml` records the project state:

- `version`
- `project`
- `target_venue`
- `stage`
- `artifacts`
- `paper_conclusions`
- `experiments`
- `reviews`
- `revision_ledger`
- `submission_checks`

The file is not meant to contain the whole paper. It is a routing and status spine. Concrete outputs still live in manuscript, review, evidence, experiment, submission, artifact, and rebuttal files.

![Artifact contract](../assets/ccfa-skills-artifacts.svg)

## Owner Boundaries

The family intentionally merged helper skills into owner modes. In v0.8, `ccf-visual-composer` also carries a small self-contained Python SVG plotting recipe library so paper-visual examples can run without optional plotting dependencies.

| Capability | Owner | Boundary |
| --- | --- | --- |
| Workflow planning | `ccf-pipeline-orchestrator` | Coordinates stages; does not write, search, review, or rebut. |
| Literature monitoring | `ccf-literature-monitor` | Tracks recent papers, venue feeds, labs, and competitors; deep retrieval stays with literature search. |
| Compression and presentations | `ccf-paper-writer` | Changes manuscript-derived text; does not judge acceptance risk. |
| Exemplar extraction | `ccf-paper-to-exemplar` | Converts PDFs into writing pattern cards; does not draft or review manuscripts. |
| Writing review | `ccf-paper-reviewer` | Diagnoses writing and format-facing risk; does not rewrite unless handed back to writer. |
| Environment design | `ccf-env-design` | Owns the paper scenario and formal optimization problem; does not validate environment code or design the algorithm. |
| Environment implementation gate | `ccf-env-code-auditor` | Establishes `environment-valid`; does not judge algorithm performance. |
| Algorithm design | `ccf-algorithm-designer` | Consumes a versioned environment contract; cannot rewrite environment semantics. |
| Algorithm implementation gate | `ccf-algorithm-code-auditor` | Establishes executable algorithm evidence and the `joint-ready` gate. |
| Failed-MVP repair | `ccf-experiment-debugger` | Routes one minimal change to one owner and closes all affected reruns; does not replace either auditor. |
| Conclusion/evidence audit | `ccf-integrity-auditor` | Checks supported conclusions, existing citations, numbers, and figures; broad discovery stays with literature search. |
| Result evidence and specs | `ccf-experiment-designer` | Uses real results; never invents numbers. |
| Publication figures/tables and plots | `ccf-visual-composer` | Owns visual contracts, bundled Python plotting recipes, palettes, panel/table layout, captions, manuscript integration, and render QA from supplied results. |
| Venue format and artifacts | `ccf-submission-checker` | Checks package readiness; content polishing stays with writer. |
| Resubmission adaptation | `ccf-rebuttal-writer` | Maintains response/ledger logic; manuscript edits route back to writer. |
| Docs SVGs | `ccf-skill-forger` | Repository maintenance only; research figures/tables stay with experiment designer and visual composer. |

![Review boundaries](../assets/ccfa-skills-review-boundaries.svg)

## Venue Branch

Venue-specific LaTeX and policy notes are reference material:

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

Use `ccf-paper-writer` for venue-aware manuscript text and page-budget-aware drafting. Use `ccf-submission-checker` for final page limits, anonymity, PDF metadata, camera-ready checks, and package readiness. If a from-scratch writing request names a venue, writer reads the venue guide and length budget first; if no venue is named or the guide is missing, writer falls back to the NeurIPS template. Underfilled full drafts stay with writer for expansion; overfilled drafts stay with writer for compression before final submission checks.

## Source Of Truth

`SKILL.md` is authoritative for runtime behavior. These files are public indexes and audit aids:

- [SKILLS_CATALOG.md](SKILLS_CATALOG.md)
- [NAMING_AND_MERGE_AUDIT.md](NAMING_AND_MERGE_AUDIT.md)
- `ccf-common/references/routing.md`
- `ccf-common/references/skill-trigger-registry.yaml`
- `ccf-common/references/artifact-contracts.md`
