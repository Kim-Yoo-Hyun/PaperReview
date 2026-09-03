# OpenSeg: Scaling Open-Vocabulary Image Segmentation with Image-Level Labels

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2112.12143.
> PDF retrieval source: https://arxiv.org/pdf/2112.12143. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model, semantic, open-vocabulary, segmentation
- Official paper: https://arxiv.org/abs/2112.12143
- Full-text retrieval: https://arxiv.org/pdf/2112.12143
- Code/Project: https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/openseg
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Scaling Open-Vocabulary Image Segmentation with Image-Level Labels 3 However, the issue with this approach is in the scalability of training data.를 문제로 두고, We call our method OpenSeg, standing for open-vocabulary image segmentation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** Image segmentation is an important step to organize an image into a small number of regions in order to understand "what" and "where" are in ...
- **p. 2 / 1 Introduction - extractive body cue:** Each region represents a semantically meaningful entity, which can be a thing (e.g., a chair) or stuff(e.g., floor).
- **p. 2 / 1 Introduction - extractive body cue:** Language is a natural interface to describe what is in an image.
- **p. 2 / 1 Introduction - extractive body cue:** However, semantic segmentation algorithms often only learn with closed-set categories, and thus are unable to recognize concepts outside labeled datasets.
- **p. 2 / 1 Introduction - extractive body cue:** The segmentation model takes text queries as inputs and produces segmented regions accordingly.
- **p. 3 / 1 Introduction - extractive body cue:** Scaling Open-Vocabulary Image Segmentation with Image-Level Labels 3 However, the issue with this approach is in the scalability of training data.
- **p. 3 / 1 Introduction - extractive body cue:** We show that the model can generalize well to other datasets, reaching superior performances compared with prior works on segmentation proposals [3,33].

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** We call our method OpenSeg, standing for open-vocabulary image segmentation.
- **p. 3 / 1 Introduction - extractive body cue:** To evaluate our method, we measure performances on holdout image segmentation datasets.
- **p. 6 / 3 Method - extractive body cue:** 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction and a cross-attention ...
- **p. 6 / 3 Method - extractive body cue:** We use a cross-attention module taking inputs as FP E s and a randomly initialized queries q0 ∈RN×D to generate mask queries q ∈RN×D.
- **p. 7 / 3 Method - extractive body cue:** We follow MuST [17] and first train a teacher model on a segmentation dataset with only the segmentation loss LS.
- **p. 8 / 3 Method - extractive body cue:** 3.4 Inference Up to this point, we learn a vision model that predicts segmentation masks s ∈RN×H×W and corresponding features z ∈RN×D.
- **p. 7 / 3 Method - extractive body cue:** Then we annotate a large image-text dataset with pseudo segmentation labels using the teacher model.
- **p. 8 / 3 Method - extractive body cue:** Given an evaluation segmentation dataset, we encode its categories using the text encoder.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We argue that what is missing in these state-of-the-art open-vocabulary classification models are mid-level representations from visual groupings [48], which organize an image into a small set of segmentation masks. | camera/depth stream, pose, map와 language goal | p. 2 (1 Introduction), p. 6 (3 Method) |
| State/latent | argue, what, missing, state-of-the-art, open-vocabulary, classification, models, mid-level, representations, visual, groupings, organize | robot pose, free-space/semantic map와 local goal | p. 2 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method) |
| Output/action | We use a cross-attention module taking inputs as FP E s and a randomly initialized queries q0 ∈RN×D to generate mask queries q ∈RN×D. | collision-free trajectory 또는 velocity command | p. 6 (3 Method), p. 6 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | The grounding loss aims at maximizing the normalized score of a labeled image-caption pair ⟨Ib, Cb⟩over all images and all captions in a mini-batch. | goal reach, safety, localization error와 replanning latency | p. 7 (3 Method), p. 6 (3 Method), p. 7 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** We call our method OpenSeg, standing for open-vocabulary image segmentation.
- **p. 3 / 1 Introduction - extractive body cue:** To evaluate our method, we measure performances on holdout image segmentation datasets.
- **p. 6 / 3 Method - extractive body cue:** 3.1 Learning Segmentation Masks We design a model architecture which consists of a feature pyramid network (FPN) [32] for multi-scale feature extraction and a cross-attention ...
- **p. 11 / 4 Experiments - extractive body cue:** OpenSeg significantly outperforms pre-trained ALIGN [23]: OpenSeg trained on COCO outperforms ALIGN baseline on all of the benchmarks significantly.
- **p. 12 / 4 Experiments - extractive body cue:** This model significantly outperforms the strongest LSeg model with ViT-L backbone (+19.9 mIoU on PASCAL-20).
- **p. 12 / 4 Experiments - extractive body cue:** LSeg+ significantly outperforms LSeg (and also SPNet [49] and ZS3Net [6]) as it is trained on the larger dataset of COCO instead of PASCAL-20.
- **p. 11 / 4 Experiments - extractive body cue:** While adding proposals to ALIGN improves mIoU results.
- **p. 13 / 4 Experiments - extractive body cue:** 6.8 11.2 24.8 45.9 Incorporating proposals at inference time improves accuracy: We are curious about the importance of mask proposals in OpenSeg during inference.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Embodiment/environment | Training Datasets COCO: We use the panoptic segmentation [26] and caption [9] annotations in the 2017 splits which include 118k/5k train/val images. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 9 (4 Experiments) |
| Dataset/benchmark | Evaluation Datasets PASCAL Context: PASCAL Context [35] includes per-pixel segmentation annotations of object and stuffon 5k/5k train/val images from various indoor and outdoor senses. | role, split, size and leakage | p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 12 (4 Experiments) |
| Metric | 4.2 Predicting Masks Across Datasets We train the segmentation proposal model on COCO and evaluate on COCO and PC-59 with recalls at IoU 50%, 70%, and 90% as metrics. | definition, denominator, direction and uncertainty | p. 9 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments) |
| Baseline/ablation | Then we discuss the experimental results with our open-vocabulary baselines and state-of-the-art open-vocabulary and zero-shot methods. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Conclusion - extractive body cue:** We hope to encourage future works to learn a generalist segmentation model that can transfer across datasets using language as the interface.
- **p. 14 / 4 Experiments - extractive body cue:** The small performance differences across different ways of text filtering show OpenSeg is robust to the noise in the input words to some degree.
- **p. 10 / 4 Experiments - extractive body cue:** Notably, OpenSeg is trained on COCO which does not include underwater scenes.
- **p. 11 / 4 Experiments - extractive body cue:** We find that predictions in the mIoU and Grounding mIoU settings can look quite differently and sometimes mIoU does not correctly reflect the prediction quality ...
- **p. 20 / Figure/Table caption - extractive body cue:** Table 7. OpenSeg is robust to the batch size. We present performance of OpenSeg trained on COCO+Loc. Narr. and different batch sizes. Numbers inside the ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Scaling Open-Vocabulary Image Segmentation with Image-Level Labels 3 However, the issue with this approach is in the scalability of training data.를 문제로 두고, We call our method OpenSeg, standing for open-vocabulary image segmentation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 3 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 8 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
