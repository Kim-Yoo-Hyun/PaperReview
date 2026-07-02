# PointCNN: Convolution On X-Transformed Points

- Year/Venue: 2018 / NeurIPS
- Category: Foundations: 3D Geometry and Point Clouds
- Tags: 3D Vision, point cloud, geometry, representation
- Paper link: ./2018/NeurIPS/2018_NeurIPS_PointCNN-Convolution-On-X-Transformed-Points/paper.pdf
- Code/Project: https://github.com/yangyanli/PointCNN
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We illustrate the problems and challenges of applying convolutions on point clouds in Figure 1.
- To address these problems, we propose to learn an X -transformation from the input points to simultaneously promote two causes: the first is the weighting of the input ...

## Core Idea
- To verify the effectiveness of the X -transformation, we propose PointCNN without it as a baseline, where lines 4-6 of Algorithm 1 are replaced by Fp ← Conv(K, ...
- To address these problems, we propose to learn an X -transformation from the input points to simultaneously promote two causes: the first is the weighting of the input ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show that PointCNN achieves on par or better performance than state-of-the-art methods on multiple challenging benchmark datasets and tasks.
- Note that PointCNN achieved top performance on both ModelNet40 and ScanNet.
- 4.1 Classification and Segmentation Results We summarize our 3D point cloud classification results on ModelNet40 and ScanNet in Table 1, and compare to several neural network methods designed ...

## Limitation
- While X -Conv is empirically demonstrated to be effective in practice, a rigorous understanding of it, especially when being composited into a deep neural network, is still an ...

## Contribution
- Experiments show that PointCNN achieves on par or better performance than state-of-the-art methods on multiple challenging benchmark datasets and tasks.
- To address these problems, we propose to learn an X -transformation from the input points to simultaneously promote two causes: the first is the weighting of the input ...
- We present a simple and general framework for feature learning from point clouds.

## Abstract Cue
- We present a simple and general framework for feature learning from point clouds.
