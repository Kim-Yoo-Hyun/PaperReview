# Method

- Year/Venue: 2025 / NeurIPS Poster
- Category: Vision-Language-Action and Robot Manipulation
- Tags: VLA, Vision-Language Model, Reinforcement Learning
- Paper link: ./2025/NeurIPS/2025_NeurIPS_ChatVLA-2-Vision-Language-Action-Model-with-Open-World-Rea/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- In contrast, our approach deals with diverse, novel reasoning types not encountered in the training data.
- We introduce an enhanced reasoning-following module designed to improve reasoning capabilities in action models.
- Therefore, our method requires a more robust and flexible VLA model capable of effectively following complex, out-of-distribution reasoning.

## 원리적 동기
- Intuitively, pre-training a VLA model consists of a powerful, pre-trained VLMs, such as PaliGemma or Qwen-VL , should equip the robot with not only stronger vision-language feature embeddings ...
- As a result, the VLA model may fail to accomplish tasks that seem trivial to humans, simply because these tasks were absent from the training dataset.
- In contrast, our approach deals with diverse, novel reasoning types not encountered in the training data.

## 핵심 방법론
- In contrast, our approach deals with diverse, novel reasoning types not encountered in the training data.
- We introduce an enhanced reasoning-following module designed to improve reasoning capabilities in action models.
- Therefore, our method requires a more robust and flexible VLA model capable of effectively following complex, out-of-distribution reasoning.
- A distinctive feature of our method is that the model not only follows given instructions but also aligns robotic actions closely with the generated reasoning.
- Specifically, our approach utilizes an adaptive routing strategy where expert modules are dynamically selected based on the characteristics of the visual and textual inputs.
