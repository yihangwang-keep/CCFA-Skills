#!/usr/bin/env python3
"""Validate current CCFA structure without rewriting files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_SKILLS = {
    "ccf-algorithm-code-auditor",
    "ccf-common",
    "ccf-env-code-auditor",
    "ccf-complexity-upgrade",
    "ccf-idea-optimizer",
    "ccf-idea-reviewer",
    "ccf-integrity-auditor",
    "ccf-literature-monitor",
    "ccf-literature-searcher",
    "ccf-mes-validation",
    "ccf-visual-composer",
    "ccf-paper-reviewer",
    "ccf-paper-writer",
    "ccf-pipeline-orchestrator",
    "ccf-project-scaffolder",
    "ccf-rebuttal-writer",
    "ccf-skill-forger",
    "ccf-submission-checker",
    "ccf-paper-to-exemplar",
}

COMMUNICATION_CHAIN = {
    "ccf-env-code-auditor",
    "ccf-mes-validation",
    "ccf-complexity-upgrade",
    "ccf-algorithm-code-auditor",
}

FORBIDDEN_RUNTIME_TERM = re.compile(
    r"(?<![A-Za-z])(?:over|sub)?claim(?:s|ed|ing)?(?![A-Za-z])",
    flags=re.IGNORECASE,
)
REFERENCE_TERM_POLICY_FILES = {
    "ccf-common/references/ccfa-yaml-contract.md",
    "ccf-common/references/communication-research-terms.md",
}
REFERENCE_TERM_EXCLUDED_PREFIXES = (
    "ccf-paper-writer/references/exemplars/papers/",
    "ccf-paper-writer/references/venue-guides/",
)
FORBIDDEN_COMMUNICATION_DEFAULTS = {
    "AI/ML": re.compile(r"\bAI\s*/\s*ML\b", flags=re.IGNORECASE),
    "artificial intelligence": re.compile(r"\bartificial intelligence\b", flags=re.IGNORECASE),
    "machine learning": re.compile(r"\bmachine learning\b", flags=re.IGNORECASE),
    "deep learning": re.compile(r"\bdeep learning\b", flags=re.IGNORECASE),
    "reinforcement learning": re.compile(r"\breinforcement learning\b", flags=re.IGNORECASE),
    "learning-based": re.compile(r"\blearning[- ]based\b", flags=re.IGNORECASE),
    "learned": re.compile(r"\blearned\b", flags=re.IGNORECASE),
    "training": re.compile(r"\btraining\b", flags=re.IGNORECASE),
    "dataset": re.compile(r"\bdatasets?\b", flags=re.IGNORECASE),
    "neural": re.compile(r"\bneural(?:\s+networks?)?\b", flags=re.IGNORECASE),
    "LLM": re.compile(r"\bLLMs?\b", flags=re.IGNORECASE),
    "reward": re.compile(r"\brewards?\b", flags=re.IGNORECASE),
    "人工智能": re.compile(r"人工智能"),
    "人工智慧": re.compile(r"人工智慧"),
    "机器学习": re.compile(r"机器学习"),
    "機器學習": re.compile(r"機器學習"),
    "深度学习": re.compile(r"深度学习"),
    "深度學習": re.compile(r"深度學習"),
    "强化学习": re.compile(r"强化学习"),
    "強化學習": re.compile(r"強化學習"),
    "神经网络": re.compile(r"神经网络"),
    "神經網路": re.compile(r"神經網路"),
    "数据集": re.compile(r"数据集"),
    "训练": re.compile(r"训练"),
    "訓練": re.compile(r"訓練"),
    "資料集": re.compile(r"資料集"),
}

REQUIRED_CORE_GATES = {
    "ccf-env-code-auditor/SKILL.md": (
        "Authority gate",
        "Design-contract gate",
        "Traceability gate",
        "Semantic-correctness gate",
        "Independent-execution gate",
        "Optimization-fidelity gate",
        "Layer-2 tradeoff-resistance gate",
        "Acceptance gate",
    ),
    "ccf-algorithm-code-auditor/SKILL.md": (
        "Authority gate",
        "Environment-contract gate",
        "Design-contract gate",
        "Traceability gate",
        "Semantic-correctness gate",
        "Proposed-method eligibility gate",
        "Reference gate",
        "Independent-MES gate",
        "Acceptance gate",
    ),
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(path: Path) -> dict[str, str]:
    text = read(path)
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter")
    fm = text[4:end]
    result: dict[str, str] = {}
    for key in ("name", "description"):
        match = re.search(rf"^{key}:\s*(.+)$", fm, flags=re.MULTILINE)
        if not match:
            raise ValueError(f"missing {key}")
        value = match.group(1).strip().strip('"').strip("'")
        if not value:
            raise ValueError(f"empty {key}")
        result[key] = value
    shared = re.search(r"shared_controls:\s*(.+)$", fm, flags=re.MULTILINE)
    if shared:
        result["shared_controls"] = shared.group(1).strip().strip('"').strip("'")
    return result


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_skills(errors: list[str]) -> list[str]:
    names: list[str] = []
    for path in sorted(ROOT.rglob("SKILL.md")):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        try:
            fm = frontmatter(path)
        except ValueError as exc:
            fail(errors, f"{rel}: {exc}")
            continue
        name = fm["name"]
        names.append(name)
        if not name.startswith("ccf-"):
            fail(errors, f"{rel}: skill name must start with ccf-, got {name}")
        shared = fm.get("shared_controls")
        if shared:
            target = (path.parent / shared).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"{rel}: shared_controls points outside repo: {shared}")
            if not target.exists():
                fail(errors, f"{rel}: shared_controls target missing: {shared}")
    if len(names) != len(set(names)):
        seen = set()
        dupes = sorted({name for name in names if name in seen or seen.add(name)})
        fail(errors, f"duplicate skill names: {', '.join(dupes)}")
    actual = set(names)
    if actual != EXPECTED_SKILLS:
        extra = sorted(actual - EXPECTED_SKILLS)
        missing = sorted(EXPECTED_SKILLS - actual)
        if extra:
            fail(errors, "unexpected runtime skills: " + ", ".join(extra))
        if missing:
            fail(errors, "missing expected runtime skills: " + ", ".join(missing))
    return names


def check_registry(skill_names: list[str], errors: list[str]) -> None:
    registry = ROOT / "ccf-common" / "references" / "skill-trigger-registry.yaml"
    if not registry.is_file():
        fail(errors, "missing skill-trigger-registry.yaml")
        return
    text = read(registry)
    registered = set(re.findall(r"^\s*-\s+name:\s*(ccf-[a-z0-9-]+)\s*$", text, flags=re.MULTILINE))
    missing = sorted(set(skill_names) - registered)
    if missing:
        fail(errors, "registry missing skills: " + ", ".join(missing))


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def check_research_terminology(errors: list[str]) -> None:
    runtime_entries = list(ROOT.glob("ccf-*/SKILL.md"))
    runtime_entries.extend(ROOT.glob("ccf-*/agents/openai.yaml"))
    for path in sorted(runtime_entries):
        text = read(path)
        match = FORBIDDEN_RUNTIME_TERM.search(text)
        if match:
            rel = path.relative_to(ROOT).as_posix()
            fail(
                errors,
                f"{rel}:{line_number(text, match.start())}: use paper conclusion, supported conclusion, "
                "applicability range, or statement instead of claim terminology",
            )

    reference_entries = sorted(ROOT.glob("ccf-*/references/**/*.md"))
    for path in reference_entries:
        rel = path.relative_to(ROOT).as_posix()
        if rel in REFERENCE_TERM_POLICY_FILES:
            continue
        if rel.startswith(REFERENCE_TERM_EXCLUDED_PREFIXES):
            continue
        if "evaluation" in path.relative_to(ROOT).parts:
            continue
        text = read(path)
        match = FORBIDDEN_RUNTIME_TERM.search(text)
        if match:
            fail(
                errors,
                f"{rel}:{line_number(text, match.start())}: first-party runtime reference uses "
                "retired assertion terminology",
            )

    for skill in sorted(COMMUNICATION_CHAIN):
        root = ROOT / skill
        paths = [root / "SKILL.md"]
        reference_root = root / "references"
        if reference_root.is_dir():
            paths.extend(sorted(reference_root.rglob("*.md")))
        for path in paths:
            text = read(path)
            for label, pattern in FORBIDDEN_COMMUNICATION_DEFAULTS.items():
                match = pattern.search(text)
                if match:
                    rel = path.relative_to(ROOT).as_posix()
                    fail(
                        errors,
                        f"{rel}:{line_number(text, match.start())}: communication chain contains "
                        f"the disallowed default term {label!r}",
                    )


def check_design_validation_contract(errors: list[str]) -> None:
    for rel in (
        "ccf-common/references/implementation-review-protocol.md",
        "ccf-common/references/ralph-phase-contract.md",
        "ccf-mes-validation/references/phase-a-problem-contract.md",
        "ccf-complexity-upgrade/references/phase-b-upgrade-contract.md",
        "ccf-pipeline-orchestrator/references/evidence-plan.md",
    ):
        if not (ROOT / rel).is_file():
            fail(errors, f"missing shared protocol: {rel}")

    review_ref = "../ccf-common/references/implementation-review-protocol.md"
    for rel in (
        "ccf-env-code-auditor/SKILL.md",
        "ccf-algorithm-code-auditor/SKILL.md",
    ):
        if review_ref not in read(ROOT / rel):
            fail(errors, f"{rel}: missing CCFA-native implementation-review reference")

    semantic_tokens = {
        "ccf-common/references/implementation-review-protocol.md": (
            "canonical review envelope",
            "review_protocol_digest",
            "coordinator_id",
            "fresh: true",
            "read_only: true",
            "implementer_ids",
            "reviewer_distinctness_check",
            "reviewer_coordinator_exclusion_check",
            "cannot offset",
            "stale",
            "terminal_acceptance",
        ),
    }
    for rel, tokens in semantic_tokens.items():
        protocol_text = read(ROOT / rel)
        for token in tokens:
            if token not in protocol_text:
                fail(errors, f"{rel}: missing protected contract token {token!r}")

    phase_contract_tokens = {
        "ccf-mes-validation/SKILL.md": (
            "Phase A",
            "Accepted Input Document",
            "mes_role: anchor",
            "anchor_accepted",
            "ccf-env-code-auditor",
            "ccf-algorithm-code-auditor",
        ),
        "ccf-complexity-upgrade/SKILL.md": (
            "Phase B",
            "Accepted Upgrade Document",
            "stage_case",
            "anchor regression",
            "never creates another MES",
        ),
        "ccf-env-code-auditor/SKILL.md": (
            "complexity-stage-audit",
            "do not recompute `algorithmic_need`",
            "do not rerun the sweep",
        ),
        "ccf-common/references/ralph-phase-contract.md": (
            "one smallest delta",
            "mes_validation",
            "complexity_upgrade",
            "creating another MES",
            "freezing the anchor before algorithm acceptance",
        ),
        "ccf-mes-validation/references/mes-validation-record.md": (
            "status: active | document_accepted",
            "scope: anchor_candidate_only",
            "mes_role: candidate | anchor",
            "terminal_evidence",
        ),
        "ccf-complexity-upgrade/references/complexity-upgrade-record.md": (
            "status: active | document_accepted",
            "anchor_mes_version",
            "stage_case_id",
            "environment_consistency",
            "anchor_regression",
            "terminal_evidence",
        ),
    }
    for rel, tokens in phase_contract_tokens.items():
        phase_text = read(ROOT / rel)
        for token in tokens:
            if token not in phase_text:
                fail(errors, f"{rel}: missing phase-boundary token {token!r}")

    for rel, gates in REQUIRED_CORE_GATES.items():
        text = read(ROOT / rel)
        for gate in gates:
            if f"**{gate}:**" not in text:
                fail(errors, f"{rel}: missing preserved core gate {gate!r}")

    pipeline_text = read(ROOT / "ccf-pipeline-orchestrator" / "SKILL.md")
    for token in ("evidence-plan", "research reframe", "TBD", "ccf-visual-composer"):
        if token not in pipeline_text:
            fail(errors, f"ccf-pipeline-orchestrator/SKILL.md missing evolution token: {token}")

    phase_paths = (
        ROOT / "ccf-common" / "references" / "ralph-phase-contract.md",
        ROOT / "ccf-mes-validation" / "SKILL.md",
        ROOT / "ccf-complexity-upgrade" / "SKILL.md",
        ROOT / "ccf-common" / "references" / "implementation-review-protocol.md",
        ROOT / "ccf-env-code-auditor" / "SKILL.md",
        ROOT / "ccf-env-code-auditor" / "references" / "audit-protocol.md",
        ROOT / "ccf-algorithm-code-auditor" / "SKILL.md",
        ROOT / "ccf-algorithm-code-auditor" / "references" / "algorithm-audit-protocol.md",
    )
    forbidden_external_invocations = ("$code-review", "$diagnosing-bugs", "$tdd", "$research")
    forbidden_git_fixed_points = (
        "dedicated loop branch",
        "dedicated branch or worktree",
        "checkpoint commit",
        "loop_base_sha",
        "round_base_sha",
        "checkpoint_head",
        "reviewed `HEAD`",
    )
    for path in phase_paths:
        phase_text = read(path)
        for token in forbidden_external_invocations:
            if token in phase_text:
                fail(errors, f"{path.relative_to(ROOT)} must not invoke external workflow {token}")
        for token in forbidden_git_fixed_points:
            if token in phase_text:
                fail(errors, f"{path.relative_to(ROOT)} must not require Git fixed point {token!r}")

    scaffold = ROOT / "ccf-project-scaffolder" / "assets" / "ccfa.yaml"
    scaffold_text = read(scaffold)
    if 'version: "0.5.0"' not in scaffold_text:
        fail(errors, "ccfa.yaml scaffold must use contract version 0.5.0")
    if "paper_conclusions:" not in scaffold_text:
        fail(errors, "ccfa.yaml scaffold missing paper_conclusions")
    if re.search(r"^claims\s*:", scaffold_text, flags=re.MULTILINE):
        fail(errors, "ccfa.yaml scaffold still contains the retired claims field")
    for artifact in (
        "phase_a",
        "phase_b",
        "environment_audit",
        "algorithm_audit",
    ):
        if not re.search(rf"^\s{{2}}{artifact}:\s*", scaffold_text, flags=re.MULTILINE):
            fail(errors, f"ccfa.yaml scaffold missing artifacts.{artifact}")

    contract_rel = "ccf-common/references/ccfa-yaml-contract.md"
    contract_text = read(ROOT / contract_rel)
    policy_match = re.search(r"```json\s+(\{.*?\})\s+```", contract_text, flags=re.DOTALL)
    if not policy_match:
        fail(errors, f"{contract_rel}: missing machine-readable migration policy")
    else:
        try:
            migration_policy = json.loads(policy_match.group(1)).get("migration", {})
        except json.JSONDecodeError as exc:
            fail(errors, f"{contract_rel}: invalid migration policy JSON: {exc}")
            migration_policy = {}
        expected_policy = {
            "source_versions": ["0.4.x"],
            "target_version": "0.5.0",
            "legacy_field": "claims",
            "canonical_field": "paper_conclusions",
            "read_mode": "read_only_alias",
            "authorized_copy": "verbatim",
            "dual_field_merge": "stable_id",
            "same_id_same_content": "retain_once",
            "same_id_different_content": "report_conflict",
            "unkeyed_entries": "preserve_source_order",
            "remove_legacy": "after_validated_write",
            "unauthorized_write": "leave_unchanged_and_report",
        }
        if migration_policy != expected_policy:
            fail(errors, f"{contract_rel}: migration policy does not match the v0.4-to-v0.5 contract")

    for rel in (
        "ccf-project-scaffolder/SKILL.md",
        "ccf-pipeline-orchestrator/SKILL.md",
        "ccf-literature-monitor/SKILL.md",
        "ccf-integrity-auditor/SKILL.md",
        "ccf-submission-checker/SKILL.md",
    ):
        text = read(ROOT / rel)
        if "ccfa-yaml-contract.md" not in text:
            fail(errors, f"{rel}: does not route legacy project state through the shared contract")
        if "artifact-contracts.md" not in text:
            fail(errors, f"{rel}: does not load shared artifact ownership for project state")


def check_venue_guides(errors: list[str]) -> None:
    legacy = ROOT / "ccf-conference-skills"
    if legacy.exists() and list(legacy.rglob("SKILL.md")):
        fail(errors, "legacy ccf-conference-skills/**/SKILL.md still exists")
    guide_root = ROOT / "ccf-paper-writer" / "references" / "venue-guides"
    index = guide_root / "index.md"
    if not index.is_file():
        fail(errors, "missing venue-guides/index.md")
        return
    text = read(index)
    rows = [line for line in text.splitlines() if line.startswith("| [")]
    if len(rows) < 100:
        fail(errors, f"venue index too small: {len(rows)} rows")
    for slug in ("cvpr", "neurips", "sigmod"):
        guide = guide_root / f"{slug}.md"
        if not guide.is_file():
            fail(errors, f"missing venue guide: {slug}")
            continue
        guide_text = read(guide)
        if "ccf-latex-templates" not in guide_text:
            fail(errors, f"{slug} guide lacks template path")
    for match in re.findall(r"`(ccf-latex-templates/[^`]+)`", text):
        candidate = ROOT / match
        if not candidate.exists():
            fail(errors, f"template path missing: {match}")


def check_required_files(errors: list[str]) -> None:
    required = [
        "docs/SKILLS_CATALOG.md",
        "docs/ARCHITECTURE.md",
        "docs/INSTALLATION_MATRIX.md",
        "docs/INSTALLATION_MATRIX.zh-CN.md",
        "docs/INSTALLATION_MATRIX.zh-TW.md",
        "AGENT_GUIDE.md",
        "CHANGELOG.md",
        "demo/attention-is-all-you-need/README.md",
        "demo/attention-is-all-you-need/ccfa.yaml",
        "demo/attention-is-all-you-need/skill-self-tests.md",
        "demo/attention-is-all-you-need/artifacts/00-original-paper-reading.md",
        "demo/attention-is-all-you-need/artifacts/01-idea-document.md",
        "demo/attention-is-all-you-need/artifacts/02-iclr-closed-loop-skill-run.md",
        "demo/attention-is-all-you-need/artifacts/03-idea-review.md",
        "demo/attention-is-all-you-need/artifacts/03-writing-draft.md",
        "demo/attention-is-all-you-need/artifacts/04-review-and-rebuttal.md",
        "demo/attention-is-all-you-need/artifacts/05-submission-check.md",
        "demo/attention-is-all-you-need/artifacts/06-family-self-audit.md",
        "demo/attention-is-all-you-need/artifacts/official-data.md",
        "demo/attention-is-all-you-need/artifacts/result-tables.md",
        "demo/attention-is-all-you-need/visual-composer/README.md",
        "demo/attention-is-all-you-need/visual-composer/plot_demo.py",
        "demo/attention-is-all-you-need/visual-composer/figures/translation_bleu_lollipop.svg",
        "demo/attention-is-all-you-need/visual-composer/figures/training_schedule_slopegraph.svg",
        "demo/attention-is-all-you-need/visual-composer/figures/configuration_ratio_heatmap.svg",
        "demo/attention-is-all-you-need/visual-composer/figures/base_big_small_multiples.svg",
        "demo/attention-is-all-you-need/paper/attention_iclr_submission.tex",
        "demo/attention-is-all-you-need/paper/iclr2026_conference.sty",
        "ccf-common/references/artifact-contracts.md",
        "ccf-common/references/ccfa-yaml-contract.md",
        "ccf-visual-composer/resources/python/ccfa_plot_recipes.py",
        "ccf-visual-composer/references/python-plot-recipes.md",
        "ccf-visual-composer/references/plot-inspiration-map.md",
        "ccf-paper-writer/references/output-style-policy.md",
        "ccf-paper-writer/references/research-writing-patterns.md",
        "ccf-paper-writer/references/prose-quality-guardrails.md",
        "ccf-project-scaffolder/assets/ccfa.yaml",
        ".codex-plugin/plugin.json",
        ".claude-plugin/plugin.json",
        ".github/workflows/validate.yml",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            fail(errors, f"missing required file: {rel}")
    manifests: dict[str, dict[str, object]] = {}
    for rel in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
        path = ROOT / rel
        if path.exists():
            try:
                manifests[rel] = json.loads(read(path))
            except json.JSONDecodeError as exc:
                fail(errors, f"{rel}: invalid JSON: {exc}")
    versions = {str(manifest.get("version", "")) for manifest in manifests.values()}
    if len(versions) > 1:
        fail(errors, "plugin manifest versions do not match: " + ", ".join(sorted(versions)))
    codex_manifest = manifests.get(".codex-plugin/plugin.json", {})
    interface = codex_manifest.get("interface", {})
    if isinstance(interface, dict):
        long_description = str(interface.get("longDescription", ""))
        expected_count = f"{len(EXPECTED_SKILLS)}-skill"
        if expected_count not in long_description:
            fail(errors, f"Codex plugin longDescription must describe the {expected_count} family")
    for key in (
        "architecture",
        "workflow",
        "review-boundaries",
        "catalog",
        "routing",
        "artifacts",
        "installation",
        "demo-attention",
    ):
        for suffix in ("", ".zh-CN", ".zh-TW"):
            rel = f"assets/ccfa-skills-{key}{suffix}.svg"
            path = ROOT / rel
            if not path.is_file() or "<svg" not in read(path):
                fail(errors, f"missing or invalid SVG: {rel}")


def main() -> int:
    errors: list[str] = []
    names = check_skills(errors)
    check_registry(names, errors)
    check_research_terminology(errors)
    check_design_validation_contract(errors)
    check_venue_guides(errors)
    check_required_files(errors)
    if errors:
        print("CCFA validation failed:")
        for error in errors:
            print(f"[ERROR] {error}")
        return 1
    print(f"CCFA validation passed. Skills: {len(names)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
