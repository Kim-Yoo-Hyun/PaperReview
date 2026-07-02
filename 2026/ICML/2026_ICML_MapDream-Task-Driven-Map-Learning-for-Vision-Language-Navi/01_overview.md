# MapDream: Task-Driven Map Learning for Vision-Language Navigation

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: Vision-Language Model, Navigation
- Paper link: ./2026/ICML/2026_ICML_MapDream-Task-Driven-Map-Learning-for-Vision-Language-Navi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, most existing approaches rely on hand-crafted maps constructed independently of the navigation policy.
- A central difficulty of VLN is partial observability.
- Agents perceive the environment only through local, sequential observations, which limits their understanding of the space.

## Core Idea
- Based on this insight, we propose MapDream, a map-in-the-loop framework that formulates map construction as autoregressive bird’seye-view (BEV) image synthesis.
- Supervised pretraining bootstraps a reliable mapping-to-control interface, while the autoregressive design enables end-to-end joint optimization through reinforcement fine-tuning.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on R2RCE and RxR-CE achieve state-of-the-art monocular performance, validating task-driven generative map learning.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments on R2RCE and RxR-CE achieve state-of-the-art monocular performance, validating task-driven generative map learning.
- Based on this insight, we propose MapDream, a map-in-the-loop framework that formulates map construction as autoregressive bird’seye-view (BEV) image synthesis.
- Supervised pretraining bootstraps a reliable mapping-to-control interface, while the autoregressive design enables end-to-end joint optimization through reinforcement fine-tuning.

## Abstract Cue
- Module Vision-Language Navigation (VLN) requires agents to follow natural language instructions in partially observed 3D environments, motivating map representations that aggregate spatial context beyond local perception.
