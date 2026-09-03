# Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2303.05499.
> PDF retrieval source: https://arxiv.org/pdf/2303.05499. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: Vision Foundation Model, grounding, open-vocabulary
- Official paper: https://arxiv.org/abs/2303.05499
- Full-text retrieval: https://arxiv.org/pdf/2303.05499
- Code/Project: https://github.com/IDEA-Research/GroundingDINO
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (33 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Most existing open-set models [14,21] rely on pre-trained CLIP models for concept generalization.를 문제로 두고, To mitigate this issue and improve model performance during grounded training, we introduce a technique that utilizes sub-sentence level text features.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / 1 Introduction - extractive body cue:** A key indicator of an Artificial General Intelligence (AGI) system's capability is its proficiency in handling open-world scenarios.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we aim to develop a strong system to detect arbitrary objects specified by human language inputs, a task commonly referred to as ...
- **p. 2 / 1 Introduction - extractive body cue:** The task has wide applications for its great potential as a generic object detector.
- **p. 2 / 1 Introduction - extractive body cue:** For example, we can cooperate with generative models for image editing (as shown in Fig.
- **p. 2 / 1 Introduction - extractive body cue:** In pursuit of this goal, we design the strong open-set object detector Grounding DINO by following the two principles: tight modality fusion based on DINO ...
- **p. 3 / 1 Introduction - extractive body cue:** Most existing open-set models [14,21] rely on pre-trained CLIP models for concept generalization.
- **p. 2 / 1 Introduction - extractive body cue:** The key to open-set detection is introducing language for unseen object generalization [1,7,25].

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** To mitigate this issue and improve model performance during grounded training, we introduce a technique that utilizes sub-sentence level text features.
- **p. 3 / 1 Introduction - extractive body cue:** The layer-by-layer design enables it to interact with language information easily.
- **p. 19 / A.2 Pseudo Code Language-Guided Query Selection - extractive body cue:** We present the pseudo-code of the Language-Guided Query Selection module in Algorithm 1.
- **p. 2 / 1 Introduction - extractive body cue:** Most existing open-set detectors are developed by extending closed-set detectors to open-set scenarios with language information.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we aim to develop a strong system to detect arbitrary objects specified by human language inputs, a task commonly referred to as ...
- **p. 5 / 1. Model Overall - extractive body cue:** Input Text Input Image Model Outputs Keys& Values Cross-Modality Queries Text Features Image Features Vanilla Text Features A Cross-Modality Decoder Layer Cross-Modality Query Self-Attention Image ...
- **p. 19 / A.1 Hyperparameters - extractive body cue:** Item Value optimizer AdamW lr 1e-4 lr of image backbone 1e-5 lr of text backbone 1e-5 weight decay 0.0001 clip max norm 0.1 number of ...
- **p. 19 / A.2 Pseudo Code Language-Guided Query Selection - extractive body cue:** We use bs and ndim for batch size and feature dimension in the pseudo-code. num_img_tokens and num_text_tokens are used for the number of image and ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Input Text Input Image Model Outputs Keys& Values Cross-Modality Queries Text Features Image Features Vanilla Text Features A Cross-Modality Decoder Layer Cross-Modality Query Self-Attention Image Cross-Attention Text Cross-Attention FF ... | 논문이 명시한 observation과 task input | p. 5 (1. Model Overall), p. 2 (1 Introduction) |
| State/latent | Input, Text, Image, Model, Outputs, Keys, Values, Cross-Modality, Queries, Features, Vanilla, Decoder | task state 또는 decision variable | p. 5 (1. Model Overall), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | The key to achieving this goal is using contrastive loss between region outputs and language features at the neck and/or head outputs. | paper-specific output/action | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | Item Value optimizer AdamW lr 1e-4 lr of image backbone 1e-5 lr of text backbone 1e-5 weight decay 0.0001 clip max norm 0.1 number of encoder layers 6 number of decoder layers ... | primary task objective와 closed-loop behavior | p. 19 (A.1 Hyperparameters), p. 5 (1. Model Overall) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** To mitigate this issue and improve model performance during grounded training, we introduce a technique that utilizes sub-sentence level text features.
- **p. 3 / 1 Introduction - extractive body cue:** The layer-by-layer design enables it to interact with language information easily.
- **p. 19 / A.2 Pseudo Code Language-Guided Query Selection - extractive body cue:** We present the pseudo-code of the Language-Guided Query Selection module in Algorithm 1.
- **p. 2 / 1 Introduction - extractive body cue:** Most existing open-set detectors are developed by extending closed-set detectors to open-set scenarios with language information.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we aim to develop a strong system to detect arbitrary objects specified by human language inputs, a task commonly referred to as ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 9: Transfer pre-trained DINO to Grounding DINO. We freeze shared modules between DINO and Grounding DINO during grounded fine-tuning. All models are trained with ...
- **p. 13 / 4 Experiments - extractive body cue:** The results show that encoder fusion significantly improves model performance on both COCO and LVIS datasets.
- **p. 13 / 4 Experiments - extractive body cue:** Grounding DINO 13 The results show that RefC helps improve the COCO zero-shot and fine-tuning performance but hurts the LVIS and ODinW results.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 21 (Figure/Table caption), p. 13 (4 Experiments) |
| Embodiment/environment | LVIS Benchmark LVIS [15] is a dataset for long-tail objects. | hardware/simulator version and reset protocol | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Dataset/benchmark | We pre-train models on large-scale datasets and directly evaluate our model on the COCO benchmark. | role, split, size and leakage | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Metric | This suggests that while GLIPv2 may exhibit larger performance variance across different datasets, Grounding DINO maintains a more consistent performance level. | definition, denominator, direction and uncertainty | p. 11 (4 Experiments), p. 12 (Figure/Table caption), p. 9 (4 Experiments) |
| Baseline/ablation | Table 2. We pre-train models on large-scale datasets and directly evaluate our model on the COCO benchmark. As the O365 dataset [43] has (nearly4) covered all categories in COCO, we evaluate an ... | fair input/data/compute/action matching | p. 9 (Figure/Table caption), p. 10 (4 Experiments), p. 10 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / Figure/Table caption - extractive body cue:** Table 7: Ablations for our model. All models are trained on the O365 dataset with a Swin Transformer Tiny backbone. fusion approach. Moreover, we extend ...
- **p. 10 / 4 Experiments - extractive body cue:** To our knowledge, no existing DETR-like models effectively address the rarity challenge in LVIS without extra training data, which may be a characteristic limitation of ...
- **p. 10 / 4 Experiments - extractive body cue:** A larger-scale training will be left as our future work.
- **p. 11 / 4 Experiments - extractive body cue:** In our future work, we will perform more studies, including varying the semantic concept coverage of the training data and increasing the scale of the ...
- **p. 21 / Figure/Table caption - extractive body cue:** Table 9: Transfer pre-trained DINO to Grounding DINO. We freeze shared modules between DINO and Grounding DINO during grounded fine-tuning. All models are trained with ...

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 Most existing open-set models [14,21] rely on pre-trained CLIP models for concept generalization.를 문제로 두고, To mitigate this issue and improve model performance during grounded training, we introduce a technique that utilizes sub-sentence level text features.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 5 (1. Model Overall), p. 19 (A.1 Hyperparameters) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
