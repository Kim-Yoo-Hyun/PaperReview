# ODG: Occupancy Prediction Using Dual Gaussians

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ODG-Occupancy-Prediction-Using-Dual-Gaussians/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- But existing methods utilize a single transformer which can only handle a smaller number of Gaussians.
- To overcome such drawbacks, another line of research formulate the task of 3D occupancy as direct set prediction, effectively predicting 3D occupancy as set of sparse points from ...
- Existing methods either adopt dense grids as scene representation which is difficult to scale to high resolution, or learn the entire scene using a single set of sparse ...

## Core Idea
- In this section, we present our proposed 3D occupancy approach, ODG, in which we adopt a dual Gaussian query design to capture the respective dynamic and static elements ...
- In this paper, we present ODG, a hierarchical dual sparse Gaussian representation to effectively capture complex scene dynamics.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on the Occ3D-nuScenes and Occ3D-Waymo benchmarks demonstrate our proposed method sets new state-of-the-art results while maintaining low inference cost.
- For experiments on Waymo, we sample 20% of the data matching practices in previous works .
- 4.1 Experiment Setup Datasets: We evaluate our model on the Occ3D benchmark which bootstraps the nuScenes and Waymo-Open dataset.1 nuScenes consists of 1,000 scenes with a split of ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments on the Occ3D-nuScenes and Occ3D-Waymo benchmarks demonstrate our proposed method sets new state-of-the-art results while maintaining low inference cost.
- In this paper, we present ODG, a hierarchical dual sparse Gaussian representation to effectively capture complex scene dynamics.
- We utilize a hierarchical Gaussian transformer to predict the occupied voxel centers and semantic classes along with the Gaussian parameters.

## Abstract Cue
- Occupancy prediction infers fine-grained 3D geometry and semantics from camera images of the surrounding environment, making it a critical perception task for autonomous driving.
