# SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation

- Year/Venue: 2026 / IROS
- Category: Navigation and Embodied AI
- Tags: Navigation, Graph Reasoning
- Authors: Hao Su, Yuehao Huang, Yukai Ma, Yong Liu, Jiajun Lv
- Paper: https://arxiv.org/abs/2606.25497
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다.

## Core Idea
핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다.

## Paper-Specific Cues
- Topic cue: Object-Goal Navigation (ObjNav) requires embodied agents to autonomously locate specified targets using only egocentric visual observations.
- Method cue: To address these limitations, we propose SAGE-Nav, a novel hierarchical framework that integrates the reasoning capabilities of Large Language Models (LLMs) with dynamic scene ...
- Result cue: Extensive evaluations in the i-THOR and RoboTHOR environments demonstrate that SAGE-Nav achieves state-of-the-art performance, delivering substantial gains in navigation efficiency and zero-shot generalization while ...

## Input / Output
Input: language/navigation goal plus egocentric observations or 3D maps. Output: waypoint, action, route, or grounded target decision.

## Main Claims
- 논문은 `structured 3D scene graph reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- structured 3D scene graph reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Navigation, Graph Reasoning.
- 초록에서 확인되는 주요 cue: Object-Goal, Navigation, ObjNav, Existing, SAGE-Nav, Large, Language, Models.
