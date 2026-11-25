#!/usr/bin/env python3
"""Build or audit the literature survey without destructive defaults.

Running this file without flags is read-only. Network metadata refresh, PDF
downloads, note replacement, registry replacement, and manifest replacement
must each be requested explicitly.
"""

from __future__ import annotations

import concurrent.futures
import argparse
import html
import json
import os
import re
import shutil
import subprocess
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

import requests

try:
    from taxonomy import canonicalize
    from registry_schema import enrich_record, next_paper_id
except ModuleNotFoundError:  # import as work.scripts.build_lit_survey
    from .taxonomy import canonicalize
    from .registry_schema import enrich_record, next_paper_id


ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "work"
SOURCES = WORK / "sources"
MANIFEST = SOURCES / "papers.json"
REGISTRY_META = SOURCES / "registry_meta.json"
HEADERS = {
    "User-Agent": "Mozilla/5.0 literature-survey-bot (academic personal use)"
}


KNOWN_DATASETS = [
    "ScanNet", "ScanNet200", "ScanRefer", "Nr3D", "Sr3D", "ReferIt3D", "ScanQA",
    "S3DIS", "Replica", "Matterport3D", "HM3D", "Habitat", "R2R", "RxR", "VLN-CE",
    "RLBench", "CALVIN", "LIBERO", "BridgeData", "Open X-Embodiment", "OXE",
    "Google Robot", "WidowX", "Ravens", "ManiSkill", "Meta-World", "nuScenes",
    "Waymo", "KITTI", "SemanticKITTI", "Argoverse", "nuPlan", "ScanScribe",
    "Objaverse", "ShapeNet", "COCO", "ImageNet", "LAION", "HSSD", "3R-Scan",
    "TUM RGB-D", "EuRoC", "ETH3D", "7-Scenes", "MegaDepth", "Map-free",
    "RealEstate10K", "DTU", "TartanAir", "SynGrasp", "SocialNav-SUB",
]

KNOWN_METRICS = [
    "Acc@0.25", "Acc@0.5", "mIoU", "IoU", "AP", "mAP", "success rate", "SR",
    "SPL", "nDTW", "RGS", "BLEU", "CIDEr", "ROUGE", "METEOR", "EM", "F1",
    "PSNR", "SSIM", "LPIPS", "ATE", "RPE", "AUC", "Chamfer", "F-score",
    "translation error", "rotation error", "completion rate", "episode length",
]


def clean_text(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def safe_slug(value: str, max_len: int = 58) -> str:
    replacements = {
        "π": "pi",
        "$": "",
        "^": "",
        "{": "",
        "}": "",
        "\\": "",
        "/": "-",
        ":": "",
        ";": "",
        ",": "",
        "?": "",
        "!": "",
        "(": "",
        ")": "",
        "[": "",
        "]": "",
        "&": "and",
    }
    for k, v in replacements.items():
        value = value.replace(k, v)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^A-Za-z0-9.+-]+", "-", value).strip("-")
    value = re.sub(r"-+", "-", value)
    return value[:max_len].rstrip("-") or "paper"


def venue_without_year(value: str) -> str:
    value = re.sub(r"\b20\d{2}\b", "", value or "")
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -_/")


def venue_bucket(value: str) -> str:
    value = venue_without_year(value)
    value = re.sub(r"\b(SpotlightPoster|Poster|Spotlight|Oral|regular)\b", "", value, flags=re.I)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -_/") or "venue"


def folder_name(paper: dict) -> str:
    short = paper.get("short") or safe_slug(paper["title"])
    venue = safe_slug(venue_bucket(paper["venue"]), 24)
    return f"{paper['year']}/{venue}/{paper['year']}_{venue}_{short}"


def venue_display(value: str) -> str:
    label = venue_without_year(value)
    label = re.sub(r"\bSpotlightPoster\b", "Spotlight/Poster", label, flags=re.I)
    label = re.sub(r"\bregular\b", "", label, flags=re.I)
    label = re.sub(r"\s+", " ", label)
    return label.strip(" -_/") or value


def venue_for_registry(value: str) -> str:
    return venue_display(value)



def fetch(url: str, timeout: int = 25) -> str:
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout)
        if r.status_code == 200:
            return r.text
    except Exception:
        pass
    return ""


def fetch_arxiv_metadata(papers: list[dict]) -> None:
    arxiv_papers = [p for p in papers if p.get("arxiv")]
    for i in range(0, len(arxiv_papers), 50):
        batch = arxiv_papers[i : i + 50]
        ids = ",".join(p["arxiv"] for p in batch)
        url = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(ids)
        try:
            r = requests.get(url, headers=HEADERS, timeout=30)
            if r.status_code != 200:
                continue
            root = ET.fromstring(r.content)
            ns = {"a": "http://www.w3.org/2005/Atom"}
            by_id = {}
            for entry in root.findall("a:entry", ns):
                eid = entry.findtext("a:id", default="", namespaces=ns).split("/")[-1]
                eid = re.sub(r"v\d+$", "", eid)
                by_id[eid] = {
                    "abstract": clean_text(entry.findtext("a:summary", default="", namespaces=ns)),
                    "authors": ", ".join(a.findtext("a:name", default="", namespaces=ns) for a in entry.findall("a:author", ns)[:6]),
                }
            for p in batch:
                meta = by_id.get(p["arxiv"])
                if meta:
                    p.update({k: v for k, v in meta.items() if v})
        except Exception as exc:
            print(f"[warn] arxiv metadata failed: {exc}")
        time.sleep(1.0)


