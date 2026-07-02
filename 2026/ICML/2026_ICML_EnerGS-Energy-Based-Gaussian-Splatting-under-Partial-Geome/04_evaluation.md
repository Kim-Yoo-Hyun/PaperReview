# Evaluation

- Year/Venue: 2026 / ICML
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_EnerGS-Energy-Based-Gaussian-Splatting-under-Partial-Geome/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- Waymo

## Metrics
- mAP
- PSNR
- SSIM

## Evaluation Protocol and Results
- Extensive experiments on large-scale outdoor scenes demonstrate that, under both sparse multi-view and monocular settings, EnerGS consistently improves photometric quality and geometric stability, while effectively mitigating overfitting during ...
- EnerGS addresses this limitation by partitioning space into occupied, free, and unknown regions and guiding the spatial distribution of Gaussians with a geometric energy field, enabling more stable ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
