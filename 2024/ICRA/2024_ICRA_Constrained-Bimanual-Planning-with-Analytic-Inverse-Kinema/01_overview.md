# Constrained Bimanual Planning with Analytic Inverse Kinematics

- Year/Venue: 2024 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, bimanual manipulation, motion planning, inverse kinematics
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://tommycohn.com/Bimanual-Web/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- We leverage an analytic solution to the inverse kinematics problem to parametrize the configuration space, resulting in a lower-dimensional representation where the set of valid configurations has positive ...
- In the case of certain bimanual planning problems, there is additional structure that
- In addition, the set of feasible configurations becomes a measure zero set, which presents a challenge to sampling-based motion planners.

## Core Idea
- D ISCUSSION We presented a novel parametrization of the constrained configuration space that arises in bimanual manipulation, which can be leveraged by both sampling-based planners and trajectory optimizers ...
- We use the multi-query PRM algorithm , initialized with nodes from multiple BiRRTs to ensure connectivity, as in [8, §C].

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- — In order for a bimanual robot to manipulate an object that is held by both hands, it must construct motion plans such that the transformation between its ...
- This amounts to complicated nonlinear equality constraints in the configuration space, which are difficult for trajectory optimizers.
- In addition, the set of feasible configurations becomes a measure zero set, which presents a challenge to sampling-based motion planners.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We leverage an analytic solution to the inverse kinematics problem to parametrize the configuration space, resulting in a lower-dimensional representation where the set of valid configurations has positive ...
- In the case of certain bimanual planning problems, there is additional structure that
- In addition, the set of feasible configurations becomes a measure zero set, which presents a challenge to sampling-based motion planners.

## Abstract Cue
- — In order for a bimanual robot to manipulate an object that is held by both hands, it must construct motion plans such that the transformation between its end effectors remains fixed.
