# HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2025 / ICRA
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Tags: Robotics, humanoid, whole-body control, Reinforcement Learning, NVIDIA
- Official paper: https://research.nvidia.com/labs/lpr/publication/he2025hover/
- Code/Project: https://hover-versatile-humanoid.github.io/
- Source audit: official NVIDIA publication and project pages checked; full robot protocol remains UNVERIFIED.

## Why This Paper Is Here

다양한 command modality를 수용하는 neural whole-body humanoid controller로 NVIDIA의 simulation-to-real humanoid control 계보를 보강한다.

## Problem

locomotion, pose/keypoint tracking 등 여러 whole-body commands를 하나의 real humanoid controller가 안정적으로 수행한다.

## Core Idea

multi-mode command conditioning과 large-scale physics training을 결합한 unified neural controller를 학습한다.

## Interface

humanoid proprioception과 velocity/pose/keypoint commands를 whole-body joint actions로 매핑한다.

## Evaluation Scope

simulation 및 physical humanoid의 다양한 command tracking과 robustness가 보고된다.
