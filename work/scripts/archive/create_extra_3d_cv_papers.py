#!/usr/bin/env python3
"""Create a 3D-computer-vision-first supplement."""

from __future__ import annotations

import csv
import html
import io
import json
import re
import urllib.parse
from pathlib import Path

import requests

from create_extra_venue_papers import norm_title


WORK = Path(__file__).resolve().parent
CVF_CANDIDATES = WORK / "cvf_candidates.json"
OPENREVIEW_CANDIDATES = WORK / "openreview_2025_2026_candidates.json"
OUT = WORK / "extra_papers_3d_cv.json"
LOG = WORK / "extra_papers_3d_cv_log.json"

ECVA_PAPERS = "https://www.ecva.net/papers.php"
THREEDV_CSV = "https://3dvconf.github.io/2025/schedule_updated2.csv"


FOUNDATIONAL_ARXIV = [
    ("Dynamic Graph CNN for Learning on Point Clouds", 2019, "TOG", "1801.07829", "Foundations: 3D Representation Learning"),
    ("KPConv: Flexible and Deformable Convolution for Point Clouds", 2019, "ICCV", "1904.08889", "Foundations: 3D Representation Learning"),
    ("4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks", 2019, "CVPR", "1904.08755", "Foundations: 3D Representation Learning"),
    ("Point Transformer", 2021, "ICCV", "2012.09164", "Foundations: 3D Representation Learning"),
    ("CenterPoint: Center-based 3D Object Detection and Tracking", 2021, "CVPR", "2006.11275", "Foundations: 3D Detection and BEV Perception"),
    ("Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling", 2022, "CVPR", "2111.14819", "Foundations: 3D Representation Learning"),
    ("Point-MAE: Masked Autoencoders for Point Cloud Self-supervised Learning", 2022, "ECCV", "2203.06604", "Foundations: 3D Representation Learning"),
    ("PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection", 2020, "CVPR", "1912.13192", "Foundations: 3D Detection and BEV Perception"),
    ("PETR: Position Embedding Transformation for Multi-View 3D Object Detection", 2022, "ECCV", "2203.05625", "Foundations: 3D Detection and BEV Perception"),
    ("BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection", 2023, "AAAI", "2206.10092", "Foundations: 3D Detection and BEV Perception"),
    ("VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion", 2023, "CVPR", "2302.12251", "Foundations: 3D Semantic Occupancy"),
    ("Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data", 2024, "CVPR", "2401.10891", "Foundations: Monocular Geometry"),
    ("Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation", 2024, "CVPR", "2312.02145", "Foundations: Monocular Geometry"),
    ("Depth Anything V2", 2024, "NeurIPS", "2406.09414", "Foundations: Monocular Geometry"),
    ("UniDepth: Universal Monocular Metric Depth Estimation", 2024, "CVPR", "2403.18913", "Foundations: Monocular Geometry"),
]


