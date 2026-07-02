# VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians

- Year/Venue: 2025 / ICML Poster
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICML/2025_ICML_VTGaussian-SLAM-RGBD-SLAM-for-Large-Scale-Scenes-with-Spla/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- SLAM methods resolve the computational problem of mapping unknown environments while tracking camera locations.

## Core Idea
- To resolve this issue, we propose novel tracking and mapping strategies to work with a novel 3D representation, dubbed view-tied 3D Gaussians, for RGBD SLAM systems.
- We compare our method with the latest RGBD SLAM methods, including NeRF-based RGBD SLAM methods: NICE-SLAM (Zhu et al., 2022), VoxFusion (Yang et al., 2022), ESLAM (Johari et ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- State-of-the-art methods employ 3D Gaussians to represent a scene, and render these Gaussians through splatting for higher efficiency and better rendering.
- We justify the effectiveness of these designs, and report better performance over the latest methods on the widely used benchmarks in terms of rendering and tracking accuracy and ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To resolve this issue, we propose novel tracking and mapping strategies to work with a novel 3D representation, dubbed view-tied 3D Gaussians, for RGBD SLAM systems.
- Moreover, our strategies remove the need of maintaining all Gaussians learnable throughout the training, while improving rendering quality, and tracking accuracy.
- However, these methods cannot scale up to extremely large scenes, due to the inefficient tracking and mapping strategies that need to optimize all 3D Gaussians in the limited ...

## Abstract Cue
- Introduction SLAM is an important task in computer vision (Keetha et al., 2024; Zhu et al., 2022), 3D reconstruction (Wang et al., 2023; Hu & Han, 2023), and robotics (Adamkiewicz et al., 2022).
