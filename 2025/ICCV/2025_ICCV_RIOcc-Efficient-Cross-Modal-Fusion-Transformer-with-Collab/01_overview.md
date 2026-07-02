# RIOcc: Efficient Cross-Modal Fusion Transformer with Collaborative Feature Refinement for 3D Semantic Occupancy Prediction

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_RIOcc-Efficient-Cross-Modal-Fusion-Transformer-with-Collab/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing methods mainly focus on processing large-scale voxels, which bring high computational costs and degrade details.

## Core Idea
- In this paper, we propose a novel LiDAR-Camera 3D semantic occupancy prediction framework called RIOcc, with collaborative feature refinement and multi-scale cross-modal fusion transformer.
- Finally, to facilitate effective cross-modal complementarity, we develop the Deformable Dual-Attention (DDA) module.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that RIOcc achieves state-of-the-art performance, with 54.2 mIoU and 25.9 mIoU on the Occ3DnuScenes and nuScenes-Occupancy datasets, respectively.
- Instead of processing voxel features like OpenOccupancy, we choose BEV features to achieve higher computational efficiency.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that RIOcc achieves state-of-the-art performance, with 54.2 mIoU and 25.9 mIoU on the Occ3DnuScenes and nuScenes-Occupancy datasets, respectively.
- In this paper, we propose a novel LiDAR-Camera 3D semantic occupancy prediction framework called RIOcc, with collaborative feature refinement and multi-scale cross-modal fusion transformer.
- Finally, to facilitate effective cross-modal complementarity, we develop the Deformable Dual-Attention (DDA) module.

## Abstract Cue
- Fusion module Backbone The multi-modal 3D semantic occupancy task provides a comprehensive understanding of the scene and has received considerable attention in the field of autonomous driving.
