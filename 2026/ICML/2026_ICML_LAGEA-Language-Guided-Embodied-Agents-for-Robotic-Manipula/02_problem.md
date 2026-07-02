# Problem

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Reinforcement Learning
- Paper link: ./2026/ICML/2026_ICML_LAGEA-Language-Guided-Embodied-Agents-for-Robotic-Manipula/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- Yet converting such priors into reliable learning signals still hinges on reward design, which remains a bottleneck across tasks and scenes.
- Robotic manipulation benefits from foundation models that describe goals, but today’s agents still lack a principled way to learn from their own mistakes.
- L AGEA summarizes each attempt in concise language, localizes the decisive moments in the trajectory, aligns feedback with visual state in a shared representation, and converts goal progress ...

## 해결하려는 문제
- On the Meta-World MT10 and Robotic Fetch embodied manipulation benchmark, L AGEA improves average success over the state-of-the-art (SOTA) methods by 9.0% on random goals, 5.3% on fixed ...
- We introduce L AGEA (Language Guided Embodied Agents), a framework that turns episodic, schema-constrained reflections from a vision language model (VLM) into temporally grounded guidance for reinforcement learning.
- Simply adding these signals can destabilize training or encourage reward hacking.

## 선행 연구 / 배경 단서
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.
