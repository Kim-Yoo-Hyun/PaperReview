# Evaluation

- Year/Venue: 2023 / CVPR
- Category: Open-Vocabulary 3D Mapping
- Tags: open-vocabulary, 3D semantic, CLIP
- Paper link: ./2023/CVPR/2023_CVPR_OpenScene-3D-Scene-Understanding-with-Open-Vocabularies/paper.pdf
- Code/Project: https://pengsongyou.github.io/openscene
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- Matterport3D
- KITTI
- nuScenes
- Waymo

## Metrics
- accuracy
- mIoU
- mAP

## Evaluation Protocol and Results
- For example, given the house shown in Figure 1, we would like to predict which surfaces are part of a fan (semantics), made of metal (materials), within a ...
- Traditional 3D scene understanding systems are trained with supervision from benchmark datasets designed for specific tasks (e.g., 3D semantic segmentation for a closed set of 20 classes ).

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
