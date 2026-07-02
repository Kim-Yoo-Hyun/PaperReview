# SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting, semantic
- Paper link: ./2024/ECCV/2024_ECCV_SGS-SLAM-Semantic-Gaussian-Splatting-For-Neural-Dense-SLAM/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Dense Visual Simultaneous Localization and Mapping (SLAM) is a crucial problem in the field of computer vision.
- However, NeRF-based SLAM methods employ multi-layer perceptrons (MLPs) as the implicit neural representation of scenes, which introduces several challenging limitations.
- Traditional visual SLAM systems stand out in sparse mapping using point clouds and voxels, but fall short in dense reconstruction.

## Core Idea
- We present SGS-SLAM, the first semantic visual SLAM system based on Gaussian Splatting.
- We introduce a unique semantic feature loss that effectively compensates for the shortcomings of traditional depth and color losses in object optimization.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that SGS-SLAM delivers state-of-the-art performance in camera pose estimation, map reconstruction, precise semantic segmentation, and object-level geometric accuracy, while ensuring real-time rendering capabilities.
- 4.1 Experimental Setup Datasets We evaluate our method on both synthetic and real-world datasets.
- To compare with other neural implicit SLAM methods, we evaluate synthetic scenes from Replica dataset and real-world scenes from ScanNet and ScanNet++ datasets.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present SGS-SLAM, the first semantic visual SLAM system based on Gaussian Splatting.
- Extensive experiments demonstrate that SGS-SLAM delivers state-of-the-art performance in camera pose estimation, map reconstruction, precise semantic segmentation, and object-level geometric accuracy, while ensuring real-time rendering capabilities.
- We introduce a unique semantic feature loss that effectively compensates for the shortcomings of traditional depth and color losses in object optimization.

## Abstract Cue
- We present SGS-SLAM, the first semantic visual SLAM system based on Gaussian Splatting.
