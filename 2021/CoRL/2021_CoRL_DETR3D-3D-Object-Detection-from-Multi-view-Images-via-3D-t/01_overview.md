# DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D Queries

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2110.06922.
> PDF retrieval source: https://arxiv.org/pdf/2110.06922. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, BEV, 3D detection, camera
- Official paper: https://arxiv.org/abs/2110.06922
- Full-text retrieval: https://arxiv.org/pdf/2110.06922
- Code/Project: https://github.com/WangYueFt/detr3d
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 3D object detection from visual information is a long-standing challenge for low-cost autonomous driving systems.를 문제로 두고, We summarize our key contributions as follows: • We present a streamlined 3D object detection model from RGB images.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce a framework for multi-camera 3D object detection.
- **p. 1 / Abstract - extractive body cue:** In contrast to existing works, which estimate 3D bounding boxes directly from monocular images or use depth prediction networks to generate input for 3D object ...
- **p. 1 / Abstract - extractive body cue:** Our architecture extracts 2D features from multiple camera images and then uses a sparse set of 3D object queries to index into these 2D features, ...
- **p. 1 / Abstract - extractive body cue:** Finally, our model makes a bounding box prediction per object query, using a set-to-set loss to measure the discrepancy between the ground-truth and the prediction.
- **p. 1 / Abstract - extractive body cue:** This top-down approach outperforms its bottom-up counterpart in which object bounding box prediction follows per-pixel depth estimation, since it does not suffer from the compounding ...
- **p. 1 / 1 Introduction - extractive body cue:** 3D object detection from visual information is a long-standing challenge for low-cost autonomous driving systems.
- **p. 1 / 1 Introduction - extractive body cue:** Existing methods [1, 2] typically build their detection pipelines purely from 2D computations.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** We summarize our key contributions as follows: • We present a streamlined 3D object detection model from RGB images.
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, our method does not require any post-processing, such as non-maximum suppression (NMS), improving efficiency and reducing reliance on hand-designed methods for cleaning its output.
- **p. 1 / Abstract - extractive body cue:** We introduce a framework for multi-camera 3D object detection.
- **p. 1 / Abstract - extractive body cue:** In contrast to existing works, which estimate 3D bounding boxes directly from monocular images or use depth prediction networks to generate input for 3D object ...
- **p. 2 / 1 Introduction - extractive body cue:** To the best of our knowledge, this is the first attempt to cast multi-camera detection as 3D set-to-set prediction. • We introduce a module that ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose a more graceful transition between 2D observations and 3D predictions for autonomous driving, which does not rely on a module ...
- **p. 1 / Abstract - extractive body cue:** Our architecture extracts 2D features from multiple camera images and then uses a sparse set of 3D object queries to index into these 2D features, ...
- **p. 1 / Abstract - extractive body cue:** Finally, our model makes a bounding box prediction per object query, using a set-to-set loss to measure the discrepancy between the ground-truth and the prediction.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In contrast to existing works, which estimate 3D bounding boxes directly from monocular images or use depth prediction networks to generate input for 3D object detection from 2D information, our method manipulates ... | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (Abstract), p. 2 (1 Introduction) |
| State/latent | contrast, existing, works, estimate, bounding, boxes, directly, monocular, images, depth, prediction, networks | geometry, map, object/relationship state | p. 1 (Abstract), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | In this paper, we propose a more graceful transition between 2D observations and 3D predictions for autonomous driving, which does not rely on a module for dense depth prediction. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | 3D object detection from visual information is a long-standing challenge for low-cost autonomous driving systems. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** We summarize our key contributions as follows: • We present a streamlined 3D object detection model from RGB images.
- **p. 2 / 1 Introduction - extractive body cue:** Moreover, our method does not require any post-processing, such as non-maximum suppression (NMS), improving efficiency and reducing reliance on hand-designed methods for cleaning its output.
- **p. 1 / Abstract - extractive body cue:** We introduce a framework for multi-camera 3D object detection.
- **p. 1 / Abstract - extractive body cue:** In contrast to existing works, which estimate 3D bounding boxes directly from monocular images or use depth prediction networks to generate input for 3D object ...
- **p. 7 / 4 Experiments - extractive body cue:** We also provide quantitative results in Table 5, which shows that iterative refinement indeed improves performance significantly.
- **p. 7 / 4 Experiments - extractive body cue:** Furthermore, we provide ablations on the number of object queries in Table 6; increasing the number queries consistently improves the performance until it gets saturated ...
- **p. 6 / 4 Experiments - extractive body cue:** As shown in Table 1, our method outperforms these methods even though we do not use any post-processing.
- **p. 6 / 4 Experiments - extractive body cue:** On the test set (Table 2), our method outperforms all existing methods as of 10/13/2021; our method uses the same backbone as DD3D [37] for ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | We test our method on the nuScenes dataset [33]. nuScenes consists of 1,000 sequences; each sequence is roughly 20s long, with a sampling rate of 20 frames/second. | hardware/simulator version and reset protocol | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Dataset/benchmark | On the nuScenes dataset, there are no publicly available pseudo-LiDAR works for us to make a direct comparison. | role, split, size and leakage | p. 5 (4 Experiments), p. 5 (4 Experiments), p. 7 (4 Experiments), p. 6 (4 Experiments) |
| Metric | One possible explanation is that pseudoLiDAR object detectors suffer from compounding errors introduced by inaccurate depth prediction, that in turn is known to overfit to training data and generalizes poorly to other ... | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Baseline/ablation | 4.2 Comparison to Existing Works We compare to previous state-of-the-art methods CenterNet [1] and FCOS3D [2]. | fair input/data/compute/action matching | p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 Conclusion - extractive body cue:** Some failure cases include the far ahead car in CAM FRONT, that was not detected.
- **p. 6 / 4 Experiments - extractive body cue:** To further demonstrate the advantages of fused inference, we calculate the metrics for boxes falling into the camera overlaps.
- **p. 8 / 5 Conclusion - extractive body cue:** Furthermore, the new detection head is input-agnostic, and including other modalities such as LiDAR/RADAR would enhance performance and robustness.
- **p. 6 / 4 Experiments - extractive body cue:** Our method is robust to the usage of NMS. ∗: CenterNet uses a customized backbone DLA [38]. ‡: this model is trained with depth weight ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 3D object detection from visual information is a long-standing challenge for low-cost autonomous driving systems.를 문제로 두고, We summarize our key contributions as follows: • We present a streamlined 3D object detection model from RGB images.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
