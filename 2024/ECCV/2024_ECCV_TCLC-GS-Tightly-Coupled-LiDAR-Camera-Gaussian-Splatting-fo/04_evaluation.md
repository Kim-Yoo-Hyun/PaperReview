# Evaluation

- Year/Venue: 2024 / ECCV
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Gaussian Splatting
- Paper link: ./2024/ECCV/2024_ECCV_TCLC-GS-Tightly-Coupled-LiDAR-Camera-Gaussian-Splatting-fo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- nuScenes
- Waymo

## Metrics
- accuracy
- PSNR
- SSIM
- LPIPS
- AbsRel
- RMSE

## Evaluation Protocol and Results
- For our experiments, we selected six challenging recording sequences from this dataset, utilizing surrounding views captured by three cameras and corresponding data
- Utilizing a single NVIDIA RTX 3090 Ti, our method demonstrates fast training and achieves real-time RGB and depth rendering at 90 FPS in resolution of 1920×1280 (Waymo), and ...
- For our experiments, we selected six challenging recording sequences from this dataset, utilizing surrounding views captured by three cameras and corresponding data

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
