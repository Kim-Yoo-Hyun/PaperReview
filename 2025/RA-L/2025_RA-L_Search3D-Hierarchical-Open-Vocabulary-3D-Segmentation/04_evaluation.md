# Evaluation

- Year/Venue: 2025 / RA-L
- Category: 3D Large Multimodal Models
- Tags: 3D Vision, semantic
- Paper link: ./2025/RA-L/2025_RA-L_Search3D-Hierarchical-Open-Vocabulary-3D-Segmentation/paper.pdf
- Code/Project: http://search3d-segmentation.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- ScanNet200
- 3RScan
- LERF

## Metrics
- accuracy
- mIoU
- AP

## Evaluation Protocol and Results
- Search3D outperforms baselines in scene-scale open-vocabulary 3D part segmentation, while maintaining strong performance in segmenting 3D objects and materials.
- For systematic evaluation, we further contribute a scene-scale open-vocabulary 3D part segmentation benchmark based on MultiScan, along with a set of open-vocabulary fine-grained part annotations on ScanNet++.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
