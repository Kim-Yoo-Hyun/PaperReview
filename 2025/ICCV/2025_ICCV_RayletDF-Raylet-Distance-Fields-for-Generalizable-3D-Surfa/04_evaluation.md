# Evaluation

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Representations and Neural Fields
- Tags: Gaussian Splatting, 3D reconstruction, point cloud, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_RayletDF-Raylet-Distance-Fields-for-Generalizable-3D-Surfa/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet

## Metrics
- accuracy
- Chamfer
- RMSE
- ADE

## Evaluation Protocol and Results
- Most notably, our method achieves exceptional generalization ability, successfully recovering 3D surfaces in a single-forward pass across unseen datasets in testing.
- While achieving excellent results in 3D reconstruction, these coordinate-based methods and their variants typically demand dense network evaluations to obtain explicit surfaces, thus being computationally heavy.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
