# Problem

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Representation Learning and Foundation Models
- Tags: point cloud, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_U-CAN-Unsupervised-Point-Cloud-Denoising-with-Consistency/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- In response to this challenge, we introduce a novel consistency-aware constraint that specifically targets the denoising geometric consistency.
- Another challenge in predicting robust denoising arises from the unknown location of true surfaces when only noisy observations are available.
- However, the current unsupervised approaches still struggle to predict precise clean point cloud while keeping high-fidelity local geometries due to the lack of sufficient constraints at local-level.

## 해결하려는 문제
- Our evaluations denoising show significant improvement over the state-of-the-art unsupervised methods, where U-CAN also produces comparable results with the supervised methods.
- Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.
- In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.

## 선행 연구 / 배경 단서
- In response to this challenge, we introduce a novel consistency-aware constraint that specifically targets the denoising geometric consistency.
- Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by designing a neural network to infer a ...
- Another challenge in predicting robust denoising arises from the unknown location of true surfaces when only noisy observations are available.
