# Apprenticeship Learning via Inverse Reinforcement Learning

- Year/Venue: 2004 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Imitation Learning, inverse reinforcement learning, apprenticeship learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://ai.stanford.edu/~pabbeel/irl/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Introduction Given a sequential decision making problem posed in the Markov decision process (MDP) formalism, a number of standard algorithms exist for finding an optimal or near-optimal policy.
- The MDP formalism is useful for many problems because it is often easier to specify the reward function than to directly specify the value function (and/or optimal policy).
- However, we believe that even the reward function is frequently difficult to specify manually.

## Core Idea
- We consider learning in a Markov decision process where we are not explicitly given a reward function, but where instead we can observe an expert demonstrating the task ...
- This setting is useful in applications (such as the task of driving) where it may be difficult to write down an explicit reward function specifying exactly how different ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We think of the expert as trying to maximize a reward function that is expressible as a linear combination of known features, and give an algorithm for learning ...
- We show that our algorithm terminates in a small number of iterations, and that even though we may never recover the expert’s reward function, the policy output by ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We think of the expert as trying to maximize a reward function that is expressible as a linear combination of known features, and give an algorithm for learning ...
- We show that our algorithm terminates in a small number of iterations, and that even though we may never recover the expert’s reward function, the policy output by ...
- Introduction Given a sequential decision making problem posed in the Markov decision process (MDP) formalism, a number of standard algorithms exist for finding an optimal or near-optimal policy.

## Abstract Cue
- We consider learning in a Markov decision process where we are not explicitly given a reward function, but where instead we can observe an expert demonstrating the task that we want to learn to perform.
