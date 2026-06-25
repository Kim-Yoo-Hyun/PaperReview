#!/usr/bin/env python3
"""Create extra 2025/2026 venue papers after auditing non-CVF venues."""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import requests


WORK = Path(__file__).resolve().parent
OPENREVIEW_CANDIDATES = WORK / "openreview_2025_2026_candidates.json"
ICRA2026_CANDIDATES = WORK / "icra2026_candidates.json"
OUT = WORK / "extra_papers_2025_2026.json"
LOG = WORK / "extra_papers_2025_2026_log.json"


OPENREVIEW_SELECTED = {
    "ICLR.cc/2025/Conference": [
        "HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation",
        "GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation",
        "ImagineNav: Prompting Vision-Language Models as Embodied Navigator through Scene Imagination",
        "VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation",
        "3D Vision-Language Gaussian Splatting",
        "AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation",
        "LLaRA: Supercharging Robot Learning Data for Vision-Language Policy",
        "SPA: 3D Spatial-Awareness Enables Effective Embodied Representation",
        "DenseGrounding: Improving Dense Language-Vision Semantics for Ego-centric 3D Visual Grounding",
        "TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies",
        "DenseMatcher: Learning 3D Semantic Correspondence for Category-Level Manipulation from a Single Demo",
        "3D-SPATIAL MULTIMODAL MEMORY",
        "Articulate-Anything:  Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model",
        "3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds",
        "UniGS: Unified Language-Image-3D Pretraining with Gaussian Splatting",
        "Learning Geometric Reasoning Networks For Robot Task And Motion Planning",
        "PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks",
        "RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation",
        "ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY",
    ],
    "ICLR.cc/2026/Conference": [
        "MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation",
        "From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors",
        "Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes",
        "Spatially Guided Training for Vision-Language-Action Model",
        "Vision-Language-Action Instruction Tuning: From Understanding to Manipulation",
        "From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation",
        "RoboInter: A Holistic Intermediate Representation Suite Towards Robotic Manipulation",
        "OmniEVA: Embodied Versatile Planner via Task-Adaptive 3D-Grounded and Embodiment-aware Reasoning",
        "Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning",
        "AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild",
        "Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation",
        "MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning",
        "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model",
        "HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model",
        "Interleave-VLA: Enhancing Robot Manipulation with Image-Text Interleaved Instructions",
        "RobotArena $\\infty$: Scalable Robot Benchmarking via Real-to-Sim Translation",
        "Sim2Real VLA: Zero-Shot Generalization of Synthesized Skills to Realistic Manipulation",
        "Generalizable Coarse-to-Fine Robot Manipulation via Language-Aligned 3D Keypoints",
        "JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation",
        "Uncertainty-Aware Gaussian Map for Vision-Language Navigation",
        "EquAct: An SE(3)-Equivariant Multi-Task Transformer for 3D Robotic Manipulation",
        "Towards Physically Executable 3D Gaussian for Embodied Navigation",
        "GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models",
    ],
    "NeurIPS.cc/2025/Conference": [
        "BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models",
        "Dynam3D: Dynamic Layered 3D Tokens Empower VLM for Vision-and-Language Navigation",
        "VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models",
        "RoboRefer: Towards Spatial Referring with Reasoning in Vision-Language Models for Robotics",
        "Scaffolding Dexterous Manipulation with Vision-Language Models",
        "ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning",
        "DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation",
        "SimWorld-Robotics: Synthesizing Photorealistic and Dynamic Urban Environments for Multimodal Robot Navigation and Collaboration",
        "Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning",
        "Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better",
        "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching",
        "4D-VLA:  Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration",
        "BeliefMapNav: 3D Voxel-Based Belief Map for Zero-Shot Object Navigation",
        "DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge",
        "OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis",
        "SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning",
        "SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation",
        "NavBench: Probing Multimodal Large Language Models for Embodied Navigation",
        "ViSPLA: Visual Iterative Self-Prompting for Language-Guided 3D Affordance Learning",
        "ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning",
        "ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation",
        "Spatial Understanding from Videos: Structured Prompts Meet Simulation Data",
        "3D Equivariant Visuomotor Policy Learning via Spherical Projection",
        "Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting",
    ],
    "ICML.cc/2025/Conference": [
        "ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning",
        "UP-VLA:  A Unified Understanding and Prediction Model for Embodied Agent",
        "DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression",
        "OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction",
        "Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning",
        "SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space",
        "Unifying 2D and 3D Vision-Language Understanding",
        "From Thousands to Billions: 3D Visual Language Grounding via Render-Supervised Distillation from 2D VLMs",
        "ReferSplat: Referring Segmentation in 3D Gaussian Splatting",
        "EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents",
        "Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models",
        "SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation",
        "VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians",
        "3D Question Answering via only 2D Vision-Language Models",
        "VIP: Vision Instructed Pre-training for Robotic Manipulation",
        "LOCATE 3D: Real-World Object Localization via Self-Supervised Learning in 3D",
        "How Do Images Align and Complement LiDAR? Towards a Harmonized Multi-modal 3D Panoptic Segmentation",
    ],
    "ICML.cc/2026/Conference": [
        "Joint Navigation and Manipulation Planning with 3D Interaction Chains",
        "AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation",
        "TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments",
        "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies",
        "HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control",
        "HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning",
        "LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model",
        "Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action",
        "LAGEA: Language Guided Embodied Agents for Robotic Manipulation",
        "RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation",
        "Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting",
        "Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models",
        "Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving",
        "XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations",
        "Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation",
        "RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation",
        "RoboOmni: Actions Are Just Another Modality for Vision-Language Models",
        "SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks",
        "MapDream: Task-Driven Map Learning for Vision-Language Navigation",
        "Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds",
        "SpatioLM: Towards General Physical Spatial Intelligence in Vision-Language Models",
    ],
}


