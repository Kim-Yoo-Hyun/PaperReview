# DINOv2: Learning Robust Visual Features without Supervision

- Year/Venue: 2023 / TMLR
- Category: Foundations: Vision Foundation Models
- Tags: self-supervised, representation
- Paper link: ./2023/TMLR/2023_TMLR_DINOv2-Learning-Robust-Visual-Features-without-Supervision/paper.pdf
- Code/Project: https://github.com/facebookresearch/dinov2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size.
- This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources.

## Core Idea
- In terms of data, we propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data, as typically done in the self-supervised ...
- We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- First, we show that our self-supervised features outperform the current state of the art by a very large margin.
- In Table 5, we show that the Top-1 accuracy on the validation set of ImageNet-1k improves by more than +2% when the backbone is finetuned.
- We also want to validate that our features are competitive with state-of-the-art open-source weakly supervised models.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources.
- We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size.
- In terms of data, we propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data, as typically done in the self-supervised ...

## Abstract Cue
- The recent breakthroughs in natural language processing for model pretraining on large quantities of data have opened the way for similar foundation models in computer vision.
