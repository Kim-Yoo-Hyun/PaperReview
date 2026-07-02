# 3D Gaussian Splatting for Real-Time Radiance Field Rendering

- Year/Venue: 2023 / SIGGRAPH
- Category: Foundations: 3D Scene Representations
- Tags: Gaussian Splatting, 3D reconstruction, representation
- Paper link: ./2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/paper.pdf
- Code/Project: https://github.com/graphdeco-inria/gaussian-splatting
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- While the continuous nature of these methods helps optimization, the stochastic sampling required for rendering is costly and can result in noise.
- 2006] and initialize the set of 3D Gaussians with the sparse point cloud produced for free as part of the SfM process.

## Core Idea
- We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive training times, while ...
- The second component of our method is optimization of the properties of the 3D Gaussians – 3D position, opacity 𝛼, anisotropic covariance, and spherical harmonic (SH) coefficients – ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Limitation
- Comparison of failure artifacts: Mip-NeRF360 has “floaters” and grainy appearance (left, foreground), while our method produces coarse, anisoptropic Gaussians resulting in low-detail visuals (right, background).
- Our method is not without limitations.
- This could be addressed by antialiasing, which we leave as future work.

## Contribution
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Abstract Cue
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
