# Problem

- Year/Venue: 2023 / AAAI
- Category: Foundations: 3D Detection and BEV Perception
- Tags: depth, 3D Vision
- Paper link: ./2023/AAAI/2023_AAAI_BEVDepth-Acquisition-of-Reliable-Depth-for-Multi-view-3D-O/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- It is an ill-posed problem because estimating the depth of objects from monocular images is inherently ambiguous.
- Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since the depth prediction module is indirectly ...
- VoxelNet (Zhou and Tuzel 2018) voxelizes the point cloud, converting it from sparse to dense voxels, and then proposes bounding boxes in dense space to aid the index ...

## 해결하려는 문제
- In this research, we propose a new 3D object detector with a trustworthy depth estimation, dubbed BEVDepth, for camera-based Bird’s-Eye-View (BEV) 3D object detection.
- Aided by customized Efficient Voxel Pooling and multi-frame mechanism, BEVDepth achieves the new stateof-the-art 60.9% NDS on the challenging nuScenes test set while maintaining high efficiency.

## 선행 연구 / 배경 단서
- It is an ill-posed problem because estimating the depth of objects from monocular images is inherently ambiguous.
- Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since the depth prediction module is indirectly ...
- While LiDAR-based methods have demonstrated their ability to deliver trustworthy 3D detection results, multi-view camera-based methods have recently attracted increasing attention because of their lower cost.
