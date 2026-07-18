# CCFA Skills Catalog

This catalog is the public trigger-conflict index for the current 21-skill CCFA family. The table below contains all 21 runtime owners. If this document conflicts with a skill's `SKILL.md`, `SKILL.md` is authoritative.

![Runtime catalog](../assets/ccfa-skills-catalog.svg)

## Runtime Skills

| Skill | Stage | Startup condition | 中文触发 | Included modes | Do not use for |
| --- | --- | --- | --- | --- | --- |
| `ccf-project-scaffolder` | Setup | Create project folders, copy/select templates, initialize `ccfa.yaml`. | 创建论文项目、复制模板、初始化 `ccfa.yaml`。 | scaffold | Research content generation. |
| `ccf-pipeline-orchestrator` | Planning | Plan workflow, decompose tasks, coordinate gates and handoffs. | 拆任务、排阶段、定 gate、决定下一个 owner。 | planning, status, gate | Writing, review, search, experiment design, rebuttal. |
| `ccf-idea-optimizer` | Idea | Explore, rescue, and turn rough directions into problem-gap-insight-method-evidence plans. | 优化粗 idea、具象化研究思路、找方向、救方向、形成 problem-gap-insight。 | exploratory idea shaping, rescue routes | Ranking multiple ideas as the main task. |
| `ccf-idea-reviewer` | Idea gate | Score, compare, rank, and triage early ideas only when judgment is explicit. | idea 评分、选题排名、严格锐评、明确要求判断创新性和取舍。 | idea scoring, stage-aware triage | Brainstorming, rescuing, or developing a single rough idea. |
| `ccf-literature-monitor` | Monitoring | Track recent arXiv/OpenReview/venue papers, labs, competitors, and novelty-threat signals. | 竞品监控、新论文追踪、最近有没有类似 idea、arXiv/会议动态。 | arxiv-watch, venue-watch, novelty-check, trend-scouting, competitor-tracking | Deep related-work search, citation audit, or final idea scoring. |
| `ccf-literature-searcher` | Evidence | Search and screen literature, prior art, datasets, benchmarks, and opportunity gaps. | 检索相关工作、prior art、数据集、benchmark、方向调研、open gap。 | search, screening, opportunity map | Auditing only already cited papers or acting as a final idea kill gate. |
| `ccf-env-design` | Environment design | Own the paper scenario, formal optimization problem, parameter applicability range, complete core-tradeoff MES anchor, and method-independent complexity ladder. | 设计并维护论文场景、正式优化问题、参数适用范围、包含核心 Tradeoff 的最小但完整 MES，接受后冻结锚点并管理复杂度阶梯。 | design, audit, repair, handoff-spec | Environment-code validation or algorithm design. |
| `ccf-env-code-auditor` | Environment implementation gate | Audit authority, anchor-MES/complexity-stage contract traceability, semantics, independent MES execution, optimization fidelity, and central-tradeoff evidence. | 核验权威版本、锚点 MES 与复杂度阶段、契约追踪、语义、独立 MES 执行、优化保真和中心权衡证据。 | static-trace, executable-audit, repair, acceptance-gate | Scenario design or algorithm performance. |
| `ccf-algorithm-designer` | Algorithm design | Define the formal target, analyze structure, select a family, derive the mechanism, specify the algorithm MVP against the frozen anchor, and plan stage verification. | 按正式目标、问题结构、算法族、机制、冻结锚点上的算法 MVP 和阶段验证计划顺序设计算法。 | design, mvp, repair, handoff-spec | Scenario redesign, code audit, or publication experiments. |
| `ccf-algorithm-code-auditor` | Algorithm implementation gate | Audit authority/contracts, design-to-code traceability, semantics, reference evidence, and independent algorithm-MVP behavior. | 核验算法权威版本、契约、公式到代码、语义、参照证据和 MVP 行为。 | static-trace, mvp-audit, repair, acceptance-gate | Initial algorithm selection or environment audit. |
| `ccf-experiment-designer` | Paper-range usage evidence | Use accepted anchor/complexity-stage methods to design experiments and build real-result tables/figures. | 基于已接受 anchor/复杂度阶段算法设计论文范围使用实验、baseline、metric、消融、结果表和真实结果图。 | experiment design, result templates, result figures/tables | Defining/repairing environment or algorithm semantics, auditing code, inventing results, or drawing CCFA docs diagrams. |
| `ccf-experiment-debugger` | Stage repair / failure coordination | Repair a failed accepted anchor/complexity-stage run with one owner, one delta, and closed reruns. | 修复已接受 anchor/复杂度阶段的失败运行，定位单一 owner，执行一次最小修改并闭合重跑。 | diagnose, design-validation-loop, owner isolation, minimal repair, rerun closure | Replacing auditors, designing initial methods, or planning paper-range experiments. |
| `ccf-visual-composer` | Visual evidence | Compose publication-grade figures/tables, Python plotting code, palettes, captions, panel maps, and manuscript layout integration from supplied results. | 图表排版、配色、多面板 figure、Python 绘图代码、创意数据分析图、表格版式、caption、正文嵌入、视觉 QA。 | visual-contract, figure-design, python-plotting, table-design, layout-integration, render-qa | Designing experiments, inventing results, writing manuscript prose as the main task, or final submission compliance. |
| `ccf-paper-to-exemplar` | Writing support | Convert paper PDFs into reusable writing exemplar cards for `ccf-paper-writer`. | 把论文 PDF 转成写作范例卡、建立个人 exemplar 库。 | exemplar extraction, style-pattern cards, custom exemplar registration | Writing papers or performing review. |
| `ccf-paper-writer` | Manuscript | Draft, revise, polish, compress, preserve source format during edits, create venue- and length-aware LaTeX manuscripts from ideas, and presentation-adapt paper text. | 写作、润色、压缩；保留原格式；只有 idea 时按目标会议 LaTeX 和篇幅预算起草；缺省回退 NeurIPS。 | draft, polish, compression, venue-aware LaTeX drafting, page-budget drafting, presentation | Full review, evidence audit, package check, rebuttal. |
| `ccf-paper-reviewer` | Review | Review manuscripts scientifically and stylistically. | 科学审稿、写作评审、格式风险、评分、AC/meta-review。 | scientific review, writing review, format-facing review | Rewriting manuscript text or drafting rebuttals. |
| `ccf-integrity-auditor` | Conclusion/evidence audit | Audit supported conclusions, numbers, figures/tables, citations, BibTeX, and context support. | 审计结论与证据边界、数字、图表、引用、BibTeX 和上下文支撑。 | conclusion audit, numeric audit, citation audit | Full scientific review or broad literature search. |
| `ccf-submission-checker` | Submission | Check venue rules, LaTeX/PDF package, anonymity, metadata, artifacts. | 查会议格式、模板页数、匿名、PDF metadata、artifact/reproducibility。 | venue format, package check, artifact | Polishing manuscript content. |
| `ccf-rebuttal-writer` | Post-review | Write rebuttals, response letters, revision ledgers, resubmission plans. | 写 rebuttal、response letter、revision ledger、保守重投计划。 | rebuttal, ledger, response letter, resubmission | Ordinary manuscript writing. |
| `ccf-common` | Governance | Maintain shared routing, source registry, privacy/evidence policy, artifact contracts. | 维护共享路由、source registry、隐私/证据策略、artifact 合约。 | governance | Ordinary research work. |
| `ccf-skill-forger` | Maintenance | Maintain skills, routing, docs, SVG diagrams, validation, and releases. | 维护 skills、路由、README、SVG、校验和 release。 | skill maintenance, docs/SVG maintenance | Research writing, review, or experiments. |

