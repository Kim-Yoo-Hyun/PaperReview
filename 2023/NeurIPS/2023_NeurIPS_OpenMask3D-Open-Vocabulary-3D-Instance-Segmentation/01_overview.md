# OpenMask3D: Open-Vocabulary 3D Instance Segmentation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2306.13631.
> PDF retrieval source: https://arxiv.org/pdf/2306.13631. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: open-vocabulary, 3D segmentation, CLIP
- Official paper: https://arxiv.org/abs/2306.13631
- Full-text retrieval: https://arxiv.org/pdf/2306.13631
- Code/Project: https://openmask3d.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Hence, the second key problem with closed-vocabulary approaches is their inherent limitation to recognize only object classes that are predefined at training time.를 문제로 두고, Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given text-query are identified. • We propose OpenMask3D, which ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce the task of open-vocabulary 3D instance segmentation.
- **p. 1 / Abstract - extractive body cue:** Current approaches for 3D instance segmentation can typically only recognize object categories from a pre-defined closed set of classes that are annotated in the training ...
- **p. 1 / Abstract - extractive body cue:** This results in important limitations for real-world applications where one might need to perform tasks guided by novel, open-vocabulary queries related to a wide variety ...
- **p. 1 / Abstract - extractive body cue:** Recently, open-vocabulary 3D scene understanding methods have emerged to address this problem by learning queryable features for each point in the scene.
- **p. 1 / Abstract - extractive body cue:** While such a representation can be directly employed to perform semantic segmentation, existing methods cannot separate multiple object instances.
- **p. 2 / 1 Introduction - extractive body cue:** Hence, the second key problem with closed-vocabulary approaches is their inherent limitation to recognize only object classes that are predefined at training time.
- **p. 2 / 1 Introduction - extractive body cue:** In an attempt to address and overcome the limitations of a closed-vocabulary setting, there has been a growing interest in open-vocabulary approaches.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given text-query ...
- **p. 2 / 1 Introduction - extractive body cue:** Our approach is intrinsically different from the existing 3D open-vocabulary scene understanding approaches [24, 32, 52] as we propose an instance-based feature computation approach instead ...
- **p. 4 / 3 Method - extractive body cue:** Our pipeline consists of four subsequent steps: 1⃝Our approach takes as input posed RGB-D images of a 3D indoor scene along with its reconstructed point ...
- **p. 3 / 3 Method - extractive body cue:** The key novelty of our method is that it follows an instance-mask oriented approach, contrary to existing 3D open-vocabulary scene understanding models which typically compute ...
- **p. 4 / 3 Method - extractive body cue:** 3, the mask-feature computation module consists of several steps.
- **p. 4 / 3 Method - extractive body cue:** The architecture consists of a sparse convolutional backbone based on the MinkowskiUNet [9], and a transformer decoder.
- **p. 7 / Model - extractive body cue:** In order to compute image features on the mask-crops, we use CLIP [55] visual encoder from the ViT-L/14 model pre-trained at a 336 pixel resolution, ...
- **p. 8 / Model - extractive body cue:** First, we analyze the performance of our model when we use class-agnostic masks from a mask-predictor trained on the 20 original ScanNet classes [10], and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our pipeline takes as input a collection of posed RGB-D images captured in an indoor scene, and the reconstructed point cloud representation of the scene. | camera/depth stream, pose, map와 language goal | p. 3 (3 Method), p. 6 (3 Method) |
| State/latent | pipeline, takes, input, collection, posed, RGB-D, images, captured, indoor, scene, reconstructed, point | robot pose, free-space/semantic map와 local goal | p. 3 (3 Method), p. 6 (3 Method), p. 3 (3 Method) |
| Output/action | 3.2.3 CLIP feature extraction and mask-feature aggregation For each instance mask, we collect k ⋅L images by selecting top-k views and obtaining L multi-level crops as described in Sec. | collision-free trajectory 또는 velocity command | p. 6 (3 Method), p. 3 (3 Method), p. 4 (3 Method) |
| Objective/outcome | For this experiment, we perform Hungarian matching between the predicted masks and oracle masks discarding all class-losses, and we only match based on the masks. | goal reach, safety, localization error와 replanning latency | p. 9 (Model) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given text-query ...
- **p. 2 / 1 Introduction - extractive body cue:** Our approach is intrinsically different from the existing 3D open-vocabulary scene understanding approaches [24, 32, 52] as we propose an instance-based feature computation approach instead ...
- **p. 4 / 3 Method - extractive body cue:** Our pipeline consists of four subsequent steps: 1⃝Our approach takes as input posed RGB-D images of a 3D indoor scene along with its reconstructed point ...
- **p. 3 / 3 Method - extractive body cue:** The key novelty of our method is that it follows an instance-mask oriented approach, contrary to existing 3D open-vocabulary scene understanding models which typically compute ...
- **p. 4 / 3 Method - extractive body cue:** 3, the mask-feature computation module consists of several steps.
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an overlap range, and AP evaluated at 50% ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: 3D instance segmentation results on the Replica [61] dataset. To assess how well our model generalizes to other datasets, we use instance masks ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 18 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | To assess the generalization capability of our method, we further experiment with the Replica [61] dataset, and evaluate on the office0, office1, office2, office3, office4, room0, room1, room2 scenes. | hardware/simulator version and reset protocol | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Dataset/benchmark | To assess the generalization capability of our method, we further experiment with the Replica [61] dataset, and evaluate on the office0, office1, office2, office3, office4, room0, room1, room2 scenes. | role, split, size and leakage | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Metric | Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized in the image) are concentrated in a small ... | definition, denominator, direction and uncertainty | p. 18 (Figure/Table caption), p. 6 (4 Experiments), p. 19 (Figure/Table caption) |
| Baseline/ablation | Table 5: 3D instance segmentation results on the ScanNet200 validation set, using oracle masks. We use ground truth instance masks for computing the per-mask features. We also report results from the fully- ... | fair input/data/compute/action matching | p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 18 / Figure/Table caption - extractive body cue:** Figure 9: Output of SAM, using only 5 randomly sampled points (visualized as green dots) of the projected 3D mask as input. A.2.4 Why do ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 3D instance segmentation results on the ScanNet200 validation set. Metrics are respectively: AP averaged over an overlap range, and AP evaluated at 50% ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 10: Output of SAM, using only 5 randomly sampled points of the mask as input. Here the sampled points (the green points visualized in ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 7: Difference between the bounding boxes obtained by tightly cropping around the projected points from the 3D instance mask (left), and the bounding box ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Hence, the second key problem with closed-vocabulary approaches is their inherent limitation to recognize only object classes that are predefined at training time.를 문제로 두고, Our contributions are three-fold: • We introduce the open-vocabulary 3D instance segmentation task in which the object instances that are similar to a given text-query are identified. • We propose OpenMask3D, which ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 4 (3 Method), p. 7 (Model), p. 4 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
