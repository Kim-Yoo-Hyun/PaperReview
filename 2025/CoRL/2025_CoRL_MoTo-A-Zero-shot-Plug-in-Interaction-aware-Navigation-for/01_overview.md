# MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation

- Year/Venue: 2025 / CoRL
- Category: Navigation and Embodied AI
- Tags: Navigation, mobile manipulation, VLM
- Paper link: ./2025/CoRL/2025_CoRL_MoTo-A-Zero-shot-Plug-in-Interaction-aware-Navigation-for/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- We can control the robot by solving an optimization problem that minimizes the distance between the two keypoints and considers several additional constraints, including collision avoidance, smoothness, and ...
- However, the requirements to perform diverse tasks in unstructured environments (e.g., assisting humans in their daily lives) present significant challenges.

## Core Idea
- To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base ...
- Specifically, we propose an interactionaware navigation policy to generate robot docking points for generalized mobile manipulation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional ...
- 5.1 Comparison with State-of-the-art Methods Table 1 demonstrates the performance of MoTo on the OVMM validation set compared to the baseline, decomposing it into four sequential stages: finding ...
- As shown in Table 1, Home-Robot w/ MoTo outperforms Home-Robot (RL), achieving a 3.52% higher overall success rate.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional ...
- Specifically, we propose an interactionaware navigation policy to generate robot docking points for generalized mobile manipulation.
- To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base ...

## Abstract Cue
- : Mobile manipulation is the fundamental challenge for robotics in assisting humans with diverse tasks and environments in everyday life.
