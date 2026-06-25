# 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Scene Graph, LLM, Graph Reasoning
- Authors: Tatiana Zemskova, Dmitry Yudin ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 8885-8895
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zemskova_3DGraphLLM_Combining_Semantic_Graphs_and_Large_Language_Models_for_3D_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다.

## Core Idea
핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다.

## Paper-Specific Cues
- Topic cue: A 3D scene graph represents a compact scene model by capturing both the objects present and the semantic relationships between them, making it a ...
- Method cue: In this work, we propose 3DGraphLLM, a method for constructing a learnable representation of a 3D scene graph that explicitly incorporates semantic relationships.
- Result cue: Recent methods for learning scene representations have shown that adapting these representations to the 3D world can significantly improve the quality of LLM responses.

## Input / Output
Input: image/3D observations and natural language. Output: aligned representation, answer, reasoning trace, caption, or grounded decision.

## Main Claims
- 논문은 `structured 3D scene graph reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- structured 3D scene graph reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Scene Graph, LLM, Graph Reasoning.
- 초록에서 확인되는 주요 cue: Large, Language, Models, LLMs, Recent, LLM, However, This.
