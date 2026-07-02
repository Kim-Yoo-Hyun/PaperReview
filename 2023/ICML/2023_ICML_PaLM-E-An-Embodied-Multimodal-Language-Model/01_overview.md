# PaLM-E: An Embodied Multimodal Language Model

- Year/Venue: 2023 / ICML
- Category: Foundations: Vision-Language-Action and Robotics
- Tags: LLM, Vision-Language, Robotics
- Paper link: ./2023/ICML/2023_ICML_PaLM-E-An-Embodied-Multimodal-Language-Model/paper.pdf
- Code/Project: https://palm-e.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may lead to representations ...
- However, enabling general inference in the real world, e.g. for robotics problems, raises the challenge of grounding.
- Previous work (Ahn et al., 2022) interfaces the output of LLMs with learned robotic policies and affordance functions to make decisions, but is limited in that the LLM ...

## Core Idea
- We propose embodied language models to directly incorporate real-world continuous sensor modalities into language models and thereby establish the link between words and percepts.
- However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may lead to representations ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typic
- Our largest model, PaLM-E-562B with 562B parameters, in addition to being trained on robotics tasks, is a visual-language generalist with state-of-the-art performance on OK-VQA, and retains generalist language ...
- Our evaluations show that PaLM-E, a single large embodied multimodal model, can address a variety of embodied reasoning tasks, from a variety of observation modalities, on multiple embodiments, ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Further, in our experiments we show that current state-of-the-art visuallanguage models trained on typic
- However, a limitation of such models for inference in the real world is the issue of grounding: while training LLMs on massive textual data may lead to representations ...
- Our evaluations show that PaLM-E, a single large embodied multimodal model, can address a variety of embodied reasoning tasks, from a variety of observation modalities, on multiple embodiments, ...

## Abstract Cue
- Large language models have been demonstrated to perform complex tasks.
