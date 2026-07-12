# Result Templates

Use these templates to produce fill-in result tables. Keep all unknown numbers blank, `TBD`, or bracketed placeholders.

## Claim-Evidence Matrix(must)

```md
| Claim | Reviewer question | Evidence needed | Dataset/benchmark | Baselines | Metrics | Result placeholder | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | TBD | planned / running / done |
```
Evidence needed must answer what the evidences needed for this claim.

## Main Comparison Table

```md
| Method | Source | Setting | Metric 1 ↑/↓ | Metric 2 ↑/↓ | Metric 3 ↑/↓ | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| User method | this paper |  | TBD | TBD | TBD |  |
| Baseline A | citation needed |  | TBD | TBD | TBD |  |
| Baseline B | citation needed |  | TBD | TBD | TBD |  |
```

## Ablation Table(if needed)

```md
| Variant | Component changed | Mechanism tested | Metric 1 ↑/↓ | Metric 2 ↑/↓ | Interpretation after user fills result |
| --- | --- | --- | --- | --- | --- |
| Full method | none | full mechanism | TBD | TBD |  |
| w/o component A | remove A | necessity of A | TBD | TBD |  |
| generic replacement | replace A | specificity of design | TBD | TBD |  |
```

## Robustness / Stress Test Table(if needed)

```md
| Stress condition | Why it matters | Dataset/workload | Metric | User result | Failure threshold | Reviewer concern answered |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | TBD |  |  |
```

## Qualitative / Case Study Table(if needed)

```md
| Case | Selection rule | Expected observation | User-provided result | What it demonstrates | Failure or limitation |
| --- | --- | --- | --- | --- | --- |
|  | representative / hard / failure |  | TBD |  |  |
```

## Execution Priority Table(must)

```md
| Priority | Experiment | Claim defended | Cost | Dependency | Appendix/main | Stop condition |
| --- | --- | --- | --- | --- | --- | --- |
| P0 |  |  | low/medium/high |  | main |  |
```

## No-Fabrication Reminder

Use this note when returning templates:

```text
No experimental result has been generated here. All TBD cells must be filled from user-run experiments, paper-provided numbers, or verified public baseline reports with matching protocol.
```
