# A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision

- Year/Venue: 2025 / ICCV
- Category: 3D Generative Modeling and Diffusion
- Tags: Gaussian Splatting, Diffusion, Generation, 3D Vision
- Paper link: ./2025/ICCV/2025_ICCV_A-Lesson-in-Splats-Teacher-Guided-Diffusion-for-3D-Gaussia/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- First, it is an ill-posed problem because different 3D shapes can produce identical 2D projections.
- A key challenge in training 3D diffusion models with 2D supervi- sion is that the standard training paradigm requires both the denoising process and supervision to be in ...
- Current approaches for 3D reconstruction from single images can be categorized into two main types: deterministic predictions and generative models, each with distinct limitations.

## Core Idea
- We present a novel framework for training 3D imageconditioned diffusion models using only 2D supervision.
- Our approach leverages suboptimal predictions from a deterministic imageto-3D model—acting as a "teacher"—to generate noisy 3D inputs, enabling effective 3D diffusion training without requiring full 3D ground truth.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our results show that our approach consistently improves upon these deterministic teachers, demonstrating its effectiveness in scalable and high-fidelity 3D generative modeling.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We present a novel framework for training 3D imageconditioned diffusion models using only 2D supervision.
- Our results show that our approach consistently improves upon these deterministic teachers, demonstrating its effectiveness in scalable and high-fidelity 3D generative modeling.
- Our approach leverages suboptimal predictions from a deterministic imageto-3D model—acting as a "teacher"—to generate noisy 3D inputs, enabling effective 3D diffusion training without requiring full 3D ground truth.

## Abstract Cue
- We present a novel framework for training 3D imageconditioned diffusion models using only 2D supervision.
