# Problem

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_VarSplat-Uncertainty-aware-3D-Gaussian-Splatting-for-Robus/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Despite these advances, a key limitation exists: measurement reliability is rarely modeled explicitly.
- However, existing 3DGS-SLAM approaches handle measurement reliability implicitly, making pose estimation and global alignment susceptible to drift in lowtexture regions, transparent surfaces, or areas with complex reflectance properties.
- 3D Gaussian Splatting (3DGS) further addresses this bottleneck by rasterizing anisotropic Gaussians with alpha compositing, enabling fast, differentiable rendering.

## 해결하려는 문제
- Ex- perimental results on Replica (synthetic) and TUM-RGBD, ScanNet, and ScanNet++ (real-world) show that VarSplat improves robustness and achieves competitive or superior tracking, mapping, and novel view synthesis ...
- To this end, we introduce VarSplat, an uncertainty-aware 3DGS-SLAM system that explicitly learns per-splat appearance variance.
- 3D Gaussian Splatting (3DGS) further addresses this bottleneck by rasterizing anisotropic Gaussians with alpha compositing, enabling fast, differentiable rendering.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
