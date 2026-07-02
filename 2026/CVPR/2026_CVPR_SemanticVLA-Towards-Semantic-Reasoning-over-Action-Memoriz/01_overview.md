# SemanticVLA: Towards Semantic Reasoning over Action Memorization via Synergistic Explicit Trace and Latent Action Planning

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, semantic reasoning, Planning
- Paper link: ./2026/CVPR/2026_CVPR_SemanticVLA-Towards-Semantic-Reasoning-over-Action-Memoriz/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, current works fail to genuinely leverage VLM capabilities: VLMs produce latent embeddings that lack semantic interpretability, providing ambiguous and unstable guidance to downstream policies, while solely action ...

## Core Idea
- To bridge this gap, we introduce SemanticVLA, which leverages VLM reasoning through synergistic dual-path design.
- By bridging VLM reasoning and action expert through semantically explicit trace and visually grounded latent action tokens, our approach enables semantic reasoning rather than action memorization.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- SemanticVLA achieves 97.0% average success rate on LIBERO and 65.1% on SimplerEnv WidowX, substantially outperforming strong baselines.
- More importantly, SemanticVLA maintains significantly more stable performance under instruction rephrasing in both simulation suites, and demonstrates strong advantages on real-world long-horizon and reasoning-intensive tasks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- SemanticVLA achieves 97.0% average success rate on LIBERO and 65.1% on SimplerEnv WidowX, substantially outperforming strong baselines.
- However, current works fail to genuinely leverage VLM capabilities: VLMs produce latent embeddings that lack semantic interpretability, providing ambiguous and unstable guidance to downstream policies, while solely action ...
- To bridge this gap, we introduce SemanticVLA, which leverages VLM reasoning through synergistic dual-path design.

## Abstract Cue
- Vision-Language-Action (VLA) models have emerged as a promising paradigm where pretrained Vision-Language Models (VLMs) serve as System 2 for high-level reasoning, connected to action experts as System 1 for low-level motor control.
