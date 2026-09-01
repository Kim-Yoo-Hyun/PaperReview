# Problem - E(n) Equivariant Graph Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2102.09844; PDF retrieval source: https://arxiv.org/pdf/2102.09844. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): Many problems exhibit 3D translation and rotation symmetries.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** This paper introduces a new model to learn graph neural networks equivariant to rotations, translations, reflections and permutations called E(n)- Equivariant Graph Neural Networks (EGNNs).
- **p. 1 / Abstract - extractive PDF cue:** In contrast with existing methods, our work does not require computationally expensive higher-order representations in intermediate layers while it still achieves competitive or better performance.
- **p. 1 / Abstract - extractive PDF cue:** In addition, whereas existing methods are limited to equivariance on 3 dimensional spaces, our model is easily scaled to higher-dimensional spaces.
- **p. 1 / Abstract - extractive PDF cue:** We demonstrate the effectiveness of our method on dynamical systems modelling, representation learning in graph autoencoders and predicting molecular properties.
- **p. 1 / 1. Introduction - extractive PDF cue:** Although deep learning has largely replaced hand-crafted features, many advances are critically dependent on inductive biases in deep neural networks.
- **p. 1 / 1. Introduction - extractive PDF cue:** Many problems exhibit 3D translation and rotation symmetries.
- **p. 1 / 1. Introduction - extractive PDF cue:** An effective method to restrict neural networks to relevant functions is to exploit the symmetry of problems by enforcing equivariance with respect to transformations from ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Many problems exhibit 3D translation and rotation symmetries. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The decoder g(·) proposed by (Liu et al., 2019) takes as input the embedding space z and outputs the reconstructed adjacency matrix ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | decoder, Liu, takes, input, embedding, space, outputs, reconstructed, adjacency, matrix | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Additionally, practice, many, types, data, inputs, outputs, restricted | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: decoder, Liu, takes, input, embedding, space, outputs, reconstructed, adjacency, matrix | p. 6 (5.2. Graph Autoencoder), p. 2 (2.1. Equivariance), p. 1 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: section, introduce, relevant, materials, equivariance, graph, neural, networks | p. 2 (2. Background), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: training, loss, defined, binary, cross, entropy, between, estimated | p. 8 (5.2. Graph Autoencoder), p. 6 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** An effective method to restrict neural networks to relevant functions is to exploit the symmetry of problems by enforcing equivariance with respect to transformations from ...

## What the Paper Changes

PDF contribution framing (p. 2 (2. Background), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 6 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder)): In this section we introduce the relevant materials on equivariance and graph neural networks which will later complement the definition of our method.

- **p. 1 / 1. Introduction - extractive PDF cue:** In this work we present a new architecture that is translation, rotation and reflection equivariant (E(n)), and permutation equivariant with respect to an input set ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Our method reports the best or very competitive performance in all three experiments.
- **p. 6 / 5.2. Graph Autoencoder - extractive PDF cue:** We will explain how Graph Autoencoders can benefit from equivariance and we will show how our method outperforms standard GNN autoencoders in the provided datasets.
- **p. 8 / 5.2. Graph Autoencoder - extractive PDF cue:** Additionally this experiment also showed that our method can successfully perform in a E(n) equivariant task for higher dimensional spaces where n > 3.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Although we observed that adding noise to the GNN improves the results, it is difficult to exactly measure ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Table 3. Mean Absolute Error for the molecular property prediction benchmark in QM9 dataset. *DimeNet++ uses slightly different ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The symmetry problem: The above stated autoencoder may seem straightforward to implement at first sight but in some ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | To avoid this limitation, all models exchange messages among all nodes and the edge information is provided as ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (5.2. Graph Autoencoder), p. 2 (2.1. Equivariance), p. 1 (1. Introduction), p. 7 (5.2. Graph Autoencoder). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 6 (5.2. Graph Autoencoder), p. 2 (2.1. Equivariance), p. 1 (1. Introduction), p. 7 (5.2. Graph Autoencoder), objective p. 8 (5.2. Graph Autoencoder), p. 6 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 7 (5.2. Graph Autoencoder), p. 8 (5.2. Graph Autoencoder).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
