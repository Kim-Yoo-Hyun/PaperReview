# VGGT: Visual Geometry Grounded Transformer

- Year/Venue: 2025 / CVPR
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, geometry, Transformer
- Paper link: ./2025/CVPR/2025_CVPR_VGGT-Visual-Geometry-Grounded-Transformer/paper.pdf
- Code/Project: https://github.com/facebookresearch/vggt
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction We consider the problem of estimating the 3D attributes of a scene, captured in a set of images, utilizing a feedforward neural network.
- Even so, visual geometry still plays a major role in 3D reconstruction, which increases complexity and computational cost.

## Core Idea
- We present a qualitative comparison with DUSt3R on inthe-wild scenes in Fig.
- Recent contributions like DUSt3R and its evolution We present VGGT, a feed-forward neural network that directly infers all key 3D attributes of a scene, including camera parameters, point ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking.
- MASt3R have shown promising results in this direction, but these networks can only process two images at once and rely on post-processing to reconstruct more images, fusing pairwise ...
- It is also simple and efficient, reconstructing images in under one second, and still outperforming alternatives that require post-processing with visual geometry optimization techniques.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- The network achieves state-of-the-art results in multiple 3D tasks, including camera parameter estimation, multi-view depth estimation, dense point cloud reconstruction, and 3D point tracking.
- Recent contributions like DUSt3R and its evolution We present VGGT, a feed-forward neural network that directly infers all key 3D attributes of a scene, including camera parameters, point ...
- MASt3R have shown promising results in this direction, but these networks can only process two images at once and rely on post-processing to reconstruct more images, fusing pairwise ...

## Abstract Cue
- Introduction We consider the problem of estimating the 3D attributes of a scene, captured in a set of images, utilizing a feedforward neural network.
