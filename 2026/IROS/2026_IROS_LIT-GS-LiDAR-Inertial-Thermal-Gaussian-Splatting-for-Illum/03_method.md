# Method

- Year/Venue: 2026 / IROS
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting
- Paper link: ./2026/IROS/2026_IROS_LIT-GS-LiDAR-Inertial-Thermal-Gaussian-Splatting-for-Illum/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We present LIT-GS, a LiDAR–inertial–thermal Gaussian Splatting framework that injects LiDAR-derived plane geometry as an explicit constraint in both pose/structure refinement and Gaussian optimization.
- Although our method introduces additional geometry-aware constraints during optimization, the explicit Gaussian representation together with splattingbased rasterization remains computationally efficient.
- Runtime and Computational Cost Analysis Training on the Car scene takes 70.6 minutes.

## 원리적 동기
- This efficiency has rapidly motivated radiance-field mapping for robotics and large-scale environments, yet most existing 3DGS-based mapping pipelines still depend heavily on RGB imagery and Structure-from-Motion (SfM) to ...
- Reliance on visible imagery poses a fundamental limitation.
- We present LIT-GS, a LiDAR–inertial–thermal Gaussian Splatting framework that injects LiDAR-derived plane geometry as an explicit constraint in both pose/structure refinement and Gaussian optimization.

## 핵심 방법론
- Although our method introduces additional geometry-aware constraints during optimization, the explicit Gaussian representation together with splattingbased rasterization remains computationally efficient.
- Runtime and Computational Cost Analysis Training on the Car scene takes 70.6 minutes.
- Zhang, “GSSDF: LiDAR-augmented Gaussian splatting and neural SDF for geometrically consistent rendering and reconstruction,” arXiv preprint arXiv:2503.10170, 2025.
- Xue, “ThermalGaussian: Thermal 3D Gaussian splatting,” arXiv preprint arXiv:2409.07200, 2024.
- Shen, “GS-LIVO: Real-time LiDAR, inertial, and visual multi-sensor fused odometry with Gaussian mapping,” arXiv preprint arXiv:2501.08672, 2025.
