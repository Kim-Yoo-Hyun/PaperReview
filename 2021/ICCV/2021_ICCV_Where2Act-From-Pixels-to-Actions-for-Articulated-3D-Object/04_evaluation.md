# Evaluation

- Year/Venue: 2021 / ICCV
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, affordance, articulated objects, active perception, point cloud
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://cs.stanford.edu/~kaichun/where2act/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet
- Replica
- PartNet
- PartNet-Mobility

## Metrics
- accuracy
- mAP
- F-score
- SR
- success rate

## Evaluation Protocol and Results
- We show two high-rated proposals (left) and two with lower scores (right) due to interaction orientations and potential robot-object collisions.
- We propose, discuss, and evaluate novel network architectures that given image and depth data, predict the set of actions possible at each pixel, and the regions over articulated ...

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
