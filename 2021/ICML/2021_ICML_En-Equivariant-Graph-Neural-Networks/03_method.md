# Method

- Year/Venue: 2021 / ICML
- Category: Foundations: Equivariance and Geometry
- Tags: equivariant, graph reasoning, 3D geometry
- Paper link: ./2021/ICML/2021_ICML_En-Equivariant-Graph-Neural-Networks/paper.pdf
- Code/Project: https://github.com/vgsatorras/egnn
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- We will explain how Graph Autoencoders can benefit from equivariance and we will show how our method outperforms standard GNN autoencoders in the provided datasets.
- We demonstrate the effectiveness of our method on dynamical systems modelling, representation learning in graph autoencoders and predicting molecular properties.
- In this experiment section we use our EGNN to build an Equivariant Graph Autoencoder.

## 원리적 동기
- An effective method to restrict neural networks to relevant functions is to exploit the symmetry of problems by enforcing equivariance with respect to transformations from a certain symmetry ...
- Many problems exhibit 3D translation and rotation symmetries.
- We will explain how Graph Autoencoders can benefit from equivariance and we will show how our method outperforms standard GNN autoencoders in the provided datasets.

## 핵심 방법론
- We will explain how Graph Autoencoders can benefit from equivariance and we will show how our method outperforms standard GNN autoencoders in the provided datasets.
- In this experiment section we use our EGNN to build an Equivariant Graph Autoencoder.
- We use n = 8 dimensions for the embedding space.
- We sampled 5.000 graphs for training, 500 for validation and 500 for test for both datasets.
- In the following, we report on a similar experiment as above, but instead of using 3.000 training samples we generated a new training partition of E(n) Equivariant Graph ...
