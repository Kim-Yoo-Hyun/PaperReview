# From Thousands to Billions: 3D Visual Language Grounding via Render-Supervised Distillation from 2D VLMs

- Year/Venue: 2025 / ICML Poster
- Category: 3D Vision-Language Grounding
- Tags: Vision-Language Model, 3D Vision
- Paper link: ./2025/ICML/2025_ICML_From-Thousands-to-Billions-3D-Visual-Language-Grounding-vi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision.
- This six-order-of-magnitude gap in data availability severely limits the capabilities of current 3D grounding systems, creating one of the most significant challenges in embodied AI.
- While 2D vision-language models are trained on billions of labeled images and masks (Achiam et al., 2023; Touvron et al., 2023; Radford et al., 2021; Labs, 2023), existing ...

## Core Idea
- This rendersupervised formulation enables end-to-end training of complete encoder-decoder architectures and is inherently model-agnostic.
- Loss Ablation Existing pretraining pipelines primarily focus on the encoder (Zhu et al., 2023b; Banani et al., 2021), whereas the render-supervised formulation can pretrain the entire architecture in ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- LIFT-GS achieves state-of-the-art results with 25.7% mAP on open-vocabulary instance segmentation (vs.
- 20.2% prior SOTA) and consistent 10-30% improvements on referential grounding tasks.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- This rendersupervised formulation enables end-to-end training of complete encoder-decoder architectures and is inherently model-agnostic.
- LIFT-GS achieves state-of-the-art results with 25.7% mAP on open-vocabulary instance segmentation (vs.
- We introduce LIFT-GS, a practical distillation technique that overcomes this limitation by using differentiable rendering to bridge 3D and 2D supervision.

## Abstract Cue
- 3D vision-language grounding faces a fundamental data bottleneck: while 2D models train on billions of images, 3D models have access to only thousands of labeled scenes–a six-order-ofmagnitude gap that severely limits performance.
