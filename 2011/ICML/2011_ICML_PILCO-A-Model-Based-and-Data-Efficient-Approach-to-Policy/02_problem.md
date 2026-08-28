# Problem — PILCO: A Model-Based and Data-Efficient Approach to Policy Search

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2011 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, model-based RL, Gaussian Process
- Official paper: https://www.deisenroth.cc/publication/deisenroth-2011-c/
- Code/Project: not identified
- Source audit: author publication page and abstract checked; derivations and result magnitudes remain UNVERIFIED.

## Target Problem and Assumptions

실제 시스템에서 많은 interaction 없이 continuous-control policy를 학습한다.

## Closed-Loop Position

state-action transition data를 learned dynamics와 continuous control policy로 연결한다.

## Audit Questions

정독 시 가정이 실제 robot dynamics, partial observability, contact와 distribution shift에서 유지되는지 확인한다.
