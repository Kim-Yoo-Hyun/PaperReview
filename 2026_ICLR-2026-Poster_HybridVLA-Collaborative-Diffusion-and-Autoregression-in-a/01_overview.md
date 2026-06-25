# HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model

- Year/Venue: 2026 / ICLR 2026 Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Diffusion
- Authors: Jiaming Liu, Hao Chen, Zhuoyang Liu, Pengju An, Renrui Zhang, Chenyang Gu, Xiaoqi Li, Ziyu Guo
- Paper: https://openreview.net/forum?id=H1KDMNOKQn
- PDF status: downloaded
- GitHub/Project: not identified from OpenReview

## Problem
생성 모델 또는 policy 모델이 3D 구조와 물리 제약을 보존하지 못하면 로봇 실행이나 3D 장면 생성에서 일관성이 깨진다.

## Core Idea
핵심은 diffusion score/denoising process를 action, 3D generation, 또는 structured scene representation에 적용하면서 geometry prior를 넣는 것이다.

## Paper-Specific Cues
- Topic cue: A central objective of manipulation policy design is to enable robots to comprehend human instructions and predict generalized actions in unstructured environments.
- Method cue: To integrate the complementary strengths of autoregressive and diffusion generation, we introduce HybridVLA, which innovatively leverages a shared LLM backbone to perform iterative action ...
- Result cue: While these models achieve efficient and scalable training, the discretization undermines the continuity required for precise control.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `diffusion-based generation or policy learning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
대규모 pretraining 의존성, benchmark 편향, compute 비용, 실제 환경 generalization을 별도로 검증해야 한다.

## Contribution
- diffusion-based generation or policy learning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: VLA, Vision-Language Model, Robotics, Diffusion.
- 초록에서 확인되는 주요 cue: Recent, VLA, VLMs, While, VLM, LLM, HybridVLA, Specifically.
