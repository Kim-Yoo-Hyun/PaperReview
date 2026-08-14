# Evaluation

- Year/Venue: 2021 / CoRL
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, locomotion, Reinforcement Learning, massively parallel simulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://leggedrobotics.github.io/legged_gym/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- mAP
- success rate

## Evaluation Protocol and Results
- 4, we compare these results with the baseline, which allows us to select the most favorable trade-off between policy performance and training time.
- We then conduct experiments in which we increase the number of robots while keeping the batch size constant.
- Using this very large batch size results in the best policy but at the cost of a relatively long training time.
- : In this work, we present and study a training set-up that achieves fast policy generation for real-world robotic tasks by using massive parallelism on a single workstation ...
- 4, we compare these results with the baseline, which allows us to select the most favorable trade-off between policy performance and training time.

## Baselines
- 4, we compare these results with the baseline, which allows us to select the most favorable trade-off between policy performance and training time.
- We begin by setting a baseline with nrobots = 20000 and nsteps = 50, resulting in a batch size of 1M samples.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
