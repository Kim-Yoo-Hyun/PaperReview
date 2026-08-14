# Evaluation

- Year/Venue: 2022 / RSS
- Category: Robotics-Enabling 3D Perception
- Tags: Robotics, 3D Vision, scene flow, articulated objects, point cloud, manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://flowbot3d.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- PartNet
- PartNet-Mobility
- ManiSkill

## Metrics
- accuracy
- success rate
- collision

## Evaluation Protocol and Results
- Results show that our system achieves state-of-theart performance in both simulated and real-world experiments.
- We then deploy an analytical motion planner based on this vector field to achieve a policy that yields maximum articulation.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
