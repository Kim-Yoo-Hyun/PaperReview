# Hindsight Experience Replay

- Year/Venue: 2017 / NeurIPS
- Category: Robotics Foundations: Robot Learning
- Tags: Robotics, Reinforcement Learning, goal-conditioned RL, sparse rewards
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/openai/baselines
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Reinforcement learning (RL) combined with neural networks has recently led to a wide range of successes in learning policies for sequential decision-making problems.
- However, a common challenge, especially for robotics, is the need to engineer a reward function that not only reflects the task at hand but is also carefully shaped ...
- For example, Popov et al. (2017) use a cost function consisting of five relatively complicated terms which need to be carefully weighted in order to train a policy ...

## Core Idea
- Our approach is based on training universal policies (Schaul et al., 2015a) which take as input not only the current state, but also a goal state.
- We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need for complicated reward ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 4.6 we show the results of the experiments on the physical robot.
- 4.3 we check if HER improves performance in the single-goal setup.
- In particular, we run experiments on three different tasks: pushing, sliding, and pick-and-place, in each case using only binary rewards indicating whether or not the task is completed.

## Limitation
- We showed that HER allows training policies which push, slide and pick-and-place objects with a robotic arm to the specified positions while the vanilla RL algorithm fails to ...

## Contribution
- Our ablation studies show that Hindsight Experience Replay is a crucial ingredient which makes training possible in these challenging environments.
- We demonstrate our approach on the task of manipulating objects with a robotic arm.
- We present a novel technique called Hindsight Experience Replay which allows sample-efficient learning from rewards which are sparse and binary and therefore avoid the need for complicated reward ...

## Abstract Cue
- Dealing with sparse rewards is one of the biggest challenges in Reinforcement Learning (RL).