CVF_TITLES = [
    # CVPR 2024: reconstruction, 3DGS, LiDAR, diffusion, semantic geometry.
    "pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction",
    "SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering",
    "SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM",
    "ReconFusion: 3D Reconstruction with Diffusion Priors",
    "Scaling Diffusion Models to Real-World 3D LiDAR Scene Completion",
    "Diffusion 3D Features (Diff3F): Decorating Untextured Shapes with Distilled Semantic Features",
    "3DiffTection: 3D Object Detection with Geometry-Aware Diffusion Features",
    "SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks",
    "HandDiff: 3D Hand Pose Estimation with Diffusion on Image-Point Cloud",
    "IPoD: Implicit Field Learning with Point Diffusion for Generalizable 3D Object Reconstruction from Single RGB-D Images",
    "Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers",
    "Total-Decom: Decomposed 3D Scene Reconstruction with Minimal Interaction",
    "PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar",
    "3D Geometry-Aware Deformable Gaussian Splatting for Dynamic View Synthesis",
    "MVIP-NeRF: Multi-view 3D Inpainting on NeRF Scenes via Diffusion Prior",
    "Bayesian Diffusion Models for 3D Shape Reconstruction",
    "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",
    "TIGER: Time-Varying Denoising Model for 3D Point Cloud Generation with Diffusion Process",
    "GaussianDreamer: Fast Generation from Text to 3D Gaussians by Bridging 2D and 3D Diffusion Models",
    "Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models",

    # CVPR 2025.
    "SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction",
    "UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting",
    "DroneSplat: 3D Gaussian Splatting for Robust 3D Reconstruction from In-the-Wild Drone Imagery",
    "SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving",
    "Rethinking Temporal Fusion with a Unified Gradient Descent View for 3D Semantic Occupancy Prediction",
    "V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection",
    "Touch2Shape: Touch-Conditioned 3D Diffusion for Shape Exploration and Reconstruction",
    "CraftsMan3D: High-fidelity Mesh Generation with 3D Native Diffusion and Interactive Geometry Refiner",
    "PartGen: Part-level 3D Generation and Reconstruction with Multi-view Diffusion Models",
    "SeaLion: Semantic Part-Aware Latent Point Diffusion Models for 3D Generation",
    "DIFIX3D+: Improving 3D Reconstructions with Single-Step Diffusion Models",
    "DiET-GS: Diffusion Prior and Event Stream-Assisted Motion Deblurring 3D Gaussian Splatting",
    "EAP-GS: Efficient Augmentation of Pointcloud for 3D Gaussian Splatting in Few-shot Scene Reconstruction",
    "Taming Video Diffusion Prior with Scene-Grounding Guidance for 3D Gaussian Splatting from Sparse Inputs",
    "High-fidelity 3D Object Generation from Single Image with RGBN-Volume Gaussian Reconstruction Model",
    "Light Transport-aware Diffusion Posterior Sampling for Single-View Reconstruction of 3D Volumes",
    "G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation",

    # CVPR 2026.
    "Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images",
    "TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction",
    "E2EGS: Event-to-Edge Gaussian Splatting for Pose-Free 3D Reconstruction",
    "ExtrinSplat: Decoupling Geometry and Semantics for Open-Vocabulary Understanding in 3D Gaussian Splatting",
    "Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction",
    "PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting",
    "3D Gaussian Splatting with Self-Constrained Priors for High Fidelity Surface Reconstruction",
    "AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM",
    "BA-GS: Bayesian Adaptive Gaussian Splatting for SFM-Free 3D Reconstruction",
    "C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion",
    "Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting",
    "DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures",
    "GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator",
    "GaussianZoom: Progressive Zoom-in Generative 3D Gaussian Splatting with Geometric and Semantic Guidance",
    "Geometry-Aware Cross-Modal Graph Alignment for Referring Segmentation in 3D Gaussian Splatting",
    "HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction",
    "L3DR: 3D-aware LiDAR Diffusion and Rectification",
    "MAPo: Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for High-Fidelity Dynamic Scene Reconstruction",
    "NG-GS: NeRF-guided 3D Gaussian Splatting Segmentation",
    "Ov3R: Open-Vocabulary Semantic 3D Reconstruction from RGB Videos",
    "SDGS: Spatial Difference Guided Gaussian Splatting for Simultaneous Localization and 3D Reconstruction",
    "SR3R: Rethinking Super-Resolution 3D Reconstruction With Feed-Forward Gaussian Splatting",
    "Urban-GS: A Unified 3D Gaussian Splatting Framework for Compact and High-Fidelity Aerial-to-Street Reconstruction",
    "VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM",
    "GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance",

    # ICCV 2025.
    "Dream-to-Recon: Monocular 3D Reconstruction with Diffusion-Depth Distillation from Single Images",
    "FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction",
    "RayletDF: Raylet Distance Fields for Generalizable 3D Surface Reconstruction from Point Clouds or Gaussians",
    "RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction",
    "Distilling Diffusion Models to Efficient 3D LiDAR Scene Completion",
    "RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes",
    "GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting",
    "SEGS-SLAM: Structure-enhanced 3D Gaussian Splatting SLAM with Appearance Embedding",
    "SpatialSplat: Efficient Semantic 3D from Sparse Unposed Images",
    "MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions",
    "QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization",
    "DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction",
    "ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera Samplings and Diffusion Priors",
    "GSV3D: Gaussian Splatting-based Geometric Distillation with Stable Video Diffusion for Single-Image 3D Object Generation",
    "A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision",
    "Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors",
    "NeRF Is a Valuable Assistant for 3D Gaussian Splatting",
    "Liberated-GS: 3D Gaussian Splatting Independent from SfM Point Clouds",
    "DiGA3D: Coarse-to-Fine Diffusional Propagation of Geometry and Appearance for Versatile 3D Inpainting",
    "Tree Skeletonization from 3D Point Clouds by Denoising Diffusion",
    "VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling",
    "Repurposing 2D Diffusion Models with Gaussian Atlas for 3D Generation",
    "Robust and Efficient 3D Gaussian Splatting for Urban Scene Reconstruction",
    "Learning 3D Object Spatial Relationships from Pre-trained 2D Diffusion Models",

    # WACV 2025.
    "DepthSSC: Monocular 3D Semantic Scene Completion via Depth-Spatial Alignment and Voxel Adaptation",
    "Test-Time Adaptation of 3D Point Clouds via Denoising Diffusion Models",
    "UW-GS: Distractor-Aware 3D Gaussian Splatting for Enhanced Underwater Scene Reconstruction",
]


