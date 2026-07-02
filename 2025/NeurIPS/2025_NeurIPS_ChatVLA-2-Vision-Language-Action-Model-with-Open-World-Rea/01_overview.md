# ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ChatVLA-2-Vision-Language-Action-Model-with-Open-World-Rea/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Intuitively, pre-training a VLA model consists of a powerful, pre-trained VLMs, such as PaliGemma or Qwen-VL , should equip the robot with not only stronger vision-language feature embeddings ...
- As a result, the VLA model may fail to accomplish tasks that seem trivial to humans, simply because these tasks were absent from the training dataset.
- We argue that a generalizable VLA model should retain and expand upon the VLM’s core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from ...

## Core Idea
- In contrast, our approach deals with diverse, novel reasoning types not encountered in the training data.
- We introduce an enhanced reasoning-following module designed to improve reasoning capabilities in action models.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We argue that a generalizable VLA model should retain and expand upon the VLM’s core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from ...
- We do not evaluate using simulation benchmarks, as the VLA capabilities demonstrated by our approach exceed what current simulation benchmarks can assess.
- These experiments examine the model’s proficiency in mathematical reasoning, spatial reasoning, optical character recognition (OCR), and object recognition and localization, most within an open-world context involving scenarios that ...

## Limitation
- Developing models capable of reasoning and general understanding within open-world scenarios remains a frontier research topic that has yet to be thoroughly explored.

## Contribution
- We argue that a generalizable VLA model should retain and expand upon the VLM’s core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from ...
- However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic tasks.

## Abstract Cue
- Vision-language-action (VLA) models have emerged as the next generation of models in robotics.
