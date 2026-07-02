# Problem

- Year/Venue: 2017 / NeurIPS
- Category: Foundations: 3D Geometry and Point Clouds
- Tags: 3D geometry, point cloud, representation
- Paper link: ./2017/NeurIPS/2017_NeurIPS_PointNet++-Deep-Hierarchical-Feature-Learning-on-Point-Set/paper.pdf
- Code/Project: https://github.com/charlesq34/pointnet2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Deciding the appropriate scale of local neighborhood balls, however, is a more challenging yet intriguing problem, due to the entanglement of feature scale and non-uniformity of input point ...
- Few prior works study deep learning on point sets.

## 해결하려는 문제
- With further observation that point sets are usually sampled with varying densities, which results in greatly decreased performance for networks trained on uniform densities, we propose novel set ...
- In particular, results significantly better than state-of-the-art have been obtained on challenging benchmarks of 3D point clouds.
- In this work, we introduce a hierarchical neural network that applies PointNet recursively on a nested partitioning of the input point set.

## 선행 연구 / 배경 단서
- Deciding the appropriate scale of local neighborhood balls, however, is a more challenging yet intriguing problem, due to the entanglement of feature scale and non-uniformity of input point ...
- Few prior works study deep learning on point sets.
- We introduce a hierarchical neural network, named as PointNet++, to process a set of points sampled in a metric space in a hierarchical fashion.
