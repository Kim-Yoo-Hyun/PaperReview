# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Equivariance, Calibration, and Registration
- Tags: geometry, sensor fusion, LiDAR, point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_GeGS-PCR-Fast-and-Robust-Color-3D-Point-Cloud-Registration/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI

## Metrics
- accuracy

## Evaluation Protocol and Results
- To validate the performance of the GeGS-PCR model, we evaluate it on the indoor benchmarks Color3DMatch (C3DM) and Color3DLoMatch (C3DLM), as well as our colorized outdoor ColorKitti (The ...
- Our method achieves state-of-the-art performance with Registration Recall at 99.9%, Relative Rotation Error as low as 0.013, and Relative Translation Error as low as 0.024, improving precision by ...
- Additionally, fast differentiable rendering is utilized to refine the registration process, leading to improved convergence.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
