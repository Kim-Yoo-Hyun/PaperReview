#!/usr/bin/env python3
"""Build the 3D vision + robotics + vision-language literature survey.

The script intentionally keeps notes concise and provenance-heavy. It downloads
the primary PDF where available, extracts lightweight metadata, and creates the
folder/markdown registry requested by the user.
"""

from __future__ import annotations

import concurrent.futures
import html
import json
import os
import re
import shutil
import subprocess
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "survey_work"
CVF_CANDIDATES = WORK / "cvf_candidates.json"
EXTRA_PAPERS_FILES = [
    WORK / "extra_papers_2025_2026.json",
    WORK / "extra_papers_eccv_iccv_ral_iros.json",
    WORK / "extra_papers_3d_cv.json",
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
        unique.append(p)
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
    p["folder"] = str(out_dir.relative_to(ROOT))
    if pdf_path.exists() and pdf_path.stat().st_size > 20_000:
        p["pdf_status"] = "downloaded"
        return p
    url = p.get("pdf")
    if not url:
        (out_dir / "paper_pdf_error.txt").write_text("No PDF URL identified.\n", encoding="utf-8")
        p["pdf_status"] = "missing-url"
        return p
    try:
        with requests.get(url, headers=HEADERS, timeout=45, stream=True, allow_redirects=True) as r:
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


def write_notes(p: dict) -> None:
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
- PDF status: {p.get('pdf_status', 'unknown')}
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

    problem_md = f"""# Problem

## 왜 문제인가
{problem}

## 해결하려는 문제
- 연구 유형: {fam}
- 목표: 3D geometry/semantics와 language/action 사이의 mismatch를 줄이고, 실제 embodied setting에서 쓸 수 있는 표현 또는 policy를 만드는 것.
- 중요한 이유: 로봇은 closed-set category 인식보다 더 복합적인 공간 관계, affordance, 장기 계획, sensor noise를 다뤄야 한다.
- Abstract problem cue: {cues.get('problem', '자동 추출 없음.')}

## 선행 연구 분석
- 2D VLM/LLM은 semantic prior가 강하지만 metric 3D 구조와 physical feasibility가 약하다.
- 고전 3D geometry/SLAM은 구조적 안정성이 있지만 open-vocabulary language grounding과 high-level reasoning이 약하다.
- 이 논문은 두 축을 결합하는 흐름 안에서, `{', '.join(tags[:4])}` 관점의 개선을 제안한다.
"""

    method_md = f"""# Method

## Brief Method
{method}

## Abstract Method Cue
{cues.get('method', '자동 추출 없음.')}

## 원리적 동기
- 3D 구조는 물체 간 거리, pose, occlusion, affordance를 제공한다.
- Vision-language/LLM prior는 open vocabulary와 commonsense를 제공한다.
- 두 표현을 alignment하면 annotation-heavy 3D supervision 없이도 더 넓은 task로 확장할 수 있다.

## 핵심 방법론
- Task family: {fam}
- Representation: {', '.join([t for t in tags if any(k in t.lower() for k in ['3d', 'gaussian', 'nerf', 'graph', 'geometry', 'slam', 'semantic', 'vla', 'vlm', 'llm'])]) or 'paper-specific representation'}
- Training/optimization: paper-specific; PDF의 method section에서 loss, supervision, inference pipeline 확인 필요.
- Deployment assumption: sensor calibration, scene reconstruction quality, and action feasibility are likely critical when moved to real robots.
"""

    evaluation_md = f"""# Evaluation

## Dataset
{', '.join(datasets) if datasets else 'PDF/abstract 자동 추출에서 명확한 dataset 명칭을 찾지 못함. 본문의 experiment section 확인 필요.'}

## Benchmark
- 주요 benchmark는 task family `{fam}`에 맞춰 3D grounding, segmentation, reconstruction, navigation, manipulation success, 또는 VQA 형태로 구성된다.

## Metrics
{', '.join(metrics) if metrics else '관련 후보: success rate, IoU/mIoU, Acc@k, SPL/nDTW, PSNR/SSIM/LPIPS, ATE/RPE 등 task별 확인 필요.'}

## Splits
- 자동 추출로 split 세부사항은 안정적으로 확인하지 않았다.
- 재현 시 train/val/test scene split, object split, instruction split, embodiment split을 분리해서 확인할 것.

## Baselines
- 비교 기준은 보통 closed-set 3D model, 2D VLM projection, prior 3D grounding/model-free policy, classical geometry/SLAM, 또는 diffusion/action-policy baseline이다.

## Main Results
- Abstract result cue: {cues.get('result', '자동 추출 없음.')}
- 정확한 수치는 paper.pdf의 tables를 기준으로 확인할 것.

## Reproducibility Notes
- Code/Project: {project}
- PDF status: {p.get('pdf_status', 'unknown')}
- 재현 난이도 체크포인트: data availability, pretrained model checkpoint, camera/depth calibration, GPU memory, simulator/real-robot dependency.
"""

    insights_md = f"""# Insights

## Limitation
{limitation}

## Strength
- `{fam}` 문제를 3D geometry와 language/action prior를 함께 쓰는 방향으로 밀어붙인다.
- 사용자의 연구 키워드 중 `{', '.join(tags[:5])}`와 직접적으로 연결된다.

## Paper Claim
- 논문의 중심 claim은 기존 2D-only, closed-set, 또는 task-specific 접근보다 더 일반화 가능한 3D-aware representation/policy/reasoning을 제공한다는 것이다.
- Abstract result cue: {cues.get('result', '자동 추출 없음.')}

## Future Work
- dynamic scene, partial observation, sensor noise, cross-embodiment transfer, real-time inference, safety-aware planning을 추가 검증하는 것이 중요하다.
- 3D scene graph/semantic Gaussian/SLAM map을 VLA policy의 persistent memory로 연결하는 방향이 유망하다.

## 내 관점
- 이 논문은 `{p['category']}` 축에서 읽어야 한다.
- 후속 연구 아이디어: language-grounded 3D memory를 만들고, robot policy가 이를 action feasibility와 uncertainty까지 포함해 조회하도록 설계한다.
"""

    files = {
        "01_overview.md": overview,
        "02_problem.md": problem_md,
        "03_method.md": method_md,
        "04_evaluation.md": evaluation_md,
        "05_insights.md": insights_md,
    }
    for name, content in files.items():
        (out_dir / name).write_text(content, encoding="utf-8")


def write_registry(papers: list[dict]) -> None:
    papers_sorted = sorted(papers, key=lambda p: (p["category"], p["year"], p["title"]))
    by_cat: dict[str, list[dict]] = {}
    for p in papers_sorted:
        by_cat.setdefault(p["category"], []).append(p)

    lines = [
        "# PAPER Registry",
        "",
        f"- Generated: {time.strftime('%Y-%m-%d %H:%M:%S %Z')}",
        f"- Total papers with folders: {len(papers_sorted)}",
        "- Scope: 3D Vision + Robotics + Vision-Language, with recent top-tier CVF/PMLR/arXiv primary PDFs and foundational CV/LLM/robotics papers.",
        "- Note: `survey_work/cvf_candidates.json` contains the broad CVF keyword census used for the 2024-current screening pass.",
        "",
        "## Reading Priority",
        "1. VLA/robotics: OpenVLA, Octo, RT-2, Diffusion Policy, PerAct, RVT, VoxPoser, ReKep, 3DS-VLA, CoT-VLA, ActiveVLA.",
        "2. 3D language grounding: ScanRefer, ReferIt3D, 3DVG-Transformer, 3D-VisTA, VLM-Grounder, RoboSpatial, ReasonGrounder.",
        "3. 3D semantic memory/fields: CLIP-Fields, ConceptFusion, LERF, OpenScene, LangSplat, Open3DSG, OnlinePG.",
        "4. Geometry backbone: PointNet/PointNet++, NeRF, 3DGS, DUSt3R, MASt3R, VGGT, CUT3R, DROID-SLAM.",
        "",
    ]

    for cat, items in by_cat.items():
        lines.append(f"## {cat}")
        lines.append("")
        lines.append("| Year | Venue | Paper | Tags | PDF | Code/Project |")
        lines.append("|---:|---|---|---|---|---|")
        for p in items:
            folder = p["folder"]
            title_link = f"[{p['title']}](./{urllib.parse.quote(folder)}/01_overview.md)"
            pdf_link = f"[paper.pdf](./{urllib.parse.quote(folder)}/paper.pdf)" if (ROOT / folder / "paper.pdf").exists() else "missing"
            proj = p.get("project", "not identified")
            if proj and proj.startswith("http"):
                proj_cell = f"[link]({proj})"
            else:
                proj_cell = proj
            venue_label = venue_for_registry(p["venue"])
            lines.append(f"| {p['year']} | {venue_label} | {title_link} | {', '.join(p.get('tags', []))} | {pdf_link} | {proj_cell} |")
        lines.append("")

    lines += [
        "## Keyword Index",
        "",
    ]
    keywords: dict[str, list[dict]] = {}
    for p in papers_sorted:
        for tag in p.get("tags", []):
            keywords.setdefault(tag, []).append(p)
    for tag in sorted(keywords, key=lambda s: s.lower()):
        refs = ", ".join(f"[{safe_slug(p['title'], 24)}](./{urllib.parse.quote(p['folder'])}/01_overview.md)" for p in keywords[tag][:12])
        lines.append(f"- **{tag}**: {refs}")

    (ROOT / "PAPER.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_manifest(papers: list[dict]) -> None:
    manifest = []
    for p in papers:
        manifest.append({k: p.get(k) for k in ["title", "year", "venue", "category", "tags", "folder", "pdf", "page", "project", "pdf_status"]})
    (WORK / "selected_papers.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    WORK.mkdir(exist_ok=True)
    papers = build_papers()
    print(f"[info] selected papers: {len(papers)}")

    fetch_arxiv_metadata(papers)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        list(ex.map(fetch_page_metadata, papers))

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        papers = list(ex.map(download_pdf, papers))

    for p in papers:
        write_notes(p)

    write_registry(papers)
    write_manifest(papers)

    downloaded = sum(1 for p in papers if p.get("pdf_status") == "downloaded")
    print(f"[info] PDFs downloaded: {downloaded}/{len(papers)}")
    print(f"[info] registry: {ROOT / 'PAPER.md'}")


if __name__ == "__main__":
    main()
