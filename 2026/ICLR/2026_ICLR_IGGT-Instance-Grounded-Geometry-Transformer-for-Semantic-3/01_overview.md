# IGGT: Instance-Grounded Geometry Transformer for Semantic 3D Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=swiL18PmUV.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/248038. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D reconstruction, semantic, alignment, 3D Vision
- Official paper: https://openreview.net/forum?id=swiL18PmUV
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/248038
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (26 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these approaches suffer from three critical limitations.를 문제로 두고, 3.1 OVERVIEW Our method consists of two main phases.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Humans naturally perceive the geometric structure and semantic content of a 3D world as intertwined dimensions, enabling coherent and accurate understanding of complex scenes.
- **p. 1 / ABSTRACT - extractive body cue:** However, most prior approaches prioritize training large geometry models for low-level 3D reconstruction and treat high-level spatial understanding in isolation, overlooking the crucial interplay between ...
- **p. 1 / ABSTRACT - extractive body cue:** Recent attempts have mitigated this issue by simply aligning 3D models with specific language models, thus restricting perception to the aligned model's capacity and limiting ...
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we propose InstanceGrounded Geometry Transformer (IGGT), an end-to-end large unified transformer to unify the knowledge for both spatial reconstruction and instance-level contextual ...
- **p. 1 / ABSTRACT - extractive body cue:** Specifically, we design a 3D-Consistent Contrastive Learning strategy that guides IGGT to encode a unified representation with geometric structures and instance-grounded clustering through only 2D ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, these approaches suffer from three critical limitations.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Recently emerged methods (Fan et al., 2024; Sun et al., 2025) attempt to bridge this gap by aligning spatial models with specific VLM (Li et ...

## Core Idea

- **p. 4 / 3 METHODOLOGY - extractive body cue:** 3.1 OVERVIEW Our method consists of two main phases.
- **p. 7 / 3 METHODOLOGY - extractive body cue:** We present two example scenes from ScanNet (Dai et al., 2017) and ScanNet++ (Yeshwanth et al., 2023), and compare our method with SAM2* and SpaTracker+SAM.
- **p. 6 / 3 METHODOLOGY - extractive body cue:** 1, our method is the only one that simultaneously enables multi-view instance matching, image-to-3D reconstruction, and scene understanding, while achieving state-of-the-art performance across all tasks.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this, we propose Instance-Grounded Geometry Transformer (IGGT), a novel end-to-end framework that unifies the representation for spatial reconstruction and contextual understanding.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Moreover, regarding real-world scenarios, we propose a novel data curation pipeline that includes multi-view mask anVanilla GT Our Refined RGB Image (c) RGBD-Scan Scene Gen.
- **p. 4 / 3 METHODOLOGY - extractive body cue:** (1) Our IGGT consists of three parts: 1) a Large Unified Transformer to capture Unified Token Representation from multiple images; 2) two Downstream Heads with ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** Overall, we train the whole model in a multi-task loss: Loverall = Lpose + Ldepth + Lpmap + Lmvc, (5) where geometry supervision terms pose ...
- **p. 5 / 3 METHODOLOGY - extractive body cue:** (2) Moreover, to enhance the fine-grained spatial awareness of the instance head, we propose a crossmodal fusion block Fwin(·), which utilizes a sliding window cross ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Overall, we train the whole model in a multi-task loss: Loverall = Lpose + Ldepth + Lpmap + Lmvc, (5) where geometry supervision terms pose Lpose, depth Ldepth, and point map Lpmap ... | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 METHODOLOGY), p. 2 (1 INTRODUCTION) |
| State/latent | Overall, train, whole, model, multi-task, loss, Loverall, Lpose, Ldepth, Lpmap, Lmvc, where | geometry, map, object/relationship state | p. 5 (3 METHODOLOGY), p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY) |
| Output/action | A foundational goal in the pursuit of spatial intelligence (Yang et al., 2025) is to build representations that mirror human understanding-capturing both the precise geometric structure and rich semantic content of a ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 4 (3 METHODOLOGY) |
| Objective/outcome | This objective structures the instance representations according to the 3D scene geometry, improving generalization. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3 METHODOLOGY), p. 5 (3 METHODOLOGY), p. 17 (A.4 TRAINING DETAILS) |

