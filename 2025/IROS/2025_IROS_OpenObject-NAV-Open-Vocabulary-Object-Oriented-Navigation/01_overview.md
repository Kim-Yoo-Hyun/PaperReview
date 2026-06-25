# OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph

- Year/Venue: 2025 / IROS
- Category: Navigation and Embodied AI
- Tags: Navigation, Graph Reasoning, semantic
- Authors: Yujie Tang, Meiling Wang, Yinan Deng, Zibo Zheng, Jiagui Zhong, Yufeng Yue
- Paper: https://arxiv.org/abs/2409.18743
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다.

## Core Idea
핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다.

## Paper-Specific Cues
- Topic cue: In everyday life, frequently used objects like cups often have unfixed positions and multiple instances within the same category, and their carriers frequently change ...
- Method cue: We designed a series of long-sequence navigation tasks for frequently used everyday items in the Habitat simulator.
- Result cue: The results demonstrate that by updating the CRSG, the robot can efficiently navigate to moved targets.

## Input / Output
Input: language/navigation goal plus egocentric observations or 3D maps. Output: waypoint, action, route, or grounded target decision.

## Main Claims
- 논문은 `structured 3D scene graph reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- structured 3D scene graph reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Navigation, Graph Reasoning, semantic.
- 초록에서 확인되는 주요 cue: However, This, Carrier-Relationship, Scene, Graph, CRSG, Based, Markov.
