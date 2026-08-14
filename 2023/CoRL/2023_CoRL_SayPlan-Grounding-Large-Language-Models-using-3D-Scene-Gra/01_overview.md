# SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning

- Year/Venue: 2023 / CoRL
- Category: Planning and Long-Horizon Reasoning
- Tags: Robotics, 3D Vision, LLM planning, 3D Scene Graph, replanning, mobile manipulation
- Paper link: [paper.pdf](./paper.pdf)
- Code/Project: https://sayplan.github.io/
- Source audit: regenerated from local `paper.pdf` on 2026-08-11; survey-keyword template text removed.

## Problem
- The associated challenges permeate every aspect of robotics, encompassing navigation, perception, manipulation as well as high-level task planning.
- The challenge lies in scaling these models.
- However, these efforts are primarily confined to small-scale environments, typically single rooms with pre-encoded information on all the existing assets and objects present.

## Core Idea
- We present a scalable framework for grounding the generalist task planning capabilities of pretrained LLMs in large-scale environments spanning multiple floors and rooms using 3DSG representations.
- We introduce SayPlan, a scalable approach to LLM-based, large-scale task planning for robotics using 3D scene graph (3DSG) representations.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- : Large language models (LLMs) have demonstrated impressive results in developing generalist planning agents for diverse tasks.
- SayPlan (GPT-4) in contrast achieved 86.7% and 73.3% success in identifying the desired subgraph across both the simple and complex search tasks respectively, demonstrating significantly better graph-based reasoning ...
- We evaluate our approach on two large-scale environments spanning up to 3 floors and 36 rooms with 140 assets and objects and show that our approach is capable ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We evaluate our approach on two large-scale environments spanning up to 3 floors and 36 rooms with 140 assets and objects and show that our approach is capable ...
- To ensure the scalability of our approach, we: (1) exploit the hierarchical nature of 3DSGs to allow LLMs to conduct a semantic search for task-relevant subgraphs from a ...
- : Large language models (LLMs) have demonstrated impressive results in developing generalist planning agents for diverse tasks.

## Abstract Cue
- : Large language models (LLMs) have demonstrated impressive results in developing generalist planning agents for diverse tasks.
