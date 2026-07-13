# Literature Search And Scoring

Use this file for source selection, source-quality exclusions, paper classification, and quality scoring.

## Source Tiers

Preferred primary sources:

- Official proceedings or publisher pages: ACL Anthology, CVF Open Access, PMLR, ACM Digital Library, IEEE Xplore, USENIX, VLDB, OpenReview, AAAI/OJS, SIAM, Springer/LIPIcs when venue-appropriate.
- Stable paper records: arXiv, DBLP, Semantic Scholar, OpenAlex, Crossref, DOI landing pages, project pages, dataset pages, simulator docs, and standard/specification pages when relevant.
- Strong journals and transactions when the field is journal-centered: JMLR, TPAMI, TOG, TKDE, TDSC, TOSEM, TSE, TODS, CACM, IEEE/ACM Transactions, IEEE JSAC, IEEE TCOM, IEEE TWC, IEEE TMC, IEEE/ACM ToN, Nature/Science family only when relevant.

Discovery sources are allowed for finding candidates, but final claims should point to a stable paper page or proceedings page whenever possible.

## Hard Exclusions

Exclude:

- MDPI domains, journals, proceedings, PDFs, and special issues.
- Predatory or low-signal venues with no clear review standard.
- Untraceable PDFs without title, authors, venue, or stable link.
- Papers whose only accessible evidence is a search snippet.

If an excluded paper appears important because the user specifically named it, report that it is excluded by policy and ask whether they want a separate user-directed note. Do not include it in the scored candidate table.

## Search Strategy

Use several query forms:

```text
"<task>" "<method>" evaluation setting
"<task>" "<closest baseline>" "dataset"
"<problem phrase>" site:openaccess.thecvf.com OR site:proceedings.mlr.press
"<method phrase>" OpenReview NeurIPS ICLR ICML
"<topic>" DBLP SIGMOD SIGCOMM SOSP CCS CHI PLDI STOC
"<communication task>" objective function constraints optimization formulation
"<wireless optimization problem>" IEEE INFOCOM ICC GLOBECOM WCNC TWC TCOM JSAC
"<UAV communication>" trajectory resource allocation task mission latency reliability
```

Prefer a mix of:

- recent papers from the last 2-4 years,
- one or two older anchor papers,
- closest baselines,
- dataset/evaluation-artifact papers,
- survey or taxonomy papers only when they clarify a field boundary.

For each included method paper, record the problem scenario it addresses and the algorithm it uses. Heuristic methods may be recorded only as prior art or baselines, not as proposed-algorithm candidates.

## Opportunity Mapping

When the search is for early direction scouting, classify each cluster as one or more of:

- `crowded but open`: many papers exist, but a measurable failure mode, setting, or assumption remains weak.
- `covered central claim`: the same problem, mechanism, and evidence path are already present; the idea needs a new angle.
- `evaluation-setting gap`: the field lacks a dataset, metric, stress test, simulator, channel/mobility model, evaluation standard, or accepted formulation reference.
- `mechanism gap`: papers report performance but do not explain why the method works or fails.
- `deployment/system gap`: real constraints, cost, latency, robustness, privacy, security, or user workflow are under-tested.
- `theory/analysis gap`: empirical results exist but formal understanding, bounds, or diagnostics are missing.
- `negative-result opportunity`: common assumptions fail, and a careful diagnostic or falsification paper may be valuable.

For every `covered central claim`, still report the best possible rescue route:

```text
What is covered:
Why direct novelty is weak:
Possible rescue route: new problem / new mechanism / new evidence / new venue / stop
Evidence needed to decide:
```

Do not conclude "the direction is dead" merely because the topic is popular. A direction is likely dead only when the user's central problem, mechanism, target setting, and evidence path are all already covered and no credible reframing remains.

## Paper-Type Taxonomy

Classify each included paper:

- `pure evaluation artifact`: primary contribution is dataset, simulator, scenario generator, evaluation suite, or standard formulation.
- `pure method`: primary contribution is method, algorithm, model, system design, proof, or analysis.
- `method + evaluation artifact`: introduces a method and a new dataset, simulator, standard formulation, or scenario generator that both matter.
- `survey`: synthesizes prior work.
- `system/tool`: primary contribution is implementation, infrastructure, deployment, or usable tool.
- `theory/proof`: primary contribution is theorem, bound, proof technique, or formal model.
- `other`: use only with a short explanation.

## Scoring

Use 1-5 anchors unless the user asks for another scale.

Score paper quality separately from idea viability. A high-quality close paper may reduce direct novelty while also revealing a better problem boundary, objective, constraint set, baseline, evaluation setting, or unresolved assumption. A low-quality paper should not be used as strong evidence that a direction is solved.

Insight:

- 5: clear, non-obvious insight that changes how the problem is understood.
- 4: strong idea with a specific mechanism or framing.
- 3: useful but incremental insight.
- 2: mostly engineering assembly or standard framing.
- 1: unclear or weak insight.

Completeness:

- 5: method/formulation/proof, evaluation, limitations, reproducibility, and positioning are all well covered.
- 4: strong coverage with minor missing details.
- 3: adequate but with visible gaps.
- 2: partial; important design or evidence details missing.
- 1: incomplete or hard to audit.

Experimental numeric evidence:

- 5: strong, fair, multi-setting numerical evidence with appropriate baselines and analysis.
- 4: solid numerical evidence with minor weaknesses.
- 3: adequate numbers but limited settings, baselines, or statistics.
- 2: weak numbers, narrow evaluation setting, or unclear fairness.
- 1: numerical evidence absent or not meaningful for claims.
- `N/A artifact`: use for pure simulator, scenario generator, standard formulation, evaluation suite, or dataset papers; instead write an artifact-quality note.

Artifact-quality note for `pure evaluation artifact`:

```text
Artifact scope:
Task realism:
Metric validity:
Baseline coverage:
Adoption or reproducibility signal:
Known limitation:
```

Overall quality label:

- `A`: high-priority close work.
- `B`: useful supporting or baseline work.
- `C`: background only or weak fit.
- `Risk`: must inspect because it may undercut novelty.

Do not convert scores into acceptance probability.
