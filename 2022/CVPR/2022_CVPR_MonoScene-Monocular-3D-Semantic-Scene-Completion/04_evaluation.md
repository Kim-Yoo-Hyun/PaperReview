# Evaluation

- Year/Venue: 2022 / CVPR
- Category: Foundations: 3D Semantic Occupancy
- Tags: 3D Vision, semantic, occupancy, monocular geometry
- Paper link: ./2022/CVPR/2022_CVPR_MonoScene-Monocular-3D-Semantic-Scene-Completion/paper.pdf
- Code/Project: https://github.com/cv-rits/MonoScene
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- KITTI
- SemanticKITTI
- nuScenes

## Metrics
- accuracy
- mIoU
- IoU
- mAP
- RMSE

## Evaluation Protocol and Results
- Importantly, the IoU is improved or on par (+3.87 and +0.16) which demonstrates our network captures the scene geometry while avoiding naively increasing the mIoU by lowering the ...
- On both datasets we outperform all methods by a significant mIoU margin of +4.03 on NYUv2 (Tab.
- On SemanticKITTI we get outperformed mostly on small moving objects classes (car, motorcycle, person, etc.) which we ascribe to the aggregation of moving objects in the ground truth, ...
- Note the strong interaction between IoU and mIoU since better geometry estimation (i.e. high IoU) can be achieved by invalidating semantic labels (i.e. low mIoU).
- Experiments show we outperform the literature on all metrics and datasets while hallucinating plausible scenery even beyond the camera field of view.
- Importantly, the IoU is improved or on par (+3.87 and +0.16) which demonstrates our network captures the scene geometry while avoiding naively increasing the mIoU by lowering the ...

## Baselines
- 7b), compared to baselines, MonoScene evidently captures better the scene layout, e.g. cross-roads (rows 1,3).
- We subsequently retrained all baselines.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
