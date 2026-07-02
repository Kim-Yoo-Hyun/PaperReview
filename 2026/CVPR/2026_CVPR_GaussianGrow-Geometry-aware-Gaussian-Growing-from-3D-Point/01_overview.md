# GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, point cloud, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_GaussianGrow-Geometry-aware-Gaussian-Growing-from-3D-Point/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing methods have explored predicting point maps as geometric references for inferring Gaussian primitives, while the unreliable estimated geometries may lead to poor generations.
- 3D Gaussian Splatting has demonstrated superior performance in rendering efficiency and quality, yet the generation of 3D Gaussians still remains a challenge without proper geometric priors.

## Core Idea
- Our method leverages a text-guided multiview diffusion model for appearance synthesis while constraining novel views to reduce fusion artifacts.
- For com- pleting the hard-to-observe regions, we propose to iteratively detect the camera pose by observing the largest ungrown regions in point clouds and inpainting them by inpainting ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 3D Gaussian Splatting has demonstrated superior performance in rendering efficiency and quality, yet the generation of 3D Gaussians still remains a challenge without proper geometric priors.
- We extensively evaluate GaussianGrow on textguided Gaussian generation from synthetic and even realscanned point clouds.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- For com- pleting the hard-to-observe regions, we propose to iteratively detect the camera pose by observing the largest ungrown regions in point clouds and inpainting them by inpainting ...
- In this work, we introduce GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily accessible 3D point clouds, naturally enforcing geometric accuracy ...
- 3D Gaussian Splatting has demonstrated superior performance in rendering efficiency and quality, yet the generation of 3D Gaussians still remains a challenge without proper geometric priors.

## Abstract Cue
- 3D Gaussian Splatting has demonstrated superior performance in rendering efficiency and quality, yet the generation of 3D Gaussians still remains a challenge without proper geometric priors.
