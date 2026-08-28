# AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents

> Evidence maturity: `ABSTRACT_CHECKED`. 이 문서는 정독 완료를 뜻하지 않는다.

- Year/Venue: 2024 / arXiv
- Category: Robot Learning and Data
- Tags: Robotics, robot data, Foundation Models, Fleet Learning, Google DeepMind
- Official paper: https://deepmind.google/research/publications/48151/
- Code/Project: not identified
- Source audit: official DeepMind publication page and abstract checked; deployment statistics remain UNVERIFIED.

## Why This Paper Is Here

foundation model을 robot fleet의 task proposal·safety filtering·data collection orchestration에 사용한 Google lineage의 중요한 data-engine paper다.

## Problem

다양한 실제 환경에서 여러 로봇이 유용하고 안전한 embodied data를 자율적으로 대규모 수집하게 한다.

## Core Idea

VLM/LLM 기반 scene understanding과 task generation을 robot policy 및 safety checks와 결합한다.

## Interface

scene observations를 candidate language tasks, safety decision과 robot-policy invocation으로 연결한다.

## Evaluation Scope

multi-robot real-world deployment와 collected episodes/tasks를 보고하며 정확한 규모·failure 분류는 정독 후 기록한다.
