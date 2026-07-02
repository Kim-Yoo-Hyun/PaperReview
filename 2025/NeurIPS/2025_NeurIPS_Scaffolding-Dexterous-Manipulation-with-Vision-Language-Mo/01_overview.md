# Scaffolding Dexterous Manipulation with Vision-Language Models

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Scaffolding-Dexterous-Manipulation-with-Vision-Language-Mo/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite the intrinsic advantages of dexterous hands over simpler end-effectors, existing learning paradigms have struggled to cope with their complexity .
- Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control.
- However, sourcing suitable trajectories—particularly for dexterous hands—remains a significant challenge.

## Core Idea
- Given a task description (e.g., “open the cabinet”) and a visual scene, our method uses an off-the-shelf VLM to first identify task-relevant keypoints (e.g., handles, buttons) and then ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Thus, we mainly focus our experiments on comparison with a variety of oracles and ablations: • Iterative Keypoint Rewards (IKER): We implement Iterative Keypoint Rewards , in which ...
- We run 20 trials for each configuration for a total of 2000 evaluation episodes and average results across three seeds.
- 1 We conduct a comprehensive suite of experiments to assess the effectiveness, generality, and robustness of our method across a diverse range of dexterous manipulation tasks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies.
- Moreover, we showcase that our method transfers to realworld robotic hands without any human demonstrations or handcrafted rewards.
- Given a task description (e.g., “open the cabinet”) and a visual scene, our method uses an off-the-shelf VLM to first identify task-relevant keypoints (e.g., handles, buttons) and then ...

## Abstract Cue
- Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control.
