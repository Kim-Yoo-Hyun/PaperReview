# AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00104.
> PDF retrieval source: https://openreview.net/attachment?id=fTJrKaBKZk&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: Xuqian Ren, Matias Turkulainen, Jiepeng Wang, Otto Seiskari, Iaroslav Melekhov, Juho Kannala, Esa Rahtu
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://api.crossref.org/works/10.1109/3dv66043.2025.00104
- Full-text retrieval: https://arxiv.org/pdf/2411.19271.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632)

## Why This Paper Is Here

AGS-Mesh는 휴대전화로 촬영한 실내 장면에서 불확실한 깊이·법선 단서를 거른 뒤 가우시안 표현으로부터 표면 메시를 추출한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Geometric priors are often used to enhance 3D reconstruction.
- **p. 1 / Abstract - extractive body cue:** With many smartphones featuring low-resolution depth sensors and the prevalence of off-the-shelf monocular geometry estimators, incorporating geometric priors as regularization signals has become common in ...
- **p. 1 / Abstract - extractive body cue:** However, the accuracy of depth estimates from mobile devices is typically poor for highly detailed geometry, and monocular estimators often suffer from poor multi-view consistency ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose an approach for joint surface depth and normal refinement of Gaussian Splatting methods for accurate 3D reconstruction of indoor scenes.
- **p. 1 / Abstract - extractive body cue:** We develop supervision strategies that adaptively filters low-quality depth and normal estimates by comparing the consistency of the priors during optimization.
- **p. 2 / 1. Introduction - extractive body cue:** However, performance on room-scale reconstruction with data captured by a mobile device is still lacking.
- **p. 2 / 1. Introduction - extractive body cue:** Low-texture surfaces and sparse, outward-facing captures, common in indoor room datasets [37, 55], pose challenges and ambiguities for purely photometric-based reconstruction.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors from ...
- **p. 4 / 4. Method - extractive body cue:** Our method consists of two adaptive supervision strategies for Gaussian Splatting-based methods that effectively combine supervision signals from geometric priors obtained from mobile devices and ...
- **p. 4 / 4. Method - extractive body cue:** Lastly, in Section 4.4, we propose a novel octree-based mesh extraction method that enhances surface quality and detail preservation compared to previous approaches.
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, we propose an Adaptive Normal Regularization strategy (ANR) to refine normals by mitigating regularization in regions where monocular normal estimators struggle to provide accurate ...
- **p. 5 / 4.1. Regularization with Depth Normal Consistency - extractive body cue:** Furthermore, we propose an adaptive TSDF and octree-based Marching Cubes meshing strategy enabling the extraction of smoother and more geometrically detailed meshes.
- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive body cue:** To filter inaccurate depth estimates, we check the orientation consistency between Nd and Np generated from pre-train model with an angle threshold τd for filtering: ...
- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive body cue:** We propose an adaptive depth regularization method based on the consistency of normals derived from noisy depth images and those from pretrained networks.
- **p. 5 / 4.2. Adaptive Normal Regularization - extractive body cue:** The ANR strategy is designed to first regularize Gaussian normals using the fully pre-trained normals Np, and subsequently relax the training by relying only on ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To achieve this, we employ a point cloud hint: we back-project our output depth maps from all training images into a point cloud and expand a voxel of width h if it ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (4.4. Mesh Extraction), p. 2 (1. Introduction) |
| State/latent | achieve, employ, point, cloud, hint, back-project, output, depth, maps, training, images, expand | geometry, map, object/relationship state | p. 6 (4.4. Mesh Extraction), p. 2 (1. Introduction), p. 4 (4. Method) |
| Output/action | We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors from mobile devices and off-the-shelf monocular estimator ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 4 (4. Method), p. 4 (4. Method) |
| Objective/outcome | To allow the gradients from the normal loss during optimization to directly influence the Gaussian geometry, ˆN is estimated from rendered depth maps as in [19]: ˆN(x, y) = ∇xD(x, y) × ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.2. Adaptive Normal Regularization), p. 5 (4.3. Optimization), p. 4 (4. Method) |

## Main Claims and Actual Contribution

- 측정과 예측의 일관성에 따라 깊이·법선 감독을 선별해 가우시안의 표면 방향과 위치를 학습한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=4) · [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=5)
- 장면의 스케일에 적응하는 옥트리 기반 표면 추출을 적용하고 실내 스캔에서 메시의 정확도와 완전성을 비교했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (5.3. Ablation Studies), p. 6 (5.1. 3D Reconstruction Evaluation) |
| Embodiment/environment | We focus on real-world indoor scenes captured using a mobile device. | hardware/simulator version and reset protocol | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Dataset/benchmark | We demonstrate our method with two Gaussian-based methods DN-Splatter [43] and 2DGS [19] with qualitative visuals of the reconstructed meshes for the "honka" (top) and "coffee room" (bottom) scenes from the MuSHRoom ... | role, split, size and leakage | p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.2. Novel View Synthesis), p. 7 (5.2. Novel View Synthesis) |
| Metric | For mesh reconstruction evaluation, we follow the evaluation protocol from [37, 45] and report Accuracy (Acc.), Completion (Comp.), Chamfer-L1 distance (C-L1), Normal Consistency (NC), and F-scores (F1) with a threshold of 5cm. | definition, denominator, direction and uncertainty | p. 6 (5. Experiments), p. 7 (Figure/Table caption), p. 7 (5.3. Ablation Studies) |
| Baseline/ablation | We compared our method to the following baselines: a) Traditional 3D reconstruction method Volumetric Fusion [9]. b) state-of-the-art NeRF-based method Nerfacto [41]; c) its depth regularized version Depth-Nerfacto with a depth supervis ... | fair input/data/compute/action matching | p. 6 (5. Experiments), p. 8 (Figure/Table caption), p. 6 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and ...
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Lastly, the DNC and ANR terms help preserve details for objects and reduce overall noise.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8. Qualitative visuals of our Depth Normal Consistency (DNR) and Adaptive Normal Regularization (ANR) terms. We visualize sensor depth and normals obtained from a ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 4 (3.2. Gaussian Splatting), p. 1 (1. Introduction), p. 3 (3.1. Geometric Priors from Handheld Devices), p. 4 (4.1. Regularization with Depth Normal Consistency)이다.
