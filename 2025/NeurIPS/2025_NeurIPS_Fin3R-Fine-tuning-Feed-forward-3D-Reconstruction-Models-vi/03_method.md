# Method

- Year/Venue: 2025 / NeurIPS poster
- Category: 3D Reconstruction, Geometry, and SLAM
- Tags: 3D reconstruction, depth, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Fin3R-Fine-tuning-Feed-forward-3D-Reconstruction-Models-vi/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.
- We present Fin3R, a simple, effective, and general fine-tuning method for feedforward 3D reconstruction models.
- 3.3 Training We optimize two loss functions computed over images indexed by i in the training set.

## 원리적 동기
- Existing non-synthetic depth labels are noisy and predominantly biased toward indoor environments. (2) Long-sequence pointmap degradation: Inherent ambiguities in multi-view pointmap regression impede the network’s ability to capture ...
- Fine structures are frequently over-smoothed, object boundaries become blurred, and transparent or glossy surfaces are reconstructed with significant inaccuracies, yielding point clouds that lack crisp geometry.
- To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.

## 핵심 방법론
- To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift.
- 3.3 Training We optimize two loss functions computed over images indexed by i in the training set.
- Based on these observations, we introduce Fin3R—our solution that integrates a lightweight fine-tuning stage to simultaneously address both challenges by monocular knowledge distillation.
- Teacher Pointmap Head Self-View Head 𝐿!"#$"%% We aim to enhance our model’s capability to capture fine details and complex surface geometries Figure 4: Pipeline of our method.
- 3.1 Observations and Challenges Our analysis reveals two main challenges in existing datasets and long sequence scenarios that critically affect training of geometry regression heads: Data Scarcity.
