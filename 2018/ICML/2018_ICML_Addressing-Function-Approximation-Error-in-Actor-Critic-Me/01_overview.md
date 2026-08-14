# Addressing Function Approximation Error in Actor-Critic Methods

- Year/Venue: 2018 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, continuous control, actor-critic
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/sfujim/TD3
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Introduction In reinforcement learning problems with discrete action spaces, the issue of value overestimation as a result of function approximation errors is well-studied.
- We show that this problem persists in an actor-critic setting and propose novel mechanisms to minimize its effects on both the actor and the critic.

## Core Idea
- Finally, we introduce a SARSA-style regularization technique which modifies the temporal difference target to bootstrap off similar state-action pairs.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We evaluate our method on the suite of OpenAI gym tasks, outperforming the state of the art in every environment tested.
- Our proposed method addresses these issues, and greatly outperforms the current state of the art.
- We draw the connection between target networks and overestimation bias, and suggest delaying policy updates to reduce per-update error and further improve performance.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We evaluate our method on the suite of OpenAI gym tasks, outperforming the state of the art in every environment tested.
- We show that this problem persists in an actor-critic setting and propose novel mechanisms to minimize its effects on both the actor and the critic.
- Our proposed method addresses these issues, and greatly outperforms the current state of the art.

## Abstract Cue
- In value-based reinforcement learning methods such as deep Q-learning, function approximation errors are known to lead to overestimated value estimates and suboptimal policies.
