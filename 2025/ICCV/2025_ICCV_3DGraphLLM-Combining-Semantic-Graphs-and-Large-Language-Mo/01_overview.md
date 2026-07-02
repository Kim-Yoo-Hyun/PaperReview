# 3DGraphLLM: Combining Semantic Graphs and Large Language Models for 3D Scene Understanding

- Year/Venue: 2025 / ICCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Scene Graph, LLM, Graph Reasoning
- Paper link: ./2025/ICCV/2025_ICCV_3DGraphLLM-Combining-Semantic-Graphs-and-Large-Language-Mo/paper.pdf
- Code/Project: not identified from primary page
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, existing methods typically rely only on geometric information, such as object coordinates, and overlook the rich semantic relationships between objects.

## Core Idea
- In this work, we propose 3DGraphLLM, a method for constructing a learnable representation of a 3D scene graph that explicitly incorporates semantic relationships.
- For the visual grounding task on the ScanRefer dataset, we use the standard metrics Acc@0.25 and Acc@0.5.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In our experiments on popular ScanRefer, Multi3DRefer, ScanQA, Sqa3D, and Scan2cap datasets, we demonstrate that our approach outperforms baselines that do not leverage semantic relationships between objects.
- Recent methods for learning scene representations have shown that adapting these representations to the 3D world can significantly improve the quality of LLM responses.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- In our experiments on popular ScanRefer, Multi3DRefer, ScanQA, Sqa3D, and Scan2cap datasets, we demonstrate that our approach outperforms baselines that do not leverage semantic relationships between objects.
- In this work, we propose 3DGraphLLM, a method for constructing a learnable representation of a 3D scene graph that explicitly incorporates semantic relationships.
- Recent methods for learning scene representations have shown that adapting these representations to the 3D world can significantly improve the quality of LLM responses.

## Abstract Cue
- OBJ1 lef t OBJ1 t ht OBJ4 d behin rig A 3D scene graph represents a compact scene model by capturing both the objects present and the semantic relationships between them, making it a promising structure for robotic applications.
