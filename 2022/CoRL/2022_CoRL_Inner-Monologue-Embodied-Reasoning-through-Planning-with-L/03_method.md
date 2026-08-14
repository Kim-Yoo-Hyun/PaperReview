# Method

- Year/Venue: 2022 / CoRL
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, feedback, replanning, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://innermonologue.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Brief Method
- We propose that by leveraging environment feedback, LLMs are able to form an inner monologue that allows them to more richly process and plan in robotic control scenarios.
- Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.
- Our work studies these questions by combining LLMs with various sources of textual feedback, only utilizing few-shot prompting without any additional training.

## 원리적 동기
- This raises an intriguing possibility: beyond their ability to interpret natural language instructions, can language models further serve as reasoning models that combine multiple sources of feedback and ...
- While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP ) or hierarchical learning (e.g., HRL ), effective high-level reasoning about complex tasks also ...
- We propose that by leveraging environment feedback, LLMs are able to form an inner monologue that allows them to more richly process and plan in robotic control scenarios.

## 핵심 방법론
- Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.
- Our work studies these questions by combining LLMs with various sources of textual feedback, only utilizing few-shot prompting without any additional training.
