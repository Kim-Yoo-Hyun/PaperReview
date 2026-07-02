# OccFormer: Dual-path Transformer for Vision-based 3D Semantic Occupancy Prediction

- Year/Venue: 2023 / ICCV
- Category: Foundations: 3D Semantic Occupancy
- Tags: 3D Vision, semantic, occupancy, Transformer
- Paper link: ./2023/ICCV/2023_ICCV_OccFormer-Dual-path-Transformer-for-Vision-based-3D-Semant/paper.pdf
- Code/Project: https://github.com/zhangyp15/OccFormer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Though LiDAR-based methods , with explicit depth measurements, have been dominating the leading performance on public datasets , vision-based approaches still offer advantages in terms of cost-effectiveness, stability, ...
- Experimental results demonstrate that OccFormer significantly outperforms existing methods for semantic scene completion on SemanticKITTI dataset and for LiDAR semantic segmentation on nuScenes dataset.

## Core Idea
- To address this issue, we propose the class-guided sampling method.
- More specifically, we first compute the class frequencies nc ∈ RNc from the training set, where Nc is the number of classes.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results demonstrate that OccFormer significantly outperforms existing methods for semantic scene completion on SemanticKITTI dataset and for LiDAR semantic segmentation on nuScenes dataset.
- OccFormer achieves a long-range, dynamic, and efficient encoding of the camera-generated 3D voxel features.
- Considering these tasks require either rigid bounding boxes or BEV-oriented predictions, the collapse of 3D scenes into 2D ground planes has demonstrated an excellent trade-off between performance and ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results demonstrate that OccFormer significantly outperforms existing methods for semantic scene completion on SemanticKITTI dataset and for LiDAR semantic segmentation on nuScenes dataset.
- This paper presents OccFormer, a dual-path transformer network to effectively process the 3D volume for semantic occupancy prediction.
- It is obtained by decomposing the heavy 3D processing into the local and global transformer pathways along the horizontal plane.

## Abstract Cue
- The vision-based perception for autonomous driving has undergone a transformation from the bird-eye-view (BEV) representations to the 3D semantic occupancy.
