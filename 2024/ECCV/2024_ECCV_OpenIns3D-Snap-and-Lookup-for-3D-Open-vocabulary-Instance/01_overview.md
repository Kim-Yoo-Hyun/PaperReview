# OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, semantic
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, unlike 2D data that can be easily collected from the internet, constructing a large-scale 3D-text dataset poses a challenge.를 문제로 두고, To this end, we introduce OpenIns3D, a framework designed to effectively perform 3D open-vocabulary scene understanding tasks without relying on 2D aligned images.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 3D scene understanding plays a critical role in various domains, such as autonomous driving, robotic sensing, AR/VR, and manufacturing, among others. ⋆Corresponding author.
- **p. 2 / 1 Introduction - extractive body cue:** Class Lookup Tables SNAP MASK LOOKUP 3d Point Cloud Synthetic Scene-level Images 3D Open vocabulary Instance Segmentation Mask2Pixel Guidance Class-agnostic Mask Proposals 2D openworld detector ...
- **p. 2 / 1 Introduction - extractive body cue:** OVOD ScanNetV2 OVIS-8/4 S3DIS OVIS SPTLS3D Indoor Outdoor (b) Results Comparison OV-Rec ScanNetV2 OVIS-6/6 S3DIS Fig.
- **p. 2 / 1 Introduction - extractive body cue:** 2: High-level Illustrations of OpenIns3D and Quantitative Results.
- **p. 2 / 1 Introduction - extractive body cue:** (a) OpenIns3D follows the "Mask-Snap-Lookup" steps for open-vocabulary scene understanding.
- **p. 2 / 1 Introduction - extractive body cue:** However, unlike 2D data that can be easily collected from the internet, constructing a large-scale 3D-text dataset poses a challenge.
- **p. 2 / 1 Introduction - extractive body cue:** This limitation impacts its performance in dynamic and everchanging contexts.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** To this end, we introduce OpenIns3D, a framework designed to effectively perform 3D open-vocabulary scene understanding tasks without relying on 2D aligned images.
- **p. 4 / 1 Introduction - extractive body cue:** In summary, our contributions are: - OpenIns3D employs a distinct pipeline that operates without the need for well-aligned images.
- **p. 2 / 1 Introduction - extractive body cue:** While the development of 3D closed-set understanding is relatively mature, scene understanding in an open-vocabulary setting is still in its infancy.
- **p. 2 / 1 Introduction - extractive body cue:** We believe that developing a 3D open-vocabulary framework without relying on well-aligned 2D images is meaningful, as this will simplify deployment pre
- **p. 3 / 1 Introduction - extractive body cue:** The design of OpenIns3D also allows 2D detectors to be changed without the need for retraining.
- **p. 3 / 1 Introduction - extractive body cue:** Mask: Given a 3D point cloud, the first part of OpenIns3D learns class-agnostic mask proposals with a Mask Proposal Module (MPM).
- **p. 1 / Body text (section not recovered) - extractive body cue:** The "Mask" module learns class-agnostic mask proposals in 3D point clouds, the "Snap" module generates synthetic scene-level images at multiple scales and leverages 2D vision-language ...
- **p. 2 / 1 Introduction - extractive body cue:** This means that posed 2D images, associated depth maps and camera models need to be accessible as inputs to the network.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This approach achieves state-of-the-art results across a range of benchmarks and possesses the ability to comprehend highly complex input queries. - The proposed "Snap and Lookup" combination can serve as a powerful ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | achieves, state-of-the-art, across, range, benchmarks, possesses, ability, comprehend, highly, complex, input, queries | geometry, map, object/relationship state | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 1 (Body text (section not recovered)) |
| Output/action | This means that posed 2D images, associated depth maps and camera models need to be accessible as inputs to the network. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 1 (Body text (section not recovered)), p. 2 (1 Introduction) |
| Objective/outcome | These images are specifically designed to encompass part or all of the relevant masks, aiming to minimize the need for multiple renderings. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** To this end, we introduce OpenIns3D, a framework designed to effectively perform 3D open-vocabulary scene understanding tasks without relying on 2D aligned images.
- **p. 4 / 1 Introduction - extractive body cue:** In summary, our contributions are: - OpenIns3D employs a distinct pipeline that operates without the need for well-aligned images.
- **p. 2 / 1 Introduction - extractive body cue:** While the development of 3D closed-set understanding is relatively mature, scene understanding in an open-vocabulary setting is still in its infancy.
- **p. 2 / 1 Introduction - extractive body cue:** We believe that developing a 3D open-vocabulary framework without relying on well-aligned 2D images is meaningful, as this will simplify deployment pre
- **p. 3 / 1 Introduction - extractive body cue:** The design of OpenIns3D also allows 2D detectors to be changed without the need for retraining.
- **p. 11 / 4 Experiments - extractive body cue:** Significant improvements are achieved on the S3DIS dataset, and competitive results are observed on ScanNetv2 (B/N: Base/Novel).
- **p. 12 / 4 Experiments - extractive body cue:** Model use 2D APhead APcommon APtail AP AP50 AP25 OpenScene (2D Fusion) [23] ✓ 13.4 11.6 9.9 11.7 15.2 17.8 OpenScene (2D/3D Ens.) [23] ✓ ...
- **p. 11 / 4 Experiments - extractive body cue:** With the enhanced recognition capability, the performance of 3D open-vocabulary Object Detection among the ScanNet dataset has also achieved state-of-the-art results by a large margin.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Embodiment/environment | Model 2D AP AP50 AP25 OpenScene [23] (2D Fusion) ✓ 10.9 15.6 17.3 OpenScene [23] (2D/3D Ens.) ✓ 8.2 10.4 13.3 OpenMask3D [30] ✓ 13.1 18.4 24.2 OpenScene [23] (3D Distill) ✗ ... | hardware/simulator version and reset protocol | p. 12 (4 Experiments), p. 11 (4 Experiments) |
| Dataset/benchmark | Among them, S3DIS, ScanNetv2, and ScanNet200 are indoor point cloud datasets generated from RGBD images, Replica is a photo-realistic 3D indoor scene reconstruction, while STPLS3D is an aerial photogrammetry-constructed outdoor dataset. | role, split, size and leakage | p. 12 (4 Experiments), p. 11 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments) |
| Metric | Following the evaluation on ScanNetv2, we assessed the class-agnostic mask quality using the average precision (AP) score. | definition, denominator, direction and uncertainty | p. 12 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Baseline/ablation | For STPLS3D, we compared OpenIns3D with baseline models whose classification module is PointCLIP and PointCLIPV2 [43] (Table 5). | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 12 / Figure/Table caption - extractive body cue:** Table 6: 3D instance segmentation results on the ScanNet200 validation set. OpenIns3D demonstrates robust performance when compared to 2D-input-free models. However, notable limitations emerge when ...
- **p. 12 / 4 Experiments - extractive body cue:** It also shows certain limitations on small objects that are not well-reconstructed in 3D scenes.
- **p. 11 / 4 Experiments - extractive body cue:** For 3D instance segmentation, compared to works in the PLA family [9,10,34] and the latest work Open3DIS [22], OpenIns3D does not require aligned images as ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, unlike 2D data that can be easily collected from the internet, constructing a large-scale 3D-text dataset poses a challenge.를 문제로 두고, To this end, we introduce OpenIns3D, a framework designed to effectively perform 3D open-vocabulary scene understanding tasks without relying on 2D aligned images.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (Body text (section not recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
