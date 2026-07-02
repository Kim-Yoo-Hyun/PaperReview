# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, point cloud, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_GaussianGrow-Geometry-aware-Gaussian-Growing-from-3D-Point/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our method leverages a text-guided multiview diffusion model for appearance synthesis while constraining novel views to reduce fusion artifacts.
- For com- pleting the hard-to-observe regions, we propose to iteratively detect the camera pose by observing the largest ungrown regions in point clouds and inpainting them by inpainting ...
- In this section, we present a comprehensive evaluation of GaussianGrow’s performance across multiple scenarios.

## 원리적 동기
- Existing methods have explored predicting point maps as geometric references for inferring Gaussian primitives, while the unreliable estimated geometries may lead to poor generations.
- 3D Gaussian Splatting has demonstrated superior performance in rendering efficiency and quality, yet the generation of 3D Gaussians still remains a challenge without proper geometric priors.
- Our method leverages a text-guided multiview diffusion model for appearance synthesis while constraining novel views to reduce fusion artifacts.

## 핵심 방법론
- Our method leverages a text-guided multiview diffusion model for appearance synthesis while constraining novel views to reduce fusion artifacts.
- In this section, we present a comprehensive evaluation of GaussianGrow’s performance across multiple scenarios.
- 18975 We introduce GaussianGrow, a novel approach for generating 3D Gaussians by growing them from readily available point clouds.
- TriplaneGaussian was adapted by bypassing its point cloud decoder for direct point-to-Gaussian conversion and integrating Stable Diffusion for text guidance.
- We modified DreamGaussian by replacing its random initialization with point cloud guidance, enabling direct point input.
