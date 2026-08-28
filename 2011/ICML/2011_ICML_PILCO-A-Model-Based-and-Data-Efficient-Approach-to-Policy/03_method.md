# Method — PILCO: A Model-Based and Data-Efficient Approach to Policy Search

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2011 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, model-based RL, Gaussian Process
- Official paper: https://www.deisenroth.cc/publication/deisenroth-2011-c/
- Code/Project: not identified
- Source audit: author publication page and abstract checked; derivations and result magnitudes remain UNVERIFIED.

## Pipeline

Gaussian-process dynamics의 predictive uncertainty를 장기 cost prediction에 전파하고 analytic policy gradient를 계산한다.

## Interface

state-action transition data를 learned dynamics와 continuous control policy로 연결한다.

## Implementation Audit

Loss/objective, representation, data scale, temporal horizon, control rate와 hardware detail은 원문의 section/page와 함께 보강한다.
