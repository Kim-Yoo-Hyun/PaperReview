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
IMPORTS = SOURCES / "imports"
CVF_CANDIDATES = SOURCES / "candidates" / "cvf_candidates.json"
MANIFEST = SOURCES / "papers.json"
REGISTRY_META = SOURCES / "registry_meta.json"
EXTRA_PAPERS_FILES = [
    IMPORTS / "extra_papers_2025_2026.json",
    IMPORTS / "extra_papers_eccv_iccv_ral_iros.json",
    IMPORTS / "extra_papers_3d_cv.json",
    IMPORTS / "extra_papers_priority_foundations.json",
    IMPORTS / "extra_papers_robotics.json",
    IMPORTS / "extra_papers_robotics_humanoid.json",
    IMPORTS / "extra_papers_robotics_core_expansion.json",
    IMPORTS / "extra_papers_cross_axis_gaps.json",
    IMPORTS / "extra_papers_robotics_missing_links.json",
    IMPORTS / "extra_papers_registry_carryover.json",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 literature-survey-bot (academic personal use)"
}


def arxiv_pdf(arxiv_id: str) -> str:
    return f"https://arxiv.org/pdf/{arxiv_id}"


def arxiv_abs(arxiv_id: str) -> str:
    return f"https://arxiv.org/abs/{arxiv_id}"


def pmlr_pdf(code: str) -> str:
    return f"https://raw.githubusercontent.com/mlresearch/{code.split('-')[0]}/main/assets/{code.split('-')[1]}/{code.split('-')[1]}.pdf"