## Merged Entries

| Removed standalone skill | Current owner | Why |
| --- | --- | --- |
| `ccf-workflow-planner` | `ccf-pipeline-orchestrator` | Planning and orchestration are the same project-control layer. |
| `ccf-paper-compressor` | `ccf-paper-writer` | Compression changes manuscript text and must share writing safeguards. |
| `ccf-writing-reviewer` | `ccf-paper-reviewer` | Writing review is a review mode, not a separate runtime owner. |
| `ccf-citation-auditor` | `ccf-integrity-auditor` | Citation verification is evidence integrity. |
| `ccf-figure-table-builder` | `ccf-experiment-designer`, then `ccf-visual-composer` | Evidence/result content depends on real experiment values; publication visual composition, palette, caption placement, and render QA belong to visual composer. |
| `ccf-artifact-packager` | `ccf-submission-checker` | Artifact readiness is submission readiness. |
| `ccf-venue-format-guide` | `ccf-submission-checker` | Venue format lookup is a submission gate; writing still reads venue references. |
| `ccf-resubmission-adapter` | `ccf-rebuttal-writer` | Resubmission follows reviewer-response and revision-ledger logic. |
| `ccf-paper-presenter` | `ccf-paper-writer` | Slides/posters/talk scripts are paper-derived writing outputs. |
| `ccf-doc-diagram-designer` | `ccf-skill-forger` | Docs SVGs are repository maintenance. |

