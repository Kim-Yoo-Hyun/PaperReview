# Problem

- Year/Venue: 2025 / 3DV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: geometry, depth, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_FlowMap-High-Quality-Camera-Poses-Intrinsics-and-Depth-via/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Introduction Reconstructing a 3D scene from video is one of the most fundamental problems in vision and has been studied for over five decades.
- These approaches extract sparse correspondences across frames, match them, discard outliers, and then optimize the correspondences’ 3D positions alongside the camera parameters by minimizing reprojection error .

## 해결하려는 문제
- We empirically show that camera parameters and dense depth recovered by our method enable photo-realistic novel view synthesis on 360◦ trajectories using Gaussian Splatting.
- Our method not only far outperforms prior gradientdescent based bundle adjustment methods, but surprisingly approaches the accuracy of COLMAP, the state-ofthe-art SfM method, on the downstream task of ...
- Alongside the use of point tracks to encourage long-term geometric consistency, we introduce differentiable re-parameterizations of depth, intrinsics, and pose that are amenable to first-order optimization.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
