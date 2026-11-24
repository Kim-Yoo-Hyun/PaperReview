# BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2205.13542.
> PDF retrieval source: https://arxiv.org/pdf/2205.13542. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICRA
- Authors: Zhijian Liu, Haotian Tang, Alexander Amini, Xinyu Yang, Huizi Mao, Daniela L. Rus, Song Han
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: sensor fusion, LiDAR, 3D perception
- Official paper: https://arxiv.org/abs/2205.13542
- Full-text retrieval: https://arxiv.org/pdf/2205.13542
- Code/Project: https://github.com/mit-han-lab/bevfusion
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

BEVFusion은 카메라와 LiDAR의 특징을 같은 조감도 좌표계에 모아 여러 자율주행 인지 과제에 사용한다. [PDF 1쪽](https://arxiv.org/pdf/2205.13542v3#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Multi-sensor fusion is essential for an accurate and reliable autonomous driving system.
- **p. 1 / Abstract - extractive body cue:** Recent approaches are based on point-level fusion: augmenting the LiDAR point cloud with camera features.
- **p. 1 / Abstract - extractive body cue:** However, the camera-to-LiDAR projection throws away the semantic density of camera features, hindering the effectiveness of such methods, especially for semantic-oriented tasks (such as 3D ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose BEVFusion, an efficient and generic multi-task multi-sensor fusion framework.
- **p. 1 / Abstract - extractive body cue:** It unifies multi-modal features in the shared bird's-eye view (BEV) representation space, which nicely preserves both geometric and semantic information.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Then, we propose a specialized kernel with precomputation and interval reduction to eliminate this bottleneck, achieving more than 40× speedup.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While converting all features to BEV, we identify the major prohibitive efficiency bottleneck in the view transformation: i.e., the BEV pooling operation alone takes more ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Then, we propose a specialized kernel with precomputation and interval reduction to eliminate this bottleneck, achieving more than 40× speedup.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose BEVFusion to unify multi-modal features in a shared bird's-eye view (BEV) representation space for task-agnostic learning.
- **p. 2 / III. METHOD - extractive body cue:** Given different sensory inputs, we first apply modality-specific encoders to extract their features.
- **p. 2 / III. METHOD - extractive body cue:** We then apply the convolution-based BEV encoder to the unified BEV features to alleviate the local misalignment between different features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given different sensory inputs, we first apply modality-specific encoders to extract their features. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (III. METHOD), p. 2 (I. INTRODUCTION) |
| State/latent | Given, different, sensory, inputs, first, apply, modality-specific, encoders, extract, features, BEV, Map | geometry, map, object/relationship state | p. 2 (III. METHOD), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/action | (in BEV) BEV Map Segmentation 3D Object Detection LiDAR Features Fused BEV Features LiDAR Point Cloud Multi-View RGB Images Task-Specific Heads … Flatten (along z-axis) Camera-to-BEV View Transform Camera Encoder LiDAR Encoder ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- 카메라 특징을 조감도로 변환할 때 대응 관계를 미리 계산하고 구간별 합산을 최적화해 특징 집계의 계산 부담을 줄였다. [PDF 2쪽](https://arxiv.org/pdf/2205.13542v3#page=2) · [PDF 3쪽](https://arxiv.org/pdf/2205.13542v3#page=3)
- nuScenes에서 같은 융합 표현에 서로 다른 출력기를 붙여 3차원 물체 검출과 조감도 지도 분할을 평가했다. [PDF 4쪽](https://arxiv.org/pdf/2205.13542v3#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2205.13542v3#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2205.13542v3#page=6)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Embodiment/environment | We evaluate our method on nuScenes [59] and Waymo [60], which are large-scale datasets for 3D perception with >40k annotated scenes. | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Dataset/benchmark | We evaluate BEVFusion for camera-LiDAR fusion on 3D object detection and BEV map segmentation, covering both geometric- and semantic-oriented tasks. | role, split, size and leakage | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Metric | We use the mean average precision (mAP) across 10 foreground classes and the nuScenes detection score (NDS) as our detection metrics. | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Baseline/ablation | Fig. 4: BEVFusion outperforms state-of-the-art single- and multi-modality detectors under different LiDAR sparsity, object sizes and object distances, especially under more challenging settings (i.e., sparser point clouds, small/distant ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 3 / A C - extractive body cue:** On the one hand, the LiDARto-BEV projection flattens the sparse LiDAR features along the height dimension, thus does not create geometric distortion in Figure 1a.
- **p. 4 / A C - extractive body cue:** Our method could potentially benefit from more accurate depth estimation (e.g., supervising the view transformer with groundtruth depth [42], [53]), which we leave for future ...
- **p. 4 / A C - extractive body cue:** This kernel removes the dependency between outputs (thus does not require multi-level tree reduction) and avoids writing the partial sums to the DRAM, reducing the ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** IV: BEVFusion is robust under different lighting and weather conditions, significantly boosting the performance single-modality models under challenging rainy(+10.7) and nighttime(+12.8) scenes.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 5 (IV. EXPERIMENTS)이다.
