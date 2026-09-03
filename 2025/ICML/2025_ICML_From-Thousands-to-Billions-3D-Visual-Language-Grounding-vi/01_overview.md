# From Thousands to Billions: 3D Visual Language Grounding via Render-Supervised Distillation from 2D VLMs

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=w8MCYYAvQD.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/167530. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, 3D Vision
- Official paper: https://openreview.net/forum?id=w8MCYYAvQD
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/167530
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This six-order-of-magnitude gap in data availability severely limits the capabilities of current 3D grounding systems, creating one of the most significant challenges in embodied AI.를 문제로 두고, We show how differentiable rendering enables training 3D models with 2D losses, eliminating dependence on scarce 3D annotations. • Demonstrating a pseudo-labeling strategy for distilling 2D foundation models into 3D.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** We show how differentiable rendering enables training 3D models with 2D losses, eliminating dependence on scarce 3D annotations. • Demonstrating a pseudo-labeling strategy for distilling ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce Language-Indexed Field Transfer with Gaussian Splatting (LIFT-GS), which implements this idea as a practical training pipeline.
- **p. 1 / Abstract - extractive body cue:** We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision.
- **p. 1 / Abstract - extractive body cue:** This rendersupervised formulation enables end-to-end training of complete encoder-decoder architectures and is inherently model-agnostic.
- **p. 15 / Figure/Table caption - extractive body cue:** Table 8: Comparison to 3D pseudolabels. A mask decoder trained on top of frozen LIFT-GS features matches and even outperforms a decoder trained on top ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Loss Ablation. We show the impact of different pretrain- ing losses on 3D referential grounding task. Lground significantly improves results, particularly at high ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. It significantly outperforms its counterpart trained from scratch (LIFT-GS-Scratch mAP +3.2%).
- **p. 1 / Abstract - extractive body cue:** LIFT-GS achieves state-of-the-art results with 25.7% mAP on open-vocabulary instance segmentation (vs.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This six-order-of-magnitude gap in data availability severely limits the capabilities of current 3D grounding systems, creating one of the most significant challenges in embodied AI.를 문제로 두고, We show how differentiable rendering enables training 3D models with 2D losses, eliminating dependence on scarce 3D annotations. • Demonstrating a pseudo-labeling strategy for distilling 2D foundation models into 3D.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract), p. 2 (1. Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
