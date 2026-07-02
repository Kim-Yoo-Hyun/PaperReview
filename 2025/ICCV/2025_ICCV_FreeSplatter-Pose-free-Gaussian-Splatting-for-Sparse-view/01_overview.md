# FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, geometry, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_FreeSplatter-Pose-free-Gaussian-Splatting-for-Sparse-view/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- While generalizable reconstruction models address sparse-view reconstruction using learned priors in a feed-forward manner, they still require accurate camera parameters, sidestepping a fundamental challenge in real-world applications.
- However, these approaches fail in sparse-view scenarios where traditional camera calibration techniques like Structure-from-Motion (SfM) struggle due to insufficient image overlaps.
- We introduce FreeSplatter, a scalable feed-forward framework that generates high-quality 3D Gaussians from uncalibrated sparse-view images while estimating camera parameters within seconds.

## Core Idea
- Our approach employs a streamlined transformer architecture where self-attention blocks facilitate information exchange among multi-view image tokens, decoding them into pixel-aligned 3D Gaussian primitives within a unified reference ...
- We introduce FreeSplatter, a scalable feed-forward framework that generates high-quality 3D Gaussians from uncalibrated sparse-view images while estimating camera parameters within seconds.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Remarkably, FreeSplatter outperforms several pose-dependent Large Reconstruction Models (LRMs) by a notable margin while achieving comparable or even better pose estimation accuracy compared to state-of-the-art pose-free reconstruction approach ...
- Introduction Recent breakthroughs in neural scene representation and differentiable rendering, e.g., Neural Radiance Fields (NeRF) and Gaussian Splatting (GS), have demonstrated exceptional multi-view reconstruction quality for densely-captured images ...
- Beyond technical benchmarks, FreeSplatter streamlines text/image-to-3D content creation pipelines, eliminating the complexity of camera pose management while delivering exceptional visual fidelity.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach employs a streamlined transformer architecture where self-attention blocks facilitate information exchange among multi-view image tokens, decoding them into pixel-aligned 3D Gaussian primitives within a unified reference ...
- We introduce FreeSplatter, a scalable feed-forward framework that generates high-quality 3D Gaussians from uncalibrated sparse-view images while estimating camera parameters within seconds.
- Remarkably, FreeSplatter outperforms several pose-dependent Large Reconstruction Models (LRMs) by a notable margin while achieving comparable or even better pose estimation accuracy compared to state-of-the-art pose-free reconstruction approach ...

## Abstract Cue
- Sparse-view reconstruction models typically require precise camera poses, yet obtaining these parameters from sparse-view images remains challenging.
