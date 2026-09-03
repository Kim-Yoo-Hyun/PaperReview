# BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2201.12086.
> PDF retrieval source: https://arxiv.org/pdf/2201.12086. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Foundations: Vision and Language Models
- Tier: REFERENCE
- Tags: Vision-Language Model, alignment, Generation
- Official paper: https://arxiv.org/abs/2201.12086
- Full-text retrieval: https://arxiv.org/pdf/2201.12086
- Code/Project: https://github.com/salesforce/BLIP
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 However, existing methods have two major limitations: (1) Model perspective: most methods either adopt an encoder-based model (Radford et al., 2021; Li et al., 2021a), or an encoder-decoder (Cho et al., 2021; ...를 문제로 두고, To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Vision-Language Pre-training (VLP) has advanced the performance for many vision-language tasks.
- **p. 1 / Abstract - extractive body cue:** However, most existing pre-trained models only excel in either understanding-based tasks or generation-based tasks.
- **p. 1 / Abstract - extractive body cue:** Furthermore, performance improvement has been largely achieved by scaling up the dataset with noisy image-text pairs collected from the web, which is a suboptimal source ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose BLIP, a new VLP framework which transfers flexibly to both vision-language understanding and generation tasks.
- **p. 1 / Abstract - extractive body cue:** BLIP effectively utilizes the noisy web data by bootstrapping the captions, where a captioner generates synthetic captions and a filter removes the noisy ones.
- **p. 1 / 1. Introduction - extractive body cue:** However, existing methods have two major limitations: (1) Model perspective: most methods either adopt an encoder-based model (Radford et al., 2021; Li et al., 2021a), ...
- **p. 1 / 1. Introduction - extractive body cue:** BLIP is a new VLP framework which enables a wider range of downstream tasks than existing methods.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation.
- **p. 2 / 1. Introduction - extractive body cue:** We propose multimodal mixture of encoder-decoder, a unified vision-language model which can operate in one of the three functionalities: (1) Unimodal encoder is trained with ...
- **p. 3 / 3. Method - extractive body cue:** We propose BLIP, a unified VLP framework to learn from noisy image-text pairs.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** In order to pre-train a unified model with both understanding and generation capabilities, we propose multimodal mixture of encoder-decoder (MED), a multi-task model which can ...
- **p. 4 / 3.3. CapFilt - extractive body cue:** We propose Captioning and Filtering (CapFilt), a new method to improve the quality of the text corpus.
- **p. 3 / 3. Method - extractive body cue:** This section first introduces our new model architecture MED and its pre-training objectives, and then delineates CapFilt for dataset bootstrapping.
- **p. 4 / 3.3. CapFilt - extractive body cue:** Finally, we combine the filtered image-text pairs with the human-annotated pairs to form a new dataset, which we use to pre-train a new model.
- **p. 4 / 3.3. CapFilt - extractive body cue:** The filter is an image-grounded text encoder.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We also find that more diverse captions yield larger gains. • BLIP achieves state-of-the-art performance on a wide range of vision-language tasks, including image-text re | 논문이 명시한 observation과 task input | p. 1 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | find, more, diverse, captions, yield, larger, gains, BLIP, achieves, state-of-the-art, performance, wide | task state 또는 decision variable | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/action | We also achieve state-ofthe-art zero-shot performance when directly transferring our models to two video-language tasks: text-to-video retrieval and videoQA. | paper-specific output/action | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Model Architecture) |
| Objective/outcome | It optimizes a cross entropy loss which trains the model to maximize the likelihood of the text in an autoregressive manner. | primary task objective와 closed-loop behavior | p. 3 (3.2. Pre-training Objectives), p. 3 (3.2. Pre-training Objectives), p. 4 (3.3. CapFilt) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation.
- **p. 2 / 1. Introduction - extractive body cue:** We propose multimodal mixture of encoder-decoder, a unified vision-language model which can operate in one of the three functionalities: (1) Unimodal encoder is trained with ...
- **p. 3 / 3. Method - extractive body cue:** We propose BLIP, a unified VLP framework to learn from noisy image-text pairs.
- **p. 3 / 3.1. Model Architecture - extractive body cue:** In order to pre-train a unified model with both understanding and generation capabilities, we propose multimodal mixture of encoder-decoder (MED), a multi-task model which can ...
- **p. 4 / 3.3. CapFilt - extractive body cue:** We propose Captioning and Filtering (CapFilt), a new method to improve the quality of the text corpus.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference and lack of ...
- **p. 4 / 4.2. Effect of CapFilt - extractive body cue:** Furthermore, by using a large captioner and filter with ViT-L, performance of the base model can also be improved.
- **p. 4 / 4.2. Effect of CapFilt - extractive body cue:** When only the captioner or the filter is applied to the dataset with 14M images, performance improvement can be observed.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 4 (4.2. Effect of CapFilt) |
| Embodiment/environment | In Table 1, we compare models pre-trained on different datasets to demonstrate the efficacy of CapFilt on downstream tasks, including image-text retrieval and image captioning with finetuned and zero-shot settings. | hardware/simulator version and reset protocol | p. 4 (4.2. Effect of CapFilt), p. 4 (4.1. Pre-training Details) |
| Dataset/benchmark | BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation Pre-train dataset Bootstrap Vision backbone Retrieval-FT (COCO) Retrieval-ZS (Flickr) Caption-FT (COCO) Caption-ZS (NoCaps) | role, split, size and leakage | p. 4 (4.2. Effect of CapFilt), p. 4 (4.1. Pre-training Details), p. 5 (4.2. Effect of CapFilt) |
| Metric | Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference and lack of temporal mod- eling, our models achieve state-of-the-art ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 1 (Figure/Table caption), p. 2 (Figure/Table caption) |
| Baseline/ablation | Table 11. Comparisons with state-of-the-art methods for video question answering. We report top-1 test accuracy on two datasets. Despite the domain difference and lack of temporal mod- eling, our models achieve state-of-the-art ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 4 (4.2. Effect of CapFilt), p. 6 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 9 / Figure/Table caption - extractive body cue:** Table 13. Continue training the pre-trained model offers less gain compared to training a new model with the bootstrapped dataset. from the previous pre-trained model, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 6. Zero-shot image-text retrieval results on Flickr30K. layers except for SA leads to better performance compared to not sharing, while also reducing the model ...

## Why Read It

Foundations: Vision and Language Models의 upstream 문제를 이해하기 위해 읽는다. 본문은 However, existing methods have two major limitations: (1) Model perspective: most methods either adopt an encoder-based model (Radford et al., 2021; Li et al., 2021a), or an encoder-decoder (Cho et al., 2021; ...를 문제로 두고, To this end, we propose BLIP: Bootstrapping LanguageImage Pre-training for unified vision-language understanding and generation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Method), p. 3 (3.1. Model Architecture), p. 4 (3.3. CapFilt), p. 4 (3.3. CapFilt) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
