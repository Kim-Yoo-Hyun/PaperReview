# Method

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_RIOcc-Efficient-Cross-Modal-Fusion-Transformer-with-Collab/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we propose a novel LiDAR-Camera 3D semantic occupancy prediction framework called RIOcc, with collaborative feature refinement and multi-scale cross-modal fusion transformer.
- Finally, to facilitate effective cross-modal complementarity, we develop the Deformable Dual-Attention (DDA) module.
- Additionally, we introduce an Auxiliary Semantic Loss Laux to optimize the refined semantic features extracted by the semantic encoder.

## 원리적 동기
- However, existing methods mainly focus on processing large-scale voxels, which bring high computational costs and degrade details.
- In this paper, we propose a novel LiDAR-Camera 3D semantic occupancy prediction framework called RIOcc, with collaborative feature refinement and multi-scale cross-modal fusion transformer.

## 핵심 방법론
- Additionally, we introduce an Auxiliary Semantic Loss Laux to optimize the refined semantic features extracted by the semantic encoder.
- 3D Occupancy prediction performance on the Occ3D-nuScenes dataset. * means the performance using the camera mask during training.
- Therefore, the overall loss function can be expressed as: 4.1.
