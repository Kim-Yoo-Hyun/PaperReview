# Evaluation

- Year/Venue: 2026 / ICML
- Category: 3D Semantic Understanding and Alignment
- Tags: semantic, alignment, 3D Vision
- Paper link: ./2026/ICML/2026_ICML_Rh-3DGS-Robust-Open-Vocabulary-Scene-Understanding-via-Rie/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- LERF

## Metrics
- accuracy
- mIoU
- IoU
- mAP
- PSNR
- SSIM
- LPIPS

## Evaluation Protocol and Results
- Experiments on three benchmarks show that Rh3DGS is best on open-vocabulary segmentation, boundary quality, and view-consistent rendering. (b) Baseline mask (View-1) (a) RGB(View-1) + zoom-in box (c) Baseline ...
- Lightweight Consistency Contrast (LIC) regularizes the 3D semantic field with neighborhood-based multi-positive contrast to improve local consistency and sharper boundaries.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
