# Method

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision, Reinforcement Learning
- Paper link: ./2026/ICML/2026_ICML_Reasoning-VLA-An-Efficient-and-Spatial-Guided-General-Visi/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- These results indicate that our approach provides significant improvements in open-loop evaluation, highlighting the strong generalization capability of the Reasoning-VLA architecture.
- In this paper, we propose Reasoning-VLA, a general and efficient action-generation VLA framework.
- For open-loop evaluation, we use the same testing and validation clips as employed by prior methods.

## 원리적 동기
- These limitations hinder their generalization ability to new driving scenarios.
- However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios.
- These results indicate that our approach provides significant improvements in open-loop evaluation, highlighting the strong generalization capability of the Reasoning-VLA architecture.

## 핵심 방법론
- These results indicate that our approach provides significant improvements in open-loop evaluation, highlighting the strong generalization capability of the Reasoning-VLA architecture.
- For open-loop evaluation, we use the same testing and validation clips as employed by prior methods.
- C LOSED - LOOP E VALUATION We use NeuroNCAP (Ljungbergh et al., 2024) as the closedloop real-world simulator because it provides renderings of novel, unseen scenarios.
- To fairly compare with existing methods, we retain the original training and testing splits of each dataset.
- During training, we shuffle the unified datasets and fine-tune Reasoning-VLA sequentially using SFT followed by RL.