MANUAL_PAPERS = [
    # Foundational CV / LLM / 3D / policy papers
    {"title": "Attention Is All You Need", "year": 2017, "venue": "NeurIPS", "arxiv": "1706.03762", "category": "Foundations: Transformer and Language Models", "tags": ["LLM", "Transformer", "representation"], "project": "https://github.com/tensorflow/tensor2tensor"},
    {"title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "year": 2019, "venue": "NAACL", "arxiv": "1810.04805", "category": "Foundations: Transformer and Language Models", "tags": ["LLM", "Transformer", "pretraining"], "project": "https://github.com/google-research/bert"},
    {"title": "Language Models are Few-Shot Learners", "year": 2020, "venue": "NeurIPS", "arxiv": "2005.14165", "category": "Foundations: Transformer and Language Models", "tags": ["LLM", "in-context learning"], "project": "not released"},
    {"title": "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale", "year": 2021, "venue": "ICLR", "arxiv": "2010.11929", "category": "Foundations: Vision Foundation Models", "tags": ["Vision Transformer", "representation"], "project": "https://github.com/google-research/vision_transformer"},
    {"title": "Learning Transferable Visual Models From Natural Language Supervision", "year": 2021, "venue": "ICML", "arxiv": "2103.00020", "category": "Foundations: Vision-Language Models", "tags": ["CLIP", "Vision-Language Model", "alignment"], "project": "https://github.com/openai/CLIP"},
    {"title": "DINOv2: Learning Robust Visual Features without Supervision", "year": 2023, "venue": "TMLR", "arxiv": "2304.07193", "category": "Foundations: Vision Foundation Models", "tags": ["self-supervised", "representation"], "project": "https://github.com/facebookresearch/dinov2"},
    {"title": "Segment Anything", "year": 2023, "venue": "ICCV", "arxiv": "2304.02643", "category": "Foundations: Vision Foundation Models", "tags": ["segmentation", "foundation model", "prompting"], "project": "https://github.com/facebookresearch/segment-anything"},
    {"title": "Denoising Diffusion Probabilistic Models", "year": 2020, "venue": "NeurIPS", "arxiv": "2006.11239", "category": "Foundations: Diffusion and Generative Models", "tags": ["Diffusion", "generation"], "project": "https://github.com/hojonathanho/diffusion"},
    {"title": "High-Resolution Image Synthesis with Latent Diffusion Models", "year": 2022, "venue": "CVPR", "arxiv": "2112.10752", "category": "Foundations: Diffusion and Generative Models", "tags": ["Diffusion", "latent representation", "generation"], "project": "https://github.com/CompVis/latent-diffusion"},
    {"title": "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis", "year": 2020, "venue": "ECCV", "arxiv": "2003.08934", "category": "Foundations: 3D Scene Representations", "tags": ["NeRF", "3D reconstruction", "representation"], "project": "https://github.com/bmild/nerf"},
    {"title": "3D Gaussian Splatting for Real-Time Radiance Field Rendering", "year": 2023, "venue": "SIGGRAPH", "arxiv": "2308.04079", "category": "Foundations: 3D Scene Representations", "tags": ["Gaussian Splatting", "3D reconstruction", "representation"], "project": "https://github.com/graphdeco-inria/gaussian-splatting"},
    {"title": "PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation", "year": 2017, "venue": "CVPR", "arxiv": "1612.00593", "category": "Foundations: 3D Geometry and Point Clouds", "tags": ["3D geometry", "point cloud", "representation"], "project": "https://github.com/charlesq34/pointnet"},
    {"title": "PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space", "year": 2017, "venue": "NeurIPS", "arxiv": "1706.02413", "category": "Foundations: 3D Geometry and Point Clouds", "tags": ["3D geometry", "point cloud", "representation"], "project": "https://github.com/charlesq34/pointnet2"},
    {"title": "SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks", "year": 2020, "venue": "NeurIPS", "arxiv": "2006.10503", "category": "Foundations: Equivariance and Geometry", "tags": ["equivariant", "3D geometry", "Transformer"], "project": "https://github.com/FabianFuchsML/se3-transformer-public"},
    {"title": "E(n) Equivariant Graph Neural Networks", "year": 2021, "venue": "ICML", "arxiv": "2102.09844", "category": "Foundations: Equivariance and Geometry", "tags": ["equivariant", "graph reasoning", "3D geometry"], "project": "https://github.com/vgsatorras/egnn"},
    {"title": "ORB-SLAM: A Versatile and Accurate Monocular SLAM System", "year": 2015, "venue": "T-RO", "arxiv": "1502.00956", "category": "Foundations: SLAM and Sensor Geometry", "tags": ["SLAM", "calibration", "geometry"], "project": "https://github.com/raulmur/ORB_SLAM2"},
    {"title": "DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras", "year": 2021, "venue": "NeurIPS", "arxiv": "2108.10869", "category": "Foundations: SLAM and Sensor Geometry", "tags": ["SLAM", "RGB-D", "geometry"], "project": "https://github.com/princeton-vl/DROID-SLAM"},
    {"title": "Decision Transformer: Reinforcement Learning via Sequence Modeling", "year": 2021, "venue": "NeurIPS", "arxiv": "2106.01345", "category": "Foundations: RL and Imitation Learning", "tags": ["Reinforcement Learning", "Transformer", "policy"], "project": "https://github.com/kzl/decision-transformer"},
    {"title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion", "year": 2023, "venue": "RSS", "arxiv": "2303.04137", "category": "Foundations: RL and Imitation Learning", "tags": ["Diffusion", "Imitation Learning", "robotics"], "project": "https://github.com/real-stanford/diffusion_policy"},
    {"title": "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances", "year": 2022, "venue": "CoRL", "arxiv": "2204.01691", "category": "Foundations: Vision-Language-Action and Robotics", "tags": ["LLM", "affordance", "Planning", "Robotics"], "project": "https://say-can.github.io/"},
    {"title": "RT-1: Robotics Transformer for Real-World Control at Scale", "year": 2022, "venue": "arxiv", "arxiv": "2212.06817", "category": "Foundations: Vision-Language-Action and Robotics", "tags": ["VLA", "Robotics", "Imitation Learning"], "project": "https://robotics-transformer1.github.io/"},
    {"title": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control", "year": 2023, "venue": "CoRL", "arxiv": "2307.15818", "category": "Foundations: Vision-Language-Action and Robotics", "tags": ["VLA", "Vision-Language Model", "Robotics"], "project": "https://robotics-transformer2.github.io/"},
    {"title": "PaLM-E: An Embodied Multimodal Language Model", "year": 2023, "venue": "ICML", "arxiv": "2303.03378", "category": "Foundations: Vision-Language-Action and Robotics", "tags": ["LLM", "Vision-Language", "Robotics"], "project": "https://palm-e.github.io/"},
    {"title": "Open X-Embodiment: Robotic Learning Datasets and RT-X Models", "year": 2024, "venue": "ICRA", "arxiv": "2310.08864", "category": "Foundations: Vision-Language-Action and Robotics", "tags": ["Robotics", "dataset", "Imitation Learning"], "project": "https://robotics-transformer-x.github.io/"},

    # 2020-2023 high-impact 3D/VL/robotics papers
    {"title": "ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language", "year": 2020, "venue": "ECCV", "arxiv": "1912.08830", "category": "3D Vision-Language Grounding", "tags": ["3D visual grounding", "RGB-D", "semantic"], "project": "https://daveredrum.github.io/ScanRefer/"},
    {"title": "ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes", "year": 2020, "venue": "ECCV", "pdf": "https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf", "page": "https://referit3d.github.io/", "category": "3D Vision-Language Grounding", "tags": ["3D visual grounding", "language", "scene"], "project": "https://github.com/referit3d/referit3d"},
    {"title": "3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds", "year": 2021, "venue": "ICCV", "pdf": "https://openaccess.thecvf.com/content/ICCV2021/papers/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.pdf", "page": "https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html", "category": "3D Vision-Language Grounding", "tags": ["3D visual grounding", "graph reasoning", "Transformer"], "project": "https://github.com/zlccccc/3DVG-Transformer"},
    {"title": "VLMaps: Visual-Language Maps for Robot Navigation", "year": 2023, "venue": "ICRA", "arxiv": "2210.05714", "category": "Navigation and Embodied AI", "tags": ["Vision-Language Navigation", "semantic map", "Robotics"], "project": "https://vlmaps.github.io/"},
    {"title": "CLIP-Fields: Weakly Supervised Semantic Fields for Robotic Memory", "year": 2023, "venue": "RSS", "arxiv": "2210.05663", "category": "Open-Vocabulary 3D Mapping", "tags": ["CLIP", "Robotics", "semantic", "NeRF"], "project": "https://mahis.life/clip-fields/"},
    {"title": "ConceptFusion: Open-set Multimodal 3D Mapping", "year": 2023, "venue": "RSS", "arxiv": "2302.07241", "category": "Open-Vocabulary 3D Mapping", "tags": ["sensor fusion", "open-vocabulary", "SLAM", "Robotics"], "project": "https://concept-fusion.github.io/"},
    {"title": "LERF: Language Embedded Radiance Fields", "year": 2023, "venue": "ICCV", "arxiv": "2303.09553", "category": "Language-Embedded NeRF and Gaussian Fields", "tags": ["NeRF", "Vision-Language", "grounding"], "project": "https://www.lerf.io/"},
    {"title": "OpenScene: 3D Scene Understanding with Open Vocabularies", "year": 2023, "venue": "CVPR", "arxiv": "2211.15654", "category": "Open-Vocabulary 3D Mapping", "tags": ["open-vocabulary", "3D semantic", "CLIP"], "project": "https://pengsongyou.github.io/openscene"},
    {"title": "OpenMask3D: Open-Vocabulary 3D Instance Segmentation", "year": 2023, "venue": "NeurIPS", "arxiv": "2306.13631", "category": "Open-Vocabulary 3D Mapping", "tags": ["open-vocabulary", "3D segmentation", "CLIP"], "project": "https://openmask3d.github.io/"},
    {"title": "3D-LLM: Injecting the 3D World into Large Language Models", "year": 2023, "venue": "NeurIPS", "arxiv": "2307.12981", "category": "3D Large Multimodal Models", "tags": ["LLM", "3D Vision", "Vision-Language"], "project": "https://vis-www.cs.umass.edu/3dllm/"},
    {"title": "3D-VisTA: Pre-trained Transformer for 3D Vision and Text Alignment", "year": 2023, "venue": "ICCV", "arxiv": "2308.04352", "category": "3D Large Multimodal Models", "tags": ["3D Vision-Language", "alignment", "Transformer"], "project": "https://3d-vista.github.io/"},
    {"title": "Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation", "year": 2023, "venue": "CoRL", "arxiv": "2209.05451", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["Robotics", "Imitation Learning", "3D manipulation"], "project": "https://peract.github.io/"},
    {"title": "RVT: Robotic View Transformer for 3D Object Manipulation", "year": 2023, "venue": "CoRL", "arxiv": "2306.14896", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["Robotics", "3D manipulation", "Transformer"], "project": "https://robotic-view-transformer.github.io/"},
    {"title": "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models", "year": 2023, "venue": "CoRL", "arxiv": "2307.05973", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["LLM", "VLM", "Planning", "Robotics"], "project": "https://voxposer.github.io/"},
    {"title": "Code as Policies: Language Model Programs for Embodied Control", "year": 2023, "venue": "ICRA", "arxiv": "2209.07753", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["LLM", "Planning", "Robotics"], "project": "https://code-as-policies.github.io/"},
    {"title": "VIMA: General Robot Manipulation with Multimodal Prompts", "year": 2023, "venue": "ICML", "arxiv": "2210.03094", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["Vision-Language-Action", "Imitation Learning", "Robotics"], "project": "https://vimalabs.github.io/"},
    {"title": "CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks", "year": 2022, "venue": "RA-L", "arxiv": "2112.03227", "category": "Benchmarks and Datasets", "tags": ["Vision-Language Action", "Benchmark", "Robotics"], "project": "https://calvin.cs.uni-freiburg.de/"},
    {"title": "Benchmarking Knowledge Transfer for Lifelong Robot Learning", "year": 2023, "venue": "NeurIPS", "arxiv": "2306.03310", "category": "Benchmarks and Datasets", "tags": ["Robotics", "Imitation Learning", "Benchmark"], "project": "https://libero-project.github.io/main.html"},
    {"title": "BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers", "year": 2022, "venue": "ECCV", "arxiv": "2203.17270", "category": "Sensor Fusion, LiDAR, and Autonomous Driving", "tags": ["sensor fusion", "3D perception", "Planning"], "project": "https://github.com/fundamentalvision/BEVFormer"},
    {"title": "BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation", "year": 2023, "venue": "ICRA", "arxiv": "2205.13542", "category": "Sensor Fusion, LiDAR, and Autonomous Driving", "tags": ["sensor fusion", "LiDAR", "3D perception"], "project": "https://github.com/mit-han-lab/bevfusion"},
    {"title": "Planning-oriented Autonomous Driving", "year": 2023, "venue": "CVPR", "arxiv": "2212.10156", "category": "Sensor Fusion, LiDAR, and Autonomous Driving", "tags": ["Planning", "sensor fusion", "3D perception"], "project": "https://github.com/OpenDriveLab/UniAD"},
    {"title": "DUSt3R: Geometric 3D Vision Made Easy", "year": 2024, "venue": "CVPR", "arxiv": "2312.14132", "category": "3D Reconstruction, Geometry, and SLAM", "tags": ["3D reconstruction", "calibration", "geometry"], "project": "https://github.com/naver/dust3r"},
    {"title": "Grounding Image Matching in 3D with MASt3R", "year": 2024, "venue": "ECCV", "arxiv": "2406.09756", "category": "3D Reconstruction, Geometry, and SLAM", "tags": ["3D geometry", "matching", "calibration"], "project": "https://github.com/naver/mast3r"},
    {"title": "SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities", "year": 2024, "venue": "CVPR", "arxiv": "2401.12168", "category": "3D Large Multimodal Models", "tags": ["Vision-Language Model", "spatial reasoning", "Robotics"], "project": "https://spatial-vlm.github.io/"},
    {"title": "LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning", "year": 2024, "venue": "CVPR", "arxiv": "2311.18651", "category": "3D Large Multimodal Models", "tags": ["LLM", "3D Vision", "Planning"], "project": "https://github.com/Open3DA/LL3DA"},
    {"title": "An Embodied Generalist Agent in 3D World", "year": 2024, "venue": "ICML", "arxiv": "2311.12871", "category": "3D Large Multimodal Models", "tags": ["LLM", "3D Vision", "Planning", "Robotics"], "project": "https://embodied-generalist.github.io/"},
    {"title": "OpenVLA: An Open-Source Vision-Language-Action Model", "year": 2024, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v270/main/assets/kim25c/kim25c.pdf", "page": "https://proceedings.mlr.press/v270/kim25c.html", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["VLA", "Robotics", "Imitation Learning"], "project": "https://github.com/openvla/openvla"},
    {"title": "Octo: An Open-Source Generalist Robot Policy", "year": 2024, "venue": "RSS", "arxiv": "2405.12213", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["Robotics", "generalist policy", "Imitation Learning"], "project": "https://octo-models.github.io/"},
    {"title": "VLM-Grounder: A VLM Agent for Zero-Shot 3D Visual Grounding", "year": 2024, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v270/main/assets/xu25c/xu25c.pdf", "page": "https://proceedings.mlr.press/v270/xu25c.html", "category": "3D Vision-Language Grounding", "tags": ["3D visual grounding", "VLM", "zero-shot"], "project": "https://github.com/InternRobotics/VLM-Grounder"},
    {"title": "ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation", "year": 2024, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v270/main/assets/huang25g/huang25g.pdf", "page": "https://proceedings.mlr.press/v270/huang25g.html", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["Planning", "3D geometry", "Robotics", "VLM"], "project": "https://github.com/huangwl18/ReKep"},
    {"title": "VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation", "year": 2024, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v270/main/assets/liu25i/liu25i.pdf", "page": "https://proceedings.mlr.press/v270/liu25i.html", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["VLM", "3D manipulation", "bimanual", "Robotics"], "project": "https://voxact-b.github.io/"},
    {"title": "VGGT: Visual Geometry Grounded Transformer", "year": 2025, "venue": "CVPR", "arxiv": "2503.11651", "category": "3D Reconstruction, Geometry, and SLAM", "tags": ["3D reconstruction", "geometry", "Transformer"], "project": "https://github.com/facebookresearch/vggt"},
    {"title": "Continuous 3D Perception Model with Persistent State", "year": 2025, "venue": "CVPR", "arxiv": "2501.12387", "category": "3D Reconstruction, Geometry, and SLAM", "tags": ["3D reconstruction", "SLAM", "representation"], "project": "https://cut3r.github.io/"},
    {"title": "3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation", "year": 2025, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf", "page": "https://proceedings.mlr.press/v305/li25g.html", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["VLA", "3D Vision", "Robotics"], "project": "https://vis-www.cs.umass.edu/3ds-vla/"},
    {"title": "Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation", "year": 2025, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v305/main/assets/fan25a/fan25a.pdf", "page": "https://proceedings.mlr.press/v305/fan25a.html", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["VLA", "Planning", "Robotics"], "project": "not identified"},
    {"title": "MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation", "year": 2025, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25c/wu25c.pdf", "page": "https://proceedings.mlr.press/v305/wu25c.html", "category": "Navigation and Embodied AI", "tags": ["Navigation", "mobile manipulation", "VLM"], "project": "not identified"},
    {"title": "π0.5: a Vision-Language-Action Model with Open-World Generalization", "year": 2025, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v305/main/assets/black25a/black25a.pdf", "page": "https://proceedings.mlr.press/v305/black25a.html", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["VLA", "open-world", "Robotics"], "project": "https://www.physicalintelligence.company/blog/pi05"},
    {"title": "GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data", "year": 2025, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v305/main/assets/deng25a/deng25a.pdf", "page": "https://proceedings.mlr.press/v305/deng25a.html", "category": "Vision-Language-Action and Robot Manipulation", "tags": ["VLA", "grasping", "synthetic data"], "project": "not identified"},
    {"title": "SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation", "year": 2025, "venue": "CoRL", "pdf": "https://raw.githubusercontent.com/mlresearch/v305/main/assets/munje25a/munje25a.pdf", "page": "https://proceedings.mlr.press/v305/munje25a.html", "category": "Navigation and Embodied AI", "tags": ["VLM", "Navigation", "Benchmark"], "project": "not identified"},
    {"title": "GenSplat: Bridging the Generalization Gap in 3DGS Language Comprehension", "year": 2026, "venue": "CVPR", "pdf": "https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_GenSplat_Bridging_the_Generalization_Gap_in_3DGS_Language_Comprehension_CVPR_2026_paper.pdf", "page": "https://openaccess.thecvf.com/content/CVPR2026/html/Liu_GenSplat_Bridging_the_Generalization_Gap_in_3DGS_Language_Comprehension_CVPR_2026_paper.html", "category": "Language-Embedded NeRF and Gaussian Fields", "tags": ["Gaussian Splatting", "language", "generalization"], "project": "not identified from primary page"},
    {"title": "ST4R-Splat: Spatio-Temporal Referring Segmentation in 4D Gaussian Splatting", "year": 2026, "venue": "CVPR", "pdf": "https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.pdf", "page": "https://openaccess.thecvf.com/content/CVPR2026/html/Meng_ST4R-Splat_Spatio-Temporal_Referring_Segmentation_in_4D_Gaussian_Splatting_CVPR_2026_paper.html", "category": "Language-Embedded NeRF and Gaussian Fields", "tags": ["Gaussian Splatting", "4D", "referring segmentation"], "project": "not identified from primary page"},
]


CVF_TITLES = [
    # 2024 top-tier CVF pass
    ("LangSplat: 3D Language Gaussian Splatting", "Language-Embedded NeRF and Gaussian Fields", ["Gaussian Splatting", "Vision-Language", "grounding"]),
    ("Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding", "Language-Embedded NeRF and Gaussian Fields", ["Gaussian Splatting", "open-vocabulary", "semantic"]),
    ("Open3DSG: Open-Vocabulary 3D Scene Graphs from Point Clouds with Queryable Objects and Open-Set Relationships", "3D Scene Graphs and Graph Reasoning", ["3D Scene Graph", "open-vocabulary", "Graph Reasoning"]),
    ("CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning", "3D Scene Graphs and Graph Reasoning", ["3D Scene Graph", "CLIP", "Graph Reasoning"]),
    ("EmbodiedScan: A Holistic Multi-Modal 3D Perception Suite Towards Embodied AI", "Benchmarks and Datasets", ["3D Vision", "Embodied AI", "dataset"]),
    ("SUGAR: Pre-training 3D Visual Representations for Robotics", "Vision-Language-Action and Robot Manipulation", ["3D representation", "Robotics", "pretraining"]),
    ("Diffusion-EDFs: Bi-equivariant Denoising Generative Modeling on SE(3) for Visual Robotic Manipulation", "Equivariance, Diffusion, and 3D Action", ["equivariant", "Diffusion", "Robotics"]),
    ("Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation", "Equivariance, Diffusion, and 3D Action", ["Diffusion", "Robotics", "Imitation Learning"]),
    ("Generate Subgoal Images before Act: Unlocking the Chain-of-Thought Reasoning in Diffusion Model for Robot Manipulation with Multimodal Prompts", "Vision-Language-Action and Robot Manipulation", ["Diffusion", "VLA", "Planning"]),
    ("ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation", "Vision-Language-Action and Robot Manipulation", ["LLM", "Robotics", "Vision-Language"]),
    ("Holodeck: Language Guided Generation of 3D Embodied AI Environments", "Navigation and Embodied AI", ["Generation", "3D scene", "Embodied AI"]),
    ("MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World", "3D Large Multimodal Models", ["LLM", "3D Vision", "sensor fusion"]),
    ("Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation", "Navigation and Embodied AI", ["Vision-Language Navigation", "NeRF", "Planning"]),
    ("Volumetric Environment Representation for Vision-Language Navigation", "Navigation and Embodied AI", ["Vision-Language Navigation", "3D geometry", "representation"]),
    ("GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting", "3D Reconstruction, Geometry, and SLAM", ["SLAM", "Gaussian Splatting", "geometry"]),
    ("RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding", "Open-Vocabulary 3D Mapping", ["point-language", "open-world", "semantic"]),
    ("Towards CLIP-driven Language-free 3D Visual Grounding via 2D-3D Relational Enhancement and Consistency", "3D Vision-Language Grounding", ["3D visual grounding", "CLIP", "consistency"]),

    # 2025 CVF / ICCV / WACV
    ("RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics", "3D Large Multimodal Models", ["VLM", "spatial reasoning", "Robotics"]),
    ("CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models", "Vision-Language-Action and Robot Manipulation", ["VLA", "Chain-of-Thought", "Robotics"]),
    ("PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation", "Equivariance, Diffusion, and 3D Action", ["Diffusion", "Robotics", "3D action"]),
    ("ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning", "Language-Embedded NeRF and Gaussian Fields", ["Gaussian Splatting", "grounding", "LVLM"]),
    ("Dr. Splat: Directly Referring 3D Gaussian Splatting via Direct Language Embedding Registration", "Language-Embedded NeRF and Gaussian Fields", ["Gaussian Splatting", "language embedding", "grounding"]),
    ("Chain of Semantics Programming in 3D Gaussian Splatting Representation for 3D Vision Grounding", "Language-Embedded NeRF and Gaussian Fields", ["Gaussian Splatting", "semantic", "grounding"]),
    ("SeeGround: See and Ground for Zero-Shot Open-Vocabulary 3D Visual Grounding", "3D Vision-Language Grounding", ["3D visual grounding", "zero-shot", "open-vocabulary"]),
    ("RoboGround: Robotic Manipulation with Grounded Vision-Language Priors", "Vision-Language-Action and Robot Manipulation", ["VLM", "grounding", "Robotics"]),
    ("Lift3D Policy: Lifting 2D Foundation Models for Robust 3D Robotic Manipulation", "Vision-Language-Action and Robot Manipulation", ["3D Vision", "foundation model", "Robotics"]),
    ("Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation", "Vision-Language-Action and Robot Manipulation", ["VLA", "prompting", "Robotics"]),
    ("SpatialLLM: A Compound 3D-Informed Design towards Spatially-Intelligent Large Multimodal Models", "3D Large Multimodal Models", ["LLM", "spatial reasoning", "3D Vision"]),
    ("AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning", "Open-Vocabulary 3D Mapping", ["open-vocabulary", "semantic", "alignment"]),
    ("Scene-LLM: Extending Language Model for 3D Visual Reasoning", "3D Large Multimodal Models", ["LLM", "3D visual reasoning", "Vision-Language"]),
    ("3D Gaussian Map with Open-Set Semantic Grouping for Vision-Language Navigation", "Navigation and Embodied AI", ["Gaussian Splatting", "Vision-Language Navigation", "semantic"]),
    ("Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation", "Navigation and Embodied AI", ["Navigation", "grounding", "exploration"]),
    ("Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy", "Vision-Language-Action and Robot Manipulation", ["VLA", "Diffusion", "Transformer"]),
    ("VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks", "Benchmarks and Datasets", ["VLA", "Benchmark", "long-horizon"]),
    ("GWM: Towards Scalable Gaussian World Models for Robotic Manipulation", "Vision-Language-Action and Robot Manipulation", ["Gaussian Splatting", "world model", "Robotics"]),
    ("SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining", "Language-Embedded NeRF and Gaussian Fields", ["Gaussian Splatting", "Vision-Language", "semantic"]),
    ("AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting", "Open-Vocabulary 3D Mapping", ["semantic occupancy", "Vision-Language", "Gaussian Splatting"]),
    ("3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding", "3D Scene Graphs and Graph Reasoning", ["3D Scene Graph", "LLM", "Graph Reasoning"]),

    # 2026 CVPR current pass
    ("D3D-VLP: Dynamic 3D Vision-Language-Planning Model for Embodied Grounding and Navigation", "Navigation and Embodied AI", ["3D Vision", "Vision-Language", "Planning", "Navigation"]),
    ("EmbodiedSplat: Online Feed-Forward Semantic 3DGS for Open-Vocabulary 3D Scene Understanding", "Language-Embedded NeRF and Gaussian Fields", ["Gaussian Splatting", "open-vocabulary", "semantic"]),
    ("ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation", "Vision-Language-Action and Robot Manipulation", ["VLA", "active perception", "3D manipulation"]),
    ("ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation", "Vision-Language-Action and Robot Manipulation", ["VLA", "consistency", "4D reasoning"]),
    ("Localizing, Structuring, and Rendering: Bridging 3D and 2D Vision-Language-Action Models for Robotic Manipulation", "Vision-Language-Action and Robot Manipulation", ["VLA", "3D-2D alignment", "Robotics"]),
    ("G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning", "3D Large Multimodal Models", ["VLM", "3D reconstruction", "spatial reasoning"]),
    ("MSGNav: Unleashing the Power of Multi-modal 3D Scene Graph for Zero-Shot Embodied Navigation", "Navigation and Embodied AI", ["3D Scene Graph", "Navigation", "zero-shot"]),
    ("SpatialStack: Layered Geometry-Language Fusion for 3D VLM Spatial Reasoning", "3D Large Multimodal Models", ["geometry", "VLM", "spatial reasoning"]),
    ("GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation", "Navigation and Embodied AI", ["Vision-Language Navigation", "geometry", "BEV"]),
    ("Grounded 3D-Aware Spatial Vision-Language Modeling", "3D Large Multimodal Models", ["Vision-Language", "3D spatial", "grounding"]),
    ("SemanticVLA: Towards Semantic Reasoning over Action Memorization via Synergistic Explicit Trace and Latent Action Planning", "Vision-Language-Action and Robot Manipulation", ["VLA", "semantic reasoning", "Planning"]),
    ("ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models", "Vision-Language-Action and Robot Manipulation", ["VLA", "Chain-of-Thought", "Planning"]),
    ("SaPaVe: Towards Active Perception and Manipulation in Vision-Language Action Models for Robotics", "Vision-Language-Action and Robot Manipulation", ["VLA", "active perception", "Robotics"]),
    ("OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting", "Open-Vocabulary 3D Mapping", ["Gaussian Splatting", "semantic mapping", "open-vocabulary"]),
    ("LightSplat: Fast and Memory-Efficient Open-Vocabulary 3D Scene Understanding in Five Seconds", "Language-Embedded NeRF and Gaussian Fields", ["Gaussian Splatting", "open-vocabulary", "efficiency"]),
    ("LangRef3DGS: Natural Language-Guided 3D Referential Segmentation from Partial Observations via 3D Gaussian Splatting", "Language-Embedded NeRF and Gaussian Fields", ["Gaussian Splatting", "referring segmentation", "language"]),
    ("RealVLG-R1: A Large-Scale Real-World Visual-Language Grounding Benchmark for Robotic Perception and Manipulation", "Benchmarks and Datasets", ["Visual-Language Grounding", "Benchmark", "Robotics"]),
    ("SIMPACT: Simulation-Enabled Action Planning using Vision-Language Models", "Vision-Language-Action and Robot Manipulation", ["VLM", "Planning", "simulation"]),
    ("DiffuView: Multi-View Diffusion Pretraining for 3D Aware Robotic Manipulation", "Equivariance, Diffusion, and 3D Action", ["Diffusion", "3D manipulation", "Robotics"]),
]


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



def load_cvf_map() -> dict[str, dict]:
    if not CVF_CANDIDATES.exists():
        return {}
    items = json.loads(CVF_CANDIDATES.read_text(encoding="utf-8"))
    return {item["title"]: item for item in items}


def build_papers() -> list[dict]:
    papers = []
    for item in MANUAL_PAPERS:
        p = dict(item)
        if "arxiv" in p:
            p.setdefault("pdf", arxiv_pdf(p["arxiv"]))
            p.setdefault("page", arxiv_abs(p["arxiv"]))
        p["source_kind"] = "manual"
        papers.append(p)

    for extra_file in EXTRA_PAPERS_FILES:
        if not extra_file.exists():
            continue
        for item in json.loads(extra_file.read_text(encoding="utf-8")):
            p = dict(item)
            if "arxiv" in p:
                p.setdefault("pdf", arxiv_pdf(p["arxiv"]))
                p.setdefault("page", arxiv_abs(p["arxiv"]))
            p["source_kind"] = extra_file.stem
            papers.append(p)

    cvf_map = load_cvf_map()
    for title, category, tags in CVF_TITLES:
        item = cvf_map.get(title)
        if not item:
            print(f"[warn] CVF title not found in candidates: {title}")
            continue
        year_match = re.search(r"(20\d{2})", item["venue"])
        year = int(year_match.group(1)) if year_match else 0
        p = {
            "title": title,
            "year": year,
            "venue": item["venue"].replace("CVPR", "CVPR ").replace("ICCV", "ICCV ").replace("WACV", "WACV ").strip(),
            "pdf": item.get("pdf"),
            "page": item.get("page"),
            "category": category,
            "tags": tags,
            "project": "not identified from primary page",
            "source_kind": "cvf",
        }
        papers.append(p)

    # Deduplicate by title while preserving first occurrence.
    seen = set()
    unique = []
    for p in papers:
        key = p["title"].lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(canonicalize(p))
    return unique


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
    WORK.mkdir(exist_ok=True)
    papers = build_papers()
    existing_by_title = {}
    if MANIFEST.exists():
        existing_by_title = {
            item["title"].casefold(): item
            for item in json.loads(MANIFEST.read_text(encoding="utf-8"))
        }
    for paper in papers:
        existing = existing_by_title.get(paper["title"].casefold(), {})
        paper["folder"] = existing.get("folder") or folder_name(paper)
    print(f"[info] selected papers: {len(papers)}")

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
