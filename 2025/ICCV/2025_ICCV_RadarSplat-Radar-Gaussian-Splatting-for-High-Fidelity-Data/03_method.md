# Method

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_RadarSplat-Radar-Gaussian-Splatting-for-High-Fidelity-Data/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- This allows simulating safety-critical scenarios and augmenting training datasets without incurring further data collection costs.
- Introduction Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.
- To address these limitations, this paper proposes RadarSplat, which integrates Gaussian Splatting with novel radar noise modeling to enable realistic radar data synthesis and enhanced 3D reconstruction.

## 원리적 동기
- Introduction Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.
- To address these limitations, this paper proposes RadarSplat, which integrates Gaussian Splatting with novel radar noise modeling to enable realistic radar data synthesis and enhanced 3D reconstruction.
- This allows simulating safety-critical scenarios and augmenting training datasets without incurring further data collection costs.

## 핵심 방법론
- Image Synthesis Scene Reconstruction PSNR↑ SSIM↑ LPIPS↓ RMSE↓ R-CD.↓ Radar Fields 22.66 0.20 0.60 3.03 0.29 Acc.↑ 0.59 Ours 26.06 0.51 0.37 1.81 0.04 0.91 Table 1.
- Image synthesis and geometry reconstruction evaluation on
