# Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control

- Year/Venue: 2025 / CoRL Poster
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, locomotion, end-effector stabilization, multi-rate control
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://lecar-lab.github.io/SoFTA/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- While humanoids are increasingly featured in flashy demos—dancing, delivering packages, traversing rough terrain—fine-grained control during locomotion remains a significant challenge.

## Core Idea
- To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards.
- During training, reward functions, termination conditions, and curriculum design are consistent and frequency-agnostic across all comparisons.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments aim to answer the following key questions: • Q1 (Section 4.1): Can the Two-Agent design of SoFTA perform better in simulation? • Q2 (Section 4.2): What ...
- In this section, we evaluate the performance of SoFTA in both simulation and real-world environments.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards.
- While humanoids are increasingly featured in flashy demos—dancing, delivering packages, traversing rough terrain—fine-grained control during locomotion remains a significant challenge.

## Abstract Cue
- : Can your humanoid walk up and hand you a full cup of beer—without spilling a drop?
