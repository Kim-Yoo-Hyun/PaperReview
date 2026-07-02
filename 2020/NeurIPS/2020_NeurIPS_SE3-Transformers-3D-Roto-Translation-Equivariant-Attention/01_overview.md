# SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Equivariance and Geometry
- Tags: equivariant, 3D geometry, Transformer
- Paper link: ./2020/NeurIPS/2020_NeurIPS_SE3-Transformers-3D-Roto-Translation-Equivariant-Attention/paper.pdf
- Code/Project: https://github.com/FabianFuchsML/se3-transformer-public
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- In this paper, we find that the explicit imposition of equivariance constraints on the self-attention mechanism addresses these challenges.
- Their relative implementational simplicity coupled with high efficacy on a wide range of tasks such as language modeling , image recognition , or graph-based problems , make them ...
- However, their generality of application means that for specific tasks, knowledge of existing underlying structure is unused.

## Core Idea
- We introduce the SE(3)-Transformer, a variant of the self-attention module for 3D point clouds and graphs, which is equivariant under continuous 3D rototranslations.
- Here, we present the SE(3)-Transformer.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- We compare to publicly available, state-of-the-art results as well as a set of our own baselines.
- We further achieve competitive performance on two real-world datasets, ScanObjectNN and QM9.
- In all cases, our model outperforms a strong, non-equivariant attention baseline and an equivariant model without attention.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We introduce the SE(3)-Transformer, a variant of the self-attention module for 3D point clouds and graphs, which is equivariant under continuous 3D rototranslations.
- The SE(3)Transformer leverages the benefits of self-attention to operate on large point clouds and graphs with varying number of points, while guaranteeing SE(3)-equivariance for robustness.
- In all cases, our model outperforms a strong, non-equivariant attention baseline and an equivariant model without attention.

## Abstract Cue
- We introduce the SE(3)-Transformer, a variant of the self-attention module for 3D point clouds and graphs, which is equivariant under continuous 3D rototranslations.
