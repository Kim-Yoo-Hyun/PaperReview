# Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation

- Year/Venue: 2023 / CoRL
- Category: Language-Embedded NeRF and Gaussian Fields
- Tags: Robotics, NeRF, Vision-Language, manipulation
- Paper link: ./2023/CoRL/2023_CoRL_Distilled-Feature-Fields-Enable-Few-Shot-Language-Guided-M/paper.pdf
- Code/Project: https://f3rm.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- One challenge that makes distilled feature fields unwieldy for robotics is the long time it takes to model each scene.
- Many robotic tasks, however, require a detailed understanding of 3D geometry, which is often lacking in 2D image features.

## Core Idea
- We present few-shot learning experiments on grasping and placing tasks, where our robot is able to handle open-set generalization to objects that differ significantly in shape, appearance, materials, ...
- We present a few-shot learning method for 6-DOF grasping and placing that harnesses these strong spatial and semantic priors to achieve in-the-wild generalization to unseen objects.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We present a few-shot learning method for 6-DOF grasping and placing that harnesses these strong spatial and semantic priors to achieve in-the-wild generalization to unseen objects.
- While the baselines using density, RGB color values, or intermediate features from NeRF achieve respectable performance, they struggle to identify the semantic category of the objects we care ...
- Using features distilled from a vision-language model, CLIP, we present a way to designate novel objects for manipulation via free-text natural language, and demonstrate its ability to generalize ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present a few-shot learning method for 6-DOF grasping and placing that harnesses these strong spatial and semantic priors to achieve in-the-wild generalization to unseen objects.
- Using features distilled from a vision-language model, CLIP, we present a way to designate novel objects for manipulation via free-text natural language, and demonstrate its ability to generalize ...
- Many robotic tasks, however, require a detailed understanding of 3D geometry, which is often lacking in 2D image features.

## Abstract Cue
- : Self-supervised and language-supervised image models contain rich knowledge of the world that is important for generalization.
