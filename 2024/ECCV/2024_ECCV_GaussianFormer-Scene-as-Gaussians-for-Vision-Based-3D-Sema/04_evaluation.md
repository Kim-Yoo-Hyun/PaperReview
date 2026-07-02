# Evaluation

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2024/ECCV/2024_ECCV_GaussianFormer-Scene-as-Gaussians-for-Vision-Based-3D-Sema/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- KITTI
- nuScenes

## Metrics
- mIoU
- IoU

## Evaluation Protocol and Results
- We conducted experiments on the nuScenes dataset and the KITTI-360 dataset for 3D semantic occupancy prediction with surrounding and monocular cameras, respectively.
- Experimental results demonstrate that GaussianFormer achieves comparable performance with state-of-the-art methods with only 17.8% - 24.8% of their memory consumption.
- We conduct extensive experiments on the widely adopted nuScenes and KITTI-360 datasets.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
