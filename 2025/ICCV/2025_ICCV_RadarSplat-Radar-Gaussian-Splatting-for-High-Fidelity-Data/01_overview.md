# RadarSplat: Radar Gaussian Splatting for High-Fidelity Data Synthesis and 3D Reconstruction of Autonomous Driving Scenes

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_RadarSplat-Radar-Gaussian-Splatting-for-High-Fidelity-Data/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Introduction Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.
- To address these limitations, this paper proposes RadarSplat, which integrates Gaussian Splatting with novel radar noise modeling to enable realistic radar data synthesis and enhanced 3D reconstruction.
- High-fidelity 3D scene reconstruction plays a crucial role in autonomous driving by enabling novel data generation from existing datasets.

## Core Idea
- This allows simulating safety-critical scenarios and augmenting training datasets without incurring further data collection costs.
- Introduction Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Compared to the state-of- the-art, RadarSplat achieves superior radar image synthesis (+3.4 PSNR / 2.6× SSIM) and improved geometric reconstruction (−40% RMSE / 1.5× Accuracy), demonstrating its effectiveness ...
- Although the state-of-the-art radar-based neural representation shows promise for 3D driving scene reconstruction, it performs poorly in scenarios with significant radar noise, including receiver saturation and multipath reflection.
- While recent advances in radiance fields have demonstrated promising results in 3D reconstruction and sensor data synthesis using cameras and LiDAR, their potential for radar remains largely unexplored.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Compared to the state-of- the-art, RadarSplat achieves superior radar image synthesis (+3.4 PSNR / 2.6× SSIM) and improved geometric reconstruction (−40% RMSE / 1.5× Accuracy), demonstrating its effectiveness ...
- Introduction Data-driven, learning-based methods have significantly advanced autonomous driving; however, acquiring suitable training data remains a substantial challenge.
- Although the state-of-the-art radar-based neural representation shows promise for 3D driving scene reconstruction, it performs poorly in scenarios with significant radar noise, including receiver saturation and multipath reflection.

## Abstract Cue
- High-fidelity 3D scene reconstruction plays a crucial role in autonomous driving by enabling novel data generation from existing datasets.
