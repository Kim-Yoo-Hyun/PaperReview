# Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation

- Year/Venue: 2026 / ICML
- Category: Navigation and Embodied AI
- Tags: Navigation, Reinforcement Learning
- Paper link: ./2026/ICML/2026_ICML_Plan-in-Sandbox-Navigate-in-Open-Worlds-Learning-Physics-G/paper.pdf
- Code/Project: not identified from OpenReview
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- Although the research community has turned to Reinforcement Learning (RL) to facilitate policy adaptation (Zeng et al., 2024; Choi et al., 2024; Wang & Huang, 2025) from highlevel ...
- Problem Formulation We formulate the learning problem via three core components: (1) a physics-grounded semantic sandbox S, which provides an environment ES ; (2) an unknown target task ...
- Navigation Task We formulate the navigation task N as a Goal-Conditioned Reinforcement Learning (GCRL) (Liu et al., 2022) problem.

## Core Idea
- These sub-goals are subsequently executed by • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. ...
- To this end, we propose Sandbox-Abstracted Grounded Experience (SAGE), a framework that enables agents to learn within a physics-grounded semantic abstraction rather than a photorealistic simulation, mimicking the ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We demonstrate that SAGE significantly improves planner-assisted embodied navigation, achieving a 53.21% LLM-Match Success Rate on A-EQA (+9.7% over baseline), while showing encouraging transfer to physical indoor robot ...
- SAGE demonstrates superior performance, significantly outperforming traditional RL baselines by a large margin.
- Extensive experiments demonstrate that SAGE delivers strong performance across simulated embodied navigation benchmarks and provides encouraging evidence of transfer to physical indoor robot deployment.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- These sub-goals are subsequently executed by • We introduce a novel Generative Experience-Driven Learning paradigm to address the severe data scarcity and real-world transfer challenges in embodied navigation. ...
- Optimized Policy Observations Task Egocentric Views Visual Buffers 1 Frontier 1 Real-World Env Frontier Memory Node Node EVOLUTION black NAVIGATION Open-world Sandbox (a) SAGE Agent (c) GOAT-Bench Performance ...
- We demonstrate that SAGE significantly improves planner-assisted embodied navigation, achieving a 53.21% LLM-Match Success Rate on A-EQA (+9.7% over baseline), while showing encouraging transfer to physical indoor robot ...

## Abstract Cue
- Introduction Recent rapid advancements in Vision-Language Models (VLMs) (Achiam et al., 2023; Liu et al., 2023; Yang et al., 2025a) have empowered agent systems with unprecedented capabilities in open-world perception, semantic reasoning, and zero-shot generalization.
