#!/usr/bin/env python3
"""Regenerate per-paper notes from local PDF text cues.

This intentionally avoids survey-keyword templates.  When the script cannot
extract a reliable cue from the paper text, it writes an explicit manual-review
marker instead of inventing content.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER_MD = ROOT / "PAPER.md"
REPORT_JSON = ROOT / "survey_work" / "note_audit_report.json"
TODAY = datetime.now().strftime("%Y-%m-%d")


@dataclass
class PaperEntry:
    year: str
    venue: str
    title: str
    category: str
    tags: str
    overview_path: Path
    pdf_link: str
    project: str

    @property
    def folder(self) -> Path:
        return (ROOT / self.overview_path).parent

    @property
    def pdf_path(self) -> Path:
        return self.folder / "paper.pdf"


DATASETS = [
    "WMT 2014",
    "ImageNet",
    "COCO",
    "ScanNet",
    "ScanNet200",
    "S3DIS",
    "Matterport3D",
    "Replica",
    "3RScan",
    "KITTI",
    "SemanticKITTI",
    "nuScenes",
    "Waymo",
    "Argoverse",
    "Occ3D",
    "ModelNet40",
    "ShapeNet",
    "ShapeNetPart",
    "Objaverse",
    "PartNet",
    "PartNet-Mobility",
    "DTU",
    "CO3D",
    "Tanks and Temples",
    "ETH3D",
    "TUM RGB-D",
    "EuRoC",
    "Habitat",
    "HM3D",
    "AI2-THOR",
    "R2R",
    "RxR",
    "VLN-CE",
    "RLBench",
    "CALVIN",
    "LIBERO",
    "ManiSkill",
    "BridgeData",
    "Open X-Embodiment",
    "RoboTwin",
    "VLABench",
    "EmbodiedScan",
    "EmbodiedBench",
    "ScanRefer",
    "ReferIt3D",
    "Nr3D",
    "Sr3D",
    "SQA3D",
    "ScanQA",
    "LERF",
]

METRICS = [
    "BLEU",
    "accuracy",
    "mIoU",
    "IoU",
    "AP",
    "mAP",
    "NDS",
    "Chamfer",
    "F-score",
    "PSNR",
    "SSIM",
    "LPIPS",
    "ATE",
    "RPE",
    "AbsRel",
    "RMSE",
    "SPL",
    "SR",
    "nDTW",
    "success rate",
    "collision",
    "ADE",
    "FDE",
    "ECE",
    "AUROC",
]

PROBLEM_WORDS = [
    "problem",
    "challenge",
    "limitation",
    "existing",
    "prior work",
    "prior methods",
    "previous work",
    "difficult",
    "bottleneck",
    "lack",
    "fail",
    "cost",
    "expensive",
    "sequential",
    "sparse",
    "ambiguous",
    "hallucination",
]

METHOD_WORDS = [
    "we propose",
    "we present",
    "we introduce",
    "we develop",
    "our method",
    "our approach",
    "we use",
    "consists",
    "architecture",
    "training",
    "loss function",
    "training objective",
    "attention",
    "transformer",
    "diffusion",
    "gaussian",
    "encoder",
    "decoder",
]

METHOD_HEADINGS = [
    "Model Architecture",
    "Proposed Method",
    "Our Method",
    "Method",
    "Methods",
    "Approach",
    "Methodology",
    "Architecture",
    "Framework",
]

AUTHOR_FOOTNOTE_BREAK = re.compile(
    r"(?i)(?:[*∗†‡]\s*)*(?:equal contribution|listing order is random|work performed while)"
)

RESULT_WORDS = [
    "achieve",
    "outperform",
    "state-of-the-art",
    "improve",
    "results",
    "experiments",
    "demonstrate",
    "show",
    "evaluate",
    "benchmark",
    "ablation",
]

LIMIT_WORDS = [
    "limitation",
    "future work",
    "failure",
    "fail",
    "cannot",
    "does not",
    "remains",
    "challenge",
    "discussion",
]


def split_md_table_row(line: str) -> list[str]:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return cells


def strip_md_link(text: str) -> tuple[str, str]:
    match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", text)
    if not match:
        return text.strip(), ""
    return match.group(1).strip(), match.group(2).strip()


def parse_registry() -> list[PaperEntry]:
    entries: list[PaperEntry] = []
    category = ""
    for line in PAPER_MD.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            category = line[3:].strip()
            continue
        if not re.match(r"^\|\s*\d{4}\s*\|", line):
            continue
        cells = split_md_table_row(line)
        if len(cells) < 6:
            continue
        title, overview = strip_md_link(cells[2])
        _, pdf = strip_md_link(cells[4])
        _, project = strip_md_link(cells[5])
        if not project:
            project = cells[5].strip()
        entries.append(
            PaperEntry(
                year=cells[0],
                venue=cells[1],
                title=title,
                category=category,
                tags=cells[3],
                overview_path=Path(overview),
                pdf_link=pdf,
                project=project,
            )
        )
    return entries


def pdf_to_text(pdf_path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", str(pdf_path), "-"],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=90,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"pdftotext failed: {pdf_path}")
    return result.stdout


def normalize_text(text: str) -> str:
    text = "".join(ch if ch in "\n\t\r" or ord(ch) >= 32 else " " for ch in text)
    text = text.replace("\x0c", "\n")
    text = re.sub(r"(?<=\w)-\n(?=\w)", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def truncate_back_matter(text: str) -> str:
    """Drop references, acknowledgements, and appendices before cue extraction."""
    matches = re.finditer(
        r"(?im)^\s*(?:\d+(?:\.\d+)*\s+)?(?:references|acknowledg(?:e)?ments|appendix|appendices|supplementary material)\s*$",
        text,
    )
    cut_points = [match.start() for match in matches if match.start() > 2000]
    if not cut_points:
        return text
    return text[: min(cut_points)].strip()


def find_next_section_break(text: str, start: int, max_chars: int) -> int:
    end = min(len(text), start + max_chars)
    chunk = text[start:end]
    direct = re.search(
        r"(?im)^\s*(?:[1-9]\d*\s+[A-Z][^\n]{2,100}|References|Acknowledg(?:e)?ments|Appendix)\s*$",
        chunk,
    )
    candidates = [direct.start() if direct else None]

    lines = list(re.finditer(r"(?m)^.*$", chunk))
    for idx, line_match in enumerate(lines):
        line = line_match.group(0).strip()
        if not re.fullmatch(r"[1-9]\d*", line):
            continue
        next_line = ""
        for next_match in lines[idx + 1 : idx + 5]:
            candidate = next_match.group(0).strip()
            if candidate:
                next_line = candidate
                break
        if not next_line:
            continue
        if re.match(r"(?i)^(figure|table|algorithm)\b", next_line):
            continue
        if 2 <= len(next_line.split()) <= 12 and re.match(r"[A-Z]", next_line):
            candidates.append(line_match.start())
            break

    valid = [pos for pos in candidates if pos is not None and pos > 200]
    if valid:
        return start + min(valid)
    return end


def find_heading_window(text: str, headings: list[str], max_chars: int = 7000) -> str:
    patterns = []
    for heading in headings:
        escaped = re.escape(heading)
        patterns.append(rf"(?im)^\s*(?:\d+(?:\.\d+)*\s+)?{escaped}\s*$")
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            start = match.end()
            end = find_next_section_break(text, start, max_chars)
            return text[start:end]
    return ""


def extract_abstract(text: str) -> str:
    match = re.search(
        r"(?is)\babstract\b\s*(.*?)(?:\n\s*(?:1\s+)?introduction\b|\n\s*keywords\b|\n\s*index terms\b)",
        text,
    )
    if match:
        return clean_abstract_body(match.group(1))
    match = re.search(r"(?is)\babstract\b\s*(.{400,2500})", text)
    return clean_abstract_body(match.group(1)) if match else ""


def clean_abstract_body(body: str) -> str:
    body = AUTHOR_FOOTNOTE_BREAK.split(body.strip(), maxsplit=1)[0]
    cleaned_lines = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            cleaned_lines.append("")
            continue
        low = stripped.lower()
        if re.match(r"^[*∗†‡]\s*(corresponding authors?|correspondence|contact)\b", low):
            continue
        if re.fullmatch(r"(?:\([A-D]\)\s*)?[^.]{0,80}(?:representation|front view|top view|side view|image|rgb|depth|tokens?|visual encoder|mllm|bev|map)", low):
            continue
        if re.fullmatch(r"[0-9]+", low):
            continue
        cleaned_lines.append(stripped)
    body = "\n".join(cleaned_lines)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body


def sentence_split(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text)
    clean = re.sub(r"\[[0-9,\s-]+\]", "", clean)
    clean = re.sub(r"[*∗†‡]\s*equal contribution\..*?(?=\b(?:1\s+)?introduction\b)", "", clean, flags=re.I)
    clean = re.sub(r"[*∗†‡]\s*work performed while.*?(?=\b(?:1\s+)?introduction\b)", "", clean, flags=re.I)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", clean)
    out = []
    for part in parts:
        part = part.strip()
        if len(part) < 35:
            continue
        if re.search(r"^(figure|table|appendix|references)\b", part, re.I):
            continue
        if part.count("…") >= 3:
            continue
        if re.search(r"\([A-D]\).*\([A-D]\)", part) and re.search(
            r"\b(illustration|visualization|example|overview|represent|framework)\b", part, re.I
        ):
            continue
        low = part.lower()
        if any(
            marker in low
            for marker in [
                "equal contribution",
                "listing order is random",
                "corresponding author",
                "work performed while",
                "token numbers represent",
                "we thank",
                "we are grateful",
                "was supported by",
                "is supported by",
                "funded by",
                "copyright",
                "published as a conference paper",
            ]
        ):
            continue
        out.append(part)
    return out


def score_sentence(sentence: str, keywords: list[str]) -> int:
    low = sentence.lower()
    score = 0
    matched = False
    for idx, keyword in enumerate(keywords):
        if keyword in low:
            matched = True
            score += max(1, len(keywords) - idx)
    if matched and ("we " in low or "our " in low):
        score += 2
    return score


def shorten(sentence: str, max_words: int = 28) -> str:
    sentence = "".join(ch if ch in "\n\t\r" or ord(ch) >= 32 else " " for ch in sentence)
    sentence = AUTHOR_FOOTNOTE_BREAK.split(sentence, maxsplit=1)[0]
    sentence = re.sub(r"\s+", " ", sentence).strip()
    words = sentence.split()
    if len(words) > max_words:
        sentence = " ".join(words[:max_words]) + " ..."
    return sentence.rstrip()


def first_sentence_cue(text: str, max_words: int = 45) -> list[str]:
    for sentence in sentence_split(text):
        cue = shorten(sentence, max_words=max_words)
        if cue:
            return [cue]
    return []


def select_cues(text: str, keywords: list[str], count: int = 3, max_words: int = 28) -> list[str]:
    sentences = sentence_split(text)
    scored = []
    for order, sentence in enumerate(sentences):
        score = score_sentence(sentence, keywords)
        if score > 0:
            scored.append((score, -order, sentence))
    scored.sort(reverse=True)
    cues = []
    seen = set()
    for _, _, sentence in scored:
        cue = shorten(sentence, max_words=max_words)
        if not cue:
            continue
        key = cue.lower()
        if key in seen:
            continue
        seen.add(key)
        cues.append(cue)
        if len(cues) >= count:
            break
    if cues:
        return cues
    return [shorten(s, max_words=max_words) for s in sentences[:count]]


def select_strict_cues(text: str, keywords: list[str], count: int = 3, max_words: int = 28) -> list[str]:
    sentences = sentence_split(text)
    scored = []
    for order, sentence in enumerate(sentences):
        score = score_sentence(sentence, keywords)
        if score > 0:
            scored.append((score, -order, sentence))
    scored.sort(reverse=True)
    cues = []
    seen = set()
    for _, _, sentence in scored:
        cue = shorten(sentence, max_words=max_words)
        if not cue:
            continue
        key = cue.lower()
        if key in seen:
            continue
        seen.add(key)
        cues.append(cue)
        if len(cues) >= count:
            break
    return cues


def select_problem_cues(primary: str, fallback: str, count: int = 3) -> list[str]:
    def is_result(sentence: str) -> bool:
        low = sentence.lower()
        return any(keyword in low for keyword in RESULT_WORDS)

    scored = []
    for order, sentence in enumerate(sentence_split(primary)):
        if is_result(sentence):
            continue
        score = score_sentence(sentence, PROBLEM_WORDS)
        if score > 0:
            scored.append((score, -order, sentence))
    scored.sort(reverse=True)
    cues = [shorten(sentence) for _, _, sentence in scored[:count]]
    if len(cues) >= count:
        return cues
    for cue in select_strict_cues(fallback, PROBLEM_WORDS, count=count - len(cues)):
        if cue not in cues:
            cues.append(cue)
    if cues:
        return cues
    return [shorten(s) for s in sentence_split(primary or fallback)[:count]]


def select_method_cues(text: str, count: int = 3) -> list[str]:
    scored = []
    for sentence in sentence_split(text):
        low = sentence.lower()
        has_method = any(keyword in low for keyword in METHOD_WORDS)
        has_result_only = any(keyword in low for keyword in RESULT_WORDS) and not any(
            keyword in low for keyword in ["we propose", "we present", "we introduce", "consists", "architecture", "attention", "encoder", "decoder"]
        )
        if has_method and not has_result_only:
            scored.append((score_sentence(sentence, METHOD_WORDS), sentence))
    scored.sort(reverse=True)
    cues = []
    seen = set()
    for _, sentence in scored:
        cue = shorten(sentence)
        if not cue:
            continue
        if cue.lower() in seen:
            continue
        seen.add(cue.lower())
        cues.append(cue)
        if len(cues) >= count:
            break
    return cues or select_cues(text, METHOD_WORDS, count=count)


def find_terms(text: str, terms: list[str]) -> list[str]:
    found = []
    for term in terms:
        pattern = rf"(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            found.append(term)
    return found


def bullet_list(items: list[str], fallback: str = "자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.") -> str:
    items = [str(item).strip() for item in items if str(item).strip()]
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)


def section_note(name: str, cues: list[str]) -> str:
    return f"## {name}\n{bullet_list(cues)}\n"


def clean_items(items: list[str] | str, limit: int | None = None) -> list[str]:
    if isinstance(items, str):
        values = [items]
    else:
        values = items
    cleaned = []
    seen = set()
    for item in values:
        item = re.sub(r"\s+", " ", str(item)).strip()
        if not item:
            continue
        key = item.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(item)
        if limit is not None and len(cleaned) >= limit:
            break
    return cleaned


def profile_for(entry: PaperEntry) -> dict[str, list[str] | str]:
    text = f"{entry.category} {entry.tags} {entry.title}".lower()

    profiles = [
        (
            ["vision-language-action", "vla", "robot manipulation", "action"],
            {
                "reuse": [
                    "Language-conditioned perception을 바로 action/policy token으로 연결하는 방식을 3D object state, affordance, contact-aware manipulation으로 확장할 수 있다.",
                    "2D image 중심 VLA가 놓치는 pose, metric distance, occlusion을 3D representation이나 scene memory로 보강하는 연구 질문으로 이어진다.",
                ],
                "gap": "robot action까지 보인 경우에도 3D state grounding, closed-loop correction, force/tactile feedback, unseen embodiment generalization은 별도 검증이 필요하다.",
                "questions": [
                    "3D geometry token을 VLA policy에 넣을 때 action success와 language following 중 어느 부분이 실제로 개선되는가?",
                    "open-vocabulary instruction과 metric manipulation constraint를 같은 representation에서 안정적으로 맞출 수 있는가?",
                    "long-horizon task에서 memory/action token이 누적될 때 failure recovery를 어떻게 설계할 수 있는가?",
                ],
                "eval_datasets": ["CALVIN", "LIBERO", "RLBench", "Open X-Embodiment"],
                "eval_metrics": ["success rate", "task completion", "generalization gap", "collision"],
                "verify": "language-conditioned manipulation success, unseen object/task generalization, closed-loop recovery를 확인한다.",
            },
        ),
        (
            ["navigation", "vln", "embodied ai", "semantic navigation"],
            {
                "reuse": [
                    "Language/semantic goal을 metric 3D map, BEV, scene graph, frontier/map memory와 연결해 navigation state representation으로 사용할 수 있다.",
                    "Navigation의 핵심 병목을 visual-language matching만이 아니라 spatial memory, localization, graph planning 문제로 재정의할 수 있다.",
                ],
                "gap": "navigation 성능을 보인 뒤에도 geometry-aware memory의 누적 오류, unseen scene transfer, semantic grounding failure는 후속 연구 지점으로 남는다.",
                "questions": [
                    "3D map/scene graph/gaussian map 중 어떤 representation이 language/semantic goal following에 가장 안정적인가?",
                    "semantic goal grounding과 metric path planning을 분리해야 하는가, 아니면 end-to-end로 결합해야 하는가?",
                    "online exploration 중 잘못된 language grounding을 어떻게 감지하고 수정할 수 있는가?",
                ],
                "eval_datasets": ["R2R", "RxR", "VLN-CE", "Habitat"],
                "eval_metrics": ["SR", "SPL", "nDTW", "collision"],
                "verify": "instruction/semantic goal following, path efficiency, unseen environment generalization, online correction을 확인한다.",
            },
        ),
        (
            ["scene graph", "graph reasoning", "graph"],
            {
                "reuse": [
                    "Object, relation, room/scene hierarchy를 graph로 구조화해 3D perception 결과를 robot planning과 language reasoning에 넘기는 중간 표현으로 사용할 수 있다.",
                    "관계 중심 표현은 단일 object detection보다 task-relevant affordance, spatial relation, commonsense reasoning을 붙이기 쉽다.",
                ],
                "gap": "static scene graph 품질을 보인 뒤에도 dynamic updates, uncertainty, open-vocabulary relation grounding, robot action coupling은 별도 문제로 남는다.",
                "questions": [
                    "3D scene graph의 node/edge uncertainty를 planning cost나 action selection에 어떻게 반영할 수 있는가?",
                    "language query에 필요한 relation만 선택적으로 구성하면 dense graph보다 효율과 성능이 개선되는가?",
                    "dynamic manipulation/navigation 중 graph를 어떻게 갱신해야 consistency가 유지되는가?",
                ],
                "eval_datasets": ["ScanNet", "3RScan", "Matterport3D"],
                "eval_metrics": ["mIoU", "Recall@K", "relation accuracy", "task success"],
                "verify": "relation prediction, open-vocabulary grounding, downstream planning utility를 확인한다.",
            },
        ),
        (
            ["gaussian", "nerf", "neural field", "scene representations", "radiance"],
            {
                "reuse": [
                    "Differentiable 3D scene representation을 semantic map, view synthesis, robot memory, planning cost field로 재사용할 수 있다.",
                    "Geometry와 appearance를 함께 담는 표현은 language feature, object identity, dynamic state를 붙이는 기반이 된다.",
                ],
                "gap": "reconstruction/view synthesis 품질을 보인 뒤에도 real-time update, semantic consistency, dynamic interaction, robot-safe planning은 후속 과제로 남는다.",
                "questions": [
                    "Gaussian/NeRF field에 language feature를 붙일 때 3D consistency와 open-vocabulary retrieval을 동시에 유지할 수 있는가?",
                    "robot이 움직이며 갱신하는 online field에서 drift와 hallucinated semantics를 어떻게 줄일 수 있는가?",
                    "rendering quality가 실제 navigation/manipulation success로 이어지는 조건은 무엇인가?",
                ],
                "eval_datasets": ["Replica", "ScanNet", "Mip-NeRF 360", "Tanks and Temples"],
                "eval_metrics": ["PSNR", "SSIM", "LPIPS", "mIoU"],
                "verify": "view synthesis 품질뿐 아니라 semantic querying, map update, robot task success를 같이 확인한다.",
            },
        ),
        (
            ["diffusion", "generation", "generative"],
            {
                "reuse": [
                    "Diffusion/generative prior를 sparse observation completion, 3D scene/object generation, action trajectory proposal에 사용할 수 있다.",
                    "생성 모델의 prior는 부족한 geometry나 demonstration을 보완하지만, physical feasibility와 metric correctness를 별도 제약으로 확인해야 한다.",
                ],
                "gap": "visual/shape generation 품질 이후에도 geometry correctness, controllability, physical plausibility, robot execution 가능성은 남는다.",
                "questions": [
                    "2D/3D diffusion prior가 실제 3D reconstruction이나 planning에서 metric error를 줄이는가, 아니면 plausible hallucination을 늘리는가?",
                    "language-conditioned generation 결과를 robot execution constraint로 어떻게 검증하고 거를 수 있는가?",
                    "generated scene/action 후보의 uncertainty를 downstream planner에 어떻게 전달할 수 있는가?",
                ],
                "eval_datasets": ["ShapeNet", "Objaverse", "ScanNet", "RLBench"],
                "eval_metrics": ["Chamfer", "F-score", "CLIP score", "success rate"],
                "verify": "generation fidelity, geometric validity, physical feasibility, downstream task utility를 함께 확인한다.",
            },
        ),
        (
            ["equivariance", "equivariant", "se3", "registration", "calibration"],
            {
                "reuse": [
                    "SE(3)/rotation/translation structure를 representation이나 policy에 넣어 viewpoint, pose, sensor-frame 변화에 강한 3D reasoning을 만들 수 있다.",
                    "Registration/calibration 관점은 multi-view, LiDAR-camera, robot-camera alignment 문제의 공통 기반으로 사용할 수 있다.",
                ],
                "gap": "symmetry-aware representation이 특정 task에서 성능을 보인 뒤에도 large-scale scene, language grounding, real robot noise에서의 이득은 별도 검증이 필요하다.",
                "questions": [
                    "SE(3)-equivariant feature가 open-vocabulary 3D grounding이나 manipulation policy에서도 실제 sample efficiency를 높이는가?",
                    "learned alignment와 classical calibration/registration을 결합하면 sensor drift와 domain shift를 줄일 수 있는가?",
                    "equivariance constraint가 language-conditioned tasks에서 오히려 semantic flexibility를 제한하지 않는가?",
                ],
                "eval_datasets": ["ModelNet40", "ScanNet", "KITTI", "nuScenes"],
                "eval_metrics": ["rotation error", "translation error", "mIoU", "success rate"],
                "verify": "pose robustness, calibration/registration accuracy, downstream perception/action 성능을 확인한다.",
            },
        ),
        (
            ["sensor fusion", "lidar", "occupancy", "autonomous", "bev", "detection"],
            {
                "reuse": [
                    "Camera/LiDAR/Radar/BEV/occupancy representation을 robot 또는 autonomous agent의 metric world model로 사용할 수 있다.",
                    "Sensor fusion의 핵심은 modality-specific noise와 calibration error를 줄이면서 semantics와 geometry를 같은 map으로 정렬하는 것이다.",
                ],
                "gap": "perception benchmark 성능 이후에도 open-vocabulary semantics, online calibration, planning-aware uncertainty는 후속 연구 지점으로 남는다.",
                "questions": [
                    "multi-sensor 3D representation에 language/semantic feature를 붙이면 planning-relevant perception이 실제로 개선되는가?",
                    "calibration error나 missing modality 상황에서 fusion model의 uncertainty를 어떻게 표현하고 사용할 수 있는가?",
                    "occupancy/BEV representation을 navigation/manipulation planner가 바로 쓰기 좋은 구조로 바꿀 수 있는가?",
                ],
                "eval_datasets": ["nuScenes", "Waymo", "KITTI", "Occ3D"],
                "eval_metrics": ["mAP", "NDS", "IoU", "mIoU"],
                "verify": "detection/occupancy 성능, robustness, calibration sensitivity, planning utility를 확인한다.",
            },
        ),
        (
            ["vision-language grounding", "open-vocabulary", "semantic understanding", "alignment", "language-embedded"],
            {
                "reuse": [
                    "2D vision-language feature를 3D object/point/field/map에 정렬해 open-vocabulary querying과 semantic grounding에 사용할 수 있다.",
                    "핵심은 language prior를 3D metric structure와 맞추면서 view inconsistency와 hallucination을 줄이는 것이다.",
                ],
                "gap": "open-vocabulary recognition이나 grounding을 보인 뒤에도 3D consistency, ambiguous reference resolution, robot-action relevance는 남는다.",
                "questions": [
                    "2D VLM feature를 3D로 lift할 때 multi-view consistency와 fine-grained object boundary를 동시에 유지할 수 있는가?",
                    "language query가 robot action에 필요한 geometry/affordance까지 정확히 가리키는지 어떻게 평가할 수 있는가?",
                    "semantic confidence와 geometric uncertainty를 함께 쓰면 false grounding을 줄일 수 있는가?",
                ],
                "eval_datasets": ["ScanNet", "ScanRefer", "ReferIt3D", "SQA3D"],
                "eval_metrics": ["mIoU", "Acc@0.25", "Acc@0.5", "Recall@K"],
                "verify": "open-vocabulary segmentation/localization, 3D consistency, task-relevant grounding을 확인한다.",
            },
        ),
        (
            ["large multimodal", "3d-llm", "spatial llm", "3d spatial"],
            {
                "reuse": [
                    "3D observation을 language model이 다룰 수 있는 token/memory/query interface로 바꾸는 방식을 spatial reasoning과 embodied planning에 사용할 수 있다.",
                    "LLM/VLM의 commonsense를 쓰되, 3D geometry가 제공하는 metric constraint로 hallucination을 제어하는 방향이 중요하다.",
                ],
                "gap": "3D QA/reasoning 성능 이후에도 metric grounding, benchmark leakage, embodied action validation은 별도 검증이 필요하다.",
                "questions": [
                    "LLM이 답한 spatial reasoning이 실제 3D metric relation과 일치하는지 어떻게 자동 검증할 수 있는가?",
                    "3D scene token과 language token 사이 alignment를 dense annotation 없이 학습할 수 있는가?",
                    "reasoning output을 robot planner/action policy로 넘길 때 필요한 intermediate representation은 무엇인가?",
                ],
                "eval_datasets": ["ScanNet", "SQA3D", "EmbodiedScan", "Matterport3D"],
                "eval_metrics": ["accuracy", "mIoU", "grounding accuracy", "task success"],
                "verify": "3D spatial reasoning, answer grounding, embodied task transfer를 확인한다.",
            },
        ),
        (
            ["transformer", "language models", "bert", "chain-of-thought"],
            {
                "reuse": [
                    "Attention 기반 token interaction을 3D object, scene, map, trajectory token 사이의 long-range relation modeling에 사용할 수 있다.",
                    "Sequence modeling의 병렬화/장거리 의존성 처리를 embodied memory, planning history, multi-view observation aggregation으로 확장할 수 있다.",
                ],
                "gap": "원 논문이 sequence/language task에서 보인 구조는 metric 3D geometry, SE(3) consistency, sensor noise, robot execution constraint를 직접 다루지 않는다.",
                "questions": [
                    "3D point/object/map/action token에 attention을 적용할 때 어떤 positional encoding이 metric geometry를 보존하는가?",
                    "long-horizon embodied task에서 full attention, sparse attention, graph attention 중 무엇이 memory와 planning에 유리한가?",
                    "language reasoning token과 3D geometry token을 어떤 intermediate representation으로 정렬해야 hallucination을 줄일 수 있는가?",
                ],
                "eval_datasets": ["ScanNet", "Matterport3D", "R2R", "CALVIN"],
                "eval_metrics": ["accuracy", "mIoU", "SR", "success rate"],
                "verify": "3D relation reasoning, spatial memory, language-conditioned planning 성능을 확인한다.",
            },
        ),
        (
            ["vision foundation", "segment anything", "dino", "mae", "clip", "blip", "align"],
            {
                "reuse": [
                    "Large-scale pretraining feature를 3D perception의 initialization, pseudo-label, open-vocabulary semantic prior로 사용할 수 있다.",
                    "2D foundation model의 강한 recognition prior를 3D consistency, view aggregation, robot task relevance로 재해석해야 한다.",
                ],
                "gap": "2D/vision-language representation 성능 이후에도 3D metric alignment, temporal consistency, robot interaction feedback은 별도 문제로 남는다.",
                "questions": [
                    "2D foundation feature를 3D point/gaussian/map에 정렬할 때 어떤 consistency loss나 aggregation이 가장 안정적인가?",
                    "segmentation/recognition prior가 affordance나 manipulation success까지 설명하는가?",
                    "foundation model confidence를 3D map uncertainty로 변환해 active perception에 사용할 수 있는가?",
                ],
                "eval_datasets": ["ImageNet", "COCO", "ScanNet", "S3DIS"],
                "eval_metrics": ["accuracy", "mIoU", "Recall@K", "success rate"],
                "verify": "2D recognition transfer, 3D semantic consistency, downstream robotics utility를 확인한다.",
            },
        ),
        (
            ["slam", "reconstruction", "geometry", "monocular", "depth", "sfm"],
            {
                "reuse": [
                    "Geometry reconstruction, pose estimation, map update 원리를 robot의 spatial memory와 3D scene understanding 기반으로 사용할 수 있다.",
                    "Classical geometry/SLAM의 metric constraint는 VLM/LLM 기반 semantic reasoning이 놓치는 scale, pose, visibility 문제를 보정한다.",
                ],
                "gap": "geometric accuracy 이후에도 open-vocabulary semantics, dynamic objects, learned priors, task-aware mapping은 후속 연구 지점으로 남는다.",
                "questions": [
                    "SLAM/reconstruction map에 language-aligned semantic feature를 붙여도 geometric consistency가 유지되는가?",
                    "learned depth/geometry prior와 online sensor measurement를 어떻게 결합해야 drift와 hallucination을 줄일 수 있는가?",
                    "robot task success에 필요한 map detail은 reconstruction metric과 어떻게 다른가?",
                ],
                "eval_datasets": ["TUM RGB-D", "EuRoC", "KITTI", "ScanNet"],
                "eval_metrics": ["ATE", "RPE", "AbsRel", "RMSE"],
                "verify": "pose/reconstruction accuracy, semantic map consistency, robot navigation/manipulation utility를 확인한다.",
            },
        ),
        (
            ["point cloud", "representation learning", "foundation models", "3d representation"],
            {
                "reuse": [
                    "Point/voxel/patch-level 3D representation을 downstream segmentation, grounding, manipulation state encoding의 backbone으로 사용할 수 있다.",
                    "Self-supervised 또는 foundation-style 3D feature는 annotation-heavy 3D supervision을 줄이는 방향의 출발점이 된다.",
                ],
                "gap": "representation benchmark 성능 이후에도 language alignment, embodied interaction, dynamic scene transfer는 별도 검증이 필요하다.",
                "questions": [
                    "3D pretraining feature가 open-vocabulary grounding과 robot manipulation 모두에 transfer되는가?",
                    "geometry-only feature에 semantic/language supervision을 더할 때 어느 layer에서 alignment하는 것이 좋은가?",
                    "static point cloud benchmark 성능이 online robot perception에서도 유지되는가?",
                ],
                "eval_datasets": ["ModelNet40", "ShapeNet", "ScanNet", "S3DIS"],
                "eval_metrics": ["accuracy", "mIoU", "Chamfer", "success rate"],
                "verify": "3D representation transfer, semantic grounding, robot downstream performance를 확인한다.",
            },
        ),
        (
            ["benchmark", "dataset"],
            {
                "reuse": [
                    "Dataset/benchmark 설계 방식을 연구 아이디어의 evaluation protocol과 failure taxonomy를 잡는 기준으로 사용할 수 있다.",
                    "새 방법을 제안하기 전, 이 benchmark가 어떤 input, annotation, split, metric을 표준화했는지 확인해야 한다.",
                ],
                "gap": "benchmark는 task를 정의하지만, 실제 robot deployment나 open-world generalization을 완전히 대변하지 못할 수 있다.",
                "questions": [
                    "현재 benchmark metric이 3D CV 성능과 robotics task success 사이의 차이를 충분히 드러내는가?",
                    "새로운 representation/method가 train/test split이 아니라 scene/object/task shift에서 강한지 어떻게 확인할 수 있는가?",
                    "annotation schema가 language, geometry, action failure를 분리해서 분석할 수 있는가?",
                ],
                "eval_datasets": ["paper-defined benchmark"],
                "eval_metrics": ["paper-defined metrics", "generalization gap", "failure rate"],
                "verify": "benchmark coverage, split validity, metric-task alignment를 확인한다.",
            },
        ),
    ]

    for needles, profile in profiles:
        if any(needle in text for needle in needles):
            return profile

    return {
        "reuse": [
            "논문이 제안한 representation/method를 3D scene understanding과 robot decision-making 사이의 중간 표현으로 재해석할 수 있다.",
            "핵심 단서를 그대로 쓰기보다 geometry, semantics, action constraint 중 무엇을 보강해야 하는지 확인하는 출발점으로 삼는다.",
        ],
        "gap": "논문이 다룬 task 범위 밖의 3D consistency, robotics transfer, open-world generalization은 후속 연구 질문으로 남는다.",
        "questions": [
            "이 방법의 핵심 representation이 3D geometry와 semantic grounding을 동시에 보존하는가?",
            "동일한 idea가 online robot perception/action setting에서도 유지되는가?",
            "failure case가 data 부족, geometry mismatch, language ambiguity, policy limitation 중 어디에서 오는가?",
        ],
        "eval_datasets": ["ScanNet", "Matterport3D", "nuScenes", "CALVIN"],
        "eval_metrics": ["mIoU", "accuracy", "success rate", "generalization gap"],
        "verify": "paper task 성능과 3D/robotics downstream utility를 함께 확인한다.",
    }


def build_insights(entry: PaperEntry, extracted: dict[str, list[str] | str]) -> str:
    profile = profile_for(entry)
    problem_cues = clean_items(extracted["problem_cues"], limit=2)
    method_cues = clean_items(extracted["method_cues"], limit=2)
    result_cues = clean_items(extracted["result_cues"], limit=2)
    limitation_cues = clean_items(extracted["limitation_cues"], limit=2)
    future_cues = clean_items(extracted["future_cues"], limit=2)
    dataset_terms = clean_items(extracted["datasets"], limit=5)
    metric_terms = clean_items(extracted["metrics"], limit=5)

    core_concepts = []
    if method_cues:
        core_concepts.append(f"핵심 방법 단서: {method_cues[0]}")
    if problem_cues:
        core_concepts.append(f"출발 문제 단서: {problem_cues[0]}")
    if result_cues:
        core_concepts.append(f"주장된 효과 단서: {result_cues[0]}")

    reuse = clean_items(profile["reuse"], limit=3)
    research_use = [
        "위 paper-specific cue를 논문 claim으로만 두지 말고, 3D Vision + Robotics에서 representation, memory, planning 설계 원리로 재사용한다.",
        *reuse,
    ]

    endpoint = []
    if result_cues:
        endpoint.append(f"논문이 도달한 지점: {result_cues[0]}")
    if limitation_cues:
        endpoint.append(f"논문 내 한계/논의 단서: {limitation_cues[0]}")
    elif future_cues:
        endpoint.append(f"저자가 남긴 확장 방향: {future_cues[0]}")
    endpoint.append(str(profile["gap"]))

    extension_datasets = clean_items(profile["eval_datasets"], limit=5)
    extension_metrics = clean_items(profile["eval_metrics"], limit=5)
    experiment = [
        f"논문 내 evaluation 단서: {', '.join(dataset_terms) if dataset_terms else '자동 추출에서 명확한 dataset 단서 없음'} / {', '.join(metric_terms) if metric_terms else '자동 추출에서 명확한 metric 단서 없음'}",
        f"내 연구 확장 benchmark 후보: {', '.join(extension_datasets)}",
        f"내 연구 확장 metric 후보: {', '.join(extension_metrics)}",
        f"검증 초점: {profile['verify']}",
    ]

    evidence = []
    if problem_cues:
        evidence.append(f"Problem cue: {problem_cues[0]}")
    if method_cues:
        evidence.append(f"Method cue: {method_cues[0]}")
    if result_cues:
        evidence.append(f"Result cue: {result_cues[0]}")
    if not evidence:
        evidence.append("자동 추출 가능한 paper-specific cue가 부족하다. `paper.pdf`를 수동 확인해야 한다.")

    return f"""# Insights

