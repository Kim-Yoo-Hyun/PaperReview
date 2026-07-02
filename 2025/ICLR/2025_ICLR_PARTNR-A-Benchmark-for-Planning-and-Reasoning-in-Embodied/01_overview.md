# PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks

- Year/Venue: 2025 / ICLR Poster
- Category: Benchmarks and Datasets
- Tags: Robotics, Benchmark
- Paper link: ./2025/ICLR/2025_ICLR_PARTNR-A-Benchmark-for-Planning-and-Reasoning-in-Embodied/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- housenode denoting the environment where tasks are taking place.
- Apart from the semantic information, each node also stores the 3D location of the entity and its affordance states e.g., clean/dirty, on/off, open/close, etc.
- The graph can then be serialized or accessed via specialized tools by ReAct policies.

## Core Idea
- 4.3 H UMAN - IN - THE - LOOP E VALUATION We build on the human-in-the-loop infrastructure from Habitat 3.0 (Puig et al., 2024) and adapt it to ...
- This indicates that the finetuning effectively distills task-relevant information from the training set and generalizes to new test tasks.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In contrast, human pairs outperform single humans, in our human-in-the-loop experiments, highlighting potential for improving LLM collaboration strategies.
- As PARTNR consists of natural language tasks and LLMs have shown strong results in planning (Yao et al., 2023; Ahn et al., 2022; Huang et al., 2022), we ...
- When comparing model sizes, we observe that a smaller fine-tuned Llama3.18B achieves a similar performance to a Llama3.1-70B without finetuning, while being 8.6X faster.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- housenode denoting the environment where tasks are taking place.
- Apart from the semantic information, each node also stores the 3D location of the entity and its affordance states e.g., clean/dirty, on/off, open/close, etc.
- The graph can then be serialized or accessed via specialized tools by ReAct policies.

## Abstract Cue
- housenode denoting the environment where tasks are taking place.
