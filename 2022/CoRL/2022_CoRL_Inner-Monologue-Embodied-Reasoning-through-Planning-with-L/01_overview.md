# Inner Monologue: Embodied Reasoning through Planning with Language Models

- Year/Venue: 2022 / CoRL
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, feedback, replanning, long-horizon manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://innermonologue.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- This raises an intriguing possibility: beyond their ability to interpret natural language instructions, can language models further serve as reasoning models that combine multiple sources of feedback and ...
- While conventionally these challenges have been approached from the perspective of planning (e.g., TAMP ) or hierarchical learning (e.g., HRL ), effective high-level reasoning about complex tasks also ...
- While prior work has investigated using language models as planners or incorporating Robot Planning & Interaction Grounded Closed-Loop Feedback Robot Environments Robot Human Can you bring me the ...

## Core Idea
- We propose that by leveraging environment feedback, LLMs are able to form an inner monologue that allows them to more richly process and plan in robotic control scenarios.
- Inspired by the human thought process, we propose that such an inner monologue is a natural framework for incorporating feedback for LLMs.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Below, we show results for a tabletop manipulation environment in sim (Sec 4.1) and real (Sec 4.2) as well as a mobile manipulation environment in real (Sec 4.3).
- We find that closed-loop language feedback significantly improves high-level instruction completion on three domains, including simulated and real table top rearrangement tasks and long-horizon mobile manipulation tasks in ...
- For more details about the experiment setup and results, please refer to the Appendix.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We propose that by leveraging environment feedback, LLMs are able to form an inner monologue that allows them to more richly process and plan in robotic control scenarios.
- In this work, we investigate to what extent LLMs used in such embodied contexts can reason over sources of feedback provided through natural language, without any additional training.
- We find that closed-loop language feedback significantly improves high-level instruction completion on three domains, including simulated and real table top rearrangement tasks and long-horizon mobile manipulation tasks in ...

## Abstract Cue
- : Recent works have shown how the reasoning capabilities of Large Language Models (LLMs) can be applied to domains beyond natural language processing, such as planning and interaction for robots.
