# LAGEA: Language Guided Embodied Agents for Robotic Manipulation

- Year/Venue: 2026 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Robotics, Reinforcement Learning
- Paper link: ./2026/ICML/2026_ICML_LAGEA-Language-Guided-Embodied-Agents-for-Robotic-Manipula/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Yet converting such priors into reliable learning signals still hinges on reward design, which remains a bottleneck across tasks and scenes.
- Robotic manipulation benefits from foundation models that describe goals, but today’s agents still lack a principled way to learn from their own mistakes.
- L AGEA summarizes each attempt in concise language, localizes the decisive moments in the trajectory, aligns feedback with visual state in a shared representation, and converts goal progress ...

## Core Idea
- We introduce L AGEA (Language Guided Embodied Agents), a framework that turns episodic, schema-constrained reflections from a vision language model (VLM) into temporally grounded guidance for reinforcement learning.
- Simply adding these signals can destabilize training or encourage reward hacking.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- On the Meta-World MT10 and Robotic Fetch embodied manipulation benchmark, L AGEA improves average success over the state-of-the-art (SOTA) methods by 9.0% on random goals, 5.3% on fixed ...
- These results support our hypothesis: language, when structured and grounded in time, is an effective mechanism for teaching robots to selfreflect on mistakes and make better choices.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- On the Meta-World MT10 and Robotic Fetch embodied manipulation benchmark, L AGEA improves average success over the state-of-the-art (SOTA) methods by 9.0% on random goals, 5.3% on fixed ...
- We introduce L AGEA (Language Guided Embodied Agents), a framework that turns episodic, schema-constrained reflections from a vision language model (VLM) into temporally grounded guidance for reinforcement learning.
- Simply adding these signals can destabilize training or encourage reward hacking.

## Abstract Cue
- grounded affordance reasoning (Ahn et al., 2022) to vision–language–action transfer, robots now display compelling zero-shot behaviour and semantic competence (Driess et al., 2023; Kim et al., 2024; Brohan et al., 2024).
