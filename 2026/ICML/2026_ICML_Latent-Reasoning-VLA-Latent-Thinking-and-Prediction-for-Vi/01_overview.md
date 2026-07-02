# Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_Latent-Reasoning-VLA-Latent-Thinking-and-Prediction-for-Vi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- § Code Vision Vision-Language-Action (VLA) models benefit from chain-of-thought (CoT) reasoning, but existing approaches incur high inference overhead and rely on discrete reasoning representations that mismatch continuous perception ...

## Core Idea
- To realize latent embodied reasoning, we introduce a curriculum-based training paradigm that progressively transitions from explicit textual and visual CoT supervision to latent reasoning, and finally adapts latent ...
- To address these limitations, we introduce latent reasoning, in which textual CoT is replaced by compact continuous latent variables learned via curriculum-style training, and visual CoT is aligned ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experimental results show that LaRA-VLA consistently outperforms state-of-the-art VLA methods while reducing inference latency by up to 90% compared to explicit CoT-based approaches, demonstrating latent reasoning as an ...
- As shown in Figure 5, LaRA-VLA achieves the highest average success rate among all compared methods, substantially outperforming ACT and ECoT and surpassing GR00T N1.5 overall.
- Experiments on simulated benchmarks and long-horizon real-robot manipulation tasks demonstrate that LaRA-VLA achieves strong performance while significantly improving inference efficiency, supporting the view that structured reasoning for embodied ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experimental results show that LaRA-VLA consistently outperforms state-of-the-art VLA methods while reducing inference latency by up to 90% compared to explicit CoT-based approaches, demonstrating latent reasoning as an ...
- To realize latent embodied reasoning, we introduce a curriculum-based training paradigm that progressively transitions from explicit textual and visual CoT supervision to latent reasoning, and finally adapts latent ...
- We propose Latent Reasoning VLA (LaRA-VLA), a unified VLA framework that internalizes multimodal CoT reasoning into continuous latent representations for embodied action.

## Abstract Cue
- § Code Vision Vision-Language-Action (VLA) models benefit from chain-of-thought (CoT) reasoning, but existing approaches incur high inference overhead and rely on discrete reasoning representations that mismatch continuous perception and control.
