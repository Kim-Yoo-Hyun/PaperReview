# Evaluation

- Year/Venue: 2024 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2024/CVPR/2024_CVPR_IPoD-Implicit-Field-Learning-with-Point-Diffusion-for-Gene/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ShapeNet
- CO3D

## Metrics
- accuracy
- Chamfer
- F-score

## Evaluation Protocol and Results
- Experiments conducted on the CO3D-v2 dataset affirm the superiority of IPoD, achieving 7.8% improvement in F-score and 28.6% in Chamfer distance over existing methods.
- Current state-of-the-art methods develop Transformer-based implicit field learning, necessitating an intensive learning paradigm that requires dense query-supervision uniformly sampled throughout the entire space.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
