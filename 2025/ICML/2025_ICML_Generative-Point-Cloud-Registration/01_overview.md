# Generative Point Cloud Registration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/jiang25k.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/167215. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Haobo Jiang, Jin Xie, Jian Yang, Liang Yu, Jianmin Zheng
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: geometry, Diffusion, Generation, point cloud, 3D Vision
- Official paper: https://proceedings.mlr.press/v267/jiang25k.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25k/jiang25k.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jiang25k/jiang25k.pdf)

## Why This Paper Is Here

Generative Point Cloud Registration은 정합할 두 점군의 깊이에서 서로 일관된 가상 컬러 영상을 생성해 점 대응을 찾는다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jiang25k/jiang25k.pdf#page=1) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jiang25k/jiang25k.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a novel 3D registration paradigm, Generative Point Cloud Registration, which bridges advanced 2D generative models with 3D matching tasks to ...
- **p. 1 / Abstract - extractive body cue:** Our key idea is to generate cross-view consistent image pairs that are wellaligned with the source and target point clouds, enabling geometry-color feature fusion to ...
- **p. 1 / Abstract - extractive body cue:** To ensure high-quality matching, the generated image pair should feature both 2D-3D geometric consistency and crossview texture consistency.
- **p. 1 / Abstract - extractive body cue:** To achieve this, we introduce Match-ControlNet, a matching-specific, controllable 2D generative model.
- **p. 1 / Abstract - extractive body cue:** Specifically, it leverages the depth-conditioned generation capability of ControlNet to produce images that are geometrically aligned with depth maps derived from point clouds, ensuring 2D-3D ...
- **p. 1 / 1. Introduction - extractive body cue:** However, in geometry-only point cloud registration, the RGB images corresponding to the point clouds are unavailable, and existing methods rely solely on 3D geometric information ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike geometry-only matching in previous methods, our approach introduces MatchControlNet, a matching-specific 2D generative model that generates cross-view images pairs from point cloud data, providing ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To summarize, our contributions are as follows: • We propose a new Generative Point Cloud Registration paradigm, aimed at generating cross-view image pairs for both ...
- **p. 2 / 1. Introduction - extractive body cue:** To achieve this, we introduce MatchControlNet, a matching-specific, controllable 2D generative model.
- **p. 4 / 3.3. Zero-Shot Texture Consistency Generation - extractive body cue:** Additionally, we introduce two key designs: coupled conditional denoising and coupled prompt guidance to achieve the cross-view texture consistency generation.
- **p. 4 / 3.3. Zero-Shot Texture Consistency Generation - extractive body cue:** To enable effective cross-view message passing without any finetuning (i.e., zero-shot), we propose an efficient coupled conditional denoising scheme for joint, interactive source and target ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike geometry-only matching in previous methods, our approach introduces MatchControlNet, a matching-specific 2D generative model that generates cross-view images pairs from point cloud data, providing ...
- **p. 4 / 3.2. Zero-Shot Geometric Consistency Generation - extractive body cue:** The denoiser follows a UNet architecture with an encoder, middle block, and skip-connected decoder, incorporating stacked transformer and residual modules.
- **p. 4 / 3.3. Zero-Shot Texture Consistency Generation - extractive body cue:** 4 illustrates that by coupling the source and target noisy latent representations, each feature element can establish longrange dependencies with all feature elements from both ...
- **p. 5 / 3.4. Few-Shot Consistency Fine-tuning - extractive body cue:** Finally, we use the loss function below to finetune the denoiser: L = ExPQ t ,t,˜c,dPQ,ϵ∼N(0,1) h

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Notably, ControlNet allows the use of depth maps as conditional inputs to generate RGB images that preserve geometric structures well-aligned with the provided depth prior. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Zero-Shot Geometric Consistency Generation), p. 5 (3.5. Geometric-Color Fused Point Descriptor) |
| State/latent | Notably, ControlNet, allows, depth, maps, conditional, inputs, generate, RGB, images, preserve, geometric | geometry, map, object/relationship state | p. 4 (3.2. Zero-Shot Geometric Consistency Generation), p. 5 (3.5. Geometric-Color Fused Point Descriptor), p. 4 (3.2. Zero-Shot Geometric Consistency Generation) |
| Output/action | These color point clouds are subsequently used as inputs to the color point cloud registration method, like ColorPCR (Mu et al., 2024), for 3D registration. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.5. Geometric-Color Fused Point Descriptor), p. 4 (3.2. Zero-Shot Geometric Consistency Generation), p. 2 (1. Introduction) |
| Objective/outcome | This capability perfectly aligns with our objective and motivates us to convert the source and target point clouds into their corresponding depth maps, DP and DQ ∈RH×W ×1, via the intrinsic matrix. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.2. Zero-Shot Geometric Consistency Generation), p. 5 (3.4. Few-Shot Consistency Fine-tuning), p. 4 (3.3. Zero-Shot Texture Consistency Generation) |

