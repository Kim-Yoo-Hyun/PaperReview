# Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation

- Year/Venue: 2024 / CVPR
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Diffusion, Robotics, Imitation Learning
- Paper link: ./2024/CVPR/2024_CVPR_Hierarchical-Diffusion-Policy-for-Kinematics-Aware-Multi-T/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- This paper introduces Hierarchical Diffusion Policy (HDP), a hierarchical agent for multi-task robotic manipulation.
- HDP factorises a manipulation policy into a hierarchical structure: a high-level task-planning agent which predicts a distant next-best end-effector pose (NBP), and a low-level goal-conditioned diffusion policy which ...
- The factorised policy representation allows HDP to tackle both long-horizon task planning while generating fine-grained low-level actions.

## Core Idea
- To generate context-aware motion trajectories while satisfying robot kinematics constraints, we present a novel kinematicsaware goal-conditioned control agent, Robot Kinematics Diffuser (RK-Diffuser).
- We introduce HDP, a hierarchical agent for robotic manipulation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Empirically, we show that HDP achieves a significantly higher success rate than the state-of-the-art methods in both simulation and real-world.1 1.
- Recent advances in learning next-best-pose (NBP) agents [6, 7, 15–17, 20, 34, 43] have significantly improved 1 Code and videos are available in our project page.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Empirically, we show that HDP achieves a significantly higher success rate than the state-of-the-art methods in both simulation and real-world.1 1.
- To generate context-aware motion trajectories while satisfying robot kinematics constraints, we present a novel kinematicsaware goal-conditioned control agent, Robot Kinematics Diffuser (RK-Diffuser).
- We introduce HDP, a hierarchical agent for robotic manipulation.

## Abstract Cue
- This paper introduces Hierarchical Diffusion Policy (HDP), a hierarchical agent for multi-task robotic manipulation.
