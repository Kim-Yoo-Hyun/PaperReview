# GaussReg: Fast 3D Registration with Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2380_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Jiahao Chang, Yinglin Xu, Yihao Li, Yuantao Chen, Wensen Feng, Xiaoguang Han
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, geometry, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2380_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

GaussReg는 각각 Gaussian Splatting으로 표현된 두 장면을 점군으로 먼저 정렬하고 렌더링한 영상으로 세밀하게 맞춘다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf#page=1)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** In traditional 3D scene scanning and reconstruction, a large-scale scene is usually divided into different blocks, resulting in many independent sub-scenes that may † Corresponding ...
- **p. 2 / 1 Introduction - extractive body cue:** Scene A Scene B Render Render Render Register Scene A+B Fig.
- **p. 2 / 1 Introduction - extractive body cue:** 1: The purpose of our method is to register scenes A and B with Gaussian Splatting [17] models, and then combine A with B to ...
- **p. 2 / 1 Introduction - extractive body cue:** The first row is the visualization of the 3D Gaussians. not in the same coordinate system.
- **p. 2 / 1 Introduction - extractive body cue:** Therefore, the registration between them plays a crucial role.
- **p. 2 / 1 Introduction - extractive body cue:** But this method faces two issues: a) it is difficult to turn NeRF of unbounded scene to bounded voxel; b) the resolution limitation of the ...
- **p. 3 / 1 Introduction - extractive body cue:** However, it still lacks evaluation benchmarks of scene-level registration with GS.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** The main contributions can be summarized as: • To the best of our knowledge, we are the first to explore the registration of 3D scenes ...
- **p. 3 / 1 Introduction - extractive body cue:** Ultimately, we propose a novel coarse-to-fine GS registration framework: GaussReg.
- **p. 2 / 1 Introduction - extractive body cue:** 1: The purpose of our method is to register scenes A and B with Gaussian Splatting [17] models, and then combine A with B to ...
- **p. 5 / 3 Method - extractive body cue:** In this section, we present our proposed GaussReg for 3D Registration with Gaussian Splatting (GS).
- **p. 5 / 3 Method - extractive body cue:** 3.1 Overview As shown in Figure 2, the proposed GaussReg mainly consists of two stages, including the Coarse Registration, and the Image-Guided Fine Registration.
- **p. 6 / 3 Method - extractive body cue:** Our key idea is to first locate overlapping region between scene A and B and render some training images covering the region to support more ...
- **p. 7 / 3 Method - extractive body cue:** Without loss of generality, we use scene A as an example in the following description.
- **p. 8 / 3 Method - extractive body cue:** Our loss function mainly consists of two parts, depth loss and registration loss.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The coarse registration accepts PointsA and PointsB as input, and output a coarse transformation {sc, Rc, Tc}. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 Method), p. 6 (3 Method) |
| State/latent | coarse, registration, accepts, PointsA, PointsB, input, output, transformation, Training, Strategy, Loss, Function | geometry, map, object/relationship state | p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method) |
| Output/action | Training Strategy and Loss Function Due to the scale uncertainty in monocular video reconstruction, we performed data augmentation not only on rotation and translation but also on scaling for the input Gaussian ... | point map, pose, scene graph, affordance 또는 query result | p. 6 (3 Method), p. 7 (3 Method), p. 6 (3 Method) |
| Objective/outcome | Followed by the 3DCNN regularization, the probability volume PA ∈RD×H×W and feature volume FA ∈RC×D×H×W are obtained from the cost volumes, where C is the number of feature channels, and (H, W) ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (3 Method), p. 8 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- Gaussian의 공간 위치에서 거친 상대 자세를 얻은 뒤 렌더링 시점의 세밀한 기하 정보를 정합에 반영한다. [PDF 4쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf#page=4) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf#page=7)
- ScanNet 기반 ScanNet-GSReg와 직접 수집한 GSReg를 구성하고 단계별 정합 정확도를 비교했다. [PDF 9쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf#page=9) · [PDF 10쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf#page=10) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf#page=11) · [PDF 12쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02380.pdf#page=12)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 12 (4 Experiment), p. 11 (4 Experiment) |
| Embodiment/environment | Furthermore, to validate the generalization of our method, we collected 10 real-world scenes for testing, called GSReg dataset, which includes 6 indoor and 4 outdoor scenes. | hardware/simulator version and reset protocol | p. 10 (4 Experiment), p. 10 (4 Experiment) |
| Dataset/benchmark | ScanNet [8] is a frequently used 3D dataset for indoor scenes, consisting of 1513 training scenes and 100 test scenes. | role, split, size and leakage | p. 10 (4 Experiment), p. 10 (4 Experiment), p. 9 (4 Experiment), p. 9 (4 Experiment) |
| Metric | For a fair comparison, we follow DReg-NeRF [7] to evaluate GaussReg on the Objaverse dataset with two metrics: 1) Relative Rotational Error (RRE); 2) Absolute Translational Error (ATE), the Euclidean distance between ... | definition, denominator, direction and uncertainty | p. 10 (4 Experiment), p. 10 (4 Experiment), p. 11 (4 Experiment) |
| Baseline/ablation | Therefore, we select the current SOTA method, HLoc [28] (SuperPoint [10] + SuperGlue [29]), as the baseline for comparison on ScanNet. | fair input/data/compute/action matching | p. 11 (4 Experiment), p. 12 (4 Experiment), p. 11 (4 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 5 Discussion - extractive body cue:** Limitations and Future Work We only adopt a simple strategy to fuse and filter two GS models.
- **p. 11 / 4 Experiment - extractive body cue:** For indoor scenes in ScanNetGSReg, SuperPoint [10] sometimes fails to extract effective keypoints, leading to registration failures.
- **p. 13 / 5 Discussion - extractive body cue:** Future work can further explore to address this issue.
- **p. 10 / 4 Experiment - extractive body cue:** Eventually, after excluding cases of failed initial point cloud generation or unsuccessful GS reconstruction, we obtain 1297 training samples and 82 test samples.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 6 (3 Method), p. 7 (3 Method)이다.
