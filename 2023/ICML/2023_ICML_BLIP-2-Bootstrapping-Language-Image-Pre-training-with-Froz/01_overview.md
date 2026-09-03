# BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2301.12597.
> PDF retrieval source: https://arxiv.org/pdf/2301.12597. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: Vision-Language Model, LLM, alignment
- Official paper: https://arxiv.org/abs/2301.12597
- Full-text retrieval: https://arxiv.org/pdf/2301.12597
- Code/Project: https://github.com/salesforce/LAVIS
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 We pre-train a lightweight Querying Transformer following a two-stage strategy to bridge the modality gap.를 문제로 두고, To achieve effective vision-language alignment with frozen unimodal models, we propose a Querying Transformer (QFormer) pre-trained with a new two-stage pre-training strategy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The cost of vision-and-language pre-training has become increasingly prohibitive due to end-toend training of large-scale models.
- **p. 1 / Abstract - extractive body cue:** This paper proposes BLIP-2, a generic and efficient pretraining strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language models.
- **p. 1 / Abstract - extractive body cue:** BLIP-2 bridges the modality gap with a lightweight Querying Transformer, which is pretrained in two stages.
- **p. 1 / Abstract - extractive body cue:** The first stage bootstraps vision-language representation learning from a frozen image encoder.
- **p. 1 / Abstract - extractive body cue:** The second stage bootstraps vision-to-language generative learning from a frozen language model.
- **p. 1 / 1. Introduction - extractive body cue:** We pre-train a lightweight Querying Transformer following a two-stage strategy to bridge the modality gap.
- **p. 1 / 1. Introduction - extractive body cue:** It acts as an information bottleneck between the frozen image encoder and the frozen LLM, where it feeds the most useful.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** To achieve effective vision-language alignment with frozen unimodal models, we propose a Querying Transformer (QFormer) pre-trained with a new two-stage pre-training strategy.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose a generic and Querying Transformer Q-Former Large Language Model (LLM) Queries Text Image Encoder Bootstrapping Pre-trained Image Models Bootstrapping Pre-trained ...
- **p. 2 / 3.1. Model Architecture - extractive body cue:** We propose Q-Former as the trainable module to bridge the gap between a frozen image encoder and a frozen LLM.
- **p. 2 / 3. Method - extractive body cue:** We propose BLIP-2, a new vision-language pre-training method that bootstraps from frozen pre-trained unimodal models.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** (Right) The self-attention masking strategy for each objective to control query-text interaction. for visual feature extraction, (2) a text transformer that can function as both ...
- **p. 3 / 3.2. Bootstrap Vision-Language Representation - extractive body cue:** Since the architecture of Q-Former does not allow direct interactions between the frozen image encoder and the text tokens, the information required for generating the ...
- **p. 2 / 3.1. Model Architecture - extractive body cue:** As shown in Figure 2, Q-Former consists of two transformer submodules that share the same self-attention layers: (1) an image transformer that interacts with the ...
- **p. 2 / 3. Method - extractive body cue:** This section first introduces the model architecture of Q-Former, and then delineates the two-stage pre-training procedures.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It extracts a fixed number of output features from the image encoder, independent of input image resolution. | 논문이 명시한 observation과 task input | p. 2 (3.1. Model Architecture), p. 4 (3.2. Bootstrap Vision-Language Representation) |
| State/latent | extracts, fixed, number, output, features, image, encoder, independent, input, resolution, fully-connected, layer | task state 또는 decision variable | p. 2 (3.1. Model Architecture), p. 4 (3.2. Bootstrap Vision-Language Representation), p. 4 (3.2. Bootstrap Vision-Language Representation) |
| Output/action | The fully-connected layer adapts from the output dimension of the Q-Former to the input dimension of the chosen LLM. | paper-specific output/action | p. 4 (3.2. Bootstrap Vision-Language Representation), p. 4 (3.2. Bootstrap Vision-Language Representation), p. 2 (1. Introduction) |
| Objective/outcome | Inspired by BLIP (Li et al., 2022), we jointly optimize three pre-training objectives that share the same input format and model parameters. | primary task objective와 closed-loop behavior | p. 3 (3.2. Bootstrap Vision-Language Representation), p. 3 (3.1. Model Architecture), p. 4 (3.3. Bootstrap Vision-to-Language Generative Learning) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** To achieve effective vision-language alignment with frozen unimodal models, we propose a Querying Transformer (QFormer) pre-trained with a new two-stage pre-training strategy.
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose a generic and Querying Transformer Q-Former Large Language Model (LLM) Queries Text Image Encoder Bootstrapping Pre-trained Image Models Bootstrapping Pre-trained ...
- **p. 2 / 3.1. Model Architecture - extractive body cue:** We propose Q-Former as the trainable module to bridge the gap between a frozen image encoder and a frozen LLM.
- **p. 2 / 3. Method - extractive body cue:** We propose BLIP-2, a new vision-language pre-training method that bootstraps from frozen pre-trained unimodal models.
- **p. 6 / 4. Experiment - extractive body cue:** Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training.
- **p. 6 / 4.1. Instructed Zero-shot Image-to-Text Generation - extractive body cue:** (2) Within the same LLM family, larger models outperform smaller ones.
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Comparison with state-of-the-art models fine-tuned for visual question answering. of-the-art performance with significant improvement on NoCaps over existing methods, demonstrating strong gener- alization ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. The image-grounded text generation (ITG) loss improves image-text retrieval performance by enforcing the queries to extract language-relevant visual features.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4. Experiment), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Embodiment/environment | On the OK-VQA (Marino et al., 2019) dataset, BLIP-2 comes secondary to Flamingo80B. | hardware/simulator version and reset protocol | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Dataset/benchmark | BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models Models #Trainable Params NoCaps Zero-shot (validation set) COCO Fine-tuned in-domain near-domain out-domain overall Karpathy test | role, split, size and leakage | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 7 (4.1. Instructed Zero-shot Image-to-Text Generation) |
| Metric | We make a promising observation from Table 2: a stronger image encoder or a stronger LLM both lead to better performance. | definition, denominator, direction and uncertainty | p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 6 (4. Experiment), p. 7 (Figure/Table caption) |
| Baseline/ablation | Compared to previous state-of-the-art models, BLIP-2 achieves improved performance while requiring substantially fewer number of trainable parameters during vision-language pre-training. | fair input/data/compute/action matching | p. 6 (4. Experiment), p. 6 (4.1. Instructed Zero-shot Image-to-Text Generation), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Limitation - extractive body cue:** The LLMs cannot learn from it the correlation among multiple image-text pairs in a single sequence.
- **p. 8 / 5. Limitation - extractive body cue:** We aim to create a similar dataset in future work.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Effect of vision-language representation learning on vision-to-language generative learning. Without representation learning, the Q-Former fails the bridge the modality gap, leading to significantly ...

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 We pre-train a lightweight Querying Transformer following a two-stage strategy to bridge the modality gap.를 문제로 두고, To achieve effective vision-language alignment with frozen unimodal models, we propose a Querying Transformer (QFormer) pre-trained with a new two-stage pre-training strategy.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Model Architecture), p. 3 (3.2. Bootstrap Vision-Language Representation), p. 2 (3.1. Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
