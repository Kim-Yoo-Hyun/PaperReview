# GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data

- Year/Venue: 2025 / CoRL
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, grasping, synthetic data
- Paper link: ./2025/CoRL/2025_CoRL_GraspVLA-a-Grasping-Foundation-Model-Pre-trained-on-Billio/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, unlike vision and language modalities, action data is absent from existing Internet datasets, demanding a new paradigm for data collection.
- However, gathering real-world data at a large scale is both labor-intensive and costly, requiring a large number of robots and human operators, as well as diverse physical setups.
- In contrast, synthetic data offers a more accessible and cost-effective alternative – yet its potential remains largely underestimated.

## Core Idea
- In summary, our contributions are as follows: a) we introduce a novel pretraining paradigm that relies entirely on synthetic action data, significantly reducing the real world action data ...
- To efficiently learn from this dataset, we propose GraspVLA, an end-to-end network that integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chainof-Thought (CoT) process, named ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive evaluations across real-world and simulation benchmarks demonstrate GraspVLA’s advanced zero-shot generalizability and few-shot adaptability to specific human preferences.
- We will release SynGrasp We evaluate GraspVLA to answer the following questions: (1) How does GraspVLA compare with existing work under various generalization factors? (2) How does GraspVLA ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- : Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training.
- Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks.
- Extensive evaluations across real-world and simulation benchmarks demonstrate GraspVLA’s advanced zero-shot generalizability and few-shot adaptability to specific human preferences.

## Abstract Cue
- : Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training.
