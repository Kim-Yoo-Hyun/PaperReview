# LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00113.
> PDF retrieval source: https://openreview.net/attachment?id=MaN2x3O2Rk&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: Weijie Ma, Jingwei Jiang, Yang Yang, Zehui Chen, Hao Chen
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: sensor fusion, LiDAR, 3D Vision
- Official paper: https://api.crossref.org/works/10.1109/3dv66043.2025.00113
- Full-text retrieval: https://arxiv.org/pdf/2411.06173.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125638)

## Why This Paper Is Here

LSSInst는 여러 카메라의 영상을 조감도에서 먼저 검출한 뒤 인스턴스별로 원래 영상 특징을 다시 조회해 3차원 물체를 검출한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125638#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125638#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** With the attention gained by camera-only 3D object detection in autonomous driving, methods based on Bird-EyeView (BEV) representation especially derived from the forward view transformation ...
- **p. 1 / Abstract - extractive body cue:** The BEV representation formulated by the frustum based on depth distribution prediction is ideal for learning the road structure and scene layout from multi-view images.
- **p. 1 / Abstract - extractive body cue:** However, to retain computational efficiency, the compressed BEV representation such as in resolution and axis is inevitably weak in retaining the individual geometric details, undermining ...
- **p. 1 / Abstract - extractive body cue:** With this in mind, to compensate for the missing details and utilize multi-view geometry constraints, we propose LSSInst, a two-stage object detector incorporating BEV and ...
- **p. 1 / Abstract - extractive body cue:** The proposed detector exploits fine-grained pixel-level features that can be flexibly integrated into existing LSS-based BEV networks.
- **p. 1 / 1. Introduction - extractive body cue:** However, unlike LiDAR sensors that provide direct and accurate depth information, detecting objects solely based on camera sensor images poses a significant challenge.
- **p. 2 / 1. Introduction - extractive body cue:** However, this collaboration also poses challenges, as the most straightforward solution of naively sharing the bounding box proposal is intuitively and experimentally failed 1.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with ...
- **p. 2 / 1. Introduction - extractive body cue:** With this in mind, we propose the instance adaptor module to establish semantic coherence between the scene and instances and an instance branch for detection.
- **p. 3 / 3. Methodology - extractive body cue:** The overview of our framework is shown in Fig.
- **p. 3 / 3. Methodology - extractive body cue:** In this work, we propose LSSInst, which looks back for the more geometry-aware and finegrained target feature extraction to bridge the adaptation between scene-level and ...
- **p. 5 / 3. Methodology - extractive body cue:** Then we introduce five separated linear projections {Ej l3}2 j=1 ∈R3×C, {Ej l2}2 j=1 ∈R2×C and Eg ∈RC×C for comprehensive encoding, of which the former ...
- **p. 4 / 3. Methodology - extractive body cue:** Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence ...
- **p. 4 / 3. Methodology - extractive body cue:** BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D image backbone network ...
- **p. 5 / 3. Methodology - extractive body cue:** Instance Adapter: Scene-to-instance adaptation For the sake of preserving a coherent and solid semantic consistency between BEV and instance representations, we propose the instance adapter ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D image backbone network for feature extraction. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3. Methodology), p. 4 (3. Methodology) |
| State/latent | BEV, Branch, Looking, around, scene-level, representation, multi-view, sequential, images, previous, frames, first | geometry, map, object/relationship state | p. 4 (3. Methodology), p. 4 (3. Methodology), p. 2 (1. Introduction) |
| Output/action | Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence Feature Extraction Net Voxel Pooling ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3. Methodology), p. 2 (1. Introduction), p. 3 (3. Methodology) |
| Objective/outcome | Lastly, the model makes the final prediction based on the updated output. briefly introduces the BEV branch. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3. Methodology), p. 4 (3. Methodology), p. 5 (3. Methodology) |

## Main Claims and Actual Contribution

- 조감도에서 생성한 인스턴스 제안과 영상 질의를 어댑터로 연결해 뷰 변환 과정에서 손실되는 세부 단서를 이용한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125638#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125638#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125638#page=5)
- nuScenes에서 3차원 검출을 비교하고 영상 특징의 재조회와 입력 교란이 검출 성능에 주는 영향을 평가했다. [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125638#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125638#page=7) · [PDF 8쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125638#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.3. Generalization Ability and Geometric-Wise), p. 6 (4.2. Benchmark Results) |
| Embodiment/environment | Dataset We conducted extensive experiments on the nuScenes 3D detection benchmark [1], a large-scale dataset in the autonomous driving scene. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Dataset/benchmark | Although we have verified the high performance of LSSInst on nuScenes [1], even the large-scale autonomous driving dataset inevitably contain disturbances in the extrinsics obtained when sensors collect data in huge quantities. | role, split, size and leakage | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.4. Noise Resistance for Practical Robustness), p. 7 (4.3. Generalization Ability and Geometric-Wise) |
| Metric | Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property (here we use * to denote this) by ... | definition, denominator, direction and uncertainty | p. 13 (Figure/Table caption), p. 7 (4.4. Noise Resistance for Practical Robustness), p. 7 (4.4. Noise Resistance for Practical Robustness) |
| Baseline/ablation | We compared our approach with LSS-based and two-stage state-of-the-art methods on the nuScenes val and test sets. | fair input/data/compute/action matching | p. 6 (4.2. Benchmark Results), p. 8 (4.5. Multiplicate Queries Ablations), p. 6 (4.2. Benchmark Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.5. Multiplicate Queries Ablations - extractive body cue:** We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries ...
- **p. 7 / 4.4. Noise Resistance for Practical Robustness - extractive body cue:** In actual autonomous driving scenarios, the detector is required to be resistant to the disturbance noise caused by small measurement errors.
- **p. 8 / 4.5. Multiplicate Queries Ablations - extractive body cue:** The noise resistance results for robustness.
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property (here ...
- **p. 8 / 4.5. Multiplicate Queries Ablations - extractive body cue:** Method Noise mAP%↑Attenu.%↓NDS%↑Attenu.%↓ Baseline 0 35.74 - 46.84 - LSSInst 38.28 - 49.43 - Baseline 0.5% 35.38 1.01 46.44 0.85 LSSInst 38.01 0.71 49.19 0.49 ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Methodology), p. 3 (3. Methodology)이다.
