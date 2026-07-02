# Method

- Year/Venue: 2024 / ECCV
- Category: 3D Scene Graphs and Graph Reasoning
- Tags: 3D Vision, Graph Reasoning
- Paper link: ./2024/ECCV/2024_ECCV_Heterogeneous-Graph-Learning-for-Scene-Graph-Prediction-in/paper.pdf
- Code/Project: not identified
- Source audit: regenerated from local `paper.pdf` on 2026-07-02; survey-keyword template text removed.

## Brief Method
- Specifically, our method consists of two stages: a heterogeneous graph structure learning (HGSL) stage and a heterogeneous graph reasoning (HGR) stage.
- We propose a novel framework named 3D Heterogeneous Scene Graph Prediction (3D-HetSGP).
- In this paper, we propose a 3D Heterogeneous Scene Graph Prediction (3D-HetSGP) framework, which performs graph reasoning on the 3D scene graph in a heterogeneous fashion.

## 원리적 동기
- Although remarkable progress has been made in recent years, 3D SGP remains highly challenging as 1) 3D point cloud data is typically sparse and irregular in spatial dimension.
- Extensive experiments show that our method achieves comparable or superior performance to existing methods on 3DSSG dataset.
- Specifically, our method consists of two stages: a heterogeneous graph structure learning (HGSL) stage and a heterogeneous graph reasoning (HGR) stage.

## 핵심 방법론
- We propose a novel framework named 3D Heterogeneous Scene Graph Prediction (3D-HetSGP).
- The training objective for mapping a 3D scene from point clouds to a scene graph is to maximize the joint probability: \label {joint_P} P(\mathcal {G}, \mathcal {T}|D)= P(\mathcal ...
- We use a directed heterogeneous graph G = (V, E, TE ) to represent our 3D scene graph, where the nodes V consist of the objects O, the ...
- Our framework consists of two stages.
