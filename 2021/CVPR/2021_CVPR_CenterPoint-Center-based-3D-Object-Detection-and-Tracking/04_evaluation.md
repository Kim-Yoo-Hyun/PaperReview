# Evaluation

- Year/Venue: 2021 / CVPR
- Category: Foundations: 3D Detection and BEV Perception
- Tags: point cloud, 3D Vision
- Paper link: ./2021/CVPR/2021_CVPR_CenterPoint-Center-based-3D-Object-Detection-and-Tracking/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- nuScenes
- Waymo

## Metrics
- accuracy
- IoU
- mAP
- NDS

## Evaluation Protocol and Results
- CenterPoint achieved state-of-theart performance on the nuScenes benchmark for both 3D detection and tracking, with 65.5 NDS and 63.8 AMOTA for a single model.
- On the Waymo Open Dataset, CenterPoint outperforms all previous single model method by a large margin and ranks first among all Lidar-only submissions.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
