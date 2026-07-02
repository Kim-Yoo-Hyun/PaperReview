# PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space

- Year/Venue: 2017 / NeurIPS
- Category: Foundations: 3D Geometry and Point Clouds
- Tags: 3D geometry, point cloud, representation
- Paper link: ./2017/NeurIPS/2017_NeurIPS_PointNet++-Deep-Hierarchical-Feature-Learning-on-Point-Set/paper.pdf
- Code/Project: https://github.com/charlesq34/pointnet2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Deciding the appropriate scale of local neighborhood balls, however, is a more challenging yet intriguing problem, due to the entanglement of feature scale and non-uniformity of input point ...
- Few prior works study deep learning on point sets.

## Core Idea
- With further observation that point sets are usually sampled with varying densities, which results in greatly decreased performance for networks trained on uniform densities, we propose novel set ...
- Finally, we propose our PointNet++ that is able to robustly learn features even in non-uniformly sampled point sets (Sec.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In particular, results significantly better than state-of-the-art have been obtained on challenging benchmarks of 3D point clouds.
- Firstly, our hierarchical learning architecture achieves significantly better performance than the non-hierarchical PointNet .
- Experiments show that our network called PointNet++ is able to learn deep point set features efficiently and robustly.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- With further observation that point sets are usually sampled with varying densities, which results in greatly decreased performance for networks trained on uniform densities, we propose novel set ...
- In particular, results significantly better than state-of-the-art have been obtained on challenging benchmarks of 3D point clouds.
- In this work, we introduce a hierarchical neural network that applies PointNet recursively on a nested partitioning of the input point set.

## Abstract Cue
- Few prior works study deep learning on point sets.
