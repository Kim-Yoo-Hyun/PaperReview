# Problem

- Year/Venue: 2024 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: NeRF, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_PlatoNeRF-3D-Reconstruction-in-Plato-s-Cave-via-Single-Vie/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing methods for single-view 3D reconstruction with NeRF rely on either data priors to hallucinate views of occluded regions, which may not be physically accurate, or shadows observed ...
- We propose using time-offlight data captured by a single-photon avalanche diode to overcome these limitations.
- 3D reconstruction from a single-view is challenging because of the ambiguity from monocular cues and lack of information about occluded regions.

## 해결하려는 문제
- We propose using time-offlight data captured by a single-photon avalanche diode to overcome these limitations.
- In addition, we demonstrate improved generalization under practical constraints on sensor spatialand temporal-resolution.
- Our method models two-bounce optical paths with NeRF, using lidar transient data for supervision.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
