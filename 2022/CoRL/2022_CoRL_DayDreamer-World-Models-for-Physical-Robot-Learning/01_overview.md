# DayDreamer: World Models for Physical Robot Learning

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2022 / CoRL
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, real robot, model-based reinforcement learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://danijar.com/project/daydreamer/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- In this paper, we leverage recent advances of the Dreamer world model for training a variety of robots in the most straight-forward and fundamental problem setting: online reinforcement ...
- The tasks cover a range of challenges, including different action spaces, sensory modalities, and reward structures. • Walking in 1 Hour We teach a quadruped from scratch in ...
- Replay Buﬀer Real World Teaching robots to solve complex tasks in the real world is a foundational problem of robotics research.

## Core Idea
- This section summarizes the general algorithm, as well as details on the training architecture and sensor fusion needed for the robotics experiments.
- The world model is based on the Recurrent State-Space Model (RSSM; Hafner et al., 2018), which consists of four components: Encoder Network: encθ (st | st−1 , at−1 ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The Dreamer algorithm has recently shown great promise for learning from small amounts of interaction by planning within a learned world model, outperforming pure reinforcement learning in video ...
- The goal of the experiments is to evaluate whether the recent successes of learned world models enables sample-efficient robot learning directly in the real world.
- Using the same hyperparameters across all experiments, we find that Dreamer is capable of online learning in the real world, which establishes a strong baseline.

## Limitation
- Limitations While Dreamer shows promising results, learning on hardware over many hours creates wear on robots that may require human intervention or repair.

## Contribution
- The Dreamer algorithm has recently shown great promise for learning from small amounts of interaction by planning within a learned world model, outperforming pure reinforcement learning in video ...
- The tasks evaluate a diverse range of challenges, including continuous and discrete actions, dense and sparse rewards, proprioceptive and camera inputs, as well as sensor fusion of multiple ...
- Using the same hyperparameters across all experiments, we find that Dreamer is capable of online learning in the real world, which establishes a strong baseline.

## Abstract Cue
- : To solve tasks in complex environments, robots need to learn from experience.
