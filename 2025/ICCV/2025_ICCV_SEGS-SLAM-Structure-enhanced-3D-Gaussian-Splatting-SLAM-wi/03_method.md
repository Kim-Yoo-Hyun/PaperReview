# Method

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_SEGS-SLAM-Structure-enhanced-3D-Gaussian-Splatting-SLAM-wi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address these problems, we propose SEGS-SLAM, a structure-enhanced 3D Gaussian Splatting SLAM, which achieves high-quality photorealistic mapping.
- Second, we propose Appearance-from-Motion embedding (AfME), enabling 3D Gaussians to better model image appearance variations across different camera poses.
- First, we propose a structure-enhanced photorealistic mapping (SEPM) framework that, for the ﬁrst time, leverages highly structured point cloud to initialize structured 3D Gaussians, leading to signiﬁcant improvements ...

## 원리적 동기
- However, most existing algorithms fail to fully capture the underlying structure, resulting in structural inconsistency.
- 3D Gaussian splatting (3D-GS) has recently revolutionized novel view synthesis in the simultaneous localization and mapping (SLAM) problem.
- To address these problems, we propose SEGS-SLAM, a structure-enhanced 3D Gaussian Splatting SLAM, which achieves high-quality photorealistic mapping.

## 핵심 방법론
- Quantitative evaluation of our method compared to SOTA methods for RGB-D camera on Replica and TUM RGB-D datasets.
- Quantitative evaluation of our method compared to SOTA methods for Monocular (Mono) and Stereo cameras on Replica, TUM RGB-D, and EuRoC MAV datasets.
- Moreover, our method remains effective in stereo scenarios.
- 6, it is evident that for the Replica dataset, only our method can accurately recover the contours of edge regions.
- 7, our approach better reconstructs the global structure and local details of the scene.
