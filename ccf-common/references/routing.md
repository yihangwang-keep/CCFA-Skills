# CCFA Routing

Route by the user's primary intent. Do not activate every downstream skill just because it may become useful later.

The runtime surface has 21 installable `ccf-*` skills, including 19 research-workflow owners and two governance skills, plus the LaTeX/template reference tree. Removed helper names must not be installed as standalone skills.

## Canonical Runtime Skills

| Intent | Owning skill | Included modes | Boundary |
| --- | --- | --- | --- |
| Create project folders, copy/select templates, initialize `ccfa.yaml`. | `ccf-project-scaffolder` | scaffold | Does not create research content. |
| Plan workflow, decompose tasks, coordinate stages/gates/handoffs. | `ccf-pipeline-orchestrator` | planning, status, gate | Does not perform downstream research work. |
| Explore, rescue, or turn a rough direction into a problem-gap-insight-method-evidence plan. | `ccf-idea-optimizer` | exploratory idea shaping, rescue routes | Does not rank multiple ideas as the main task. |
| Score, compare, rank, and triage early ideas when the user explicitly asks for judgment. | `ccf-idea-reviewer` | idea scoring, stage-aware triage | Does not brainstorm directions or optimize a single idea as the main task. |
| Monitor recent papers, arXiv/OpenReview/venue feeds, labs, competitors, and recurring novelty threats. | `ccf-literature-monitor` | arxiv-watch, venue-watch, novelty-check, trend-scouting, competitor-tracking | Does not replace deep related-work search, citation audit, or final idea scoring. |
| Search literature, prior art, formulations, objectives, constraints, baselines, simulation settings, datasets, citation evidence, and opportunity gaps. | `ccf-literature-searcher` | search, screening, opportunity map | Does not audit only already cited papers or act as a final idea kill gate. |
| Design or audit a non-toy communication/networking paper scenario and derive its minimum viable version (MVP). | `ccf-env-design` | objective/constraint design, scenario abstraction, complexity balance, paper-to-MVP derivation, handoff spec | Does not design algorithms, result tables, or invent results. |
| Audit the paper scenario, its MVP, and environment code with one consistent plan-to-execution protocol. | `ccf-env-code-auditor` | plan gate, static trace, complete-MVP execution, tunable-rule gate, repair | Does not judge algorithm suitability, convergence, or performance. |
| Design the formal algorithm MVP and its stepwise verification targets for an accepted scenario MVP. | `ccf-algorithm-designer` | algorithm selection, derivation, MVP, repair | Does not redesign the scenario, audit code, or design publication experiments. |
| Audit algorithm-MVP code, feasibility, correctness/convergence, and exact/oracle/bound evidence. | `ccf-algorithm-code-auditor` | equation-to-code trace, reference checks, MVP acceptance, repair | Does not choose the initial algorithm or redesign the environment. |
| Turn validated MVP evidence into experiments and real-result tables/figures for the paper's claimed scope. | `ccf-experiment-designer` | experiment design, scenario coverage, result templates, result figures/tables | Does not invent results or own primary scenario/algorithm design. |
| Coordinate failed environment or algorithm MVP repair from auditor evidence and route the smallest owned change. | `ccf-experiment-debugger` | auditor refresh, owner isolation, minimal repair, rerun closure | Does not replace either auditor or design the initial experiment. |
| Compose publication-grade figures/tables, Python plotting code, palettes, captions, panel maps, and manuscript visual layout integration from supplied results. | `ccf-visual-composer` | visual-contract, figure-design, python-plotting, table-design, layout-integration, render-qa | Does not design experiments, invent results, write manuscript prose, or perform final submission compliance. |
| Draft, revise, polish, compress, and presentation-adapt paper text. | `ccf-paper-writer` | writing, polishing, compression, venue-aware LaTeX drafting, slides/poster/talk/Q&A | Preserves user format for edits; does not run full review or rebuttal. |
| Convert user-provided paper PDFs into reusable writing exemplar cards. | `ccf-paper-to-exemplar` | exemplar extraction, writing-pattern cards, custom exemplar registration | Does not write papers or perform review. |
| Review manuscripts scientifically and stylistically. | `ccf-paper-reviewer` | scientific review, writing review, format-facing review, AC/meta-review | Does not rewrite or rebut. |
| Audit evidence integrity, numbers, figures/tables, and existing citations. | `ccf-integrity-auditor` | claim audit, numeric audit, citation audit | Does not replace review or broad literature search. |
| Check venue rules, LaTeX/PDF package, anonymity, metadata, and artifacts. | `ccf-submission-checker` | venue format, package check, artifact/reproducibility | Does not polish content. |
| Write rebuttals, revision ledgers, response letters, and resubmission plans. | `ccf-rebuttal-writer` | rebuttal, revision ledger, response letter, resubmission | Does not trigger for ordinary writing. |
| Shared routing, source registry, privacy/evidence, artifact contracts. | `ccf-common` | governance | Not an ordinary research task skill. |
| Maintain skills, docs, SVG diagrams, routing, validation, and releases. | `ccf-skill-forger` | skill maintenance, docs/SVG maintenance, release validation | Does not do research writing or review. |

## Default Paper Project Flow

