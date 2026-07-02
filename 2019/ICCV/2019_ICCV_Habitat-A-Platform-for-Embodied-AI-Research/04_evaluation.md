# Evaluation

- Year/Venue: 2019 / ICCV
- Category: Benchmarks and Datasets
- Tags: Robotics, Navigation, Embodied AI, Benchmark
- Paper link: ./2019/ICCV/2019_ICCV_Habitat-A-Platform-for-Embodied-AI-Research/paper.pdf
- Code/Project: https://aihabitat.org/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- COCO
- Matterport3D
- Replica
- Habitat
- AI2-THOR

## Metrics
- mAP
- SPL
- collision

## Evaluation Protocol and Results
- Specifically, in the context of point-goal navigation: (1) we revisit the comparison between learning and SLAM approaches from two recent works and find evidence for the opposite conclusion ...
- Habitat-Sim is fast – when rendering a scene from Matterport3D, it achieves several thousand frames per second (fps) running single-threaded, and can reach over 10,000 fps multi-process on ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
