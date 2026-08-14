# RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation

- Year/Venue: 2023 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, generalist policy, cross-embodiment, self-improvement, robot manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://deepmind.google/discover/blog/robocat-a-self-improving-robotic-agent/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- This is because, even though the cost of task design and robot experience generation is very high, leveraging heterogeneous robot data at scale has remained a challenging problem ...

## Core Idea
- Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation.
- The latter allows us to compare the benefit of training on diverse robotic ma13 Published in Transactions on Machine Learning Research (12/2023) Embodiment Sawyer 7-DoF Simulation Real World ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement ...
- With RoboCat, we demonstrate the ability to generalise to new tasks and robots, both zero-shot as well as through adaptation using only 100–1000 examples for the target task.
- We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new ...

## Limitation
- While our reward labelling process to determine successful and desired behaviours is a starting point for this, future work should consider adapting alignment techniques successfully used for language ...
- In addition, since RoboCat takes actions in the physical world—and on multiple embodiments—it may pose new challenges with respect to safety.
- Such a self-improvement loop poses additional challenges with respect to AGI safety since it, partially, implements a reinforcement learning loop; which comes with its own safety concerns (see ...

## Contribution
- We also show how a trained model itself can be used to generate data for subsequent training iterations, thus providing a basic building block for an autonomous improvement ...
- We find that as we grow and diversify its training data, RoboCat not only shows signs of cross-task transfer, but also becomes more efficient at adapting to new ...
- Inspired by recent advances in foundation models for vision and language, we propose a multi-embodiment, multi-task generalist agent for robotic manipulation.

## Abstract Cue
- The ability to leverage heterogeneous robotic experience from different robots and tasks to quickly master novel skills and embodiments has the potential to transform robot learning.
