# Problem

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ODG-Occupancy-Prediction-Using-Dual-Gaussians/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- But existing methods utilize a single transformer which can only handle a smaller number of Gaussians.
- To overcome such drawbacks, another line of research formulate the task of 3D occupancy as direct set prediction, effectively predicting 3D occupancy as set of sparse points from ...
- Existing methods either adopt dense grids as scene representation which is difficult to scale to high resolution, or learn the entire scene using a single set of sparse ...

## 해결하려는 문제
- Extensive experiments on the Occ3D-nuScenes and Occ3D-Waymo benchmarks demonstrate our proposed method sets new state-of-the-art results while maintaining low inference cost.
- In this paper, we present ODG, a hierarchical dual sparse Gaussian representation to effectively capture complex scene dynamics.
- We utilize a hierarchical Gaussian transformer to predict the occupied voxel centers and semantic classes along with the Gaussian parameters.

## 선행 연구 / 배경 단서
- But existing methods utilize a single transformer which can only handle a smaller number of Gaussians.
- Our contributions can be summarized as follows: • Dual Gaussian Query Design: We propose a novel dual-query architecture comprising two distinct sets of Gaussian queries to separately model ...
- Therefore we propose to predict Gaussians in a coarse-to-fine manner with a series of transformer layers, enabling the use of a much larger number of Gaussians and thereby ...
