# Evaluation

- Year/Venue: 2021 / NeurIPS
- Category: Foundations: SLAM and Sensor Geometry
- Tags: SLAM, RGB-D, geometry
- Paper link: ./2021/NeurIPS/2021_NeurIPS_DROID-SLAM-Deep-Visual-SLAM-for-Monocular-Stereo-and-RGB-D/paper.pdf
- Code/Project: https://github.com/princeton-vl/DROID-SLAM
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ScanNet
- ETH3D
- EuRoC

## Metrics
- accuracy
- mAP
- ATE

## Evaluation Protocol and Results
- Monocular ORB-SLAM DeepV2D TartanVO Ours MH000 1.30 6.15 4.88 0.08 MH001 0.04 2.12 0.26 0.05 MH002 2.37 4.54 2.00 0.04 MH003 2.45 3.89 0.94 0.02 MH004 X 2.71 ...
- Following prior work, we evaluate the accuracy of the camera trajectory , primarily using Absolute Trajectory Error (ATE) .
- Despite training on monocular video, it can leverage stereo or RGB-D video to achieve improved performance at test time.
- Monocular ORB-SLAM DeepV2D TartanVO Ours MH000 1.30 6.15 4.88 0.08 MH001 0.04 2.12 0.26 0.05 MH002 2.37 4.54 2.00 0.04 MH003 2.45 3.89 0.94 0.02 MH004 X 2.71 ...

## Baselines
- We compare to both deep learning and established classical SLAM algorithms and put specific emphasis on cross-dataset generalization.
- While some datasets have ground truth point clouds , there is no standard protocol to compare 3D reconstructions directly given by SLAM systems because a SLAM systems can ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
