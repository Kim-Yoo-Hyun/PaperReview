# SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning

- Year/Venue: 2025 / NeurIPS Spotlight
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2025/NeurIPS/2025_NeurIPS_SafeVLA-Towards-Safety-Alignment-of-Vision-Language-Action/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Our proposed pipeline employs multifaceted framework for the systematic safety alignment of vision-language-action (VLA) models. challenges posed by the complex and unpredictable physical world .
- To tackle this challenge, we make the first systematic explorations into VLA safety alignment.
- Our investigation addresses the significant engineering challenges in adapting and scaling these principles for VLAs, focusing on how to effectively model, elicit, and utilize safety signals.

## Core Idea
- We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The results demonstrate that our approach with dynamic Lagrangian multipliers achieves a superior trade-off, adhering to the cost limit while attaining a higher success rate than any fixed-penalty ...
- The results consistently show that ISA alignment leads to substantial improvements across these models, evidenced by significant reductions in CC alongside stable SR when evaluated on Safety-CHORES and ...
- ISA achieves an average SR increase of 3.85% compared to FLaRe, outperforming IL-only baselines and matching or exceeding other RL-based methods.

## Limitation
- Crucially, aligned policies showed robust safety assurance, mitigating long-tail risks and generalizing to out-of-distribution perturbations and extreme failures, marking a first systematic integration of explicit safety constraints into ...
- In this work, we introduce an ISA to mitigate significant safety challenges of VLA.

## Contribution
- Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, reducing the cumulative cost of safety violations by 83.58% compared to the ...
- We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, ...
- Vision-language-action models (VLAs) show potential as generalist robot policies.

## Abstract Cue
- Vision-language-action models (VLAs) show potential as generalist robot policies.
