# RoboDreamer: Learning Compositional World Models for Robot Imagination

- Year/Venue: 2024 / ICML
- Category: World Models, Safety, and Recovery
- Tags: Robotics, world model, video prediction, language planning, compositional generalization
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://robodreamer.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- When existing text-to-video models (AVDC (Ko et al., 2023)) are given unusual combinations of language instructions, they are unable to synthesize videos that align accurately with these descriptions.

## Core Idea
- To resolve this issue, we introduce RoboDreamer, an innovative approach for learning a compositional world model by factorizing the video generation.
- However, one major issue in such models is generalization – models are limited to synthesizing videos subject to language instructions similar to those seen at training time.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Our approach can successfully synthesize video plans on unseen goals in the RT-X, enables successful robot execution in simulation, and substantially outperforms monolithic baseline approaches to video generation.
- We further show how such a factorization enables us to add additional multimodal goals, allowing us to specify a video we wish to generate given both natural language ...
- Text-to-video models have demonstrated substantial potential in robotic decision-making, enabling the imagination of realistic plans of future actions as well as accurate environment simulation.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Our approach can successfully synthesize video plans on unseen goals in the RT-X, enables successful robot execution in simulation, and substantially outperforms monolithic baseline approaches to video generation.
- To resolve this issue, we introduce RoboDreamer, an innovative approach for learning a compositional world model by factorizing the video generation.
- However, one major issue in such models is generalization – models are limited to synthesizing videos subject to language instructions similar to those seen at training time.

## Abstract Cue
- Text-to-video models have demonstrated substantial potential in robotic decision-making, enabling the imagination of realistic plans of future actions as well as accurate environment simulation.
