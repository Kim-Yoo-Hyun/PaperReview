# Evaluation

- Year/Venue: 2022 / ECCV
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision
- Paper link: ./2022/ECCV/2022_ECCV_PETR-Position-Embedding-Transformation-for-Multi-View-3D-O/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- nuScenes

## Metrics
- mAP
- NDS
- SR

## Evaluation Protocol and Results
- All experiments are trained for 24 epochs (2x schedule) on 8 Tesla V100 GPUs with a batch size of 8.
- 4.1 Datasets and Metrics We validate our method on nuScenes benchmark .
- PETR achieves state-of-the-art performance (50.4% NDS and 44.1% mAP) on standard nuScenes dataset and ranks 1st place on the benchmark.
- All experiments are trained for 24 epochs (2x schedule) on 8 Tesla V100 GPUs with a batch size of 8.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
