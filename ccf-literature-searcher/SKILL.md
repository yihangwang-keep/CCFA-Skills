---
name: ccf-literature-searcher
description: "Search and screen literature, related work, prior art, domain evidence, problem formulations, objectives, constraints, baselines, simulation settings, datasets, citation evidence, and research opportunity maps for CCF workflows. Use for literature search, related work, prior art, formulation search, communication/networking formulation evidence, objective/constraint search, baseline search, direction scouting, 文献检索, 相关工作, 通信问题建模依据, 目标函数依据, 约束依据, baseline依据, 方向调研. Do not audit only already-cited references or write the manuscript as the main task."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Literature Searcher

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep literature search separate from idea optimization, manuscript writing, experiment design, paper review, and rebuttal.

Load `../ccf-common/references/task-modes.md` before deciding exploratory, quick, or standard mode. Use exploratory mode for early direction scouting, "看看还有没有机会", "这个方向是不是被做完了", or literature search meant to feed idea optimization rather than a final novelty verdict. Use quick mode for a narrow related-work scan or a small set of candidate citations. Use standard mode for Related Work, Introduction, mature idea novelty grounding, experiment design, or any task that will feed another CCFA module.

If the user asks for recurring watch, latest-paper monitoring, competitor tracking, "recently any similar idea", arXiv/OpenReview feed scans, or lab/project tracking, route to `ccf-literature-monitor` by the shared handoff mode. Use this skill for deep retrieval, closest-work clustering, related-work structure, and citation candidates.

Treat user ideas, draft text, unpublished results, and private manuscripts as private material. Load `../ccf-common/references/privacy-and-evidence.md` before browsing. Search with public keywords, public titles, venue names, method names, public abstracts, or user-approved query text. Do not paste private draft sentences into a search query unless the user explicitly authorizes it.

Source-quality exclusion: do not search, cite, recommend, or include policy-excluded venues, journals, URLs, or PDFs. The shared policy includes MDPI sources in this exclusion set; record exclusions only in internal screening or the search-notes file.

## Core Rule

Ground novelty and positioning using high-quality, inspectable sources. Prefer influential conferences, strong journals, official proceedings pages, archival repositories, and public paper pages. Do not invent papers, citations, venues, links, acceptance status, or numerical results. Separate searched evidence from inference. Literature search is not a kill gate: the presence of related work should produce differentiation options, open gaps, field-appropriate evidence choices, and caution labels before any "direction is covered" conclusion. For communication, networking, and optimization work, organize findings around problem formulations, objective functions, decision variables, constraints, channel or mobility assumptions, tractability arguments, classical baselines, oracle/bound references, and simulation parameter regimes. Follow the user's requested output shape: short list, related-work clusters, opportunity map, BibTeX candidates, search folder, or handoff summary.

## Mandatory Search Checklist

In standard mode, complete this checklist before final output. In quick mode, run the relevant subset and return a compact checklist status.

1. The user's topic is converted into safe public search queries.
2. For each included method paper, state the problem scenario it addresses and the algorithm it uses.
3. Shared source-quality exclusions are applied to search domains, candidates, and final outputs.
4. Sources prioritize primary or high-confidence venues: official proceedings, arXiv/OpenReview when appropriate, ACL Anthology, CVF, PMLR, ACM, IEEE, USENIX, DBLP, Semantic Scholar, OpenAlex, Crossref, and venue or project pages.
5. Candidate papers are deduplicated by title and linked to a stable URL.
6. Each included paper has venue/year/source status, paper type, and relevance rationale.
7. Paper quality is scored on insight, completeness, and experimental numeric evidence. Pure evaluation-artifact papers skip the numeric-results score and receive a quality note for the artifact they introduce.
8. Paper type is one of `pure evaluation artifact`, `pure method`, `method + evaluation artifact`, `survey`, `system/tool`, `theory/proof`, or `other`.
9. Every claim about a paper is traceable to the linked source or marked as inferred.
10. For idea-stage searches, each closest-work cluster includes what is already covered, what remains under-tested, and at least one possible differentiation or rescue route.
11. A literature-search folder is written when file access is available and the user asked for a reusable report or standard workflow.
12. Optional handoff to `ccf-literature-monitor`, `ccf-paper-writer`, `ccf-idea-optimizer`, `ccf-idea-reviewer`, `ccf-experiment-designer`, or `ccf-paper-reviewer` follows CCFA handoff mode.

