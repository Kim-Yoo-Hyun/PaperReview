# PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar

- Year/Venue: 2024 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: NeRF, 3D reconstruction, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_PlatoNeRF-3D-Reconstruction-in-Plato-s-Cave-via-Single-Vie/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing methods for single-view 3D reconstruction with NeRF rely on either data priors to hallucinate views of occluded regions, which may not be physically accurate, or shadows observed ...
- We propose using time-offlight data captured by a single-photon avalanche diode to overcome these limitations.
- 3D reconstruction from a single-view is challenging because of the ambiguity from monocular cues and lack of information about occluded regions.

## Core Idea
- We use a dataset of single-photon lidar data captured by Henley et al. to validate our method outside of simulation.
- We propose using time-offlight data captured by a single-photon avalanche diode to overcome these limitations.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In addition, we demonstrate improved generalization under practical constraints on sensor spatialand temporal-resolution.
- By leveraging the advantages of both NeRF and two-bounce light measured by lidar, we demonstrate that we can reconstruct visible and occluded geometry without data priors or reliance ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose using time-offlight data captured by a single-photon avalanche diode to overcome these limitations.
- In addition, we demonstrate improved generalization under practical constraints on sensor spatialand temporal-resolution.
- Our method models two-bounce optical paths with NeRF, using lidar transient data for supervision.

## Abstract Cue
- 3D reconstruction from a single-view is challenging because of the ambiguity from monocular cues and lack of information about occluded regions.
