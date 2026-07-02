# Evaluation

- Year/Venue: 2021 / ICCV
- Category: Foundations: 3D Representation Learning
- Tags: 3D Vision, point cloud, representation, self-supervised
- Paper link: ./2021/ICCV/2021_ICCV_Self-Supervised-Pretraining-of-3D-Features-on-any-Point-Cl/paper.pdf
- Code/Project: https://github.com/facebookresearch/DepthContrast
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- S3DIS
- Matterport3D
- KITTI
- Waymo

## Metrics
- accuracy
- mIoU
- IoU
- AP
- mAP

## Evaluation Protocol and Results
- We evaluate our models on 9 benchmarks for object detection, semantic segmentation, and object classification, where they achieve stateof-the-art results and can outperform supervised pretraining.
- Our pretraining which uses unlabeled single-view 3D data, outperforms training from scratch, and achieves the same detection performance with about half the detection labels. points that need to ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
