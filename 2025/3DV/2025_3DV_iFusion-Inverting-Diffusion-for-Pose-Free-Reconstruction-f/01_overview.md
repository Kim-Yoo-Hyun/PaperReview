# iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00080.
> PDF retrieval source: https://openreview.net/attachment?id=W7vOFBCGPm&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: Chin-Hsuan Wu, Yen-Chun Chen, Bolivar Solarte, Lu Yuan, Min Sun
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, geometry, Diffusion, 3D Vision, camera pose
- Official paper: https://api.crossref.org/works/10.1109/3dv66043.2025.00080
- Preprint PDF: https://arxiv.org/pdf/2312.17250
- Full-text retrieval at original review: https://openreview.net/attachment?id=W7vOFBCGPm&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593)

## Why This Paper Is Here

iFusion은 카메라 자세를 모르는 두 물체 영상에서 상대 자세를 찾고 사전학습된 확산 모델을 해당 물체에 적응시켜 3차원 형상을 복원한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593#page=1) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present iFusion, a novel 3D object reconstruction framework that requires only two views with unknown camera poses.
- **p. 1 / Abstract - extractive body cue:** While single-view reconstruction yields visually appealing results, it can deviate significantly from the actual object, especially on unseen sides.
- **p. 1 / Abstract - extractive body cue:** Additional views improve reconstruction fidelity but necessitate known camera poses.
- **p. 1 / Abstract - extractive body cue:** However, assuming the availability of pose may be unrealistic, and existing pose estimators fail in sparseview scenarios.
- **p. 1 / Abstract - extractive body cue:** To address this, we harness a pre-trained novel view synthesis diffusion model, which embeds implicit knowledge about the geometry and appearance of diverse objects.
- **p. 1 / 1. Introduction - extractive body cue:** Reconstructing objects from sparse views poses a significant challenge yet holds paramount importance for various applications, including 3D content creation, augmented reality, virtual reality, and ...
- **p. 2 / 1. Introduction - extractive body cue:** A generic framework for pose-free, sparse-view 3D reconstruction is still lacking, posing a significant obstacle to real-world applications with casually captured photos.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we introduce iFusion, a novel framework that reconstructs diverse 3D objects with sparse, pose-free views.
- **p. 2 / 1. Introduction - extractive body cue:** We propose a novel camera pose estimator that significantly outperforms existing methods in terms of both accuracy and required number of input views, while being ...
- **p. 4 / 3.2. From Single-View to Multi-View - extractive body cue:** We propose to close the gap by further fine-tuning the DM with the given views and estimated poses.
- **p. 3 / 2. Preliminary - extractive body cue:** For instance, the standalone SD takes texts as the condition c and enables textto-image generation (T2I).
- **p. 3 / 3. Method - extractive body cue:** Next, the registered views are leveraged to customized the novel view synthesis model for the target object as in Fig.
- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (a) Pose Optimization + noise Pre-trained Diffusion Reconstruction Loss (b) Sparse-view Fine-tuning + noise Pre-trained Diffusion LoRA Reconstruction Loss (c) 3D Reconstruction Reconstruction Module Pre-trained ...
- **p. 5 / 3.3. From Sparse Views to 3D Reconstruction - extractive body cue:** 3.2, and then feed them as the training data to the differentiable renderer, e.g., NeRF [38] and NeuS [69].
- **p. 4 / 3.1. Diffusion as a Pose Estimator - extractive body cue:** (c) Conditioned on ˆTr→q and the refined diffusion model, we optimize a reconstruction module to perform sparse view 3D reconstruction.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (a) Given as few as two pose-free images (xr, xq), we estimate the pose ˆTr→q from T0 to optimally reconstruct the input view through the frozen diffusion model. | conditioning observation와 noisy/intermediate sample | p. 4 (3.1. Diffusion as a Pose Estimator), p. 2 (1. Introduction) |
| State/latent | Given, pose-free, images, estimate, pose, optimally, reconstruct, input, view, through, frozen, diffusion | latent/noise variable와 conditional distribution | p. 4 (3.1. Diffusion as a Pose Estimator), p. 2 (1. Introduction), p. 3 (2. Preliminary) |
| Output/action | More specifically, we adopt an analysisby-synthesis paradigm [7, 45, 78] that optimizes the transformation by minimizing the difference between the denoised latent visual features, i.e., Zero123's output image feature map, and the ... | generated sample, action chunk 또는 trajectory | p. 2 (1. Introduction), p. 3 (2. Preliminary), p. 3 (3.1. Diffusion as a Pose Estimator) |
| Objective/outcome | To ensure that the estimated pose ˆTr→q continue to lie on the SE(3) manifold during the gradientbased optimization, we parameterize the pose Tr→q = exp(ξ), where ξ ∈R6 is the twist coordinates ... | distribution fit, multimodality, sample quality와 latency | p. 3 (3.1. Diffusion as a Pose Estimator), p. 4 (3.1. Diffusion as a Pose Estimator), p. 3 (3.1. Diffusion as a Pose Estimator) |

