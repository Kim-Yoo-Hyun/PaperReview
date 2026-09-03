# FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2402.04555.
> PDF retrieval source: https://arxiv.org/pdf/2402.04555. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Vision-Language Model, semantic
- Official paper: https://arxiv.org/abs/2402.04555
- Full-text retrieval: https://arxiv.org/pdf/2402.04555
- Code/Project: https://github.com/HKUST-Aerial-Robotics/FM-Fusion
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, the supervised object detectors are trained in specific data distribution and lack generalization ability.를 문제로 두고, Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Semantic mapping based on the supervised object detectors is sensitive to image distribution.
- **p. 1 / Abstract - extractive body cue:** In real-world environments, the object detection and segmentation performance can lead to a major drop, preventing the use of semantic mapping in a wider domain.
- **p. 1 / Abstract - extractive body cue:** On the other hand, the development of vision-language foundation models demonstrates a strong zero-shot transferability across data distribution.
- **p. 1 / Abstract - extractive body cue:** It provides an opportunity to construct generalizable instance-aware semantic maps.
- **p. 1 / Abstract - extractive body cue:** Hence, this work explores how to boost instance-aware semantic mapping from object detection generated from foundation models.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the supervised object detectors are trained in specific data distribution and lack generalization ability.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, these challenges have not been considered in traditional semantic mapping works.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address such challenges, we propose a probabilistic label fusion method following the Bayes filter algorithm.
- **p. 6 / 6 Method - extractive body cue:** Compared with Kimera using RAM-GroundedSAM, our method achieved +15.6 mAP50.
- **p. 6 / 6 Method - extractive body cue:** The rest of the ScanNet experiment focus on evaluating each module of our method through an ablation study.
- **p. 7 / 6 Method - extractive body cue:** As shown in Figure 10(b), our method detects the table correctly.
- **p. 6 / 6 Method - extractive body cue:** Our instance refinement module merges over-segmented instances caused by inconsistent instance masks at changed viewpoints.
- **p. 7 / 6 Method - extractive body cue:** We consider those limitations of foundation models.
- **p. 7 / 6 Method - extractive body cue:** One of the reasons is that foundation models preserve strong generalization ability.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| State/latent | GroundingDINO, latest, State-of-the-Arts, SOTA, openset, object, detection, network, reads, text, prompt, performs | robot pose, free-space/semantic map와 local goal | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | The SLAM modules generate a camera pose and a global volumetric map. | collision-free trajectory 또는 velocity command | p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 6 (6 Method) |
| Objective/outcome | Since Kimera updates the label measurements with a manually assigned likelihood probability and ignores the similarity score provided by GroundingDINO, it is easier to be affected by false label measurements. | goal reach, safety, localization error와 replanning latency | p. 6 (6 Method), p. 7 (6 Method), p. 7 (6 Method) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address such challenges, we propose a probabilistic label fusion method following the Bayes filter algorithm.
- **p. 6 / 6 Method - extractive body cue:** Compared with Kimera using RAM-GroundedSAM, our method achieved +15.6 mAP50.
- **p. 6 / 6 Method - extractive body cue:** The rest of the ScanNet experiment focus on evaluating each module of our method through an ablation study.
- **p. 7 / 6 Method - extractive body cue:** As shown in Figure 10(b), our method detects the table correctly.
- **p. 5 / V. EXPERIMENT - extractive body cue:** Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores.
- **p. 5 / V. EXPERIMENT - extractive body cue:** In experiment with fine-tune Mask R-CNN, although the mean AP is improved, they still reconstruct a few of semantic classes with 0 AP.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 11: Reconstructions in SceneNN 096. False semantic and over-segmented instances are highlighted in red circles. So far, the system run offline. As shown in ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT) |
| Embodiment/environment | We chose the public dataset ScanNet and SceneNN to evaluate the semantic mapping quality. | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT) |
| Dataset/benchmark | IEEE ROBOTICS AND AUTOMATION LETTERS, VOL.9, NO.3, MARCH 2024 | role, split, size and leakage | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT), p. 6 (V. EXPERIMENT) |
| Metric | Even for those predictable semantic classes, the pretrained Mask R-CNN suffers from the issue of generalization and achieve low AP50 scores. | definition, denominator, direction and uncertainty | p. 5 (V. EXPERIMENT), p. 5 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Baseline/ablation | We compared our method with Kimera 2 and a selfimplemented Fusion++. | fair input/data/compute/action matching | p. 5 (V. EXPERIMENT), p. 5 (V. EXPERIMENT), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 6 Method - extractive body cue:** As shown in Figure 10(a), RAM fails to recognize a table due to the extreme viewpoint, and GroundingDINO cannot detect it either.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: The visualization shows instance voxel grid map (a) before and (b) after the merge. The inconsistent instance mask is a natural limitation for ...
- **p. 7 / 6 Method - extractive body cue:** We consider those limitations of foundation models.
- **p. 5 / V. EXPERIMENT - extractive body cue:** Compared with the original Fusion++ method, the main difference is that our implemented version does not maintain a foreground probability for each voxel.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, the supervised object detectors are trained in specific data distribution and lack generalization ability.를 문제로 두고, Our method incrementally fuses the object detections from foundation models into an instance-aware semantic map.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 6 (6 Method), p. 6 (6 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