ECCV_TITLES = [
    "MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images",
    "GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting",
    "MVSGaussian: Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo",
    "GeoCalib: Learning Single-image Calibration with Geometric Optimization",
    "GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction",
    "CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field",
    "GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering",
    "GaussReg: Fast 3D Registration with Gaussian Splatting",
    "SAGS: Structure-Aware 3D Gaussian Splatting",
    "Surface Reconstruction for 3D Gaussian Splatting via Local Structural Hints",
    "Gaussian Grouping: Segment and Edit Anything in 3D Scenes",
    "SG-NeRF: Neural Surface Reconstruction with Scene Graph Optimization",
]


OPENREVIEW_TITLES = [
    # ICLR 2025.
    "No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images",
    "SplatFormer: Point Transformer for Robust 3D Gaussian Splatting",
    "CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes",
    "GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting",
    "ComPC: Completing a 3D Point Cloud with 2D Diffusion Priors",
    "Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors",
    "DiffSplat: Repurposing Image Diffusion Models for Scalable Gaussian Splat Generation",
    "GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks",
    "LaGeM: A Large Geometry Model for 3D Representation Learning and Diffusion",
    "SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting",
    "ThermalGaussian: Thermal 3D Gaussian Splatting",
    "Multimodality Helps Few-shot 3D Point Cloud Semantic Segmentation",
    "Segment Any 3D Object with Language",

    # ICLR 2026.
    "Dens3R: A Foundation Model for 3D Geometry Prediction",
    "G4Splat: Geometry-Guided Gaussian Splatting with Generative Prior",
    "Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM",
    "GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception",
    "GeoPurify: A Data-Efficient Geometric Distillation Framework for Open-Vocabulary 3D Segmentation",
    "RayI2P: Learning Rays for Image-to-Point Cloud Registration",
    "SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors",
    "UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction",
    "UrbanGS: Efficient and Scalable Architecture for Geometrically Accurate Large-Scene Reconstruction",
    "WorldSplat: Gaussian-Centric Feed-Forward 4D Scene Generation for Autonomous Driving",
    "IGGT: Instance-Grounded Geometry Transformer for Semantic 3D Reconstruction",
    "SimULi: Real-Time LiDAR and Camera Simulation with Unscented Transforms",
    "Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling",

    # NeurIPS 2025.
    "EAG3R: Event-Augmented 3D Geometry Estimation for Dynamic and Extreme-Lighting Scenes",
    "SIU3R: Simultaneous Scene Understanding and 3D Reconstruction Beyond Feature Alignment",
    "OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects",
    "Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation",
    "PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-forward Planar Splatting",
    "GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion",
    "MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild",
    "Multimodal LiDAR-Camera Novel View Synthesis with Unified  Pose-free  Neural  Fields",
    "Object-X: Learning to Reconstruct Multi-Modal 3D Object Representations",
    "Spiral: Semantic-Aware Progressive LiDAR Scene Generation and Understanding",
    "ODG: Occupancy Prediction Using Dual Gaussians",
    "U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching",
    "Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training",
    "QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction",
    "VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via View Alignment",

    # ICML 2025/2026.
    "Generative Point Cloud Registration",
    "PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting for Novel View Synthesis",
    "GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model",
    "Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks",
    "Towards Learning to Complete Anything in Lidar",
    "Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment",
    "VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency",
    "WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting",
    "PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration",
    "PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation",
    "Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling",
    "S2GS: Streaming Semantic Gaussian Splatting for Online Scene Understanding and Reconstruction",
    "EnerGS: Energy-Based Gaussian Splatting under Partial Geometric Priors",
    "Flow Equivariant World Models: Structured Memory for Dynamic Environments",
    "Affine-Equivariant Kernel Space Encoding for NeRF Editing",
    "Rethinking Serialization in Linear 3D Vision: Decoupling Anisotropic Geometry from Isotropic Semantics",
    "Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation",
]


