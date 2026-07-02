# Evaluation

- Year/Venue: 2025 / ICML Poster
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting
- Paper link: ./2025/ICML/2025_ICML_VTGaussian-SLAM-RGBD-SLAM-for-Large-Scale-Scenes-with-Spla/paper.pdf
- Code/Project: not identified from OpenReview
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
- State-of-the-art methods employ 3D Gaussians to represent a scene, and render these Gaussians through splatting for higher efficiency and better rendering.
- We justify the effectiveness of these designs, and report better performance over the latest methods on the widely used benchmarks in terms of rendering and tracking accuracy and ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
