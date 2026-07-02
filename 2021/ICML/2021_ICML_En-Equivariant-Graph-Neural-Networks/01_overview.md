# E(n) Equivariant Graph Neural Networks

- Year/Venue: 2021 / ICML
- Category: Foundations: Equivariance and Geometry
- Tags: equivariant, graph reasoning, 3D geometry
- Paper link: ./2021/ICML/2021_ICML_En-Equivariant-Graph-Neural-Networks/paper.pdf
- Code/Project: https://github.com/vgsatorras/egnn
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Problem
- An effective method to restrict neural networks to relevant functions is to exploit the symmetry of problems by enforcing equivariance with respect to transformations from a certain symmetry ...
- Many problems exhibit 3D translation and rotation symmetries.
- In addition, whereas existing methods are limited to equivariance on 3 dimensional spaces, our model is easily scaled to higher-dimensional spaces.

## Core Idea
- We will explain how Graph Autoencoders can benefit from equivariance and we will show how our method outperforms standard GNN autoencoders in the provided datasets.
- We demonstrate the effectiveness of our method on dynamical systems modelling, representation learning in graph autoencoders and predicting molecular properties.

## Input / Output
- 본문 기반 자동 추출에서는 입력/출력 schema를 확정하지 않는다. 위 method/evaluation 단서와 `paper.pdf`의 method section을 함께 확인해야 한다.

## Main Claims
- In contrast with existing methods, our work does not require computationally expensive higher-order representations in intermediate layers while it still achieves competitive or better performance.
- Example of rotation equivariance on a graph with a graph neural network φ Recently, various forms and methods to achieve E(3) or SE(3) equivariance have been proposed (Thomas ...
- Many of these works achieve innovations in studying types of higher-order representations for intermediate network layers.

## Limitation
- 자동 추출 실패. `paper.pdf` 본문 수동 확인 필요.

## Contribution
- We demonstrate the effectiveness of our method on dynamical systems modelling, representation learning in graph autoencoders and predicting molecular properties.
- In contrast with existing methods, our work does not require computationally expensive higher-order representations in intermediate layers while it still achieves competitive or better performance.
- Example of rotation equivariance on a graph with a graph neural network φ Recently, various forms and methods to achieve E(3) or SE(3) equivariance have been proposed (Thomas ...

## Abstract Cue
- This paper introduces a new model to learn graph neural networks equivariant to rotations, translations, reflections and permutations called E(n)Equivariant Graph Neural Networks (EGNNs).
