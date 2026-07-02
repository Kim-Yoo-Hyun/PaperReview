# Evaluation

- Year/Venue: 2025 / ICCV
- Category: Sensor Fusion, LiDAR, Occupancy, and Autonomous 3D Perception
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_RIOcc-Efficient-Cross-Modal-Fusion-Transformer-with-Collab/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- nuScenes
- Occ3D

## Metrics
- accuracy
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- Extensive experiments demonstrate that RIOcc achieves state-of-the-art performance, with 54.2 mIoU and 25.9 mIoU on the Occ3DnuScenes and nuScenes-Occupancy datasets, respectively.
- Instead of processing voxel features like OpenOccupancy, we choose BEV features to achieve higher computational efficiency.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
