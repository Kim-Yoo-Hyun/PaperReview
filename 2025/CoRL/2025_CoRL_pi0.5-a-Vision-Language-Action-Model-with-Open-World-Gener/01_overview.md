# π0.5: a Vision-Language-Action Model with Open-World Generalization

- Year/Venue: 2025 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, open-world, Robotics
- Paper link: ./2025/CoRL/2025_CoRL_pi0.5-a-Vision-Language-Action-Model-with-Open-World-Gener/paper.pdf
- Code/Project: https://www.physicalintelligence.company/blog/pi05
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Open-world generalization represents one of the biggest open problems in physical intelligence, and scalable learning systems offer a path to enable such generalization, as they have in domains ...
- A person can draw on a lifetime of experience to synthesize appropriate solutions to each of these challenges.

## Core Idea
- Our central contribution is a system for training a highly generalizable VLA, π0.5 , together with a proof of concept that generalization can emerge from this model when ...
- We provide a detailed empirical evaluation of both π0.5 ’s generalization capabilities and the relevance of different co-training ingredients.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can ...
- While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our experiments show that this kind of knowledge transfer is essential for effective generalization, and we demonstrate for the first time that an end-to-end learning-enabled robotic system can ...
- While vision-language-action (VLA) models have demonstrated impressive results for end-to-end robot control, it remains an open question how far such models can generalize in the wild.
- We describe π0.5 , a new model based on π0 that uses co-training on heterogeneous tasks to enable broad generalization. π0.5 uses data from multiple robots, highlevel semantic ...

## Abstract Cue
- : In order for robots to be useful, they must perform practically relevant tasks in the real world, outside of the lab.
