#!/usr/bin/env python3
"""Create the ECCV/ICCV/RA-L/IROS venue-audit supplement."""

from __future__ import annotations

import html
import json
import re
import urllib.parse
from pathlib import Path

import requests

from create_extra_venue_papers import category_and_tags, norm_title


WORK = Path(__file__).resolve().parent
ROOT = WORK.parent
CVF_CANDIDATES = WORK / "cvf_candidates.json"
OUT = WORK / "extra_papers_eccv_iccv_ral_iros.json"
LOG = WORK / "extra_papers_eccv_iccv_ral_iros_log.json"

ECVA_PAPERS = "https://www.ecva.net/papers.php"


ECCV_2024_TITLES = [
    "QUAR-VLA: Vision-Language-Action Model for Quadruped Robots",
    "SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding",
    "Uni3DL: A Unified Model for 3D Vision-Language Understanding",
    "Unifying 3D Vision-Language Understanding via Promptable Queries",
    "3D Open-Vocabulary Panoptic Segmentation with 2D-3D Vision-Language Distillation",
    "3D Weakly Supervised Semantic Segmentation with 2D Vision-Language Guidance",
    "Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding",
    "Open-Vocabulary 3D Semantic Segmentation with Text-to-Image Diffusion Models",
    "Global-Local Collaborative Inference with LLM for Lidar-Based Open-Vocabulary Detection",
    "ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation",
    "NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models",
    "SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs",
    "Heterogeneous Graph Learning for Scene Graph Prediction in 3D Point Clouds",
    "OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation",
    "SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM",
    "TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving",
    "GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction",
    "DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting",
    "EchoScene: Indoor Scene Generation via Information Echo over Scene Graph Diffusion",
    "BlenderAlchemy: Editing 3D Graphics with Vision-Language Models",
    "Exploiting Semantic Reconstruction to Mitigate Hallucinations in Vision-Language Models",
]


ICCV_2025_TITLES = [
    "Egocentric Action-aware Inertial Localization in Point Clouds with Vision-Language Guidance",
    "Identity-aware Language Gaussian Splatting for Open-vocabulary 3D Semantic Segmentation",
    "Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction",
    "OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection",
    "CCL-LGS: Contrastive Codebook Learning for 3D Language Gaussian Splatting",
    "CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting",
    "DiSCO-3D : Discovering and Segmenting Sub-Concepts from Open-vocabulary Queries in NeRF",
    "EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding",
    "FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation",
    "GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding",
    "IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation",
    "LangScene-X: Reconstruct Generalizable 3D Language-Embedded Scenes with TriMap Video Diffusion",
    "ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation",
    "PhysSplat: Efficient Physics Simulation for 3D Scenes via MLLM-Guided Gaussian Splatting",
    "CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance",
    "Details Matter for Indoor Open-vocabulary 3D Instance Segmentation",
    "Exploiting Vision Language Model for Training-Free 3D Point Cloud OOD Detection via Graph Score Propagation",
    "Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics",
    "GeoProg3D: Compositional Visual Reasoning for City-Scale 3D Language Fields",
    "Kestrel: 3D Multimodal LLM for Part-Aware Grounded Description",
    "LIRA: Reasoning Reconstruction via Multimodal Large Language Models",
    "MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs",
    "Moto: Latent Motion Token as the Bridging Language for Learning Robot Manipulation from Videos",
    "OVA-Fields: Weakly Supervised Open-Vocabulary Affordance Fields for Robot Operational Part Detection",
    "Open-Vocabulary Octree-Graph for 3D Scene Understanding",
    "Towards Long-Horizon Vision-Language-Action System: Reasoning, Acting and Memory",
    "VGMamba: Attribute-to-Location Clue Reasoning for Quantity-Agnostic 3D Visual Grounding",
    "VLR-Driver: Large Vision-Language-Reasoning Models for Embodied Autonomous Driving",
    "VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers",
    "ViewSRD: 3D Visual Grounding via Structured Multi-View Decomposition",
    "Mamba-3VL: Taming State Space Model for 3D Vision Language Learning",
    "MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh",
    "On-Device Diffusion Transformer Policy for Efficient Robot Manipulation",
    "PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation",
    "PlaceIt3D: Language-Guided Object Placement in Real 3D Scenes",
    "Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration",
    "FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images",
    "Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation",
    "ZeroKey: Point-Level Reasoning and Zero-Shot 3D Keypoint Detection from Large Language Models",
]


