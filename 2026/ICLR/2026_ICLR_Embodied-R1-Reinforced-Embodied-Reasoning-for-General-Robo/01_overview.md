# Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation

- Year/Venue: 2026 / ICLR Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2026/ICLR/2026_ICLR_Embodied-R1-Reinforced-Embodied-Reasoning-for-General-Robo/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In blackboard wiping, Embodied-R1’s visual traces were executed via an impedance controller to maintain consistent contact force.

## Core Idea
- C ONCLUSION We introduce Embodied-R1, an embodied reasoning VLM that bridges the critical “seeing-to-doing” gap in robotic manipulation.
- To dissect our training paradigm, we compared RL against SFT and analyzed the impact of an explicit reasoning process.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- F, we provide further experiments, including an analysis of integration with learning-based methods, an ablation study on the benefits of mixed training, and results using RGB-D inputs.
- 6 show that RL-based models consistently outperform their SFT counterparts, highlighting the crucial role of RL in OOD generalization.
- It can be seen that Embodied-R1 achieves accurate visual trajectory prediction across various scenarios.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- F, we provide further experiments, including an analysis of integration with learning-based methods, an ablation study on the benefits of mixed training, and results using RGB-D inputs.
- 6 show that RL-based models consistently outperform their SFT counterparts, highlighting the crucial role of RL in OOD generalization.
- C ONCLUSION We introduce Embodied-R1, an embodied reasoning VLM that bridges the critical “seeing-to-doing” gap in robotic manipulation.

## Abstract Cue
- reasoning and spatial grounding. (3) Contact-Rich Manipulation: Embodied-R1 serves as a flexible interface that decouples high-level perception from low-level dynamics.
