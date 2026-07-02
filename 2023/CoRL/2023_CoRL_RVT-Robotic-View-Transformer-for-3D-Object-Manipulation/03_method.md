# Method

- Year/Venue: 2023 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, 3D manipulation, Transformer
- Paper link: ./2023/CoRL/2023_CoRL_RVT-Robotic-View-Transformer-for-3D-Object-Manipulation/paper.pdf
- Code/Project: https://robotic-view-transformer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate.
- The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state (open or closed).
- Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace.

## 원리적 동기
- In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing stateof-the-art ...
- But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability.
- In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate.

## 핵심 방법론
- The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state (open or closed).