def fetch_page_metadata(p: dict) -> None:
    if p.get("abstract") or not p.get("page"):
        return
    page = p.get("page", "")
    if any(host in page for host in ["openaccess.thecvf.com", "ecva.net", "openreview.net", "3dvconf.github.io"]):
        return
    text = fetch(p["page"])
    if not text:
        return
    abstract = ""
    m = re.search(r'<div id="abstract">\s*(.*?)\s*</div>', text, re.S)
    if m:
        abstract = clean_text(m.group(1))
    if not abstract:
        m = re.search(r"abstract\s*=\s*\{(.*?)\}\s*[,}]", text, re.S)
        if m:
            abstract = clean_text(m.group(1))
    if not abstract:
        m = re.search(r'<p class="abstract">(.*?)</p>', text, re.S)
        if m:
            abstract = clean_text(m.group(1))
    if abstract:
        p["abstract"] = abstract
    if not p.get("authors"):
        m = re.search(r'<div id="authors">(.*?)</div>', text, re.S)
        if m:
            p["authors"] = clean_text(m.group(1))


def download_pdf(p: dict) -> dict:
    out_dir = ROOT / folder_name(p)
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = out_dir / "paper.pdf"
    error_path = out_dir / "paper_pdf_error.txt"
    p["folder"] = str(out_dir.relative_to(ROOT))
    if pdf_path.exists() and pdf_path.stat().st_size > 20_000:
        error_path.unlink(missing_ok=True)
        p["pdf_status"] = "downloaded"
        return p
    url = p.get("pdf")
    if not url:
        (out_dir / "paper_pdf_error.txt").write_text("No PDF URL identified.\n", encoding="utf-8")
        p["pdf_status"] = "missing-url"
        return p
    try:
        request_headers = {} if p.get("download_without_user_agent") else HEADERS
        with requests.get(url, headers=request_headers, timeout=45, stream=True, allow_redirects=True) as r:
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code}")
            tmp = pdf_path.with_suffix(".pdf.tmp")
            with tmp.open("wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 64):
                    if chunk:
                        f.write(chunk)
            data = tmp.read_bytes()[:4]
            if data != b"%PDF" or tmp.stat().st_size < 20_000:
                raise RuntimeError("downloaded file is not a valid PDF")
            tmp.replace(pdf_path)
            error_path.unlink(missing_ok=True)
            p["pdf_status"] = "downloaded"
    except Exception as exc:
        p["pdf_status"] = f"failed: {exc}"
        (out_dir / "paper_pdf_error.txt").write_text(f"{url}\n{exc}\n", encoding="utf-8")
    return p


def extract_pdf_text(pdf_path: Path) -> str:
    if not pdf_path.exists() or not shutil.which("pdftotext"):
        return ""
    try:
        res = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "20", str(pdf_path), "-"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=25,
            check=False,
        )
        return res.stdout.decode("utf-8", errors="ignore")
    except Exception:
        return ""


def find_known(text: str, known: list[str]) -> list[str]:
    found = []
    low = text.lower()
    for item in known:
        if item.lower() in low:
            found.append(item)
    return found[:14]


def short_sentence(sentence: str, max_words: int = 24) -> str:
    words = re.findall(r"\S+", clean_text(sentence))
    if not words:
        return ""
    if len(words) <= max_words:
        return " ".join(words)
    return " ".join(words[:max_words]) + " ..."


def sentence_split(text: str) -> list[str]:
    text = clean_text(text)
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    return [p.strip() for p in parts if len(p.split()) >= 6]


def abstract_cues(abstract: str) -> dict[str, str]:
    sents = sentence_split(abstract)
    if not sents:
        return {}
    cue = {}
    problem_keys = ["however", "challenge", "limited", "lack", "difficult", "bottleneck", "remain", "requires"]
    method_keys = ["we propose", "we present", "we introduce", "we develop", "we design", "our approach", "our method"]
    result_keys = ["outperform", "achieve", "demonstrate", "show", "state-of-the-art", "improve"]
    for name, keys in [("problem", problem_keys), ("method", method_keys), ("result", result_keys)]:
        for sent in sents:
            low = sent.lower()
            if any(k in low for k in keys):
                cue[name] = short_sentence(sent)
                break
    cue.setdefault("topic", short_sentence(sents[0]))
    return cue


