#!/usr/bin/env python3
"""Migrate paper insight notes to the evidence-bounded two-layer schema.

This migration is intentionally conservative.  It keeps the five manually
reviewed notes that already use the new schema, carries forward useful cues
from older note formats, and never upgrades a paper to FULL_TEXT_CHECKED just
because a local PDF or an automatically extracted text file exists.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "work" / "sources" / "papers.json"
STATUS = ROOT / "research" / "READING_STATUS.csv"
VALID_EVIDENCE = {"CURATION_ONLY", "ABSTRACT_CHECKED", "FULL_TEXT_CHECKED", "EXPERIMENT_CHECKED"}
MODERN_SECTIONS = (
    "## Paper-supported conclusion",
    "## Researcher interpretation",
    "## Falsifiable research question",
)


def parse_sections(markdown: str) -> dict[str, str]:
    """Return level-2 sections while retaining nested headings in each body."""

    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in markdown.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections.setdefault(current, [])
        elif line.startswith("# ") and current is not None:
            current = None
        elif current is not None:
            sections[current].append(line)
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def first_section(sections: dict[str, str], *names: str) -> str:
    for name in names:
        value = sections.get(name, "").strip()
        if value:
            return value
    return ""


def extract_field(markdown: str, field: str) -> str:
    pattern = re.compile(rf"(?im)^\s*(?:[-*]\s*)?{re.escape(field)}\s*:\s*(.+?)\s*$")
    match = pattern.search(markdown)
    return match.group(1).strip() if match else ""


def extract_evidence(markdown: str) -> str:
    pattern = re.compile(r"(?im)^\s*(?:>\s*)?(?:[-*]\s*)?Evidence maturity\s*:\s*(?:`([^`]+)`|([^.\n]+))")
    match = pattern.search(markdown)
    if not match:
        return ""
    value = (match.group(1) or match.group(2) or "").strip()
    return value if value in VALID_EVIDENCE else ""


def read_tracker() -> dict[str, dict[str, str]]:
    if not STATUS.exists():
        return {}
    with STATUS.open(encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        tracker: dict[str, dict[str, str]] = {}
        for row in rows:
            overview = row.get("overview_path", "").removeprefix("./")
            if not overview:
                continue
            folder = overview.removesuffix("/01_overview.md")
            tracker[folder] = row
            tracker[folder.casefold()] = row
        return tracker


def resolve_folder(folder_name: str) -> Path:
    direct = ROOT / folder_name
    if direct.is_dir():
        return direct

    # Three legacy entries differ only by case in the manifest versus the
    # filesystem.  Resolve them without changing either canonical source.
    parts = Path(folder_name).parts
    current = ROOT
    for part in parts:
        matches = [child for child in current.iterdir() if child.name.casefold() == part.casefold()]
        if len(matches) != 1:
            raise FileNotFoundError(folder_name)
        current = matches[0]
    return current


def is_modern(markdown: str) -> bool:
    return all(section in markdown for section in MODERN_SECTIONS) and "Canonical metadata:" in markdown


def nonempty_lines(block: str) -> list[str]:
    return [line.strip() for line in block.splitlines() if line.strip()]


def strip_list_marker(line: str) -> str:
    line = re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", "", line.strip())
    return line.strip()


def is_placeholder(line: str) -> bool:
    value = strip_list_marker(line)
    if not value:
        return True
    lowered = value.casefold()
    placeholders = (
        "unverified —",
        "unverified -",
        "자동 추출 실패",
        "자동 추출 없음",
        "본문 확인 필요",
        "본문 수동 확인 필요",
        "정독 후 paper-supported",
        "정독 후 research relevance",
        "가장 작은 반증 실험을 정의한다",
        "핵심 claim을 반증할 수 있는 가장 작은 실험을 정독 후 정의한다",
        "어떤 core에서 출발하고 어떤 frontier로 이어지는지 확인한다",
    )
    return lowered.startswith(placeholders)


def useful_lines(block: str) -> list[str]:
    """Extract old-note prose while dropping repeated boilerplate."""

    result: list[str] = []
    generic_fragments = (
        "위 paper-specific cue를 논문 claim으로만 두지 말고",
        "논문이 제안한 representation/method를 3d scene understanding",
        "핵심 단서를 그대로 쓰기보다 geometry, semantics, action constraint",
        "이 파일의 활용 방향은 논문 claim이 아니라",
        "논문 내 explicit limitation/future cue가 부족한 경우",
        "논문 task 범위 밖의 3d consistency",
        "논문이 다룬 task 범위 밖의 3d consistency",
    )
    for raw in nonempty_lines(block):
        value = strip_list_marker(raw)
        lowered = value.casefold()
        if is_placeholder(value) or any(fragment in lowered for fragment in generic_fragments):
            continue
        if value not in result:
            result.append(value)
    return result


def labelled_cues(block: str) -> list[tuple[str, str]]:
    """Extract the paper/problem/method/result cues used by legacy notes."""

    labels = {
        "problem cue": "Problem cue",
        "출발 문제 단서": "Problem cue",
        "method cue": "Method cue",
        "핵심 방법 단서": "Method cue",
        "result/evaluation cue": "Result/evaluation cue",
        "result cue": "Result cue",
        "주장된 효과 단서": "Claim/result cue",
    }
    result: list[tuple[str, str]] = []
    for raw in nonempty_lines(block):
        value = strip_list_marker(raw)
        if ":" not in value:
            continue
        label, body = value.split(":", 1)
        canonical = labels.get(label.strip().casefold())
        body = body.strip()
        if canonical and body and not is_placeholder(body):
            item = (canonical, body)
            if item not in result:
                result.append(item)
    return result


def cue_values(old_sections: dict[str, str], overview_sections: dict[str, str]) -> list[tuple[str, str]]:
    cues: list[tuple[str, str]] = []

    def add(label: str, value: str) -> None:
        value = value.strip()
        if value and not is_placeholder(value) and value not in {old_value for _, old_value in cues}:
            cues.append((label, value))

    for section_name in (
        "이 논문에서 가져갈 핵심 개념",
        "Captured Source Cues — Not Yet Independently Verified",
        "근거가 되는 논문 단서",
    ):
        for label, value in labelled_cues(old_sections.get(section_name, "")):
            add(label, value)

    for section_name, label in (
        ("Paper Claim", "Claim recorded in prior note"),
        ("Paper-Supported Direction", "Claim/direction recorded in prior note"),
        ("Strength", "Strength recorded in prior note"),
    ):
        for value in useful_lines(old_sections.get(section_name, "")):
            add(label, value)

    if not cues:
        for section_name, label in (
            ("Problem", "Problem cue"),
            ("해결하려는 문제", "Problem cue"),
            ("Core Idea", "Method cue"),
            ("Main Claims", "Claim/result cue"),
            ("Abstract Cue", "Abstract cue"),
        ):
            for value in useful_lines(overview_sections.get(section_name, ""))[:3]:
                add(label, value)
    return cues[:8]


def evidence_from(item: dict[str, object], old: str, overview: str, tracker: dict[str, dict[str, str]]) -> str:
    # A manually maintained evidence header in 01_overview is strongest.
    overview_evidence = extract_evidence(overview)
    if overview_evidence:
        return overview_evidence

    audit = extract_field(overview, "Source audit") or extract_field(old, "Source audit")
    if "abstract" in audit.casefold() and "metadata registration only" not in audit.casefold():
        return "ABSTRACT_CHECKED"

    row = tracker.get(str(item["folder"])) or tracker.get(str(item["folder"]).casefold())
    if row and row.get("evidence_level") in VALID_EVIDENCE:
        return row["evidence_level"]

    # Legacy notes may carry an evidence header even when 01_overview does
    # not.  This branch is used while migrating an old-format note; modern
    # notes are handled from overview/tracker evidence above.
    if "Canonical metadata:" not in old:
        legacy_evidence = extract_evidence(old)
        if legacy_evidence:
            return legacy_evidence
    # A legacy UNREAD marker is a status, not an evidence level.  It is kept
    # conservative here because generated/local text is not manual reading.
    return "CURATION_ONLY"


def sync_tracker_evidence(markdown: str, evidence: str) -> str:
    if evidence not in VALID_EVIDENCE:
        return markdown
    pattern = re.compile(r"(?m)^> Evidence maturity: `[^`]+`\.")
    replacement = f"> Evidence maturity: `{evidence}`."
    return pattern.sub(replacement, markdown, count=1)


def sync_generated_basis(markdown: str, evidence: str, overview: str) -> str:
    if "Analysis basis:" not in markdown:
        return markdown
    generated_markers = (
        "01_overview의 source audit와 기존 insight cue를 이관했다",
        "abstract/metadata cue와 자동 추출 결과를 정리한 curation scaffold",
    )
    if not any(marker in markdown for marker in generated_markers):
        return markdown
    replacement = f"> Analysis basis: {source_basis(evidence, overview, markdown)}"
    return re.sub(r"(?m)^> Analysis basis: .*?$", replacement, markdown, count=1)


def cleanup_generated_note(markdown: str) -> str:
    """Remove the duplicated boundary sentence introduced by early migration output."""

    lines = [line for line in markdown.splitlines() if not line.startswith("- **Evidence boundary:**")]
    return "\n".join(lines).rstrip() + "\n"


def sync_generated_boundary(markdown: str, evidence: str) -> str:
    if "> **Evidence boundary:**" not in markdown:
        return markdown
    generated_markers = (
        "01_overview의 source audit와 기존 insight cue를 이관했다",
        "abstract/metadata cue와 자동 추출 결과를 정리한 curation scaffold",
    )
    if not any(marker in markdown for marker in generated_markers):
        return markdown
    replacement = f"> **Evidence boundary:** {evidence_boundary(evidence)}"
    return re.sub(r"(?m)^> \*\*Evidence boundary:\*\* .*?$", replacement, markdown, count=1)


def evidence_boundary(evidence: str) -> str:
    if evidence == "FULL_TEXT_CHECKED":
        return "본문의 method/evaluation을 수동 확인한 근거만 paper-supported conclusion으로 기록한다."
    if evidence == "EXPERIMENT_CHECKED":
        return "핵심 실험까지 확인된 근거를 paper-supported conclusion으로 기록한다."
    if evidence == "ABSTRACT_CHECKED":
        return "현재 확인 범위는 공식 abstract/project 수준이다. 상세 method, exact metric, failure는 full-text 확인 전까지 확정하지 않는다."
    return "현재 내용은 registry와 기존 curation cue를 정리한 것이다. 자동 추출이나 local PDF 보유는 정독 근거로 간주하지 않으며, 상세 claim은 full-text 확인이 필요하다."


def source_basis(evidence: str, overview: str, old: str) -> str:
    audit = extract_field(overview, "Source audit") or extract_field(old, "Source audit")
    if audit:
        audit = audit.rstrip(".")
        return f"`{evidence}`; 01_overview의 source audit와 기존 insight cue를 이관했다: {audit}. 자동 추출 결과는 수동 정독으로 간주하지 않는다."
    return f"`{evidence}`; 기존 insight cue와 registry metadata만 이관했다. 자동 추출 결과는 수동 정독으로 간주하지 않는다."


def loop_position(item: dict[str, object]) -> str:
    text = " ".join(
        [str(item.get("category", "")), str(item.get("title", "")), " ".join(str(x) for x in item.get("tags", []))]
    ).casefold()
    if any(key in text for key in ("world model", "uncertainty", "recovery", "safety", "failure")):
        return "observation → state/world model → decision/recovery"
    if any(key in text for key in ("vla", "vision-language-action", "generalist", "language")):
        return "observation/language → task decision → action/control"
    if any(key in text for key in ("3d", "slam", "scene", "depth", "geometry", "perception", "vision")):
        return "observation → state/world model"
    if any(key in text for key in ("planning", "control", "whole-body", "trajectory", "motion", "optimization")):
        return "task & motion decision → policy/control"
    if any(key in text for key in ("contact", "tactile", "manipulation", "force", "dexterity")):
        return "policy/control → contact → feedback"
    if any(key in text for key in ("locomotion", "humanoid", "quadruped", "legged")):
        return "state estimation → whole-body policy/control → contact/feedback"
    if any(key in text for key in ("dataset", "benchmark", "evaluation")):
        return "data/evaluation → policy/control comparison"
    if any(key in text for key in ("reinforcement", "imitation", "policy", "robot learning", "offline")):
        return "observation → policy/control → feedback"
    return "observation → state/world model → decision → policy/control → feedback"


def tags_text(item: dict[str, object]) -> str:
    tags = [str(tag) for tag in item.get("tags", [])]
    return ", ".join(tags[:5]) or str(item.get("category", "paper-specific interface"))


def old_research_use(sections: dict[str, str]) -> list[str]:
    return useful_lines(first_section(sections, "내 연구 방향에서 어떻게 활용할 수 있나", "Research Use", "Researcher Interpretation", "내 관점"))


def old_lineage(sections: dict[str, str]) -> list[str]:
    return useful_lines(first_section(sections, "Dependency Position", "Reading Dependency and Lineage", "Reading Dependency"))


def old_boundaries(sections: dict[str, str]) -> list[str]:
    return useful_lines(
        first_section(
            sections,
            "주의할 점",
            "Limitations / Failure Modes to Audit",
            "Limitation",
            "이 논문이 끝난 지점",
            "Future Work",
            "Close-Reading Checklist",
        )
    )


def old_reproduction(sections: dict[str, str]) -> list[str]:
    return useful_lines(
        first_section(
            sections,
            "실험으로 확인할 방향",
            "Minimum Experiment",
            "Minimal Reproduction",
        )
    )


def old_questions(sections: dict[str, str]) -> list[str]:
    return useful_lines(first_section(sections, "다음 연구 질문", "Falsifiable research question"))


def list_block(values: list[str], label: str | None = None) -> str:
    lines: list[str] = []
    for value in values:
        value = value.strip()
        if not value:
            continue
        lines.append(f"- {label + ': ' if label else ''}{value}")
    return "\n".join(lines)


def make_question(item: dict[str, object], old_questions_: list[str], position: str) -> str:
    if old_questions_:
        # Keep one source-specific question when the old note contained one;
        # the rest of the old generic prompts are not copied wholesale.
        candidate = old_questions_[0].rstrip("?。")
        if len(candidate) <= 260 and "3d geometry와 semantic grounding" not in candidate.casefold():
            return candidate + ("?" if not candidate.endswith("?") else "")
    tags = tags_text(item)
    item_text = " ".join(
        [str(item.get("category", "")), str(item.get("title", "")), " ".join(str(x) for x in item.get("tags", []))]
    ).casefold()
    if "observation/language" in position:
        return f"고정된 data·compute budget에서 {tags} action interface가 action reconstruction과 closed-loop task success를 temporal·contact perturbation 아래 개선하는가?"
    if "representation" in item_text or "pretraining" in item_text:
        return f"고정된 data·compute budget에서 {tags} representation이 단순 baseline보다 downstream task success와 representation robustness를 개선하는가?"
    if "observation" in position and "state/world model" in position:
        return f"고정된 sensor·compute budget에서 {tags} 기반 표현이 robot-relevant state 품질과 downstream task success를 sensor noise와 partial observation 아래 개선하는가?"
    if "contact" in position:
        return f"고정된 sensing/control rate에서 {tags} interface가 직접 joint-action baseline보다 contact loss와 force/pose error를 줄이는가?"
    if "decision" in position or "planning" in str(item.get("category", "")).casefold():
        return f"고정된 state, action, compute budget에서 {tags} formulation이 task cost 또는 success를 유지하면서 perturbation 이후 recovery를 개선하는가?"
    return f"고정된 data·compute·action budget에서 {tags}를 사용하는 방법이 단순 baseline보다 paper task metric과 closed-loop robustness를 함께 개선하는가?"


def make_note(item: dict[str, object], old: str, overview: str, tracker: dict[str, dict[str, str]]) -> str:
    evidence = evidence_from(item, old, overview, tracker)
    old_sections = parse_sections(old)
    overview_sections = parse_sections(overview)
    cues = cue_values(old_sections, overview_sections)
    boundaries = old_boundaries(old_sections)
    research = old_research_use(old_sections)
    lineage = old_lineage(old_sections)
    reproduction = old_reproduction(old_sections)
    questions = old_questions(old_sections)
    position = loop_position(item)
    tags = tags_text(item)

    cue_lines: list[str] = []
    for label, value in cues:
        cue_lines.append(f"- **{label}:** {value}")
    if not cue_lines:
        cue_lines.append("- Available source material does not yet establish a paper-specific contribution; verify the abstract/full text before treating this as a conclusion.")

    boundary_lines = [f"- {value}" for value in boundaries[:6]]
    if len(boundary_lines) == 1:
        boundary_lines.insert(0, "- Explicit assumptions and negative results are not recorded in the current source note; full-text review is required.")

    research_lines = [f"- **Closed-loop position:** `{position}`.", f"- **Registry interface:** `{tags}` is the paper's recorded topic/interface, not evidence that the full robotics loop was evaluated."]
    if research:
        research_lines.append("- **Prior interpretation carried forward:**")
        research_lines.extend(f"  - {value}" for value in research[:5])
    research_lines.append("- Reuse the paper by preserving its input/output boundary and testing downstream success, failure, and latency under a matched baseline budget.")

    dependency_lines: list[str] = []
    if lineage:
        dependency_lines.extend(f"- {value}" for value in lineage[:4])
        dependency_lines.append("- The recorded arrow is a reading dependency, not a confirmed citation relationship unless the references are checked.")
    else:
        dependency_lines.append(f"- Registry position: `{item.get('category', 'unclassified')}`; tags: `{tags}`.")
        dependency_lines.append("- A direct citation predecessor/successor is not recorded in the legacy note; confirm it from references and the track synthesis before asserting lineage.")

    scope = useful_lines(first_section(old_sections, "이 논문이 끝난 지점", "Future Work"))
    if scope:
        dependency_lines.append("- Recorded scope boundary/future cue:")
        dependency_lines.extend(f"  - {value}" for value in scope[:4])

    reproduction_lines: list[str] = []
    if reproduction:
        reproduction_lines.append("- **Protocol carried forward from the legacy note (candidate, not a verified paper evaluation):**")
        reproduction_lines.extend(f"  - {value}" for value in reproduction[:8])
    else:
        reproduction_lines.extend(
            [
                "1. Confirm the paper-reported input, output, task, metric, baseline, and split from the full text.",
                "2. Implement the smallest paper-specific component and a simpler matched baseline.",
                "3. Evaluate the primary paper metric plus failure rate, latency, and sensitivity to the assumption most central to the method.",
            ]
        )
    reproduction_lines.append("- Do not label a candidate benchmark, metric, or extension protocol as the paper's own evaluation until the experiment section is checked.")

    question = make_question(item, questions, position)
    reject = "**Reject the hypothesis if** the primary metric does not improve at a matched budget, or if the method adds latency, failure, or assumption sensitivity without a compensating closed-loop benefit."

    return (
        f"# Insights — {item['title']}\n\n"
        "> Canonical metadata: [01_overview.md](./01_overview.md).\n"
        f"> Evidence maturity: `{evidence}`.\n"
        f"> Analysis basis: {source_basis(evidence, overview, old)}\n\n"
        "## Paper-supported conclusion\n\n"
        f"> **Evidence boundary:** {evidence_boundary(evidence)}\n\n"
        "### What was actually new\n\n"
        + "\n".join(cue_lines)
        + "\n\n### Strongest assumption and failure boundary\n\n"
        + "\n".join(boundary_lines)
        + "\n\n## Researcher interpretation\n\n"
        + "### Reusable lesson in the robotics loop\n\n"
        + "\n".join(research_lines)
        + "\n\n### Dependency and evolution\n\n"
        + "\n".join(dependency_lines)
        + "\n\n### Minimal reproduction\n\n"
        + "\n".join(reproduction_lines)
        + "\n\n## Falsifiable research question\n\n"
        + question
        + "\n\n"
        + reject
        + "\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write migrated notes; default is a dry run")
    parser.add_argument("--show", type=int, default=0, help="show the first N generated notes in dry-run mode")
    parser.add_argument("--sync-evidence", action="store_true", help="also align existing modern note headers with tracker evidence")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    tracker = read_tracker()
    counts = Counter()
    modern = 0
    changed = 0
    previews: list[str] = []

    for item in manifest:
        folder = resolve_folder(str(item["folder"]))
        note_path = folder / "05_insights.md"
        overview_path = folder / "01_overview.md"
        old = note_path.read_text(encoding="utf-8")
        overview = overview_path.read_text(encoding="utf-8")
        if is_modern(old):
            if args.sync_evidence:
                evidence = evidence_from(item, old, overview, tracker)
                new = sync_tracker_evidence(old, evidence)
                new = sync_generated_basis(new, evidence, overview)
                new = cleanup_generated_note(new)
                new = sync_generated_boundary(new, evidence)
                if new != old:
                    changed += 1
                    counts[evidence] += 1
                    if args.apply:
                        note_path.write_text(new, encoding="utf-8")
                    continue
            modern += 1
            counts["kept_modern"] += 1
            continue
        new = make_note(item, old, overview, tracker)
        evidence = extract_evidence(new) or "MISSING"
        counts[evidence] += 1
        changed += int(new != old)
        if args.show and len(previews) < args.show:
            previews.append(f"--- {note_path}\n{new}")
        if args.apply and new != old:
            note_path.write_text(new, encoding="utf-8")

    mode = "apply" if args.apply else "dry-run"
    print({"mode": mode, "registry_papers": len(manifest), "kept_modern": modern, "to_update": changed, "evidence_after_migration": dict(counts)})
    for preview in previews:
        print(preview)


if __name__ == "__main__":
    main()
