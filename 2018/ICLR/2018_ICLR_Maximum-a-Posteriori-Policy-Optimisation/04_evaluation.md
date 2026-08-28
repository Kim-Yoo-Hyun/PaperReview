# Evaluation — Maximum a Posteriori Policy Optimisation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / ICLR
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, policy optimization, Off-Policy Learning
- Official paper: https://openreview.net/forum?id=S1ANxQW0b
- Code/Project: not identified
- Source audit: official OpenReview abstract checked; derivation and experimental details remain UNVERIFIED.

## Protocol

continuous-control benchmark에서 on/off-policy baselines와 비교하며 robot-scale 적용은 후속 MT-Opt에서 확인한다.

## Limitations and Reproducibility

critic quality, hyperparameter와 replay distribution에 의존하며 offline safety는 직접 보장하지 않는다.

정독 시 embodiment, simulator/real robot, split, metric, baseline, trial count, code/checkpoint와 compute dependency를 표로 확정한다.
