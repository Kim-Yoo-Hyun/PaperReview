# Self-Supervised Pretraining of 3D Features on any Point-Cloud

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2101.02691.
> PDF retrieval source: https://arxiv.org/pdf/2101.02691. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, point cloud, representation, self-supervised
- Official paper: https://arxiv.org/abs/2101.02691
- Full-text retrieval: https://arxiv.org/pdf/2101.02691
- Code/Project: https://github.com/facebookresearch/DepthContrast
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This cumbersome annotation process results in a lack of large annotated 3D datasets.를 문제로 두고, Our contributions can be summarized as follows: • We show that single view 3D depth scans can be used to learn powerful feature representations using selfsupervised learning. • We show that joint ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Pretraining on large labeled datasets is a prerequisite to achieve good performance in many computer vision tasks like 2D object recognition, video classification etc.
- **p. 1 / Abstract - extractive body cue:** However, pretraining is not widely used for 3D recognition tasks where state-of-the-art methods train models from scratch.
- **p. 1 / Abstract - extractive body cue:** A primary reason is the lack of large annotated datasets because 3D data is both difficult to acquire and time consuming to label.
- **p. 1 / Abstract - extractive body cue:** We present a simple self-supervised pretraining method that can work with any 3D data - single or multiview, indoor or outdoor, acquired by varied sensors, ...
- **p. 1 / Abstract - extractive body cue:** We pretrain standard point cloud and voxel based model architectures, and show that joint pretraining further improves performance.
- **p. 1 / 1. Introduction - extractive body cue:** This cumbersome annotation process results in a lack of large annotated 3D datasets.
- **p. 1 / 1. Introduction - extractive body cue:** In 3D computer vision, single-view depth scans are easy to acquire while reconstructed 3D scenes and annotations are difficult to obtain.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We show that single view 3D depth scans can be used to learn powerful feature representations using ...
- **p. 2 / 3. Approach - extractive body cue:** Our method, illustrated in Fig 2, is based on the instance discrimination framework of Wu et al.
- **p. 3 / 3.1. Instance Discrimination - extractive body cue:** Our method uses 3D data where X can be represented by point coordinates or voxels1.
- **p. 3 / 3.1. Instance Discrimination - extractive body cue:** Our method does not rely on any specific ordering of the points. use the method of He et al.
- **p. 4 / 3.4. Data Augmentation for 3D - extractive body cue:** Data augmentation is as an essential component of our framework.
- **p. 3 / 3.2. Extension to Multiple 3D Input Formats - extractive body cue:** (2) When the input formats a, b are identical, this objective reduces to the within format loss of Eq 1, and when a̸ = b ...
- **p. 4 / 3.3. Model Architecture - extractive body cue:** We use PointNet++ [67] as the backbone network which takes as input the XYZ coordinates of the 3D data.
- **p. 3 / 3. Approach - extractive body cue:** We use format-specific encoders to get spatial features which are pooled and projected to obtain global features v.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Inspired by the random crop in 2D images [92], we define a random cuboid augmentation that extracts random cuboids from the input point cloud. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.4. Data Augmentation for 3D), p. 3 (3.1. Instance Discrimination) |
| State/latent | Inspired, random, crop, images, define, cuboid, augmentation, extracts, cuboids, input, point, cloud | geometry, map, object/relationship state | p. 4 (3.4. Data Augmentation for 3D), p. 3 (3.1. Instance Discrimination), p. 3 (3. Approach) |
| Output/action | Our method, by design, makes minimal assumptions about the input X, i.e., it is an unprocessed single-view depth map. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Instance Discrimination), p. 3 (3. Approach), p. 2 (3. Approach) |
| Objective/outcome | Extending Eq 1, we can minimize a single objective that performs instance discrimination within and across input formats a, b: lab i = -log exp(va⊤ i,1 vb i,2/τ) exp(va⊤ i,1 vb i,2/τ) ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.2. Extension to Multiple 3D Input Formats), p. 3 (3.2. Extension to Multiple 3D Input Formats), p. 4 (3.5. Implementation Details) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We show that single view 3D depth scans can be used to learn powerful feature representations using ...
- **p. 2 / 3. Approach - extractive body cue:** Our method, illustrated in Fig 2, is based on the instance discrimination framework of Wu et al.
- **p. 3 / 3.1. Instance Discrimination - extractive body cue:** Our method uses 3D data where X can be represented by point coordinates or voxels1.
- **p. 3 / 3.1. Instance Discrimination - extractive body cue:** Our method does not rely on any specific ordering of the points. use the method of He et al.
- **p. 4 / 3.4. Data Augmentation for 3D - extractive body cue:** Data augmentation is as an essential component of our framework.
- **p. 5 / 4.2. Pretraining with Point Input Format - extractive body cue:** DepthContrast outperforms training from scratch on all the four datasets, and improves performance by 12.1% mAP on the small S3DIS dataset that has only 200 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Label-efficiency of our self-supervised pretraining. We finetune detection models from scratch or using our pretraining as initialization. Our pretraining which uses unlabeled single-view ...
- **p. 6 / 4.2. Pretraining with Point Input Format - extractive body cue:** DepthContrast's performance improves significantly when using both large data and large models.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4.2. Pretraining with Point Input Format), p. 1 (Figure/Table caption) |
| Embodiment/environment | We use diverse downstream datasets - full scenes/object centric; using different 3D sensors; single/multi-view; real/synthetic; indoor/outdoor. | hardware/simulator version and reset protocol | p. 5 (4.1. Transfer Datasets and Tasks), p. 5 (4. Experiments) |
| Dataset/benchmark | We evaluate DepthContrast pretraining by transfer learning, i.e., fine-tuning on downstream tasks and datasets. | role, split, size and leakage | p. 5 (4.1. Transfer Datasets and Tasks), p. 5 (4. Experiments), p. 4 (4. Experiments), p. 7 (4.2. Pretraining with Point Input Format) |
| Metric | We use the implementation of [67] for finetuning and report the detection performance using the mean Average Precision at IoU=0.25 (AP25) metric. | definition, denominator, direction and uncertainty | p. 5 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format), p. 7 (4.3. Pretraining with Multiple Input Formats) |
| Baseline/ablation | Table 3: Transfer using state-of-the-art detection frameworks. We use our pretrained model (PointNet++ 3× on Redwood-vid +ScanNet-vid) and transfer it using two state-of-the-art detection frameworks - H3DNet [118] and VoteNet [67]. Our ... | fair input/data/compute/action matching | p. 5 (Figure/Table caption), p. 5 (4.2. Pretraining with Point Input Format), p. 6 (4.2. Pretraining with Point Input Format) |

