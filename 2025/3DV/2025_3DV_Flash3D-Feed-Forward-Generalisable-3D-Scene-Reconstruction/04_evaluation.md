# Evaluation

- Year/Venue: 2025 / 3DV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_Flash3D-Feed-Forward-Generalisable-3D-Scene-Reconstruction/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI

## Metrics
- accuracy
- mAP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- It achieves state-of-the-art results when trained and tested on RealEstate10k.
- More impressively, when transferred to KITTI, Flash3D achieves better PSNR than methods trained specifically on that dataset.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
