# SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2006.10503.
> PDF retrieval source: https://arxiv.org/pdf/2006.10503. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: equivariant, 3D geometry, Transformer
- Official paper: https://arxiv.org/abs/2006.10503
- Full-text retrieval: https://arxiv.org/pdf/2006.10503
- Code/Project: https://github.com/FabianFuchsML/se3-transformer-public
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, their generality of application means that for specific tasks, knowledge of existing underlying structure is unused.를 문제로 두고, In this paper, we propose the SE(3)-Transformer shown in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce the SE(3)-Transformer, a variant of the self-attention module for 3D point clouds and graphs, which is equivariant under continuous 3D rototranslations.
- **p. 1 / Abstract - extractive body cue:** Equivariance is important to ensure stable and predictable performance in the presence of nuisance transformations of the data input.
- **p. 1 / Abstract - extractive body cue:** A positive corollary of equivariance is increased weight-tying within the model.
- **p. 1 / Abstract - extractive body cue:** The SE(3)- Transformer leverages the benefits of self-attention to operate on large point clouds and graphs with varying number of points, while guaranteeing SE(3)-equivariance for ...
- **p. 1 / Abstract - extractive body cue:** We evaluate our model on a toy N-body particle simulation dataset, showcasing the robustness of the predictions under rotations of the input.
- **p. 1 / 1 Introduction - extractive body cue:** However, their generality of application means that for specific tasks, knowledge of existing underlying structure is unused.
- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we find that the explicit imposition of equivariance constraints on the self-attention mechanism addresses these challenges.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we propose the SE(3)-Transformer shown in Fig.
- **p. 5 / 3 Method - extractive body cue:** Here, we present the SE(3)-Transformer.
- **p. 5 / 3 Method - extractive body cue:** This mechanism consists of a normalised inner product between a query vector qi 5
- **p. 6 / 3 Method - extractive body cue:** Attentive: We propose an extension of linear self-interaction, attentive self-interaction, combining self-interaction and nonlinearity.
- **p. 6 / 3 Method - extractive body cue:** These weights are SE(3)-invariant due to the invariance of inner products of features, transforming under the same representation. wℓℓ i,c′c = MLP  M c,c′ ...
- **p. 6 / 3 Method - extractive body cue:** Channels, Self-interaction Layers, and Non-Linearities Analogous to conventional neural networks, the SE(3)-Transformer can straightforwardly be extended to multiple channels per representation degree ℓ, so far ...
- **p. 5 / 3 Method - extractive body cue:** 3.2 The SE(3)-Transformer The SE(3)-Transformer itself consists of three components.
- **p. 5 / 3 Method - extractive body cue:** If we remove the attention weights then we have a tensor field convolution, and if we instead remove the dependence of WV on (xj -xi), ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Furthermore, an important property is that these structures should be invariant to global changes in overall input pose; that is, 3D translations and rotations of the input point cloud should not affect ... | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1 Introduction), p. 6 (3 Method) |
| State/latent | Furthermore, important, property, structures, should, invariant, global, changes, overall, input, pose, translations | geometry, map, object/relationship state | p. 1 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method) |
| Output/action | [25], output channels are a learned linear combination of input channels using one set of weights wℓℓ i,c′c = wℓℓ c′c per representation degree, shared across all points. | point map, pose, scene graph, affordance 또는 query result | p. 6 (3 Method), p. 6 (3 Method), p. 5 (3 Method) |
| Objective/outcome | geometric accuracy, semantic consistency와 planning/manipulation utility | geometric accuracy, semantic consistency와 planning/manipulation utility | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we propose the SE(3)-Transformer shown in Fig.
- **p. 5 / 3 Method - extractive body cue:** Here, we present the SE(3)-Transformer.
- **p. 5 / 3 Method - extractive body cue:** This mechanism consists of a normalised inner product between a query vector qi 5
- **p. 6 / 3 Method - extractive body cue:** Attentive: We propose an extension of linear self-interaction, attentive self-interaction, combining self-interaction and nonlinearity.
- **p. 8 / 4 Experiments - extractive body cue:** If both training and test set are not rotated (x = 0 in a), breaking the symmetry of the SE(3)-Transformer by providing the z-component of ...
- **p. 7 / 4 Experiments - extractive body cue:** Our model outperforms both an attention-based, but not rotation-equivariant approach (Set Transformer) and a equivariant approach which does not levarage attention (Tensor Field).
- **p. 22 / Figure/Table caption - extractive body cue:** Figure 7: Attention block for the QM9 dataset. Each component is listed with a tuple of numbers representing the output feature types and multiplicities, so ...
- **p. 8 / 4 Experiments - extractive body cue:** This results in a performance loss when deploying a fully SO(3) invariant model (see Fig.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | To test our method, we choose ScanObjectNN, a recently introduced dataset for real-world object classification. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | Points 128 1024 128 1024 1024 1024 1024 128 1024 128 1024 1024 1024 Accuracy 63.1% 71.4% 72.8 % 73.8% 74.1% 79.2% 79.5% 81.0% 84.3% 85.0% 85.5% 86.2% 87.2% 4.2 Real-World Object ... | role, split, size and leakage | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Metric | The distance between the two, averaged over samples, yields the equivariance error. | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (Figure/Table caption) |
| Baseline/ablation | We compare to publicly available, state-of-the-art results as well as a set of our own baselines. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 Conclusion - extractive body cue:** This architecture is guaranteed to be robust to rotations and translations of the input, obviating the need for training time data augmentation and ensuring stability ...
- **p. 9 / 5 Conclusion - extractive body cue:** On the other hand, compared to convential attention, adding the equivariance constraints also increases performance in all of our experiments while at the same time ...
- **p. 7 / 4 Experiments - extractive body cue:** Our model outperforms both an attention-based, but not rotation-equivariant approach (Set Transformer) and a equivariant approach which does not levarage attention (Tensor Field).
- **p. 7 / 4 Experiments - extractive body cue:** Specifically, we compare to the Set-Transformer [16], a non-equivariant attention model, and Tensor Field Networks [28], which is similar to SE(3)-Transformer but does not leverage ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, their generality of application means that for specific tasks, knowledge of existing underlying structure is unused.를 문제로 두고, In this paper, we propose the SE(3)-Transformer shown in Fig.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 1 (1 Introduction), p. 6 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
