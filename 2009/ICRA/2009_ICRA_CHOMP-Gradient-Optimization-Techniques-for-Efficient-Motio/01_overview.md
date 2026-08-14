# CHOMP: Gradient Optimization Techniques for Efficient Motion Planning

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2009 / ICRA
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, motion planning, trajectory optimization, manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://moveit.github.io/moveit_tutorials/doc/chomp_planner/chomp_planner_tutorial.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- — Existing high-dimensional motion planning algorithms are simultaneously overpowered and underpowered.
- In domains sparsely populated by obstacles, the heuristics used by sampling-based planners to navigate “narrow passages” can be needlessly complex; furthermore, additional post-processing is required to remove the ...

## Core Idea
- In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems.
- In this paper, we present CHOMP, a novel method for continuous path refinement that uses covariant gradient techniques to improve the quality of sampled trajectories.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In this paper, we present CHOMP, a novel method for continuous path refinement that uses covariant gradient techniques to improve the quality of sampled trajectories.
- The effectiveness of our proposed method is demonstrated in manipulation planning for a 6-DOF robotic arm as well as in trajectory generation for a walking quadruped robot.

## Limitation
- UNVERIFIED — full text의 해당 section을 정독한 뒤 근거와 위치를 기록한다.

## Contribution
- In this paper, we present CHOMP, a novel method for continuous path refinement that uses covariant gradient techniques to improve the quality of sampled trajectories.
- In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems.
- The effectiveness of our proposed method is demonstrated in manipulation planning for a 6-DOF robotic arm as well as in trajectory generation for a walking quadruped robot.

## Abstract Cue
- — Existing high-dimensional motion planning algorithms are simultaneously overpowered and underpowered.