## Conflict Rules

![Routing boundaries](../assets/ccfa-skills-routing.svg)

- Non-review workflow skills should follow the user's requested output shape. Their internal checklists are safeguards, not mandatory visible report templates.
- Review, audit, and submission-gate skills may remain structured because their job is traceable diagnosis and pass/fail risk control.
- Full-workflow and full-paper prompts should produce dense artifacts, not route summaries. A manuscript request should leave a manuscript; a closed-loop request should leave idea review, writing draft, review, audit, rebuttal, and submission-check artifacts.
- Idea exploration, rescue, and shaping go to `ccf-idea-optimizer`; explicit scoring/ranking goes to `ccf-idea-reviewer`.
- Recent-paper watching, competitor tracking, and "is there a new similar idea?" go to `ccf-literature-monitor`; deep related-work discovery and opportunity mapping go to `ccf-literature-searcher`; existing citation verification goes to `ccf-integrity-auditor`.
- In early research, a weak or crowded direction should produce rescue routes, narrowing options, and evidence-to-decide before `abandon` is used.
- Manuscript rewriting, compression, and presentation outputs go to `ccf-paper-writer`; judgment goes to `ccf-paper-reviewer`.
- PDF-to-exemplar conversion goes to `ccf-paper-to-exemplar`; actual manuscript drafting still goes to `ccf-paper-writer`.
- From-scratch submission manuscripts must be length-aware: underfilled drafts stay with `ccf-paper-writer` for expansion; overfilled drafts stay with `ccf-paper-writer` for compression; final page compliance goes to `ccf-submission-checker`.
- Real result/evidence structure goes to `ccf-experiment-designer`; publication-grade figure/table composition, Python plot recipes, palette, caption placement, and render QA go to `ccf-visual-composer`; docs diagrams go to `ccf-skill-forger`.
- Communication formulation and complete core-tradeoff MES design go to `ccf-env-design`; freeze the accepted MES as anchor and expand complexity stages there. Environment implementation evidence goes to `ccf-env-code-auditor`; formal algorithm design goes to `ccf-algorithm-designer`; algorithm implementation evidence goes to `ccf-algorithm-code-auditor`; failed stage repair coordination goes to `ccf-experiment-debugger`.
- The ordered design-validation loop is `ccf-env-design` -> `ccf-env-code-auditor` -> `ccf-algorithm-designer` -> `ccf-algorithm-code-auditor` -> complexity ladder -> `ccf-experiment-debugger` on failure. A complexity-stage failure preserves the anchor and routes to algorithm repair. Only an accepted formal amendment creates a new problem/MES version and invalidates every dependent algorithm, baseline, and result artifact.
- Repository checkpoints reuse the installed `$code-review` skill against a fixed comparison point and accepted specification. CCFA does not duplicate or redefine its Standards/Spec protocol.
- Venue requirements, package checks, anonymity, and artifact readiness go to `ccf-submission-checker`.
- Reviewer responses, revision ledgers, and resubmission plans go to `ccf-rebuttal-writer`.

## Venue Guides

The legacy per-venue runtime layer remains reference-only:

- `ccf-paper-writer/references/venue-guides/index.md`
- `ccf-paper-writer/references/venue-guides/<venue>.md`

Use `ccf-paper-writer` for venue-aware manuscript text and `ccf-submission-checker` for venue/package compliance.
