# Temporal Difference Learning for Model Predictive Control

- Year/Venue: 2022 / ICLR
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, model predictive control, Reinforcement Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.nicklashansen.com/td-mpc/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- To overcome these challenges, we make three key changes to model learning.
- While prior work learns a model through state or video prediction, we argue that it is remarkably inefficient to model everything in the environment, including irrelevant quantities and ...
- However, it is both costly to plan over long horizons and challenging to obtain an accurate model of the environment.

## Core Idea
- In this work, we propose Temporal Difference Learning for Model Predictive Control (TD-MPC), a framework for data-driven MPC using a task-oriented latent dynamics model and terminal value function ...
- We use a learned task-oriented latent dynamics model for local trajectory optimization over a short horizon, and use a learned terminal value function to estimate long-term return, both ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our method, TD-MPC, achieves superior sample efficiency and asymptotic performance over prior work on both state and image-based continuous control tasks from DMControl and MetaWorld.
- Data-driven model predictive control has two key advantages over model-free methods: a potential for improved sample efficiency through model learning, and better performance as computational budget for planning ...
- For example, in the Humanoid locomotion task shown in Figure 1, planning with a model may be beneficial for accurate joint movement, whereas the higher-level objective, e.g. direction ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method, TD-MPC, achieves superior sample efficiency and asymptotic performance over prior work on both state and image-based continuous control tasks from DMControl and MetaWorld.
- In this work, we propose Temporal Difference Learning for Model Predictive Control (TD-MPC), a framework for data-driven MPC using a task-oriented latent dynamics model and terminal value function ...
- We use a learned task-oriented latent dynamics model for local trajectory optimization over a short horizon, and use a learned terminal value function to estimate long-term return, both ...

## Abstract Cue
- Data-driven model predictive control has two key advantages over model-free methods: a potential for improved sample efficiency through model learning, and better performance as computational budget for planning increases.