def metric_suggestions(fam: str, tags: list[str], detected: list[str]) -> list[str]:
    blob = " ".join([fam] + tags).lower()
    suggestions: list[str]
    if "robot manipulation" in fam or "action" in blob or "vla" in blob:
        suggestions = ["success rate", "task completion", "language-conditioned generalization", "real/sim transfer"]
    elif "navigation" in fam:
        suggestions = ["SR", "SPL", "nDTW", "goal distance", "collision rate"]
    elif "grounding" in blob or "referring" in blob:
        suggestions = ["Acc@0.25", "Acc@0.5", "IoU", "mIoU", "Top-k accuracy"]
    elif "segmentation" in blob or "semantic" in blob or "open-vocabulary" in blob:
        suggestions = ["mIoU", "AP", "mAP", "open-vocabulary accuracy", "long-tail performance"]
    elif "reconstruction" in blob or "slam" in blob or "geometry" in blob:
        suggestions = ["PSNR", "SSIM", "LPIPS", "ATE", "RPE", "Chamfer", "F-score", "pose AUC"]
    elif "scene graph" in blob or "graph" in blob:
        suggestions = ["Recall@K", "mean Recall@K", "relationship accuracy", "zero-shot relation accuracy"]
    else:
        suggestions = ["task-specific accuracy", "generalization gap", "ablation metrics"]
    merged = []
    for item in suggestions + detected:
        if item not in merged:
            merged.append(item)
    return merged[:8]


def infer_io(tags: list[str], title: str, category: str) -> str:
    blob = " ".join(tags + [title, category]).lower()
    cat = category.lower()
    if "3d large multimodal" in cat:
        return "Input: 2D/3D observations, point/scene tokens, and natural-language prompts. Output: spatial answer, grounding result, caption, plan, or embodied reasoning response."
    if "benchmarks and datasets" in cat:
        return "Input: benchmark-specific observations/instructions. Output: standardized labels, tasks, or evaluation scores for comparing models."
    if "foundations:" in cat:
        return "Input/Output follows the foundational formulation: tokens, images, point sets, trajectories, or scene coordinates mapped to reusable representations or predictions."
    if "vla" in blob or "action" in blob or "manipulation" in blob or "robot" in blob:
        return "Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions."
    if "navigation" in blob:
        return "Input: language/navigation goal plus egocentric observations or 3D maps. Output: waypoint, action, route, or grounded target decision."
    if "gaussian" in blob or "nerf" in blob:
        return "Input: multi-view images/poses or reconstructed scenes plus language query. Output: language-queryable 3D field, mask, grounding, rendering, or scene edit."
    if "grounding" in blob:
        return "Input: 3D scene representation plus free-form natural language. Output: target object, 3D box, mask, or referring expression result."
    if "slam" in blob or "reconstruction" in blob or "geometry" in blob:
        return "Input: one or more images/RGB-D/LiDAR observations. Output: depth, camera pose, point map, dense reconstruction, or consistent map."
    if "llm" in blob or "vision-language" in blob or "vlm" in blob:
        return "Input: image/3D observations and natural language. Output: aligned representation, answer, reasoning trace, caption, or grounded decision."
    return "Input/Output follows the paper task formulation; see PDF for the exact interface."


def task_family(tags: list[str], title: str, category: str) -> str:
    blob = " ".join(tags + [title, category]).lower()
    cat = category.lower()
    if "foundations: transformer" in cat:
        return "sequence/representation learning"
    if "foundations: vision" in cat:
        return "vision or vision-language foundation model pretraining"
    if "foundations: 3d" in cat:
        return "core 3D geometry and scene representation learning"
    if "foundations: slam" in cat:
        return "SLAM, calibration, and geometric consistency"
    if "foundations: rl" in cat:
        return "RL and imitation learning for policies"
    if "3d large multimodal" in cat:
        return "3D vision-language spatial reasoning"
    if "transformer" in blob and "foundation" in category.lower():
        return "sequence/representation learning"
    if "diffusion" in blob:
        return "diffusion-based generation or policy learning"
    if "equivariant" in blob:
        return "geometry-aware equivariant modeling"
    if "gaussian" in blob:
        return "language-aware Gaussian/implicit 3D scene representation"
    if "nerf" in blob:
        return "language-aware neural radiance field representation"
    if "scene graph" in blob or "graph" in blob:
        return "structured 3D scene graph reasoning"
    if "navigation" in blob:
        return "embodied navigation and spatial planning"
    if "robot" in blob or "manipulation" in blob or "vla" in blob:
        return "robot manipulation and vision-language-action control"
    if "slam" in blob or "reconstruction" in blob or "geometry" in blob:
        return "3D reconstruction, calibration, and geometric consistency"
    if "open-vocabulary" in blob or "semantic" in blob:
        return "open-vocabulary 3D semantic understanding"
    if "llm" in blob or "vision-language" in blob or "vlm" in blob:
        return "vision-language alignment and multimodal reasoning"
    return "3D vision and embodied AI"


