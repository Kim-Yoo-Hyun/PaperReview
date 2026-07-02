# LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model

- Year/Venue: 2026 / ICML Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_LaST-0-Latent-Spatio-Temporal-Chain-of-Thought-for-Robotic/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- propose LaST0 , a framework that enables efficient reasoning before acting through a Latent Spatio-Temporal Chain-of-Thought (CoT), capturing fine-grained physical and robotic dynamics that are often difficult to ...
- Moreover, such reasoning is confined to the linguistic space, imposing a representational bottleneck that struggles to faithfully capture ineffable physical attributes.

## Core Idea
- Specifically, we introduce a token-efficient latent CoT space that models future visual dynamics, 3D structural information, and robot proprioceptive states, and further extends these representations across time to ...
- Furthermore, LaST0 adopts a dualsystem architecture implemented via a Mixtureof-Transformers design, where a reasoning expert conducts low-frequency latent inference and an acting expert generates high-frequency actions conditioned on ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Across 10 real-world tasks spanning tabletop, mobile, and dexterous hand manipulation, LaST0 improves mean success rates by 13%, 14% and 14% over prior state-of-the-art VLA methods, respectively.
- Project page: https://vla-last0.github.io/ Vision-Language-Action (VLA) models have recently shown strong generalization, with some approaches seeking to explicitly generate linguistic reasoning traces or predict future observations prior to execution.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Furthermore, LaST0 adopts a dualsystem architecture implemented via a Mixtureof-Transformers design, where a reasoning expert conducts low-frequency latent inference and an acting expert generates high-frequency actions conditioned on ...
- Across 10 real-world tasks spanning tabletop, mobile, and dexterous hand manipulation, LaST0 improves mean success rates by 13%, 14% and 14% over prior state-of-the-art VLA methods, respectively.
- Specifically, we introduce a token-efficient latent CoT space that models future visual dynamics, 3D structural information, and robot proprioceptive states, and further extends these representations across time to ...

## Abstract Cue
- propose LaST0 , a framework that enables efficient reasoning before acting through a Latent Spatio-Temporal Chain-of-Thought (CoT), capturing fine-grained physical and robotic dynamics that are often difficult to verbalize.
