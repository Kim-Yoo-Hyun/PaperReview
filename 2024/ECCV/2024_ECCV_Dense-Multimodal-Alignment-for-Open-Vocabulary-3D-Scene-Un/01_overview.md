# Dense Multimodal Alignment for Open-Vocabulary 3D Scene Understanding

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, semantic
- Paper link: ./2024/ECCV/2024_ECCV_Dense-Multimodal-Alignment-for-Open-Vocabulary-3D-Scene-Un/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, the annotation of large-scale 3D data is very costly , impeding the training of generalizable models for open-vocabulary scene understanding.

## Core Idea
- In this work, we propose a Dense Multimodal Alignment (DMA) framework to densely co-embed different modalities into a common space for maximizing their synergistic benefits.
- 1, we propose a dense multimodal alignment (DMA) framework for open-vocabulary 3D scene understanding, where we construct dense correspondences across 2D image pixels, 3D points and 1D texts, ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our DMA(OpenSeg) using only 3D model for prediction outperforms OpenScene(OpenSeg)-2D3D by 5.4% mIoU at a significantly lower latency, wherein the mIoU (F) and mIoU (B) are improved by ...
- Extensive experiments show that our DMA method produces highly competitive open-vocabulary segmentation performance on various indoor and outdoor tasks.
- When using text supervision only, our method outperforms the text-supervised approach RegionPLC by 9.5%, and even surpasses OpenScene(OpenSeg)-2D3D by 2.6% in terms of mIoU.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we propose a Dense Multimodal Alignment (DMA) framework to densely co-embed different modalities into a common space for maximizing their synergistic benefits.
- Extensive experiments show that our DMA method produces highly competitive open-vocabulary segmentation performance on various indoor and outdoor tasks.
- Recent vision-language pre-training models have exhibited remarkable generalization ability in zero-shot recognition tasks.

## Abstract Cue
- Recent vision-language pre-training models have exhibited remarkable generalization ability in zero-shot recognition tasks.
