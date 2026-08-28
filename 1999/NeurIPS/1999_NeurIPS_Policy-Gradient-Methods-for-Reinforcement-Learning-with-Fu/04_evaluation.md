# Evaluation — Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1999 / NeurIPS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Policy Gradient, actor-critic
- Official paper: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Code/Project: not identified
- Source audit: official proceedings abstract checked; theorem and experiment details remain UNVERIFIED.

## Protocol

이론과 소규모 실험이 중심이며 robot manipulation/locomotion 평가는 후속 연구에서 이루어진다.

## Limitations and Reproducibility

on-policy sampling과 variance, stability 문제가 남아 TRPO/PPO류가 필요하다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
