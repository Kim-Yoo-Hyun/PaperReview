# Method

- Year/Venue: 2026 / ICRA
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, Reinforcement Learning
- Paper link: ./2026/ICRA/2026_ICRA_Goal-VLA-Image-Generative-VLMs-As-Object-Centric-World-Mod/paper.pdf
- Code/Project: not identified from venue audit
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In this work, we present GoalVLA, a zero-shot framework that leverages Image-Generative VLMs as world models to generate desired goal states, from which the target object pose is ...
- To further improve robustness, we introduce a Reflection-through-Synthesis process that iteratively validates and refines the generated goal image before execution.
- Spatial Grounding The Spatial Grounding module consists of two main stages: semantic matching and point-cloud registration.

## 원리적 동기
- — Generalization remains a fundamental challenge in robotic manipulation.
- To tackle this challenge, recent VisionLanguage-Action (VLA) models build policies on top of VisionLanguage Models (VLMs), seeking to transfer their openworld semantic knowledge.
- In this work, we present GoalVLA, a zero-shot framework that leverages Image-Generative VLMs as world models to generate desired goal states, from which the target object pose is ...

## 핵심 방법론
- Spatial Grounding The Spatial Grounding module consists of two main stages: semantic matching and point-cloud registration.
- A significant drawback, however, is that the low-level policy typically needs to be trained to interpret these visual goals, which reintroduces a data dependency and undermines the objective ...
- Reflection in Foundation Models Reflection mechanisms, which enable generative models to iteratively critique and refine their outputs, have recently attracted growing attention as a promising approach for enhancing ...
