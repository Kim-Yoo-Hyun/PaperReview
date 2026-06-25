# Vision-Language Interactive Relation Mining for Open-Vocabulary Scene Graph Generation

- Year/Venue: 2025 / ICCV 2025
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: Vision-Language Model, Graph Reasoning, semantic
- Authors: Yukuan Min, Muli Yang, Jinhao Zhang, Yuxuan Wang, Aming Wu, Cheng Deng ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2025, pp. 16755-16764
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Min_Vision-Language_Interactive_Relation_Mining_for_Open-Vocabulary_Scene_Graph_Generation_ICCV_2025_paper.html
- PDF status: downloaded
- GitHub/Project: not identified

## Problem
3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다.

## Core Idea
핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다.

## Paper-Specific Cues
- Topic cue: To promote the deployment of scenario understanding in the real world, Open-Vocabulary Scene Graph Generation (OV-SGG) has attracted much attention recently, aiming to generalize ...
- Method cue: To this end, we propose a novel Vision-Language Interactive Relation Mining model (VL-IRM) for OV-SGG, which explores learning generalized relation-aware knowledge through multi-modal interaction.
- Result cue: Extensive experiments demonstrate the superior OV-SGG performance of our method.

## Input / Output
Input: image/3D observations and natural language. Output: aligned representation, answer, reasoning trace, caption, or grounded decision.

## Main Claims
- 논문은 `structured 3D scene graph reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- structured 3D scene graph reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: Vision-Language Model, Graph Reasoning, semantic.
- 초록에서 확인되는 주요 cue: Open-Vocabulary, Scene, Graph, Generation, OV-SGG, Towards, VLMs, However.
