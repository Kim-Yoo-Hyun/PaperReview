# Evaluation

- Year/Venue: 2026 / CVPR
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, semantic, alignment, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_Geometry-Aware-Cross-Modal-Graph-Alignment-for-Referring-S/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- LERF

## Metrics
- accuracy
- mIoU
- IoU
- mAP

## Evaluation Protocol and Results
- GeoCGA consistently outperforms prior state-of-the-art methods, yielding relative mIoU improvements of 20.8% on Ref-LERF, 5.7% on LERF-OVS, and 1.0% on 3D-OVS.
- Although recent progress using 3D Gaussian Splatting (3DGS) has improved rendering quality, existing methods still struggle to spatially ground textual references due to two fundamental limitations: (1) language ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
