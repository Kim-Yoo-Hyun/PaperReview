# BridgeData V2: A Dataset for Robot Learning at Scale

- Year/Venue: 2023 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Dataset, Imitation Learning, robot manipulation, data scaling, generalization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://rail-berkeley.github.io/bridgedata/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- However, in practice, assembling a dataset with the right features to accelerate research in large-scale robot learning presents a significant challenge.
- Many existing robot datasets contain only one or a few environments and tasks , meaning a researcher would need to exactly replicate a scene from the data to ...
- BridgeData V2 contains 60,096 trajectories collected across 24 environments on a publicly available low-cost robot.

## Core Idea
- Project page: https://rail-berkeley.github.io/bridgedata/ Many Skills 24 Environments move the green cloth from the left burner to the right burner remove the carrot from the drawer and put it ...
- In this paper, we propose a new dataset, which we call BridgeData V2 (Figure 1) because it greatly expands on the previously released Bridge Dataset .

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In our experiments, we train 6 state-of-the-art imitation learning and offline reinforcement learning methods on our dataset, and find that they succeed on a suite of tasks requiring ...
- We also demonstrate that the performance of these methods improves with more data and higher capacity models, and that training on a greater variety of skills leads to ...
- The goal of our experiments is to evaluate the utility of our dataset for testing a variety of multi-task offline learning methods.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We also demonstrate that the performance of these methods improves with more data and higher capacity models, and that training on a greater variety of skills leads to ...
- In our experiments, we train 6 state-of-the-art imitation learning and offline reinforcement learning methods on our dataset, and find that they succeed on a suite of tasks requiring ...
- Project page: https://rail-berkeley.github.io/bridgedata/ Many Skills 24 Environments move the green cloth from the left burner to the right burner remove the carrot from the drawer and put it ...

## Abstract Cue
- : We introduce BridgeData V2, a large and diverse dataset of robotic manipulation behaviors designed to facilitate research on scalable robot learning.
