# Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction

- Year/Venue: 2026 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Gau-Occ-Geometry-Completed-Gaussians-for-Multi-Modal-3D-Oc/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite notable progress, two main challenges remain: (i) raw point clouds are sparse and occlusion-biased, capturing mostly visible surfaces while missing many occupied but unobserved regions, limiting the ...
- While promising, existing Gaussian-based approaches are predominantly vision-only, and their application to multimodal occupancy prediction remains underexplored, particularly under real-world constraints such as sparse LiDAR sampling and limited ...
- To ensure geometric completeness, we propose a LiDAR Completion Diffuser (LCD) that recovers missing structures from sparse LiDAR to initialize robust Gaussian anchors.

## Core Idea
- To ensure geometric completeness, we propose a LiDAR Completion Diffuser (LCD) that recovers missing structures from sparse LiDAR to initialize robust Gaussian anchors.
- We present Gau-Occ, a multi-modal framework that bypasses dense volumetric processing by modeling the scene as a compact collection of semantic 3D Gaussians.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments across challenging benchmarks demonstrate that Gau-Occ achieves state-of-the-art performance with significant computational efficiency. semantic information.
- While multi-modal fusion improves accuracy over vision-only methods, it typically relies on computationally expensive dense voxel or BEV tensors.
- Recent advances in 3D Gaussian primitives demonstrate that such representations can model scene geometry and semantics with high expressiveness from multi-view observations .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments across challenging benchmarks demonstrate that Gau-Occ achieves state-of-the-art performance with significant computational efficiency. semantic information.
- To ensure geometric completeness, we propose a LiDAR Completion Diffuser (LCD) that recovers missing structures from sparse LiDAR to initialize robust Gaussian anchors.
- We present Gau-Occ, a multi-modal framework that bypasses dense volumetric processing by modeling the scene as a compact collection of semantic 3D Gaussians.

## Abstract Cue
- 3D semantic occupancy prediction is crucial for autonomous driving.
