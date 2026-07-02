# Uni3DL: A Unified Model for 3D Vision-Language Understanding

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2024/ECCV/2024_ECCV_Uni3DL-A-Unified-Model-for-3D-Vision-Language-Understandin/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Extending these successes of unified vision-language modeling in the 2D domain to 3D perception tasks remains a formidable challenge.
- This difficulty primarily stems from the substantial architectural differences between 2D and 3D models, along with the limited availability of extensive 3D datasets for pre-training purposes.
- Despite these successes, task-specific models in 3D perception often lack generalizability, constraining their effectiveness across diverse tasks.

## Core Idea
- We present Uni3DL, a unified model for 3D Vision-Language understanding.
- On the BLEU-1 and ROUGE-L scores, our method beats precious STOA methods by a large margin (more than 20%).

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Following the official benchmark, we use 1,201 scenes for training, 312 for validation.
- Uni3DL has been rigorously evaluated across diverse 3D vision-language understanding tasks, including semantic segmentation, object detection, instance ⋆ 4.1 Dataset (12) ScanNet (v2) captures more than 1,500 3D ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present Uni3DL, a unified model for 3D Vision-Language understanding.
- With a unified architecture, our Uni3DL model enjoys seamless task decomposition and substantial parameter sharing across tasks.
- At the core of Uni3DL, a query transformer is designed to learn task-agnostic semantic and mask outputs by attending to 3D visual features, and a task router is ...

## Abstract Cue
- We present Uni3DL, a unified model for 3D Vision-Language understanding.
