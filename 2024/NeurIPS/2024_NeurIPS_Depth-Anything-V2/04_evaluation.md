# Evaluation

- Year/Venue: 2024 / NeurIPS
- Category: Foundations: Monocular Geometry
- Tags: depth, 3D Vision
- Paper link: ./2024/NeurIPS/2024_NeurIPS_Depth-Anything-V2/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- ETH3D

## Metrics
- accuracy
- mAP
- AbsRel
- RMSE

## Evaluation Protocol and Results
- As shown in Table 2, our results are superior to MiDaS and comparable to V1 .
- Improvement in these dimensions cannot be correctly reflected in current benchmarks.
- As shown in Table 3, on our proposed benchmark with diverse scenes, even our smallest model is significantly better than other heavy SD-based
- Performance on our proposed benchmark DA-2K.
- As shown in Table 2, our results are superior to MiDaS and comparable to V1 .
- Improvement in these dimensions cannot be correctly reflected in current benchmarks.

## Baselines
- Since our model predicts affine-invariant inverse depth, for fairness, we compare with Depth Anything V1 and MiDaS V3.1 on five unseen test datasets.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
