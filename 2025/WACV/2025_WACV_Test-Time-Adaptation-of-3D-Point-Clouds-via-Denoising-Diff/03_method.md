# Method

- Year/Venue: 2025 / WACV
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2025/WACV/2025_WACV_Test-Time-Adaptation-of-3D-Point-Clouds-via-Denoising-Diff/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this paper, we introduce a novel 3D test-time adaptation method, termed 3DD-TTA, which stands for 3D Denoising Diffusion Test-Time Adaptation.
- Test-time adaptation (TTA) of 3D point clouds is crucial for mitigating discrepancies between training and testing samples in real-world scenarios, particularly when handling corrupted point clouds.
- Reconstruction of corrupted point clouds using the proposed 3DD-TTA method. between training and testing samples is minimal.

## 원리적 동기
- Existing methods often focus on fine-tuning pre-trained models based on self-supervised learning or pseudo-labeling, which can lead to forgetting valuable source domain knowledge over time and reduce generalization ...
- LiDAR data, for instance, can be affected by sensor failures or environmental factors, causing domain gaps.
- In this paper, we introduce a novel 3D test-time adaptation method, termed 3DD-TTA, which stands for 3D Denoising Diffusion Test-Time Adaptation.

## 핵심 방법론
- Baselines Setup: We adopted the hierarchical latent diffusion model proposed in , pre-trained on the ShapeNet dataset for our 3DD-TTA model.
