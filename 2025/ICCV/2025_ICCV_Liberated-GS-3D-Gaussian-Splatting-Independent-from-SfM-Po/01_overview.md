# Liberated-GS: 3D Gaussian Splatting Independent from SfM Point Clouds

- Year/Venue: 2025 / ICCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: Gaussian Splatting, geometry, point cloud, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Liberated-GS-3D-Gaussian-Splatting-Independent-from-SfM-Po/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address this limitation, we propose a novel initialization pipeline, achieving highfidelity reconstruction from dense image sequences without relying on SfM-derived point clouds.
- While 3DGS effectively addresses the slow rendering problem caused by radiance fields, it introduces additional input requirements.
- However, it heavily relies on high-quality initial sparse points from Structure-from-Motion (SfM), which often struggles in textureless regions, degrading the geometry and visual quality of 3DGS.

## Core Idea
- Then, we introduce a progressive segmented initialization process that leverages both local and global Gaussians to construct a coarse solution.
- To address this limitation, we propose a novel initialization pipeline, achieving highfidelity reconstruction from dense image sequences without relying on SfM-derived point clouds.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Notably, our method outperforms the SfM-based method by a 14.4% improvement in LPIPS on 1.
- Extensive experiments demonstrate the superiority of our method over previous approaches and its compatibility with other advanced 3D Gaussian models.
- the Mip-NeRF360 datasets and a 30.7% improvement on the Tanks and Temples datasets.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate the superiority of our method over previous approaches and its compatibility with other advanced 3D Gaussian models.
- Notably, our method outperforms the SfM-based method by a 14.4% improvement in LPIPS on 1.
- To address this limitation, we propose a novel initialization pipeline, achieving highfidelity reconstruction from dense image sequences without relying on SfM-derived point clouds.

## Abstract Cue
- the Mip-NeRF360 datasets and a 30.7% improvement on the Tanks and Temples datasets.