## Main Claims and Actual Contribution

- **p. 4 / 3 METHODOLOGY - extractive body cue:** 3.1 OVERVIEW Our method consists of two main phases.
- **p. 7 / 3 METHODOLOGY - extractive body cue:** We present two example scenes from ScanNet (Dai et al., 2017) and ScanNet++ (Yeshwanth et al., 2023), and compare our method with SAM2* and SpaTracker+SAM.
- **p. 6 / 3 METHODOLOGY - extractive body cue:** 1, our method is the only one that simultaneously enables multi-view instance matching, image-to-3D reconstruction, and scene understanding, while achieving state-of-the-art performance across all tasks.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address this, we propose Instance-Grounded Geometry Transformer (IGGT), a novel end-to-end framework that unifies the representation for spatial reconstruction and contextual understanding.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Moreover, regarding real-world scenarios, we propose a novel data curation pipeline that includes multi-view mask anVanilla GT Our Refined RGB Image (c) RGBD-Scan Scene Gen.
- **p. 20 / A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS - extractive body cue:** Our method significantly outperforms graph-based grouping approaches such as VGGT+Graph Cut across all metrics, achieving an 8.83 improvement in AP.
- **p. 9 / 8.83 AP while avoiding its expensive mesh gen - extractive body cue:** This further demonstrates the flexibility of our method in using different VLMs to achieve improved text query performance.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** By leveraging implicit 3D reasoning, our approach successfully distinguishes object identities to achieve nearly 100% TSR accuracy.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS), p. 9 (8.83 AP while avoiding its expensive mesh gen) |
| Embodiment/environment | We evaluate our model on various OOD scenarios: outdoor scenes (ETH3D (Schops et al., 2017)), autonomous driving scenes (Waymo Open Dataset (Sun et al., 2020)), and egocentric-view data (robotics data and a ... | hardware/simulator version and reset protocol | p. 9 (8.83 AP while avoiding its expensive mesh gen), p. 7 (4 EXPERIMENTS) |
| Dataset/benchmark | While web-captured datasets such as RE10K (Zhou et al., 2018) offer a large number of scenes (i.e., high diversity), they lack depth and 3D-consistent instance masks. | role, split, size and leakage | p. 9 (8.83 AP while avoiding its expensive mesh gen), p. 7 (4 EXPERIMENTS), p. 17 (A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET), p. 17 (A.6 ADDITION INFORMATION OF OUR INSSCENE-15K DATASET) |
| Metric | (a) For MultiView Instance Matching evaluation, we evaluate tracking performance using Temporal mIoU (TmIoU) and Temporal Success Rate (T-SR). | definition, denominator, direction and uncertainty | p. 7 (4 EXPERIMENTS), p. 20 (A.8 CLASS-AGNOSTIC SEGMENTATION EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Baseline/ablation | Figure 9: Visualization of the Class-Agnostic 3D Mask Segmentation Results. Applications of QA Scene Grounding. We present the QA application results in Fig. 11 on the Teatime scene from the LERF-OVS (Kerr ... | fair input/data/compute/action matching | p. 9 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 24 / A.13 LIMITATION - extractive body cue:** As a result, the accuracy of object boundaries in the clustered masks cannot yet rival that of state-of-the-art segmentation models (e.g., SAM2 (Ravi et al., ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 16: We visualize the RGB and semantic 3D points of the ground truth, IGGT(Ours), LSM(Multi-Views), and Feature-3DGS. supervision fails to provide sufficiently discriminative instance ...
- **p. 24 / A.13 LIMITATION - extractive body cue:** Future work may integrate stronger DETR-based (Cheng et al., 2022) instance heads and larger annotated datasets to improve segmentation accuracy.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** In contrast, baseline methods fail at this crucial task, yielding a T-mIoU below 30%, whereas our approach surpasses 60%.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these approaches suffer from three critical limitations.를 문제로 두고, 3.1 OVERVIEW Our method consists of two main phases.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
