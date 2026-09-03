# Problem - 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.08755; PDF retrieval source: https://arxiv.org/pdf/1904.08755. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): To resolve most, if not all, of the challenges in the highdimensional perception, we adopt a sparse tensor [8, 9] for our problem and propose the generalized sparse convolutions.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** In many robotics and VR/AR applications, 3D-videos are readily-available sources of input (a continuous sequence of depth images, or LIDAR scans).
- **p. 1 / Abstract - extractive body cue:** However, these 3D-videos are processed frame-by-frame either through 2D convnets or 3D perception algorithms in many cases.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose 4-dimensional convolutional neural networks for spatio-temporal perception that can directly process such 3D-videos using high-dimensional convolutions.
- **p. 1 / Abstract - extractive body cue:** For this, we adopt sparse tensors [8, 9] and propose the generalized sparse convolution which encompasses all discrete convolutions.
- **p. 1 / Abstract - extractive body cue:** To implement the generalized sparse convolution, we create an open-source auto-differentiation library for sparse tensors that provides extensive functions for highdimensional convolutional neural networks.1 We ...
- **p. 1 / 1. Introduction - extractive body cue:** To resolve most, if not all, of the challenges in the highdimensional perception, we adopt a sparse tensor [8, 9] for our problem and propose ...
- **p. 1 / 1. Introduction - extractive body cue:** However, there are many technical challenges in using 3Dvideos for high-level perception tasks.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | To resolve most, if not all, of the challenges in the highdimensional perception, we adopt a sparse tensor [8, 9] for our ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 3 reduces the input features that map to the same output coordinate. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | reduces, input, features, same, output, coordinate, Similar, pooling, algorithm, input-tooutput | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | many, robotics, VR/AR, applications, D-videos, readily-available, sources, input | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: reduces, input, features, same, output, coordinate, Similar, pooling, algorithm, input-tooutput | p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling), p. 1 (Abstract) |
| Decision / output variable | geometry/map/query r; body terms: overcome, challenge, custom, kernels, non-, hyper, cubic, shapes | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Second, networks, have, incentive, make, prediction, consistent, throughout | p. 6 (6.3. Learning with 7D Sparse Convolution), p. 6 (6. Trilateral Stationary-CRF), p. 5 (5. Minkowski Convolutional Neural Networks), p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (5. Minkowski Convolutional Neural Networks), p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (7.3. Datasets), p. 7 (7.2. Training and Evaluation), p. 8 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** However, there are many technical challenges in using 3Dvideos for high-level perception tasks.
- **p. 2 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose custom kernels with non-(hyper)-cubic shapes using the generalized sparse convolution.
- **p. 2 / 1. Introduction - extractive body cue:** We use variational inference to convert the conditional random field to differentiable recurrent layers which can be implemented in as a 7D generalized sparse convnet ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 3 (4. Minkowski Engine)): To overcome this challenge, we propose custom kernels with non-(hyper)-cubic shapes using the generalized sparse convolution.

- **p. 2 / 1. Introduction - extractive body cue:** To enforce consistency, we propose high-dimensional conditional random fields defined in a 7D trilateral space (space-time-color) with a stationary pairwise consistency function.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose 4-dimensional convolutional neural networks for spatio-temporal perception that can directly process such 3D-videos using high-dimensional convolutions.
- **p. 1 / Abstract - extractive body cue:** To overcome challenges in the high-dimensional 4D space, we propose the hybrid kernel, a special case of the generalized sparse convolution, and the trilateral-stationary conditional ...
- **p. 3 / 4. Minkowski Engine - extractive body cue:** In this section, we propose an open-source autodifferentiation library for sparse tensors and the generalized sparse convolution (Sec.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Specifically, when we simulate noise in sensory inputs on the 4D Synthia dataset, we can observe that the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | However, the loss does not enforce consistency as it does not have pair-wise terms. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | We used elastic distortion, Gaussian noise, and chromatic shift in the color for the noisy 4D Synthia experiments. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Since the dataset is purely synthetic, we added various noise to the input point clouds to simulate noisy ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling), p. 1 (Abstract), p. 3 (3.1. Generalized Sparse Convolution). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling), p. 1 (Abstract), p. 3 (3.1. Generalized Sparse Convolution), objective p. 6 (6.3. Learning with 7D Sparse Convolution), p. 6 (6. Trilateral Stationary-CRF), p. 5 (5. Minkowski Convolutional Neural Networks), p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
