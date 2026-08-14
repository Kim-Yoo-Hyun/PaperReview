# Evaluation

- Year/Venue: 2020 / NeurIPS
- Category: Robot Learning and Data
- Tags: Robotics, offline reinforcement learning, model-based RL, distribution shift
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/tianheyu927/mopo
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- ImageNet

## Metrics
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Evaluation Protocol and Results
- In our experiments, we aim to study the follow questions: (1) How does MOPO perform on standard offline RL benchmarks in comparison to prior state-of-the-art approaches? (2) Can ...
- We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms.
- 5.1 Evaluation on the D4RL benchmark To answer question (1), we evaluate our method on a large subset of datasets in the D4RL benchmark based on the MuJoCo ...
- To answer question (3), we conduct a complete ablation study to analyze the effect of each module in MOPO in Appendix D.
- Our algorithm, Model-based Offline Policy Optimization (MOPO), outperforms standard model-based RL algorithms and prior state-of-the-art model-free offline RL algorithms on existing offline RL benchmarks and two challenging continuous ...
- In our experiments, we aim to study the follow questions: (1) How does MOPO perform on standard offline RL benchmarks in comparison to prior state-of-the-art approaches? (2) Can ...

## Baselines
- We compare against several baselines, including the current state-of-the-art model-free offline RL algorithms.
- In our experiments, we aim to study the follow questions: (1) How does MOPO perform on standard offline RL benchmarks in comparison to prior state-of-the-art approaches? (2) Can ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
