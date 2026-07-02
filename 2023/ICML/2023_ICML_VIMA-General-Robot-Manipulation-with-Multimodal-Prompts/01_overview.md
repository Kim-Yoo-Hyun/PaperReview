# VIMA: General Robot Manipulation with Multimodal Prompts

- Year/Venue: 2023 / ICML
- Category: Vision-Language-Action and Robot Manipulation
- Tags: Vision-Language-Action, Imitation Learning, Robotics
- Paper link: ./2023/ICML/2023_ICML_VIMA-General-Robot-Manipulation-with-Multimodal-Prompts/paper.pdf
- Code/Project: https://vimalabs.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- the same model to perform question answering, machine translation, text summarization, etc.
- Prompt-based learning provides an accessible and flexible interface to communicate a natural language understanding task to a general-purpose model.
- Prompt-based learning has emerged as a successful paradigm in natural language processing, where a single general-purpose language model can be instructed to perform any task specified by input ...

## Core Idea
- Accordingly, we develop a new simulation benchmark that consists of thousands of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for imitation learning, and a four-level evaluation ...
- With 10× less training data, VIMA still performs 2.7× better than the best competing variant.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- VIMA features a recipe that achieves strong model scalability and data efficiency.
- It outperforms alternative designs in the hardest zero-shot generalization setting by up to 2.9× task success rate given the same training data.
- We show that a wide spectrum of robot manipulation tasks can be expressed with multimodal prompts, interleaving textual and visual tokens.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Accordingly, we develop a new simulation benchmark that consists of thousands of procedurally-generated tabletop tasks with multimodal prompts, 600K+ expert trajectories for imitation learning, and a four-level evaluation ...
- It outperforms alternative designs in the hardest zero-shot generalization setting by up to 2.9× task success rate given the same training data.
- With 10× less training data, VIMA still performs 2.7× better than the best competing variant.

## Abstract Cue
- the same model to perform question answering, machine translation, text summarization, etc.
