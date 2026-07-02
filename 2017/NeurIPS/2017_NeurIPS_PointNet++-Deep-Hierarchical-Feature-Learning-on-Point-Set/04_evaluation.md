# Evaluation

- Year/Venue: 2017 / NeurIPS
- Category: Foundations: 3D Geometry and Point Clouds
- Tags: 3D geometry, point cloud, representation
- Paper link: ./2017/NeurIPS/2017_NeurIPS_PointNet++-Deep-Hierarchical-Feature-Learning-on-Point-Set/paper.pdf
- Code/Project: https://github.com/charlesq34/pointnet2
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- ModelNet40

## Metrics
- accuracy

## Evaluation Protocol and Results
- Firstly, our hierarchical learning architecture achieves significantly better performance than the non-hierarchical PointNet .
- We use a three-level hierarchical network with three fully connected layers 1 Results.
- Datasets We evaluate on four datasets ranging from 2D objects (MNIST ), 3D objects (ModelNet40 rigid object, SHREC15 non-rigid object) to real 3D scenes (ScanNet ).
- 4.1 Point Set Classification in Euclidean Metric Space We evaluate our network on classifying point clouds sampled from both 2D (MNIST) and 3D (ModleNet40) Euclidean spaces.
- In particular, results significantly better than state-of-the-art have been obtained on challenging benchmarks of 3D point clouds.
- Firstly, our hierarchical learning architecture achieves significantly better performance than the non-hierarchical PointNet .

## Baselines
- In Table 1 and Table 2, we compare our method with a representative set of previous state of the arts.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
