# Evaluation

- Year/Venue: 2022 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, behavior diversity
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/walk-these-ways
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- collision

## Evaluation Protocol and Results
- MoB facilitates this if some subset of learned behaviors outperform the gait-free policy by the new task metric.
- To start, we demonstrate generating and switching between structured gaits that are well-known in the locomotion community.
- 4.1 Sim-to-Real Transfer and Gait Switching We deploy the controller learned in simulation in the real world and first evaluate its performance on flat ground similar to the ...
- This necessitates a slow and iterative cycle of reward and environment redesign to achieve good performance on a new task.
- MoB facilitates this if some subset of learned behaviors outperform the gait-free policy by the new task metric.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
