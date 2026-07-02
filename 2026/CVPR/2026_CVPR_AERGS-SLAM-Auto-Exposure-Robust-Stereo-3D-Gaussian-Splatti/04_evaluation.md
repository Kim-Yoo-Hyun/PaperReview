# Evaluation

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_AERGS-SLAM-Auto-Exposure-Robust-Stereo-3D-Gaussian-Splatti/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- EuRoC

## Metrics
- accuracy
- mAP
- PSNR
- SSIM
- LPIPS
- RMSE

## Evaluation Protocol and Results
- Extensive experiments on public datasets and our self-collected realworld dataset demonstrate that AERGS-SLAM outperforms baselines in both localization performance and photorealistic mapping quality.
- Firstly, we propose a camera exposure network to model the camera exposure process, which we integrate with Gaussian splatting to achieve exposure-controlled novel view synthesis.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
