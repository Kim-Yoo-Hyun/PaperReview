# C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion

- Year/Venue: 2026 / CVPR
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, sensor fusion, LiDAR, Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_C-GenReg-Training-Free-3D-Point-Cloud-Registration-by-Mult/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Generated RGB Branch World Foundation Model Geometric Branch Geometric Feature Extractor (𝑹∗ , 𝒕∗ ) Geometric Feature Matching Figure 1.
- C-GenReg: A training-free point cloud registration framework.
- The pipeline operates in two parallel branches: (1) GeneratedRGB Branch - a World Foundation Model generates RGB views that are geometrically aligned with the input source and target ...

## Core Idea
- For the VFM branch, we use K =4 input views from the L=50 views, and the probability temperature parameter is τm = 0.1.
- Standard point cloud registration consists of feature extraction, feature matching, and robust pose estimation (e.g.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In contrast, the image domain has largely overcome such generalization limits through Vision Foundation Models (VFMs), which achieve remarkable robustness by training on massive, heterogeneous datasets .

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In contrast, the image domain has largely overcome such generalization limits through Vision Foundation Models (VFMs), which achieve remarkable robustness by training on massive, heterogeneous datasets .
- Standard point cloud registration consists of feature extraction, feature matching, and robust pose estimation (e.g.
- C-GenReg: A training-free point cloud registration framework.

## Abstract Cue
- Generated RGB Branch World Foundation Model Geometric Branch Geometric Feature Extractor (𝑹∗ , 𝒕∗ ) Geometric Feature Matching Figure 1.
