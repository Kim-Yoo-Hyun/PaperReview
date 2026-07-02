# 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation

- Year/Venue: 2025 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, 3D Vision, Robotics
- Paper link: ./2025/CoRL/2025_CoRL_3DS-VLA-A-3D-Spatial-Aware-Vision-Language-Action-Model-fo/paper.pdf
- Code/Project: https://vis-www.cs.umass.edu/3ds-vla/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image observations .
- Yet, robotic manipulation requires intricate environmental interactions, and such methods often lack a broader understanding of the robot’s action with its surroundings in terms of spatial and temporal.
- The constraints construct dynamic affordance conditions from sequential keypoints, explicitly encoding “where” and “when” the robot should interact with the environment.

## Core Idea
- 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1 , . . . , τN } of N expert demonstrations, each demonstration τ is paired ...
- To address this, we propose 3DS-VLA, which enhances pretrained 2D vision-language models (VLMs) with comprehensive 3D awareness, enabling the prediction of robust end-effector poses.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments in simulation and real world demonstrate that 3DS-VLA outperforms previous state-of-the-art policies and showcase its generalizable capabilities across multi-task, multi-embodiment, and diverse environmental settings.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments in simulation and real world demonstrate that 3DS-VLA outperforms previous state-of-the-art policies and showcase its generalizable capabilities across multi-task, multi-embodiment, and diverse environmental settings.
- To address this, we propose 3DS-VLA, which enhances pretrained 2D vision-language models (VLMs) with comprehensive 3D awareness, enabling the prediction of robust end-effector poses.
- Specifically, we enable the 2D vision encoder of the VLMs to encode both 2D images and 3D spatial observation by introducing a 2D-to-3D positional alignment mechanism.

## Abstract Cue
- : Recently, 2D vision-language-action (VLA) models have made significant strides in multi-task manipulation.
