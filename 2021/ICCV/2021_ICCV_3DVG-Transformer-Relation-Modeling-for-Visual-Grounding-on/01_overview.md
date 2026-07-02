# 3DVG-Transformer: Relation Modeling for Visual Grounding on Point Clouds

- Year/Venue: 2021 / ICCV
- Category: 3D Vision-Language Grounding
- Tags: 3D visual grounding, graph reasoning, Transformer
- Paper link: ./2021/ICCV/2021_ICCV_3DVG-Transformer-Relation-Modeling-for-Visual-Grounding-on/paper.pdf
- Code/Project: https://github.com/zlccccc/3DVG-Transformer
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- By formulating this task as a grounding-by-detection problem, lots of recent works focus on how to exploit more powerful detectors and comprehensive language features, but (1) how to ...
- Recently, Chen et al. and Achlioptas et al. proposed to tackle visual grounding on 3D point clouds by formulating it as a grounding-by-detection problem, together with two newly ...

## Core Idea
- Inspired by the well-known transformer architecture, we propose a relation-aware visual grounding method on 3D point clouds, named as 3DVGTransformer, to fully utilize the contextual clues for relationenhanced ...
- Our framework consists of two newly designed transformer-like modules (i.e. the coordinate-guided contextual aggregation module and multiplex attention module) to exploit rich relations within point clouds.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We validate that our 3DVG-Transformer outperforms the state-of-the-art methods by a large margin, on two point cloud-based visual grounding datasets, ScanRefer and Nr3D/Sr3D from ReferIt3D, especially for complex ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Inspired by the well-known transformer architecture, we propose a relation-aware visual grounding method on 3D point clouds, named as 3DVGTransformer, to fully utilize the contextual clues for relationenhanced ...
- We validate that our 3DVG-Transformer outperforms the state-of-the-art methods by a large margin, on two point cloud-based visual grounding datasets, ScanRefer and Nr3D/Sr3D from ReferIt3D, especially for complex ...
- By formulating this task as a grounding-by-detection problem, lots of recent works focus on how to exploit more powerful detectors and comprehensive language features, but (1) how to ...

## Abstract Cue
- relations in complex 3D scenes and distinguish the proposals of the target object from other similar proposals.
