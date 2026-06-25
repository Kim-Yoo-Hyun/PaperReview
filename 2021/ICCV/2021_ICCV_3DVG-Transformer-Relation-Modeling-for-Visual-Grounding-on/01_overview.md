# 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds

- Year/Venue: 2021 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D visual grounding, graph reasoning, Transformer
- Authors: Lichen Zhao, Daigang Cai, Lu Sheng, Dong Xu ; Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2021, pp. 2928-2937
- Paper: https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_3DVG-Transformer_Relation_Modeling_for_Visual_Grounding_on_Point_Clouds_ICCV_2021_paper.html
- PDF status: downloaded
- GitHub/Project: https://github.com/zlccccc/3DVG-Transformer

## Problem
3D scene graph는 객체와 관계를 구조화하지만 closed vocabulary, annotation cost, geometric relation ambiguity 때문에 실제 로봇 질의에 확장하기 어렵다.

## Core Idea
핵심은 객체 노드와 관계 엣지를 3D geometry 및 language embedding과 정렬해 queryable relation reasoning을 가능하게 하는 것이다.

## Paper-Specific Cues
- Topic cue: Visual grounding on 3D point clouds is an emerging vision and language task that benefits various applications in understanding the 3D visual world.
- Method cue: Inspired by the well-known transformer architecture, we propose a relation-aware visual grounding method on 3D point clouds, named as 3DVG-Transformer, to fully utilize the ...
- Result cue: We validate that our 3DVG-Transformer outperforms the state-of-the-art methods by a large margin, on two point cloud-based visual grounding datasets, ScanRefer and Nr3D/Sr3D from ...

## Input / Output
Input: 3D scene representation plus free-form natural language. Output: target object, 3D box, mask, or referring expression result.

## Main Claims
- 논문은 `structured 3D scene graph reasoning`에서 기존 방법의 일반화, 정렬, 효율, 또는 3D grounding 한계를 줄이는 것을 주장한다.
- 평가가 확인된 경우, 아래 evaluation note의 datasets/metrics를 기준으로 비교한다.

## Limitation
2D foundation model에서 온 semantic feature가 3D geometry와 완벽히 정렬되지 않으며, long-tail 관계/속성 평가는 여전히 어렵다.

## Contribution
- structured 3D scene graph reasoning 문제를 명확한 시스템/모델/벤치마크 형태로 정의.
- 핵심 키워드: 3D visual grounding, graph reasoning, Transformer.
- 초록에서 확인되는 주요 cue: Visual, Inspired, Transformer, CCA, ScanRefer, Nr3D, Sr3D, ReferIt3D.
