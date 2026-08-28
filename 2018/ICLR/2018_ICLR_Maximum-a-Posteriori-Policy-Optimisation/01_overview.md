# Maximum a Posteriori Policy Optimisation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2018 / ICLR
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, policy optimization, Off-Policy Learning
- Official paper: https://openreview.net/forum?id=S1ANxQW0b
- Code/Project: not identified
- Source audit: official OpenReview abstract checked; derivation and experimental details remain UNVERIFIED.

## Why This Paper Is Here

DeepMind의 MPO로 안정적인 off-policy continuous-control policy optimization을 정립해 MT-Opt류 scalable robot RL의 직접 기반이 된다.

## Problem

sample-efficient off-policy learning에서 large policy update가 만드는 instability를 제한한다.

## Core Idea

relative-entropy constrained E-step policy improvement와 supervised M-step projection을 번갈아 수행한다.

## Interface

replay trajectories와 critic estimates를 continuous stochastic policy update로 변환한다.

## Evaluation Scope

continuous-control benchmark에서 on/off-policy baselines와 비교하며 robot-scale 적용은 후속 MT-Opt에서 확인한다.
