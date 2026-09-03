# Geometry Forcing: Marrying Video Diffusion and 3D Representation for Consistent World Modeling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=ULXYZCms41.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247965. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Diffusion, Generation, 3D Vision
- Official paper: https://openreview.net/forum?id=ULXYZCms41
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247965
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 generative 문제를 이해하기 위해 읽는다. 본문은 Bridging the gap between video diffusion models and the dynamic 3D structure of the world presents significant challenges, primarily due to the limited annotated 3D data.를 문제로 두고, To align these two representations, our method introduces two complementary alignment objectives: Angular Alignment and Scale Alignment.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Videos inherently represent 2D projections of a dynamic 3D world.
- **p. 1 / ABSTRACT - extractive body cue:** However, our analysis suggests that video diffusion models trained solely on raw video data often fail to capture meaningful geometric-aware structure in their learned representations.
- **p. 1 / ABSTRACT - extractive body cue:** To bridge the gap between video diffusion models and the underlying 3D nature of the physical world, we propose Geometry Forcing, a simple yet effective ...
- **p. 1 / ABSTRACT - extractive body cue:** Our key insight is to guide the model's intermediate representations toward geometry-aware structure by aligning them with features from a geometric foundation model.
- **p. 1 / ABSTRACT - extractive body cue:** To this end, we introduce two complementary alignment objectives: Angular Alignment, which enforces directional consistency via cosine similarity, and Scale Alignment, which preserves scale-related information ...
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** Bridging the gap between video diffusion models and the dynamic 3D structure of the world presents significant challenges, primarily due to the limited annotated 3D ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this work, we aim to bridge the gap between video diffusion models and the underlying dynamic 3D structure of the physical world.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To align these two representations, our method introduces two complementary alignment objectives: Angular Alignment and Scale Alignment.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Experimental results demonstrate that our method delivers substantial gains in geometric consistency and visual quality over the baseline methods.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 4.2, we introduce two regularization objectives designed to facilitate representation alignment between the diffusion model and geometric foundation model.
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** In this section, we provide a brief overview of both components to establish the foundation for our method.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** In this work, inspired by recent advances in REPA (Yu et al., 2024a), we propose Geometry Forcing (GF) that aligns the features of video diffusion ...
- **p. 20 / C.4 METRICS - extractive body cue:** Method Frames FVD↓ LPIPS↓ SSIM↑ PSNR↑ RPE↓ RVE↓ DFoT (Song et al., 2025) 256 364 0.55 0.36 11.40 0.3575 297 Geometry Forcing-4 256 261 0.51 ...
- **p. 18 / C.4 METRICS - extractive body cue:** Specifically, DROID-SLAM first extracts corresponding features across frames and then refines camera poses (Gt) and per-pixel depth estimates (dt) through its differentiable Dense Bundle Adjustment ...
- **p. 18 / C.2 TRAINING - extractive body cue:** The geometric alignment loss is combined with the standard diffusion training objective.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We evaluate the effectiveness of GF on two widely adopted benchmarks: camera-view-conditioned video generation on RealEstate10K (Zhou et al., 2018) and action-conditioned video generation in the Minecraft environment (Baker et al., 2022). | conditioning observation와 noisy/intermediate sample | p. 2 (1 INTRODUCTION), p. 21 (C.4 METRICS) |
| State/latent | evaluate, effectiveness, widely, adopted, benchmarks, camera-view-conditioned, video, generation, RealEstate10K, Zhou, action-conditioned, Minecraft | latent/noise variable와 conditional distribution | p. 2 (1 INTRODUCTION), p. 21 (C.4 METRICS), p. 21 (C.4 METRICS) |
| Output/action | The feature extraction time of the VGGT model increases with the number of input views. | generated sample, action chunk 또는 trajectory | p. 21 (C.4 METRICS), p. 21 (C.4 METRICS), p. 4 (3 PRELIMINARIES) |
| Objective/outcome | The geometric alignment loss is combined with the standard diffusion training objective. | distribution fit, multimodality, sample quality와 latency | p. 18 (C.2 TRAINING), p. 18 (C.4 METRICS), p. 20 (C.4 METRICS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To align these two representations, our method introduces two complementary alignment objectives: Angular Alignment and Scale Alignment.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Experimental results demonstrate that our method delivers substantial gains in geometric consistency and visual quality over the baseline methods.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** 4.2, we introduce two regularization objectives designed to facilitate representation alignment between the diffusion model and geometric foundation model.
- **p. 3 / 3 PRELIMINARIES - extractive body cue:** In this section, we provide a brief overview of both components to establish the foundation for our method.
- **p. 4 / 3 PRELIMINARIES - extractive body cue:** In this work, inspired by recent advances in REPA (Yu et al., 2024a), we propose Geometry Forcing (GF) that aligns the features of video diffusion ...
- **p. 20 / C.4 METRICS - extractive body cue:** Experimental results demonstrate that our approach achieves improvements across multiple evaluation dimensions, including visual aesthetics, motion smoothness, and motion quality, as detailed in Table 11.
- **p. 19 / C.4 METRICS - extractive body cue:** We conduct Geometry Forcing algorithm on Pi3 model and also achieves significant improvement on video generation as shown in Tab.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 5, the model achieves a lower FVD score, indicating that GF can be seamlessly integrated into video diffusion models and yields measurable gains.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 20 (C.4 METRICS), p. 19 (C.4 METRICS) |
| Embodiment/environment | In this section, we evaluate Geometry Forcing (GF) on camera-view-conditioned video generation on the RealEstate10K (Zhou et al., 2018) dataset and action-conditioned video generation on the Minecraft environment (Baker et al., 2022). | hardware/simulator version and reset protocol | p. 6 (5 EXPERIMENTS), p. 18 (C.1 DATASET) |
| Dataset/benchmark | 2 presents qualitative comparisons on the RealEstate10K dataset. | role, split, size and leakage | p. 6 (5 EXPERIMENTS), p. 18 (C.1 DATASET), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Metric | 5, the model achieves a lower FVD score, indicating that GF can be seamlessly integrated into video diffusion models and yields measurable gains. | definition, denominator, direction and uncertainty | p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 6 (5 EXPERIMENTS) |
| Baseline/ablation | Figure 2: Qualitative comparison of camera view-conditioned video generation under full- circle rotation. Videos are generated from a single frame, and per-frame camera poses simulate a full 360° rotation. Our method (GF) ... | fair input/data/compute/action matching | p. 7 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6 CONCLUSION - extractive body cue:** The primary limitation of this work lies in its scale.
- **p. 22 / C.4 METRICS - extractive body cue:** E.4 FAILURE CASE ANALYSIS Although our method significantly improves visual quality and geometric consistency in video generation, they still struggle in certain complex scenarios.
- **p. 23 / Figure/Table caption - extractive body cue:** Figure 6: Failure Case Analysis. The transparent, reflective glass table intermittently disappears and reappears across frames, indicating that the model still has difficulty handling reflective ...
- **p. 24 / C.4 METRICS - extractive body cue:** While angular alignment alone helps maintain basic geometric coherence, the lack of scale supervision often leads to inconsistent camera motion, manifesting as unstable perspective changes ...
- **p. 6 / 236 Discussion - extractive body cue:** To combine the autoregressive nature with diffusion models, Diffusion Forcing (Chen et al., 2024a) proposes training video diffusion models with independent noise levels for each ...
- **p. 10 / 6 CONCLUSION - extractive body cue:** Motivated by the observation that video diffusion models trained on raw pixel data often fail to capture meaningful 3D structure, our method introduces two alignment ...
- **p. 19 / C.4 METRICS - extractive body cue:** D SUPPLEMENTARY EXPERIMENTS D.1 ABLATION ON TEACHER MODEL Geometry Forcing does not depend on a specific 3D foundation model but still requires the 3D foundation ...

## Why Read It

World models, safety, uncertainty, and recovery의 generative 문제를 이해하기 위해 읽는다. 본문은 Bridging the gap between video diffusion models and the dynamic 3D structure of the world presents significant challenges, primarily due to the limited annotated 3D data.를 문제로 두고, To align these two representations, our method introduces two complementary alignment objectives: Angular Alignment and Scale Alignment.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (3 PRELIMINARIES), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (3 PRELIMINARIES), p. 5 (3 PRELIMINARIES), p. 20 (C.4 METRICS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
