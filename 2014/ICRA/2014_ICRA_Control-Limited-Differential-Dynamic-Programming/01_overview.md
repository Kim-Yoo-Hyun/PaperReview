# Control-Limited Differential Dynamic Programming

- Year/Venue: 2014 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, optimal control, trajectory optimization, control limits
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- This is particularly problematic when an expensive robot is strong enough to break itself.
- We apply our algorithm to three simulated problems, including the 36-DoF HRP-2 robot.
- Shooting methods – which trace their ancestry to the two-point boundary-value problem of the venerable Maximum Principle – are an important sub-class of trajectory optimization methods.

## Core Idea
- — Trajectory optimizers are a powerful class of methods for generating goal-directed robot motion.
- Differential Dynamic Programming (DDP) is an indirect method which optimizes only over the unconstrained control-space and is therefore fast enough to allow real-time control of a full humanoid ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- A movie of our results can be found here goo.gl/eeiMnn I.
- In this paper, we demonstrate that simple heuristics used to enforce limits (clamping and penalizing) are not efficient in general.
- Classically, a simple proportional or proportional-derivative controller in the task space is used , but it results in simple trajectories that behave badly when coming close to obstacles ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- A movie of our results can be found here goo.gl/eeiMnn I.
- In this paper, we demonstrate that simple heuristics used to enforce limits (clamping and penalizing) are not efficient in general.
- Classically, a simple proportional or proportional-derivative controller in the task space is used , but it results in simple trajectories that behave badly when coming close to obstacles ...

## Abstract Cue
- — Trajectory optimizers are a powerful class of methods for generating goal-directed robot motion.