THREEDV_TITLES = [
    "MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion",
    "FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent",
    "Flash3D: Feed-Forward Generalisable 3D Scene Reconstruction from a Single Image",
    "AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones",
    "LoopSplat: Loop Closure by Registering 3D Gaussian Splats",
    "WaterSplatting: Fast Underwater 3D Scene Reconstruction using Gaussian Splatting",
    "SparseGS: Sparse View Synthesis using 3D Gaussian Splatting",
    "LangOcc: Open Vocabulary Occupancy Estimation via Volume Rendering",
    "Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds",
    "SSRFlow: Semantic-aware Fusion with Spatial Temporal Re-embedding for Real-world Scene Flow",
    "SMORE: Simultaneous Map and Object REconstruction",
    "iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views",
    "GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion",
    "CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences",
    "LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation",
]


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def category_and_tags(title: str, default_category: str | None = None) -> tuple[str, list[str]]:
    low = title.lower()
    tags: list[str] = []

    def has_word(pattern: str) -> bool:
        return re.search(pattern, low) is not None

    def add(tag: str) -> None:
        if tag not in tags:
            tags.append(tag)

    if "gaussian" in low or "splat" in low:
        add("Gaussian Splatting")
    if "nerf" in low or "radiance" in low or "neural field" in low:
        add("NeRF")
    if "reconstruction" in low or "surface" in low or "mesh" in low:
        add("3D reconstruction")
    if "slam" in low or "sfm" in low or "pose" in low or "calibration" in low or "registration" in low:
        add("geometry")
    if has_word(r"\blidar\b") or has_word(r"\bradar\b") or has_word(r"\bbev\b") or "occupancy" in low or "sensor" in low or has_word(r"\bfusion\b"):
        add("sensor fusion")
        add("LiDAR")
    if "semantic" in low or "open-vocabulary" in low or "segmentation" in low or "alignment" in low:
        add("semantic")
        add("alignment")
    if "diffusion" in low or "generation" in low or "generative" in low:
        add("Diffusion")
        add("Generation")
    if "equivariant" in low or "equivariance" in low or "se(3)" in low or "e(3)" in low:
        add("equivariant")
    if "depth" in low or "monocular" in low:
        add("depth")
    if "point cloud" in low or "point" in low:
        add("point cloud")
    add("3D Vision")

    if default_category:
        return default_category, tags[:9]
    if "equivariant" in tags or "registration" in low or "calibration" in low or "sfm" in low:
        category = "3D Equivariance, Calibration, and Registration"
    elif has_word(r"\blidar\b") or has_word(r"\bradar\b") or has_word(r"\bbev\b") or "occupancy" in low or "sensor" in low or has_word(r"\bfusion\b"):
        category = "Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception"
    elif "diffusion" in low or "generation" in low or "generative" in low or "text-to-3d" in low:
        category = "3D Generative Modeling and Diffusion"
    elif "semantic" in low or "open-vocabulary" in low or "segmentation" in low or "alignment" in low:
        category = "3D Semantic Understanding and Alignment"
    elif "gaussian" in low or "splat" in low or "nerf" in low or "radiance" in low:
        category = "3D Scene Representations and Neural Fields"
    elif "reconstruction" in low or "slam" in low or "surface" in low or "depth" in low:
        category = "3D Reconstruction, Geometry, and SLAM"
    else:
        category = "3D Representation Learning and Foundation Models"
    return category, tags[:9]


def make_entry(title: str, year: int, venue: str, pdf: str | None = None, page: str | None = None, arxiv: str | None = None, abstract: str = "", authors: str = "", category: str | None = None) -> dict:
    cat, tags = category_and_tags(title, category)
    out = {
        "title": normalize_space(title),
        "year": year,
        "venue": venue,
        "category": cat,
        "tags": tags,
        "project": "not identified",
    }
    if pdf:
        out["pdf"] = pdf
    if page:
        out["page"] = page
    if arxiv:
        out["arxiv"] = arxiv
    if abstract:
        out["abstract"] = normalize_space(abstract)
    if authors:
        out["authors"] = normalize_space(authors)
    return out


