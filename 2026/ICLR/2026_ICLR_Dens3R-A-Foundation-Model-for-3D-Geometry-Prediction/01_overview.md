# Dens3R: A Foundation Model for 3D Geometry Prediction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=kxVjQhkAWz.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/247872. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision
- Official paper: https://openreview.net/forum?id=kxVjQhkAWz
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/247872
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (31 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, training such a multi-task, multi-output 3D foundation model still faces significant challenges.를 문제로 두고, For the training strategy, we propose a novel two-staged approach.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Recent advances in dense 3D reconstruction have led to significant progress, yet achieving accurate unified geometric prediction remains a major challenge.
- **p. 1 / ABSTRACT - extractive body cue:** Most existing methods are limited to predicting a single geometry quantity from input images.
- **p. 1 / ABSTRACT - extractive body cue:** However, geometric quantities such as depth, surface normals, and point maps are inherently correlated, and estimating them in isolation often fails to ensure consistency, thereby ...
- **p. 1 / ABSTRACT - extractive body cue:** This motivates us to explore a unified framework that explicitly models the structural coupling among different geometric properties to enable joint regression.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we present Dens3R, a 3D foundation model designed for joint geometric dense prediction and adaptable to a wide range of downstream tasks.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, training such a multi-task, multi-output 3D foundation model still faces significant challenges.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Furthermore, the aforementioned methods mainly handle only one geometric quantity prediction and cannot generalize to output multiple geometric quantities in a single forward pass.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** For the training strategy, we propose a novel two-staged approach.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, our method allows the communication between 3D geometric representation and normal prediction without known camera poses.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we present Dens3R, a foundation model for high-quality geometric prediction.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** We propose Dens3R, a dense visual transformer backbone featuring a shared encoder-decoder architecture and multiple task-specific heads for geometric prediction.
- **p. 5 / 3 METHOD - extractive body cue:** To this end, we propose to build upon a unified geometric representation since all geometric representations are inherently interconvertible.
- **p. 7 / 3 METHOD - extractive body cue:** Specifically, we introduce high-quality normal supervision based on the first stage's point map, and jointly fine-tune the encoder-decoder module, point map prediction head, and newly ...
- **p. 5 / 3 METHOD - extractive body cue:** (2025a;b), we first employ a sharedweight encoder to process input image sequences and extract image features Feai, which are then fed into the decoder.
- **p. 6 / 3 METHOD - extractive body cue:** Suppose ˆ M = (i, j) is the set of ground-truth correspondences where the ith pixel in the first image matches the jth pixel in ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The normal prediction head is connected after the initial point map training is completed, allowing the model to consistently output coherent normal mappings from the same input image, thereby internalizing this intrinsic ... | RGB-D, image set, point cloud, depth와 camera pose | p. 7 (3 METHOD), p. 5 (3 METHOD) |
| State/latent | normal, prediction, head, connected, after, initial, point, training, completed, allowing, model, consistently | geometry, map, object/relationship state | p. 7 (3 METHOD), p. 5 (3 METHOD), p. 4 (1 INTRODUCTION) |
| Output/action | Given an image pair of image sequence (Ii)2 i=1 ∈R3×H×W , Dens3R's dense visual transformer is a function f that maps the input to a corresponding set of 3D quantities per frame: ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 METHOD), p. 4 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective/outcome | This loss function simultaneously optimizes for two objectives. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3 METHOD), p. 6 (3 METHOD), p. 7 (3 METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** For the training strategy, we propose a novel two-staged approach.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** In contrast, our method allows the communication between 3D geometric representation and normal prediction without known camera poses.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we present Dens3R, a foundation model for high-quality geometric prediction.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** We propose Dens3R, a dense visual transformer backbone featuring a shared encoder-decoder architecture and multiple task-specific heads for geometric prediction.
- **p. 5 / 3 METHOD - extractive body cue:** To this end, we propose to build upon a unified geometric representation since all geometric representations are inherently interconvertible.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparison of normal prediction. Dens3R generates more accurate and de- tailed normal maps than previous methods for both object-centric and unbounded scenes,. ...
- **p. 24 / Figure/Table caption - extractive body cue:** Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. inputs ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative comparison of depth maps and pointmaps. We compare our method with previous DUSt3R-based methods and demonstrate high-quality depth prediction results. Dens3R also ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 24 (Figure/Table caption) |
| Embodiment/environment | 4.1 NORMAL AND MATCHING PREDICTION We evaluate our Dens3R on several surface normal prediction datasets that include both indoor and outdoor scenes. | hardware/simulator version and reset protocol | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Dataset/benchmark | The dataset includes indoor scenes, outdoor scenes, and object-level data. | role, split, size and leakage | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.3 IMPLEMENTATION DETAILS), p. 20 (A.3 IMPLEMENTATION DETAILS) |
| Metric | It can be seen that our method yields higher accuracy and surpasses previous methods across nearly all datasets, demonstrating our superior performance across various evaluation protocols. | definition, denominator, direction and uncertainty | p. 9 (4 EXPERIMENTS), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Baseline/ablation | Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. inputs without causing degenerated predictions like p ... | fair input/data/compute/action matching | p. 24 (Figure/Table caption), p. 9 (4 EXPERIMENTS), p. 23 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 24 / Figure/Table caption - extractive body cue:** Figure 12: Limitations. Despite that our method outperforms previous methods in geometric pre- dictions, the prediction quality for thin structures still require further improvement. inputs ...
- **p. 28 / A.8 LIMITATION - extractive body cue:** We compare our depth prediction results with VGGT and Dens3R demonstrates more robust and accurate predictions.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Dens3R is a feed-forward visual foundation model that takes unposed images as input and outputs high-quality 3D pointmap with unified geometric dense prediction. ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** As for pointmap prediction, MoGe and VGGT often fail to recover depth for reflective surfaces and tend to produce flattened pointmaps in background regions.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 6: High-quality geometric predictions for high-resolution (2K) inputs. Please zoom in to better observe the fine-grained details. Position-Interpolated Rotary Positional Encoding. Dens3R can support ...
- **p. 18 / Figure/Table caption - extractive body cue:** Table 4: Ablation on shared encoder-decoder structure. We conduct experiments for both of the model on image pairs with 512 resolution. With the shared encoder-decoder ...
- **p. 19 / A.3 IMPLEMENTATION DETAILS - extractive body cue:** We then make the most of high-quality synthetic data in the training process for more accurate and robust predictions.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, training such a multi-task, multi-output 3D foundation model still faces significant challenges.를 문제로 두고, For the training strategy, we propose a novel two-staged approach.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 7 (3 METHOD), p. 5 (3 METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
