# GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2024/ECCV/2024_ECCV_GaussianFormer-Scene-as-Gaussians-for-Vision-Based-3D-Sema/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite the promising applications, the dense output space of 3D occupancy prediction poses a great challenge in how to efficiently and effectively represent the 3D scene.
- It is also more difficult to capture scene dynamics with grid-based representations since it is objects instead of grids that move in the 3D space .
- We employ a set of 3D semantic Gaussians to sparsely describe a 3D scene.

## Core Idea
- To address this, we propose an object-centric representation to describe 3D scenes with sparse 3D semantic Gaussians where each Gaussian represents a flexible region of interest and its ...
- We aggregate information from images through the attention mechanism and iteratively refine the properties of 3D Gaussians including position, covariance, and semantics.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results demonstrate that GaussianFormer achieves comparable performance with state-of-the-art methods with only 17.8% - 24.8% of their memory consumption.
- We conduct extensive experiments on the widely adopted nuScenes and KITTI-360 datasets.
- We conducted experiments on the nuScenes dataset and the KITTI-360 dataset for 3D semantic occupancy prediction with surrounding and monocular cameras, respectively.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results demonstrate that GaussianFormer achieves comparable performance with state-of-the-art methods with only 17.8% - 24.8% of their memory consumption.
- To address this, we propose an object-centric representation to describe 3D scenes with sparse 3D semantic Gaussians where each Gaussian represents a flexible region of interest and its ...
- We aggregate information from images through the attention mechanism and iteratively refine the properties of 3D Gaussians including position, covariance, and semantics.

## Abstract Cue
- 3D semantic occupancy prediction aims to obtain 3D finegrained geometry and semantics of the surrounding scene and is an important task for the robustness of vision-centric autonomous driving.
