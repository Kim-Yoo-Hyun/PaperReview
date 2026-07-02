# Method

- Year/Venue: 2020 / NeurIPS
- Category: Foundations: Equivariance and Geometry
- Tags: equivariant, 3D geometry, Transformer
- Paper link: ./2020/NeurIPS/2020_NeurIPS_SE3-Transformers-3D-Roto-Translation-Equivariant-Attention/paper.pdf
- Code/Project: https://github.com/FabianFuchsML/se3-transformer-public
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We introduce the SE(3)-Transformer, a variant of the self-attention module for 3D point clouds and graphs, which is equivariant under continuous 3D rototranslations.
- Here, we present the SE(3)-Transformer.
- 3.2 The SE(3)-Transformer The SE(3)-Transformer itself consists of three components.

## 원리적 동기
- In this paper, we find that the explicit imposition of equivariance constraints on the self-attention mechanism addresses these challenges.
- Their relative implementational simplicity coupled with high efficacy on a wide range of tasks such as language modeling , image recognition , or graph-based problems , make them ...
- We introduce the SE(3)-Transformer, a variant of the self-attention module for 3D point clouds and graphs, which is equivariant under continuous 3D rototranslations.

## 핵심 방법론
- Here, we present the SE(3)-Transformer.
- 3.2 The SE(3)-Transformer The SE(3)-Transformer itself consists of three components.
- These are 1) edge-wise attention weights αij , constructed to be SE(3)-invariant on each edge ij, 2) edge-wise SE(3)-equivariant value messages, propagating information between nodes, as found in ...
- Neighbourhoods reduce the computational complexity of the attention mechanism from quadratic in the number of points to linear.
- Attention is performed on a per-neighbourhood basis as follows: X X ` k f`out,i = W`` + αij W`k (10) V fin,i V (xj − xi )fin,j . ...
