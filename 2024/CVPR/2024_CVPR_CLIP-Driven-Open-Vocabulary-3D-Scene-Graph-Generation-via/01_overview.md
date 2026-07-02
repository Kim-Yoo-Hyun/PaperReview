# CLIP-Driven Open-Vocabulary 3D Scene Graph Generation via Cross-Modality Contrastive Learning

- Year/Venue: 2024 / CVPR
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Scene Graph, CLIP, Graph Reasoning
- Paper link: ./2024/CVPR/2024_CVPR_CLIP-Driven-Open-Vocabulary-3D-Scene-Graph-Generation-via/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, current 3DSGG methods struggle with two main challenges.
- Despite notable advancements in 3DSGG, existing stateof-the-art (SOTA) methods still encounter two obstacles that constrain their practicality in the open-vocabulary (OV) s

## Core Idea
- Specifically, we propose a novel Cross-Modality Contrastive Learning 3DSGG (CCL-3DSGG) method.
- Our method surpasses the competing models in both tasks, registering an average Recall of 60.1 and a Mean Recall of 51.3.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Lastly, the recognition of novel object and predicate classes is achieved by calculating the cosine similarity between prompts and 3DSG features.
- Our rigorous experiments confirm the superior open-vocabulary capability and applicability of CCL-3DSGG in real-world contexts.
- Existing 3DSGG models are mainly working in two directions to improve the accuracy.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Specifically, we propose a novel Cross-Modality Contrastive Learning 3DSGG (CCL-3DSGG) method.
- Existing 3DSGG models are mainly working in two directions to improve the accuracy.
- 2) Closed-set classes training hampers the recognition of novel objects and predicates.

## Abstract Cue
- 3D Scene Graph Generation (3DSGG) aims to classify objects and their predicates within 3D point cloud scenes.
