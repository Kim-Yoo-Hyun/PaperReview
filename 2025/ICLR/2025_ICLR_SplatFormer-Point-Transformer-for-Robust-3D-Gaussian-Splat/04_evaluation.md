# Evaluation

- Year/Venue: 2025 / ICLR Spotlight
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, point cloud, 3D Vision
- Paper link: ./2025/ICLR/2025_ICLR_SplatFormer-Point-Transformer-for-Robust-3D-Gaussian-Splat/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ShapeNet
- Objaverse

## Metrics
- mAP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- To capture high-frequency details and improve gradient flow, skip connection MLP modules are used to map intermediate downsampling outputs to residuals, which are then added to the upsampling ...
- The metric is evaluated on OOD test views with elevation ϕood ≥ 70◦ ; colors indicate the 1st , 2nd , and 3rd best-performing model Methods Standard Regularized ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
