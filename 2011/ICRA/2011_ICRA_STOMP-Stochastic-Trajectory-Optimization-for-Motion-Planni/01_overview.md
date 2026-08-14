# STOMP: Stochastic Trajectory Optimization for Motion Planning

- Year/Venue: 2011 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, motion planning, trajectory optimization, stochastic optimization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://moveit.github.io/moveit_tutorials/doc/stomp_planner/stomp_planner_tutorial.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- No gradient information is required for the particular optimization algorithm that we use and so general costs for which derivatives may not be available (e.g. costs corresponding to ...
- The approach relies on generating noisy trajectories to explore the space around an initial (possibly infeasible) trajectory, which are then combined to produced an updated trajectory with lower ...
- A cost function based on a combination of obstacle and smoothness cost is optimized in each iteration.

## Core Idea
- — We present a new approach to motion planning using a stochastic trajectory optimization framework.
- In this paper, we present a new approach to motion planning that can deal with general constraints.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate our approach through both simulation and experimental results with the PR2 mobile manipulation robot.
- We demonstrate the approach both in simulation and on a mobile manipulation system for unconstrained and constrained tasks.
- We experimentally show that the stochastic nature of STOMP allows it to overcome local minima that gradient-based methods like CHOMP can get stuck in.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We demonstrate our approach through both simulation and experimental results with the PR2 mobile manipulation robot.
- No gradient information is required for the particular optimization algorithm that we use and so general costs for which derivatives may not be available (e.g. costs corresponding to ...
- — We present a new approach to motion planning using a stochastic trajectory optimization framework.

## Abstract Cue
- — We present a new approach to motion planning using a stochastic trajectory optimization framework.
