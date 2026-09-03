# Sensor-Invariant Tactile Representation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=RnJY9WcpA3.
> PDF retrieval source: https://arxiv.org/pdf/2502.19638. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, tactile sensing, sensor transfer, representation learning
- Official paper: https://openreview.net/forum?id=RnJY9WcpA3
- Full-text retrieval: https://arxiv.org/pdf/2502.19638
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 However, many works that directly apply existing representation learning methods to the tactile modality ignore the significant domain gap seen between sensors.를 문제로 두고, In this section, we introduce our framework for training Sensor-Invariant Tactile Representation (SITR).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** High-resolution tactile sensors have become critical for embodied perception and robotic manipulation.
- **p. 1 / ABSTRACT - extractive body cue:** However, a key challenge in the field is the lack of transferability between sensors due to design and manufacturing variations, which result in significant differences ...
- **p. 1 / ABSTRACT - extractive body cue:** This limitation hinders the ability to transfer models or knowledge learned from one sensor to another.
- **p. 1 / ABSTRACT - extractive body cue:** To address this, we introduce a novel method to extract Sensor-Invariant Tactile Representations (SITR), enabling zero-shot transfer across optical tactile sensors.
- **p. 1 / ABSTRACT - extractive body cue:** Our approach utilizes a transformer-based architecture trained on a diverse dataset of simulated sensor designs, allowing generalizability to new sensors in the real world with ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, many works that directly apply existing representation learning methods to the tactile modality ignore the significant domain gap seen between sensors.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** However, these methods often depend on large datasets and treat sensor types as fixed categories, failing to account for variations within the same sensor type ...

## Core Idea

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In this section, we introduce our framework for training Sensor-Invariant Tactile Representation (SITR).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce a novel framework for generating sensor-invariant feature representations from highresolution tactile readings, enabling zero-shot transfer to unseen sensors across multiple downstream tasks.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our framework introduces a novel combination of geometry-preserving supervision, supervised contrastive learning, and sensor-specific calibration images.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our framework incorporates three core innovations: 1.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** We introduce random variability in the calibration positions to make the training more robust to the real-world setting.
- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** Classification Decoders We use Cross Entropy Loss for this task. • SITR: We unpatchify the output tokens xi to a feature map and pass it ...
- **p. 15 / A.1.2 ARCHITECTURE - extractive body cue:** Pose Estimation Decoders We use MSE loss for this task. • SITR: We pass 2 tactile images x1 and x2 into the network separately.
- **p. 14 / A.1.2 ARCHITECTURE - extractive body cue:** SITR Training Decoders: During the pre-training phase for SITR, we use two decoders: • Normal Map Reconstruction Decoder: We apply a simple linear projection to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We subtract the sensor background from all the input images to get the pixel-wise color change as described in Section 3.1. | tactile image/force, vision과 proprioceptive history | p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |
| State/latent | subtract, sensor, background, input, images, pixel-wise, color, change, described, Section, NETWORK, ARCHITECTURE | contact geometry, force state 또는 latent dynamics | p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION), p. 14 (A.1.2 ARCHITECTURE) |
| Output/action | 3.2 NETWORK ARCHITECTURE Input: We use the tactile image and a set of calibration images for the sensor as inputs for the network. | grasp/contact action, force command 또는 object motion | p. 4 (1 INTRODUCTION), p. 14 (A.1.2 ARCHITECTURE), p. 14 (A.1.2 ARCHITECTURE) |
| Objective/outcome | Classification Decoders We use Cross Entropy Loss for this task. • SITR: We unpatchify the output tokens xi to a feature map and pass it through a ResNet-18 network. | slip/contact success, force/pose error와 robustness | p. 14 (A.1.2 ARCHITECTURE), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS), p. 24 (A.6.1 CONTRIBUTION OF LOSS TERMS) |

## Main Claims and Actual Contribution

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In this section, we introduce our framework for training Sensor-Invariant Tactile Representation (SITR).
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We introduce a novel framework for generating sensor-invariant feature representations from highresolution tactile readings, enabling zero-shot transfer to unseen sensors across multiple downstream tasks.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our framework introduces a novel combination of geometry-preserving supervision, supervised contrastive learning, and sensor-specific calibration images.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our framework incorporates three core innovations: 1.
- **p. 5 / 1 INTRODUCTION - extractive body cue:** We introduce random variability in the calibration positions to make the training more robust to the real-world setting.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Results of object classification accuracy on 16 classes for model transfer and no-transfer performance. We report the mean and standard deviation of transfer ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 8: Ablation study examining the impact of SCL and varying contrastive temperature τ on SITR's performance. Subplots (i) and (ii) show classification accuracy in ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** As shown in Table 1, SITR outperforms all baselines by a large margin regarding classification accuracy when transferred across sensors.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 10 (Figure/Table caption) |
| Embodiment/environment | 5.3 OBJECT CLASSIFICATION We compare SITR with baselines using our real-world classification dataset from Section 4.2 and report top-1 accuracy. | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Dataset/benchmark | 6 presents the t-SNE visualization of the SITR features for the contacts in our real-world classification dataset. | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Metric | Let Aij represent the performance (e.g., classification accuracy or pose estimation error) when trained on Si and evaluated on Sj. | definition, denominator, direction and uncertainty | p. 6 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (Figure/Table caption) |
| Baseline/ablation | As shown in Table 1, SITR outperforms all baselines by a large margin regarding classification accuracy when transferred across sensors. | fair input/data/compute/action matching | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Despite these limitations, the preservation of dense surface features demonstrates the robustness of SITR in accurately modeling the contact geometry across varying sensor inputs.
- **p. 10 / 7 DISCUSSION - extractive body cue:** Another direction of future work is incorporating marker-based tactile information to SITR.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Though, these reconstructions are naturally constrained by the resolution and sensitivity limitations of the sensors.
- **p. 10 / 8 CONCLUSION - extractive body cue:** Our experimental results demonstrate that SITR outperforms baseline models and other related tactile representations in different downstream tasks, showcasing robust transferability and effectiveness.
- **p. 9 / 5 EXPERIMENTS - extractive body cue:** We choose case (18*) for SITR since increasing the number of calibration images does not incur additional inference costs, as calibration tokens are computed only ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 However, many works that directly apply existing representation learning methods to the tactile modality ignore the significant domain gap seen between sensors.를 문제로 두고, In this section, we introduce our framework for training Sensor-Invariant Tactile Representation (SITR).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 14 (A.1.2 ARCHITECTURE) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
