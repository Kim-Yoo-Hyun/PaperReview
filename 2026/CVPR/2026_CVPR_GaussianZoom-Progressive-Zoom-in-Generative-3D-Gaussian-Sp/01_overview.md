# GaussianZoom: Progressive Zoom-in Generative 3D Gaussian Splatting with Geometric and Semantic Guidance

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Shi_GaussianZoom_Progressive_Zoom-in_Generative_3D_Gaussian_Splatting_with_Geometric_and_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_GaussianZoom_Progressive_Zoom-in_Generative_3D_Gaussian_Splatting_with_Geometric_and_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Jiale Shi, Jiarui Hu, Zesong Yang, Kaixuan Luan, Hujun Bao, Zhaopeng Cui
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, semantic, alignment, Diffusion, Generation, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Shi_GaussianZoom_Progressive_Zoom-in_Generative_3D_Gaussian_Splatting_with_Geometric_and_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_GaussianZoom_Progressive_Zoom-in_Generative_3D_Gaussian_Splatting_with_Geometric_and_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

GaussianZoom은 저해상도 관측으로부터 점차 확대해 볼 수 있는 3D 장면을 생성한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce GaussianZoom, a generative zoom-in 3D reconstruction system with an iterative progressive framework that combines geometry-consistent scene modeling and multi-scale semantic reasoning to enable ...
- **p. 1 / Abstract - extractive body cue:** To achieve this, we develop a novel multi-view consistent super-resolution module with depth-based feature warping and VLM-driven detail synthesis, ensuring accurate multiview correspondence while enriching ...
- **p. 1 / Abstract - extractive body cue:** To support zooming across large magnification ranges, we further introduce a new expandable continuous Level-of-Detail hierarchy that dynamically modulates Gaussian visibility for smooth, alias-free cross-scale ...
- **p. 1 / Abstract - extractive body cue:** Experiments on Mip-NeRF360 and Tanks&Temples demonstrate that GaussianZoom achieves superior perceptual quality, multi-view consistency, and ro
- **p. 1 / 1. Introduction - extractive body cue:** Reconstructing high-fidelity 3D scenes from images is a fundamental problem in computer vision and graphics, supporting applications such as immersive VR/AR, digital content creation, and ...
- **p. 2 / 1. Introduction - extractive body cue:** However, these approaches inherently lack cross-view geometric consistency, because single-image SR independently sharpens each frame without enforcing geometric alignment [5, 6, 17, 36, 38], while ...
- **p. 2 / 1. Introduction - extractive body cue:** These limitations suggest that zoom-in 3D reconstruction is fundamentally a progressive generative process rather than a single-shot upsampling problem.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Beyond iterative refinement, we introduce an expandable continuous Level-of-Detail (LoD) representation that elevates LoD from a discrete efficiency-oriented mechanism to a continuous generative scaffold.
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose GaussianZoom, a progressive zoom-in generative 3D Gaussian Splatting framework that performs iterative coupling between geometry-consistent modeling and semantic-guided detail synthesis.
- **p. 4 / 4.1. Multi-View Consistent SR Module - extractive body cue:** Our framework jointly leverages geometry-aware alignment, semantic priors, and a continuous Level-ofDetail (LoD) representation to perform generative zoom-in reconstruction.
- **p. 8 / Method - extractive body cue:** 3, our method achieves the lowest FVD scores on both Mip-NeRF360 and Tanks&Temples, indicating superior temporal consistency.
- **p. 5 / 4.2. Continuous LoD Representation - extractive body cue:** Conversely, when ψ′/ψ falls below 1/s, the primitive sufficiently covers its projected footprint, and its contribution is increased while finer-level components are suppressed.
- **p. 5 / 4.1. Multi-View Consistent SR Module - extractive body cue:** These HR outputs then serve as supervision for updating the Gaussian representation at the corresponding zoom level.
- **p. 4 / 4.1. Multi-View Consistent SR Module - extractive body cue:** Depth-based Feature Warping SR Model 𝝐𝜽 ❄ Training For 𝑳𝑵 GS x N steps Full View Pairs Rendering with Zoomed Focal Traverse Image Pairs Zoomed ...
- **p. 5 / 4.1. Multi-View Consistent SR Module - extractive body cue:** The text description c, together with the multi-view consistent features ˜Fi obtained through depth-guided warping and the original feature representation Fi, provides semantic and geometric ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | A geometrically consistent low-resolution Gaussian model G is first optimized from input LR images Ii, producing reliable per-view depth maps Di that serve as explicit geometric priors. | conditioning observation와 noisy/intermediate sample | p. 4 (4.1. Multi-View Consistent SR Module), p. 2 (1. Introduction) |
| State/latent | geometrically, consistent, low-resolution, Gaussian, model, first, optimized, input, images, producing, reliable, per-view | latent/noise variable와 conditional distribution | p. 4 (4.1. Multi-View Consistent SR Module), p. 2 (1. Introduction), p. 4 (4.1. Multi-View Consistent SR Module) |
| Output/action | Traditional 3D super-resolution (SR) attempts to address this issue by employing 2D image or video SR models on input images before 3D reconstruction. | generated sample, action chunk 또는 trajectory | p. 2 (1. Introduction), p. 4 (4.1. Multi-View Consistent SR Module), p. 5 (4.3. Training Objective) |
| Objective/outcome | This enforces that the HR rendering does not deviate from the coarse-scale appearance when projected back to the LR domain. \mathcal {L } = \ l a m bda _\text { h ... | distribution fit, multimodality, sample quality와 latency | p. 5 (4.3. Training Objective), p. 8 (Method), p. 3 (4. Methods) |

## Main Claims and Actual Contribution

- 깊이를 이용한 시점 간 특징 정렬과 시각·언어 모델을 이용한 세부 합성을 결합한다.
- 확대 배율에 따라 가우시안의 가시성을 조절해 여러 축척의 장면을 렌더링한다.

[원문 초록](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_GaussianZoom_Progressive_Zoom-in_Generative_3D_Gaussian_Splatting_with_Geometric_and_CVPR_2026_paper.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.1. Experiment Settings), p. 7 (5.1. Experiment Settings) |
| Embodiment/environment | We evaluate our method on two real-world benchmarks: Mip-NeRF360 [2] and Tanks&Temples [13]. | hardware/simulator version and reset protocol | p. 5 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings) |
| Dataset/benchmark | We follow their official implementations to generate SRenhanced images and train corresponding 3DGS models on the refined datasets. | role, split, size and leakage | p. 5 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings), p. 5 (5.1. Experiment Settings) |
| Metric | These results demonstrate the robustness of our framework in reconstructing semantically coherent details under large magnification, validating its ability to generalize beyond supervised resolution scales. | definition, denominator, direction and uncertainty | p. 7 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings), p. 6 (5.1. Experiment Settings) |
| Baseline/ablation | For the extreme zoom-in task, we compare only with SRGS [6] and Sequence Matters [14], as the remaining baselines already exhibit substantial performance gaps at the 4× setting. | fair input/data/compute/action matching | p. 6 (5.1. Experiment Settings), p. 7 (5.1. Experiment Settings), p. 7 (5.1. Experiment Settings) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** Future work will investigate more capable content creative zoomin approaches to enable seamless transitions from cosmicscale environments down to microscopic and molecular scenes.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Method overview. Our framework jointly leverages geometry-aware alignment, semantic priors, and a continuous Level-of- Detail (LoD) representation to perform generative zoom-in reconstruction. Starting ...
- **p. 7 / 5.1. Experiment Settings - extractive body cue:** SRGS [6], which relies on a single-image super-resolution backbone, improves per-view sharpness but fails to maintain crossview coherence, since each frame is enhanced independently without ...
- **p. 7 / 5.1. Experiment Settings - extractive body cue:** The super-resolution involved methods including SRGS [6] and Sequence Matters [14] are chosen for comparsion, while SuperGaussian [24] fails to produce meaningful results under this ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6. Without prompt guidance, the reconstructed region exhibits semantic and material inconsistencies with the low- resolution inputs, producing mismatched textures or over- simplified surfaces. ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (4.1. Multi-View Consistent SR Module), p. 4 (4.1. Multi-View Consistent SR Module)이다.
