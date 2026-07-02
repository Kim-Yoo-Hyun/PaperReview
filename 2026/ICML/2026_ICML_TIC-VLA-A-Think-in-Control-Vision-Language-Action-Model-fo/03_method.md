# Method

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: VLA, Vision-Language Model, Robotics, Navigation, Reinforcement Learning
- Paper link: ./2026/ICML/2026_ICML_TIC-VLA-A-Think-in-Control-Vision-Language-Action-Model-fo/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- To support realistic evaluation, we present DynaNav, a physics-accurate, photo-realistic simulation suite for language-guided navigation in dynamic environments.
- We introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly models delayed semantic reasoning during action generation.
- We further propose a latency-consistent training pipeline that injects reasoning inference delays during imitation learning and online reinforcement learning, aligning training with asynchronous deployment.

## 원리적 동기
- Robots in dynamic, human-centric environments must follow language instructions while maintaining real-time reactive control.
- Vision-languageaction (VLA) models offer a promising framework, but they assume temporally aligned reasoning and control, despite semantic inference being inherently delayed relative to real-time action.
- To support realistic evaluation, we present DynaNav, a physics-accurate, photo-realistic simulation suite for language-guided navigation in dynamic environments.

## 핵심 방법론
- All evaluations are conducted zero-shot, without task-specific training data.
