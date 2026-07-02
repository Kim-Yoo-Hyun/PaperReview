# GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion

- Year/Venue: 2025 / 3DV
- Category: 3D Generative Modeling and Diffusion
- Tags: Diffusion, Generation, depth, 3D Vision
- Paper link: ./2025/3DV/2025_3DV_GRIN-Zero-Shot-Metric-Depth-with-Pixel-Level-Diffusion/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- 3D reconstruction from a single image is a long-standing problem in computer vision.
- Introduction Depth estimation is a fundamental problem in computer vision and a core component of many practical applications, including augmented reality , medical imaging mobile robotics , and ...
- The challenges with this approach are two-fold: (i) the choice of priors themselves, that should Figure 1.

## Core Idea
- Conclusion We introduce GRIN (Geometric RIN), a diffusion-based framework for depth estimation designed to circumvent two of the main shortcomings shown by recent diffusion methods when applied to ...
- In this paper we present GRIN, an efficient diffusion model designed to ingest sparse unstructured training data.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- With comprehensive experiments across eight indoor and outdoor datasets, we show that GRIN establishes a new state of the art in zero-shot metric monocular depth estimation even when ...
- As a result, state of the art approaches show impressive performance in zero-shot relative and metric depth estimation.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In this paper we present GRIN, an efficient diffusion model designed to ingest sparse unstructured training data.
- We use image features with 3D geometric positional encodings to condition the diffusion process both globally and locally, generating depth predictions at a pixel-level.
- GRIN sets a new state of the art in zero-shot metric monocular depth estimation, via efficient pixel-level diffusion and the proper handling of sparse training data.

## Abstract Cue
- 3D reconstruction from a single image is a long-standing problem in computer vision.