## 이 논문에서 가져갈 핵심 개념
{bullet_list(core_concepts)}

## 내 연구 방향에서 어떻게 활용할 수 있나
{bullet_list(research_use)}

## 이 논문이 끝난 지점
{bullet_list(endpoint)}

## 다음 연구 질문
{bullet_list(clean_items(profile["questions"], limit=4))}

## 실험으로 확인할 방향
{bullet_list(experiment)}

## 주의할 점
- 이 파일의 활용 방향은 논문 claim이 아니라, 위 paper-specific cue를 3D Vision + Robotics 연구 방향으로 확장한 survey-level 해석이다.
- 논문 내 explicit limitation/future cue가 부족한 경우, 후속 질문은 method scope와 evaluation scope의 빈틈에서 도출했다.

## 근거가 되는 논문 단서
{bullet_list(evidence)}
"""


def paper_context(entry: PaperEntry) -> str:
    return (
        f"- Year/Venue: {entry.year} / {entry.venue}\n"
        f"- Category: {entry.category}\n"
        f"- Tags: {entry.tags}\n"
        f"- Paper link: {entry.pdf_link or 'local paper.pdf'}\n"
        f"- Code/Project: {entry.project or 'not identified'}\n"
        f"- Source audit: regenerated from local `paper.pdf` on {TODAY}; survey-keyword template text removed.\n"
    )


def write_notes(entry: PaperEntry, extracted: dict[str, list[str] | str]) -> None:
    abstract_cues = extracted["abstract_cues"]
    problem_cues = extracted["problem_cues"]
    method_cues = extracted["method_cues"]
    method_detail_cues = extracted["method_detail_cues"]
    evaluation_cues = extracted["evaluation_cues"]
    result_cues = extracted["result_cues"]
    limitation_cues = extracted["limitation_cues"]
    dataset_terms = extracted["datasets"]
    metric_terms = extracted["metrics"]
    abstract_text = extracted["abstract_text"]

    folder = entry.folder
    folder.mkdir(parents=True, exist_ok=True)

    overview = f"""# {entry.title}

