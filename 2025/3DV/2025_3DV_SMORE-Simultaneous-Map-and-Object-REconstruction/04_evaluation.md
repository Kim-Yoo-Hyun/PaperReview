# Evaluation

- Year/Venue: 2025 / 3DV
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_SMORE-Simultaneous-Map-and-Object-REconstruction/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- nuScenes
- Argoverse

## Metrics
- accuracy
- mAP
- Chamfer
- PSNR
- SSIM
- LPIPS
- ATE

## Evaluation Protocol and Results
- To achieve this, we take inspiration from recent novel view synthesis methods and frame the reconstruction problem as a global optimization over neural surfaces, ego poses, and object ...
- We analyze the surface reconstruction step for rolling-shutter LiDARs, and show that deskewing operations common in continuous time SLAM can be applied to dynamic objects as well, improving ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
