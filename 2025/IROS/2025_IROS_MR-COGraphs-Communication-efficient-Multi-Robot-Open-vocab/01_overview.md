# MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs

- Year/Venue: 2025 / IROS
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: Robotics, 3D Vision, Graph Reasoning, semantic
- Paper link: ./2025/IROS/2025_IROS_MR-COGraphs-Communication-efficient-Multi-Robot-Open-vocab/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing map representations that support open-vocabulary queries often involve large data volumes, which becomes a bottleneck for multi-robot transmission in communication-limited environments.
- To address this challenge, we develop a method to construct a graph-structured 3D representation called COGraph, where nodes represent objects with semantic features and edges capture their spatial ...

## Core Idea
- To facilitate mapping and query evaluation, we develop a ROS wrapper 1 to extract RGB-D sequences and ground-truth poses from the dataset, transforming them into ROS bag files ...
- To address this challenge, we develop a method to construct a graph-structured 3D representation called COGraph, where nodes represent objects with semantic features and edges capture their spatial ...

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- The results demonstrate that, compared to existing baselines for open-vocabulary map construction, our framework reduces the data volume by over 80% while maintaining mapping and query performance without ...
- With the emergence of foundation models, robots can now not only perceive geometric information but also achieve open-vocabulary scene understanding.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- The results demonstrate that, compared to existing baselines for open-vocabulary map construction, our framework reduces the data volume by over 80% while maintaining mapping and query performance without ...
- To address this challenge, we develop a method to construct a graph-structured 3D representation called COGraph, where nodes represent objects with semantic features and edges capture their spatial ...
- Before transmission, a data-driven feature encoder is applied to compress the feature dimensions of the COGraph.

## Abstract Cue
- — Collaborative perception in unknown environments is crucial for multi-robot systems.
