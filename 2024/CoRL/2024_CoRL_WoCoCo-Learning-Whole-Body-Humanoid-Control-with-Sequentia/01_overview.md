# WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts

- Year/Venue: 2024 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, sequential contacts, Reinforcement Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://wococo-humanoid.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- In WoCoCo, we reformulate the problem as the sequential fulfillment of multiple contact stages (detailed in Section 2), which also breaks down the exploration burden into separate stages.
- This then transforms each challenge to a question: Q1: How to reach desired contact states within each stage?
- This drives the robot to explore further stages to maximize cumulative rewards, thus mitigating the shortsightedness caused by the RL policy strategically staying in the current stage to ...

## Core Idea
- To better facilitate exploration, we propose a task-agnostic curiosity reward term.
- In this work, we propose WoCoCo (Whole-Body Control with Sequential Contacts), a unified framework to learn whole-body humanoid control with sequential contacts by naturally decomposing the tasks into ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrated that endto-end RL-based controllers trained with WoCoCo enable four challenging wholebody humanoid tasks involving diverse contact sequences in the real world without any motion priors: 1) ...
- We further show that WoCoCo is a general framework beyond humanoid by applying it in 22-DoF dinosaur robot loco-manipulation tasks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this work, we propose WoCoCo (Whole-Body Control with Sequential Contacts), a unified framework to learn whole-body humanoid control with sequential contacts by naturally decomposing the tasks into ...
- We demonstrated that endto-end RL-based controllers trained with WoCoCo enable four challenging wholebody humanoid tasks involving diverse contact sequences in the real world without any motion priors: 1) ...
- We further show that WoCoCo is a general framework beyond humanoid by applying it in 22-DoF dinosaur robot loco-manipulation tasks.

## Abstract Cue
- : Humanoid activities involving sequential contacts are crucial for complex robotic interactions and operations in the real world and are traditionally solved by model-based motion planning, which is time-consuming and often relies on simplified dynamics models.
