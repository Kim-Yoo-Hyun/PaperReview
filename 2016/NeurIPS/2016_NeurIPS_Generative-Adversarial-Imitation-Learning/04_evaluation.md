# Evaluation

- Year/Venue: 2016 / NeurIPS
- Category: Foundations: RL and Imitation Learning
- Tags: Robotics, Imitation Learning, Reinforcement Learning
- Paper link: ./2016/NeurIPS/2016_NeurIPS_Generative-Adversarial-Imitation-Learning/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Evaluation Protocol and Results
- Our algorithm almost always achieved at least 70% of expert performance for all dataset
- We were able to slightly improve our algorithm’s performance on Reacher using causal entropy regularization—in the 4-trajectory setting, the improvement from λ = 0 to λ = 10−3 ...
- We evaluated Algorithm 1 against baselines on 9 physics-based control tasks, ranging from lowdimensional control tasks from the classic RL literature—the cartpole , acrobot , and mountain car ...
- Then, to evaluate imitation performance with respect to sample complexity of expert data, we sampled datasets of varying trajectory counts from the expert policies.
- Our algorithm almost always achieved at least 70% of expert performance for all dataset
- We were able to slightly improve our algorithm’s performance on Reacher using causal entropy regularization—in the 4-trajectory setting, the improvement from λ = 0 to λ = 10−3 ...

## Baselines
- We evaluated Algorithm 1 against baselines on 9 physics-based control tasks, ranging from lowdimensional control tasks from the classic RL literature—the cartpole , acrobot , and mountain car ...
- We tested Algorithm 1 against three baselines: 1.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
