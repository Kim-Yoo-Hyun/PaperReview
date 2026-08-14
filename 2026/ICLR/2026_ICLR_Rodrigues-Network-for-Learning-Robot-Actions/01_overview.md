# Rodrigues Network for Learning Robot Actions

- Year/Venue: 2026 / ICLR Oral
- Category: Robot Learning and Data
- Tags: Robotics, kinematics, action representation, Imitation Learning
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- I NTRODUCTION We study the problem of understanding and predicting the actions of articulated actors.
- However, common architectures such as MLPs and Transformers lack inductive biases that reflect the underlying kinematic structure of articulated systems.

## Core Idea
- Additionally, we introduce a cross-attention layer following the self-attention layer to enable interactions between joint and link features and the input image tokens.
- To this end, we propose the Neural Rodrigues Operator, a learnable generalization of the classical forward kinematics operation, designed to inject kinematics-aware inductive bias into neural computation.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We evaluate the expressivity of our network on two synthetic tasks on kinematic and motion prediction, showing significant improvements compared to standard backbones.
- Our results suggest that integrating structured kinematic priors into the network architecture improves action learning in various domains.
- We further demonstrate its effectiveness in two realistic applications: (i) imitation learning on robotic benchmarks with the Diffusion Policy, and (ii) single-image 3D hand reconstruction.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our results suggest that integrating structured kinematic priors into the network architecture improves action learning in various domains.
- However, common architectures such as MLPs and Transformers lack inductive biases that reflect the underlying kinematic structure of articulated systems.
- We further demonstrate its effectiveness in two realistic applications: (i) imitation learning on robotic benchmarks with the Diffusion Policy, and (ii) single-image 3D hand reconstruction.

## Abstract Cue
- Built upon this operator, the Rodrigues Network leverages the kinematic structure of articulated systems to advance a wide range of action-learning tasks.
