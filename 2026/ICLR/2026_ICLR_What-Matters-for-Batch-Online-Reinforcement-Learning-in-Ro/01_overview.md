# What Matters for Batch Online Reinforcement Learning in Robotics?

- Year/Venue: 2026 / ICLR Poster
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, batch online RL, real robot
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://pd-perry.github.io/batch-online-rl/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- In this work, we perform a systematic empirical study to investigate what enables effective batch online RL in robotics with the goal of providing a general recipe to ...
- Prior approaches to the batch online RL problem in robotics often focus on IL or filtered-IL methods as approaches that are easy to carry out.
- IL methods have inherent limitations in their ability to leverage suboptimal demonstrations within autonomously collected datasets, while methods based on weighted or filtered IL often have diminishing returns ...

## Core Idea
- On top of the recipe, we propose a simple practical addition to induce even more diversity and achieve better sample efficiency: applying a small amount of temporally correlated ...
- Based on this analysis, we propose a general recipe for effective batch online RL.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We then show a simple addition to the recipe, namely using temporally-correlated noise to obtain more diversity, results in further performance gains.
- Yet, despite the promise of this paradigm, it remains challenging to achieve due to algorithms not being able to learn effectively from the autonomous data.
- : The ability to learn from large batches of autonomously collected data for policy improvement—a paradigm we refer to as batch online reinforcement learning—holds the promise of enabling ...

## Limitation
- For researchers, we bring to attention open questions for future work to optimize each component of the recipe further.

## Contribution
- For example, prior works have applied imitation learning and filtered imitation learning methods to the batch online RL problem, but these algorithms often fail to efficiently improve from ...
- Based on this analysis, we propose a general recipe for effective batch online RL.
- We then show a simple addition to the recipe, namely using temporally-correlated noise to obtain more diversity, results in further performance gains.

## Abstract Cue
- : The ability to learn from large batches of autonomously collected data for policy improvement—a paradigm we refer to as batch online reinforcement learning—holds the promise of enabling truly scalable robot learning by significantly reducing the need for human effort of data collection while getting ...
