# From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors

- Year/Venue: 2026 / ICLR Poster
- Category: 3D Vision-Language Grounding
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Paper link: ./2026/ICLR/2026_ICLR_From-Spatial-to-Actions-Grounding-Vision-Language-Action-M/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- These designs enable FALCON to address limitations in spatial representation, modality transferability, and alignment.
- A BSTRACT Existing vision-language-action (VLA) models act in 3D real-world but are typically built on 2D encoders, leaving a spatial reasoning gap that limits generalization and adaptability.
- Recent 3D integration techniques for VLAs either require specialized sensors and transfer poorly across modalities, or inject weak cues that lack geometry and degrade vision-language alignment.

## Core Idea
- In this work, we introduce FALCON (From Spatial to Action), a novel paradigm that injects rich 3D spatial tokens into the action head.
- In contrast, our method exhibits strong robustness to scale variations, avoiding these issues and achieving the highest success rates in both scenarios.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In comprehensive evaluations across three simulation benchmarks and eleven real-world tasks, our proposed FALCON achieves state-of-the-art performance, consistently surpasses competitive baselines, and remains robust under clutter, spatial-prompt conditioning, ...
- The model achieves state-of-the-art performance across a diverse range of benchmark evaluations.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In comprehensive evaluations across three simulation benchmarks and eleven real-world tasks, our proposed FALCON achieves state-of-the-art performance, consistently surpasses competitive baselines, and remains robust under clutter, spatial-prompt conditioning, ...
- The model achieves state-of-the-art performance across a diverse range of benchmark evaluations.
- In this work, we introduce FALCON (From Spatial to Action), a novel paradigm that injects rich 3D spatial tokens into the action head.

## Abstract Cue
- spatial instructions, and strong few-shot generalizability in real-world scenes.
