# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Equivariance, Calibration, and Registration
- Tags: Gaussian Splatting, geometry, point cloud, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_Liberated-GS-3D-Gaussian-Splatting-Independent-from-SfM-Po/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Then, we introduce a progressive segmented initialization process that leverages both local and global Gaussians to construct a coarse solution.
- To address this limitation, we propose a novel initialization pipeline, achieving highfidelity reconstruction from dense image sequences without relying on SfM-derived point clouds.
- Conclusion In this work, we propose Librated-GS, a novel approach that removes the dependence on accurate initial point clouds in 3DGS for novel view synthesis from a sequence ...

## 원리적 동기
- To address this limitation, we propose a novel initialization pipeline, achieving highfidelity reconstruction from dense image sequences without relying on SfM-derived point clouds.
- While 3DGS effectively addresses the slow rendering problem caused by radiance fields, it introduces additional input requirements.
- Then, we introduce a progressive segmented initialization process that leverages both local and global Gaussians to construct a coarse solution.

## 핵심 방법론
- Then, we introduce a progressive segmented initialization process that leverages both local and global Gaussians to construct a coarse solution.
- Conclusion In this work, we propose Librated-GS, a novel approach that removes the dependence on accurate initial point clouds in 3DGS for novel view synthesis from a sequence ...
- Note that our method surpasses the original 3DGS not only in areas with insufficient SfM points but also in regions with abundant points.
- As our method does not modify the refinement stage, its runtime remains comparable to the original pipeline.
- 6, our method recovers more details in scenes where depth estimation confidence is high (e.g., indoor scenes) and effectively mitigates artifacts and reconstruction errors caused by depth inaccuracies ...