def problem_statement(p: dict) -> str:
    fam = task_family(p.get("tags", []), p["title"], p["category"])
    if "robot manipulation" in fam:
        return "로봇은 언어 지시, 시각 관측, 3D 공간 제약을 동시에 만족하며 행동해야 하지만 데이터 수집 비용, embodiment 차이, 장기 과제 일반화가 병목이다."
    if "3D vision-language spatial reasoning" in fam:
        return "VLM/LLM은 강한 semantic prior를 갖지만 3D 위치, 거리, 관점, affordance 같은 metric spatial reasoning에는 취약하다."
    if "navigation" in fam:
        return "실내/실외 이동 에이전트는 언어 목표와 3D 공간 구조를 연결해야 하며, partial observation과 탐색-활용 균형 때문에 단순 2D 인식만으로는 안정적이지 않다."
    if "Gaussian" in fam or "radiance" in fam:
        return "NeRF/3DGS는 장면을 잘 렌더링하지만 언어 질의, open-vocabulary semantics, instance-level grounding을 직접 지원하지 않는 경우가 많다."
    if "scene graph" in fam:
        return "3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다."
    if "reconstruction" in fam:
        return "현실의 3D reconstruction/SLAM은 calibration, pose, correspondence, temporal consistency가 불완전한 상태에서 metric geometry를 추정해야 한다."
    if "open-vocabulary" in fam:
        return "3D semantic perception은 라벨 공간이 제한적이고 long-tail 객체/속성/affordance를 다루기 어려워 foundation model alignment가 필요하다."
    if "diffusion" in fam:
        return "생성 모델 또는 policy 모델이 3D 구조와 물리 제약을 보존하지 못하면 로봇 실행이나 3D 장면 생성에서 일관성이 깨진다."
    return "이 논문은 3D perception, language grounding, representation learning 사이의 연결 부족을 해결하려는 흐름에 속한다."


def method_statement(p: dict) -> str:
    fam = task_family(p.get("tags", []), p["title"], p["category"])
    if "robot manipulation" in fam:
        return "핵심은 pretrained VLM/LLM 또는 3D representation을 policy/action space에 결합해 language-conditioned manipulation을 더 일반화 가능하게 만드는 것이다."
    if "3D vision-language spatial reasoning" in fam:
        return "핵심은 2D/3D visual tokens, point/scene representation, language model을 정렬해 공간 질의와 embodied reasoning을 한 모델에서 처리하는 것이다."
    if "navigation" in fam:
        return "핵심은 metric/semantic map, 3D scene graph, neural field, 또는 VLM reasoning을 이용해 언어 목표를 이동 가능한 공간 의사결정으로 바꾸는 것이다."
    if "Gaussian" in fam:
        return "핵심은 Gaussian primitive 또는 rendered feature에 language-aligned semantic feature를 부여하여 3DGS를 질의 가능한 장면 표현으로 확장하는 것이다."
    if "radiance" in fam:
        return "핵심은 radiance field의 공간 좌표/뷰 의존 표현에 CLIP/VLM feature를 결합해 3D 위치에서 언어적 의미를 조회할 수 있게 하는 것이다."
    if "scene graph" in fam:
        return "핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다."
    if "reconstruction" in fam:
        return "핵심은 transformer, pointmap, dense matching, SLAM optimization, 또는 3DGS를 사용해 pose/depth/shape를 한 표현 안에서 일관되게 추정하는 것이다."
    if "diffusion" in fam:
        return "핵심은 diffusion score/denoising process를 action, 3D generation, 또는 structured scene representation에 적용하면서 geometry prior를 넣는 것이다."
    if "sequence" in fam:
        return "핵심은 attention 기반 sequence modeling을 통해 장거리 의존성과 modality alignment를 scale-up 가능한 방식으로 학습하는 것이다."
    return "핵심은 foundation model feature와 3D 구조를 정렬하여 downstream task별 supervision 의존도를 줄이는 것이다."


def limitations_statement(p: dict) -> str:
    fam = task_family(p.get("tags", []), p["title"], p["category"])
    if "robot" in fam or "navigation" in fam:
        return "실제 로봇 배치에서는 센서 calibration, latency, safety, embodiment mismatch, 실패 복구가 추가 변수다."
    if "Gaussian" in fam or "radiance" in fam:
        return "3DGS/NeRF 기반 방법은 scene reconstruction 품질, 카메라 포즈, memory/runtime, dynamic scene 처리에 민감하다."
    if "open-vocabulary" in fam or "scene graph" in fam:
        return "2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다."
    if "reconstruction" in fam:
        return "강한 benchmark 성능이 실제 로봇 센서 노이즈, rolling shutter, 동적 객체, 저조도 환경까지 보장하지는 않는다."
    return "대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다."


