# SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Vision, Graph Reasoning
- Authors: Yang Miao, Francis Engelmann, Olga Vysotska, Federico Tombari, Marc Pollefeys, Daniel Barath*
- Paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1255_ECCV_2024_paper.php
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다.

## Core Idea
핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다.

## Paper-Specific Cues
- Topic cue: "We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
- Method cue: "We introduce the task of localizing an input image within a multi-modal reference map represented by a collection of 3D scene graphs.
- Result cue: This strategy significantly outperforms other cross-modal methods, even without incorporating images into the map representation.

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `structured 3D scene graph reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- structured 3D scene graph reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Vision, Graph Reasoning.
- 초록에서 확인되는 주요 cue: These, Given, This, With, Code.
