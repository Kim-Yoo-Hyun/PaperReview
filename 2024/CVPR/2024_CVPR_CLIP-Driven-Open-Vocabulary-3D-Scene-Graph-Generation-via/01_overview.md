# CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Scene Graph, CLIP, Graph Reasoning
- Authors: Lianggangxu Chen, Xuejiao Wang, Jiale Lu, Shaohui Lin, Changbo Wang, Gaoqi He ; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024, pp. 27863-27873
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Chen_CLIP-Driven_Open-Vocabulary_3D_Scene_Graph_Generation_via_Cross-Modality_Contrastive_Learning_CVPR_2024_paper.html
- PDF status: downloaded
- GitHub/Project: not identified from primary page

## Problem
3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다.

## Core Idea
핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다.

## Paper-Specific Cues
- Topic cue: 3D Scene Graph Generation (3DSGG) aims to classify objects and their predicates within 3D point cloud scenes.
- Method cue: Specifically we propose a novel Cross-Modality Contrastive Learning 3DSGG (CCL-3DSGG) method.
- Result cue: Lastly the recognition of novel object and predicate classes is achieved by calculating the cosine similarity between prompts and 3DSG features.

## Input / Output
Input/Output follows the paper task formulation; see PDF for the exact interface.

## Main Claims
- 논문은 `structured 3D scene graph reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- structured 3D scene graph reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D Scene Graph, CLIP, Graph Reasoning.
- 초록에서 확인되는 주요 cue: Scene, Graph, Generation, However, The, Closed-set, Addressing, CLIP.
