# HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_HiMe-Hierarchical-Embodied-Memory-for-Long-Horizon-Vision/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing solutions face a “frequency-competence paradox,” where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities.
- HiMe addresses this challenge by organizing embodied intelligence into a hierarchical structure that separates fast execution from memory-driven reasoning over long time scales. tion with large-scale internet-level pretraining.
- This inherent limitation prevents them from maintaining a persistent belie

## Core Idea
- To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry for working memory, ...
- Most existing architectures rely on the Markov assumption, where the policy is conditioned only on the transient observation at the current time step.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments demonstrate that this approach not only outperforms flat memory baselines but also exhibits the novel ability to selfcorrect its internal knowledge based on human preferences.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments demonstrate that this approach not only outperforms flat memory baselines but also exhibits the novel ability to selfcorrect its internal knowledge based on human preferences.
- HiMe addresses this challenge by organizing embodied intelligence into a hierarchical structure that separates fast execution from memory-driven reasoning over long time scales. tion with large-scale internet-level pretraining.
- Most existing architectures rely on the Markov assumption, where the policy is conditioned only on the transient observation at the current time step.

## Abstract Cue
- Episode Memory Text memory: Alice’s toy is a duck Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate observations.
