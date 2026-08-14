# Towards Tight Convex Relaxations for Contact-Rich Manipulation

- Year/Venue: 2024 / RSS
- Category: Manipulation, Contact, and Dexterity
- Tags: Robotics, contact-rich manipulation, convex relaxation, trajectory optimization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.roboticsproceedings.org/rss20/p132.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Approaches that blend the discrete and continuous components often do so locally (around a given trajectory) and are unable to reason about the global problem; or rely on ...
- We formulate the motion-planning problem as a shortest-path problem in a graph of convex sets, where a path in the graph corresponds to a contact sequence and a ...
- In this work, we introduce a method that naturally blends the discrete logic and the continuous dynamics of planning through contact into a convex optimization problem.

## Core Idea
- This highlights a key advantage of our approach: by reasoning on a global level, our method (empirically) always finds a solution, without relying on an initial guess.
- — We present a novel method for global motion planning of robotic systems that interact with the environment through contacts.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Exhaustive experiments show that our convexoptimization method generates plans that are consistently within a small percentage of the global optimum, without relying on an initial guess, and that ...
- For each contact mode, we use semidefinite programming to relax the nonconvex dynamics that results from the simultaneous optimization of the object’s pose, contact locations, and contact forces.
- We demonstrate the quality of these plans on a real robotic system.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Exhaustive experiments show that our convexoptimization method generates plans that are consistently within a small percentage of the global optimum, without relying on an initial guess, and that ...
- For each contact mode, we use semidefinite programming to relax the nonconvex dynamics that results from the simultaneous optimization of the object’s pose, contact locations, and contact forces.
- In this work, we introduce a method that naturally blends the discrete logic and the continuous dynamics of planning through contact into a convex optimization problem.

## Abstract Cue
- — We present a novel method for global motion planning of robotic systems that interact with the environment through contacts.
