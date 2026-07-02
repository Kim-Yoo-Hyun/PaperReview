# U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Representation Learning and Foundation Models
- Tags: point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_U-CAN-Unsupervised-Point-Cloud-Denoising-with-Consistency/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In response to this challenge, we introduce a novel consistency-aware constraint that specifically targets the denoising geometric consistency.
- Another challenge in predicting robust denoising arises from the unknown location of true surfaces when only noisy observations are available.
- However, the current unsupervised approaches still struggle to predict precise clean point cloud while keeping high-fidelity local geometries due to the lack of sufficient constraints at local-level.

## Core Idea
- In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.
- This is particularly clear in areas of high-frequency information, such as edges, textures, and intricate patterns, where our method maintains the integrity of these details while effectively reducing ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our evaluations denoising show significant improvement over the state-of-the-art unsupervised methods, where U-CAN also produces comparable results with the supervised methods.
- We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- For the experiments on synthetic shapes, we follow ScoreDenoise to train our network on the PUNet dataset.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our evaluations denoising show significant improvement over the state-of-the-art unsupervised methods, where U-CAN also produces comparable results with the supervised methods.
- Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.
- In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.

## Abstract Cue
- Point clouds captured by scanning sensors are often perturbed by noise, which have a highly negative impact on downstream tasks (e.g. surface reconstruction and shape understanding).
