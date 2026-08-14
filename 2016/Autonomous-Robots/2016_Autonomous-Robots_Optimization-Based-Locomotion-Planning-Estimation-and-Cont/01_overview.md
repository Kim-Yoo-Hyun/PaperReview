# Optimization-Based Locomotion Planning, Estimation, and Control Design for the Atlas Humanoid Robot

- Year/Venue: 2016 / Autonomous Robots
- Category: Robotics Foundations: Planning and Control
- Tags: Robotics, humanoid, locomotion planning, optimization, state estimation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not released
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- In this paper we describe our approach to addressing these problems with Atlas.
- To plan a sequence of safe footsteps, we decompose the problem into three steps.
- Given this obstacle map, we solve a sequence of optimization problems to compute a set of convex safe footstep regions in the configuration space of the foot.

## Core Idea
- Our approach to walking combines an efficient footstep planner with a simple dynamic model of the robot to efficiently compute desired walking trajectories.
- In this paper we describe our approach to addressing these problems with Atlas.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- 6.1 State estimation evaluation To characterize the state estimator we evaluate its performance in a variety of experiments.
- We describe our complete system integration and experiments carried out on Atlas, a full-size hydraulic humanoid robot built by Boston Dynamics, Inc.
- B Scott Kuindersma scottk@csail.mit.edu Robin Deits rdeits@csail.mit.edu Maurice Fallon mfallon@csail.mit.edu Andrés Valenzuela avalenzu@csail.mit.edu Hongkai Dai daih@csail.mit.edu Frank Permenter fpermenter@csail.mit.edu Twan Koolen tkoolen@csail.mit.edu Pat Marion patmarion@csail.mit.edu Russ Tedrake russt@csail.mit.edu ...

## Limitation
- Despite significant sensor limitations and inevitable model inaccuracies, we have been able to achieve reliable balancing and walking with Atlas.
- 15 Snapshots from a motion plan for jumping off a cinder block. a Starting posture, b toe-off, c apex, d avoiding collision, e touch-down, f final posture 7 ...
- However, recovering safely in cluttered environments and on irregular terrain remains an exciting open question.

## Contribution
- We describe our complete system integration and experiments carried out on Atlas, a full-size hydraulic humanoid robot built by Boston Dynamics, Inc.
- To make challenging locomotion tasks tractable, we describe several novel applications of convex, mixed-integer, and sparse nonlinear optimization to problems ranging from footstep placement to whole-body planning and ...

## Abstract Cue
- This paper describes a collection of optimization algorithms for achieving dynamic planning, control, and state estimation for a bipedal robot designed to operate reliably in complex environments.
