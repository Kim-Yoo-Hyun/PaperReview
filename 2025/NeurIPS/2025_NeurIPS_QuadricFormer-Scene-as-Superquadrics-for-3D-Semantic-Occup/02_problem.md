# Problem

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_QuadricFormer-Scene-as-Superquadrics-for-3D-Semantic-Occup/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions .
- Vision-centric autonomous driving systems have gained much attention for their cost-effectiveness over LiDAR-based solutions .
- While voxel-based methods use dense 3D grids to capture fine details, they ignore the sparsity of driving scenes and suffer from high computational costs.

## 해결하려는 문제
- Extensive experiments on the nuScenes and KITTI-360 datasets demonstrate that QuadricFormer achieves state-of-the-art performance while maintaining superior efficiency.
- To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent shape diversity.
- Building on this, we present QuadricFormer, a superquadric-based model for efficient 3D occupancy prediction, and introduce a pruning-and-splitting module to further enhance modeling efficiency by concentrating superquadrics in ...

## 선행 연구 / 배경 단서
- Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions .
- Vision-centric autonomous driving systems have gained much attention for their cost-effectiveness over LiDAR-based solutions .
- While voxel-based methods use dense 3D grids to capture fine details, they ignore the sparsity of driving scenes and suffer from high computational costs.