def load_cvf() -> dict[str, dict]:
    data = json.loads(CVF_CANDIDATES.read_text(encoding="utf-8"))
    return {item["title"]: item for item in data}


def load_ecva() -> dict[str, dict]:
    text = requests.get(ECVA_PAPERS, timeout=30).text
    pattern = re.compile(
        r'<dt class="ptitle"><br>\s*<a href=([^>]+)>\s*(.*?)</a>\s*</dt><dd>\s*(.*?)</dd>\s*<dd>\[<a href=\'([^\']+\.pdf)\'>pdf</a>\]',
        re.S,
    )
    out = {}
    for page, title, authors, pdf in pattern.findall(text):
        title = normalize_space(html.unescape(re.sub(r"<[^>]+>", " ", title)))
        out[title] = {
            "title": title,
            "authors": normalize_space(html.unescape(re.sub(r"<[^>]+>", " ", authors))),
            "pdf": urllib.parse.urljoin(ECVA_PAPERS, pdf),
            "page": urllib.parse.urljoin(ECVA_PAPERS, page),
        }
    return out


def load_openreview() -> dict[str, dict]:
    data = json.loads(OPENREVIEW_CANDIDATES.read_text(encoding="utf-8"))
    out = {}
    for venueid, items in data.items():
        for item in items:
            out[item["title"]] = item
    return out


def load_3dv() -> dict[str, dict]:
    text = requests.get(THREEDV_CSV, timeout=30).text
    rows = csv.DictReader(io.StringIO(text))
    return {row["Title"]: row for row in rows if row.get("Title")}


def year_from_venue(venue: str) -> int:
    match = re.search(r"20\d{2}", venue or "")
    return int(match.group(0)) if match else 0


def main() -> None:
    added: list[dict] = []
    missing: list[dict] = []

    for title, year, venue, arxiv_id, category in FOUNDATIONAL_ARXIV:
        added.append(make_entry(title, year, venue, arxiv=arxiv_id, category=category))

    cvf = load_cvf()
    for title in CVF_TITLES:
        item = cvf.get(title)
        if not item:
            missing.append({"source": "CVF", "title": title})
            continue
        year = year_from_venue(item.get("venue", ""))
        venue = item.get("venue", "")
        venue = venue.replace("CVPR", "CVPR ").replace("ICCV", "ICCV ").replace("WACV", "WACV ").strip()
        added.append(make_entry(title, year, venue, pdf=item.get("pdf"), page=item.get("page"), abstract=item.get("abstract", "")))

    ecva = load_ecva()
    for title in ECCV_TITLES:
        item = ecva.get(title)
        if not item:
            missing.append({"source": "ECVA", "title": title})
            continue
        added.append(make_entry(title, 2024, "ECCV", pdf=item["pdf"], page=item["page"], authors=item.get("authors", "")))

    openreview = load_openreview()
    for title in OPENREVIEW_TITLES:
        item = openreview.get(title)
        if not item:
            missing.append({"source": "OpenReview", "title": title})
            continue
        year = year_from_venue(item.get("venue", ""))
        authors = item.get("authors", "")
        if isinstance(authors, list):
            authors = ", ".join(authors[:8])
        added.append(make_entry(
            item["title"],
            year,
            item.get("venue", ""),
            pdf=item.get("pdf"),
            page=item.get("page"),
            abstract=item.get("abstract", ""),
            authors=authors,
        ))

    threedv = load_3dv()
    for title in THREEDV_TITLES:
        item = threedv.get(title)
        if not item:
            missing.append({"source": "3DV 2025 CSV", "title": title})
            continue
        added.append(make_entry(
            title,
            2025,
            "3DV",
            pdf=item.get("PDF Link"),
            page="https://3dvconf.github.io/2025/accepted-papers/",
            abstract=item.get("Abstract", ""),
            authors=item.get("Authors", ""),
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
    print(f"added {len(unique)} 3D-CV-first papers")
    if missing:
        print(f"missing {len(missing)} titles; see {LOG}")


if __name__ == "__main__":
    main()
