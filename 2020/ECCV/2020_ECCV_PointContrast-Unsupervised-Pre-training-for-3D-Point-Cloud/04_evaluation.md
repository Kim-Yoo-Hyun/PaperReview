# Evaluation

- Year/Venue: 2020 / ECCV
- Category: Foundations: 3D Representation Learning
- Tags: 3D Vision, point cloud, representation, self-supervised
- Paper link: ./2020/ECCV/2020_ECCV_PointContrast-Unsupervised-Pre-training-for-3D-Point-Cloud/paper.pdf
- Code/Project: https://github.com/facebookresearch/PointContrast
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- ScanNet
- S3DIS
- KITTI
- ShapeNet
- ShapeNetPart

## Metrics
- accuracy
- mIoU
- IoU
- mAP
- SR

## Evaluation Protocol and Results
- Our findings are extremely encouraging: using a unified triplet of architecture, source dataset, and contrastive loss for pre-training, we achieve improvement over recent best results in segmentation and ...
- Furthermore, the improvement was similar to supervised pre-training, suggesting that future efforts should favor scaling data collection over more detailed annotation.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
