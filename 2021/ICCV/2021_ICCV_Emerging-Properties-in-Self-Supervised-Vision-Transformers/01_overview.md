# Emerging Properties in Self-Supervised Vision Transformers

- Year/Venue: 2021 / ICCV
- Category: Foundations: Vision Foundation Models
- Tags: Vision Foundation Model, self-supervised, representation
- Paper link: ./2021/ICCV/2021_ICCV_Emerging-Properties-in-Self-Supervised-Vision-Transformers/paper.pdf
- Code/Project: https://github.com/facebookresearch/dino
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction Transformers have recently emerged as an alternative to convolutional neural networks (convnets) for visual recognition .
- Their adoption has been coupled with a training strategy inspired by natural language processing (NLP), that is, pretraining on large quantities of data and finetuning on the target ...
- The resulting Vision Transformers (ViT) are competitive with convnets but, they have not yet delivered clear benefits over them: they are computationally more demanding, require more training data, ...

## Core Idea
- These self-supervised pretraining objectives use the words in a sentence to create pretext tasks that provide a richer learning signal than the supervised objective of predicting a single ...
- Our motivation is that one of the main ingredients for the success of Transformers in NLP was the use of self-supervised pretraining, in the form of close procedure ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We show the synergy between DINO and ViTs by achieving 80.1% top-1 on ImageNet in linear evaluation with ViT-Base. ∗ Univ.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we question whether the muted success of Transformers in vision can be explained by the use of supervision in their pretraining.
- Our motivation is that one of the main ingredients for the success of Transformers in NLP was the use of self-supervised pretraining, in the form of close procedure ...
- These self-supervised pretraining objectives use the words in a sentence to create pretext tasks that provide a richer learning signal than the supervised objective of predicting a single ...

## Abstract Cue
- Introduction Transformers have recently emerged as an alternative to convolutional neural networks (convnets) for visual recognition .
