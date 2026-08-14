# Gallant: Voxel Grid-Based Humanoid Locomotion and Local Navigation across 3-D Constrained Terrains

- Year/Venue: 2026 / CVPR
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, perceptive locomotion, LiDAR, 3D navigation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://gallantloco.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- However, existing perception modules, mainly based on depth images or elevation maps, offer only partial and locally flattened views of the environment, failing to capture the full 3D ...
- While recent systems have progressed from lab prototypes to real-world deployment , ensuring operational safety remains a key challenge.
- Existing perception modules, such as those based on depth images or elevation maps, provide only partial and locally flattened views of the environment, limiting the robot’s understanding of ...

## Core Idea
- We introduce Gallant, a voxel-grid–based perceptive learning framework for humanoid locomotion and local navigation in 3D constrained environments.
- This requires a perception architecture that enables anticipatory collision checking, clearance-aware motion generation, and planning of contact-rich maneuvers.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Gallant also firstly achieves over-90% success rates in challenging scenarios such as stair climbing and stepping onto elevated platforms through improved end-to-end optimization.
- Experimental results show that Gallant’s broader perceptual coverage facilitates the use of a single policy that goes beyond the limitations of previous methods confined to ground-level obstacles, extending ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results show that Gallant’s broader perceptual coverage facilitates the use of a single policy that goes beyond the limitations of previous methods confined to ground-level obstacles, extending ...
- Gallant also firstly achieves over-90% success rates in challenging scenarios such as stair climbing and stepping onto elevated platforms through improved end-to-end optimization.
- This requires a perception architecture that enables anticipatory collision checking, clearance-aware motion generation, and planning of contact-rich maneuvers.

## Abstract Cue
- Robust humanoid locomotion requires accurate and globally consistent perception of the surrounding 3D environment.
