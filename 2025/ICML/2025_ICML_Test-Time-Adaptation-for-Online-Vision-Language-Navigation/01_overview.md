# Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning

- Year/Venue: 2025 / ICML Poster
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation, Reinforcement Learning
- Paper link: ./2025/ICML/2025_ICML_Test-Time-Adaptation-for-Online-Vision-Language-Navigation/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- One existing approach (Gao et al., 2024a) relies on the widely adopted TTA paradigm of entropy minimization (Wang et al., 2020a; Zhang et al., 2022), where we identify ...
- Navigating in an unfamiliar environment during deployment poses a critical challenge for a vision-language navigation (VLN) agent.
- Specifically, F EED TTA learns by maximizing binary episodic feedback, a practical setup in which the agent receives a binary scalar after each episode that indicates the success ...

## Core Idea
- Additionally, we propose a gradient regularization technique that leverages the binary structure of F EED TTA to achieve a balance between plasticity and stability during adaptation.
- Experiments In this section, we present experimental results of our study.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our extensive experiments on challenging VLN benchmarks demonstrate the superior adaptability of F EED TTA, even outperforming the stateof-the-art offline training methods in REVERIE benchmark with a single ...
- Additionally, we propose a gradient regularization technique that leverages the binary structure of F EED TTA to achieve a balance between plasticity and stability during adaptation.
- The simplicity and efficacy of the FeedTTA framework demonstrate its potential for practical applications in real-world navigation scenarios. via imitation learning on a vast collection of annotated expert ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our extensive experiments on challenging VLN benchmarks demonstrate the superior adaptability of F EED TTA, even outperforming the stateof-the-art offline training methods in REVERIE benchmark with a single ...
- Additionally, we propose a gradient regularization technique that leverages the binary structure of F EED TTA to achieve a balance between plasticity and stability during adaptation.
- To address this, we introduce F EED TTA, a novel TTA framework for online VLN utilizing feedback-based reinforcement learning.

## Abstract Cue
- Navigating in an unfamiliar environment during deployment poses a critical challenge for a vision-language navigation (VLN) agent.
