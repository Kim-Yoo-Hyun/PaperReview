# Evaluation

- Year/Venue: 2026 / CVPR
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, Diffusion, Generation, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_L3DR-3D-aware-LiDAR-Diffusion-and-Rectification/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- SemanticKITTI
- nuScenes
- Waymo

## Metrics
- mAP

## Evaluation Protocol and Results
- Extensive experiments over multiple benchmarks including KITTI, KITTI360, nuScenes and Waymo show that the proposed L3DR achieves state-of-theart generation and superior geometry-realism consistently.
- Leveraging such analysis, we design a 3D residual regression network that rectifies RV artifacts and achieves superb geometry realism by predicting pointlevel offsets in 3D space.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
