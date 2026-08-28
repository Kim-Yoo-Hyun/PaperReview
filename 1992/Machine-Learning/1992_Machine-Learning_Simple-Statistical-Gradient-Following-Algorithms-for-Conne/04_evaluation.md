# Evaluation — Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Policy Gradient, REINFORCE
- Official paper: https://doi.org/10.1007/BF00992696
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; estimator derivation remains UNVERIFIED.

## Protocol

connectionist learning examples와 estimator 분석이 중심이며 modern continuous-control benchmark는 없다.

## Limitations and Reproducibility

gradient variance와 sample inefficiency가 크며 safety constraint를 직접 다루지 않는다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