```text
ccf-project-scaffolder
  -> ccf-pipeline-orchestrator
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-literature-monitor
  -> ccf-literature-searcher
  -> ccf-env-design (paper scenario + scenario MVP)
  -> ccf-env-code-auditor (scenario-MVP acceptance; rerun after environment changes)
  -> ccf-algorithm-designer (formal algorithm + algorithm MVP)
  -> ccf-algorithm-code-auditor (algorithm-MVP acceptance)
  -> ccf-experiment-debugger (conditional failure routing and repair)
  -> ccf-experiment-designer (paper-scope evidence)
  -> ccf-visual-composer
  -> ccf-paper-to-exemplar (optional style-reference sidecar)
  -> ccf-paper-writer
  -> ccf-paper-reviewer
  -> ccf-integrity-auditor
  -> ccf-submission-checker
  -> ccf-rebuttal-writer

Governance: ccf-common / ccf-skill-forger
```

## Merged Capability Map

| Old standalone entry | Current owner | Reason |
| --- | --- | --- |
| `ccf-workflow-planner` | `ccf-pipeline-orchestrator` | Planning and stage routing are one project-control responsibility. |
| `ccf-paper-compressor` | `ccf-paper-writer` | Compression changes manuscript text and must preserve writing scope. |
| `ccf-writing-reviewer` | `ccf-paper-reviewer` | Writing review and scientific review are review modes over the same manuscript. |
| `ccf-citation-auditor` | `ccf-integrity-auditor` | Citation verification is evidence integrity, not broad literature search. |
| `ccf-figure-table-builder` | `ccf-experiment-designer`, then `ccf-visual-composer` | Experiment designer owns evidence design and real result values; visual composer owns publication layout, palette, captions, and render QA. |
| `ccf-artifact-packager` | `ccf-submission-checker` | Artifact readiness is part of submission package readiness. |
| `ccf-venue-format-guide` | `ccf-submission-checker` | Venue format lookup is a submission/package gate; paper writing still reads venue references. |
| `ccf-resubmission-adapter` | `ccf-rebuttal-writer` | Resubmission follows review-response and revision-ledger ownership. |
| `ccf-paper-presenter` | `ccf-paper-writer` | Talks, posters, and Q&A are paper-derived writing outputs. |
| `ccf-doc-diagram-designer` | `ccf-skill-forger` | Documentation SVGs are repository maintenance, not research workflow. |

## Venue Layer Rule

Venue knowledge is reference material, not venue-specific runtime skills. Use:

- `ccf-paper-writer/references/venue-guides/index.md`
- `ccf-paper-writer/references/venue-guides/<venue>.md`
- `ccf-submission-checker` for venue format, template, page-limit, anonymity, and package questions

For manuscript writing from only an idea, `ccf-paper-writer` checks the venue guide first and drafts in that venue's LaTeX style. If no target venue guide exists or no venue is named, it uses the NeurIPS guide/template as the fallback and leaves final policy freshness to `ccf-submission-checker`.

## Smoke Prompts

| Prompt | Expected route |
| --- | --- |
| 先帮我把论文项目流程和下一步拆清楚 | `ccf-pipeline-orchestrator` |
| 优化一个 NeurIPS idea / 找几个可做方向 / 这个方向还能怎么救 | `ccf-idea-optimizer` |
| 给三个 idea 评分排名 / 明确让我严格取舍 | `ccf-idea-reviewer` |
| 监控竞品 / 追踪新论文 / 最近有没有类似 idea | `ccf-literature-monitor` |
| 搜索 related work、目标函数、约束、baseline、建模依据和 open gap | `ccf-literature-searcher` |
| 设计通信优化目标函数和约束 / 判断任务通信问题是不是玩具 / 做 env-design | `ccf-env-design` |
| 先审查场景问题和计划，再检查完整代码实现是否迫使启发式在 tradeoff 两侧之间取舍 | `ccf-env-code-auditor` |
| 从论文场景形成 MVP，并设计正式算法 MVP 与逐步验证目标 | `ccf-algorithm-designer` |
| 核验算法 MVP 的公式到代码、可行性、oracle/bound 和端到端结果 | `ccf-algorithm-code-auditor` |
| 设计对比实验、消融和结果表 | `ccf-experiment-designer` |
| 环境或算法 MVP 失败，根据 auditor 证据定位 owner、做最小修改并闭环复审 | `ccf-experiment-debugger` |
| 根据真实结果规划论文图表的数据和证据结构 | `ccf-experiment-designer` |
| 优化图表排版 / 选择论文配色 / 多面板 figure 放正文里 | `ccf-visual-composer` |
| 用 Python 画漂亮数据分析图 / 创造有趣但可信的论文图 | `ccf-visual-composer` |
| 把这篇 PDF 做成写作范例 / 添加 exemplar | `ccf-paper-to-exemplar` |
| 润色 introduction 或压缩到页数限制 | `ccf-paper-writer` |
| 把论文做成 slides 和 Q&A | `ccf-paper-writer` |
| 完整审稿、逐段写作评审或 LaTeX 表达检查 | `ccf-paper-reviewer` |
| 检查 claim、数字、引用是否一致且有支撑 | `ccf-integrity-auditor` |
| NeurIPS page limit / template / anonymity / artifact checklist | `ccf-submission-checker` |
| 根据 R1/R2 写 rebuttal 并维护修改表 | `ccf-rebuttal-writer` |
| 迁移到 ICLR 但不新增实验 | `ccf-rebuttal-writer` |
| 维护 CCFA skill、README、SVG 或 release | `ccf-skill-forger` |
