# 3D-SPATIAL MULTIMODAL MEMORY

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/639f9db06bf70c4ff44cf22a7f92cb08-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/114814. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Xueyan Zou, Yuchen Song, Ri-Zhao Qiu, Xuanbin Peng, Jianglong Ye, Sifei Liu, Xiaolong Wang
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Robotics, 3D Vision, Gaussian Splatting
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/639f9db06bf70c4ff44cf22a7f92cb08-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/639f9db06bf70c4ff44cf22a7f92cb08-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

문제 관련 발췌 — We observe two key issues: First, due to the computational limitations, the feature vector dimensions in Gaussian primitives are significantly reduced compared to the original 2D feature maps (typically 16-64 versus 1024), ...

방법 관련 발췌 — Specifically, we propose to store the original high-dimensional 2D feature maps in a memory bank called principal scene components and use the low-dimensional principal queries from 3D Gaussians as indices.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** We present 3D Spatial MultiModal Memory (M3), a multimodal memory system designed to retain information about medium-sized static scenes through video sources for visual perception.
- **p. 1 / ABSTRACT - extractive body cue:** By integrating 3D Gaussian Splatting techniques with foundation models, M3 builds a multimodal memory capable of rendering feature representations across granularities, encompassing a wide range ...
- **p. 1 / ABSTRACT - extractive body cue:** In our exploration, we identify two key challenges in previous works on feature splatting: (1) computational constraints in storing high-dimensional features for each Gaussian primitive, ...
- **p. 1 / ABSTRACT - extractive body cue:** To address these challenges, we propose M3 with key components of principal scene components and Gaussian memory attention, enabling efficient training and inference.
- **p. 1 / ABSTRACT - extractive body cue:** To validate M3, we conduct comprehensive quantitative evaluations of feature similarity and downstream tasks, as well as qualitative visualizations to highlight the pixel trace of ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We observe two key issues: First, due to the computational limitations, the feature vector dimensions in Gaussian primitives are significantly reduced compared to the original ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these models lack the capability to retain the semantic understanding of the scene like humans.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Specifically, we propose to store the original high-dimensional 2D feature maps in a memory bank called principal scene components and use the low-dimensional principal queries ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these issues, we present MultiModal Memory (M3), a better integration of Gaussian splatting and multimodal foundation models that efficiently store expressive multimodal memory ...
- **p. 3 / 3 METHOD - extractive body cue:** A real-world visual perception scene (V) consists of both structure (S) and knowledge (I).
- **p. 4 / 3 METHOD - extractive body cue:** We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered features ( ˆR), ...
- **p. 4 / 3 METHOD - extractive body cue:** To maintain efficiency while preserving the global representation of foundation model features, we compress the extracted features from foundation models into principal scene components (PSC) ...
- **p. 3 / 3 METHOD - extractive body cue:** The organic integration of Gaussian splatting and Foundation Models infuses scene structure with multi3
- **p. 3 / 3 METHOD - extractive body cue:** Gaussian splatting serves as a framework for constructing scene structure with finest granularity, represented as gaussian primitives, while foundation models provide vast world knowledge spanning ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We formally define the input of M3 as a video sequence with frames, where each frame corresponds to a view V∗. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3 METHOD), p. 4 (3 METHOD) |
| State/latent | formally, define, input, video, sequence, frames, where, frame, corresponds, view, Visual, granularity | geometry, map, object/relationship state | p. 4 (3 METHOD), p. 4 (3 METHOD), p. 2 (1 INTRODUCTION) |
| Output/action | Visual granularity (VG) typically represents the clustering pixel scope of an image, a concept introduced in Semantic-SAM [20]. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3 METHOD), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered features ( ˆR), which can be linked back to various ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Specifically, we propose to store the original high-dimensional 2D feature maps in a memory bank called principal scene components and use the low-dimensional principal queries ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these issues, we present MultiModal Memory (M3), a better integration of Gaussian splatting and multimodal foundation models that efficiently store expressive multimodal memory ...
- **p. 3 / 3 METHOD - extractive body cue:** A real-world visual perception scene (V) consists of both structure (S) and knowledge (I).
- **p. 4 / 3 METHOD - extractive body cue:** We introduce optimizable attribute queries (q) to Gaussian primitives, and apply a Gaussian Memory Attention (Agm) mechanism to produce the final rendered features ( ˆR), ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Our method, M3, outperforms F-Splat while reducing significantly compute than F-3DGS.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** The table clearly shows that increasing the number degree will generally improve the performance on all metrics.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 QUANTITATIVE RESULTS Baseline Implementation For quantitative experiments, we compare M3 with two recent distillation-based feature GS methods [26; 51].
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** M3 demonstrates superior downstream task accuracy with reduced training costs and shows practical utility when deployed on a real robot.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Embodiment/environment | To support extensive quantitative and qualitative evaluation, we perform experiments using several existing scene datasets [3; 18; 10] and collected a custom robot dataset (M3-Robot) using a quadruped robot and a drone. | hardware/simulator version and reset protocol | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Dataset/benchmark | After memorizing the scene with M3, the robot is able to locate and grasp any object with text query on decoded CLIP feature. | role, split, size and leakage | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Metric | M3 demonstrates superior downstream task accuracy with reduced training costs and shows practical utility when deployed on a real robot. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Baseline/ablation | 4.2 QUANTITATIVE RESULTS Baseline Implementation For quantitative experiments, we compare M3 with two recent distillation-based feature GS methods [26; 51]. | fair input/data/compute/action matching | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 EXPERIMENTS - extractive body cue:** SEEM and LLaMA3 features extraction failed on FSplat, which we assume was mainly due to the ground truth feature extraction procedure, where duplication was performed ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 4 (3 METHOD), p. 3 (3 METHOD)이다.
