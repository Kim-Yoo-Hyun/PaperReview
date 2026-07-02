# Method

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Representation Learning and Foundation Models
- Tags: point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_U-CAN-Unsupervised-Point-Cloud-Denoising-with-Consistency/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.
- This is particularly clear in areas of high-frequency information, such as edges, textures, and intricate patterns, where our method maintains the integrity of these details while effectively reducing ...
- Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.

## 원리적 동기
- In response to this challenge, we introduce a novel consistency-aware constraint that specifically targets the denoising geometric consistency.
- Another challenge in predicting robust denoising arises from the unknown location of true surfaces when only noisy observations are available.
- In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.

## 핵심 방법론
- This is particularly clear in areas of high-frequency information, such as edges, textures, and intricate patterns, where our method maintains the integrity of these details while effectively reducing ...
- Specifically, given a sparse point cloud with M points as the input, we add Gaussian noise to it for r times independently, resulting in a noisy dense point ...
