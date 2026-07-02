# PDFactor: Learning Tri-Perspective View Policy Diffusion Field for Multi-Task Robotic Manipulation

- Year/Venue: 2025 / CVPR
- Category: Equivariance, Diffusion, and 3D Action
- Tags: Diffusion, Robotics, 3D action
- Paper link: ./2025/CVPR/2025_CVPR_PDFactor-Learning-Tri-Perspective-View-Policy-Diffusion-Fi/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- High Value Low Value Parameterization  Robotic manipulation based on visual observations and natural language instructions is a long-standing challenge in robotics.

## Core Idea
- In response, we propose PDFactor, a novel framework that models action distribution with a hybrid triplane representation.
- We employ a small denoising network conceptually as both a parameterized loss function measuring the quality of the learned latent features and an action gradient decoder to sample ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments demonstrate that PDFactor outperforms state-of-theart approaches across a diverse range of manipulation tasks in RLBench simulation.
- Yet prevailing approaches model action distribution by adopting explicit or implicit representations, which often struggle to achieve a trade-off between accuracy and efficiency.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We employ a small denoising network conceptually as both a parameterized loss function measuring the quality of the learned latent features and an action gradient decoder to sample ...
- Experiments demonstrate that PDFactor outperforms state-of-theart approaches across a diverse range of manipulation tasks in RLBench simulation.
- In particular, PDFactor decomposes 3D point cloud into three orthogonal feature planes and leverages a tri-perspective view transformer to produce dense cubic features as a latent diffusion field ...

## Abstract Cue
- High Value Low Value Parameterization  Robotic manipulation based on visual observations and natural language instructions is a long-standing challenge in robotics.
