# Constrained Policy Optimization

- Year/Venue: 2017 / ICML
- Category: World Models, Safety, and Recovery
- Tags: Robotics, safe reinforcement learning, constraints, policy optimization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/jachiam/cpo
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- For many applications of reinforcement learning it can be more convenient to specify both a reward function and constraints, rather than trying to design behavior through the reward ...
- For example, systems that physically interact with or around humans should satisfy safety constraints.
- Recent advances in policy search algorithms (Mnih et al., 2016; Schulman et al., 2015; Lillicrap et al., 2016; Levine et al., 2016) have enabled new capabilities in highdimensional ...

## Core Idea
- Our method allows us to train neural network policies for high-dimensional control while making guarantees about policy behavior all throughout training.
- We propose Constrained Policy Optimization (CPO), the first general-purpose policy search algorithm for constrained reinforcement learning with guarantees for near-constraint satisfaction at each iteration.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Introduction Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using pixels as inputs) (Mnih et ...
- Recent work in deep RL assumes that agents are free to explore any behavior during learning, so long as it leads to performance improvement.
- We demonstrate the effectiveness of our approach on simulated robot locomotion tasks where the agent must satisfy constraints motivated by safety.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method allows us to train neural network policies for high-dimensional control while making guarantees about policy behavior all throughout training.
- We demonstrate the effectiveness of our approach on simulated robot locomotion tasks where the agent must satisfy constraints motivated by safety.
- Introduction Recently, deep reinforcement learning has enabled neural network policies to achieve state-of-the-art performance on many high-dimensional control tasks, including Atari games (using pixels as inputs) (Mnih et ...

## Abstract Cue
- For many applications of reinforcement learning it can be more convenient to specify both a reward function and constraints, rather than trying to design behavior through the reward function.
