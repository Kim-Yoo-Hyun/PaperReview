# Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching

- Year/Venue: 2024 / CoRL
- Category: Robot Learning and Data
- Tags: Robotics, point cloud, conditional flow matching, Imitation Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Imitation learning (IL) is the widely studied problem of training policies from a given set of expert demonstrations .
- To overcome these limitations, Conditional Flow Matching (CFM) has been proposed as an efficient generalization of diffusion models .

## Core Idea
- This result demonstrates that the combination of our choices of observation type, encoder architecture, and training objective leads to a highly effective imitation learning algorithm.
- Training objective unplug charger close door open box open fridge frame hanger open oven books shelf shoes box Mean SR Delta SR Img.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, double the performance of ...
- We show that CFM gives the best performance when combined with point cloud input observations.
- Additionally, we study the feasibility of a CFM formulation on the SO(3) manifold and evaluate its suitability with a simplified example.

## Limitation
- Limitations: There are a few limitations to our proposed method.
- In addition to this, as usual in the fixed-data imitation learning setting, CFM cannot extrapolate out of distribution and thus, only learns motion correction behavior when included in ...

## Contribution
- We perform extensive experiments on RLBench which demonstrate that our proposed PointFlowMatch approach achieves a state-of-the-art average success rate of 67.8% over eight tasks, double the performance of ...
- However, imitation learning algorithms require a number of design choices ranging from the input modality, training objective, and 6-DoF end-effector pose representation.
- : Learning from expert demonstrations is a promising approach for training robotic manipulation policies from limited data.

## Abstract Cue
- : Learning from expert demonstrations is a promising approach for training robotic manipulation policies from limited data.