ARXIV_PAPERS = [
    # ECCV 2026: official proceedings are not yet mirrored on ECVA/CVF, so use arXiv records with ECCV comments.
    ("LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models", 2026, "ECCV 2026", "2606.23686", "https://libero-safety.github.io/"),
    ("VLA Knows Its Limits: Adaptive Execution Horizons for Robot Policies", 2026, "ECCV 2026", "2602.21445", "https://hatchetproject.github.io/"),
    ("PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models", 2026, "ECCV 2026", "2606.22540", "https://inceptionwang.github.io/PolicyTrim/"),

    # RA-L 2024-2026.
    ("GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping", 2024, "RA-L", "2403.09637", "https://github.com/MrSecant/GaussianGrasper"),
    ("Clio: Real-time Task-Driven Open-Set 3D Scene Graphs", 2024, "RA-L", "2404.13696", "https://github.com/MIT-SPARK/Clio"),
    ("FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models", 2024, "RA-L", "2402.04555", "https://github.com/HKUST-Aerial-Robotics/FM-Fusion"),
    ("Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation", 2024, "RA-L", "2403.08605", "https://moma-llm.cs.uni-freiburg.de/"),
    ("S3E: A Multi-Robot Multimodal Dataset for Collaborative SLAM", 2024, "RA-L", "2210.13723", "https://pengyu-team.github.io/S3E/"),
    ("Search3D: Hierarchical Open-Vocabulary 3D Segmentation", 2025, "RA-L", "2409.18431", "http://search3d-segmentation.github.io/"),
    ("TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation", 2025, "RA-L", "2409.12514", "https://tiny-vla.github.io/"),
    ("Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation", 2025, "RA-L", "2410.11989", "https://github.com/BJHYZJ/DovSG"),
    ("HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting", 2025, "RA-L", "2501.14147", "https://hammer-project.github.io/"),
    ("ActiveGS: Active Scene Reconstruction using Gaussian Splatting", 2025, "RA-L", "2412.17769", "https://github.com/dmar-bonn/active-gs"),
    ("PointVLA: Injecting the 3D World into Vision-Language-Action Models", 2026, "RA-L", "2503.07511", "not identified"),
    ("LAMP: Implicit Language Map for Robot Navigation", 2026, "RA-L", "2602.11862", "https://lab-of-ai-and-robotics.github.io/LAMP/"),
    ("CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion", 2026, "RA-L", "2601.09512", "https://tum-lsy.github.io/CLARE/"),
    ("ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles", 2026, "RA-L", "2602.11575", "https://syeon-yoo.github.io/readygo/"),
    ("Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization", 2026, "RA-L", "2606.24767", "not identified"),

    # IROS 2025 papers with public arXiv PDFs.
    ("VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model", 2025, "IROS 2025", "2410.08792", "https://ai4ce.github.io/SeeDo/"),
    ("PD-VLA: Accelerating Vision-Language-Action Model Integrated with Action Chunking via Parallel Decoding", 2025, "IROS 2025", "2503.02310", "not identified"),
    ("WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation", 2025, "IROS 2025", "2503.02247", "https://b0b8k1ng.github.io/WMNav/"),
    ("Helpful DoggyBot: Open-World Object Fetching using Legged Robots and Vision-Language Models", 2025, "IROS 2025", "2410.00231", "https://helpful-doggybot.github.io/"),
    ("OpenGS-Fusion: Open-Vocabulary Dense Mapping with Hybrid 3D Gaussian Splatting for Refined Object-Level Understanding", 2025, "IROS 2025", "2508.01150", "not identified"),
    ("LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments", 2025, "IROS 2025", "2411.12185", "not identified"),
    ("MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs", 2025, "IROS 2025", "2412.18381", "not identified"),
    ("Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps", 2025, "IROS 2025", "2403.02751", "not identified"),
    ("OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph", 2025, "IROS 2025", "2409.18743", "not identified"),
    ("SORT3D: Spatial Object-centric Reasoning Toolbox for Zero-Shot 3D Grounding Using Large Language Models", 2025, "IROS 2025", "2504.18684", "not identified"),
    ("FunGraph: Functionality Aware 3D Scene Graphs for Language-Prompted Scene Interaction", 2025, "IROS 2025", "2503.07909", "not identified"),
    ("FOCI: Trajectory Optimization on Gaussian Splats", 2025, "IROS 2025", "2505.08510", "https://rffr.leggedrobotics.com/works/foci/"),
    ("GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting", 2025, "IROS 2025", "2503.05152", "not identified"),
    ("GRaD-Nav: Efficiently Learning Visual Drone Navigation with Gaussian Radiance Fields and Differentiable Dynamics", 2025, "IROS 2025", "2503.03984", "https://qianzhong-chen.github.io/gradnav.github.io/"),

    # IROS 2026 accepted papers visible on arXiv as of this audit.
    ("LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping", 2026, "IROS 2026", "2606.20424", "not identified"),
    ("FAST-LIVGO: A Degeneracy-Robust LiDAR-Inertial-Visual-GNSS Fusion Odometry", 2026, "IROS 2026", "2606.19190", "not identified"),
    ("SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation", 2026, "IROS 2026", "2606.25497", "not identified"),
]


