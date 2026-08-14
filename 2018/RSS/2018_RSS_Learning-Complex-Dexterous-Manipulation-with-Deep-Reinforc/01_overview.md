# Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations

- Year/Venue: 2018 / RSS
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, Reinforcement Learning, dexterous manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sites.google.com/view/deeprl-dexterous-manipulation
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- This makes dexterous manipulation with multi-fingered hands a challenging problem.
- However, these methods typically rely on accurate dynamics models and state estimates, which are often difficult to obtain for contact rich manipulation tasks, especially in the real world.

## Core Idea
- C ONCLUSION In this work, we developed a set of manipulation tasks representative of the types of tasks we encounter in everyday life.
- For this section of the evaluation we use only sparse task completion rewards, since we are using demonstrations.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In this work, we show that model-free DRL can effectively scale up to complex manipulation tasks with a high-dimensional 24-DoF hand, and solve them from scratch in simulated ...
- We demonstrate successful policies for object relocation, in-hand manipulation, tool use, and door opening, which are shown in the supplementary video.
- Deep reinforcement learning (DRL) provides a model-agnostic approach to control complex dynamical systems, but has not been shown to scale to highdimensional dexterous manipulation.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we show that model-free DRL can effectively scale up to complex manipulation tasks with a high-dimensional 24-DoF hand, and solve them from scratch in simulated ...
- We demonstrate successful policies for object relocation, in-hand manipulation, tool use, and door opening, which are shown in the supplementary video.
- Deep reinforcement learning (DRL) provides a model-agnostic approach to control complex dynamical systems, but has not been shown to scale to highdimensional dexterous manipulation.

## Abstract Cue
- —Dexterous multi-fingered hands are extremely versatile and provide a generic way to perform a multitude of tasks in human-centric environments.
