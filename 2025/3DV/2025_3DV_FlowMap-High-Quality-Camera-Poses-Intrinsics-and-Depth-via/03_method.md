# Method

- Year/Venue: 2025 / 3DV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: geometry, depth, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_FlowMap-High-Quality-Camera-Poses-Intrinsics-and-Depth-via/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We use 90% of the available views for training and 10% for testing.
- Alongside the use of point tracks to encourage long-term geometric consistency, we introduce differentiable re-parameterizations of depth, intrinsics, and pose that are amenable to first-order optimization.
- We use the 3D points provided by COLMAP, DROID-SLAM, and FlowMap as input to 3D Gaussian Splatting.

## 원리적 동기
- Introduction Reconstructing a 3D scene from video is one of the most fundamental problems in vision and has been studied for over five decades.
- These approaches extract sparse correspondences across frames, match them, discard outliers, and then optimize the correspondences’ 3D positions alongside the camera parameters by minimizing reprojection error .
- We use 90% of the available views for training and 10% for testing.

## 핵심 방법론
- We use 90% of the available views for training and 10% for testing.
- We use the 3D points provided by COLMAP, DROID-SLAM, and FlowMap as input to 3D Gaussian Splatting.
- For each candidate, we use our pose solver Eq.
- We further highlight that FlowMap’s reparameterizations are necessary to estimate poses and intrinsics in a single forward pass, which is crucial for the generalizable (pretraining) setting explored in ...
- During pre-training, in order to minimize the time spent computing correspondences, we do not use point tracks and use GMFlow to compute optical flow instead of RAFT.
