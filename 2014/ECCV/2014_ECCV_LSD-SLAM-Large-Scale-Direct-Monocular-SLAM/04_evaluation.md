# Evaluation

- Year/Venue: 2014 / ECCV
- Category: Foundations: SLAM and Sensor Geometry
- Tags: 3D Vision, SLAM, monocular geometry, 3D reconstruction
- Paper link: ./2014/ECCV/2014_ECCV_LSD-SLAM-Large-Scale-Direct-Monocular-SLAM/paper.pdf
- Code/Project: https://github.com/tum-vision/lsd_slam
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- TUM RGB-D

## Metrics
- accuracy
- mAP
- RMSE
- SR

## Evaluation Protocol and Results
- 4.1 Qualitative Results on Large Trajectories We tested the algorithm on several long and challenging trajectories, which include many camera rotations, large scale changes and major loop closures.
- Some of the evaluated trajectories are shown in full in the supplementary video.
- We evaluate LSD-SLAM both quantitatively on publicly available datasets as well as on challenging outdoor trajectories, recorded with a hand-held monocular camera.
- We propose a direct (feature-less) monocular SLAM algorithm which, in contrast to current state-of-the-art regarding direct methods, allows to build large-scale, consistent maps of the environment.
- 4.1 Qualitative Results on Large Trajectories We tested the algorithm on several long and challenging trajectories, which include many camera rotations, large scale changes and major loop closures.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
