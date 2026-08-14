# LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

- Year/Venue: 2023 / arXiv
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, LLM planning, classical planning, PDDL, plan verification
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://github.com/Cranial-XIX/llm-p
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- A Failure Example of GPT-4 in Planning Problem (P1): You have 5 blocks.
- However, so far, LLMs cannot reliably solve long-horizon robot planning problems.
- By contrast, classical planners, once a problem is given in a formatted way, can use efficient search algorithms to quickly identify correct, or even optimal, plans.

## Core Idea
- Specifically, they can be (relatively) easily fooled by, for example, asking for the result of a straightforward arithmetic problem that does not appear in their training corpus or ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Via a comprehensive set of experiments on these benchmark problems, we find that LLM+P is able to provide optimal solutions for most problems, while LLMs fail to provide ...
- We also show LLM+P enables a home robot to solve a complex manipulation task that is specified by the user in natural language.
- — Large language models (LLMs) have demonstrated remarkable zero-shot generalization abilities: stateof-the-art chatbots can provide plausible answers to many common questions that arise in daily life.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Via a comprehensive set of experiments on these benchmark problems, we find that LLM+P is able to provide optimal solutions for most problems, while LLMs fail to provide ...
- Specifically, they can be (relatively) easily fooled by, for example, asking for the result of a straightforward arithmetic problem that does not appear in their training corpus or ...
- Along with LLM+P, we define a diverse set of different benchmark problems taken from robot planning scenarios.

## Abstract Cue
- — Large language models (LLMs) have demonstrated remarkable zero-shot generalization abilities: stateof-the-art chatbots can provide plausible answers to many common questions that arise in daily life.