{paper_context(entry)}
## Problem
{bullet_list(problem_cues)}

## Core Idea
{bullet_list(method_cues[:2])}

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
{bullet_list(result_cues)}

## Limitation
{bullet_list(limitation_cues)}

## Contribution
{bullet_list(abstract_cues)}

## Abstract Cue
{bullet_list(first_sentence_cue(abstract_text, max_words=45) if abstract_text else [])}
"""

    problem = f"""# Problem

{paper_context(entry)}
## 왜 문제인가
{bullet_list(problem_cues)}

## 해결하려는 문제
{bullet_list(abstract_cues)}

## 선행 연구 / 배경 단서
{bullet_list(extracted["intro_cues"])}
"""

    method = f"""# Method

{paper_context(entry)}
## Brief Method
{bullet_list(method_cues)}

## 원리적 동기
{bullet_list(problem_cues[:2] + method_cues[:1])}

## 핵심 방법론
{bullet_list(method_detail_cues)}
"""

    evaluation = f"""# Evaluation

{paper_context(entry)}
## Dataset / Benchmark
{bullet_list(dataset_terms)}

## Metrics
{bullet_list(metric_terms)}

## Evaluation Protocol and Results
{bullet_list(evaluation_cues + result_cues[:2])}

## Baselines
{bullet_list(extracted["baseline_cues"])}

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
"""

    insights = build_insights(entry, extracted)

    def clean_markdown(text: str) -> str:
        return "".join(ch if ch in "\n\t\r" or ord(ch) >= 32 else " " for ch in text)

    (folder / "01_overview.md").write_text(clean_markdown(overview), encoding="utf-8")
    (folder / "02_problem.md").write_text(clean_markdown(problem), encoding="utf-8")
    (folder / "03_method.md").write_text(clean_markdown(method), encoding="utf-8")
    (folder / "04_evaluation.md").write_text(clean_markdown(evaluation), encoding="utf-8")
    (folder / "05_insights.md").write_text(clean_markdown(insights), encoding="utf-8")


def extract_paper_cues(text: str) -> dict[str, list[str] | str]:
    text = truncate_back_matter(normalize_text(text))
    abstract = extract_abstract(text)
    intro = find_heading_window(text, ["Introduction"], max_chars=9000)
    method = find_heading_window(
        text,
        METHOD_HEADINGS,
        max_chars=12000,
    )
    evaluation = find_heading_window(
        text,
        [
            "Experiments",
            "Experiment",
            "Evaluation",
            "Experimental Results",
            "Results",
            "Benchmark",
        ],
        max_chars=12000,
    )
    conclusion = find_heading_window(
        text,
        ["Conclusion", "Conclusions", "Discussion", "Limitations", "Broader Impact"],
        max_chars=5000,
    )
    abstract_or_empty = abstract
    intro_or_abstract = intro or abstract
    method_fallback = method or intro
    method_or_abstract = " ".join(part for part in [abstract, method_fallback] if part)
    method_only = method_fallback
    eval_only = evaluation
    result_source = " ".join(part for part in [abstract, evaluation] if part)
    conclusion_or_empty = conclusion

    baseline_cues = (
        select_strict_cues(eval_only, ["baseline", "compare", "comparison", "previous", "state-of-the-art"], count=2)
        if eval_only
        else []
    )
    future_cues = select_strict_cues(conclusion_or_empty, ["future", "limitation", "remain", "could", "would", "challenge"], count=2) if conclusion_or_empty else []
    limitation_cues = select_strict_cues(conclusion_or_empty, LIMIT_WORDS, count=3) if conclusion_or_empty else []

    return {
        "abstract_text": abstract,
        "abstract_cues": select_cues(abstract_or_empty, METHOD_WORDS + RESULT_WORDS + PROBLEM_WORDS, count=3) if abstract_or_empty else [],
        "problem_cues": select_problem_cues(intro_or_abstract, abstract, count=3) if intro_or_abstract else [],
        "intro_cues": select_cues(intro, PROBLEM_WORDS + METHOD_WORDS, count=3) if intro else [],
        "method_cues": select_method_cues(method_or_abstract, count=3) if method_or_abstract else [],
        "method_detail_cues": select_method_cues(method_only, count=5) if method_only else [],
        "evaluation_cues": select_cues(eval_only, RESULT_WORDS, count=4) if eval_only else [],
        "result_cues": select_cues(result_source, RESULT_WORDS, count=3) if result_source else [],
        "limitation_cues": limitation_cues,
        "future_cues": future_cues,
        "baseline_cues": baseline_cues,
        "datasets": find_terms(text, DATASETS),
        "metrics": find_terms(text, METRICS),
    }


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    limit_arg = next((arg for arg in sys.argv if arg.startswith("--limit=")), None)
    limit = int(limit_arg.split("=", 1)[1]) if limit_arg else None
    only_arg = next((arg for arg in sys.argv if arg.startswith("--only=")), None)
    only = only_arg.split("=", 1)[1] if only_arg else None

    entries = parse_registry()
    if only:
        entries = [entry for entry in entries if only in str(entry.folder)]
    if limit is not None:
        entries = entries[:limit]

    report = {
        "date": TODAY,
        "dry_run": dry_run,
        "total_registry_entries_seen": len(entries),
        "processed": 0,
        "missing_pdf": [],
        "pdftotext_failed": [],
        "abstract_missing": [],
        "method_heading_missing": [],
        "evaluation_heading_missing": [],
    }

    for idx, entry in enumerate(entries, 1):
        if not entry.pdf_path.exists():
            report["missing_pdf"].append(str(entry.folder.relative_to(ROOT)))
            continue
        try:
            text = pdf_to_text(entry.pdf_path)
        except Exception as exc:  # noqa: BLE001
            report["pdftotext_failed"].append({"folder": str(entry.folder.relative_to(ROOT)), "error": str(exc)})
            continue
        normalized = truncate_back_matter(normalize_text(text))
        if not extract_abstract(normalized):
            report["abstract_missing"].append(str(entry.folder.relative_to(ROOT)))
        if not find_heading_window(
            normalized,
            METHOD_HEADINGS,
            max_chars=1000,
        ):
            report["method_heading_missing"].append(str(entry.folder.relative_to(ROOT)))
        if not find_heading_window(
            normalized,
            ["Experiments", "Experiment", "Evaluation", "Experimental Results", "Results", "Benchmark"],
            max_chars=1000,
        ):
            report["evaluation_heading_missing"].append(str(entry.folder.relative_to(ROOT)))
        extracted = extract_paper_cues(normalized)
        if not dry_run:
            write_notes(entry, extracted)
        report["processed"] += 1
        if idx % 50 == 0:
            print(f"processed {idx}/{len(entries)}", flush=True)

    if not dry_run:
        REPORT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
