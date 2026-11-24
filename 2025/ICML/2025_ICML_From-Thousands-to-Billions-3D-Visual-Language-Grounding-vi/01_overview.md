# From Thousands to Billions: 3D Visual Language Grounding via Render-Supervised Distillation from 2D VLMs

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/cao25a.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/167530. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Ang Cao, Sergio Arnaud, Oleksandr Maksymets, Jianing Yang, Ayush Jain, Ada Martin, Vincent-Pierre Berges, Paul Mcvay, Ruslan Partsey, Aravind Rajeswaran, Franziska Meier, Justin Johnson, Jeong Joon Park, Alexander Sax
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision
- Official paper: https://proceedings.mlr.press/v267/cao25a.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/cao25a/cao25a.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/cao25a/cao25a.pdf)

## Why This Paper Is Here

LIFT-GS는 점군에서 예측한 언어 조건부 3D 마스크를 영상에 렌더링하고 2D 기반 모델의 출력으로 감독해 수작업 3D 라벨 의존도를 낮춘다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/cao25a/cao25a.pdf#page=1) · [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/cao25a/cao25a.pdf#page=3)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D vision-language grounding faces a fundamental data bottleneck: while 2D models train on billions of images, 3D models have access to only thousands of labeled ...
- **p. 1 / Abstract - extractive body cue:** We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision.
- **p. 1 / Abstract - extractive body cue:** LIFT-GS predicts 3D Gaussian representations from point clouds and uses them to render predicted language-conditioned 3D masks into 2D views, enabling supervision from 2D foundation ...
- **p. 1 / Abstract - extractive body cue:** This rendersupervised formulation enables end-to-end training of complete encoder-decoder architectures and is inherently model-agnostic.
- **p. 1 / Abstract - extractive body cue:** LIFT-GS achieves state-of-the-art results with 25.7% mAP on open-vocabulary instance segmentation (vs.
- **p. 1 / 1. Introduction - extractive body cue:** This six-order-of-magnitude gap in data availability severely limits the capabilities of current 3D grounding systems, creating one of the most significant challenges in embodied AI.
- **p. 1 / 1. Introduction - extractive body cue:** Yet despite its importance, 3D vision-language grounding (3D VLG) faces a fundamental bottleneck: data scarcity.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We show how differentiable rendering enables training 3D models with 2D losses, eliminating dependence on scarce 3D annotations. • Demonstrating a pseudo-labeling strategy for distilling ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce Language-Indexed Field Transfer with Gaussian Splatting (LIFT-GS), which implements this idea as a practical training pipeline.
- **p. 1 / Abstract - extractive body cue:** We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision.
- **p. 1 / Abstract - extractive body cue:** This rendersupervised formulation enables end-to-end training of complete encoder-decoder architectures and is inherently model-agnostic.
- **p. 2 / 1. Introduction - extractive body cue:** First, it is inherently architecture-agnostic; specifying only the outputs leaves flexibility in underlying model design.
- **p. 2 / 1. Introduction - extractive body cue:** Second, this allows us to overcome fundamental scaling limitations by training a large transformer decoder instead of previous dual-encoder approaches (as shown in Fig 3) ...
- **p. 1 / 1. Introduction - extractive body cue:** [The] [bookshelf][near] [the] [table] [besides] [the] [wall] 3D Grounding Model 2D VLM Model 2D Grounding Loss 3D Segments Point Cloud Rendered Grounding Figure 1: LIFT-GS ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We train a powerful 3D vision language grounding model (i.e., 3D mask decoder) with point clouds and language as inputs by learning from 2D VLM foundation models without any 3D supervision. of ... | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | train, powerful, vision, language, grounding, model, mask, decoder, point, clouds, inputs, learning | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract) |
| Output/action | Third, the approach is highly practical: LIFT-GS operates directly on raw point clouds from sensors, such as the outputs from SLAM or SfM systems, eliminating the preprocessing and feature fusion required by ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 1 (Abstract), p. 2 (1. Introduction) |
| Objective/outcome | [The] [bookshelf][near] [the] [table] [besides] [the] [wall] 3D Grounding Model 2D VLM Model 2D Grounding Loss 3D Segments Point Cloud Rendered Grounding Figure 1: LIFT-GS Overview. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Main Claims and Actual Contribution

- SAM·CLIP의 영상 마스크와 언어 특징 등을 이용해 2D 의사 표적을 구성하고, 미분 가능한 가우시안 렌더링을 통해 3D 예측기를 학습한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/cao25a/cao25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/cao25a/cao25a.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/cao25a/cao25a.pdf#page=6)
- 개방 어휘 인스턴스 분할과 지시 표현에 의한 위치 추정에서 사전학습 유무 및 미세조정 데이터 규모의 효과를 비교했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/cao25a/cao25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/cao25a/cao25a.pdf#page=8) · [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/cao25a/cao25a.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 15 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Embodiment/environment | Although this provides good generalization, performance degrades with more detailed descriptions typical of real-world queries, as illustrated in Figure 3. | hardware/simulator version and reset protocol | p. 1 (1. Introduction), p. 1 (Abstract) |
| Dataset/benchmark | LIFT-GS achieves state-of-the-art performance on standard 3D VLG benchmarks, with 25.7% mAP on open-vocabulary instance segmentation (vs. | role, split, size and leakage | p. 1 (1. Introduction), p. 1 (Abstract), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Metric | Table 2: 3D Referential Grounding. We report top-1 accuracy with various IoU thresholds (0.25, 0.5). SR3D NR3D ScanRefer | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Baseline/ablation | Table 3: Comparison with other Pretraining Baseline. LIFT-GS clearly outperforms Ponder-v2 and its variant Ponder-v2†, which is trained on the same SAM-CLIP features as ours. | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 15 (Figure/Table caption), p. 1 (Abstract) |

## Explicit Limitations and Failure Boundary

- **p. 1 / 1. Introduction - extractive body cue:** From this perspective, the dual-encoder approach falls short of 3D grounding as it contradicts a core grounding requirement.
- **p. 1 / Abstract - extractive body cue:** We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision.
- **p. 2 / 1. Introduction - extractive body cue:** Second, this allows us to overcome fundamental scaling limitations by training a large transformer decoder instead of previous dual-encoder approaches (as shown in Fig 3) ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: 3D grounding with CLIP-style (dual-decoder) method. Grounding heatmaps from a representative approach (Guo et al., 2024). Heatmaps are computed using dot product similarity ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract)이다.
