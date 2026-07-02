# Dream-to-Recon: Monocular 3D Reconstruction with Diffusion-Depth Distillation from Single Images

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, depth, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Dream-to-Recon-Monocular-3D-Reconstruction-with-Diffusion/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- While MDE is already useful for many applications, it has a severe limitation: Depth maps are only a 2D projection of the 3D scene, and do not capture ...
- This limitation makes pure MDE unsuitable for many 3D understanding tasks, e.g. planning the path of a vehicle into a parking spot that was only partially observed.
- However, such 3D ground truth is difficult and expensive to obtain, e.g. by accumulating Lidar scans from a 1.

## Core Idea
- We propose to leverage pre-trained 2D diffusion models and depth prediction models to generate synthetic scene geometry from a single image.
- Scene Reconstruction We first test our method’s ability to generate accurate volumetric geometry from a single image in complex scenes.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments on the challenging KITTI-360 and Waymo datasets demonstrate that our method matches or outperforms state-of-the-art baselines that use multi-view supervision, and offers unique advantages, for example ...
- Through architectural improvements, scaled-up datasets with high-quality ground-truth, and cross-dataset training, these methods have achieved strong generalization capabilities and can be used in an off-the-shelf way .
- Recent volumetric reconstruction methods achieve impressive results, but generally require expensive 3D ground truth or multi-view supervision.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experiments on the challenging KITTI-360 and Waymo datasets demonstrate that our method matches or outperforms state-of-the-art baselines that use multi-view supervision, and offers unique advantages, for example ...
- Through architectural improvements, scaled-up datasets with high-quality ground-truth, and cross-dataset training, these methods have achieved strong generalization capabilities and can be used in an off-the-shelf way .
- We propose to leverage pre-trained 2D diffusion models and depth prediction models to generate synthetic scene geometry from a single image.

## Abstract Cue
- Traditionally, this task has been mainly approached via monocular depth estimation (MDE), where a network predicts per-pixel distance values for a given single image.
