# Method

- Year/Venue: 2025 / NeurIPS poster
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_QuadricFormer-Scene-as-Superquadrics-for-3D-Semantic-Occup/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent shape diversity.
- Building on this, we present QuadricFormer, a superquadric-based model for efficient 3D occupancy prediction, and introduce a pruning-and-splitting module to further enhance modeling efficiency by concentrating superquadrics in ...
- We develop a probabilistic superquadric mixture model, which interprets each superquadric as an occupancy probability distribution with a corresponding geometry prior, and calculates semantics through probabilistic mixture.

## 원리적 동기
- Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions .
- Vision-centric autonomous driving systems have gained much attention for their cost-effectiveness over LiDAR-based solutions .
- To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent shape diversity.

## 핵심 방법론
- The official split contains 7 sequences for training, 1 for validation, and 1 for testing, corresponding to 8487, 1812, and 2566 key frames, respectively.
- MonoScene C 262144 37.87 12.31 19.34 0.43 0.58 8.02 2.03 0.86 48.35 11.38 28.13 3.22 32.89 3.53 26.15 16.75 6.92 5.67 4.20 3.09 Voxformer C 262144 38.76 11.91 ...
- IoU mIoU MonoScene Atlas BEVFormer TPVFormer TPVFormer* OccFormer SurroundOcc GaussianFormer GaussianFormer-2 23.96 7.31 4.03 0.35 8.00 8.04 2.90 0.28 1.16 0.67 4.01 4.35 27.72 5.20 15.13 11.29 9.03 ...