## Main Claims and Actual Contribution

- Match-ControlNet은 두 영상의 잡음 제거와 프롬프트 조건을 결합해 각 영상이 자기 점군에 맞으면서 공통 영역의 질감을 공유하도록 한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jiang25k/jiang25k.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jiang25k/jiang25k.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jiang25k/jiang25k.pdf#page=5)
- 생성된 색상 특징을 기하 특징과 결합하고 3DMatch와 ScanNet에서 기존 정합기에 추가했을 때의 대응 및 정합 성능을 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jiang25k/jiang25k.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/jiang25k/jiang25k.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (4.3. Ablation Studies and Analysis), p. 7 (4.3. Ablation Studies and Analysis) |
| Embodiment/environment | We first perform model evaluation on a widely-used, large-scale indoor benchmark dataset, ScanNet (Dai et al., 2017). | hardware/simulator version and reset protocol | p. 6 (4.2. Comparison with Existing Methods), p. 6 (4.1. Experimental Setting) |
| Dataset/benchmark | We next evaluate our method on 3DMatch (Zeng et al., 2017), another widely-used benchmark dataset for 3D registration. | role, split, size and leakage | p. 6 (4.2. Comparison with Existing Methods), p. 6 (4.1. Experimental Setting), p. 7 (4.2. Comparison with Existing Methods), p. 8 (4.3. Ablation Studies and Analysis) |
| Metric | Following (El Banani et al., 2021; Yuan et al., 2023), we use rotation error, translation error, and Chamfer error, including the accuracy across varying thresholds and mean/median errors, for performance evaluation. | definition, denominator, direction and uncertainty | p. 6 (4.1. Experimental Setting), p. 6 (Figure/Table caption), p. 7 (4.3. Ablation Studies and Analysis) |
| Baseline/ablation | Compared to the 20-frame separation used in (El Banani et al., 2021; Yuan et al., 2023), our approach with a 50-frame separation further reduces the overlap ratio (i.e., lower overlap), thereby increasing ... | fair input/data/compute/action matching | p. 6 (4.2. Comparison with Existing Methods), p. 7 (4.2. Comparison with Existing Methods), p. 7 (4.3. Ablation Studies and Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Pipeline of Generative Point Cloud Registration. Given a source and a target point cloud, we first apply Match-ControlNet to generate their corresponding images. ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Instead of independently performing ControlNet to gen- erate source and target images, our Match-ControlNet integrates their denoising generation processes into a unified framework, ...
- **p. 8 / 4.3. Ablation Studies and Analysis - extractive body cue:** 6 (right) shows that RGB data from real-world conditions can degrade under poor lighting, negatively impacting RGB-D matching performance.
- **p. 8 / 4.3. Ablation Studies and Analysis - extractive body cue:** Our results indicate that both overly high ω (which overemphasizes geometry) and overly low ω (which overemphasizes color) lead to degraded registration accuracy.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.2. Zero-Shot Geometric Consistency Generation), p. 4 (3.3. Zero-Shot Texture Consistency Generation), p. 5 (3.4. Few-Shot Consistency Fine-tuning)이다.
