# Center-Based 3D Object Detection and Tracking

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2006.11275.
> PDF retrieval source: https://arxiv.org/pdf/2006.11275. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / CVPR
- Authors: Tianwei Yin, Xingyi Zhou, Philipp Krahenbuhl
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: point cloud, 3D Vision
- Official paper: https://arxiv.org/abs/2006.11275
- Full-text retrieval: https://arxiv.org/pdf/2006.11275
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf)

## Why This Paper Is Here

CenterPoint는 LiDAR 점군에서 3D 물체 중심을 검출한 뒤 크기·방향·속도를 회귀하고 중심의 이동을 이용해 물체를 추적한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Three-dimensional objects are commonly represented as 3D boxes in a point-cloud.
- **p. 1 / Abstract - extractive body cue:** This representation mimics the well-studied image-based 2D bounding-box detection but comes with additional challenges.
- **p. 1 / Abstract - extractive body cue:** Objects in a 3D world do not follow any particular orientation, and box-based detectors have difficulties enumerating all orientations or fitting an axis-aligned bounding box ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we instead propose to represent, detect, and track 3D objects as points.
- **p. 1 / Abstract - extractive body cue:** Our framework, CenterPoint, first detects centers of objects using a keypoint detector and regresses to other attributes, including 3D size, 3D orientation, and velocity.
- **p. 1 / 1. Introduction - extractive body cue:** However, during a safety-critical left turn (bottom), anchor-based methods have difficulty fitting axisaligned bounding boxes to rotated objects.
- **p. 1 / 1. Introduction - extractive body cue:** Compared to the wellstudied 2D detection problem, 3D detection on point-clouds offers a series of interesting challenges: First, point-clouds are sparse, and most regions of ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** These marked differences between 2D and 3D detection made a transfer of ideas bea) Anchor-based t=1 c) Anchor-based t=2 b) Center-based t=1 d) Center-based t=2 ...
- **p. 3 / 3. Preliminaries - extractive body cue:** We introduce a novel center-based detection head but rely on existing 3D backbones (VoxelNet or PointPillars).
- **p. 2 / 1. Introduction - extractive body cue:** Thirdly, point-based feature extraction enables us to design an effective two-stage refinement module that is much faster than previous approaches [44-46].
- **p. 1 / Abstract - extractive body cue:** Our framework, CenterPoint, first detects centers of objects using a keypoint detector and regresses to other attributes, including 3D size, 3D orientation, and velocity.
- **p. 3 / 3. Preliminaries - extractive body cue:** Each bounding box b = (u, v, d, w, l, h, α) consists of a center location (u, v, d), relative to the objects ground ...
- **p. 3 / 3. Preliminaries - extractive body cue:** The 3D encoder then pools these features into its primary feature representation.
- **p. 3 / 3. Preliminaries - extractive body cue:** A point-based network [40] then extracts features for all points inside a bin.
- **p. 4 / 4. CenterPoint - extractive body cue:** Then, a 2D CNN architecture detection head finds object centers and regress to full 3D bounding boxes using center features.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes an input image and predicts a w × h heatmap ˆY ∈[0, 1]w×h×K for each of K classes. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3. Preliminaries), p. 3 (3. Preliminaries) |
| State/latent | takes, input, image, predicts, heatmap, classes, output, backbone, network, map-view, feature-map, width | geometry, map, object/relationship state | p. 3 (3. Preliminaries), p. 3 (3. Preliminaries), p. 4 (4. CenterPoint) |
| Output/action | The output of a backbone network is a map-view feature-map M ∈RW ×L×F of width W and length L with F channels in a map-view reference frame. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Preliminaries), p. 4 (4. CenterPoint), p. 4 (4.1. Two-Stage CenterPoint) |
| Objective/outcome | CenterPoint combines all heatmap and regression losses in one common objective and jointly optimizes them. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4. CenterPoint), p. 4 (4.1. Two-Stage CenterPoint), p. 2 (1. Introduction) |

## Main Claims and Actual Contribution

- 조감도 특징의 중심 히트맵과 물체 속성을 예측하고, 선택적 2단계 검출기는 예측 상자의 표면에서 특징을 다시 모아 상자를 정제한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=4)
- nuScenes와 Waymo에서 3D 검출과 추적을 평가하고 중심 및 속도에 기반한 단순 프레임 간 연결의 성능을 보고했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=7)

## Evaluation Scope

nuScenes에서 65.5 NDS는 3D 검출 점수이고 63.8 AMOTA는 여러 재현율에서 집계한 추적 정확도다. 두 값은 서로 다른 과제의 지표다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=1) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2021/papers/Yin_Center-Based_3D_Object_Detection_and_Tracking_CVPR_2021_paper.pdf#page=6)

## Explicit Limitations and Failure Boundary

- **p. 6 / 5.1. Main Results - extractive body cue:** Notably, our tracking does not require a separate motion model and runs in a negligible time, 1ms on top of detection.
- **p. 7 / 5.2. Ablation studies - extractive body cue:** Two-stage refinement does not bring an improvement over the single-stage CenterPoint model on nuScenes in our experiments.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminaries)이다.
