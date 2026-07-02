# Evaluation

- Year/Venue: 2021 / ICCV
- Category: Foundations: Monocular Geometry
- Tags: 3D Vision, monocular depth, Vision Transformer, geometry
- Paper link: ./2021/ICCV/2021_ICCV_Vision-Transformers-for-Dense-Prediction/paper.pdf
- Code/Project: https://github.com/isl-org/DPT
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- KITTI
- ETH3D

## Metrics
- accuracy
- mIoU
- mAP
- AbsRel
- RMSE

## Evaluation Protocol and Results
- Our experiments show that this architecture yields substantial improvements on dense prediction tasks, especially when a large amount of training data is available.
- For monocular depth estimation, we observe an improvement of up to 28% in relative performance when compared to a state-of-theart fully-convolutional network.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
