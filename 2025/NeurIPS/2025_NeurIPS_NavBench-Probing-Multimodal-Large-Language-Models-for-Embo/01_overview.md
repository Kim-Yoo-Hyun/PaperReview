# NavBench: Probing Multimodal Large Language Models for Embodied Navigation

- Year/Venue: 2025 / NeurIPS Poster
- Category: Navigation and Embodied AI
- Tags: Navigation
- Paper link: ./2025/NeurIPS/2025_NeurIPS_NavBench-Probing-Multimodal-Large-Language-Models-for-Embo/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- For example, navigating across multiple rooms with ambiguous instructions poses greater challenges than following simple step-by-step commands in a single hallway.
- The step-by-step navigation is assessed from different difficulty levels, which is defined by cognitive, spatial, and execution complexity. and ObjectNav , were developed prior to the emergence of ...
- Furthermore, navigation tasks in real-world environments can vary significantly in difficulty due to differences in spatial layout, instruction complexity, and required decision-making steps.

## Core Idea
- We present NavBench, a benchmark to evaluate the embodied navigation capabilities of MLLMs under zero-shot settings.
- To support real-world deployment, we introduce a pipeline that converts MLLMs’ outputs into robotic actions.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Results also show that models with higher comprehension scores tend to achieve better execution performance.
- Providing map-based context improves decision accuracy, especially in medium-difficulty scenarios.
- We present NavBench, a benchmark to evaluate the embodied navigation capabilities of MLLMs under zero-shot settings.

## Limitation
- We hope NavBench can serve as a useful resource for analyzing the embodied capabilities of MLLMs and supporting future work in this direction.
- Through evaluation and targeted analysis, NavBench reveals limitations in temporal understanding and action grounding that are not captured by standard success metrics.

## Contribution
- We present NavBench, a benchmark to evaluate the embodied navigation capabilities of MLLMs under zero-shot settings.
- Results also show that models with higher comprehension scores tend to achieve better execution performance.
- To support real-world deployment, we introduce a pipeline that converts MLLMs’ outputs into robotic actions.

## Abstract Cue
- Multimodal Large Language Models (MLLMs) have demonstrated strong generalization in vision-language tasks, yet their ability to understand and act within embodied environments remains underexplored.
