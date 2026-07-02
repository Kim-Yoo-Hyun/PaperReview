# SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving

- Year/Venue: 2025 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_SplatAD-Real-Time-Lidar-and-Camera-Rendering-with-3D-Gauss/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address these limitations, we propose SplatAD, the first 3DGS-based method for realistic, real-time rendering of dynamic scenes for both camera and lidar data.
- Nevertheless, 3DGS-based methods for the AD setting inherit the limitation of only being able to render camera data, overlooking the lidar modality.
- However, existing neural radiance field (NeRF) methods for sensor-realistic rendering of camera and lidar data suffer from low rendering speeds, limiting their applicability for large-scale testing.

## Core Idea
- To address these limitations, we propose SplatAD, the first 3DGS-based method for realistic, real-time rendering of dynamic scenes for both camera and lidar data.
- While 3D Gaussian Splatting (3DGS) enables real-time rendering, current methods are limited to camera data and are unable to render lidar data essential for autonomous driving.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 3DGS provides an attractive alternative to NeRFs, as its accelerated rendering achieves comparable image realism while increasing inference speeds by an order of magnitude.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address these limitations, we propose SplatAD, the first 3DGS-based method for realistic, real-time rendering of dynamic scenes for both camera and lidar data.
- Motivated by this, a multitude of methods have emerged based on neural radiance fields (NeRFs) and 3D Gaussian Splatting (3DGS) .
- While 3D Gaussian Splatting (3DGS) enables real-time rendering, current methods are limited to camera data and are unable to render lidar data essential for autonomous driving.

## Abstract Cue
- Introduction Large-scale testing is essential to ensure the safety of autonomous robots, such as self-driving vehicles (SDVs), before real-world deployment.
