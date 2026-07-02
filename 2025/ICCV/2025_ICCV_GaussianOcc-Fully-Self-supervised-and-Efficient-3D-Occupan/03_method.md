# Method

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_GaussianOcc-Fully-Self-supervised-and-Efficient-3D-Occupan/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection.
- Training details: We propose a two-stage training for fully self-supervised 3D occupancy estimation as indicated in Figure 2.
- We propose Gaussian Splatting from Voxel space (GSV) to leverage the fast rendering properties of Gaussian splatting.

## 원리적 동기
- To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection.
- Additionally, existing methods rely on volume rendering for final 3D voxel representation learning using 2D signals (depth maps and semantic maps), which is time-consuming and less effective.
- To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection.

## 핵심 방법론
- Training details: We propose a two-stage training for fully self-supervised 3D occupancy estimation as indicated in Figure 2.
- GT Pose mIoU* mIoU MonoScene BEVDet BEVFormer OccFormer TPVFormer CTF-Occ ✓ ✓ ✓ ✓ ✓ ✓ × × × × × × 6.33 20.03 24.64 22.39 28.69 29.54 ...
