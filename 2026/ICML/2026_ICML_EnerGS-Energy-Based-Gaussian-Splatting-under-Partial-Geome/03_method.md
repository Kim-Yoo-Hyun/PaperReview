# Method

- Year/Venue: 2026 / ICML
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_EnerGS-Energy-Based-Gaussian-Splatting-under-Partial-Geome/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Our method renders significantly finer details in these areas compared to baselines, aligning with our theoretical expectation that the adaptive energy field facilitates robust reconstruction in sensor blind ...
- Without sufficient constraints, the optimization often gravitates towards geometrically invalid local minima, spawning floaters or near-camera artifacts to overfit training views [46, 29 Photometry Waymo Open Dataset Geometry ...
- 3D Gaussian Splatting (3DGS) has been widely adopted for scene reconstruction, where training inherently constitutes a highly coupled and nonconvex optimization problem.

## 원리적 동기
- In such sparse-view regimes, the reconstruction problem becomes inherently ill-posed.
- To address this challenge, we model partially observable geometry as a continuous energy field induced by geometric evidence and propose EnerGS.
- Our method renders significantly finer details in these areas compared to baselines, aligning with our theoretical expectation that the adaptive energy field facilitates robust reconstruction in sensor blind ...

## 핵심 방법론
- Our method renders significantly finer details in these areas compared to baselines, aligning with our theoretical expectation that the adaptive energy field facilitates robust reconstruction in sensor blind ...
- While such misalignment may not be apparent in training views, it manifests as floaters and structural distortions in novel viewpoints, degrading the final photometric quality.
- Photometry Waymo Open Dataset Geometry #G (M)↓ PSNR↑ SSIM↑ Leak↓ OccCov↑ Margin↑ Thick↓ Photometry Geometry #G (M)↓ PSNR↑ SSIM↑ Leak↓ OccCov↑ Margin↑ Thick↓ 3DGS ToG 23 15.01 2DGS ...
