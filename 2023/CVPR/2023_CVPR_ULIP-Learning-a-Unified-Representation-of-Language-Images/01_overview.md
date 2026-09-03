# ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2212.05171.
> PDF retrieval source: https://arxiv.org/pdf/2212.05171. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, Vision-Language Model, point cloud, alignment
- Official paper: https://arxiv.org/abs/2212.05171
- Full-text retrieval: https://arxiv.org/pdf/2212.05171
- Code/Project: https://github.com/salesforce/ULIP
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To circumvent the lack of triplet data, we take advantage of a vision-language model pretrained on massive imagetext pairs, and align the feature space of a 3D point cloud encoder to the ...를 문제로 두고, We present the standard 3D classification performances of our baselines and our methods on ScanObjectNN in Table 7.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The recognition capabilities of current state-of-the-art 3D models are limited by datasets with a small number of annotated data and a pre-defined set of categories.
- **p. 1 / Abstract - extractive body cue:** In its 2D counterpart, recent advances have shown that similar problems can be significantly alleviated by employing knowledge from other modalities, such as language.
- **p. 1 / Abstract - extractive body cue:** Inspired by this, leveraging multimodal information for 3D modality could be promising to improve 3D understanding under the restricted data regime, but this line of ...
- **p. 1 / Abstract - extractive body cue:** Therefore, we introduce ULIP to learn a unified representation of images, texts, and 3D point clouds by pre-training with object triplets from the three modalities.
- **p. 1 / Abstract - extractive body cue:** To overcome the shortage of training triplets, ULIP leverages a pre-trained vision-language model that has already learned a common visual and textual space by training ...
- **p. 2 / 1. Introduction - extractive body cue:** To circumvent the lack of triplet data, we take advantage of a vision-language model pretrained on massive imagetext pairs, and align the feature space of ...
- **p. 2 / 1. Introduction - extractive body cue:** Our framework uses CLIP as the vision and language model because of its excellent generalization performance.

## Core Idea

- **p. 5 / 4.4. Standard 3D Classification - extractive body cue:** We present the standard 3D classification performances of our baselines and our methods on ScanObjectNN in Table 7.
- **p. 2 / 1. Introduction - extractive body cue:** An illustration of our framework is shown in Figure 1.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose Learning a Unified Representation of Language, Images, and Point Clouds (ULIP).
- **p. 5 / 4.4. Standard 3D Classification - extractive body cue:** Specifically, our framework improves PointBERT and PointMLP significantly by around 3%.
- **p. 6 / Model - extractive body cue:** It conducts zero-shot 3D classification by first converting a 3D point cloud into 6 orthogonal depth maps, then using CLIP's image encoder to get ensembled ...
- **p. 3 / 3.1. Creating Training Triplets for ULIP - extractive body cue:** Then a 3D encoder takes the augmented point cloud Pi as input and outputs its 3D representation hP i via
- **p. 5 / 4.3. Implementation Details - extractive body cue:** We use our pre-trained models as they are when performing zero-shot classification.
- **p. 5 / 4.3. Implementation Details - extractive body cue:** On ModelNet40, we use the learning rate as 0.00015 and fine-tune our model for 200 epochs, with the batch size as 24 for PointNet++.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Then a 3D encoder takes the augmented point cloud Pi as input and outputs its 3D representation hP i via | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Creating Training Triplets for ULIP), p. 3 (3.1. Creating Training Triplets for ULIP) |
| State/latent | Then, encoder, takes, augmented, point, cloud, input, outputs, representation, During, iteration, pre-training | geometry, map, object/relationship state | p. 3 (3.1. Creating Training Triplets for ULIP), p. 3 (3.1. Creating Training Triplets for ULIP), p. 2 (1. Introduction) |
| Output/action | During each iteration of pre-training, we randomly select one image or depth map from each CAD model's 60 renderred candidates as Ii and take Ii as input of the image encoder fI(·) ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Creating Training Triplets for ULIP), p. 2 (1. Introduction), p. 6 (Model) |
| Objective/outcome | We use 64 as the batch size, 10-3 as the learning rate, and AdamW as the optimizer. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4.3. Implementation Details), p. 5 (4.3. Implementation Details) |

## Main Claims and Actual Contribution

- **p. 5 / 4.4. Standard 3D Classification - extractive body cue:** We present the standard 3D classification performances of our baselines and our methods on ScanObjectNN in Table 7.
- **p. 2 / 1. Introduction - extractive body cue:** An illustration of our framework is shown in Figure 1.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose Learning a Unified Representation of Language, Images, and Point Clouds (ULIP).
- **p. 5 / 4.4. Standard 3D Classification - extractive body cue:** Specifically, our framework improves PointBERT and PointMLP significantly by around 3%.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Standard 3D classification results on ModelNet40. ULIP significantly improves our baselines. Our best number achieves new SOTA. * means a voting technique is ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Zero-shot 3D classification on ScanObjectNN. ULIP- based methods outperform the previous SOTA (PointCLIP) by a very large margin (at least 29.2% on top-1 ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. 3D classification results on ScanObjectNN. ULIP signifi- cantly improves our baselines. Our best result outperforms SOTA largely by around 3% on Overall Acc. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 3. Data efficiency comparison. The X axis indicates the percentage of samples used for training and Y axis denotes the overall accuracy. Both PointMLP ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Embodiment/environment | ModelNet40 is a synthetic dataset of 3D CAD models. | hardware/simulator version and reset protocol | p. 4 (4.2. Downstream Datasets), p. 4 (4.2. Downstream Datasets) |
| Dataset/benchmark | On ScanObjectNN, we use the learning rate of 0.03 and finetune for 350 epochs with batch size 32 for PointMLP. | role, split, size and leakage | p. 4 (4.2. Downstream Datasets), p. 4 (4.2. Downstream Datasets), p. 5 (4.3. Implementation Details), p. 5 (4.3. Implementation Details) |
| Metric | Table 5. Zero-shot 3D classification on ScanObjectNN. ULIP- based methods outperform the previous SOTA (PointCLIP) by a very large margin (at least 29.2% on top-1 accuracy). Table 3 for ScanObjectNN and ModelNet40 ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 4 (4. Experiments) |
| Baseline/ablation | Table 1. 3D classification results on ScanObjectNN. ULIP signifi- cantly improves our baselines. Our best result outperforms SOTA largely by around 3% on Overall Acc. †indicates a model uses 2K sampled points ... | fair input/data/compute/action matching | p. 5 (Figure/Table caption), p. 7 (Figure/Table caption), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.3. Implementation Details - extractive body cue:** During pre-training, we utilize an advanced version of CLIP, namely SLIP [32], that shows superior performance as our image-text encoders.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To circumvent the lack of triplet data, we take advantage of a vision-language model pretrained on massive imagetext pairs, and align the feature space of a 3D point cloud encoder to the ...를 문제로 두고, We present the standard 3D classification performances of our baselines and our methods on ScanObjectNN in Table 7.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (Model), p. 3 (3.1. Creating Training Triplets for ULIP), p. 5 (4.3. Implementation Details), p. 5 (4.3. Implementation Details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
