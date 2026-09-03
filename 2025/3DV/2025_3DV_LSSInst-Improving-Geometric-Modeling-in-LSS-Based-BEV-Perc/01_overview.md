# LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=MaN2x3O2Rk&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: sensor fusion, LiDAR, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=MaN2x3O2Rk&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, unlike LiDAR sensors that provide direct and accurate depth information, detecting objects solely based on camera sensor images poses a significant challenge.를 문제로 두고, Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with instance representations; ii) We proposed the instance ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** With the attention gained by camera-only 3D object detection in autonomous driving, methods based on Bird-EyeView (BEV) representation especially derived from the forward view transformation ...
- **p. 1 / Abstract - extractive body cue:** The BEV representation formulated by the frustum based on depth distribution prediction is ideal for learning the road structure and scene layout from multi-view images.
- **p. 1 / Abstract - extractive body cue:** However, to retain computational efficiency, the compressed BEV representation such as in resolution and axis is inevitably weak in retaining the individual geometric details, undermining ...
- **p. 1 / Abstract - extractive body cue:** With this in mind, to compensate for the missing details and utilize multi-view geometry constraints, we propose LSSInst, a two-stage object detector incorporating BEV and ...
- **p. 1 / Abstract - extractive body cue:** The proposed detector exploits fine-grained pixel-level features that can be flexibly integrated into existing LSS-based BEV networks.
- **p. 1 / 1. Introduction - extractive body cue:** However, unlike LiDAR sensors that provide direct and accurate depth information, detecting objects solely based on camera sensor images poses a significant challenge.
- **p. 2 / 1. Introduction - extractive body cue:** However, this collaboration also poses challenges, as the most straightforward solution of naively sharing the bounding box proposal is intuitively and experimentally failed 1.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with ...
- **p. 2 / 1. Introduction - extractive body cue:** With this in mind, we propose the instance adaptor module to establish semantic coherence between the scene and instances and an instance branch for detection.
- **p. 3 / 3. Methodology - extractive body cue:** The overview of our framework is shown in Fig.
- **p. 3 / 3. Methodology - extractive body cue:** In this work, we propose LSSInst, which looks back for the more geometry-aware and finegrained target feature extraction to bridge the adaptation between scene-level and ...
- **p. 5 / 3. Methodology - extractive body cue:** Then we introduce five separated linear projections {Ej l3}2 j=1 ∈R3×C, {Ej l2}2 j=1 ∈R2×C and Eg ∈RC×C for comprehensive encoding, of which the former ...
- **p. 4 / 3. Methodology - extractive body cue:** Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence ...
- **p. 4 / 3. Methodology - extractive body cue:** BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D image backbone network ...
- **p. 5 / 3. Methodology - extractive body cue:** Instance Adapter: Scene-to-instance adaptation For the sake of preserving a coherent and solid semantic consistency between BEV and instance representations, we propose the instance adapter ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | BEV Branch: Looking around for scene-level representation The multi-view sequential images with the previous T frames are first input into the 2D image backbone network for feature extraction. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3. Methodology), p. 4 (3. Methodology) |
| State/latent | BEV, Branch, Looking, around, scene-level, representation, multi-view, sequential, images, previous, frames, first | geometry, map, object/relationship state | p. 4 (3. Methodology), p. 4 (3. Methodology), p. 2 (1. Introduction) |
| Output/action | Backbone Multi-frame Multi-view Features Multi-view Images with Previous T Frames Depth Distribution Map BEV Feature BEV Temporal Encoder BEV Branch Temporally-shared View Transformation BEV Sequence Feature Extraction Net Voxel Pooling ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3. Methodology), p. 2 (1. Introduction), p. 3 (3. Methodology) |
| Objective/outcome | Lastly, the model makes the final prediction based on the updated output. briefly introduces the BEV branch. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3. Methodology), p. 4 (3. Methodology), p. 5 (3. Methodology) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with ...
- **p. 2 / 1. Introduction - extractive body cue:** With this in mind, we propose the instance adaptor module to establish semantic coherence between the scene and instances and an instance branch for detection.
- **p. 3 / 3. Methodology - extractive body cue:** The overview of our framework is shown in Fig.
- **p. 3 / 3. Methodology - extractive body cue:** In this work, we propose LSSInst, which looks back for the more geometry-aware and finegrained target feature extraction to bridge the adaptation between scene-level and ...
- **p. 5 / 3. Methodology - extractive body cue:** Then we introduce five separated linear projections {Ej l3}2 j=1 ∈R3×C, {Ej l2}2 j=1 ∈R2×C and Eg ∈RC×C for comprehensive encoding, of which the former ...
- **p. 6 / 4.3. Generalization Ability and Geometric-Wise - extractive body cue:** The table reveals that our LSSInst achieves notable improvements in mAP and NDS compared to standalone BEV detectors at a minor cost.
- **p. 6 / 4.2. Benchmark Results - extractive body cue:** On the test set, our LSSInst achieves an mAP of 54.6% and an NDS of 62.9% without any additional augmentation, outperforming all LSS-based methods.
- **p. 7 / 4.5. Multiplicate Queries Ablations - extractive body cue:** On the other hand, though the proposal queries from BEV alone can achieve overall good results, adding more queries 7

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.3. Generalization Ability and Geometric-Wise), p. 6 (4.2. Benchmark Results) |
| Embodiment/environment | Dataset We conducted extensive experiments on the nuScenes 3D detection benchmark [1], a large-scale dataset in the autonomous driving scene. | hardware/simulator version and reset protocol | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings) |
| Dataset/benchmark | Although we have verified the high performance of LSSInst on nuScenes [1], even the large-scale autonomous driving dataset inevitably contain disturbances in the extrinsics obtained when sensors collect data in huge quantities. | role, split, size and leakage | p. 6 (4.1. Experimental Settings), p. 6 (4.1. Experimental Settings), p. 7 (4.4. Noise Resistance for Practical Robustness), p. 7 (4.3. Generalization Ability and Geometric-Wise) |
| Metric | Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property (here we use * to denote this) by ... | definition, denominator, direction and uncertainty | p. 13 (Figure/Table caption), p. 7 (4.4. Noise Resistance for Practical Robustness), p. 7 (4.4. Noise Resistance for Practical Robustness) |
| Baseline/ablation | We compared our approach with LSS-based and two-stage state-of-the-art methods on the nuScenes val and test sets. | fair input/data/compute/action matching | p. 6 (4.2. Benchmark Results), p. 8 (4.5. Multiplicate Queries Ablations), p. 6 (4.2. Benchmark Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.5. Multiplicate Queries Ablations - extractive body cue:** We can observe that on the one hand, relying solely on the potential queries cannot play a major role, and even utilizing all 900 queries ...
- **p. 7 / 4.4. Noise Resistance for Practical Robustness - extractive body cue:** In actual autonomous driving scenarios, the detector is required to be resistant to the disturbance noise caused by small measurement errors.
- **p. 8 / 4.5. Multiplicate Queries Ablations - extractive body cue:** The noise resistance results for robustness.
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 3. Comparison results of per-classes mAP on nuScenes val set. D.2.2 Verification for Translation Improvement The mA*E is designed to measure a property (here ...
- **p. 8 / 4.5. Multiplicate Queries Ablations - extractive body cue:** Method Noise mAP%↑Attenu.%↓NDS%↑Attenu.%↓ Baseline 0 35.74 - 46.84 - LSSInst 38.28 - 49.43 - Baseline 0.5% 35.38 1.01 46.44 0.85 LSSInst 38.01 0.71 49.19 0.49 ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, unlike LiDAR sensors that provide direct and accurate depth information, detecting objects solely based on camera sensor images poses a significant challenge.를 문제로 두고, Our main contributions can be concluded as follows: i) We proposed LSSInst, a two-stage framework that improves the geometric details in LSS-based BEV perception with instance representations; ii) We proposed the instance ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Methodology), p. 4 (3. Methodology), p. 3 (3. Methodology) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
