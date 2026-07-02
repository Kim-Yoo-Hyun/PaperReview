# PointVLA: Injecting the 3D World into Vision-Language-Action Models

- Year/Venue: 2026 / RA-L
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, 3D Vision, Reinforcement Learning
- Paper link: ./2026/RA-L/2026_RA-L_PointVLA-Injecting-the-3D-World-into-Vision-Language-Actio/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Retraining these models with 3D data is computationally prohibitive, while discarding existing 2D datasets wastes valuable resources.
- Therefore, it is essential to explore novel frameworks that can integrate additional 3D input into pre-existing foundation robot models, a research area that has not been underexplored in ...

## Core Idea
- To bridge this gap, we propose PointVLA, a framework that enhances pre-trained VLAs with point cloud inputs without requiring retraining.
- We compare our method against Diffusion Policy and 3D Diffusion Policy (DP3) .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that PointVLA outperforms state-of-the-art 2D imitation learning methods, such as OpenVLA , Diffusion Policy and DexVLA , across both simulated and real-world robotic Vision-Language-Action (VLA) ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that PointVLA outperforms state-of-the-art 2D imitation learning methods, such as OpenVLA , Diffusion Policy and DexVLA , across both simulated and real-world robotic Vision-Language-Action (VLA) ...
- To bridge this gap, we propose PointVLA, a framework that enhances pre-trained VLAs with point cloud inputs without requiring retraining.
- Retraining these models with 3D data is computationally prohibitive, while discarding existing 2D datasets wastes valuable resources.

## Abstract Cue
- the vanilla action expert and injects 3D features via a lightweight modular block.