def contribution_bullets(p: dict) -> list[str]:
    tags = p.get("tags", [])
    fam = task_family(tags, p["title"], p["category"])
    bullets = [
        f"{fam} 문제를 명확한 시스템/모델/벤치마크 형태로 정의.",
        f"핵심 키워드: {', '.join(tags[:6]) if tags else '3D vision, robotics, vision-language'}.",
    ]
    if p.get("abstract"):
        words = re.findall(r"\b[A-Z][A-Za-z0-9+.-]{2,}\b", p["abstract"])
        cues = []
        for w in words:
            if w not in cues and len(cues) < 8:
                cues.append(w)
        if cues:
            bullets.append("초록에서 확인되는 주요 cue: " + ", ".join(cues) + ".")
    return bullets


def write_notes(p: dict, *, overwrite: bool = False) -> None:
    out_dir = ROOT / p["folder"]
    pdf_path = out_dir / "paper.pdf"
    pdf_text = extract_pdf_text(pdf_path)
    combined = " ".join([p.get("abstract", ""), pdf_text])
    datasets = find_known(combined, KNOWN_DATASETS)
    detected_metrics = find_known(combined, KNOWN_METRICS)
    tags = p.get("tags", [])
    fam = task_family(tags, p["title"], p["category"])
    metrics = metric_suggestions(fam, tags, detected_metrics)
    cues = abstract_cues(p.get("abstract", ""))
    io = infer_io(tags, p["title"], p["category"])
    problem = problem_statement(p)
    method = method_statement(p)
    limitation = limitations_statement(p)
    paper_link = p.get("page") or p.get("pdf") or ""
    project = p.get("project", "not identified")
    authors = p.get("authors", "not extracted")

    venue_label = venue_display(p["venue"])

    overview = f"""# {p['title']}

- Year/Venue: {p['year']} / {venue_label}
- Category: {p['category']}
- Tags: {', '.join(tags)}
- Authors: {authors}
- Paper: {paper_link}
- GitHub/Project: {project}

## Problem
{problem}

## Core Idea
{method}

## Paper-Specific Cues
- Topic cue: {cues.get('topic', '초록 cue를 자동 추출하지 못함.')}
- Method cue: {cues.get('method', '초록에서 명시적 propose/present 문장을 자동 추출하지 못함.')}
- Result cue: {cues.get('result', '초록에서 result claim 문장을 자동 추출하지 못함.')}

## Input / Output
{io}

## Main Claims
- 논문은 `{fam}`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
{limitation}

## Contribution
""" + "\n".join(f"- {b}" for b in contribution_bullets(p)) + "\n"

    problem_md = f"""# Problem — {p['title']}

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: abstract/metadata cue 기반 scaffold; exact formulation은 본문 수동 확인 필요. tracker의 reading status/evidence는 자동으로 올리지 않는다.

## Problem in One Sentence

{problem}

## System and Scope

- **Object / environment:** `{fam}`에 해당하는 논문의 robot/embodied task scope; 구체적인 embodiment와 환경은 본문 확인 필요.
- **Observation / input:** {io}
- **Latent state / decision variable:** state, geometry, semantic representation 또는 policy context의 정확한 정의는 본문 확인 필요.
- **Output / action:** paper-specific representation, prediction 또는 robot action; exact interface는 본문 확인 필요.
- **Horizon / evaluation target:** primary task metric과 closed-loop horizon은 본문 확인 필요.

## Formal Problem Formulation

- **State / model:** abstract cue에서 확인되는 `{fam}` 문제의 state/model; equation과 transition은 본문 확인 필요.
- **Objective / loss / cost:** paper-specific objective와 optimization target은 본문 확인 필요.
- **Constraints / initial-boundary-terminal conditions:** sensing, geometry, action, contact와 task constraints는 본문 확인 필요.
- **Success / guarantee:** abstract의 claim은 참고 cue로만 두고, 성공 정의와 보장은 본문 evaluation에서 확인한다.

## Bottleneck in Prior Work

{cues.get('problem', problem)}

## What the Paper Changes

{method}

## Assumptions and Failure Boundary

| Assumption | Why it is needed | Failure boundary |
|---|---|---|
| source의 observation/model/task cue가 유효하다고 가정 | abstract 수준의 문제를 구조화하기 위해 필요 | exact assumption과 negative result는 본문 확인 전 확정하지 않음 |

## Position in the Robotics Loop

observation → state/world model → task & motion decision → policy/control → contact → feedback 중 `{fam}` 관련 단계; paper-specific closed-loop 위치는 본문 확인 필요.

## Verification Questions

- **Evidence anchor:** abstract problem/method cue와 등록된 input/output cue.
- **Still to verify:** state, objective/loss, constraints, initial/terminal condition, success metric과 실제 robot closed-loop 연결을 원문에서 확정한다.
"""

    method_md = f"""# Method — {p['title']}

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`. Full-text reading is not implied.
> Analysis basis: abstract/metadata cue 기반 scaffold; exact method detail은 본문 수동 확인 필요.

## Method in One Sentence

{method}

## Design Rationale

{problem}

## Source Evidence Cues

- Method cue: {cues.get('method', '자동 추출 없음.')}
- Task family cue: {fam}
- Representation cue: {', '.join([t for t in tags if any(k in t.lower() for k in ['3d', 'gaussian', 'nerf', 'graph', 'geometry', 'slam', 'semantic', 'vla', 'vlm', 'llm'])]) or 'paper-specific representation'}

## Pipeline

| Module | Purpose | Input | Operation | Output | Interface / expected benefit | Evidence |
|---|---|---|---|---|---|---|
| Paper-specific method module | task-specific representation과 prediction/control을 연결 | {io} | {method} | paper-specific prediction/action | {fam} task utility는 04와 대조 | abstract/metadata cue; exact section/page 확인 필요 |

## Objective / Update Rule

- **Objective/loss/control law:** 본문 확인 필요.
- **Optimization/update:** paper-specific; method section 확인 필요.
- **Constraint/regularization:** sensor calibration, scene reconstruction quality, action feasibility와 task-specific constraints를 본문에서 확인한다.

## Variables and Parameters

| Symbol / parameter | Type / unit | Meaning | Used in | Source |
|---|---|---|---|---|
| oₜ / xₜ | observation/state | paper input or state | representation | method section 확인 필요 |
| aₜ / yₜ | action/prediction | paper output | execution/evaluation | method section 확인 필요 |
| θ | parameters | learned/optimized quantities | update | method section 확인 필요 |

## Observation–State–Action Interface

- **Observation / input:** {io}
- **State / latent representation:** 본문 확인 필요.
- **Action / output:** 본문 확인 필요.
- **Planner–controller / policy–environment interface:** 본문 확인 필요.

## Temporal and Runtime Contract

- **Horizon:** 본문 확인 필요.
- **Inference/control rate:** 본문 확인 필요.
- **History / memory:** 본문 확인 필요.
- **Compute / latency dependency:** data preprocessing, encoder/decoder, optimization/inference steps와 hardware dependency를 확인한다.

## Training vs Inference

- **Training / offline setup:** 본문 확인 필요.
- **Inference / online execution:** 본문 확인 필요.
- **Boundary to keep separate:** training, inference, control rate, horizon과 memory를 구분한다.

## Method-Specific Formal Details

- Exact equation/loss/control law와 variable meaning은 본문 확인 필요.

## Evaluation Link

- **Module-to-evaluation link:** [04_evaluation.md](./04_evaluation.md)의 baseline/ablation이 위 method module을 어떻게 isolate하는지 확인한다.
- **Protocol/metric cue:** {cues.get('result', '자동 추출 없음.')}

## Failure and Ablation Link

- Strongest assumption, failure mode와 module ablation은 본문 및 04_evaluation.md에서 확인 필요.

## Reproduction Checklist

1. [ ] method section에서 module input/output와 exact objective를 확인한다.
2. [ ] variable/unit, horizon, rate, memory와 implementation dependency를 기록한다.
3. [ ] 04의 baseline, ablation, metric, split과 failure protocol을 대조한다.

## Verification Questions

- **Still to verify:** exact method equation, variable source, training/inference boundary, runtime contract과 module-level evaluation attribution.
"""

    dataset_cue = ', '.join(datasets) if datasets else 'not found in current registry/abstract cue'
    metric_cue = ', '.join(metrics) if metrics else 'task-specific metric not found in current registry/abstract cue'
    result_cue = cues.get('result', 'registry/abstract result cue not found')
    evaluation_md = f"""# Evaluation — {p['title']}

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`. Full-text reading is not implied.
> Analysis basis: registry/abstract cue 기반 evaluation scaffold; exact experiment detail은 본문 수동 확인 필요.

## Evaluation in One Sentence

{result_cue}

## Evaluation Type and Scope

- **Evaluation type:** provisional; theory, system, learning, simulation/real-robot 또는 benchmark 유형을 본문에서 확인한다.
- **Target system/task:** task family `{fam}`에 해당하는 paper-specific task/system
- **Input/observation boundary:** {io}
- **Output/decision under evaluation:** paper-specific prediction, plan, control 또는 task outcome; 본문 확인 필요.
- **Primary target:** {metric_cue}

## Experimental Matrix

| Experiment / claim | Type & setting | Dataset / split | Robot / system | Baseline | Metric / result cue | Trials / seeds | Source |
|---|---|---|---|---|---|---|---|
| primary evaluation claim | setting과 sim/real 여부는 본문 확인 필요 | {dataset_cue}; split/role not verified | embodiment/hardware not verified | baseline identity not verified | {metric_cue}; exact definition not verified | not reported | abstract/experiment section 확인 필요 |

## Dataset / Benchmark Role

| Resource | Role | Split / size | Source |
|---|---|---|---|
| {dataset_cue} | registry/abstract cue; train/eval/pretraining/auxiliary role은 본문 확인 필요 | not reported | dataset/experiment section 확인 필요 |

- Dataset name이 언급됐다는 사실만으로 final evaluation dataset으로 확정하지 않는다.

## Embodiment / Environment

| Dimension | Recorded cue | Missing detail | Source |
|---|---|---|---|
| Robot / simulator / hardware | not reported | hardware, simulator/real 여부와 configuration 확인 필요 | evaluation section 확인 필요 |
| Observation / sensor | {io} | sensor, calibration와 preprocessing 확인 필요 | method/evaluation section 확인 필요 |
| Task / episode unit | not reported | task count, reset, timeout와 success denominator 확인 필요 | evaluation protocol 확인 필요 |
| Generalization split/variation | not reported | scene/object/instruction/embodiment split 확인 필요 | dataset/protocol 확인 필요 |

## Metrics and Success Definition

| Metric / success signal | Direction / unit | Status | Source |
|---|---|---|---|
| {metric_cue} | not reported | registry/abstract cue; exact definition, direction와 aggregation 확인 필요 | evaluation table 확인 필요 |

- **Success/failure/timeout definition:** 본문 확인 필요.

## Baselines and Fairness

| Baseline / comparison cue | What it should isolate | Same data/observation/compute? | Source |
|---|---|---|---|
| not found | comparison identity와 configuration 확인 필요 | not reported | baseline table 확인 필요 |

**Baseline fairness audit**

| Fairness dimension | Current record | Required check |
|---|---|---|
| Observation/action interface | not reported | modality, action space와 preprocessing을 맞춘다 |
| Data/pretraining | not reported | demonstrations, pretraining과 additional labels를 맞춘다 |
| Compute/runtime | not reported | parameter budget, inference steps, latency와 control rate를 맞춘다 |
| Evaluation protocol | not reported | split, reset/timeout, seeds와 success denominator를 맞춘다 |

## Ablations and Sensitivity

| Ablation / sensitivity factor | Method component | Expected interpretation | Reported status / source |
|---|---|---|---|
| not reported | core method module | component attribution과 strongest assumption sensitivity 확인 필요 | ablation table 확인 필요 |

## Main Results / Claim–Evidence Map

| Claim / target | Evidence or result cue | Evaluation type | Strength | Source |
|---|---|---|---|---|
| primary evaluation claim | {result_cue} | provisional | registry/abstract cue; exact result와 condition은 본문 확인 필요 | result table/figure 확인 필요 |

## Generalization and Failure Cases

| Assumption / regime | Failure or stress test | Status | Source |
|---|---|---|---|
| source의 observation/model/task cue가 유효하다고 가정 | distribution shift, sensor failure, contact/long-horizon failure는 본문 확인 필요 | unverified | problem/evaluation section 확인 필요 |

## Statistics, Efficiency, and Reproducibility

| Reproducibility field | Recorded value/cue | Status | Source |
|---|---|---|---|
| Trials / episodes | not reported | count와 repeat unit 확인 필요 | protocol 확인 필요 |
| Random seeds / repeats | not reported | seed/repeat policy 확인 필요 | protocol 확인 필요 |
| Mean ± std / CI | not reported | uncertainty reporting 확인 필요 | result table 확인 필요 |
| Latency / throughput | not reported | inference/control runtime 확인 필요 | method/evaluation 확인 필요 |
| Compute / hardware dependency | not reported | hardware, checkpoint와 environment 확인 필요 | reproducibility section 확인 필요 |
| Train/eval split and leakage control | not reported | split, preprocessing와 leakage control 확인 필요 | dataset section 확인 필요 |
| Code / checkpoint / environment | canonical pointer는 01_overview.md 참조 | availability/configuration을 본문에서 확인 | 01_overview.md |

## Limitations and Verification Questions

- **Evidence boundary:** registry/abstract cue를 reported result로 승격하지 않는다. exact table/figure/page는 본문 확인이 필요하다.
- **Current limitation cue:** {limitation}
- **Claim–condition check:** 모든 수치는 task, embodiment/simulator, input/action interface, metric, baseline와 trial/seed 조건을 함께 기록한다.
- **Reproduction check:** reset/timeout/success denominator, preprocessing, checkpoint, compute, inference/control rate와 failure handling을 별도로 확인한다.
"""

    insights_md = f"""# Insights — {p['title']}

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `CURATION_ONLY`.
> Analysis basis: abstract/metadata cue와 자동 추출 결과를 정리한 curation scaffold; full-text manual review required.

## Paper-supported conclusion

> **Evidence boundary:** 아래 내용은 현재 확인 가능한 abstract/source cue의 범위다. 자동 추출이나 local PDF 보유를 수동 정독으로 간주하지 않으며, 상세 claim은 full-text 확인 전까지 확정하지 않는다.

### What was actually new

- **Problem cue:** {problem}
- **Method cue:** {method}
- **Result cue:** {cues.get('result', 'abstract에서 명시적 result cue를 확인하지 못함.')}

### Strongest assumption and failure boundary

- {limitation}
- Exact assumptions, negative results, benchmark protocol, and transfer limits remain to be checked against the full text.

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** observation → state/world model → task decision → policy/control → feedback.
- `{fam}` 논문의 input/output boundary를 유지한 채, downstream task success, failure, latency와 sensor/embodiment shift를 별도로 측정한다.

### Dependency and evolution

- `{p['category']}` / tags: `{', '.join(tags[:5])}`.
- Direct citation predecessor/successor is not asserted until the references and related work are checked.

### Minimal reproduction

1. Confirm the paper-reported task, input/output, dataset or simulator, metric, baseline, and split from the full text.
2. Implement the smallest paper-specific component and compare it with a matched simpler baseline.
3. Report the primary metric together with failure rate, latency, and sensitivity to the strongest assumption.

## Falsifiable research question

At a matched data, compute, and action budget, does the paper's `{', '.join(tags[:4]) or fam}` interface improve its primary task metric and downstream robustness over a simpler baseline?

**Reject the hypothesis if** the primary metric does not improve or the method adds latency, failures, or assumption sensitivity without a compensating benefit.
"""

    files = {
        "01_overview.md": overview,
        "02_problem.md": problem_md,
        "03_method.md": method_md,
        "04_evaluation.md": evaluation_md,
        "05_insights.md": insights_md,
    }
    for name, content in files.items():
        path = out_dir / name
        if overwrite or not path.exists():
            path.write_text(content, encoding="utf-8")


