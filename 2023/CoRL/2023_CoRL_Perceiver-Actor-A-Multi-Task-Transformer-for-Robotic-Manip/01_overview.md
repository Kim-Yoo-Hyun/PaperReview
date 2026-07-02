# Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation

- Year/Venue: 2023 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Imitation Learning, 3D manipulation
- Paper link: ./2023/CoRL/2023_CoRL_Perceiver-Actor-A-Multi-Task-Transformer-for-Robotic-Manip/paper.pdf
- Code/Project: https://peract.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Can we still bring the power of Transformers to 6-DoF manipulation with the right problem formulation?
- Thus, while Transformers may be domain agnostic, they still require the right problem formulation to be data efficient.
- P ER ACT is essentially a classifier trained with supervised learning to detect actions akin to prior work like CLIPort , except our observations and actions are represented ...

## Core Idea
- 5 Limitations and Conclusion We presented P ER ACT, a Transformer-based multi-task agent for 6-DoF manipulation.
- With- Press Handsan 5 10 90 out any sim-to-real transfer or pre-training, we trained a multi-task Put Marker 8 10 70 8 10 60 P ER ACT agent ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- C2FARM-BC is a 3D fully-convolutional network by James et al. that has achieved state-of-the-art results on RLBench tasks.
- Our results show that P ER ACT significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.
- In contrast, P ER ACT’s voxel-based formulation naturally allows for integrating multi-view observations, learning 6-DoF action representations, and data-augmentation in 3D, all of which are non-trivial to achieve ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our results show that P ER ACT significantly outperforms unstructured image-to-action agents and 3D ConvNet baselines for a wide range of tabletop tasks.
- Can manipulation still benefit from Transformers with the right problem formulation?
- With this formulation, we train a single multi-task Transformer for 18 RLBench tasks (with 249 variations) and 7 real-world tasks (with 18 variations) from just a few demonstrations ...

## Abstract Cue
- : Transformers have revolutionized vision and natural language processing with their ability to scale with large datasets.
