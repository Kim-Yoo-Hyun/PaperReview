# LSSInst: Improving Geometric Modeling in LSS-Based BEV Perception with Instance Representation

- Year/Venue: 2025 / 3DV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_LSSInst-Improving-Geometric-Modeling-in-LSS-Based-BEV-Perc/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The proposed detector exploits fine-grained pixel-level features that can be flexibly integrated into existing LSS-based BEV networks.

## Core Idea
- With this in mind, to compensate for the missing details and utilize multi-view geometry constraints, we propose LSSInst, a two-stage object detector incorporating BEV and instance representations in ...
- Param (M) Training Cost (min/epoch) Inference Cost (sec/frame) 0.758 0.658 55.7 64.0 14 18 0.04 0.05 0.281 0.275 0.610 0.492 83.5 91.8 11 13 0.10 0.11 0.675 0.658 ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrated that our proposed framework is of excellent generalization ability and performance, which boosts the performances of modern LSS-based BEV perception methods without bells and whistles ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrated that our proposed framework is of excellent generalization ability and performance, which boosts the performances of modern LSS-based BEV perception methods without bells and whistles ...
- With this in mind, to compensate for the missing details and utilize multi-view geometry constraints, we propose LSSInst, a two-stage object detector incorporating BEV and instance representations in ...
- With the attention gained by camera-only 3D object detection in autonomous driving, methods based on Bird-EyeView (BEV) representation especially derived from the forward view transformation paradigm, i.e., lift-splat-shoot ...

## Abstract Cue
- With the attention gained by camera-only 3D object detection in autonomous driving, methods based on Bird-EyeView (BEV) representation especially derived from the forward view transformation paradigm, i.e., lift-splat-shoot (LSS), have recently seen significant progress.
