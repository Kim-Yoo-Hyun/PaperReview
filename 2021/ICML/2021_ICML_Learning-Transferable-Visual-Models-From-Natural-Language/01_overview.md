# Learning Transferable Visual Models From Natural Language Supervision

- Year/Venue: 2021 / ICML
- Category: Foundations: Vision-Language Models
- Tags: CLIP, Vision-Language Model, alignment
- Paper link: ./2021/ICML/2021_ICML_Learning-Transferable-Visual-Models-From-Natural-Language/paper.pdf
- Code/Project: https://github.com/openai/CLIP
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and ...

## Core Idea
- For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on.
- The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories.
- We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch ...
- We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch ...
- For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on.
- After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks.

## Abstract Cue
- State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories.