def write_registry(papers: list[dict]) -> None:
    # Historical discovery lists are incomplete. Never let a table rebuild
    # silently remove identities already admitted to the canonical manifest.
    if MANIFEST.exists():
        existing = json.loads(MANIFEST.read_text(encoding="utf-8"))
        existing_ids = {item["paper_id"] for item in existing}
        incoming_ids = {item.get("paper_id") for item in papers}
        missing = existing_ids - incoming_ids
        if missing:
            raise ValueError(f"Registry rebuild would omit {len(missing)} canonical paper IDs")
    try:
        from normalize_taxonomy import registry
    except ModuleNotFoundError:
        from .normalize_taxonomy import registry
    (ROOT / "PAPER.md").write_text(registry(papers), encoding="utf-8")


def write_manifest(papers: list[dict]) -> None:
    existing = {}
    if MANIFEST.exists():
        existing = {
            item["title"].casefold(): item
            for item in json.loads(MANIFEST.read_text(encoding="utf-8"))
        }
    available = list(existing.values())
    manifest = []
    for source in papers:
        old = existing.get(source["title"].casefold(), {})
        merged = dict(old)
        for key in ["title", "year", "venue", "category", "tags", "folder", "pdf", "page", "project"]:
            value = source.get(key)
            if value is None or (isinstance(value, str) and not value.strip()):
                continue
            if key == "folder" and old.get("folder"):
                continue
            merged[key] = value
        canonicalize(merged)
        paper_id = merged.get("paper_id") or next_paper_id(available)
        merged = enrich_record(merged, paper_id=paper_id, root=ROOT)
        manifest.append(merged)
        available.append(merged)
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if REGISTRY_META.exists():
        meta = json.loads(REGISTRY_META.read_text(encoding="utf-8"))
        meta["paper_count"] = len(manifest)
        meta["generated_on"] = date.today().isoformat()
        REGISTRY_META.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only survey audit by default; mutations require explicit flags."
    )
    parser.add_argument(
        "--refresh-metadata",
        action="store_true",
        help="query supported official/arXiv pages for metadata",
    )
    parser.add_argument(
        "--download-pdfs",
        action="store_true",
        help="download optional PDF caches (never implied by another flag)",
    )
    parser.add_argument(
        "--create-missing-notes",
        action="store_true",
        help="create only absent standard notes; existing notes are preserved",
    )
    parser.add_argument(
        "--overwrite-notes",
        action="store_true",
        help="replace every generated note; use only for an intentional rebuild",
    )
    parser.add_argument("--write-registry", action="store_true")
    parser.add_argument("--write-manifest", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not MANIFEST.exists():
        raise SystemExit("Canonical manifest missing; refusing a legacy-list rebuild")
    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(papers, list) or not papers or any(
        not all(item.get(key) for key in ("paper_id", "title", "folder"))
        for item in papers
    ):
        raise SystemExit("Invalid canonical manifest; run the repository audit before writing")
    print(f"[info] canonical papers: {len(papers)}")

    if args.refresh_metadata:
        fetch_arxiv_metadata(papers)
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
            list(ex.map(fetch_page_metadata, papers))

    if args.download_pdfs:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
            papers = list(ex.map(download_pdf, papers))

    if args.create_missing_notes or args.overwrite_notes:
        for p in papers:
            write_notes(p, overwrite=args.overwrite_notes)

    if args.write_registry:
        write_registry(papers)
    if args.write_manifest:
        write_manifest(papers)

    if args.download_pdfs:
        downloaded = sum(1 for p in papers if p.get("pdf_status") == "downloaded")
        print(f"[info] PDFs downloaded in this explicit run: {downloaded}/{len(papers)}")
    if not any(vars(args).values()):
        print("[info] read-only audit complete; no files or network state changed")


if __name__ == "__main__":
    main()
