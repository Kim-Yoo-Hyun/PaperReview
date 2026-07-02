# Method

- Year/Venue: 2025 / ICML Poster
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICML/2025_ICML_VTGaussian-SLAM-RGBD-SLAM-for-Large-Scale-Scenes-with-Spla/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To resolve this issue, we propose novel tracking and mapping strategies to work with a novel 3D representation, dubbed view-tied 3D Gaussians, for RGBD SLAM systems.
- We compare our method with the latest RGBD SLAM methods, including NeRF-based RGBD SLAM methods: NICE-SLAM (Zhu et al., 2022), VoxFusion (Yang et al., 2022), ESLAM (Johari et ...
- Moreover, our strategies remove the need of maintaining all Gaussians learnable throughout the training, while improving rendering quality, and tracking accuracy.

## 원리적 동기
- SLAM methods resolve the computational problem of mapping unknown environments while tracking camera locations.
- To resolve this issue, we propose novel tracking and mapping strategies to work with a novel 3D representation, dubbed view-tied 3D Gaussians, for RGBD SLAM systems.

## 핵심 방법론
- We compare our method with the latest RGBD SLAM methods, including NeRF-based RGBD SLAM methods: NICE-SLAM (Zhu et al., 2022), VoxFusion (Yang et al., 2022), ESLAM (Johari et ...
- 3D Gaussian Splatting SplaTAM 34.11 Gaussian-SLAM 42.08 LoopSplat∗ 36.63 0.970 0.996 0.985 0.100 0.018 0.112 22.80 25.05 22.72 0.893 0.929 0.873 0.178 0.168 0.259 19.14 27.70 24.92 0.716 ...
