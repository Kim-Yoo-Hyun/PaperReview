# Do As I Can, Not As I Say: Grounding Language in Robotic Affordances

- Year/Venue: 2022 / CoRL
- Category: Foundations: Vision-Language-Action and Robotics
- Tags: LLM, affordance, Planning, Robotics
- Paper link: ./2022/CoRL/2022_CoRL_Do-As-I-Can-Not-As-I-Say-Grounding-Language-in-Robotic-Aff/paper.pdf
- Code/Project: https://say-can.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, a significant weakness of language models is that they lack real-world experience, which makes it difficult to leverage them for decision making within a given embodiment.

## Core Idea
- We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are both feasible and ...
- Recent progress in training large language models (LLMs) has led to systems that can generate complex text based on prompts, answer questions, or even engage in dialogue on ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The results in Table 2 illustrate the necessity of the language grounding where BC NL achieves 0% in all tasks and BC USE achieves 60% for single primitives, ...
- In the mock kitchen, PaLMSayCan achieved a planning success rate of 84% and an execution rate of 74%.
- We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is capable of completing long-horizon, ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We evaluate our method on a number of real-world robotic tasks, where we show the need for real-world grounding and that this approach is capable of completing long-horizon, ...
- We propose to provide real-world grounding by means of pretrained skills, which are used to constrain the model to propose natural language actions that are both feasible and ...
- We show how low-level skills can be combined with large language models so that the language model provides high-level knowledge about the procedures for performing complex and temporally ...

## Abstract Cue
- : Large language models can encode a wealth of semantic knowledge about the world.
