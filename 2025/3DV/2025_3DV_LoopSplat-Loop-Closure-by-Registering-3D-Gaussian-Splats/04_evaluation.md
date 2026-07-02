# Evaluation

- Year/Venue: 2025 / 3DV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_LoopSplat-Loop-Closure-by-Registering-3D-Gaussian-Splats/paper.pdf
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
- It uses a robust pose graph optimization formulation and rigidly aligns the submaps to achieve global consistency.
- LoopSplat triggers loop closure online and computes relative loop edge constraints between submaps directly via 3DGS registration, leading to improvements in efficiency and accuracy over traditional global-to-local point ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
