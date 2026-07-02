# Method

- Year/Venue: 2024 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: NeRF, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_PlatoNeRF-3D-Reconstruction-in-Plato-s-Cave-via-Single-Vie/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We use a dataset of single-photon lidar data captured by Henley et al. to validate our method outside of simulation.
- We propose using time-offlight data captured by a single-photon avalanche diode to overcome these limitations.
- We believe our method is a promising direction as single-photon lidars become ubiquitous on consumer devices, such as phones, tablets, and headsets.

## 원리적 동기
- Existing methods for single-view 3D reconstruction with NeRF rely on either data priors to hallucinate views of occluded regions, which may not be physically accurate, or shadows observed ...
- We propose using time-offlight data captured by a single-photon avalanche diode to overcome these limitations.
- We use a dataset of single-photon lidar data captured by Henley et al. to validate our method outside of simulation.

## 핵심 방법론
- We use a dataset of single-photon lidar data captured by Henley et al. to validate our method outside of simulation.
- We also render corresponding ground truth depth images both from the training view and across 120 test views around the scene for evaluation.
