# RVT: Robotic View Transformer for 3D Object Manipulation

- Year/Venue: 2023 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D manipulation, Transformer
- Paper link: ./2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/paper.pdf
- Code/Project: https://robotic-view-transformer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing stateof-the-art ...
- But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability.

## Core Idea
- In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate.
- The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state (open or closed).

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- To achieve the target gripper pose, we generate joint space actions by using the same sampling-based motion planner as in .
- It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct.
- We compare with two variants with CNN and ViT vision encoders respectively. (2) C2F-ARM-BC is a behavior cloning agent that converts the RGB-D images into multi-resolution voxels and ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate.
- Visual results, code, and trained model are provided at: https://robotic-view-transformer.github.io/.
- Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace.

## Abstract Cue
- : For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images.
