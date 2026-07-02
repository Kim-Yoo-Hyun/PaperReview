# On-Device Diffusion Transformer Policy for Efficient Robot Manipulation

- Year/Venue: 2025 / ICCV
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Diffusion
- Paper link: ./2025/ICCV/2025_ICCV_On-Device-Diffusion-Transformer-Policy-for-Efficient-Robot/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We first conduct an extensive computational analysis on existing Diffusion Policy architectures, identifying the denoising network as the primary contributor to latency.
- However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures involve billions of parameters, leading ...
- To address these challenges, recent work by DeeR-VLA introduces a multi-exit architecture built on the Roboflamingo framework , enabling dynamic termination of the computation process to accelerate action ...

## Core Idea
- To overcome performance degradation typically associated with conventional pruning methods, we introduce a unified pruning and retraining pipeline, optimizing the model’s postpruning recoverability explicitly.
- In this paper, we propose LightDP, a novel framework specifically designed to accelerate Diffusion Policies for real-time deployment on mobile devices.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive real-world experiments also show the proposed LightDP can achieve performance comparable to state-ofthe-art Diffusion Policies.
- Experimental evaluations on the standard datasets, i.e., PushT, Robomimic, CALVIN, and LIBERO, demonstrate that LightDP achieves real-time action prediction on mobile devices with competitive performance, marking an important ...
- While this design achieves considerable computation reduction on GPU devices, its early exit strategy remains suboptimally tuned for mobile platforms.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive real-world experiments also show the proposed LightDP can achieve performance comparable to state-ofthe-art Diffusion Policies.
- We first conduct an extensive computational analysis on existing Diffusion Policy architectures, identifying the denoising network as the primary contributor to latency.
- However, this endeavor presents multifaceted challenges: 1) Diffusion Policies require multiple denoising steps, which slows down the generation process; 2) the standard architectures involve billions of parameters, leading ...

## Abstract Cue
- zhenghao.chen@newcastle.edu.au Diffusion Policies have significantly advanced robotic manipulation tasks via imitation learning, but their application on resource-constrained mobile platforms remains challenging due to computational inefficiency and extensive memory footprint.
