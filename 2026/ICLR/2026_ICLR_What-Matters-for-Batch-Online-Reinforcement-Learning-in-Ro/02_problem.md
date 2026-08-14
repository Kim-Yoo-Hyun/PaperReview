# Problem

- Year/Venue: 2026 / ICLR Poster
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, batch online RL, real robot
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://pd-perry.github.io/batch-online-rl/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## 왜 문제인가
- In this work, we perform a systematic empirical study to investigate what enables effective batch online RL in robotics with the goal of providing a general recipe to ...
- Prior approaches to the batch online RL problem in robotics often focus on IL or filtered-IL methods as approaches that are easy to carry out.
- IL methods have inherent limitations in their ability to leverage suboptimal demonstrations within autonomously collected datasets, while methods based on weighted or filtered IL often have diminishing returns ...

## 해결하려는 문제
- For example, prior works have applied imitation learning and filtered imitation learning methods to the batch online RL problem, but these algorithms often fail to efficiently improve from ...
- Based on this analysis, we propose a general recipe for effective batch online RL.
- We then show a simple addition to the recipe, namely using temporally-correlated noise to obtain more diversity, results in further performance gains.

## 선행 연구 / 배경 단서
- In this work, we perform a systematic empirical study to investigate what enables effective batch online RL in robotics with the goal of providing a general recipe to ...
- Prior approaches to the batch online RL problem in robotics often focus on IL or filtered-IL methods as approaches that are easy to carry out.
- Learning from autonomously collected data for policy improvement, however, remains a significant challenge in robot learning as current algorithms struggle to fully leverage this autonomous data .
