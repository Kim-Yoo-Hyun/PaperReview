# Evaluation

- Year/Venue: 2022 / ECCV
- Category: Sensor Fusion, LiDAR, and Autonomous Driving
- Tags: sensor fusion, 3D perception, Planning
- Paper link: ./2022/ECCV/2022_ECCV_BEVFormer-Learning-Bird-s-Eye-View-Representation-from-Mul/paper.pdf
- Code/Project: https://github.com/fundamentalvision/BEVFormer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- nuScenes
- Waymo

## Metrics
- accuracy
- IoU
- AP
- mAP
- NDS
- ATE

## Evaluation Protocol and Results
- 4.1 Datasets We conduct experiments on two challenging public autonomous driving datasets, namely nuScenes dataset and Waymo open dataset .
- The mean average precision (mAP) of nuScenes is computed using the center distance on the ground plane rather than the 3D Intersection over Union (IoU) to match the ...
- Our approach achieves the new state-of-the-art 56.9% in terms of NDS metric on the nuScenes test set, which is 9.0 points higher than previous best arts and on ...
- We further show that BEVFormer remarkably improves the accuracy of velocity estimation and recall of objects under low visibility conditions.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