ICRA_SELECTED = [
    # ICRA 2025, confirmed by official/proceedings TOC where available.
    {"title": "MiniVLN: Efficient Vision-And-Language Navigation by Progressive Knowledge Distillation", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    {"title": "VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    {"title": "IRef-VLA: A Benchmark for Interactive Referential Grounding with Imperfect Language in 3D Scenes", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    {"title": "Graph2Nav: 3D Object-Relation Graph Generation to Robot Navigation", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    {"title": "Point2Graph: An End-To-End Point Cloud-Based 3D Open-Vocabulary Scene Graph for Robot Navigation", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    {"title": "LE-Object: Language Embedded Object-Level Neural Radiance Fields for Open-Vocabulary Scene", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    {"title": "Gaussian Splatting Visual MPC for Granular Media Manipulation", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    {"title": "Persistent Object Gaussian Splat (POGS) for Tracking Human and Robot Manipulation of Irregularly Shaped Objects", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    {"title": "VITaL Pretraining: Visuo-Tactile Pretraining for Tactile and Non-Tactile Manipulation Policies", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    {"title": "Context Graph-based Visual-Language Place Recognition", "year": 2025, "venue": "ICRA 2025", "page": "https://www.proceedings.com/content/081/081087webtoc.pdf"},
    # ICRA 2026, confirmed by Papercept public program.
    {"title": "RynnVLA-001: Using Human Demonstrations to Improve Robot Manipulation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html"},
    {"title": "Audio-VLA: Adding Contact Audio Perception to Vision-Language-Action Model for Robotic Manipulation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html"},
    {"title": "DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework for Robot Manipulation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html"},
    {"title": "MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html"},
    {"title": "FP3: A 3D Foundation Policy for Robotic Manipulation", "year": 2026, "venue": "ICRA 2026", "page": "https://2026.ieee-icra.org/awards/"},
    {"title": "FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html"},
    {"title": "Scalable Vision-Language-Action Model Pretraining for Robotic Dexterous Manipulation with Real-Life Human Activity Videos", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html"},
    {"title": "GaussianVLM: Scene-Centric 3D Vision-Language Models Using Language-Aligned Gaussian Splats for Embodied Reasoning and Beyond", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html"},
    {"title": "OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html"},
    {"title": "OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html"},
    {"title": "EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html"},
    {"title": "LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html"},
    {"title": "Goal-VLA: Image-Generative VLMs As Object-Centric World Models Empowering Zero-Shot Robot Manipulation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html"},
    {"title": "VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning Via Online Monte Carlo Tree Search", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html"},
    {"title": "VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html"},
    {"title": "Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html"},
    {"title": "Semantically Consistent Language Gaussian Splatting for 3D Point-Level Open-Vocabulary Querying", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html"},
    {"title": "SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_3.html"},
    {"title": "TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation", "year": 2026, "venue": "ICRA 2026", "page": "https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html"},
]


ARXIV_OVERRIDES = {
    "FP3: A 3D Foundation Policy for Robotic Manipulation": "2503.08950",
    "FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation": "2602.02142",
    "Scalable Vision-Language-Action Model Pretraining for Robotic Dexterous Manipulation with Real-Life Human Activity Videos": "2510.21571",
    "GaussianVLM: Scene-Centric 3D Vision-Language Models Using Language-Aligned Gaussian Splats for Embodied Reasoning and Beyond": "2507.00886",
    "OmniVLA: Physically-Grounded Multimodal VLA with Unified Multi-Sensor Perception for Robotic Manipulation": "2511.01210",
    "OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation": "2509.19480",
    "EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation": "2511.05397",
    "LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments": "2510.19655",
    "Goal-VLA: Image-Generative VLMs As Object-Centric World Models Empowering Zero-Shot Robot Manipulation": "2506.23919",
    "VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning Via Online Monte Carlo Tree Search": "2509.22643",
    "VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting": "2507.01125",
    "Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning": "2509.23107",
    "Semantically Consistent Language Gaussian Splatting for 3D Point-Level Open-Vocabulary Querying": "2503.21767",
    "SINGER: An Onboard Generalist Vision-Language Navigation Policy for Drones": "2509.18610",
    "TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation": "2603.02972",
}


def norm_title(title: str) -> str:
    title = title.lower()
    title = title.replace("and", "and")
    title = re.sub(r"\\$[^$]*\\$", " ", title)
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\\s+", " ", title).strip()


def get_year_from_venueid(venueid: str) -> int:
    m = re.search(r"20\d{2}", venueid)
    return int(m.group(0)) if m else 0


def category_and_tags(title: str, keywords: list[str] | None = None) -> tuple[str, list[str]]:
    blob = " ".join([title] + (keywords or [])).lower()
    tags: list[str] = []
    def add(tag: str) -> None:
        if tag not in tags:
            tags.append(tag)
    if "vision-language-action" in blob or "vla" in blob:
        add("VLA")
    if "vision-language" in blob or "vlm" in blob:
        add("Vision-Language Model")
    if "robot" in blob or "manipulation" in blob:
        add("Robotics")
    if "3d" in blob or "spatial" in blob or "geometry" in blob:
        add("3D Vision")
    if "navigation" in blob or "vln" in blob:
        add("Navigation")
    if "gaussian" in blob or "splat" in blob:
        add("Gaussian Splatting")
    if "scene graph" in blob or "graph" in blob:
        add("Graph Reasoning")
    if "diffusion" in blob:
        add("Diffusion")
    if "reinforcement" in blob or "rl" in blob:
        add("Reinforcement Learning")
    if "imitation" in blob:
        add("Imitation Learning")
    if "benchmark" in blob:
        add("Benchmark")
    if "open-vocabulary" in blob or "semantic" in blob:
        add("semantic")
    if "equivariant" in blob or "se(3)" in blob:
        add("equivariant")

    if "benchmark" in blob or "dataset" in blob:
        category = "Benchmarks and Datasets"
    elif "navigation" in blob or "vln" in blob:
        category = "Navigation and Embodied AI"
    elif "scene graph" in blob:
        category = "3D Scene Graphs and Graph Reasoning"
    elif "gaussian" in blob or "splat" in blob or "nerf" in blob or "radiance" in blob:
        category = "Language-Embedded NeRF and Gaussian Fields"
    elif "grounding" in blob or "referring" in blob or "referential" in blob:
        category = "3D Vision-Language Grounding"
    elif "vision-language-action" in blob or "vla" in blob or "robot" in blob or "manipulation" in blob:
        category = "Vision-Language-Action and Robot Manipulation"
    elif "3d" in blob and ("vision-language" in blob or "vlm" in blob or "llm" in blob):
        category = "3D Large Multimodal Models"
    else:
        category = "3D Large Multimodal Models"
    return category, tags[:8] or ["3D Vision", "Vision-Language"]


def arxiv_lookup(title: str) -> dict | None:
    if title in ARXIV_OVERRIDES:
        arxiv_id = ARXIV_OVERRIDES[title]
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": arxiv_id})
        try:
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                root = ET.fromstring(r.content)
                ns = {"a": "http://www.w3.org/2005/Atom"}
                entry = root.find("a:entry", ns)
                if entry is not None:
                    return {
                        "title": (entry.findtext("a:title", default=title, namespaces=ns) or title).strip(),
                        "arxiv": arxiv_id,
                        "abstract": re.sub(r"\s+", " ", entry.findtext("a:summary", default="", namespaces=ns)).strip(),
                        "authors": ", ".join(a.findtext("a:name", default="", namespaces=ns) for a in entry.findall("a:author", ns)[:6]),
                    }
        except Exception:
            pass
        return {"title": title, "arxiv": arxiv_id, "abstract": "", "authors": ""}

    # Use several short title slices because arXiv's exact title search is brittle.
    clean = re.sub(r"[:!?.]", " ", title)
    words = [w for w in re.split(r"\\s+", clean) if len(w) > 2 and not re.match(r"^[A-Z]{2,}[-A-Z0-9]*$", w)]
    queries = [
        f'ti:"{title}"',
        f'all:"{title}"',
        "all:" + " AND ".join(words[:8]),
        "all:" + " AND ".join(words[:5]),
    ]
    target = norm_title(title)
    for query in queries:
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
            "search_query": query,
            "start": 0,
            "max_results": 5,
            "sortBy": "relevance",
        })
        try:
            r = requests.get(url, timeout=30)
            if r.status_code != 200:
                continue
            root = ET.fromstring(r.content)
            ns = {"a": "http://www.w3.org/2005/Atom"}
            entries = root.findall("a:entry", ns)
            best = None
            best_score = -1
            for entry in entries:
                etitle = (entry.findtext("a:title", default="", namespaces=ns) or "").strip()
                nt = norm_title(etitle)
                overlap = len(set(target.split()) & set(nt.split()))
                score = overlap
                if target in nt or nt in target:
                    score += 20
                if score > best_score:
                    best_score = score
                    eid = entry.findtext("a:id", default="", namespaces=ns).split("/")[-1]
                    eid = re.sub(r"v\\d+$", "", eid)
                    best = {
                        "title": etitle,
                        "arxiv": eid,
                        "abstract": re.sub(r"\\s+", " ", entry.findtext("a:summary", default="", namespaces=ns)).strip(),
                        "authors": ", ".join(a.findtext("a:name", default="", namespaces=ns) for a in entry.findall("a:author", ns)[:6]),
                    }
            if best and best_score >= max(4, min(8, len(set(target.split())) // 2)):
                return best
        except Exception:
            pass
        time.sleep(0.2)
    return None


def openreview_papers() -> tuple[list[dict], list[dict]]:
    data = json.loads(OPENREVIEW_CANDIDATES.read_text(encoding="utf-8"))
    added = []
    missing = []
    for venueid, titles in OPENREVIEW_SELECTED.items():
        by_title = {item["title"]: item for item in data.get(venueid, [])}
        for title in titles:
            item = by_title.get(title)
            if not item:
                missing.append({"source": venueid, "title": title, "reason": "not in OpenReview candidate file"})
                continue
            category, tags = category_and_tags(item["title"], item.get("keywords") or [])
            added.append({
                "title": item["title"],
                "year": get_year_from_venueid(venueid),
                "venue": item["venue"].replace("poster", "Poster").replace("oral", "Oral").replace("spotlight", "Spotlight"),
                "pdf": item["pdf"],
                "page": item["page"],
                "abstract": item.get("abstract", ""),
                "authors": ", ".join(item.get("authors", [])[:8]) if isinstance(item.get("authors"), list) else item.get("authors", ""),
                "category": category,
                "tags": tags,
                "project": "not identified from OpenReview",
            })
    return added, missing


def icra_papers() -> tuple[list[dict], list[dict]]:
    added = []
    missing = []
    for item in ICRA_SELECTED:
        meta = arxiv_lookup(item["title"])
        if not meta:
            missing.append({**item, "reason": "arXiv PDF not found by title search"})
            continue
        category, tags = category_and_tags(item["title"], [])
        added.append({
            "title": item["title"],
            "year": item["year"],
            "venue": item["venue"],
            "arxiv": meta["arxiv"],
            "page": item["page"],
            "abstract": meta.get("abstract", ""),
            "authors": meta.get("authors", ""),
            "category": category,
            "tags": tags,
            "project": "not identified from venue audit",
        })
        time.sleep(0.3)
    return added, missing


def main() -> None:
    openreview_added, openreview_missing = openreview_papers()
    icra_added, icra_missing = icra_papers()
    all_added = openreview_added + icra_added

    # Preserve stable order and remove exact duplicate titles.
    seen = set()
    unique = []
    for item in all_added:
        key = norm_title(item["title"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)

    OUT.write_text(json.dumps(unique, ensure_ascii=False, indent=2), encoding="utf-8")
    LOG.write_text(json.dumps({
        "added": len(unique),
        "openreview_added": len(openreview_added),
        "icra_added": len(icra_added),
        "missing": openreview_missing + icra_missing,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"added {len(unique)} papers")
    print(f"openreview {len(openreview_added)}, icra {len(icra_added)}, missing {len(openreview_missing) + len(icra_missing)}")


if __name__ == "__main__":
    main()
