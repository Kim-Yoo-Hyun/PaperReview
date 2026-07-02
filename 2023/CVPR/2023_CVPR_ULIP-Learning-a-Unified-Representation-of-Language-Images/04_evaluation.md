# Evaluation

- Year/Venue: 2023 / CVPR
- Category: 3D Representation Learning and Foundation Models
- Tags: 3D Vision, Vision-Language Model, point cloud, alignment
- Paper link: ./2023/CVPR/2023_CVPR_ULIP-Learning-a-Unified-Representation-of-Language-Images/paper.pdf
- Code/Project: https://github.com/salesforce/ULIP
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- ModelNet40
- ShapeNet

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- Experiments show that ULIP effectively improves the performance of multiple recent 3D backbones by simply pre-training them on ShapeNet55 using our framework, achieving state-of-the-art performance in both standard ...
- ULIP also improves the performance of PointMLP by around 3% in 3D classification on ScanObjectNN, and outperforms PointCLIP by 28.8% on top-1 accuracy for zero-shot 3D classification on ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
