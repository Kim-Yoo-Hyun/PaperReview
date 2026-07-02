# Evaluation

- Year/Venue: 2020 / ECCV
- Category: Foundations: 3D Detection and BEV Perception
- Tags: 3D Vision, BEV, sensor fusion, camera
- Paper link: ./2020/ECCV/2020_ECCV_Lift-Splat-Shoot-Encoding-Images-from-Arbitrary-Camera-Rig/paper.pdf
- Code/Project: https://github.com/nv-tlabs/lift-splat-shoot
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- KITTI
- nuScenes
- Waymo

## Metrics
- accuracy
- IoU
- mAP

## Evaluation Protocol and Results
- On standard bird’seye-view tasks such as object segmentation and map segmentation, our model outperforms all baselines and prior work.
- In pursuit of the goal of learning dense representations for motion planning, we show that the representations inferred by our model enable interpretable end-to-end motion planning by “shooting” ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
