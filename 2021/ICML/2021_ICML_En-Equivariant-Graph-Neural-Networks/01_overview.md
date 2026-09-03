# E(n) Equivariant Graph Neural Networks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2102.09844.
> PDF retrieval source: https://arxiv.org/pdf/2102.09844. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: equivariant, Graph Reasoning, 3D geometry
- Official paper: https://arxiv.org/abs/2102.09844
- Full-text retrieval: https://arxiv.org/pdf/2102.09844
- Code/Project: https://github.com/vgsatorras/egnn
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Many problems exhibit 3D translation and rotation symmetries.를 문제로 두고, In this section we introduce the relevant materials on equivariance and graph neural networks which will later complement the definition of our method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This paper introduces a new model to learn graph neural networks equivariant to rotations, translations, reflections and permutations called E(n)- Equivariant Graph Neural Networks (EGNNs).
- **p. 1 / Abstract - extractive body cue:** In contrast with existing methods, our work does not require computationally expensive higher-order representations in intermediate layers while it still achieves competitive or better performance.
- **p. 1 / Abstract - extractive body cue:** In addition, whereas existing methods are limited to equivariance on 3 dimensional spaces, our model is easily scaled to higher-dimensional spaces.
- **p. 1 / Abstract - extractive body cue:** We demonstrate the effectiveness of our method on dynamical systems modelling, representation learning in graph autoencoders and predicting molecular properties.
- **p. 1 / 1. Introduction - extractive body cue:** Although deep learning has largely replaced hand-crafted features, many advances are critically dependent on inductive biases in deep neural networks.
- **p. 1 / 1. Introduction - extractive body cue:** Many problems exhibit 3D translation and rotation symmetries.
- **p. 1 / 1. Introduction - extractive body cue:** An effective method to restrict neural networks to relevant functions is to exploit the symmetry of problems by enforcing equivariance with respect to transformations from ...

## Core Idea

- **p. 2 / 2. Background - extractive body cue:** In this section we introduce the relevant materials on equivariance and graph neural networks which will later complement the definition of our method.
- **p. 1 / 1. Introduction - extractive body cue:** In this work we present a new architecture that is translation, rotation and reflection equivariant (E(n)), and permutation equivariant with respect to an input set ...
- **p. 2 / 1. Introduction - extractive body cue:** Our method reports the best or very competitive performance in all three experiments.
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** We will explain how Graph Autoencoders can benefit from equivariance and we will show how our method outperforms standard GNN autoencoders in the provided datasets.
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Additionally this experiment also showed that our method can successfully perform in a E(n) equivariant task for higher dimensional spaces where n > 3.
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The decoder g(·) proposed by (Liu et al., 2019) takes as input the embedding space z and outputs the reconstructed adjacency matrix ˆA = g(z), ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** Implementation details: Our Equivariant Graph AutoEncoder is composed of an EGNN encoder followed by the decoder from Equation 9.
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Our EGNN network consists of 7 layers, 128 features per hidden layer and the Swish activation function as a non-linearity.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The decoder g(·) proposed by (Liu et al., 2019) takes as input the embedding space z and outputs the reconstructed adjacency matrix ˆA = g(z), this decoder function is defined as follows: ... | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (5.2. Graph Autoencoder), p. 2 (2.1. Equivariance) |
| State/latent | decoder, Liu, takes, input, embedding, space, outputs, reconstructed, adjacency, matrix, function, defined | geometry, map, object/relationship state | p. 6 (5.2. Graph Autoencoder), p. 2 (2.1. Equivariance), p. 1 (1. Introduction) |
| Output/action | We say a function φ : X -→Y is equivariant to g if there exists an equivalent transformation on its output space Sg : Y -→Y such that: φ(Tg(x)) = Sg(φ(x)) (1) ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (2.1. Equivariance), p. 1 (1. Introduction), p. 7 (5.2. Graph Autoencoder) |
| Objective/outcome | The training loss is defined as the binary cross entropy between the estimated and the ground truth edges L = P ij BCE( ˆAij, Aij). | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder) |

## Main Claims and Actual Contribution

- **p. 2 / 2. Background - extractive body cue:** In this section we introduce the relevant materials on equivariance and graph neural networks which will later complement the definition of our method.
- **p. 1 / 1. Introduction - extractive body cue:** In this work we present a new architecture that is translation, rotation and reflection equivariant (E(n)), and permutation equivariant with respect to an input set ...
- **p. 2 / 1. Introduction - extractive body cue:** Our method reports the best or very competitive performance in all three experiments.
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** We will explain how Graph Autoencoders can benefit from equivariance and we will show how our method outperforms standard GNN autoencoders in the provided datasets.
- **p. 8 / 5.2. Graph Autoencoder - extractive body cue:** Additionally this experiment also showed that our method can successfully perform in a E(n) equivariant task for higher dimensional spaces where n > 3.
- **p. 5 / 5.1. Modelling a dynamical system - N-body system - extractive body cue:** Results As shown in Table 2 our model significantly outperforms the other equivariant and non-equivariant alternatives while still being efficient in terms of running time.
- **p. 15 / Figure/Table caption - extractive body cue:** Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, Noise-GNN ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Mean Absolute Error for the molecular property prediction benchmark in QM9 dataset. *DimeNet++ uses slightly different train/val/test partitions than the other papers listed ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 5 (5.1. Modelling a dynamical system - N-body system), p. 15 (Figure/Table caption) |
| Embodiment/environment | Dataset: We sampled 3.000 trajectories for training, 2.000 for validation and 2.000 for testing. | hardware/simulator version and reset protocol | p. 5 (5.1. Modelling a dynamical system - N-body system), p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Dataset/benchmark | Dataset: We sampled 3.000 trajectories for training, 2.000 for validation and 2.000 for testing. | role, split, size and leakage | p. 5 (5.1. Modelling a dynamical system - N-body system), p. 5 (5.1. Modelling a dynamical system - N-body system) |
| Metric | Figure 5. In the Table at the left we report the Binary Cross Entropy, % Error and F1 scores for the test partition on the Graph Autoencoding experiment in the Community Small ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Baseline/ablation | A Linear model that simply considers the motion equation p(t) = p(0) + v(0)t is also included as a baseline. | fair input/data/compute/action matching | p. 5 (5.1. Modelling a dynamical system - N-body system), p. 5 (5.1. Modelling a dynamical system - N-body system), p. 15 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** Although we observed that adding noise to the GNN improves the results, it is difficult to exactly measure the impact of the symmetry limitation in ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Mean Absolute Error for the molecular property prediction benchmark in QM9 dataset. *DimeNet++ uses slightly different train/val/test partitions than the other papers listed ...
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** The symmetry problem: The above stated autoencoder may seem straightforward to implement at first sight but in some cases there is a strong limitation regarding ...
- **p. 7 / 5.2. Graph Autoencoder - extractive body cue:** To avoid this limitation, all models exchange messages among all nodes and the edge information is provided as edge attributes aij = Aij in all ...
- **p. 6 / 5.2. Graph Autoencoder - extractive body cue:** This method introduces noise sampled from a Gaussian distribution into the input node features of the graph h0 i ∼N(0, σI).
- **p. 15 / Figure/Table caption - extractive body cue:** Table 4. Analysis of the % of wrong edges and F1 score for different n embedding sizes {2, 4, 8 } for the GNN, Noise-GNN ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Many problems exhibit 3D translation and rotation symmetries.를 문제로 두고, In this section we introduce the relevant materials on equivariance and graph neural networks which will later complement the definition of our method.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 6 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder), p. 6 (5.2. Graph Autoencoder) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
