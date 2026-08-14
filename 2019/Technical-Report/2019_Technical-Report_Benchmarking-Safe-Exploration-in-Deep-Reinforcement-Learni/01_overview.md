# Benchmarking Safe Exploration in Deep Reinforcement Learning

- Year/Venue: 2019 / Technical Report
- Category: World Models, Safety, and Recovery
- Tags: Robotics, safe reinforcement learning, Safety Gym, Benchmark, constraints
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/openai/safety-gym
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- While “sim-to-real” transfer learning algorithms may mitigate this issue, we expect that in problems centered on AI-human interaction or very complex systems, challenges in building useful simulators will ...
- While RL is not yet fully mature or ready to serve as an “off-the-shelf” solution, it appears to offer a viable path to solving hard sequential decision-making problems ...
- The general-purpose nature of RL makes it an attractive option for a wide range of applications, including self-driving cars [Kendall et al., 2018], surgical robotics [Richter et al., ...

## Core Idea
- Towards standardizing safety specifications: Based on a range of prior work, we propose to standardize constrained RL [Altman, 1999] as the main formalism for incorporating safety specifications into ...
- First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe exploration.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- However, we highlight a few common rules that guide our discussion: • All agents that fail to satisfy constraints are strictly worse than all agents that satisfy constraints. ...
- In this section, we describe our experiments to baseline existing unconstrained and constrained RL algorithms on Safety Gym environments.
- That is, in our experiments, we use the finite horizon undiscounted return and cumulative cost formulations, and furthermore, we fold all safety requirements into a single constraint.

## Limitation
- There are a number of avenues we consider promising for future work.

## Contribution
- Second, we present the Safety Gym benchmark suite, a new slate of high-dimensional continuous control environments for measuring research progress on constrained RL.
- First, building on a wide range of prior work on safe reinforcement learning, we propose to standardize constrained RL as the main formalism for safe exploration.
- While it is currently typical to train RL agents mostly or entirely in simulation, where safety concerns are minimal, we anticipate that challenges in simulating the complexities of ...

## Abstract Cue
- Reinforcement learning (RL) agents need to explore their environments in order to learn optimal policies by trial and error.
