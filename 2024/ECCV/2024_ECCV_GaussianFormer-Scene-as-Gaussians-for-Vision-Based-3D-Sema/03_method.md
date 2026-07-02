# Method

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2024/ECCV/2024_ECCV_GaussianFormer-Scene-as-Gaussians-for-Vision-Based-3D-Sema/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this, we propose an object-centric representation to describe 3D scenes with sparse 3D semantic Gaussians where each Gaussian represents a flexible region of interest and its ...
- We aggregate information from images through the attention mechanism and iteratively refine the properties of 3D Gaussians including position, covariance, and semantics.
- Zheng et al. method to generate 3D occupancy predictions, which only aggregates the neighboring Gaussians for a certain position.

## 원리적 동기
- Despite the promising applications, the dense output space of 3D occupancy prediction poses a great challenge in how to efficiently and effectively represent the 3D scene.
- It is also more difficult to capture scene dynamics with grid-based representations since it is objects instead of grids that move in the 3D space .
- To address this, we propose an object-centric representation to describe 3D scenes with sparse 3D semantic Gaussians where each Gaussian represents a flexible region of interest and its ...

## 핵심 방법론
- This is due to 3D Gaussians can adaptively change their positions and covariance to match the boundaries of small objects in images in contrast to rigid grid projections ...
- Notably, GaussianFormer surpasses all existing competitors with significantly reduced mem-
- Furthermore, the flexibility of 3D Gaussians also benefits the predictions for general objects (i.e. categories with other- prefix) which often have distinct shapes and appearances with normal categories.
