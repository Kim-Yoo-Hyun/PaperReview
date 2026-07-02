# BEVDepth: Acquisition of Reliable Depth for Multi-view 3D Object Detection

- Year/Venue: 2023 / AAAI
- Category: Foundations: 3D Detection and BEV Perception
- Tags: depth, 3D Vision
- Paper link: ./2023/AAAI/2023_AAAI_BEVDepth-Acquisition-of-Reliable-Depth-for-Multi-view-3D-O/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- It is an ill-posed problem because estimating the depth of objects from monocular images is inherently ambiguous.
- Based on this observation, we point out that the depth learning mechanism in existing Lift-splat brings three deficiencies: • Inaccurate Depth Since the depth prediction module is indirectly ...
- VoxelNet (Zhou and Tuzel 2018) voxelizes the point cloud, converting it from sparse to dense voxels, and then proposes bounding boxes in dense space to aid the index ...

## Core Idea
- In this research, we propose a new 3D object detector with a trustworthy depth estimation, dubbed BEVDepth, for camera-based Bird’s-Eye-View (BEV) 3D object detection.
- We use the classification heatmap for evaluation, th denotes the threshold of heatmap.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Aided by customized Efficient Voxel Pooling and multi-frame mechanism, BEVDepth achieves the new stateof-the-art 60.9% NDS on the challenging nuScenes test set while maintaining high efficiency.
- Then, comprehensive experiments are conducted on BEVDepth to validate the effects of our proposed components.
- For the ablation study, all experiments are trained for

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this research, we propose a new 3D object detector with a trustworthy depth estimation, dubbed BEVDepth, for camera-based Bird’s-Eye-View (BEV) 3D object detection.
- Aided by customized Efficient Voxel Pooling and multi-frame mechanism, BEVDepth achieves the new stateof-the-art 60.9% NDS on the challenging nuScenes test set while maintaining high efficiency.

## Abstract Cue
- In this research, we propose a new 3D object detector with a trustworthy depth estimation, dubbed BEVDepth, for camera-based Bird’s-Eye-View (BEV) 3D object detection.
