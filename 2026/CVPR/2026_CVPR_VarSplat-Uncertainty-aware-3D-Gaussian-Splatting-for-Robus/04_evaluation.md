# Evaluation

- Year/Venue: 2026 / CVPR
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, geometry, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_VarSplat-Uncertainty-aware-3D-Gaussian-Splatting-for-Robus/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Replica

## Metrics
- accuracy
- mAP
- PSNR
- SSIM
- LPIPS
- ATE
- RMSE

## Evaluation Protocol and Results
- Ex- perimental results on Replica (synthetic) and TUM-RGBD, ScanNet, and ScanNet++ (real-world) show that VarSplat improves robustness and achieves competitive or superior tracking, mapping, and novel view synthesis ...
- Classical methods based on voxels, TSDFs, surfels, or meshes can achieve real-time tracking and mapping but struggle to capture photorealistic appearance.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
