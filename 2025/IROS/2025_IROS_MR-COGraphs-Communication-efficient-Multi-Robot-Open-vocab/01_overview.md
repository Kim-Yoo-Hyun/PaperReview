# MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs

- Year/Venue: 2025 / IROS
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: Robotics, 3D Vision, Graph Reasoning, semantic
- Authors: Qiuyi Gu, Zhaocheng Ye, Jincheng Yu, Jiahao Tang, Tinghao Yi, Yuhan Dong
- Paper: https://arxiv.org/abs/2412.18381
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다.

## Core Idea
핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다.

## Paper-Specific Cues
- Topic cue: Collaborative perception in unknown environments is crucial for multi-robot systems.
- Method cue: To address this challenge, we develop a method to construct a graph-structured 3D representation called COGraph, where nodes represent objects with semantic features and ...
- Result cue: With the emergence of foundation models, robots can now not only perceive geometric information but also achieve open-vocabulary scene understanding.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `structured 3D scene graph reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- structured 3D scene graph reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Robotics, 3D Vision, Graph Reasoning, semantic.
- 초록에서 확인되는 주요 cue: Collaborative, With, However, COGraph, Before, Upon, COGraphs, The.
