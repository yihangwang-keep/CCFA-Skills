# CCFA Artifact Contracts

These contracts prevent CCFA skills from overwriting each other's work. Read broadly, write narrowly.

| Artifact | Primary owner | Contract |
| --- | --- | --- |
| `ccfa.yaml` | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator` | Scaffold creates it; orchestrator updates stage/gate state. Other skills may read and propose updates. |
| `literature-monitor/*.md`, `output/literature-monitor/*` | `ccf-literature-monitor` | Stores dated monitoring reports, overlap flags, and watch summaries. Literature searcher may deep-retrieve flagged papers; reviewer/optimizer may use the flags for score or rescue decisions. |
| `manuscript/*.tex` | `ccf-paper-writer` | Review and audit skills suggest edits; writing changes route back to paper writer unless user explicitly authorizes otherwise. |
| `references/*.bib` | `ccf-integrity-auditor` | Integrity auditor verifies existing entries; literature searcher proposes new candidates. |
| `experiments/results.*` | user, `ccf-experiment-designer` | Figure/table and integrity skills read supplied numbers only. |
| `environment-design/*.md`, `environment-design/*.yaml` | `ccf-env-design` | Stores the paper scenario, formal optimization problem, parameter applicability range, frozen anchor MES, complexity-ladder contract, information pattern, feasibility meaning, supported conclusion range, and accepted environment amendments. Accepted versions are append-only evidence. |
| `environment-design/complexity-ladder/*` | `ccf-env-design` | Stores anchor-linked stage IDs, method-independent complexity deltas, parent stage relations, anchor regression requirements, failure ownership, stage evidence, and invalidation/rerun records. The debugger links its failure ledger from `experiment-debug/`; this artifact never stores a replacement MES for ordinary complexity expansion. |
| `environment-design/scenario-evolution/*` | `ccf-env-design` | Stores method-independent complexity-stage proposals, exceptional formal amendments, legacy change classifications, invalidation impact, decisions, and required reruns. Complexity expansion keeps the anchor MES; it does not create an MES successor. |
| `environment-audit/*.md` | `ccf-env-code-auditor` | Stores authority/design-contract status, anchor-only L2 heuristic-probe evidence, complexity-stage L1 consistency and anchor-regression evidence, model-to-code traceability, semantics, independent MES evidence, optimization/tradeoff findings, artifact manifests, CCFA-native two-axis implementation-review reports, minimal repairs, and verdicts. It preserves the authoritative design and pre-audit evidence. |
| `algorithm-design/*.md`, `algorithm-design/*.yaml` | `ccf-algorithm-designer` | Stores the algorithm family decision, derivation, assumptions, MVP, verification targets, guarantee/reference target, interface requests, and revision record. |
| `algorithm-audit/*.md` | `ccf-algorithm-code-auditor` | Stores equation-to-code traceability, semantic/feasibility/reference evidence, method-role and no-heuristic findings, algorithm-MVP acceptance, artifact manifests, CCFA-native two-axis implementation-review reports, repairs, and verdicts. |
| `experiment-debug/*.md`, `experiment-debug/*/` | `ccf-experiment-debugger` | Stores fixed design-validation contracts, anchor-MES/complexity-stage failure signatures, loop ledgers, route-specific algorithm-repair exhaustion, environment-review decisions, non-simplification evidence, artifact-set identities, auditor/native-review evidence, evolution requests, invalidated gates, terminal status, and rerun closure. It repairs and coordinates accepted stage runs; it does not own initial design or paper-range experiment plans. It preserves original failed results. |
| `figures/*`, `tables/*` | `ccf-experiment-designer`, `ccf-visual-composer` | Experiment designer owns paper-range usage evidence, evidence/result content, and real values from accepted anchor/stage methods; visual composer owns plotting code, palette, panel/table layout, caption placement, manuscript integration, and render QA. Data must be real. Neither designs or repairs environment/algorithm semantics. |
| `visual-composer/*` | `ccf-visual-composer` | Stores visual contracts, Python plotting scripts, generated figures, panel/table maps, palette decisions, render QA ledgers, and visual iteration logs. It must not become a hidden source of invented numbers. |
| `reviews/*` | `ccf-paper-reviewer`, user | Rebuttal writer reads real reviews and maintains response ledger. |
| `reviews/revision-ledger.md` | `ccf-rebuttal-writer` | Tracks reviewer comment -> response promise -> manuscript action -> status. |
| `submission/*` | `ccf-submission-checker` | Stores build, anonymity, page, metadata, and policy readiness results. |
| `artifact/*` | `ccf-submission-checker` | Tracks code/data/model release and reproducibility package status. |
| `talk/*` | `ccf-paper-writer` | Presentation outputs only; not submission evidence. |
| `assets/ccfa-skills-*.svg` | `ccf-skill-forger` | Generated by `tools/build_ccfa_diagrams.py`; must pass browser screenshot QA, not only XML parsing. |
| governance docs | `ccf-common`, `ccf-skill-forger` | Routing, naming, trigger registry, source registry, validation, and policy documents. |
