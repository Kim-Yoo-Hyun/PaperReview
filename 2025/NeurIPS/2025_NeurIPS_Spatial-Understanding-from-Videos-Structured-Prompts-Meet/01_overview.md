# Spatial Understanding from Videos: Structured Prompts Meet Simulation Data

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: 3D Large Multimodal Models
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2025/NeurIPS/2025_NeurIPS_Spatial-Understanding-from-Videos-Structured-Prompts-Meet/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- To address these challenges, we propose a dual approach for enhancing 3D spatial reasoning in pre-trained VLMs, without modifying their underlying architecture.
- However, performing 3D spatial reasoning from scanning videos presents two significant challenges: (1) Spatial Uncertainty.
- Effectively addressing this challenge demands multi-step logical reasoning across frames to reconstruct coherent spatial layouts. (2) Data Scarcity.

## Core Idea
- To address these challenges, we present a unified framework for enhancing 3D spatial reasoning in pre-trained VLMs without modifying their architecture.
- 5.1 Performace Comparison We investigated the following five key questions to assess our approach: Q1: Which scene representation format is most interpretable by VLMs?

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments across multiple benchmarks demonstrate the individual and combined effectiveness of our prompting and fine-tuning strategies, and yield insights that may inspire future research on visual-spatial understanding.
- Across all models, a consistent trend emerges: the +Des variant outperforms others, followed by 7
- The experimental settings (including benchmarks, baselines, etc.) and more experimental results can be found in the Appendix A and B.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- To address these challenges, we present a unified framework for enhancing 3D spatial reasoning in pre-trained VLMs without modifying their architecture.
- Extensive experiments across multiple benchmarks demonstrate the individual and combined effectiveness of our prompting and fine-tuning strategies, and yield insights that may inspire future research on visual-spatial understanding.
- However, existing methods face spatial uncertainty and data scarcity, limiting the 3D spatial reasoning capability of pre-trained visionlanguage models (VLMs).

## Abstract Cue
- Visual-spatial understanding, the ability to infer object relationships and layouts from visual input, is fundamental to downstream tasks such as robotic navigation and embodied interaction.
