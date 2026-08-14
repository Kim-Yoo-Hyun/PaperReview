# Evaluation

- Year/Venue: 2016 / Autonomous Robots
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, humanoid, whole-body control, momentum control, inverse dynamics
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://is.mpg.de/am/publications/herzog_momentum_2016
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- mAP

## Evaluation Protocol and Results
- A summary of the experiments is shown in the attached movie 4 .
- The performance of the controller was evaluated in different scenarios: balancing experiments and a tracking task in single and double support.
- For all the experiments, we run the hierarchical inverse
- We formulated balancing and motion tracking tasks using the algorithm discussed in Section 2 together with the momentum controller discussed in Section 3 and evaluated them on the ...
- Our results demonstrate that hierarchical inverse dynamics together with momentum control can be efficiently used for feedback control under real robot conditions.
- Using a reformulation of existing algorithms, we propose a simplification of the problem that allows to achieve real-time control.

## Baselines
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
