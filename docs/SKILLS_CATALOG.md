# CCFA Skills Catalog

This catalog is the public trigger-conflict index for the current CCFA family. If this document conflicts with a skill's `SKILL.md`, `SKILL.md` is authoritative.

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
| `ccf-env-design` | Environment design | Design background, causal problem, scientific question, formal model, active coupling, complexity balance, paper-to-MVP relation, and algorithm information contract in order. | 按背景、因果问题、科学问题、数学模型、耦合复杂度、MVP 和信息接口顺序设计场景。 | design, audit, repair, handoff-spec | Environment-code validation or algorithm design. |
| `ccf-env-code-auditor` | Environment implementation gate | Audit authority, design contract, traceability, semantics, independent MVP execution, optimization fidelity, and tradeoff evidence in order. | 按权威版本、设计契约、静态追踪、语义、独立执行、优化保真和 tradeoff 顺序审查环境。 | static-trace, executable-audit, repair, acceptance-gate | Scenario design or algorithm performance. |
| `ccf-algorithm-designer` | Algorithm design | Define the formal target, analyze structure, select a family, derive the mechanism, specify the algorithm MVP, and plan verification. | 按正式目标、问题结构、算法族、机制、算法 MVP 和验证计划顺序设计算法。 | design, mvp, repair, handoff-spec | Scenario redesign, code audit, or publication experiments. |
| `ccf-algorithm-code-auditor` | Algorithm implementation gate | Audit authority/contracts, design-to-code traceability, semantics, reference evidence, and independent algorithm-MVP behavior. | 核验算法权威版本、契约、公式到代码、语义、参照证据和 MVP 行为。 | static-trace, mvp-audit, repair, acceptance-gate | Initial algorithm selection or environment audit. |
| `ccf-experiment-designer` | Evidence | Design experiments and build real-result tables/figures. | 设计实验、baseline、metric、消融、结果表和真实结果图。 | experiment design, result templates, result figures/tables | Inventing results or drawing CCFA docs diagrams. |
| `ccf-experiment-debugger` | Failure coordination | Refresh environment/algorithm auditor evidence, isolate the owner, route one minimal change, and close affected reruns. | 围绕两个 auditor 定位失败 owner、执行最小修改并闭环复审。 | auditor refresh, owner isolation, minimal repair, rerun closure | Replacing auditors or initial design. |
| `ccf-visual-composer` | Visual evidence | Compose publication-grade figures/tables, Python plotting code, palettes, captions, panel maps, and manuscript layout integration from supplied results. | 图表排版、配色、多面板 figure、Python 绘图代码、创意数据分析图、表格版式、caption、正文嵌入、视觉 QA。 | visual-contract, figure-design, python-plotting, table-design, layout-integration, render-qa | Designing experiments, inventing results, writing manuscript prose as the main task, or final submission compliance. |
| `ccf-paper-to-exemplar` | Writing support | Convert paper PDFs into reusable writing exemplar cards for `ccf-paper-writer`. | 把论文 PDF 转成写作范例卡、建立个人 exemplar 库。 | exemplar extraction, style-pattern cards, custom exemplar registration | Writing papers or performing review. |
| `ccf-paper-writer` | Manuscript | Draft, revise, polish, compress, preserve source format during edits, create venue- and length-aware LaTeX manuscripts from ideas, and presentation-adapt paper text. | 写作、润色、压缩；保留原格式；只有 idea 时按目标会议 LaTeX 和篇幅预算起草；缺省回退 NeurIPS。 | draft, polish, compression, venue-aware LaTeX drafting, page-budget drafting, presentation | Full review, evidence audit, package check, rebuttal. |
| `ccf-paper-reviewer` | Review | Review manuscripts scientifically and stylistically. | 科学审稿、写作评审、格式风险、评分、AC/meta-review。 | scientific review, writing review, format-facing review | Rewriting manuscript text or drafting rebuttals. |
| `ccf-integrity-auditor` | Audit | Audit claims, numbers, figures/tables, citations, and BibTeX. | 审计 claim、数字、图表、引用、BibTeX 和上下文支撑。 | claim audit, numeric audit, citation audit | Full scientific review or broad literature search. |
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
- Communication formulation and MVP design go to `ccf-env-design`; environment implementation evidence goes to `ccf-env-code-auditor`; formal algorithm design goes to `ccf-algorithm-designer`; algorithm implementation evidence goes to `ccf-algorithm-code-auditor`; failed MVP repair coordination goes to `ccf-experiment-debugger`.
- Venue requirements, package checks, anonymity, and artifact readiness go to `ccf-submission-checker`.
- Reviewer responses, revision ledgers, and resubmission plans go to `ccf-rebuttal-writer`.

## Venue Guides

The legacy per-venue runtime layer remains reference-only:

- `ccf-paper-writer/references/venue-guides/index.md`
- `ccf-paper-writer/references/venue-guides/<venue>.md`

Use `ccf-paper-writer` for venue-aware manuscript text and `ccf-submission-checker` for venue/package compliance.
