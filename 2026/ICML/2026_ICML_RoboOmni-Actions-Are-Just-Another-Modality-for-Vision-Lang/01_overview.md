# RoboOmni: Actions Are Just Another Modality for Vision-Language Models

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_RoboOmni-Actions-Are-Just-Another-Modality-for-Vision-Lang/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, a critical challenge has emerged: while built upon highly capable VLMs, many current VLA implementations struggle to retain the broad generalization abilities inherent in their parent models.
- However, unified discrete frameworks lag behind decoupled continuous designs due to limitations in action chunking and temporal modeling.
- Instead, they often overfit significantly to the specific robotic datasets and environments seen during training (Li et al., 2026; Kim et al., 2024), losing the zero-shot or few-shot ...

## Core Idea
- To address this, we introduce RoboOmni, a unified multi-modal next-token prediction framework.
- At the core of our method is Multi-Token Action Prediction (MTAP), which integrates action chunking directly into the discrete tokenizer.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive evaluations on the CALVIN, SimplerEnv, and realworld platforms confirm that RoboOmni establishes new state-of-the-art performance, significantly outperforming diffusion-based baselines such as π0 .
- Notably, combining our proposed MTAP with the FAST tokenizer achieves a 94.4% average success rate on CALVIN, while the Bin tokenizer implementation attains a 27× inference speedup compared ...
- Challenging the assumption that continuous modeling is essential for high-performance manipulation, RoboOmni demonstrates that actions are just another modality capable of being effectively modeled discretely.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive evaluations on the CALVIN, SimplerEnv, and realworld platforms confirm that RoboOmni establishes new state-of-the-art performance, significantly outperforming diffusion-based baselines such as π0 .
- To address this, we introduce RoboOmni, a unified multi-modal next-token prediction framework.
- At the core of our method is Multi-Token Action Prediction (MTAP), which integrates action chunking directly into the discrete tokenizer.

## Abstract Cue
- pable of complex multimodal understanding and physical interaction (Zitkovich et al., 2023; Li et al., 2023; Shao & Xie, 2024; Lin et al., 2022; Tan et al., 2023).
