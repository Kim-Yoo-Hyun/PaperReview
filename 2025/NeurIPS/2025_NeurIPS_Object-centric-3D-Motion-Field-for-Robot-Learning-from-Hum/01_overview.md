# Object-centric 3D Motion Field for Robot Learning from Human Videos

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Robot Learning and Data
- Tags: Robotics, learning from human videos, 3D motion field, cross-embodiment
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Recently, human-object interaction videos stand out as a particularly promising avenue to overcome this challenge.
- Unlike existing 3D tracking works that assume depth as a groundtruth reference, we recover accurate 3D object motion from noisy depth. amount of footage available from internet or ...
- Due to this data collection challenge, many works look into the feasibility of using real-world actionfree videos for robot learning.

## Core Idea
- Ablation Studies We also study the design choices of our Table 1: Policy Learning Ablation policy architecture and training.
- In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse tasks where prior ...
- In this section, we demonstrate the effectiveness of our 3D motion field estimator and our control policy through real world experiments.
- We evaluate the system in real world setups.

## Limitation
- Our approach overcomes key limitations of existing representations by introducing a robust 3D motion estimator and a dense flow prediction architecture, enabling better cross-embodiment transfer and background generalization.
- Limitations We identify the following limitations in this work as directions for future research.
- Broader Impact Our method targets one of the most significant challenges in robot learning: data.

## Contribution
- Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse tasks where prior ...
- In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this ...
- We introduce two novel components in its implementation.

## Abstract Cue
- Learning robot control policies from human videos is a promising direction for scaling up robot learning.
