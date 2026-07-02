# GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Gaussian Splatting, world model, Robotics
- Paper link: ./2025/ICCV/2025_ICCV_GWM-Towards-Scalable-Gaussian-World-Models-for-Robotic-Man/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- The established image-based world models and policies have shown prior success, but lack robust geometric information that requires consistent spatial and physical understanding of the three-dimensional world, even ...

## Core Idea
- To this end, we propose a novel branch of world model named Gaussian World Model (GWM) for robotic manipulation, which reconstructs the future state by inferring the propagation ...
- To achieve real-time training and inference, we design a 3D Gaussian Variational Autoencoder (VAE) to extract latent representations from 3D Gaussians, allowing the diffusion-based world model to operate ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Both simulated and real-world experiments depict that GWM can precisely predict future scenes conditioned on diverse robot actions, and can be further utilized to train policies that outperform ...
- To achieve real-time training and inference, we design a 3D Gaussian Variational Autoencoder (VAE) to extract latent representations from 3D Gaussians, allowing the diffusion-based world model to operate ...
- To comprehensively evaluate GWM, we conduct extensive experiments in action-conditioned video prediction, imitation learning, and model-based RL settings, covering 31 diverse robotic tasks across 3 domains.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To achieve real-time training and inference, we design a 3D Gaussian Variational Autoencoder (VAE) to extract latent representations from 3D Gaussians, allowing the diffusion-based world model to operate ...
- To this end, we propose a novel branch of world model named Gaussian World Model (GWM) for robotic manipulation, which reconstructs the future state by inferring the propagation ...
- Both simulated and real-world experiments depict that GWM can precisely predict future scenes conditioned on diverse robot actions, and can be further utilized to train policies that outperform ...

## Abstract Cue
- Gaussian primitives under the effect of robot actions.
