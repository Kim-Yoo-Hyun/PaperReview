# Problem

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ChatVLA-2-Vision-Language-Action-Model-with-Open-World-Rea/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Intuitively, pre-training a VLA model consists of a powerful, pre-trained VLMs, such as PaliGemma or Qwen-VL , should equip the robot with not only stronger vision-language feature embeddings ...
- As a result, the VLA model may fail to accomplish tasks that seem trivial to humans, simply because these tasks were absent from the training dataset.
- We argue that a generalizable VLA model should retain and expand upon the VLM’s core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from ...

## 해결하려는 문제
- We argue that a generalizable VLA model should retain and expand upon the VLM’s core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from ...
- However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic tasks.

## 선행 연구 / 배경 단서
- Intuitively, pre-training a VLA model consists of a powerful, pre-trained VLMs, such as PaliGemma or Qwen-VL , should equip the robot with not only stronger vision-language feature embeddings ...
- As a result, the VLA model may fail to accomplish tasks that seem trivial to humans, simply because these tasks were absent from the training dataset.
- By leveraging the mature neural architectures from language models and multimodal networks, along with advanced training techniques and pre-trained knowledge from VLMs, VLAs significantly enhance robotic learning.
