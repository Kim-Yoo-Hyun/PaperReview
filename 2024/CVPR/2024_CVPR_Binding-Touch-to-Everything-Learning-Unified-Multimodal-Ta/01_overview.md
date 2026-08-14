# Binding Touch to Everything: Learning Unified Multimodal Tactile Representations

- Year/Venue: 2024 / CVPR
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, tactile sensing, Vision-Language, multimodal representation, open-vocabulary
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://cfeng16.github.io/UniTouch/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- However, multimodal learning with touch remains challenging due to the expensive data collection process and nonstandardized sensor outputs.

## Core Idea
- We use the same architectures to ensure a fair comparison.
- We use L = 5 learnable tokens for each sensor type in our pretraining datasets with K = 3 different sensors.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We achieve this by aligning our UniTouch embeddings to pretrained image embeddings already associated with a variety of other modalities.
- To the best of our knowledge, UniTouch is the first to demonstrate such capabilities.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We introduce UniTouch, a unified tactile model for vision-based touch sensors connected to multiple modalities, including vision, language, and sound.
- We achieve this by aligning our UniTouch embeddings to pretrained image embeddings already associated with a variety of other modalities.
- To the best of our knowledge, UniTouch is the first to demonstrate such capabilities.

## Abstract Cue
- To the best of our knowledge, UniTouch is the first to demonstrate such capabilities.
