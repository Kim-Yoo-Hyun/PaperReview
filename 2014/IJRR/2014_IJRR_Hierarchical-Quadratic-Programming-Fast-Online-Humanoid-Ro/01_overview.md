# Hierarchical Quadratic Programming: Fast Online Humanoid-Robot Motion Generation

> Evidence maturity: `UNREAD`. 아래 내용은 source cue와 사전 구조화이며, 정독 전에는 paper-supported conclusion으로 인용하지 않는다.

- Year/Venue: 2014 / IJRR
- Category: Robotics Foundations: Contact and Whole-Body Control
- Tags: Robotics, whole-body control, hierarchical QP, task hierarchy
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Our method is able to solve a hierarchy of only equalities ten times faster than the iterativeprojection hierarchical solvers and can consider inequalities at any level while running ...
- This paper proposes a complete solution to solve multiple least-square quadratic problems of both equality and inequality constraints ordered into a strict hierarchy.

## Core Idea
- Our method is able to solve a hierarchy of only equalities ten times faster than the iterativeprojection hierarchical solvers and can consider inequalities at any level while running ...
- 21: Simulation B: Number of algorithm iterations and computation time with the method proposed in [De Lasa et al., 2010], using our approach using a warm start and ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Some typical trajectories of the joints are shown in Fig.

## Limitation
- The inner loop itself is composed of two sets of instructions: the first one (lines #7 to #16) concerns the activation of needed constraints, while the second one ...
- As observed in [Kanoun et al., 2011], strongly active constraints cannot be deactivated at a next level.
- It does not need an initial parameter x(0) since none of the levels (even the first one) is guaranteed to be feasible.

## Contribution
- Our method is able to solve a hierarchy of only equalities ten times faster than the iterativeprojection hierarchical solvers and can consider inequalities at any level while running ...
- This paper proposes a complete solution to solve multiple least-square quadratic problems of both equality and inequality constraints ordered into a strict hierarchy.

## Abstract Cue
- Hierarchical least-square optimization is often used in robotics to inverse a direct function when multiple incompatible objectives are involved.
