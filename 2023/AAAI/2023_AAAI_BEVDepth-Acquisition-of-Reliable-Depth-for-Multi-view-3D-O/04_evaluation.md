# Evaluation

- Year/Venue: 2023 / AAAI
- Category: Foundations: 3D Detection and BEV Perception
- Tags: depth, 3D Vision
- Paper link: ./2023/AAAI/2023_AAAI_BEVDepth-Acquisition-of-Reliable-Depth-for-Multi-view-3D-O/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- nuScenes
- Waymo

## Metrics
- accuracy
- mAP
- NDS
- AbsRel
- RMSE

## Evaluation Protocol and Results
- Then, comprehensive experiments are conducted on BEVDepth to validate the effects of our proposed components.
- For the ablation study, all experiments are trained for
- 2020) dataset is a large-scale autonomous driving benchmark containing data from six cameras, one LiDAR, and five radars.
- Aided by customized Efficient Voxel Pooling and multi-frame mechanism, BEVDepth achieves the new stateof-the-art 60.9% NDS on the challenging nuScenes test set while maintaining high efficiency.
- Then, comprehensive experiments are conducted on BEVDepth to validate the effects of our proposed components.

## Baselines
- Comparisons with other leading camera 3D detection models are presented in the end.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
