# Evaluation

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Representation Learning and Foundation Models
- Tags: point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_U-CAN-Unsupervised-Point-Cloud-Denoising-with-Consistency/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- Chamfer
- PSNR

## Evaluation Protocol and Results
- For the experiments on synthetic shapes, we follow ScoreDenoise to train our network on the PUNet dataset.
- Our evaluations denoising show significant improvement over the state-of-the-art unsupervised methods, where U-CAN also produces comparable results with the supervised methods.
- We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
