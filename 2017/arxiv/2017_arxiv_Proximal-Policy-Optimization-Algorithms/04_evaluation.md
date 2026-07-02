# Evaluation

- Year/Venue: 2017 / arxiv
- Category: Foundations: RL and Imitation Learning
- Tags: Reinforcement Learning, policy learning, Robotics
- Paper link: ./2017/arxiv/2017_arxiv_Proximal-Policy-Optimization-Algorithms/paper.pdf
- Code/Project: https://github.com/openai/baselines
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Evaluation Protocol and Results
- 6.1 Comparison of Surrogate Objectives First, we compare several different surrogate objectives under different hyperparameters.
- Here, we compare the surrogate objective LCLIP to several natural variations and ablated versions.
- No clipping or penalty: Lt (θ) = rt (θ)Ât Clipping: Lt (θ) = min(rt (θ)Ât , clip(rt (θ)), 1 − , 1 + )Ât KL penalty (fixed or ...
- Our experiments test PPO on a collection of benchmark tasks, including simulated robotic locomotion and Atari game playing, and we show that PPO outperforms other online policy gradient ...

## Baselines
- 6.1 Comparison of Surrogate Objectives First, we compare several different surrogate objectives under different hyperparameters.
- Here, we compare the surrogate objective LCLIP to several natural variations and ablated versions.

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
