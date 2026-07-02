# Evaluation

- Year/Venue: 2026 / ICML spotlight
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, depth, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_VGGT-Motion-Motion-Aware-Calibration-Free-Monocular-SLAM-f/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- Waymo

## Metrics
- accuracy
- mAP
- ATE
- RMSE

## Evaluation Protocol and Results
- Experiments show that VGGT-Motion markedly improves trajectory accuracy and efficiency, achieving state-of-the-art performance in zero-shot, long-range calibrationfree monocular SLAM.
- By exploiting context-balanced anchors, it achieves search-free, pixel-wise dense alignment and efficient loop closure without costly feature matching.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
