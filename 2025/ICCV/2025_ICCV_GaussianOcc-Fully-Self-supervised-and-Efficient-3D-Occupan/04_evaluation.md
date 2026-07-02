# Evaluation

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_GaussianOcc-Fully-Self-supervised-and-Efficient-3D-Occupan/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- nuScenes
- Occ3D

## Metrics
- accuracy
- mIoU
- mAP
- SSIM
- RMSE
- SR

## Evaluation Protocol and Results
- Existing methods achieve self-supervised learning through volume rendering, where the 2D semantic map supervision is derived from open-vocabulary semantic segmentation , and the depth map supervision is obtained ...
- To facilitate 3D occupancy estimation, several benchmarks have been developed for supervised training [40–42, 44], though these require substantial effort in 3D annotation.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
