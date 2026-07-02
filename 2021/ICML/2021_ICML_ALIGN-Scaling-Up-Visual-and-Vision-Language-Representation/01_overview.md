# ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

- Year/Venue: 2021 / ICML
- Category: Foundations: Vision-Language Models
- Tags: Vision-Language Model, alignment, representation
- Paper link: ./2021/ICML/2021_ICML_ALIGN-Scaling-Up-Visual-and-Vision-Language-Representation/paper.pdf
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction In the existing literature, visual and vision-language representation learning are mostly studied separately with different training data sources.
- Curation of such pre-training datasets requires heavy work on data gathering, sampling, and human annotation, and hence is difficult to scale.
- In this paper, we alt-text pairs, obtained without expensive filtering or post-processing steps in the Conceptual Captions dataset.

## Core Idea
- A simple dual-encoder architecture learns to align visual and language representations of the image and text pairs using a contrastive loss.
- While representation learning in NLP has transitioned to training on raw text without human annotations, visual and vision-language representations still rely heavily on curated training datasets that are ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The aligned visual and language representations enables zero-shot image classification and also set new state-of-the-art results on Flickr30K and MSCOCO image-text retrieval benchmarks, even when compared with more ...
- We show that the scale of our corpus can make up for its noise and leads to state-of-the-art representations even with such a simple learning scheme.
- Our visual representation achieves strong performance when transferred to classification tasks such as ImageNet and VTAB.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- The aligned visual and language representations enables zero-shot image classification and also set new state-of-the-art results on Flickr30K and MSCOCO image-text retrieval benchmarks, even when compared with more ...
- A simple dual-encoder architecture learns to align visual and language representations of the image and text pairs using a contrastive loss.
- Introduction In the existing literature, visual and vision-language representation learning are mostly studied separately with different training data sources.

## Abstract Cue
- Pre-trained representations are becoming crucial for many NLP and perception tasks.
