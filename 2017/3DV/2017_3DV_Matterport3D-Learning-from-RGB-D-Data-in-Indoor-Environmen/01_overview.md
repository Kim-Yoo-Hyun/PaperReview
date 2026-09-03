# Matterport3D: Learning from RGB-D Data in Indoor Environments

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1709.06158.
> PDF retrieval source: https://arxiv.org/pdf/1709.06158. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2017 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Dataset, RGB-D, Navigation
- Official paper: https://arxiv.org/abs/1709.06158
- Full-text retrieval: https://arxiv.org/pdf/1709.06158
- Code/Project: https://niessner.github.io/Matterport/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Although there has been impressive research progress on this topic, a significant limitation is the availability suitable RGB-D datasets from which models can be trained.를 문제로 두고, In this paper, we introduce Matterport3D, a large-scale RGB-D dataset containing 10,800 panoramic views from 194,400 RGB-D images of 90 building-scale scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Access to large, diverse RGB-D datasets is critical for training RGB-D scene understanding algorithms.
- **p. 1 / Abstract - extractive body cue:** However, existing datasets still cover only a limited number of views or a restricted scale of spaces.
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Matterport3D, a large-scale RGB-D dataset containing 10,800 panoramic views from 194,400 RGB-D images of 90 building-scale scenes.
- **p. 1 / Abstract - extractive body cue:** Annotations are provided with surface reconstructions, camera poses, and 2D and 3D semantic segmentations.
- **p. 1 / Abstract - extractive body cue:** The precise global alignment and comprehensive, diverse panoramic set of views over entire buildings enable a variety of supervised and self-supervised computer vision tasks, including ...
- **p. 1 / 1. Introduction - extractive body cue:** Although there has been impressive research progress on this topic, a significant limitation is the availability suitable RGB-D datasets from which models can be trained.
- **p. 1 / 1. Introduction - extractive body cue:** Unfortunately, current RGB-D datasets have small numbers of images [33], limited scene coverage [17], limited viewpoints [35], and/or motion blurred imagery.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Matterport3D, a large-scale RGB-D dataset containing 10,800 panoramic views from 194,400 RGB-D images of 90 building-scale scenes.
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** Providing scans of homes in their entirety enables opportunities for learning about long-range context, which is critical for holistic scene understanding and autonomous navigation.
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** This multiplicity and diversity of views enables opportunities for learning to predict view-dependent surface properties, such as material reflectance [4, 26], and for learning to ...
- **p. 2 / 1. Introduction - extractive body cue:** The surface normals estimated from highquality depths in diverse scenes allows training models for normal estimation from color images that outperform previous ones.
- **p. 2 / 1. Introduction - extractive body cue:** The precise global alignment over building scale allows training for state-of-the-art keypoint descriptors that can robustly match keypoints from drastically varying camera views.
- **p. 6 / 4.3. Surface Normal Estimation - extractive body cue:** The model is a fully convolutional neural network consisting of an encoder, which shares the same architecture as VGG-16 from the beginning till the first ...
- **p. 8 / 4.5. Semantic Voxel Labeling - extractive body cue:** We use 20 object class labels, and a network following the architecture of ScanNet [7], and training with 52,355 subvolume samples (418,840 augmented samples).
- **p. 7 / 4.3. Surface Normal Estimation - extractive body cue:** We train models by first pretraining on synthetic data and then finetuning on each dataset; i.e., NYUv2 and Matterport3D, respectively.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | More specifically, we train a convolutional neural network (ResNet-50 [18]) to map an input image patch to a 512 dimensional descriptor. | standardized observation, action, task state와 evaluation split | p. 5 (4.1. Keypoint Matching), p. 4 (3.3. Properties of the Dataset) |
| State/latent | More, specifically, train, convolutional, neural, network, ResNet-50, input, image, patch, dimensional, descriptor | benchmark state/goal와 method decision | p. 5 (4.1. Keypoint Matching), p. 4 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching) |
| Output/action | Most RGB-D image datasets have been captured mostly with hand-held video cameras and thus suffer from motion blur and other artifacts typical of real-time scanning; e.g., pose errors, color-to-depth misalignments, and often ... | policy/controller trajectory 또는 measured result | p. 4 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching), p. 8 (4.4. Region-Type Classification) |
| Objective/outcome | Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we subjectively estimate that the average registration error between corresponding surface points is 1cm or ... | success metric, robustness, generalization과 reproducibility | p. 3 (3.3. Properties of the Dataset), p. 5 (4.1. Keypoint Matching), p. 6 (4.2. View Overlap Prediction) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Matterport3D, a large-scale RGB-D dataset containing 10,800 panoramic views from 194,400 RGB-D images of 90 building-scale scenes.
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** Providing scans of homes in their entirety enables opportunities for learning about long-range context, which is critical for holistic scene understanding and autonomous navigation.
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** This multiplicity and diversity of views enables opportunities for learning to predict view-dependent surface properties, such as material reflectance [4, 26], and for learning to ...
- **p. 2 / 1. Introduction - extractive body cue:** The surface normals estimated from highquality depths in diverse scenes allows training models for normal estimation from color images that outperform previous ones.
- **p. 2 / 1. Introduction - extractive body cue:** The precise global alignment over building scale allows training for state-of-the-art keypoint descriptors that can robustly match keypoints from drastically varying camera views.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5: Region-type classification results. Each entry lists the prediction accuracy (percentage correct). By comparing the accuracy between [single] and [pano] we can see an ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1: Keypoint matching results. Error (%) at 95% re- call on ground truth correspondences from the SUN3D test- ing scenes. We see an improvement ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2: View overlap prediction results. Results on SUN3D and Matterport3D dataset measured by normalized discounted cumulative gain. From the comparison we can clearly see ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Embodiment/environment | This paper introduces a new RGB-D dataset of buildingscale scenes, and describes a set of scene understanding tasks that can be trained and tested from it. | hardware/simulator version and reset protocol | p. 2 (3. The Matterport3D Dataset), p. 4 (3.3. Properties of the Dataset) |
| Dataset/benchmark | This comprehensive sampling of viewpoint space provides new opportunities for learning about scenes as seen from arbitrary viewpoints that may be encountered by robots or wearable sensors as they navigate through them ... | role, split, size and leakage | p. 2 (3. The Matterport3D Dataset), p. 4 (3.3. Properties of the Dataset), p. 4 (3.3. Properties of the Dataset), p. 2 (3.1. Data Acquisition Process) |
| Metric | Table 1: Keypoint matching results. Error (%) at 95% re- call on ground truth correspondences from the SUN3D test- ing scenes. We see an improvement in performance from pretraining on Matterport3D. | definition, denominator, direction and uncertainty | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption) |
| Baseline/ablation | Figure 9: Example training correspondences (left) and im- age patches (right) extracted from Matterport3D. Triplets of matching patches (first and second columns) and non- matching patches (third column) are used to train ... | fair input/data/compute/action matching | p. 5 (Figure/Table caption), p. 6 (Figure/Table caption), p. 2 (3. The Matterport3D Dataset) |

## Explicit Limitations and Failure Boundary

- **p. 3 / 3.3. Properties of the Dataset - extractive body cue:** Although we do not have ground-truth camera poses for the dataset and so cannot measure errors objectively, we subjectively estimate that the average registration error ...
- **p. 4 / 3.3. Properties of the Dataset - extractive body cue:** Please note the accuracy of the global alignment (no ghosting) and the relatively low noise in surface normals, even without advanced depth-fusion techniques.

## Why Read It

Robotics-enabling 3D perception의 benchmark 문제를 이해하기 위해 읽는다. 본문은 Although there has been impressive research progress on this topic, a significant limitation is the availability suitable RGB-D datasets from which models can be trained.를 문제로 두고, In this paper, we introduce Matterport3D, a large-scale RGB-D dataset containing 10,800 panoramic views from 194,400 RGB-D images of 90 building-scale scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (4.3. Surface Normal Estimation), p. 8 (4.5. Semantic Voxel Labeling), p. 7 (4.3. Surface Normal Estimation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
