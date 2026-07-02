# VoxFormer: Sparse Voxel Transformer for Camera-based 3D Semantic Scene Completion

- Year/Venue: 2023 / CVPR
- Category: Foundations: 3D Semantic Occupancy
- Tags: semantic, alignment, 3D Vision
- Paper link: ./2023/CVPR/2023_CVPR_VoxFormer-Sparse-Voxel-Transformer-for-Camera-based-3D-Sem/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- However, obtaining accurate and complete 3D information of the real world is difficult, since the task is challenged by the lack of sensing resolution and the incomplete observation ...
- Introduction Holistic 3D scene understanding is an important problem in autonomous vehicle (AV) perception.
- To tackle the challenges, semantic scene completion (SSC) was proposed to jointly infer the complete scene geometry and semantics from limited observations.

## Core Idea
- To enable such capability in AI systems, we propose VoxFormer, a Transformerbased semantic scene completion framework that can output complete 3D volumetric semantics from only 2D images.
- We use 8 sampling points around each reference point for the cross-/self-attention head.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- Experiments on SemanticKITTI show that VoxFormer outperforms the state of the art with a relative improvement of 20.0% in geometry and 18.1% in semantics and reduces GPU memory ...

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- Experiments on SemanticKITTI show that VoxFormer outperforms the state of the art with a relative improvement of 20.0% in geometry and 18.1% in semantics and reduces GPU memory ...
- To enable such capability in AI systems, we propose VoxFormer, a Transformerbased semantic scene completion framework that can output complete 3D volumetric semantics from only 2D images.
- An SSC solution has to simultaneously address two subtasks: scene reconstruction for visible areas and scene hallucination for Self-Attention Cross-Attention Output Input: 2D Images Query Proposals 3D Semantic ...

## Abstract Cue
- Humans can easily imagine the complete 3D geometry of occluded objects and scenes.
