# HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model
- Paper link: ./2026/ICML/2026_ICML_HALO-A-Unified-Vision-Language-Action-Model-for-Embodied-M/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, most existing VLAs map perceptual inputs directly to motor commands, lacking explicit mechanisms for reasoning about task structure or anticipating how the environment will evolve under motion ...
- This limitation becomes particularly pronounced in long-horizon or out-of-distribution scenarios—such as novel layouts, unfamiliar objects, or contact-rich interactions—where successful execution depends more on deliberation and foresight than on ...
- Recent work has sought to address this limitation by introducing intermediate reasoning processes like human.

## Core Idea
- To enable H ALO learning at scale, we introduce an automated pipeline to synthesize EM-CoT training data along with a carefully crafted training recipe.
- To this end, we propose H ALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning through textual reasoning, fine-grained visual subgoal prediction, and EM-CoT-augmented action ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Extensive experiments demonstrate that: (1) H ALO achieves superior performance in both simulated and real world, surpassing baseline policy π0 by 25.9% on the RoboTwin benchmark; (2) all ...
- Vision-Language-Action (VLA) models (Black et al., 2024; NVIDIA et al., 2025) have shown a compelling path toward general-purpose robotic manipulation.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Extensive experiments demonstrate that: (1) H ALO achieves superior performance in both simulated and real world, surpassing baseline policy π0 by 25.9% on the RoboTwin benchmark; (2) all ...
- To enable H ALO learning at scale, we introduce an automated pipeline to synthesize EM-CoT training data along with a carefully crafted training recipe.
- We instantiate H ALO with a Mixture-ofTransformers (MoT) architecture that decouples semantic reasoning, visual foresight, and action prediction into specialized experts with seamless cross-expert collaboration.

## Abstract Cue
- Vision-Language-Action (VLA) models (Black et al., 2024; NVIDIA et al., 2025) have shown a compelling path toward general-purpose robotic manipulation.
