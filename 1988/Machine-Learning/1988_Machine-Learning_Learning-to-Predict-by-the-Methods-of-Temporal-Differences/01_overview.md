# Learning to Predict by the Methods of Temporal Differences

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1988 / Machine Learning
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, temporal difference, Value Learning
- Official paper: https://doi.org/10.1007/BF00115009
- Code/Project: not identified
- Source audit: publisher metadata and abstract checked; convergence arguments remain UNVERIFIED.

## Why This Paper Is Here

bootstrapped value prediction의 핵심 foundation으로 Q-learning, actor-critic, advantage estimation과 robot RL을 이해하는 prerequisite다.

## Problem

완전한 episode return을 기다리지 않고 sequential prediction을 online으로 갱신한다.

## Core Idea

현재 예측과 다음-step bootstrapped target의 temporal-difference error로 value estimate를 수정한다.

## Interface

state-transition-reward stream을 value prediction으로 변환하는 learning component다.

## Evaluation Scope

random-walk류 prediction task와 이론 분석이 중심이며 robot control은 직접 평가하지 않는다.
