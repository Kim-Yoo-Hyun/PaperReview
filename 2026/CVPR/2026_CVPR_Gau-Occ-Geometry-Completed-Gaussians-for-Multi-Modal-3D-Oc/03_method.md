# Method

- Year/Venue: 2026 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Gau-Occ-Geometry-Completed-Gaussians-for-Multi-Modal-3D-Oc/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To ensure geometric completeness, we propose a LiDAR Completion Diffuser (LCD) that recovers missing structures from sparse LiDAR to initialize robust Gaussian anchors.
- We present Gau-Occ, a multi-modal framework that bypasses dense volumetric processing by modeling the scene as a compact collection of semantic 3D Gaussians.
- Furthermore, we introduce Gaussian Anchor Fusion (GAF), which efficiently integrates multi-view image semantics via geometry-aligned 2D sampling and cross-modal alignment.

## 원리적 동기
- Despite notable progress, two main challenges remain: (i) raw point clouds are sparse and occlusion-biased, capturing mostly visible surfaces while missing many occupied but unobserved regions, limiting the ...
- While promising, existing Gaussian-based approaches are predominantly vision-only, and their application to multimodal occupancy prediction remains underexplored, particularly under real-world constraints such as sparse LiDAR sampling and limited ...
- To ensure geometric completeness, we propose a LiDAR Completion Diffuser (LCD) that recovers missing structures from sparse LiDAR to initialize robust Gaussian anchors.

## 핵심 방법론
- Removing GVR (Row 3) and directly feeding the original, unaggregated tokens Xi to cross-attention leads to markedly higher latency and memory usage, as the attention map must be ...
- Compared to diffusionbased alternatives such as LiDPM (omitted for brevity), our lightweight pre-trained module provides superior geometric priors.
- Qualitative comparison between Gaussianformer-2 , DAOcc and Gau-Occ on the SurroundOcc-nuScenes validation set.
- On Point Cloud Completion and Gaussian Initialization.
- Modality IoU↑ mIoU↑ MonoScene C-CONet GaussianFormer BEVFormer TPVFormer OccFormer SurroundOcc FB-Occ GaussianFormer-2 C C C C C C C C C 24.0 26.1 29.8 30.5 30.9 31.4 31.5 ...
