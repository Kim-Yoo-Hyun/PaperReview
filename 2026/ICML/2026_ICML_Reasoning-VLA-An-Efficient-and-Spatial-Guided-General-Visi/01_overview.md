# Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision, Reinforcement Learning
- Paper link: ./2026/ICML/2026_ICML_Reasoning-VLA-An-Efficient-and-Spatial-Guided-General-Visi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- These limitations hinder their generalization ability to new driving scenarios.
- However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios.
- Building on these advancements, contemporary frameworks in robotic manipulation and autonomous driving increasingly adopt vision–language generative paradigms (e.g., autoregressive or diffusion-based models (Black et al., 2024; Kim et ...

## Core Idea
- These results indicate that our approach provides significant improvements in open-loop evaluation, highlighting the strong generalization capability of the Reasoning-VLA architecture.
- In this paper, we propose Reasoning-VLA, a general and efficient action-generation VLA framework.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves stateof-the-art performance, strong generalization capability, and the excellent inference speed ...
- Leveraging large-scale pretrained foundation models, recent approaches such as DriveMOE (Yang et al., 2025) have achieved strong benchmark performance while simultaneously improving interpretability and robustness capabilities in autonomous ...
- Despite these promising results, se

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves stateof-the-art performance, strong generalization capability, and the excellent inference speed ...
- Recently, foundation models—especially large language and vision–language models like CLIP, Qwen2.5-VL, and DeepSeek-V3 (Radford et al., 2021; Bai et al., 2025; Liu et al., 2025)—have shown remarkable generalization ...
- In this paper, we propose Reasoning-VLA, a general and efficient action-generation VLA framework.

## Abstract Cue
- as poor scalability, cumulative errors, and limited generalization across hardware and datasets.
