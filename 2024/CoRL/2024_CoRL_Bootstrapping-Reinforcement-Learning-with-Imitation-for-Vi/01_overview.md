# Bootstrapping Reinforcement Learning with Imitation for Vision-Based Agile Flight

- Year/Venue: 2024 / CoRL
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, aerial robotics, Reinforcement Learning, Imitation Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://bootstrap-rl-with-il.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Thus, the ability to explore and learn efficiently in vision-based RL environments from scratch is essential, presenting a key challenge that our research seeks to overcome.
- Due to this simplification, IL typically requires fewer samples and, consequently, has been validated for real-world robot learning problems .
- However, learning from only visual inputs introduces a range of distinct challenges.

## Core Idea
- To address these challenges, we propose a novel approach that combines the performance of Reinforcement Learning (RL) and the sample efficiency of Imitation Learning (IL) in the task ...
- Our framework contains three phases: training a teacher policy using RL with privileged state information, distilling it into a student policy via IL, and adaptive fine-tuning via RL.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Testing in both simulated and real-world scenarios shows our approach can not only learn in scenarios where RL from scratch fails but also outperforms existing IL methods in ...
- Videos of the experiments are available at https://rpg.ifi.uzh.ch/bootstrap-rl-with-il/index.html.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Testing in both simulated and real-world scenarios shows our approach can not only learn in scenarios where RL from scratch fails but also outperforms existing IL methods in ...
- To address these challenges, we propose a novel approach that combines the performance of Reinforcement Learning (RL) and the sample efficiency of Imitation Learning (IL) in the task ...
- Our framework contains three phases: training a teacher policy using RL with privileged state information, distilling it into a student policy via IL, and adaptive fine-tuning via RL.

## Abstract Cue
- : Learning visuomotor policies for agile quadrotor flight presents significant difficulties, primarily from inefficient policy exploration caused by highdimensional visual inputs and the need for precise and low-latency control.
