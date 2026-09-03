# Tensor Field Networks: Rotation- and Translation-Equivariant Neural Networks for 3D Point Clouds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1802.08219.
> PDF retrieval source: https://arxiv.org/pdf/1802.08219. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2018 / arXiv
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, equivariant, 3D geometry, point cloud
- Official paper: https://arxiv.org/abs/1802.08219
- Full-text retrieval: https://arxiv.org/pdf/1802.08219
- Code/Project: https://github.com/tensorfieldnetworks/tensorfieldnetworks
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.를 문제로 두고, In this paper, we present a family of networks that enjoy richer equivariance: the symmetries of 3D Euclidean space.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.
- **p. 1 / Abstract - extractive body cue:** 3D rotation equivariance removes the need for data augmentation to identify features in arbitrary orientations.
- **p. 1 / Abstract - extractive body cue:** Our network uses filters built from spherical harmonics; due to the mathematical consequences of this filter choice, each layer accepts as input (and guarantees as ...
- **p. 1 / Abstract - extractive body cue:** We demonstrate the capabilities of tensor field networks with tasks in geometry, physics, and chemistry.
- **p. 1 / Abstract - extractive body cue:** 1 Motivation Convolutional neural networks are translation-equivariant, which means that features can be identified anywhere in a given input.

## Core Idea

- **p. 1 / Abstract - extractive body cue:** In this paper, we present a family of networks that enjoy richer equivariance: the symmetries of 3D Euclidean space.
- **p. 1 / Abstract - extractive body cue:** We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.
- **p. 2 / Abstract - extractive body cue:** Equivariance confers three main benefits: First, this is more efficient than data augmentation to obtain 3D rotation-invariant output, making computation and training less expensive.
- **p. 2 / Abstract - extractive body cue:** We call these tensor field networks because every layer of our network inputs and outputs tensor fields: scalars, vectors, and higher-order tensors at every geometric ...
- **p. 1 / Abstract - extractive body cue:** 1 Motivation Convolutional neural networks are translation-equivariant, which means that features can be identified anywhere in a given input.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our network uses filters built from spherical harmonics; due to the mathematical consequences of this filter choice, each layer accepts as input (and guarantees as output) scalars, vectors, and higher-order tensors, in ... | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (Abstract), p. 2 (Abstract) |
| State/latent | network, uses, filters, built, spherical, harmonics, mathematical, consequences, filter, choice, layer, accepts | geometry, map, object/relationship state | p. 1 (Abstract), p. 2 (Abstract), p. 1 (Abstract) |
| Output/action | We call these tensor field networks because every layer of our network inputs and outputs tensor fields: scalars, vectors, and higher-order tensors at every geometric point in the network. | point map, pose, scene graph, affordance 또는 query result | p. 2 (Abstract), p. 1 (Abstract), p. 2 (Abstract) |
| geometric accuracy, semantic consistency와 planning/manipulation utility | p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 1 / Abstract - extractive body cue:** In this paper, we present a family of networks that enjoy richer equivariance: the symmetries of 3D Euclidean space.
- **p. 1 / Abstract - extractive body cue:** We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.
- **p. 1 / Abstract - extractive body cue:** This capability has contributed significantly to their widespread success.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 1: Performance on missing point task Atoms Number of predictions Accuracy (%) (≤0.5 Å and atom type) Distance

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 1 (Abstract), p. 9 (Figure/Table caption) |
| Embodiment/environment | We demonstrate the capabilities of tensor field networks with tasks in geometry, physics, and chemistry. | hardware/simulator version and reset protocol | p. 1 (Abstract), p. 2 (Abstract) |
| Dataset/benchmark | In this paper, we explain the mathematical conditions that such a 3D rotation- and translationequivariant network must satisfy, provide several examples of equivariant-compatible network components, and give examples of tasks that this ... | role, split, size and leakage | p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract) |
| Metric | Table 1: Performance on missing point task Atoms Number of predictions Accuracy (%) (≤0.5 Å and atom type) Distance | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract) |
| Baseline/ablation | This is significantly more important in 3D than in 2D: Without equivariant filters like those in our design, achieving an angular resolution of δ would require a factor of O(δ-1) more filters ... | fair input/data/compute/action matching | p. 2 (Abstract), p. 2 (Abstract), p. 2 (Abstract) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 2 Related work - extractive body cue:** Any network that relies solely upon distances (such as SchNet [2]) or angles between points (such as ANI-1 [15]) cannot distinguish these shapes, but ours ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.를 문제로 두고, In this paper, we present a family of networks that enjoy richer equivariance: the symmetries of 3D Euclidean space.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 9 (Figure/Table caption) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
