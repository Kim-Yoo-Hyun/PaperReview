# Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining

- Year/Venue: 2025 / RSS
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, quadruped locomotion, loco-manipulation, human demonstrations
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://www.roboticsproceedings.org/rss21/p122.html
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Prior works have explored various strategies for collecting in-domain robot data, primarily focusing on robot arms , humanoid robots , and quadrupeds equipped with top-mounted arms .
- —Quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments, but equipping them with autonomous versatile manipulation skills in a scalable way remains a significant challenge.
- I NTRODUCTION While quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments , and recent advances have extended their abilities to manipulation tasks , enabling autonomous and ...

## Core Idea
- To effectively leverage the collected data, we propose an efficient modularized architecture that supports co-training and pretraining on structured modalityaligned data across different embodiments.
- In this work, we introduce a cross-embodiment imitation learning system for quadrupedal manipulation, leveraging data collected from both humans and LocoMan, a quadruped equipped with multiple manipulation modes.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We validate our system on six real-world manipulation tasks, where it *Authors contributed equally to this work. achieves an average success rate improvement of 41.9% overall and 79.7% ...
- Pretraining with human data contributes a 38.6% success rate improvement overall and 82.7% under OOD settings, enabling consistently better performance with only half the amount of robot data.
- —Quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments, but equipping them with autonomous versatile manipulation skills in a scalable way remains a significant challenge.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To effectively leverage the collected data, we propose an efficient modularized architecture that supports co-training and pretraining on structured modalityaligned data across different embodiments.
- Pretraining with human data contributes a 38.6% success rate improvement overall and 82.7% under OOD settings, enabling consistently better performance with only half the amount of robot data.
- We validate our system on six real-world manipulation tasks, where it *Authors contributed equally to this work. achieves an average success rate improvement of 41.9% overall and 79.7% ...

## Abstract Cue
- —Quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments, but equipping them with autonomous versatile manipulation skills in a scalable way remains a significant challenge.
