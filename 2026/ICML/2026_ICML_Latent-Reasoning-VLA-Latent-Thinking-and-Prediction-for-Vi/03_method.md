# Method

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics
- Paper link: ./2026/ICML/2026_ICML_Latent-Reasoning-VLA-Latent-Thinking-and-Prediction-for-Vi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To realize latent embodied reasoning, we introduce a curriculum-based training paradigm that progressively transitions from explicit textual and visual CoT supervision to latent reasoning, and finally adapts latent ...
- To address these limitations, we introduce latent reasoning, in which textual CoT is replaced by compact continuous latent variables learned via curriculum-style training, and visual CoT is aligned ...
- We propose Latent Reasoning VLA (LaRA-VLA), a unified VLA framework that internalizes multimodal CoT reasoning into continuous latent representations for embodied action.

## 원리적 동기
- § Code Vision Vision-Language-Action (VLA) models benefit from chain-of-thought (CoT) reasoning, but existing approaches incur high inference overhead and rely on discrete reasoning representations that mismatch continuous perception ...
- To realize latent embodied reasoning, we introduce a curriculum-based training paradigm that progressively transitions from explicit textual and visual CoT supervision to latent reasoning, and finally adapts latent ...

## 핵심 방법론
- To address these limitations, we introduce latent reasoning, in which textual CoT is replaced by compact continuous latent variables learned via curriculum-style training, and visual CoT is aligned ...
- Vision Language Action Models VLA models extend large multimodal language models to robotic control, with extensive efforts devoted to architectural advances (Black et al., 2024; Intelligence et al., ...
- Among these directions, CoT reasoning at training time has proven particularly effective.
