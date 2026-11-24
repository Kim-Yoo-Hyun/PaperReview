# BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2206.10092.
> PDF retrieval source: https://arxiv.org/pdf/2206.10092. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / AAAI
- Authors: Yinhao Li, Zheng Ge, Guanyi Yu, Jinrong Yang, Zengran Wang, Yukang Shi, Jianjian Sun, Zeming Li
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: depth, 3D Vision
- Official paper: https://arxiv.org/abs/2206.10092
- Full-text retrieval: https://arxiv.org/pdf/2206.10092
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://arxiv.org/pdf/2206.10092v2)

## Why This Paper Is Here

BEVDepth는 카메라 영상으로 조감도 특징을 만들 때 픽셀별 깊이를 명시적으로 감독해 멀티뷰 3D 물체 검출을 개선한다. [PDF 1쪽](https://arxiv.org/pdf/2206.10092v2#page=1) · [PDF 3쪽](https://arxiv.org/pdf/2206.10092v2#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this research, we propose a new 3D object detector with a trustworthy depth estimation, dubbed BEVDepth, for camera-based Bird's-Eye-View (BEV) 3D object detection.
- **p. 1 / Abstract - extractive body cue:** Our work is based on a key observation - depth estimation in recent approaches is surprisingly inadequate given the fact that depth is essential to ...
- **p. 1 / Abstract - extractive body cue:** Our BEVDepth resolves this by leveraging explicit depth supervision.
- **p. 1 / Abstract - extractive body cue:** A camera-awareness depth estimation module is also introduced to facilitate the depth predicting capability.
- **p. 1 / Abstract - extractive body cue:** Besides, we design a novel Depth Refinement Module to counter the side effects carried by imprecise feature unprojection.
- **p. 1 / 1 Introduction - extractive body cue:** LiDAR and camera are the two main sensors used by the current autonomous systems to detect 3D objects and perceive the environment.
- **p. 1 / 1 Introduction - extractive body cue:** Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since the depth prediction ...

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** Therefore, in this work, we introduce BEVDepth, a new multi-view 3D detector that leverages depth supervision derives from point clouds to guide depth learning.
- **p. 1 / 1 Introduction - extractive body cue:** The BEV representation is non-trivial since it not only enables an end-to-end training scheme of a multiple input cameras system but also provides a unified ...
- **p. 1 / 1 Introduction - extractive body cue:** They first "lift" multi-view features to 3D frustums using estimated depth, then "splat" frustums onto a reference plane, usually being a plane in Bird's-Eye-View (BEV).
- **p. 1 / 1 Introduction - extractive body cue:** Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since the depth prediction ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Input Image Lift-splat BEVDepth Figure 1: Depth estimation results in Lift-splat detector and BEVDepth. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 1 (Abstract) |
| State/latent | Input, Image, Lift-splat, BEVDepth, Figure, Depth, estimation, detector, observation, recent, approaches, surprisingly | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |
| Output/action | Our work is based on a key observation - depth estimation in recent approaches is surprisingly inadequate given the fact that depth is essential to camera 3D detection. | point map, pose, scene graph, affordance 또는 query result | p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction) |
| Objective/outcome | While LiDAR-based methods have demonstrated their ability to deliver trustworthy 3D detection results, multi-view camera-based methods have recently attracted increasing attention because of their lower cost. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (1 Introduction), p. 1 (1 Introduction) |

## Main Claims and Actual Contribution

- 학습 시 LiDAR를 영상에 투영한 깊이 정답을 쓰고, 카메라 파라미터를 반영하는 깊이망과 특징 정제를 통해 2D 특징을 3D로 옮긴다. [PDF 3쪽](https://arxiv.org/pdf/2206.10092v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2206.10092v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2206.10092v2#page=5)
- nuScenes에서 카메라 기반 추론을 평가하고 깊이 감독과 여러 시점의 시간적 결합이 검출·깊이 성능에 미치는 영향을 분리했다. [PDF 5쪽](https://arxiv.org/pdf/2206.10092v2#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2206.10092v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2206.10092v2#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (5 Experiment), p. 6 (5 Experiment) |
| Embodiment/environment | There are 1000 scenarios in the dataset, which are divided into 700, 150, and 150 scenes for training, validation, and testing, respectively. | hardware/simulator version and reset protocol | p. 6 (5 Experiment), p. 6 (5 Experiment) |
| Dataset/benchmark | There are 1000 scenarios in the dataset, which are divided into 700, 150, and 150 scenes for training, validation, and testing, respectively. | role, split, size and leakage | p. 6 (5 Experiment), p. 6 (5 Experiment) |
| Metric | For 3D detection task, we report nuScenes Detection Score (NDS), mean Average Precision (mAP), as well as five True Positive (TP) metrics including mean Average Translation Error (mATE), mean Average Scale Error ... | definition, denominator, direction and uncertainty | p. 6 (5 Experiment), p. 6 (5 Experiment), p. 4 (Figure/Table caption) |
| Baseline/ablation | Overall, our BEVDepth improves 4.0% mAP and 4.0% NDS compared to its baseline, showing the effectiveness of our innovations. | fair input/data/compute/action matching | p. 6 (5 Experiment), p. 6 (5 Experiment), p. 4 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 2 Related Work - extractive body cue:** If the 2.5D projection of a certain point cloud does not fall into the ith view, we simply discard it.
- **p. 5 / 2 Related Work - extractive body cue:** Benefiting from the decoupled nature of LSS (Philion and Fidler 2020), the camera-aware depth prediction module is isolated from the detection head and thus the ...
- **p. 6 / 5 Experiment - extractive body cue:** See Table 6, when we use 1×3 conv on CD ×W dimension, the information does not exchange along the depth axis, and
- **p. 4 / 2 Related Work - extractive body cue:** Such a phenomenon implies that the model without depth loss has a higher risk of over-fitting, and thus it may also be sensitive to the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Testing detectors' robustness to image sizes. We use 256 × 704 for training. mAP on nuScenes are reported. best-predicted pixel for each object. ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 6 (5 Experiment), p. 4 (Figure/Table caption)이다.
