# Evaluation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: 3D Vision, Gaussian Splatting, semantic
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Segment-then-Splat-Unified-3D-Open-Vocabulary-Segmentation/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- LERF

## Metrics
- accuracy
- mIoU
- IoU
- AP
- mAP
- PSNR

## Evaluation Protocol and Results
- Notably, 2D pixel-based methods LERF_OVS 3DOVS tend to produce relatively ambiguous boundMethod mIoU↑ Time↓ mIoU↑ Time↓ aries, whereas our approach, leveraging the SegLangSplat 46.37 62.00 82.49 68.90 ment ...
- Our method outperforms all baseline ap- static (a) and dynamic (b) scenes. proaches.
- To assess the segmentation performance of our proposed method, we conduct experiments on two static scene datasets (i.e., 3DOVS dataset and LERF_OVS dataset ) and two dynamic scene ...
- The quantitative results on the 3DOVS are presented in Tab.
- Extensive experiments on various datasets demonstrate the effectiveness of our proposed method in both static and dynamic scenarios.
- Notably, 2D pixel-based methods LERF_OVS 3DOVS tend to produce relatively ambiguous boundMethod mIoU↑ Time↓ mIoU↑ Time↓ aries, whereas our approach, leveraging the SegLangSplat 46.37 62.00 82.49 68.90 ment ...

## Baselines
- We categorize the baselines into two groups based on their querying strategies: 2D pixel-based segmentation and 3D-based segmentation.
- For static scenes, we use LangSplat , LEGaussians and Gaussian Grouping as the 2D pixel-based baselines.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
