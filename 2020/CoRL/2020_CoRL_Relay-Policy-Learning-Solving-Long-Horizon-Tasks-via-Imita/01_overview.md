# Relay Policy Learning: Solving Long-Horizon Tasks via Imitation and Reinforcement Learning

- Year/Venue: 2020 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, Imitation Learning, Reinforcement Learning, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://relay-policy-learning.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- We can simplify the above-mentioned problems by utilizing extra supervision in the form of unstructured human demonstrations, in which case the question becomes: how should we best use ...
- Hierarchical reinforcement learning (HRL) has been proposed as a potential solution that should scale to challenging long-horizon problems, by explicitly introducing temporal abstraction.
- However, HRL methods have traditionally struggled due to various practical challenges such as exploration , skill segmentation and reward definition .

## Core Idea
- : We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.
- Second, our method does not require any explicit form of skill segmentation or subgoal definition, which otherwise would need to be learned or explicitly provided.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- When we analyze the proportion of compound goals that are actually fully achieved (see Table 1, bottom row), RIL shows significant improvement over other methods.
- Videos are available at https://relay-policy-learning.github.io/ Our experiments aim to answer the following questions: (1) Does RIL improve imitation learning with unstructured and unlabelled demonstrations? (2) Is RIL more ...
- We simplify the long-horizon policy learning problem by using a novel data-relabeling algorithm for learning goal-conditioned hierarchical policies, where the low-level only acts for a fixed number of ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our method, while not necessarily perfect at imitation learning, is very amenable to further improvement via environment interaction, allowing it to scale to challenging longhorizon tasks.
- We demonstrate the effectiveness of our method on a number of multi-stage, long-horizon manipulation tasks in a challenging kitchen simulation environment.
- : We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.

## Abstract Cue
- : We present relay policy learning, a method for imitation and reinforcement learning that can solve multi-stage, long-horizon robotic tasks.
