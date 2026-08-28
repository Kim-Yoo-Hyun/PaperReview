# Eureka: Human-Level Reward Design via Coding Large Language Models

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / ICLR
- Category: Robot Learning and Data
- Tags: Robotics, Reinforcement Learning, Reward Design, Large Language Model, NVIDIA
- Official paper: https://openreview.net/forum?id=IEduRUO55F
- Code/Project: https://eureka-research.github.io/
- Source audit: official OpenReview abstract and project page checked; task-level results remain UNVERIFIED.

## Why This Paper Is Here

LLM이 executable reward code를 생성·개선해 robot RL의 reward engineering을 자동화한 NVIDIA의 대표 foundation-model-for-control paper다.

## Problem

복잡한 robot skill의 dense reward를 사람이 반복 설계하는 비용과 전문성 병목을 줄인다.

## Core Idea

LLM code generation, simulator feedback와 evolutionary refinement를 반복해 reward functions를 탐색한다.

## Interface

task description와 environment source/context를 executable reward code로 바꾸고 RL training 결과를 feedback한다.

## Evaluation Scope

Isaac Gym의 다수 tasks와 dexterous manipulation에서 human-designed rewards와 비교한다.
