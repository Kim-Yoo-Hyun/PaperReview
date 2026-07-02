# FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent

- Year/Venue: 2025 / 3DV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: geometry, depth, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_FlowMap-High-Quality-Camera-Poses-Intrinsics-and-Depth-via/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction Reconstructing a 3D scene from video is one of the most fundamental problems in vision and has been studied for over five decades.
- These approaches extract sparse correspondences across frames, match them, discard outliers, and then optimize the correspondences’ 3D positions alongside the camera parameters by minimizing reprojection error .

## Core Idea
- We use 90% of the available views for training and 10% for testing.
- Alongside the use of point tracks to encourage long-term geometric consistency, we introduce differentiable re-parameterizations of depth, intrinsics, and pose that are amenable to first-order optimization.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our method not only far outperforms prior gradientdescent based bundle adjustment methods, but surprisingly approaches the accuracy of COLMAP, the state-ofthe-art SfM method, on the downstream task of ...
- Today, essentially all state-of-the-art approaches are built on top of Structure-from-Motion (SfM) methods like COLMAP .
- This framework has delivered excellent results which un

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We empirically show that camera parameters and dense depth recovered by our method enable photo-realistic novel view synthesis on 360◦ trajectories using Gaussian Splatting.
- Our method not only far outperforms prior gradientdescent based bundle adjustment methods, but surprisingly approaches the accuracy of COLMAP, the state-ofthe-art SfM method, on the downstream task of ...
- Alongside the use of point tracks to encourage long-term geometric consistency, we introduce differentiable re-parameterizations of depth, intrinsics, and pose that are amenable to first-order optimization.

## Abstract Cue
- This paper introduces FlowMap, an end-to-end differentiable method that solves for precise camera poses, camera intrinsics, and per-frame dense depth of a video sequence.
