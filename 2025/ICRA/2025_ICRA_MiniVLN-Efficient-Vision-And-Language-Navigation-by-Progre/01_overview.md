# MiniVLN: Efficient Vision-And-Language Navigation by Progressive Knowledge Distillation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf.
> PDF retrieval source: https://arxiv.org/pdf/2409.18800v1. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Navigation
- Official paper: https://www.proceedings.com/content/081/081087webtoc.pdf
- Full-text retrieval: https://arxiv.org/pdf/2409.18800v1
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Our findings indicate that two-stage distillation is more effective in bridging the performance gap between the teacher model and the student model compared to single-stage distillation. • MiniVLN achieves comparable or superior ...를 문제로 두고, In this work, our main contributions are: • We introduce MiniVLN, a high-performance and lowcomplexity model specifically designed for deployment on resource-constrained devices. • To the best of our knowledge, our work ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In recent years, Embodied Artificial Intelligence (Embodied AI) has advanced rapidly, yet the increasing size of models conflicts with the limited computational capabilities of Embodied ...
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we aim to achieve both high model performance and practical deployability.
- **p. 1 / Abstract - extractive body cue:** Specifically, we focus on Vision-and-Language Navigation (VLN), a core task in Embodied AI.
- **p. 1 / Abstract - extractive body cue:** This paper introduces a two-stage knowledge distillation framework, producing a student model, MiniVLN, and showcasing the significant potential of distillation techniques in developing lightweight models.
- **p. 1 / Abstract - extractive body cue:** The proposed method aims to capture fine-grained knowledge during the pretraining phase and navigation-specific knowledge during the fine-tuning phase.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our findings indicate that two-stage distillation is more effective in bridging the performance gap between the teacher model and the student model compared to single-stage ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** AutoVLN [5] automatically generates a large-scale VLN dataset that significantly boosts model generalization.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, our main contributions are: • We introduce MiniVLN, a high-performance and lowcomplexity model specifically designed for deployment on resource-constrained devices. • To ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method incorporates knowledge distillation in both the pre-training and fine-tuning stages, leading to the final student model MiniVLN.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast to approaches [14], [32] that apply distillation solely during the pre-training phase or only during the finetuning phase, we introduce a two-stage distillation ...
- **p. 3 / IV. METHOD - extractive body cue:** On this premise, we propose MiniVLN with two distinct distillation strategies tailored for each training phase.
- **p. 4 / IV. METHOD - extractive body cue:** Distillation Loss The language encoder and panorama encoder in Scalepre consists of NL = 9 and NP = 2 transformer blocks respectively.
- **p. 4 / IV. METHOD - extractive body cue:** The MSE loss between the outputs of the teacher and student models for this panoramic observation is computed as: Lpano = MSE(hT t , hS ...
- **p. 3 / IV. METHOD - extractive body cue:** Knowledge Distillation During Pretraining Phase In order to distill knowledge encapsulated within the teacher model's learned features, we conduct Embedding Distillation, Attention-based Distillation, and Hidden ...
- **p. 5 / IV. METHOD - extractive body cue:** Compared to TinyBERT, the distillation method proposed in this paper includes certain optimizations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The agent must learn a policy π that predicts the next action based on the instruction I, the agent's navigation history, and the current observation Ot. | camera/depth stream, pose, map와 language goal | p. 3 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES) |
| State/latent | agent, must, learn, policy, predicts, next, action, instruction, navigation, history, current, observation | robot pose, free-space/semantic map와 local goal | p. 3 (III. PRELIMINARIES), p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD) |
| Output/action | This process is formulated as a partially observable Markov decision process (POMDP), where the agent's future observations are conditionally independent of past observations given the current state st. | collision-free trajectory 또는 velocity command | p. 2 (III. PRELIMINARIES), p. 3 (IV. METHOD), p. 4 (IV. METHOD) |
| Objective/outcome | Method Val Unseen Test Unseen Param(M)↓ SR↑ SPL↑ SR↑ SPL↑ PREVALENT [10] 57 53 54 51 209.83 RecBERT [12] 63 57 63 57 159.99 HAMT [4] 66 61 65 60 170.39 ADAPT ... | goal reach, safety, localization error와 replanning latency | p. 5 (IV. METHOD), p. 3 (IV. METHOD), p. 4 (IV. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, our main contributions are: • We introduce MiniVLN, a high-performance and lowcomplexity model specifically designed for deployment on resource-constrained devices. • To ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method incorporates knowledge distillation in both the pre-training and fine-tuning stages, leading to the final student model MiniVLN.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In contrast to approaches [14], [32] that apply distillation solely during the pre-training phase or only during the finetuning phase, we introduce a two-stage distillation ...
- **p. 3 / IV. METHOD - extractive body cue:** On this premise, we propose MiniVLN with two distinct distillation strategies tailored for each training phase.
- **p. 4 / IV. METHOD - extractive body cue:** Distillation Loss The language encoder and panorama encoder in Scalepre consists of NL = 9 and NP = 2 transformer blocks respectively.
- **p. 5 / V. EXPERIMENTS - extractive body cue:** 2) Evaluation Metrics: We assess agent performance using standard VLN metrics, including Success Rate (SR) and Success weighted by Path Length (SPL).
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Model parameters versus accuracy comparison on R2R dataset among state-of-the-art VLN methods. Compared to other student models, MiniVLN achieves the best performance. When ...
- **p. 5 / V. EXPERIMENTS - extractive body cue:** Notably, these results are achieved with MiniVLN being only about one-ninth the size of the models listed in Table II.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (V. EXPERIMENTS), p. 1 (Figure/Table caption) |
| Embodiment/environment | On the R2R datasets, the results, as shown in Figure 4, reveal that the non-distilled model achieves an SR of only 74.16 and an SPL of 65.15 on the validation unseen set, ... | hardware/simulator version and reset protocol | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Dataset/benchmark | Method Validation Unseen Test Unseen Param(M)↓ SR↑ SPL↑ RGS↑ RGSPL↑ SR↑ SPL↑ RGS↑ RGSPL↑ HAMT [4] 32.95 30.20 18.92 17.28 30.40 26.67 14.88 13.08 170.39 DUET [6] 46.98 33.73 32.15 23.03 52.51 ... | role, split, size and leakage | p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |
| Metric | 2) Evaluation Metrics: We assess agent performance using standard VLN metrics, including Success Rate (SR) and Success weighted by Path Length (SPL). | definition, denominator, direction and uncertainty | p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS) |
| Baseline/ablation | Fig. 1. Model parameters versus accuracy comparison on R2R dataset among state-of-the-art VLN methods. Compared to other student models, MiniVLN achieves the best performance. When compared to state-of-the-art (SoTA) methods, MiniVLN us ... | fair input/data/compute/action matching | p. 1 (Figure/Table caption), p. 5 (V. EXPERIMENTS), p. 5 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / VI. CONCLUSIONS - extractive body cue:** In this paper, we aim to enhance the efficiency of VLN models through knowledge distillation, enabling deployment on mobile or edge devices.
- **p. 6 / VI. CONCLUSIONS - extractive body cue:** We propose a progressive twostage knowledge distillation framework: in the pre-training phase, the model focuses on learning fine-grained knowledge, while in the fine-tuning phase, it ...
- **p. 6 / VI. CONCLUSIONS - extractive body cue:** Notably, Our experiments show that the two-stage distillation method enables the student model to more closely match the teacher model's performance than the single-stage approach.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Our findings indicate that two-stage distillation is more effective in bridging the performance gap between the teacher model and the student model compared to single-stage distillation. • MiniVLN achieves comparable or superior ...를 문제로 두고, In this work, our main contributions are: • We introduce MiniVLN, a high-performance and lowcomplexity model specifically designed for deployment on resource-constrained devices. • To the best of our knowledge, our work ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (III. PRELIMINARIES), p. 3 (III. PRELIMINARIES), p. 4 (IV. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
