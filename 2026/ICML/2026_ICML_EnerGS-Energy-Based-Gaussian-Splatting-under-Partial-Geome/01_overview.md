# EnerGS: Energy-Based Gaussian Splatting under Partial Geometric Priors

- Year/Venue: 2026 / ICML
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_EnerGS-Energy-Based-Gaussian-Splatting-under-Partial-Geome/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In such sparse-view regimes, the reconstruction problem becomes inherently ill-posed.
- To address this challenge, we model partially observable geometry as a continuous energy field induced by geometric evidence and propose EnerGS.
- 3D Gaussian Splatting (3DGS) has been widely adopted for scene reconstruction, where training inherently constitutes a highly coupled and nonconvex optimization problem.

## Core Idea
- Our method renders significantly finer details in these areas compared to baselines, aligning with our theoretical expectation that the adaptive energy field facilitates robust reconstruction in sensor blind ...
- Without sufficient constraints, the optimization often gravitates towards geometrically invalid local minima, spawning floaters or near-camera artifacts to overfit training views [46, 29 Photometry Waymo Open Dataset Geometry ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on large-scale outdoor scenes demonstrate that, under both sparse multi-view and monocular settings, EnerGS consistently improves photometric quality and geometric stability, while effectively mitigating overfitting during ...
- EnerGS addresses this limitation by partitioning space into occupied, free, and unknown regions and guiding the spatial distribution of Gaussians with a geometric energy field, enabling more stable ...
- Accurate geometric priors can significantly improve Gaussian initialization and optimization (e.g., via point clouds from LiDAR).

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments on large-scale outdoor scenes demonstrate that, under both sparse multi-view and monocular settings, EnerGS consistently improves photometric quality and geometric stability, while effectively mitigating overfitting during ...
- 3D Gaussian Splatting (3DGS) has been widely adopted for scene reconstruction, where training inherently constitutes a highly coupled and nonconvex optimization problem.
- EnerGS addresses this limitation by partitioning space into occupied, free, and unknown regions and guiding the spatial distribution of Gaussians with a geometric energy field, enabling more stable ...

## Abstract Cue
- 3D Gaussian Splatting (3DGS) has been widely adopted for scene reconstruction, where training inherently constitutes a highly coupled and nonconvex optimization problem.
