# Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning

- Year/Venue: 2026 / ICRA
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: Robotics, Graph Reasoning, semantic
- Authors: Yi Wang, Zeyu Xue, Mujie Liu, Tongqin Zhang, Yan Hu, Zhou Zhao
- Paper: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html
- PDF status: downloaded
- GitHub/Project: not identified from venue audit

## Problem
3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다.

## Core Idea
핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다.

## Paper-Specific Cues
- Topic cue: Teleoperation via natural-language reduces operator workload and enhances safety in high-risk or remote settings.
- Method cue: To mitigate this, we introduce the Spatio-Temporal Open-Vocabulary Scene Graph (ST-OVSG), a representation that enriches open-vocabulary perception with temporal dynamics and lightweight latency annotations.
- Result cue: Experiments show that our method achieves 74 percent node accuracy on the Replica benchmark, outperforming ConceptGraph.

## Input / Output
Input: language instruction plus RGB/RGB-D/point-cloud robot observations. Output: action tokens, poses, trajectories, constraints, or policy decisions.

## Main Claims
- 논문은 `structured 3D scene graph reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- structured 3D scene graph reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Robotics, Graph Reasoning, semantic.
- 초록에서 확인되는 주요 cue: Teleoperation, However, Spatio-Temporal, Open-Vocabulary, Scene, Graph, ST-OVSG, LVLMs.
