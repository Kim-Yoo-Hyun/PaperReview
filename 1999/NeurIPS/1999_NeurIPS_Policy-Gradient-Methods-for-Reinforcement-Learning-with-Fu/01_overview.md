# Policy Gradient Methods for Reinforcement Learning with Function Approximation

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 1999 / NeurIPS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, Policy Gradient, actor-critic
- Official paper: https://proceedings.neurips.cc/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
- Code/Project: not identified
- Source audit: official proceedings abstract checked; theorem and experiment details remain UNVERIFIED.

## Why This Paper Is Here

function approximation 하 policy-gradient theorem과 actor-critic 구조를 정립한 핵심 RL foundation이다.

## Problem

parameterized stochastic policy의 average performance gradient를 value approximation과 함께 계산한다.

## Core Idea

policy-gradient theorem과 compatible function approximation 조건을 제시하고 actor-critic update를 연결한다.

## Interface

state-action trajectories와 critic estimate를 policy parameter update로 변환한다.

## Evaluation Scope

이론과 소규모 실험이 중심이며 robot manipulation/locomotion 평가는 후속 연구에서 이루어진다.
