# Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets

- Year/Venue: 2025 / RSS
- Category: World Models, Safety, and Recovery
- Tags: Robotics, VLA, world model, video diffusion, action diffusion, robot data
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://weirdlabuw.github.io/uwm/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation.

## Core Idea
- Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality.
- In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on largescale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable ...
- Our results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms ...
- Imitation learning via supervised learning, often referred to as behavior cloning (BC), has shown remarkable success due to the advent of powerful multimodal generative models such as diffusion ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on largescale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable ...
- Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality.
- However, despite showing robust and reliable behavior within the training distribution, these methods can be brittle w

## Abstract Cue
- —Imitation learning has emerged as a promising approach towards building generalist robots.
