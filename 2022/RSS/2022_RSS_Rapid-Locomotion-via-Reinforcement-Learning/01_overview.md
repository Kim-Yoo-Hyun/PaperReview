# Rapid Locomotion via Reinforcement Learning

- Year/Venue: 2022 / RSS
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, Reinforcement Learning, high-speed locomotion
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://agility.csail.mit.edu/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- The problem is that trajectory optimization with a full model is not possible in real-time for a complex task such as fast running on natural terrains.
- The two key components are (i) an adaptive curriculum on velocity commands and (ii) an online system identification strategy for sim-to-real transfer leveraged from prior work.
- An alternative is to amortize the cost of trajectory optimization by learning a direct mapping from sensory observations to actions (a policy) using high-reward trajectories sampled from the ...

## Core Idea
- We present an end-to-end learned controller that achieves record agility for the MIT Mini Cheetah, sustaining speeds up to 3.9 m/s.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We present an end-to-end learned controller that achieves record agility for the MIT Mini Cheetah, sustaining speeds up to 3.9 m/s.
- One possibility is to resolve these issues by making targeted improvements to the hand-designed models used in modelbased control.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present an end-to-end learned controller that achieves record agility for the MIT Mini Cheetah, sustaining speeds up to 3.9 m/s.
- One possibility is to resolve these issues by making targeted improvements to the hand-designed models used in modelbased control.
- The problem is that trajectory optimization with a full model is not possible in real-time for a complex task such as fast running on natural terrains.

## Abstract Cue
- —Agile maneuvers such as sprinting and high-speed turning in the wild are challenging for legged robots.