## Explicit Limitations and Failure Boundary

- **p. 6 / 4.2. Pretraining with Point Input Format - extractive body cue:** More importantly, the Redwood-vid dataset does not contain camera extrinsic parameters and thus cannot be registered to get a multi-view dataset which is a necessity ...
- **p. 8 / 6. Conclusion - extractive body cue:** We hope DepthContrast helps future work in 3D self-supervised learning.
- **p. 5 / 4.2. Pretraining with Point Input Format - extractive body cue:** We observe overfitting on the small datasets like S3DIS where increasing the model capacity does not improve performance.
- **p. 7 / 4.3. Pretraining with Multiple Input Formats - extractive body cue:** For the voxel models, this pretraining does not improve consistently over training from scratch, which is in line with observations from recent work [109].
- **p. 8 / 5.2. Impact of Single-view or Multi-view 3D Data - extractive body cue:** This is not surprising given that our objective does not rely on multi-view information.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This cumbersome annotation process results in a lack of large annotated 3D datasets.를 문제로 두고, Our contributions can be summarized as follows: • We show that single view 3D depth scans can be used to learn powerful feature representations using selfsupervised learning. • We show that joint ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.2. Extension to Multiple 3D Input Formats), p. 4 (3.3. Model Architecture), p. 3 (3. Approach), p. 4 (3.3. Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
