# Test-Time Adaptation of 3D Point Clouds via Denoising Diffusion Models

- Year/Venue: 2025 / WACV
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Paper link: ./2025/WACV/2025_WACV_Test-Time-Adaptation-of-3D-Point-Clouds-via-Denoising-Diff/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Existing methods often focus on fine-tuning pre-trained models based on self-supervised learning or pseudo-labeling, which can lead to forgetting valuable source domain knowledge over time and reduce generalization ...
- LiDAR data, for instance, can be affected by sensor failures or environmental factors, causing domain gaps.
- For example, LiDAR point cloud data may be compromised by sensor failures or environmental factors, creating a domain gap that could lead to decreased performance.

## Core Idea
- In this paper, we introduce a novel 3D test-time adaptation method, termed 3DD-TTA, which stands for 3D Denoising Diffusion Test-Time Adaptation.
- Test-time adaptation (TTA) of 3D point clouds is crucial for mitigating discrepancies between training and testing samples in real-world scenarios, particularly when handling corrupted point clouds.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We conduct extensive experiments on the ShapeNet dataset and investigate its generalizability on ModelNet40 and ScanObjectNN, achieving state-of-the-art results.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper, we introduce a novel 3D test-time adaptation method, termed 3DD-TTA, which stands for 3D Denoising Diffusion Test-Time Adaptation.
- We conduct extensive experiments on the ShapeNet dataset and investigate its generalizability on ModelNet40 and ScanObjectNN, achieving state-of-the-art results.
- These latent points are corrupted with Gaussian noise and subjected to a denoising diffusion process.

## Abstract Cue
- Test-time adaptation (TTA) of 3D point clouds is crucial for mitigating discrepancies between training and testing samples in real-world scenarios, particularly when handling corrupted point clouds.
