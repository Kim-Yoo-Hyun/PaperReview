# GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_GaussianOcc-Fully-Self-supervised-and-Efficient-3D-Occupan/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection.
- Additionally, existing methods rely on volume rendering for final 3D voxel representation learning using 2D signals (depth maps and semantic maps), which is time-consuming and less effective.
- As a result, the proposed GaussianOcc method enables fully self-supervised (no ground truth ego pose) 3D occupancy estimation in competitive performance with low computational cost (2.7 times faster ...

## Core Idea
- To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection.
- Training details: We propose a two-stage training for fully self-supervised 3D occupancy estimation as indicated in Figure 2.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Existing methods achieve self-supervised learning through volume rendering, where the 2D semantic map supervision is derived from open-vocabulary semantic segmentation , and the depth map supervision is obtained ...
- To facilitate 3D occupancy estimation, several benchmarks have been developed for supervised training [40–42, 44], though these require substantial effort in 3D annotation.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection.
- We propose Gaussian Splatting from Voxel space (GSV) to leverage the fast rendering properties of Gaussian splatting.
- We introduce GaussianOcc, a systematic method that investigates Gaussian splatting for fully self-supervised and efficient 3D occupancy estimation in surround views.

## Abstract Cue
- We introduce GaussianOcc, a systematic method that investigates Gaussian splatting for fully self-supervised and efficient 3D occupancy estimation in surround views.
