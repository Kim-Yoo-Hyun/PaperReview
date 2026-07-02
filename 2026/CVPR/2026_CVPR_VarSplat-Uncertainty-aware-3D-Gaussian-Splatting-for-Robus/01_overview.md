# VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_VarSplat-Uncertainty-aware-3D-Gaussian-Splatting-for-Robus/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite these advances, a key limitation exists: measurement reliability is rarely modeled explicitly.
- However, existing 3DGS-SLAM approaches handle measurement reliability implicitly, making pose estimation and global alignment susceptible to drift in lowtexture regions, transparent surfaces, or areas with complex reflectance properties.
- 3D Gaussian Splatting (3DGS) further addresses this bottleneck by rasterizing anisotropic Gaussians with alpha compositing, enabling fast, differentiable rendering.

## Core Idea
- To this end, we introduce VarSplat, an uncertainty-aware 3DGS-SLAM system that explicitly learns per-splat appearance variance.
- Simultaneous Localization and Mapping (SLAM) with 3D Gaussian Splatting (3DGS) enables fast, differentiable rendering and high-fidelity reconstruction across diverse realworld scenes.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Ex- perimental results on Replica (synthetic) and TUM-RGBD, ScanNet, and ScanNet++ (real-world) show that VarSplat improves robustness and achieves competitive or superior tracking, mapping, and novel view synthesis ...
- Classical methods based on voxels, TSDFs, surfels, or meshes can achieve real-time tracking and mapping but struggle to capture photorealistic appearance.
- To improve visual fidelity, Neural radiance fields (NeRF) have been integrated into SLAM systems , though implicit volumetric rendering remains costly for real-time performance.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Ex- perimental results on Replica (synthetic) and TUM-RGBD, ScanNet, and ScanNet++ (real-world) show that VarSplat improves robustness and achieves competitive or superior tracking, mapping, and novel view synthesis ...
- To this end, we introduce VarSplat, an uncertainty-aware 3DGS-SLAM system that explicitly learns per-splat appearance variance.
- 3D Gaussian Splatting (3DGS) further addresses this bottleneck by rasterizing anisotropic Gaussians with alpha compositing, enabling fast, differentiable rendering.

## Abstract Cue
- Simultaneous Localization and Mapping (SLAM) with 3D Gaussian Splatting (3DGS) enables fast, differentiable rendering and high-fidelity reconstruction across diverse realworld scenes.
