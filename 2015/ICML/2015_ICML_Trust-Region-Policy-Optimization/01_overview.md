# Trust Region Policy Optimization

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2015 / ICML
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, policy optimization, on-policy RL
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://proceedings.mlr.press/v37/schulman15.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- For continuous control problems, methods like CMA have been successful at learning control policies for challenging tasks like locomotion when provided with hand-engineered policy classes with low-dimensional parameterizations ...
- These algorithms are scalable and can optimize nonlinear policies with tens of thousands of parameters, which have previously posed a major challenge for model-free policy search (Deisenroth et ...
- Most algorithms for policy optimization can be classified into three broad categories: (1) policy iteration methods, which alternate between estimating the value function under the current policy and ...

## Core Idea
- By making several approximations to the theoretically-justified procedure, we develop a practical algorithm, called Trust Region Policy Optimization (TRPO).
- Continuous gradient-based optimization has been very successful at learning function approximators for supervised learning tasks with huge numbers of parameters, and extending their success to reinforcement learning would ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments demonstrate its robust performance on a wide variety of tasks: learning simulated robotic swimming, hopping, and walking gaits; and playing Atari games using images of the ...
- We describe an iterative procedure for optimizing policies, with guaranteed monotonic improvement.
- Despite its approximations that deviate from the theory, TRPO tends to give monotonic improvement, with little tuning of hyperparameters.

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- Our experiments demonstrate its robust performance on a wide variety of tasks: learning simulated robotic swimming, hopping, and walking gaits; and playing Atari games using images of the ...
- By making several approximations to the theoretically-justified procedure, we develop a practical algorithm, called Trust Region Policy Optimization (TRPO).
- We describe an iterative procedure for optimizing policies, with guaranteed monotonic improvement.

## Abstract Cue
- We describe an iterative procedure for optimizing policies, with guaranteed monotonic improvement.
