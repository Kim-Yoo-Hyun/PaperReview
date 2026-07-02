# Method

- Year/Venue: 2026 / ICML
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, depth, point cloud, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_PointDiT-Pixel-Space-Diffusion-for-Monocular-Geometry-Esti/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce a minimalist pixel-space Diffusion Transformer built on a plain ViT, which operates directly on raw 3D point map patches and is conditioned on image tokens from ...
- State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions (e.g., MoGe), or necessitate compressing geometry into latent spaces (e.g., GeometryCrafter) to leverage pre-trained ...
- These methods often rely on complex hybrid architectures (Wang et al., Relp ↓ δ1p ↑ Reld ↓ δ1d ↑ BF1 ↑ Param Time (M) (ms) GeometryCrafter Depth Pro ...

## 원리적 동기
- Existing approaches to this challenge can be broadly categorized into two distinct groups.
- However, remains an ill-posed problem due to the fundamental scale and depth ambiguities of perspective projection.
- We introduce a minimalist pixel-space Diffusion Transformer built on a plain ViT, which operates directly on raw 3D point map patches and is conditioned on image tokens from ...

## 핵심 방법론
- Relp ↓ δ1p ↑ Reld ↓ δ1d ↑ BF1 ↑ Param Time (M) (ms) GeometryCrafter Depth Pro UniDepthV2 MoGe MoGe-2 5.45 5.71 4.45 4.21 4.53 96.75 96.71 97.35 ...