## Main Claims and Actual Contribution

- 영상 조건부 확산 모델을 역으로 사용해 상대 카메라 자세를 최적화하고 두 입력의 정보를 뷰 생성 모델에 반영한다. [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593#page=4)
- 상대 자세 오차와 새로운 시점에서의 물체 복원 품질을 구분해 두 뷰를 사용하는 효과를 비교했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Experimental Result) |
| Embodiment/environment | Datasets We conduct experiments using two publicly available object datasets: Google Scanned Object (GSO) [9] and OmniObject3D (OO3D) [73]. | hardware/simulator version and reset protocol | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Dataset/benchmark | In addition, iFusion clearly outperforms other noneoptimization-based methods Point-E [42] and Shape-E [21], which are trained on a large-scale private dataset. | role, split, size and leakage | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Experimental Result), p. 6 (4.2. Experimental Result) |
| Metric | For 3D reconstruction, we report Chamfer Distances and volumetric IoU between ground truth shapes and reconstructed ones. | definition, denominator, direction and uncertainty | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 7 (4.3. Ablation Study) |
| Baseline/ablation | Ablation of t annealing for pose estimation on GSO [9]. n poses t annealing Recall ↑ 5◦ 10◦ 20◦ (a) 4 - 48.61 56.67 61.39 (b) 4 ✓ 74.79 84.29 88.57 pervising ... | fair input/data/compute/action matching | p. 8 (4.3. Ablation Study), p. 5 (4.2. Experimental Result), p. 6 (4.2. Experimental Result) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.2. Experimental Result - extractive body cue:** Notably, COLMAP [55] cannot serve as a baseline in our evaluation due to the structural limitations of Structure-from-Motion, which requires a large number of views ...
- **p. 5 / 4.2. Experimental Result - extractive body cue:** We found that by leveraging the diffusion model [31], iFusion excels at handling diverse objects thanks to its strong prior knowledge learned during pre-training, whereas ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** Row (c) highlights the substantial improvement from the stochastic re-sampling of multiview conditions at each timestep, providing more robust outcomes than row (b).
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 8. More qualitative results on pose estimation. The predicted poses (thin) and their corresponding ground truth (bold), are plotted in the same color, while ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Preliminary), p. 4 (3.1. Diffusion as a Pose Estimator), p. 5 (3.3. From Sparse Views to 3D Reconstruction)이다.

## 검색 태그 근거

소수의 물체 영상에서 확산 모델을 역으로 사용해 먼저 상대 자세를 최적화한다. 추정 자세를 바탕으로 같은 물체의 표현을 맞추고 GSO와 OmniObject3D에서 자세·형상 오차를 평가한다. [원문 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593#page=4) · [원문 8쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125593#page=8)
