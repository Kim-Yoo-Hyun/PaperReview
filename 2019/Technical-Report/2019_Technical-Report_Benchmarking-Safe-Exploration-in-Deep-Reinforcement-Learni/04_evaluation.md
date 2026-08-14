# Evaluation

- Year/Venue: 2019 / Technical Report
- Category: World Models, Safety, and Recovery
- Tags: Robotics, safe reinforcement learning, Safety Gym, Benchmark, constraints
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/openai/safety-gym
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Dataset / Benchmark
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Metrics
- mAP

## Evaluation Protocol and Results
- However, we highlight a few common rules that guide our discussion: • All agents that fail to satisfy constraints are strictly worse than all agents that satisfy constraints. ...
- In this section, we describe our experiments to baseline existing unconstrained and constrained RL algorithms on Safety Gym environments.
- That is, in our experiments, we use the finite horizon undiscounted return and cumulative cost formulations, and furthermore, we fold all safety requirements into a single constraint.
- 5.1 Methods: Evaluation Protocol Optimization Problem: We evaluate agents based on the optimization problem X T max E rt τ ∼πθ πθ t=0 X T s.t.
- However, we highlight a few common rules that guide our discussion: • All agents that fail to satisfy constraints are strictly worse than all agents that satisfy constraints. ...
- In this section, we describe our experiments to baseline existing unconstrained and constrained RL algorithms on Safety Gym environments.

## Baselines
- In this section, we describe our experiments to baseline existing unconstrained and constrained RL algorithms on Safety Gym environments.
- That is, A1 A2 if Jr (A1 ) ≥ Jr (A2 ) J (A ) > Jr (A2 ) or r 1 ρc (A1 ) < ρc (A2 ...

## Reproducibility Notes
- 자동 추출 기준으로 확인된 내용만 위에 기록했다. dataset, split, hyperparameter, code availability는 `paper.pdf`의 experiment section과 공식 repository를 추가 확인해야 한다.
