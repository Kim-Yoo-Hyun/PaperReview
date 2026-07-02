# VLA-Reasoner: Empowering Vision-Language-Action Models with Reasoning Via Online Monte Carlo Tree Search

- Year/Venue: 2026 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Reinforcement Learning
- Paper link: ./2026/ICRA/2026_ICRA_VLA-Reasoner-Empowering-Vision-Language-Action-Models-with/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address this problem, we propose a plug-in framework named VLA-Reasoner that effectively empowers off-the-shelf VLAs with the capability of foreseeing future states via test-time scaling.
- However, existing VLAs are limited to predicting short-sighted next-action, which struggle with long-horizon trajectory tasks due to incremental deviations.

## Core Idea
- To address this problem, we propose a plug-in framework named VLA-Reasoner that effectively empowers off-the-shelf VLAs with the capability of foreseeing future states via test-time scaling.
- This raises a core question: “Can VLAs explore the longhorizon future influence of actions at test time, and decide the optimal action?” To this end, we propose a ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We conducted extensive experiments in both simulators and the real world, demonstrating that our proposed VLA-Reasoner achieves significant improvements over the state-of-the-art VLAs.
- — Vision-Language-Action models (VLAs) achieve strong performance in general robotic manipulation tasks by scaling imitation learning.
- We further leverage Monte Carlo Tree Search (MCTS) to improve search efficiency in large action spaces, where stepwise VLA predictions seed the root.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We conducted extensive experiments in both simulators and the real world, demonstrating that our proposed VLA-Reasoner achieves significant improvements over the state-of-the-art VLAs.
- To address this problem, we propose a plug-in framework named VLA-Reasoner that effectively empowers off-the-shelf VLAs with the capability of foreseeing future states via test-time scaling.
- This raises a core question: “Can VLAs explore the longhorizon future influence of actions at test time, and decide the optimal action?” To this end, we propose a ...

## Abstract Cue
- — Vision-Language-Action models (VLAs) achieve strong performance in general robotic manipulation tasks by scaling imitation learning.
