# Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: Huan Ling, Seung Wook Kim, Antonio Torralba, Sanja Fidler, Karsten Kreis
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, geometry, Diffusion, Generation, 3D Vision, video diffusion
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Align Your Gaussians는 텍스트로 지정한 장면과 움직임을 동적 3D 가우시안으로 생성한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Text-guided diffusion models have revolutionized image and video generation and have also been successfully used for optimization-based 3D object synthesis.
- **p. 1 / Abstract - extractive body cue:** Here, we instead focus on the underexplored text-to-4D setting and synthesize dynamic, animated 3D objects using score distillation methods with an additional temporal dimension.
- **p. 1 / Abstract - extractive body cue:** Compared to previous work, we pursue a novel compositional generation-based approach, and combine text-to-image, text-to-video, and 3D-aware multiview diffusion models to provide feedback during 4D ...
- **p. 1 / Abstract - extractive body cue:** Our method, called Align Your Gaussians (AYG), leverages dynamic 3D Gaussian Splatting with deformation fields as 4D representation.
- **p. 1 / Abstract - extractive body cue:** Crucial to AYG is a novel method to regularize the distribution of the moving 3D Gaussians and thereby stabilize the optimization and induce motion.
- **p. 2 / 1. Introduction - extractive body cue:** We also propose a new view-guidance method to generate consistent 3D scenes for initialization of the 4D stage, and we leverage the concurrent classifier score ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We propose Align Your Gaussians (AYG), a novel method for 4D content creation.
- **p. 2 / 1. Introduction - extractive body cue:** (iii) To scale AYG, we introduce a novel regularization method and a new motion amplification technique.
- **p. 1 / Abstract - extractive body cue:** Our method, called Align Your Gaussians (AYG), leverages dynamic 3D Gaussian Splatting with deformation fields as 4D representation.
- **p. 4 / 3. Align Your Gaussians - extractive body cue:** 3.1, we present AYG's 4D representation, and in Sec.
- **p. 4 / 3.1. AYG's 4D Representation - extractive body cue:** Specifically, each 4D scene consists of a set of N 3D Gaussians as in Sec.
- **p. 5 / 3.2. Text-to-4D as Compositional Generation - extractive body cue:** We disentangle optimization into first synthesizing a static 3D Gaussian-based object θ, and then learning the deformation field Φ to add scene dynamics.
- **p. 4 / 3.2. Text-to-4D as Compositional Generation - extractive body cue:** All used DMs are latent DMs [70, 86], which means that in practice we first encode renderings of our 4D scenes into the models' latent ...
- **p. 3 / 2. Background - extractive body cue:** In the score distillation sampling (SDS) framework, the DM's denoiser is then used to construct a gradient that is backpropagated through the differentiable rendering process ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Compared to previous work, we pursue a novel compositional generation-based approach, and combine text-to-image, text-to-video, and 3D-aware multiview diffusion models to provide feedback during 4D object optimization, thereby simultane ... | conditioning observation와 noisy/intermediate sample | p. 1 (Abstract), p. 4 (3.2. Text-to-4D as Compositional Generation) |
| State/latent | Compared, previous, pursue, novel, compositional, generation-based, combine, text-to-image, text-to-video, D-aware, multiview, diffusion | latent/noise variable와 conditional distribution | p. 1 (Abstract), p. 4 (3.2. Text-to-4D as Compositional Generation), p. 6 (3.3. AYG's Score Distillation in Practice) |
| Output/action | This video DM provides temporal feedback when rendering 2D frame sequences from our dynamic 4D scenes. | generated sample, action chunk 또는 trajectory | p. 4 (3.2. Text-to-4D as Compositional Generation), p. 6 (3.3. AYG's Score Distillation in Practice), p. 2 (1. Introduction) |
| Objective/outcome | We additionally minimize LInterpol-Reg. = //∆Φ1 -∆interpol Φ12 //2 2 within the overlap region to regularize the optimization process of ∆Φ2. | distribution fit, multimodality, sample quality와 latency | p. 7 (3.4. Scaling Align Your Gaussians), p. 2 (1. Introduction), p. 3 (2. Background) |

## Main Claims and Actual Contribution

- 정적 가우시안과 변형장을 결합해 시간에 따라 변하는 장면을 표현한다.
- 확산 생성 모델의 지도를 조합해 외형과 동작을 맞춘다.

[저자 원문](https://openaccess.thecvf.com/content/CVPR2024/html/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (4. Experiments), p. 8 (4. Experiments) |
| Embodiment/environment | Finally, due to the explicit nature of the dynamic 3D Gaussians, AYG's 4D representation, multiple animated 4D objects can be easily composed into larger scenes, each shape with its own deformation field ... | hardware/simulator version and reset protocol | p. 8 (4. Experiments), p. 8 (4. Experiments) |
| Dataset/benchmark | Finally, due to the explicit nature of the dynamic 3D Gaussians, AYG's 4D representation, multiple animated 4D objects can be easily composed into larger scenes, each shape with its own deformation field ... | role, split, size and leakage | p. 8 (4. Experiments), p. 8 (4. Experiments) |
| Metric | Figure 2. Text-to-4D synthesis with AYG. We generate dynamic 4D scenes via score distillation. We initialize the 4D sequence from a static 3D scene (gener- ated first, Fig. 3), which is represented ... | definition, denominator, direction and uncertainty | p. 2 (Figure/Table caption), p. 8 (4. Experiments), p. 8 (4. Experiments) |
| Baseline/ablation | AYG outperforms MAV3D on all metrics, achieving state-of-the-art text-to-4D performance (we also evaluated R-Precision [32, 58] on a larger prompt set used by MAV3D [78, 79], performing on par, see Supp. | fair input/data/compute/action matching | p. 8 (4. Experiments), p. 8 (4. Experiments), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusions - extractive body cue:** Overcoming this limitation would be an exciting avenue for future work.
- **p. 8 / 5. Conclusions - extractive body cue:** AYG currently cannot easily produce topological changes of the dynamic objects.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 5 (3.2. Text-to-4D as Compositional Generation), p. 4 (3.2. Text-to-4D as Compositional Generation), p. 3 (2. Background)이다.

## 검색 태그 근거

텍스트 조건부 영상·이미지 확산 모델로 시간에 따라 변형되는 가우시안을 최적화한다. 평가 대상은 여러 시점에서 렌더링하는 동적 그래픽 자산이다. [원문 4쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.pdf#page=4) · [원문 7쪽](https://openaccess.thecvf.com/content/CVPR2024/papers/Ling_Align_Your_Gaussians_Text-to-4D_with_Dynamic_3D_Gaussians_and_Composed_CVPR_2024_paper.pdf#page=7)
