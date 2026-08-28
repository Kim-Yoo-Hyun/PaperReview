# Q-Learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1992 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Q-learning, Value Learning
- Official paper: https://doi.org/10.1007/BF00992698
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; proof conditions remain UNVERIFIED.

## Why This Paper Is Here

model-free off-policy action-value learning의 고전으로 DQN, offline Q-learning과 recovery option value 비교의 기반이다.

## Problem

transition model 없이 trial-and-error data로 optimal action policy를 학습한다.

## Core Idea

reward와 다음 상태의 최대 action value를 이용한 TD update로 action-value function을 갱신한다.

## Interface

state-action-reward-next-state samples를 discrete action selection용 Q-value로 변환한다.

## Evaluation Scope

tabular setting의 이론과 예제가 중심이며 high-dimensional robotics 적용은 후속 연구 영역이다.
