# HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion

- Year/Venue: 2026 / ICLR Poster
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, robust locomotion, safety recovery
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://simonlinsx.github.io/HWC_Loco/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- To develop a reliable locomotion policy capable of generalizing from the training to the deployment environment, we propose formulating policy optimization as a robust optimization problem under misspecified ...
- To address this limitation, we propose a high-level planning policy that dynamically selects which policy to activate based on the scenario.
- These limitations significantly influence the scalability of these approaches.

## Core Idea
- In this study, we propose HWCLoco, a robust whole-body control algorithm tailored for humanoid locomotion tasks.
- The robots are commanded to follow randomly sampled velocities within the training distribution while navigating a uniformly mixed terrain comprising flat ground, obstacles, slopes, and stairs.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco’s superior performance across diverse terrains, robot structures, and locomotion tasks under ...
- To demonstrate the robustness of HWC-Loco, we conduct extensive disturbance tests in simulation.
- To evaluate the effectiveness of different components in HWC-Loco, we design a comparison method using an ablation approach as follows: 1) HWC-Loco-l sets α to a lower value, ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this study, we propose HWCLoco, a robust whole-body control algorithm tailored for humanoid locomotion tasks.
- To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco’s superior performance across diverse terrains, robot structures, and locomotion tasks under ...
- However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies between training and ...

## Abstract Cue
- Humanoid robots, capable of assuming human roles in various workplaces, have become essential to embodied intelligence.
