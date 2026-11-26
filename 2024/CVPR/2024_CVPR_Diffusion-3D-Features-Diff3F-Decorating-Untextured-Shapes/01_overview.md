# Diffusion 3D Features (Diff3F): Decorating Untextured Shapes with Distilled Semantic Features

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Niladri Shekhar Dutt, Sanjeev Muralikrishnan, Niloy J. Mitra
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, Diffusion, 3D Vision, 3D correspondence
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Diff3F는 텍스처가 없는 3D 형상에 사전학습된 2D 확산 모델의 의미 특징을 부여한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present DIFF3F as a simple, robust, and classagnostic feature descriptor that can be computed for untextured input shapes (meshes or point clouds).
- **p. 1 / Abstract - extractive body cue:** Our method distills diffusion features from image foundational models onto input shapes.
- **p. 1 / Abstract - extractive body cue:** Specifically, we use the input shapes to produce depth and normal maps as guidance for conditional image synthesis.
- **p. 1 / Abstract - extractive body cue:** In the process, we produce (diffusion) features in 2D that we subsequently lift and aggregate on the original surface.
- **p. 1 / Abstract - extractive body cue:** Our key observation is that even if the conditional image generations obtained from multi-view rendering of the input shapes are inconsistent, the associated image features ...
- **p. 2 / 1. Introduction - extractive body cue:** A significant challenge is to address the absence of textures on most 3D models.
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, when shapes are represented as meshes, they may have nonmanifold faces, making it challenging to extract UV parameterizations; when shapes are represented as point ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We propose a simple and robust solution.
- **p. 2 / 1. Introduction - extractive body cue:** We present DIFFUSION 3D FEATURES (DIFF3F), a simple and practical framework for extracting semantic features that eliminates the need for additional training or optimization.
- **p. 6 / 3.4. Computing Correspondence - extractive body cue:** We report correspondence accuracy within 1% error tolerance, with our method against competing works.
- **p. 3 / 3. Method - extractive body cue:** This enables DIFF3F to produce semantic descriptors in a zero-shot way.
- **p. 5 / 3.2. Semantics through Painting - extractive body cue:** We employ a feature fusion strategy proposed by [65], where we first normalize the features and then concatenate them as, \ma t hc al {F}^ ...
- **p. 4 / 3.2. Semantics through Painting - extractive body cue:** We use DDIM [51] to accelerate the sampling process for Stable Diffusion [47] and use 30 inference steps.
- **p. 3 / 3. Method - extractive body cue:** Given the scarcity of 3D geometry data from which to learn these meaningful descriptors, we leverage foundational vision models trained on very large datasets to ...
- **p. 4 / 3.2. Semantics through Painting - extractive body cue:** We, therefore, condition our painting module f with geometric constraints that describe the latent 3D object.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We define G as a set of geometric maps that can be applied as conditional image constraints, \ label {e q:co l oreq} G := \{\mathcal {N}(I^S_j),\mathcal {D}(I^S_j)\}, (3) where N is ... | conditioning observation와 noisy/intermediate sample | p. 4 (3.2. Semantics through Painting), p. 4 (3.1. Semantic Diffusion Features) |
| State/latent | define, geometric, maps, applied, conditional, image, constraints, label, oreq, mathcal, S_j, where | latent/noise variable와 conditional distribution | p. 4 (3.2. Semantics through Painting), p. 4 (3.1. Semantic Diffusion Features), p. 5 (3.3. Distilling 2D Features to 3D) |
| Output/action | As an emergent behaviour, pre-trained foundational vision models have been found to assign distinctive semantic features [54] to pixels in the input image, to be able to distinguish between nearby pixels to ... | generated sample, action chunk 또는 trajectory | p. 4 (3.1. Semantic Diffusion Features), p. 5 (3.3. Distilling 2D Features to 3D), p. 1 (1. Introduction) |
| Objective/outcome | We guide the texturing by providing constraints G to ControlNet [66]. | distribution fit, multimodality, sample quality와 latency | p. 4 (3.1. Semantic Diffusion Features), p. 4 (3.2. Semantics through Painting), p. 5 (3.2. Semantics through Painting) |

## Main Claims and Actual Contribution

- 여러 시점에서 형상을 관찰해 얻은 특징을 3D 표면에 모은다.
- 추가 학습 없이 형상 사이의 의미 대응을 평가한다.

[저자 원문](https://openaccess.thecvf.com/content/CVPR2024/html/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.4. Evaluation on Human Shapes), p. 7 (4.4. Evaluation on Human Shapes) |
| Embodiment/environment | For DPC and SE-ORNet, we choose SURREAL and SMAL as the training sets for human and animal shapes, respectively - these larger datasets lead to improved generalization scores. | hardware/simulator version and reset protocol | p. 6 (4.1. Datasets and Benchmarks), p. 6 (4.1. Datasets and Benchmarks) |
| Dataset/benchmark | We present results on the SHREC'19 dataset. | role, split, size and leakage | p. 6 (4.1. Datasets and Benchmarks), p. 6 (4.1. Datasets and Benchmarks), p. 7 (4.4. Evaluation on Human Shapes), p. 7 (4.4. Evaluation on Human Shapes) |
| Metric | Although our complete approach produces the second-best score in every category, incorporating all of our parts together (including fusion with DINO) resulted in the best overall balance of high accuracy and low ... | definition, denominator, direction and uncertainty | p. 8 (4.6. Ablations), p. 6 (4.2. Evaluation Metrics), p. 6 (4.2. Evaluation Metrics) |
| Baseline/ablation | We outperform baseline methods by a large margin for non-isometric shapes thanks to the semantic nature of DIFF3F. | fair input/data/compute/action matching | p. 7 (4.5. Evaluation on Animal Shapes), p. 7 (4.4. Evaluation on Human Shapes), p. 6 (4.3. Baseline Methods) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** Since our method relies on multi-view images, DIFF3F fails to produce features on parts of the shapes that are invisible from all the sampled views ...
- **p. 8 / 6. Conclusion - extractive body cue:** Further, since we aggregate (diffusion) features from image diffusion models, we inherit their limitations in terms of suffering from bias in the dataset and/or view ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Comparison. We report correspondence accuracy within 1% error tolerance, with our method against competing works. The Laplace Beltrami Operator (LBO) computation for Functional ...
- **p. 7 / 4.5. Evaluation on Animal Shapes - extractive body cue:** Results using 3D-CODED are particularly poor on TOSCA mainly for two reasons: (i) It needs a much larger dataset with ground truth annotations, which is ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Results gallery. DIFF3F's performance on various point correspondence challenges. Corresponding points are similarly colored. Note that DIFF3F can successfully distinguish between symmetric parts ...
- **p. 7 / 4.6. Ablations - extractive body cue:** Additionally, varied textured renderings enable a more robust feature aggregation due to the implicit denoising of unnecessary feature dimensions 4500

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 5 (3.2. Semantics through Painting), p. 4 (3.2. Semantics through Painting), p. 3 (3. Method)이다.

## 검색 태그 근거

텍스처가 없는 형상을 여러 방향에서 렌더링한 뒤 확산 모델 및 DINO 특징을 표면으로 역투영해 집계한다. 형상 사이의 점 대응과 부품 분할을 평가했다. [원문 3쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.pdf#page=3) · [원문 8쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.pdf#page=8)
