# Method

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_3D-Geometry-Aware-Deformable-Gaussian-Splatting-for-Dynami/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Dataset In the paper, we use both synthetic and real datasets for evaluating our method.
- In this paper, we propose a 3D geometry-aware deformable Gaussian Splatting method for dynamic view synthesis.
- 3, we use the Gaussians at the current moment to render the image.

## 원리적 동기
- Existing neural radiance fields (NeRF) based solutions learn the deformation in an implicit manner, which cannot incorporate 3D scene geometry.
- Dataset In the paper, we use both synthetic and real datasets for evaluating our method.

## 핵심 방법론
- Dataset In the paper, we use both synthetic and real datasets for evaluating our method.
- 3, we use the Gaussians at the current moment to render the image.
- Moreover, we use a 2-layer MLP with a width of 64 for the front point feature extraction, and a 3-layer MLP with a width of 64 for the ...
- Meanwhile, for the HyperNeRF dataset, we use the point cloud provided in its dataset as the initial point cloud.
- For the positional encoding process, we use L = 10 for position x and L = 6 for timestamp t.