def ecva_map() -> dict[str, dict]:
    text = requests.get(ECVA_PAPERS, timeout=30).text
    pattern = re.compile(
        r'<dt class="ptitle"><br>\s*<a href=([^>]+)>\s*(.*?)</a>\s*</dt><dd>\s*(.*?)</dd>\s*<dd>\[<a href=\'([^\']+\.pdf)\'>pdf</a>\]',
        re.S,
    )
    out = {}
    for page, title, authors, pdf in pattern.findall(text):
        clean_title = html.unescape(re.sub(r"<[^>]+>", " ", title))
        clean_title = re.sub(r"\s+", " ", clean_title).strip()
        out[clean_title] = {
            "title": clean_title,
            "authors": re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", authors))).strip(),
            "pdf": urllib.parse.urljoin(ECVA_PAPERS, pdf),
            "page": urllib.parse.urljoin(ECVA_PAPERS, page),
        }
    return out


def cvf_map() -> dict[str, dict]:
    data = json.loads(CVF_CANDIDATES.read_text(encoding="utf-8"))
    return {item["title"]: item for item in data}


def make_entry(title: str, year: int, venue: str, pdf: str | None = None, page: str | None = None, arxiv: str | None = None, authors: str = "", project: str = "not identified") -> dict:
    category, tags = category_and_tags(title, [])
    entry = {
        "title": title,
        "year": year,
        "venue": venue,
        "category": category,
        "tags": tags,
        "project": project,
    }
    if pdf:
        entry["pdf"] = pdf
    if page:
        entry["page"] = page
    if arxiv:
        entry["arxiv"] = arxiv
    if authors:
        entry["authors"] = authors
    return entry


def main() -> None:
    added: list[dict] = []
    missing: list[dict] = []

    by_ecva = ecva_map()
    for title in ECCV_2024_TITLES:
        item = by_ecva.get(title)
        if not item:
            missing.append({"source": "ECCV 2024 ECVA", "title": title})
            continue
        added.append(make_entry(
            title=title,
            year=2024,
            venue="ECCV",
            pdf=item["pdf"],
            page=item["page"],
            authors=item.get("authors", ""),
        ))

    by_cvf = cvf_map()
    for title in ICCV_2025_TITLES:
        item = by_cvf.get(title)
        if not item:
            missing.append({"source": "ICCV 2025 CVF", "title": title})
            continue
        added.append(make_entry(
            title=title,
            year=2025,
            venue="ICCV 2025",
            pdf=item.get("pdf"),
            page=item.get("page"),
        ))

    for title, year, venue, arxiv_id, project in ARXIV_PAPERS:
        added.append(make_entry(
            title=title,
            year=year,
            venue=venue,
            arxiv=arxiv_id,
            project=project,
        ))

    seen = set()
    unique = []
    for item in added:
        key = norm_title(item["title"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)

    OUT.write_text(json.dumps(unique, ensure_ascii=False, indent=2), encoding="utf-8")
    LOG.write_text(json.dumps({"added": len(unique), "missing": missing}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"added {len(unique)} papers")
    if missing:
        print(f"missing {len(missing)} titles; see {LOG}")


if __name__ == "__main__":
    main()
