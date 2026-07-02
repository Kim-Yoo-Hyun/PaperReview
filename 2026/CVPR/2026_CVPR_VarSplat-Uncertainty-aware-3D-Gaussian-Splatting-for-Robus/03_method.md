# Method

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_VarSplat-Uncertainty-aware-3D-Gaussian-Splatting-for-Robus/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To this end, we introduce VarSplat, an uncertainty-aware 3DGS-SLAM system that explicitly learns per-splat appearance variance.
- Simultaneous Localization and Mapping (SLAM) with 3D Gaussian Splatting (3DGS) enables fast, differentiable rendering and high-fidelity reconstruction across diverse realworld scenes.
- Recent 3DGS-SLAM systems adopt this explicit representation and jointly optimize camera poses and Gaussian parameters.

## 원리적 동기
- Despite these advances, a key limitation exists: measurement reliability is rarely modeled explicitly.
- However, existing 3DGS-SLAM approaches handle measurement reliability implicitly, making pose estimation and global alignment susceptible to drift in lowtexture regions, transparent surfaces, or areas with complex reflectance properties.
- To this end, we introduce VarSplat, an uncertainty-aware 3DGS-SLAM system that explicitly learns per-splat appearance variance.

## 핵심 방법론
- Neural Implicit Fields Point-SLAM 246.16 ESLAM 25.15 GO-SLAM 176.28 Loopy-SLAM N/A 632.99 2.15 145.45 N/A 830.79 27.02 38.74 25.16 271.42 20.89 85.48 234.25 574.86 35.47 106.47 81.48 511.24 ...
- Neural Implicit Fields NICE-SLAM MIPS-Fusion Point-SLAM ESLAM Co-SLAM GO-SLAM Loopy-SLAM ✗ ✗ ✗ ✗ ✗ ✗ ✗ 4.26 3.00 4.34 2.47 2.40 1.50 3.79 4.99 N/A 4.54 3.69 ...
- Neural Implicit Fields NICE-SLAM ESLAM Point-SLAM GO-SLAM Loopy-SLAM Uni-SLAM ✗ ✗ ✗ ✗ ✗ ✓ 0.97 0.71 0.61 0.34 0.24 0.49 1.31 0.70 0.41 0.29 0.24 0.48 1.07 ...
