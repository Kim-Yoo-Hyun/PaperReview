# BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

- Year/Venue: 2023 / ICML
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, LLM, alignment
- Paper link: ./2023/ICML/2023_ICML_BLIP-2-Bootstrapping-Language-Image-Pre-training-with-Froz/paper.pdf
- Code/Project: https://github.com/salesforce/LAVIS
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The cost of vision-and-language pre-training has become increasingly prohibitive due to end-toend training of large-scale models.
- BLIP-2 achieves state-of-the-art performance on various visionlanguage tasks, despite having significantly fewer trainable parameters than existing methods.

## Core Idea
- In this paper, we propose a generic and Vision-and-Language Representation Learning Encoder Q-Former Querying Transformer … arXiv:2301.12597v3 [cs.CV] 15 Jun 2023 Junnan Li Dongxu Li Silvio Savarese Steven ...
- This paper proposes BLIP-2, a generic and efficient pretraining strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language models.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- BLIP-2 achieves state-of-the-art performance on various visionlanguage tasks, despite having significantly fewer trainable parameters than existing methods.
- For example, our model outperforms Flamingo80B by 8.7% on zero-shot VQAv2 with 54x fewer trainable parameters.
- Introduction Vision-language pre-training (VLP) research has witnessed a rapid advancement in the past few years, where pre-trained models with increasingly larger scale have been developed to continuously push ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we propose a generic and Vision-and-Language Representation Learning Encoder Q-Former Querying Transformer … arXiv:2301.12597v3 [cs.CV] 15 Jun 2023 Junnan Li Dongxu Li Silvio Savarese Steven ...
- However, most state-of-the-art vision-language models incur a high computation cost during pre-training, due to end-to-end training using large-scale models and datasets.
- BLIP-2 achieves state-of-the-art performance on various visionlanguage tasks, despite having significantly fewer trainable parameters than existing methods.

## Abstract Cue
- The cost of vision-and-language pre-training has become increasingly prohibitive due to end-toend training of large-scale models.
