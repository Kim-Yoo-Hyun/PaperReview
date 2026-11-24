# EmbodiedOcc: Embodied 3D Occupancy Prediction for Vision-based Online Scene Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Yuqi Wu, Wenzhao Zheng, Sicheng Zuo, Yuanhui Huang, Jie Zhou, Jiwen Lu
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf
- Code/Project: https://github.com/YkiWu/EmbodiedOcc
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

EmbodiedOcc는 이동하며 얻은 영상으로 관측된 주변의 점유 상태를 갱신해 실내 전체의 3차원 의미 지도를 유지한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D occupancy prediction provides a comprehensive description of the surrounding scenes and has become an essential task for 3D perception.
- **p. 1 / Abstract - extractive body cue:** Most existing methods focus on offline perception from one or a few views and cannot be applied to embodied agents that demand to gradually perceive ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we formulate an embodied 3D occupancy prediction task to target this practical scenario and propose a Gaussian-based EmbodiedOcc framework to accomplish it.
- **p. 1 / Abstract - extractive body cue:** We initialize the global scene with uniform 3D semantic Gaussians and progressively update local regions observed by the embodied agent.
- **p. 1 / Abstract - extractive body cue:** For each update, we extract semantic and structural features from the observed image and efficiently incorporate them via deformable crossattention to refine the regional Gaussians.
- **p. 2 / 1. Introduction - extractive body cue:** To bridge this gap, we formulate a new embodied 3D occupancy prediction task to evaluate the ability to progressively explore an unknown scene using only ...
- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we propose a structure-aware local refinement module to update the relevant Gaussians within the current frustum.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Specifically, we propose a structure-aware local refinement module to update the relevant Gaussians within the current frustum.
- **p. 2 / 1. Introduction - extractive body cue:** We propose an EmbodiedOcc framework based on Gaussian memories to accomplish this task, considering the explicity and structural nature of 3D Gaussians.
- **p. 3 / 3.1. Embodied 3D Occupancy Prediction - extractive body cue:** Motivated by this, we propose an embodied 3D occupancy prediction task in this paper.
- **p. 1 / 1. Introduction - extractive body cue:** With the rapid development of embodied intelligence and active agents [14, 17, 32], 3D scene perception [30, 34, 41, 42] has become a crucial task ...
- **p. 3 / 3.2. Local Refinement Module - extractive body cue:** In this subsection, we will first explain our local refinement module, which extracts semantic and structural features from the monocular input and integrates them to ...
- **p. 3 / 3.2. Local Refinement Module - extractive body cue:** Different from conventional methods that conducted feature integration in a voxelized space, we use a set of 3D semantic Gaussians to represent an indoor scene ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Depth Aware Predicted Depth Map … … Input T-1 Input T … … … … Gaussian Memory T Gaussian Memory T-1 Occupancy T Occupancy T-1 Load Memory Update Memory Image Encoder Multi-Scale ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (3.1. Embodied 3D Occupancy Prediction) |
| State/latent | Depth, Aware, Predicted, Map, Input, T-1, Gaussian, Memory, Occupancy, Load, Update, Image | geometry, map, object/relationship state | p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction) |
| Output/action | Conventional methods in indoor scenarios for occupancy prediction accepted RGB-D as inputs to predict the semantic occupancy of a 3D scene which requires depth sensors. | point map, pose, scene graph, affordance 또는 query result | p. 2 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 2 (1. Introduction) |
| Objective/outcome | Then we detach and put these updated Gaussians back into the memory. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. Embodied 3D Occupancy Prediction), p. 3 (3.1. Embodied 3D Occupancy Prediction) |

## Main Claims and Actual Contribution

- 보이는 영역에 해당하는 Gaussian만 영상 특징으로 갱신하고 누적된 Gaussian을 점유 복셀로 변환한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf#page=5)
- ScanNet에서 순차 관측 평가를 구성하고 지역 예측, 누적 장면 예측, 이미 방문한 영역의 예측을 나누어 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_EmbodiedOcc_Embodied_3D_Occupancy_Prediction_for_Vision-based_Online_Scene_Understanding_ICCV_2025_paper.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.3. Main Results), p. 7 (4.3. Main Results) |
| Embodiment/environment | Apart from Occ-ScanNet and EmbodiedOcc-ScanNet datasets in the original scale, we sampled a small set from the EmbodiedOcc-ScanNet dataset as the EmbodiedOccScanNet-mini dataset which comprises 64/16 scenes in the train/val splits. | hardware/simulator version and reset protocol | p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark) |
| Dataset/benchmark | We also implemented several state-of-the-art driving scene methods [11, 13, 46] on this benchmark and our local refinement module outperforms them by a large margin. | role, split, size and leakage | p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 7 (4.3. Main Results), p. 7 (4.3. Main Results) |
| Metric | We use mIoU and IoU as the evaluation metrics. | definition, denominator, direction and uncertainty | p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 6 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 7 (4.4. Experimental Analysis) |
| Baseline/ablation | We also implemented several state-of-the-art driving scene methods [11, 13, 46] on this benchmark and our local refinement module outperforms them by a large margin. | fair input/data/compute/action matching | p. 7 (4.3. Main Results), p. 5 (4.1. EmbodiedOcc-ScanNet Benchmark), p. 7 (4.3. Main Results) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.4. Experimental Analysis - extractive body cue:** Due to space limitations, we will use a more diverse set of samples to further show the visual effect of our EmbodiedOcc in the supplementary ...
- **p. 8 / 4.4. Experimental Analysis - extractive body cue:** Besides, we replaced DepthAnything-V2 with IndoorDepth [6] in the last row to prove that our depth-aware branch does not rely on a specific depth prediction ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 3 (3.2. Local Refinement Module), p. 7 (4.3. Main Results)이다.
