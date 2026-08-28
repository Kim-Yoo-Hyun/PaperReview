# Human-level control through deep reinforcement learning

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2015 / Nature
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Deep Q-Network, Value Learning
- Official paper: https://doi.org/10.1038/nature14236
- Code/Project: not identified
- Source audit: publisher abstract and metadata checked; architecture and result details remain UNVERIFIED.

## Why This Paper Is Here

DeepMind의 DQN으로 representation learning과 Q-learning을 결합한 deep RL의 핵심 foundation이다.

## Problem

고차원 pixel observation에서 직접 action-value policy를 학습한다.

## Core Idea

convolutional Q-network에 experience replay와 target network를 결합해 학습 안정성을 높인다.

## Interface

image frame history를 discrete action Q-values로 매핑한다.

## Evaluation Scope

Atari game suite에서 단일 알고리즘의 성능을 비교하며 robotics embodiment는 직접 다루지 않는다.
