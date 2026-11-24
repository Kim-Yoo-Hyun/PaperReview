# Surface Reconstruction for 3D Gaussian Splatting via Local Structural Hints

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/274_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: Qianyi Wu, Jianmin Zheng, Jianfei Cai
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Aliases: Surface Reconstruction from 3D Gaussian Splatting via Local Structural Hints
- 게재 PDF 표제: Surface Reconstruction from 3D Gaussian Splatting via Local Structural Hints [표제면](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=1) · [학회 서지](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/274_ECCV_2024_paper.php)
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/274_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf)

## Why This Paper Is Here

GSrec은 단안 깊이·법선의 국소 단서로 가우시안의 위치와 모양을 조절하고, 그 주변에 거리장을 구성해 표면 메시를 추출한다. [PDF 1쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=1) · [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=5)

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 3D Gaussian Splatting (3DGS) [20] has garnered significant attention in the realm of 3D computer vision for its exceptional efficiency in modeling 3D radiance fields.
- **p. 1 / 1 Introduction - extractive body cue:** Given multi-view images with corresponding camera poses, 3DGS initializes Gaussian primitives from a sparse point cloud that comes from COLMAP [41] and renders a novel ...
- **p. 1 / 1 Introduction - extractive body cue:** With the dynamic densification operation on Gaussians including splitting and cloning, the final scene will be represented by millions of tiny Gaussians with unparalleled rendering ...
- **p. 1 / 1 Introduction - extractive body cue:** Despite the superior rendering efficiency and quality achieved by 3DGS over its implicit counterparts, Neural Radiance Field (NeRF) [3,31,32], its surface reconstruction ability is largely ...
- **p. 2 / 1 Introduction - extractive body cue:** Wu, J.Zheng, J.Cai. main reason is that a large number of discrete tiny Gaussians are noisy, unorganized, and do not align well with the underlying ...
- **p. 2 / 1 Introduction - extractive body cue:** Prior efforts to address this intricate challenge of extracting surface meshes from 3D Gaussian Splatting have been sparse.
- **p. 2 / 1 Introduction - extractive body cue:** These artifacts not only compromise the mesh's visual fidelity but also underscore the limitations of the regularization strategies in fully capturing complex surface geometry in ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** To address this, we propose a novel regularizer that leverages a neural implicit network to approximate the signed distance values of the MLS function at ...
- **p. 8 / 3 Method - extractive body cue:** We propose a novel strategy to further align the Gaussians with the surface.
- **p. 3 / 1 Introduction - extractive body cue:** Moreover, to ensure geometry consistency, we propose regularizing the MLS-based function prediction with a jointly learned neural implicit field.
- **p. 7 / 3 Method - extractive body cue:** Inspired by the depth rendering from [15,19,26,28], we also incorporate such a design in our framework by rendering the depth with the z-coordinate zi of ...
- **p. 2 / 1 Introduction - extractive body cue:** The key insight of our approach is to leverage the local structure hints to guide the optimization of Gaussians.
- **p. 9 / 3 Method - extractive body cue:** At first, we train the model with the color reconstruction loss as in original 3DGS [20] together with the monocular cue related losses in Sec.
- **p. 10 / 3 Method - extractive body cue:** After the optimization, we use 3D Gaussian means and normals for Poisson surface reconstruction [18] to extract the reconstructed meshes.
- **p. 5 / 3 Method - extractive body cue:** 3.1 and then elaborate on the technical details of each core module.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In addition to the vanilla IMLS definition, we further introduce a Robust IMLS (RIMLS) by applying a 1-D Gaussian kernel inputted with the norm of the difference between the normalized gradient ∇FMLP ... | RGB-D, image set, point cloud, depth와 camera pose | p. 9 (3 Method), p. 1 (1 Introduction) |
| State/latent | addition, vanilla, IMLS, definition, further, introduce, Robust, RIMLS, applying, Gaussian, kernel, inputted | geometry, map, object/relationship state | p. 9 (3 Method), p. 1 (1 Introduction), p. 5 (3 Method) |
| Output/action | Given multi-view images with corresponding camera poses, 3DGS initializes Gaussian primitives from a sparse point cloud that comes from COLMAP [41] and renders a novel view with a dedicated tile-based rasterization technique. | point map, pose, scene graph, affordance 또는 query result | p. 1 (1 Introduction), p. 5 (3 Method), p. 5 (3 Method) |
| Objective/outcome | The loss function will backpropagate the gradients to both the Gaussian Splatting field and the neural SDF. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 9 (3 Method), p. 9 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- 단안 추정으로 가우시안의 중심과 공분산을 정제한 뒤, 국소 가우시안 집합에 이동 최소제곱법을 적용해 부호 거리 함수를 정의한다. [PDF 5쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=5) · [PDF 6쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=6) · [PDF 7쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=7)
- 이 함수를 근사·정규화하는 신경 암시적 표현을 함께 학습하고, Replica 등에서 추출한 메시와 각 거리 제약의 효과를 비교했다. [PDF 8쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=8) · [PDF 11쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=11) · [PDF 13쪽](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf#page=13)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 13 (4 Experiments), p. 13 (4 Experiments) |
| Embodiment/environment | 2) ScanNet [10] is a real-world dataset captured with challenging image quality. | hardware/simulator version and reset protocol | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Dataset/benchmark | Chamfer-L1↓F-score ↑ COLMAP [41] 0.141 0.537 UNISURF [33] 0.359 0.267 NeuS [51] 0.194 0.291 VolSDF [58] 0.267 0.346 Manhattan-SDF [16] 0.070 0.602 MonoSDF (Grid) [62] 0.064 0.626 MonoSDF (MLP) [62] 0.042 0.733 ... | role, split, size and leakage | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 14 (4 Experiments), p. 11 (4 Experiments) |
| Metric | For quantitative evaluation of surface quality, we measure Chamfer Distance, Normal Consistency Score and Fscore with a threshold of 5cm on Replica. | definition, denominator, direction and uncertainty | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Baseline/ablation | We compare with previous strong baselines of neural implicit surface [16,33,51,58,62] and the 3DGS-based approach SuGaR [15]. | fair input/data/compute/action matching | p. 14 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 2: Joint optimization of 3DGS and neural implicit representation. We propose a novel strategy to further align the Gaussians with the surface. We jointly ...
- **p. 14 / 4 Experiments - extractive body cue:** Although the MonoSDF (MLP) adopts pure MLP structure which shows robustness to the camera noise, the training time of such a variant gets much longer ...
- **p. 12 / 4 Experiments - extractive body cue:** 2, the inaccurate normal estimated by the density gradient will lead to a degraded iso-surface estimation compared with Scaffold-GS+D and ScaffoldGS+N.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 9 (3 Method), p. 10 (3 Method), p. 5 (3 Method)이다.
