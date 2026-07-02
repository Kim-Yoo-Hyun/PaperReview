# Method

- Year/Venue: 2023 / SIGGRAPH
- Category: Foundations: 3D Scene Representations
- Tags: Gaussian Splatting, 3D reconstruction, representation
- Paper link: ./2023/SIGGRAPH/2023_SIGGRAPH_3D-Gaussian-Splatting-for-Real-Time-Radiance-Field-Renderi/paper.pdf
- Code/Project: https://github.com/graphdeco-inria/gaussian-splatting
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive training times, while ...
- The second component of our method is optimization of the properties of the 3D Gaussians – 3D position, opacity 𝛼, anisotropic covariance, and spherical harmonic (SH) coefficients – ...
- The third and final element of our method is our real-time rendering solution that uses fast GPU sorting algorithms and is inspired by tile-based rasterization, following recent work ...

## 원리적 동기
- While the continuous nature of these methods helps optimization, the stochastic sampling required for rendering is costly and can result in noise.
- 2006] and initialize the set of 3D Gaussians with the sparse point cloud produced for free as part of the SfM process.
- We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive training times, while ...

## 핵심 방법론
- We introduce a new approach that combines the best of both worlds: our 3D Gaussian representation allows optimization with state-of-the-art (SOTA) visual quality and competitive training times, while ...
- The second component of our method is optimization of the properties of the 3D Gaussians – 3D position, opacity 𝛼, anisotropic covariance, and spherical harmonic (SH) coefficients – ...
- The third and final element of our method is our real-time rendering solution that uses fast GPU sorting algorithms and is inspired by tile-based rasterization, following recent work ...
- 2022], which requires up to 48 hours of training time.
- We first introduce 3D Gaussians as a flexible and expressive scene representation.
