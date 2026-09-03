# GaussianFusion: Unified 3D Gaussian Representation for Multi-Modal Fusion Perception

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=7jXxQ9bGoU.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/246879. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Official paper: https://openreview.net/forum?id=7jXxQ9bGoU
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/246879
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Since different sensors present data in varying formats, such as cameras providing perspective semantic data and Lidar capturing 3D spatial information, multi-modal fusion faces significant challenges due to these view discrepancies.를 문제로 두고, Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally aggregated through the Gaussian mixture m ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** The bird's-eye view (BEV) representation enables multi-sensor features to be fused within a unified space, serving as the primary approach for achieving comprehensive 3D perception.
- **p. 1 / ABSTRACT - extractive body cue:** However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception.
- **p. 1 / ABSTRACT - extractive body cue:** In this work, we break from the conventional BEV paradigm and propose a new universal framework for multimodal fusion based on 3D Gaussian representation.
- **p. 1 / ABSTRACT - extractive body cue:** This approach naturally unifies multi-modal features within a shared and continuous 3D Gaussian space, effectively preserving edge and fine texture details.
- **p. 1 / ABSTRACT - extractive body cue:** To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Since different sensors present data in varying formats, such as cameras providing perspective semantic data and Lidar capturing 3D spatial information, multi-modal fusion faces significant ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Leveraging the distinct characteristics of each sensor helps reduce prediction uncertainty, leading to more accurate and robust perception outcomes (Liu et al., 2023b; Bai et ...

## Core Idea

- **p. 2 / 20560 M - extractive body cue:** Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally ...
- **p. 2 / 20560 M - extractive body cue:** To address these challenges, we introduce a fusion approach based on 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) to achieve more fine-grained information modeling ...
- **p. 1 / ABSTRACT - extractive body cue:** The bird's-eye view (BEV) representation enables multi-sensor features to be fused within a unified space, serving as the primary approach for achieving comprehensive 3D perception.
- **p. 6 / 6 Cameras - extractive body cue:** This Gaussian prior enables better alignment of crossmodal features to the "likely object extent," thereby enhancing fusion effectiveness-a capability absent in conventional square-shaped initialization.
- **p. 1 / ABSTRACT - extractive body cue:** To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on ...
- **p. 1 / ABSTRACT - extractive body cue:** However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception.
- **p. 6 / 6 Cameras - extractive body cue:** We then project the 3D reference points onto the BEV feature map, where each Gaussian query qi ↔Qi is updated through deformable attention, expressed as: ...
- **p. 6 / 6 Cameras - extractive body cue:** To update the Gaussian properties, we propose an iterative optimization strategy of predicting offsets instead of predicting a set of new Gaussian distributions as adopted ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | However, the discrete grid representation of BEV leads to significant detail loss and limits feature alignment and cross-modal information interaction in multimodal fusion perception. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (ABSTRACT), p. 2 (20560 M) |
| State/latent | However, discrete, grid, representation, BEV, leads, significant, detail, loss, limits, feature, alignment | geometry, map, object/relationship state | p. 1 (ABSTRACT), p. 2 (20560 M), p. 2 (20560 M) |
| Output/action | During feature extraction, perception data are projected onto a fixed-resolution BEV grid, which compresses spatial information. | point map, pose, scene graph, affordance 또는 query result | p. 2 (20560 M), p. 2 (20560 M), p. 4 (6 Cameras) |
| Objective/outcome | Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally aggregated through the Gaussian mixture m ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (20560 M), p. 1 (ABSTRACT), p. 2 (20560 M) |

## Main Claims and Actual Contribution

- **p. 2 / 20560 M - extractive body cue:** Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally ...
- **p. 2 / 20560 M - extractive body cue:** To address these challenges, we introduce a fusion approach based on 3D Gaussian Splatting (3DGS) (Kerbl et al., 2023) to achieve more fine-grained information modeling ...
- **p. 1 / ABSTRACT - extractive body cue:** The bird's-eye view (BEV) representation enables multi-sensor features to be fused within a unified space, serving as the primary approach for achieving comprehensive 3D perception.
- **p. 6 / 6 Cameras - extractive body cue:** This Gaussian prior enables better alignment of crossmodal features to the "likely object extent," thereby enhancing fusion effectiveness-a capability absent in conventional square-shaped initialization.
- **p. 1 / ABSTRACT - extractive body cue:** To achieve this, we design a novel forward-projection-based multi-modal Gaussian initialization module and a shared cross-modal Gaussian encoder that iteratively updates Gaussian properties based on ...
- **p. 8 / 4.1 DATASET - extractive body cue:** Experimental results show that, compared to BEVFusion4D (Liu et al., 2023b), our temporal variant GaussianFusion-T achieves significant improvements.
- **p. 9 / 4.1 DATASET - extractive body cue:** More importantly, benefiting from our proposed Gaussian initialization strategy and iterative update mechanism, GaussianFusion-C achieves a 1.55 mIoU improvement and nearly 4.5! computational efficiency compared ...
- **p. 10 / 4.1 DATASET - extractive body cue:** Results show that deformable attention with Gaussian priors outperforms the vanilla variant by +0.4 NDS, demonstrating that the shape prior encoded by Gaussians facilitates model ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (4.1 DATASET), p. 9 (4.1 DATASET) |
| Embodiment/environment | It is a large-scale multimodal dataset officially split into 700/150/150 scenes for training, validation, and testing, respectively. | hardware/simulator version and reset protocol | p. 7 (4.1 DATASET), p. 7 (4.1 DATASET) |
| Dataset/benchmark | We further conduct experiments on the Waymo Open Dataset (Sun et al., 2020) to evaluate the generalization capability of our approach. | role, split, size and leakage | p. 7 (4.1 DATASET), p. 7 (4.1 DATASET), p. 9 (4.1 DATASET), p. 8 (4.1 DATASET) |
| Metric | We utilize the official evaluation metric nuScenes Detection Score (NDS) and mean Average Precision (mAP) for 3D detection. | definition, denominator, direction and uncertainty | p. 7 (4.1 DATASET), p. 8 (4.1 DATASET), p. 9 (4.1 DATASET) |
| Baseline/ablation | In addition, compared with recent SOTA fusion works, such as UniTR (Wang et al., 2023a), EA-LSS (Hu et al., 2023b), and FusionFormer-S (Hu et al., 2023a), GaussianFusion shows superior performance, outperforming them ... | fair input/data/compute/action matching | p. 7 (4.1 DATASET), p. 8 (4.1 DATASET), p. 7 (4.1 DATASET) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 4.1 DATASET - extractive body cue:** 4.7 LIMITATIONS Several approaches-covering both detection (Wang et al., 2023b) and Occ (Zhang et al., 2024b)-employ carefully designed temporal fusion modules to enhance performance.
- **p. 10 / 4.1 DATASET - extractive body cue:** A promising direction for future work is to explore motion-aware Gaussian updates, for instance by predicting velocity-guided offsets, enabling more coherent 4D scene modeling over ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Since different sensors present data in varying formats, such as cameras providing perspective semantic data and Lidar capturing 3D spatial information, multi-modal fusion faces significant challenges due to these view discrepancies.를 문제로 두고, Main contributions are as follows: • We propose the first unified 3D Gaussian representation multi-modal fusion framework, where cross-view and cross-modal Gaussian representations are naturally aggregated through the Gaussian mixture m ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (20560 M), p. 1 (ABSTRACT), p. 6 (6 Cameras), p. 2 (20560 M) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
