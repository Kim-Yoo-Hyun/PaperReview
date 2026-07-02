# Evaluation

- Year/Venue: 2026 / CVPR
- Category: 3D Semantic Understanding and Alignment
- Tags: Gaussian Splatting, NeRF, semantic, alignment, 3D Vision
- Paper link: ./2026/CVPR/2026_CVPR_NG-GS-NeRF-guided-3D-Gaussian-Splatting-Segmentation/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- LERF

## Metrics
- accuracy
- mIoU
- mAP

## Evaluation Protocol and Results
- Extensive experiments on NVOS, LERF-OVS, and ScanNet benchmarks demonstrate that our method achieves state-of-theart performance, with significant gains in boundary mIoU.
- This negligence leads to the abrupt changes on the boundaries during scene segmentation, resulting in inaccurate segmentation characterized by edge artifacts, as shown in Figure 1.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
