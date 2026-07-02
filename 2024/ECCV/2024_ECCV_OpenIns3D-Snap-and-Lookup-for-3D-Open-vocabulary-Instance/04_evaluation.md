# Evaluation

- Year/Venue: 2024 / ECCV
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, semantic
- Paper link: ./2024/ECCV/2024_ECCV_OpenIns3D-Snap-and-Lookup-for-3D-Open-vocabulary-Instance/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- ScanNet
- ScanNet200
- S3DIS
- Replica

## Metrics
- accuracy
- IoU
- AP
- mAP

## Evaluation Protocol and Results
- Replica and ScanNet200 are evaluated by following the settings of OpenMask3D .
- This approach yet simple, achieves state-of-the-art performance across a wide range of 3D open-vocabulary tasks, including recognition, object detection, and instance segmentation, on both indoor and outdoor datasets.
- When integrated with powerful 2D open-world models, it achieves excellent results in scene understanding tasks.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
