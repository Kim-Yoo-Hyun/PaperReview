# Geometry-aware RL for Manipulation of Varying Shapes and Deformable Objects

- Year/Venue: 2025 / ICLR Oral
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, SE(3) equivariance, deformable manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://thobotics.github.io/hepi
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- These tasks present a range of manipulation challenges, emphasizing the role of geometric structure and requiring complex exploration strategies to coordinate the agents in completing the tasks.

## Core Idea
- We introduce two categories of tasks: rigid manipulation on diverse geometries and deformable object manipulation, all implemented in NVIDIA IsaacLab (Mittal et al., 2023) to leverage its GPU-based ...
- Finally, we introduce Cloth-Hanging, where four actuators control the corners of a cloth to hang it onto a hanger, with randomized starting positions and orientations in 3D space.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- A video showcasing the tasks can be found in the supplementary material.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We introduce two categories of tasks: rigid manipulation on diverse geometries and deformable object manipulation, all implemented in NVIDIA IsaacLab (Mittal et al., 2023) to leverage its GPU-based ...
- Additionally, we introduce a novel Rigid-Insertion-Two-Agents task, where two linear actuators work together to control an object, guiding it to a target randomly positioned in the upper hemisphere ...
- Finally, we introduce Cloth-Hanging, where four actuators control the corners of a cloth to hang it onto a hanger, with randomized starting positions and orientations in 3D space.

## Abstract Cue
- away the specifics of the robot body and consider only end-effector control.
