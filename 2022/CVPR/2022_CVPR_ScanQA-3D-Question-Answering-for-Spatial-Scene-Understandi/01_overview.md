# ScanQA: 3D Question Answering for Spatial Scene Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2112.10482.
> PDF retrieval source: https://arxiv.org/pdf/2112.10482. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Vision-Language, grounding, 3D QA
- Official paper: https://arxiv.org/abs/2112.10482
- Full-text retrieval: https://arxiv.org/pdf/2112.10482
- Code/Project: https://github.com/ATR-DBI/ScanQA
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 For example, 2D images lack an accurate sense of the relative directions and distances in the 3D scenes, i.e., the stereoscopic attribute-perception problem.를 문제로 두고, We introduce the new task of question answering for 3D modeling.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We propose a new 3D spatial understanding task for 3D question answering (3D-QA).
- **p. 1 / Abstract - extractive body cue:** In the 3D-QA task, models receive visual information from the entire 3D scene of a rich RGB-D indoor scan and answer given textual questions about ...
- **p. 1 / Abstract - extractive body cue:** Unlike the 2D-question answering of visual question answering, the conventional 2D-QA models suffer from problems with spatial understanding of object alignment and directions and fail ...
- **p. 1 / Abstract - extractive body cue:** We propose a baseline model for 3D-QA, called the ScanQA1, which learns a fused descriptor from 3D object proposals and encoded sentence embeddings.
- **p. 1 / Abstract - extractive body cue:** This learned descriptor correlates language expressions with the underlying geometric features of the 3D scan and facilitates the regression of 3D bounding boxes to determine ...
- **p. 1 / 1. Introduction - extractive body cue:** For example, 2D images lack an accurate sense of the relative directions and distances in the 3D scenes, i.e., the stereoscopic attribute-perception problem.
- **p. 1 / 1. Introduction - extractive body cue:** When multiple images are used in 2Dimage-based question answering models, such models often encounter difficulties in tracking and recognizing whether some objects are the same ...

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** We introduce the new task of question answering for 3D modeling.
- **p. 2 / 1. Introduction - extractive body cue:** We present the overview of the task in Fig.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose a 3D question answering (3DQA) task that uses 3D spatial information instead of 2D images to comprehend real-world information through ...
- **p. 4 / 4. ScanQA Model - extractive body cue:** We introduce the baseline model of ScanQA for the 3DQA task.
- **p. 5 / 4. ScanQA Model - extractive body cue:** This layer consists of object localization, object classification, and answer classification modules.
- **p. 4 / 4. ScanQA Model - extractive body cue:** Inspired by the architecture of deep modular co-attention networks of MCAN [51], often used for VQA, we use transformer blocks [44] to represent the relationships ...
- **p. 5 / 4. ScanQA Model - extractive body cue:** In addition, we use transformer decoder layers to represent the features of object proposals related to the question words by using the final output of ...
- **p. 5 / 4. ScanQA Model - extractive body cue:** Given a point cloud and RGB frame sequence that capture indoor scenes, the QA model outputs a corresponding answer by fusing 3D and language information ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The 3D-QA is formalized as follows: given inputs of the point cloud p ∈P and question q ∈Q about the 3D scene, the 3D-QA model aims to output ˆa that semantically matches ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (4. ScanQA Model), p. 4 (4. ScanQA Model) |
| State/latent | D-QA, formalized, follows, given, inputs, point, cloud, question, about, scene, model, aims | geometry, map, object/relationship state | p. 4 (4. ScanQA Model), p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model) |
| Output/action | We project a series of output states from the LSTM using a nonlinear layer with GELUs [21] activation to obtain the contextualized word representation Q′ ∈Rnq×d, where d is the hidden size ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model), p. 1 (1. Introduction) |
| Objective/outcome | To consider multiple answers, we compute final scores with the binary cross-entropy (BCE) loss function to train the module. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4. ScanQA Model), p. 5 (4. ScanQA Model) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** We introduce the new task of question answering for 3D modeling.
- **p. 2 / 1. Introduction - extractive body cue:** We present the overview of the task in Fig.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose a 3D question answering (3DQA) task that uses 3D spatial information instead of 2D images to comprehend real-world information through ...
- **p. 4 / 4. ScanQA Model - extractive body cue:** We introduce the baseline model of ScanQA for the 3DQA task.
- **p. 5 / 4. ScanQA Model - extractive body cue:** This layer consists of object localization, object classification, and answer classification modules.
- **p. 7 / 5.2. Quantitative Analysis - extractive body cue:** The results indicated that our ScanQA method significantly outperformed all baselines across all data splits over all evaluation metrics.
- **p. 7 / 5.2. Quantitative Analysis - extractive body cue:** Interestingly, VoteNet+MCAN, ScanRefer+MCAN (end-to-end), and ScanQA significantly outperformed ScanRefer+MCAN (pipeline), which detects target objects related to a question using a pretrained ScanRefer and then applies ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results. Predicted answers are described below each figure. Predicted boxes are marked blue and the ground truth is marked green. We show ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis) |
| Embodiment/environment | However, as the object IDs for the test set of ScanRefer are not publicly available, we further split the validation set of ScanRefer into two-holds as the validation set and test set ... | hardware/simulator version and reset protocol | p. 4 (3.3. Dataset Statistics), p. 3 (3.2. Question-Answer Collection) |
| Dataset/benchmark | Considering that our dataset contains not only question-answer pairs but also 3D object localization annotations, we assume that this is the largest dataset to specify the nature of objects in 3D scenes ... | role, split, size and leakage | p. 4 (3.3. Dataset Statistics), p. 3 (3.2. Question-Answer Collection), p. 3 (3.3. Dataset Statistics), p. 4 (3.3. Dataset Statistics) |
| Metric | Table 7. Feature ablation results on ScanQA (multiple) calization scores with the ground true boxes and consider positive predictions for the box with the highest IoU.) We observed that RGB values were ... | definition, denominator, direction and uncertainty | p. 13 (Figure/Table caption), p. 8 (5.4. Qualitative Analysis), p. 1 (Figure/Table caption) |
| Baseline/ablation | We compared our ScanQA model with competitive baselines VoteNet+MCAN, ScanRefer+MCAN (pipeline), and ScanRefer+MCAN (end-to-end). | fair input/data/compute/action matching | p. 7 (5.2. Quantitative Analysis), p. 7 (5.2. Quantitative Analysis), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 6 / Figure/Table caption - extractive body cue:** Table 5. Feature ablation results ground-truth answers. We also included sentence evalua- tion metrics frequently used for image captioning models because some of the questions ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 For example, 2D images lack an accurate sense of the relative directions and distances in the 3D scenes, i.e., the stereoscopic attribute-perception problem.를 문제로 두고, We introduce the new task of question answering for 3D modeling.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (4. ScanQA Model), p. 5 (4. ScanQA Model) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
