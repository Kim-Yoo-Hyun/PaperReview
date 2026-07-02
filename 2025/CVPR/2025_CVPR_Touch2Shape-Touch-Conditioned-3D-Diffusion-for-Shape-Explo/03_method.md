# Method

- Year/Venue: 2025 / CVPR
- Category: 3D Generative Modeling and Diffusion
- Tags: 3D reconstruction, Diffusion, Generation, 3D Vision
- Paper link: ./2025/CVPR/2025_CVPR_Touch2Shape-Touch-Conditioned-3D-Diffusion-for-Shape-Explo/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the latent vector to ...
- In this paper, we combine the diffusion model with policy training.
- This involves using the generated latent vector from the diffusion model to guide the touch exploration policy training through a novel reward design.

## 원리적 동기
- To overcome these limitations, we utilize tactile images to capture the local 3D information and propose a Touch2Shape model, which leverages a touch-conditioned diffusion model to explore and ...
- The main contributions of this article are as follows: • We propose Touch2Shape, a touch-conditioned 3D diffusion model for shape exploration and reconstruction, utilizing the latent vector to ...

## 핵심 방법론
- In this paper, we combine the diffusion model with policy training.
- The training process is segmented into three parts: diffusion model training, touch shape fusion module training, and policy training.
- Policy Training This module aims to create potential 3D shapes utilizing the diffusion model based on the acquired tactile (and optional visual) data, which are then employed to ...
- Experiment In this section, we describe the experiment settings and then compare our model with the state-of-art touch-based 3D reconstruction methods and validate our policy training strategy.
- We first employ the pre-trained latent encoder in Figure 2 (c) to encode both the initial and current latent vectors of the touch-conditioned diffusion model.
