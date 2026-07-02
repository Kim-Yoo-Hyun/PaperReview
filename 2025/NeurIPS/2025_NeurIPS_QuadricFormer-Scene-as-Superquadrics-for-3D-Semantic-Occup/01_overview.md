# QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_QuadricFormer-Scene-as-Superquadrics-for-3D-Semantic-Occup/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions .
- Vision-centric autonomous driving systems have gained much attention for their cost-effectiveness over LiDAR-based solutions .
- While voxel-based methods use dense 3D grids to capture fine details, they ignore the sparsity of driving scenes and suffer from high computational costs.

## Core Idea
- To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent shape diversity.
- Building on this, we present QuadricFormer, a superquadric-based model for efficient 3D occupancy prediction, and introduce a pruning-and-splitting module to further enhance modeling efficiency by concentrating superquadrics in ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments on the nuScenes and KITTI-360 datasets demonstrate that QuadricFormer achieves state-of-the-art performance while maintaining superior efficiency.
- Our method achieves state-of-the-art performance.
- Our method achieves comparable performance to GaussianFormer-2 with much fewer primitives.

## Limitation
- With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing representation efficiency.

## Contribution
- Extensive experiments on the nuScenes and KITTI-360 datasets demonstrate that QuadricFormer achieves state-of-the-art performance while maintaining superior efficiency.
- To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent shape diversity.
- Building on this, we present QuadricFormer, a superquadric-based model for efficient 3D occupancy prediction, and introduce a pruning-and-splitting module to further enhance modeling efficiency by concentrating superquadrics in ...

## Abstract Cue
- 3D occupancy prediction is crucial for robust autonomous driving systems as it enables comprehensive perception of environmental structures and semantics.
