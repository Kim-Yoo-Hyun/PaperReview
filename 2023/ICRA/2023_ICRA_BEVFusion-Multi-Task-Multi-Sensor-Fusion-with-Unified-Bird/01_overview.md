# BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2205.13542.
> PDF retrieval source: https://arxiv.org/pdf/2205.13542. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: sensor fusion, LiDAR, 3D perception
- Official paper: https://arxiv.org/abs/2205.13542
- Full-text retrieval: https://arxiv.org/pdf/2205.13542
- Code/Project: https://github.com/mit-han-lab/bevfusion
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Then, we propose a specialized kernel with precomputation and interval reduction to eliminate this bottleneck, achieving more than 40× speedup.를 문제로 두고, Then, we propose a specialized kernel with precomputation and interval reduction to eliminate this bottleneck, achieving more than 40× speedup.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 1 / I. INTRODUCTION - extractive body cue:** Then, we propose a specialized kernel with precomputation and interval reduction to eliminate this bottleneck, achieving more than 40× speedup.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose BEVFusion to unify multi-modal features in a shared bird's-eye view (BEV) representation space for task-agnostic learning.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Consequently, BEVFusion can achieve the same performance with much smaller resolution for the camera inputs, resulting in significantly lower MACs.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** III: BEVFusion outperforms the state-of-the-art multi-sensor fusion methods by 13.6% on BEV map segmentation on nuScenes (val) with consistent improvements across different categories.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: BEVFusion outperforms state-of-the-art single- and multi-modality detectors under different LiDAR sparsity, object sizes and object distances, especially under more challenging settings (i.e., sparser ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: BEVFusion unifies camera and LiDAR features in a shared BEV space instead of mapping one modality to the other. It preserves camera's semantic ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: BEVFusion extracts features from multi-modal inputs and converts them into a shared bird's-eye view (BEV) space efficiently using view transformations. It fuses the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Then, we propose a specialized kernel with precomputation and interval reduction to eliminate this bottleneck, achieving more than 40× speedup.를 문제로 두고, Then, we propose a specialized kernel with precomputation and interval reduction to eliminate this bottleneck, achieving more than 40× speedup.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. METHOD), p. 2 (III. METHOD), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
