# Method

- Year/Venue: 2017 / NeurIPS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, goal-conditioned RL, sparse rewards
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/openai/baselines
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- Our approach is based on training universal policies (Schaul et al., 2015a) which take as input not only the current state, but also a goal state.
- We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need for complicated reward ...
- In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can be combined with ...

## 원리적 동기
- Reinforcement learning (RL) combined with neural networks has recently led to a wide range of successes in learning policies for sequential decision-making problems.
- However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is also carefully shaped ...
- Our approach is based on training universal policies (Schaul et al., 2015a) which take as input not only the current state, but also a goal state.

## 핵심 방법론
- Our approach is based on training universal policies (Schaul et al., 2015a) which take as input not only the current state, but also a goal state.
- In this paper we introduce a technique called Hindsight Experience Replay (HER) which allows the algorithm to perform exactly this kind of reasoning and can be combined with ...
