# Evaluation

- Year/Venue: 2025 / 3DV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_LangOcc-Open-Vocabulary-Occupancy-Estimation-via-Volume-Re/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- nuScenes
- Occ3D
- LERF

## Metrics
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- We also achieve a mIoU score of 11.84 on the Occ3D-nuScenes dataset, surpassing previous vision-only semantic occupancy estimation methods (+1.71%), despite not being limited to a specific set ...
- LangOcc outperforms LiDAR-supervised competitors in open vocabulary occupancy with a mAP of 22.7 by a large margin (+4.3%), solely relying on vision-based training.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
