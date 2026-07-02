# GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, sensor fusion, LiDAR, point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_GeGS-PCR-Fast-and-Robust-Color-3D-Point-Cloud-Registration/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address the challenges of point cloud registration in low-overlap real-world scenarios, we propose GeGS-PCR, a two-stage method that integrates Geometric-3DGS for colored point cloud registration.
- Previous works have focused on keypoints and correspondences, leveraging specialized neural networks to extract features from point clouds, and subsequently determining the rigid transformation using robust estimators like ...
- Despite rapid progress, point cloud registration remains challenging in real-world scenarios with low overlap between point clouds , where registration often fails.

## Core Idea
- Finally, based on the GeoTransformer, we use self-attention and cross-attention to focus on the color information in the point cloud structure and guide superpoint registration.
- To overcome these limitations, we propose GeGS-PCR, a novel two-stage method that combines geometric, color, and Gaussian information for robust registration.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our method achieves state-of-the-art performance with Registration Recall at 99.9%, Relative Rotation Error as low as 0.013, and Relative Translation Error as low as 0.024, improving precision by ...
- Additionally, fast differentiable rendering is utilized to refine the registration process, leading to improved convergence.
- To validate the performance of the GeGS-PCR model, we evaluate it on the indoor benchmarks Color3DMatch (C3DM) and Color3DLoMatch (C3DLM), as well as our colorized outdoor ColorKitti (The ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method achieves state-of-the-art performance with Registration Recall at 99.9%, Relative Rotation Error as low as 0.013, and Relative Translation Error as low as 0.024, improving precision by ...
- To overcome these limitations, we propose GeGS-PCR, a novel two-stage method that combines geometric, color, and Gaussian information for robust registration.
- Our approach incorporates a dedicated color encoder that enhances color features by extracting multi-level geometric and color data from the original point cloud.

## Abstract Cue
- We address the challenge of point cloud registration using color information, where traditional methods relying solely on geometric features often struggle in lowoverlap and incomplete scenarios.