## Workflow

1. Identify the search purpose: Related Work, Introduction support, novelty check, direction scouting, idea optimization, idea review, experiment design, dataset discovery, communication formulation grounding, objective/constraint grounding, baseline grounding, or reviewer-risk diagnosis.
2. Create public queries from the user's topic. If the topic is too private or underspecified, ask only for non-sensitive keywords or infer broad keywords with lower confidence.
3. Load `references/search-and-scoring.md`. Search breadth depends on mode:
   - Exploratory: 10-20 screened candidates, 5-10 final papers or clusters, plus opportunity gaps.
   - Quick: 6-10 screened candidates, 3-6 final papers.
   - Standard: 15-30 screened candidates, 8-15 final papers unless the user requests another size.
4. Search discovery indexes first, then verify candidates through stable paper pages or official proceedings when possible. Use broad web search only to find primary links; do not rely on snippets for final claims.
5. Filter by influence and fit. Prefer CCF-A/B conferences, top-field conferences, strong journals, widely used baselines, or recent high-signal preprints from credible groups. Exclude low-quality, predatory, inaccessible, or policy-excluded sources. For exploratory searches, include one or two "near miss" or negative-signal clusters if they reveal an open gap, failed assumption, outdated evaluation setting, missing user group, or neglected system constraint.
6. Classify each paper with the paper-type taxonomy and score it:
   - `insight`: how clear and non-obvious the central idea is.
   - `completeness`: method/evaluation/proof/formulation/dataset/reproducibility coverage.
   - `experimental numeric evidence`: strength and relevance of reported numerical evidence.
7. Write the search folder using `references/report-template.md`. Default folder name:

```text
literature-search-YYYYMMDD-<topic-slug>/
  papers.md
  papers.csv
  search-notes.md
```

8. If the search feeds another module, provide a handoff summary:
   - For writing: closest-work groups, novelty gaps, citation cautions.
   - For idea optimization: stale/overcrowded directions, open gaps, timely pivots, and minimum viable research questions.
   - For idea review: novelty confidence and likely prior-art risks.
   - For literature monitoring: watch queries, tracked competitors, and recurring overlap signals.
   - For experiment environment design: task scenarios, objective functions, communication models, constraints, decision variables, baseline families, tractability notes, and unresolved realism questions for `ccf-experiment-env-design`.
   - For experiment design: problem scenarios, algorithms, datasets or simulation settings, baselines, metrics, and formulation requirements.
   - For paper review: missing related work and baseline risks.

## Adaptive Output Contracts

Return the requested artifact first. If the user asks for a list of papers, output the list/table directly. If they ask for Related Work material, output clusters and positioning notes. If they ask for a folder, write the folder and summarize it. Use the following defaults for standard or quick search reports.

For standard search, return:

```text
Search purpose:
Queries used:
Source policy:
Folder written:
Top paper table:
Excluded source notes:
Closest-work clusters:
Opportunity map:
Quality-score rationale:
Evidence object candidates:
Novelty and positioning risks:
Recommended next module:
Checklist status:
```

For quick search, return:

```text
Quick search scope:
Top candidates:
High-risk missing literature:
Opportunity hint:
Folder written:
Compact checklist status:
```

## Reference Files

Load only what is needed:

- `references/search-and-scoring.md`: Use for source policy, source-quality exclusions, source tiers, paper-type taxonomy, and scoring anchors.
- `references/report-template.md`: Use when writing the literature-search folder files.
