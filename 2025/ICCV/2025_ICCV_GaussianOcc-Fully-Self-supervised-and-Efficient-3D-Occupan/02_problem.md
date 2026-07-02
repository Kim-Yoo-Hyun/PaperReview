# Problem

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_GaussianOcc-Fully-Self-supervised-and-Efficient-3D-Occupan/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection.
- Additionally, existing methods rely on volume rendering for final 3D voxel representation learning using 2D signals (depth maps and semantic maps), which is time-consuming and less effective.
- As a result, the proposed GaussianOcc method enables fully self-supervised (no ground truth ego pose) 3D occupancy estimation in competitive performance with low computational cost (2.7 times faster ...

## 해결하려는 문제
- To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection.
- We propose Gaussian Splatting from Voxel space (GSV) to leverage the fast rendering properties of Gaussian splatting.
- We introduce GaussianOcc, a systematic method that investigates Gaussian splatting for fully self-supervised and efficient 3D occupancy estimation in surround views.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
