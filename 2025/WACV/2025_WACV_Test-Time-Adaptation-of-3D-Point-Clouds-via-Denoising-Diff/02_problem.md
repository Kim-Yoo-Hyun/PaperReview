# Problem

- Year/Venue: 2025 / WACV
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2025/WACV/2025_WACV_Test-Time-Adaptation-of-3D-Point-Clouds-via-Denoising-Diff/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Existing methods often focus on fine-tuning pre-trained models based on self-supervised learning or pseudo-labeling, which can lead to forgetting valuable source domain knowledge over time and reduce generalization ...
- LiDAR data, for instance, can be affected by sensor failures or environmental factors, causing domain gaps.
- For example, LiDAR point cloud data may be compromised by sensor failures or environmental factors, creating a domain gap that could lead to decreased performance.

## 해결하려는 문제
- In this paper, we introduce a novel 3D test-time adaptation method, termed 3DD-TTA, which stands for 3D Denoising Diffusion Test-Time Adaptation.
- We conduct extensive experiments on the ShapeNet dataset and investigate its generalizability on ModelNet40 and ScanObjectNN, achieving state-of-the-art results.
- These latent points are corrupted with Gaussian noise and subjected to a denoising diffusion process.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
