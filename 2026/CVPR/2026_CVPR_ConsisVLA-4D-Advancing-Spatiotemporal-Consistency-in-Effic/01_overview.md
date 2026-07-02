# ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation

- Year/Venue: 2026 / CVPR
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, consistency, 4D reasoning
- Paper link: ./2026/CVPR/2026_CVPR_ConsisVLA-4D-Advancing-Spatiotemporal-Consistency-in-Effic/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often rely on additional ...
- Due to the lack of a comprehensive understanding of current spatial states and insufficient knowledge of evolving scene dynamics, existing methods struggle to build consistent correlations with predicted ...
- To address these challenges, we propose ConsisVLA-4D, a unified and efficient framework that enhances spatiotemporal consistency in 3D-Perception and 4D-Reasoning.

## Core Idea
- Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We introduce CV-Aligner and ...
- To achieve explicit semantic object selection, we retain only the Top-K tokens most relevant to the instruction: (5) On the other hand, we use the aggregated geometric relation ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that, benefiting from its efficient spatiotemporal consistency design, ConsisVLA-4D achieves 21.6% and 41.5% performance improvements, along with 2.3× and 2.4× inference speedups compared to OpenVLA ...
- Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We introduce CV-Aligner and ...
- Building upon these, we introduce 3) CS-Thinker to achieve Cross-Scene spatiotemporal consistency as actions unfold.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We introduce CV-Aligner and ...
- Extensive experiments demonstrate that, benefiting from its efficient spatiotemporal consistency design, ConsisVLA-4D achieves 21.6% and 41.5% performance improvements, along with 2.3× and 2.4× inference speedups compared to OpenVLA ...
- To achieve explicit semantic object selection, we retain only the Top-K tokens most relevant to the instruction: (5) On the other hand, we use the aggregated geometric relation ...

## Abstract Cue
- Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often rely on additional sensors, introducing substantial computational overhead; 2) visual reasoning is typically limited to future-frame prediction, lacking alignment with ...
