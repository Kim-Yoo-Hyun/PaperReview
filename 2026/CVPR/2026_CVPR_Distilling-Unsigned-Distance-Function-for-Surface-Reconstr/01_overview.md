# Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Qian Li, Rao Fu, Jiangtao Li, Fan Liu
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf)

## Why This Paper Is Here

가우시안 스플래팅으로부터 열린 표면과 날카로운 세부 형상을 복원하기 위해 부호 없는 거리장을 국소 표면 주변에 증류한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Unsigned distance function (UDF) is well suited for representing open surfaces, but learning them from multi-view images is challenging because ground-truth surfaces are unavailable for ...
- **p. 1 / Abstract - extractive body cue:** Prior methods optimize UDFs with global objectives and apply gradient-based priors ignoring the non-differentiability for queries on the target surface, which leads to unstable training ...
- **p. 1 / Abstract - extractive body cue:** We address these issues by distilling a patch-based UDF prior, trained on synthetic ground truth algebraic surfaces with closed form expressions, into a lightweight student ...
- **p. 1 / Abstract - extractive body cue:** We design a band-limited knowledge distillation strategy that leverages a pretrained patch-based UDF predictor to provide reliable near-surface UDF supervision, enabling stable student training and ...
- **p. 1 / Abstract - extractive body cue:** In addition, we introduce a visibility- and geometry-aware confidence weighting that modulates teacher influence, further steering the student toward accurate surfaces in ambiguous or weakly ...
- **p. 1 / 1. Introduction - extractive body cue:** To tackle these challenges, we distill a patch-based UDF predictor, trained on synthetic ground-truth surfaces, into a student UDF module that is optimized jointly with ...
- **p. 1 / 1. Introduction - extractive body cue:** Surface reconstruction from multi-view images is a fundamental problem in computer vision and graphics.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into ...
- **p. 2 / 1. Introduction - extractive body cue:** In addition, we introduce a visibility- and geometry-aware confidence weighting, together with a joint optimization scheme, to further steer the student toward accurate surfaces from ...
- **p. 3 / 3. Method - extractive body cue:** Our framework integrates Gaussian Splatting with UDF learning via a band-limited distillation scheme: a frozen local-shape UDF teacher ut provides supervision in a narrow nearsurface ...
- **p. 3 / 3. Method - extractive body cue:** Rendering proceeds by projecting each Gaussian onto the image plane and compositing its contribution in frontto-back order.
- **p. 5 / 3.3. Band-limited Knowledge Distillation - extractive body cue:** Furthermore, the overall distillation formulation offers several advantages: it simplifies the learning task by limiting the geometric complexity within each patch, enables effective reuse of ...
- **p. 3 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** Considering the strengths of LoSF-UDF [19] including robustness to noise and local feature representation, we use it as the teacher UDF model for distillation, denoted ...
- **p. 4 / 3.2. Learning Patch-based UDF Priors - extractive body cue:** To integrate this patch-based UDF prior into the 3DGS optimization, we use it to regularize the student UDF model fs.
- **p. 5 / 3.3. Band-limited Knowledge Distillation - extractive body cue:** representation to fit the scene geometry and appearance, and then optimize the student network within this band.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor into a lightweight student network. • Our method ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 3 (3. Method) |
| State/latent | main, contributions, follows, novel, framework, learns, UDF, over, Gaussian, primitives, distilling, patch-based | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method) |
| Output/action | Our goal is to reconstruct accurate, geometrically consistent open surfaces from calibrated multi-view images. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3. Method), p. 3 (3. Method), p. 5 (3.5. Joint Optimization) |
| Objective/outcome | The Gaussian parameters are optimized by minimizing the L1 photometric loss between the rendered image C′(u, v) and the ground-truth image C(u, v): Lr = /C′(u, v) -C(u, v)/1 , (2) | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3. Method), p. 4 (3.3. Band-limited Knowledge Distillation), p. 5 (3.5. Joint Optimization) |

## Main Claims and Actual Contribution

- 거리 정답을 계산할 수 있는 합성 대수적 표면으로 국소 기하 교사 모델을 학습하고 가시성과 기하 신뢰도로 학생의 증류 손실을 조절한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=5)
- 표면 인접 영역의 거리 감독을 가우시안 최적화와 결합하고 추출한 표면의 기하 오차와 세부 구조를 비교했다. [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.2. DF3D Dataset), p. 8 (4.2. DF3D Dataset) |
| Embodiment/environment | We further evaluate our method on the DTU dataset [22], which contains 15 widely used multi-view scenes for surface reconstruction. | hardware/simulator version and reset protocol | p. 8 (4.3. DTU Dataset), p. 5 (4.1. Experiment Settings) |
| Dataset/benchmark | Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3). | role, split, size and leakage | p. 8 (4.3. DTU Dataset), p. 5 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings), p. 7 (4.2. DF3D Dataset) |
| Metric | Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3). | definition, denominator, direction and uncertainty | p. 6 (4.1. Experiment Settings), p. 8 (4.3. DTU Dataset), p. 4 (Figure/Table caption) |
| Baseline/ablation | As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared methods, including classical NeRF-style SDF baselines (NeuS [48]), Gaussian-based methods without explicit distance fields (3DGS [24], ... | fair input/data/compute/action matching | p. 8 (4.3. DTU Dataset), p. 7 (4.2. DF3D Dataset), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to further ...
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** It is well known that learning unsigned distance functions (UDFs) is intrinsically more challenging than learning signed distance fields (SDFs), due to sign ambiguity and ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Learning Patch-based UDF Priors), p. 4 (3.2. Learning Patch-based UDF Priors), p. 5 (3.3. Band-limited Knowledge Distillation)이다.
