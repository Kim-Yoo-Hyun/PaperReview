# Method

- Year/Venue: 2025 / IROS
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2025/IROS/2025_IROS_LiV-GS-LiDAR-Vision-Integration-for-3D-Gaussian-Splatting/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- — We present LiV-GS, a LiDAR-visual SLAM system in outdoor environments that leverages 3D Gaussian as a differentiable spatial representation.
- To reliably and stably update Gaussians outside the LiDAR field of view, we introduce a novel conditional Gaussian constraint that aligns these Gaussians closely with the nearest reliable ...
- To further facilitate stable tracking, we introduce a weighting function for Gaussians that distinguishes Gaussians generated solely by color supervision and those also Fig.

## 원리적 동기
- Notably, LiV-GS is the first method that directly aligns discrete and sparse LiDAR data with continuous differentiable Gaussian maps in large-scale outdoor scenes, overcoming the limitation of fixed ...
- Traditional map representations such as point clouds, voxels, and surfels suffer from bounded-resolution in mapping , while implicit neural fields demand expensive computational resources.
- — We present LiV-GS, a LiDAR-visual SLAM system in outdoor environments that leverages 3D Gaussian as a differentiable spatial representation.

## 핵심 방법론
- To further facilitate stable tracking, we introduce a weighting function for Gaussians that distinguishes Gaussians generated solely by color supervision and those also Fig.
- Our method effectively prevents these issues. by LiDAR depth in the error calculation of point clouds and Gaussian match.
- By minimizing the loss function, the Gaussian map updates the parameters of Gaussians continuously together with splitting and pruning operations of Gaussians.
- We then utilize an incremental error minimization function to ensure precise correspondences between planes and points as below: X (k) C E(xp , xg ) = wxg (nxp ...
- To construct a weight function that combines normal consistency and density factors, we first identify all the nearest Gaussian distribution centers inside the local spherical region Nr (x), ...
