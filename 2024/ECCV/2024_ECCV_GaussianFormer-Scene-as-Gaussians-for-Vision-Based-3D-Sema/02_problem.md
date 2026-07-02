# Problem

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2024/ECCV/2024_ECCV_GaussianFormer-Scene-as-Gaussians-for-Vision-Based-3D-Sema/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Despite the promising applications, the dense output space of 3D occupancy prediction poses a great challenge in how to efficiently and effectively represent the 3D scene.
- It is also more difficult to capture scene dynamics with grid-based representations since it is objects instead of grids that move in the 3D space .
- We employ a set of 3D semantic Gaussians to sparsely describe a 3D scene.

## 해결하려는 문제
- Experimental results demonstrate that GaussianFormer achieves comparable performance with state-of-the-art methods with only 17.8% - 24.8% of their memory consumption.
- To address this, we propose an object-centric representation to describe 3D scenes with sparse 3D semantic Gaussians where each Gaussian represents a flexible region of interest and its ...
- We aggregate information from images through the attention mechanism and iteratively refine the properties of 3D Gaussians including position, covariance, and semantics.

## 선행 연구 / 배경 단서
- Despite the promising applications, the dense output space of 3D occupancy prediction poses a great challenge in how to efficiently and effectively represent the 3D scene.
- It is also more difficult to capture scene dynamics with grid-based representations since it is objects instead of grids that move in the 3D space .
- We employ a set of 3D semantic Gaussians to sparsely describe a 3D scene.
