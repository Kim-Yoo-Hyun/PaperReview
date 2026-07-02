# Problem

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Equivariance and Geometry
- Tags: equivariant, 3D geometry, Transformer
- Paper link: ./2020/NeurIPS/2020_NeurIPS_SE3-Transformers-3D-Roto-Translation-Equivariant-Attention/paper.pdf
- Code/Project: https://github.com/FabianFuchsML/se3-transformer-public
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## 왜 문제인가
- In this paper, we find that the explicit imposition of equivariance constraints on the self-attention mechanism addresses these challenges.
- Their relative implementational simplicity coupled with high efficacy on a wide range of tasks such as language modeling , image recognition , or graph-based problems , make them ...
- However, their generality of application means that for specific tasks, knowledge of existing underlying structure is unused.

## 해결하려는 문제
- We introduce the SE(3)-Transformer, a variant of the self-attention module for 3D point clouds and graphs, which is equivariant under continuous 3D rototranslations.
- The SE(3)Transformer leverages the benefits of self-attention to operate on large point clouds and graphs with varying number of points, while guaranteeing SE(3)-equivariance for robustness.
- In all cases, our model outperforms a strong, non-equivariant attention baseline and an equivariant model without attention.

## 선행 연구 / 배경 단서
- In this paper, we find that the explicit imposition of equivariance constraints on the self-attention mechanism addresses these challenges.
- Their relative implementational simplicity coupled with high efficacy on a wide range of tasks such as language modeling , image recognition , or graph-based problems , make them ...
- However, their generality of application means that for specific tasks, knowledge of existing underlying structure is unused.
