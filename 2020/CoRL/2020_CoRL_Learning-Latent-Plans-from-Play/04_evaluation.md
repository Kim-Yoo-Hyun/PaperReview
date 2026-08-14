# Evaluation

- Year/Venue: 2020 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, learning from play, latent plans
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://learning-from-play.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- accuracy
- mAP

## Evaluation Protocol and Results
- The motivation of the state experiments is to understand the how all methods compare on the control problem independent of visual representation learning, which could potentially be improved ...
- In our experiments, we aim to answer the following questions: 1) Can a single play-supervised policy generalize to a wide variety of user-specified visual manipulation tasks, despite not ...
- 3) Does decoupling latent plan inference and plan decoding into independent problems, as is done in Play-LMP, improve performance over goal-conditioned Behavioral Cloning (Play-GCBC), (which does no explicit ...
- We define two sets of experiments over these datasets: pixel experiments, where we study the multitask visual manipulation problem, and state experiments, where we ignore the visual representation ...
- The motivation of the state experiments is to understand the how all methods compare on the control problem independent of visual representation learning, which could potentially be improved ...
- To learn control from play, we introduce Play-LMP, a selfsupervised method that learns to organize play behaviors in a latent space, then reuse them at test time to ...

## Baselines
- We additionally train a single multi-task behavioral cloning baseline conditioned on state and task id, Multitask BC (Rahmatizadeh et al. ), trained on all 18 BC expert demonstration ...
- To compare our play-supervised models to a conventional scenario, we collect a training set of 100 expert demonstrations per task in the environment, and train one behavioral cloning ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
