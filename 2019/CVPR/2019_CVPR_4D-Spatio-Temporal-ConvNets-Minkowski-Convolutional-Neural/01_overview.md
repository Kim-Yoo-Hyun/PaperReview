# 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1904.08755.
> PDF retrieval source: https://arxiv.org/pdf/1904.08755. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision
- Official paper: https://arxiv.org/abs/1904.08755
- Full-text retrieval: https://arxiv.org/pdf/1904.08755
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To resolve most, if not all, of the challenges in the highdimensional perception, we adopt a sparse tensor [8, 9] for our problem and propose the generalized sparse convolutions.를 문제로 두고, To overcome this challenge, we propose custom kernels with non-(hyper)-cubic shapes using the generalized sparse convolution.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In many robotics and VR/AR applications, 3D-videos are readily-available sources of input (a continuous sequence of depth images, or LIDAR scans).
- **p. 1 / Abstract - extractive body cue:** However, these 3D-videos are processed frame-by-frame either through 2D convnets or 3D perception algorithms in many cases.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose 4-dimensional convolutional neural networks for spatio-temporal perception that can directly process such 3D-videos using high-dimensional convolutions.
- **p. 1 / Abstract - extractive body cue:** For this, we adopt sparse tensors [8, 9] and propose the generalized sparse convolution which encompasses all discrete convolutions.
- **p. 1 / Abstract - extractive body cue:** To implement the generalized sparse convolution, we create an open-source auto-differentiation library for sparse tensors that provides extensive functions for highdimensional convolutional neural networks.1 We ...
- **p. 1 / 1. Introduction - extractive body cue:** To resolve most, if not all, of the challenges in the highdimensional perception, we adopt a sparse tensor [8, 9] for our problem and propose ...
- **p. 1 / 1. Introduction - extractive body cue:** However, there are many technical challenges in using 3Dvideos for high-level perception tasks.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose custom kernels with non-(hyper)-cubic shapes using the generalized sparse convolution.
- **p. 2 / 1. Introduction - extractive body cue:** To enforce consistency, we propose high-dimensional conditional random fields defined in a 7D trilateral space (space-time-color) with a stationary pairwise consistency function.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose 4-dimensional convolutional neural networks for spatio-temporal perception that can directly process such 3D-videos using high-dimensional convolutions.
- **p. 1 / Abstract - extractive body cue:** To overcome challenges in the high-dimensional 4D space, we propose the hybrid kernel, a special case of the generalized sparse convolution, and the trilateral-stationary conditional ...
- **p. 3 / 4. Minkowski Engine - extractive body cue:** In this section, we propose an open-source autodifferentiation library for sparse tensors and the generalized sparse convolution (Sec.
- **p. 6 / 6.3. Learning with 7D Sparse Convolution - extractive body cue:** Algorithm 5 Variational Inference of TS-CRF Require: Input: Logit scores φu for all xi; associated coordinate Ci, color Fi, time Ti Q0(X) = exp φu(X), ...
- **p. 3 / 4.1. Sparse Tensor Quantization - extractive body cue:** The first step in the sparse convolutional neural network is the data processing to generate a sparse tensor, which converts an input into unique coordinates, ...
- **p. 2 / 1. Introduction - extractive body cue:** We use variational inference to convert the conditional random field to differentiable recurrent layers which can be implemented in as a 7D generalized sparse convnet ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 3 reduces the input features that map to the same output coordinate. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling) |
| State/latent | reduces, input, features, same, output, coordinate, Similar, pooling, algorithm, input-tooutput, kernel, many | geometry, map, object/relationship state | p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling), p. 1 (Abstract) |
| Output/action | Similar to the max pooling algorithm, M is the (I, O) input-tooutput kernel map. | point map, pose, scene graph, affordance 또는 query result | p. 4 (4.3. Max Pooling), p. 1 (Abstract), p. 3 (3.1. Generalized Sparse Convolution) |
| Objective/outcome | Second, the networks do not have an incentive to make the prediction consistent throughout the space and time with conventional cross-entropy loss alone. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (5. Minkowski Convolutional Neural Networks), p. 6 (6.3. Learning with 7D Sparse Convolution), p. 6 (6. Trilateral Stationary-CRF) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose custom kernels with non-(hyper)-cubic shapes using the generalized sparse convolution.
- **p. 2 / 1. Introduction - extractive body cue:** To enforce consistency, we propose high-dimensional conditional random fields defined in a 7D trilateral space (space-time-color) with a stationary pairwise consistency function.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose 4-dimensional convolutional neural networks for spatio-temporal perception that can directly process such 3D-videos using high-dimensional convolutions.
- **p. 1 / Abstract - extractive body cue:** To overcome challenges in the high-dimensional 4D space, we propose the hybrid kernel, a special case of the generalized sparse convolution, and the trilateral-stationary conditional ...
- **p. 3 / 4. Minkowski Engine - extractive body cue:** In this section, we propose an open-source autodifferentiation library for sparse tensors and the generalized sparse convolution (Sec.
- **p. 7 / 7.4. Results and Analysis - extractive body cue:** We trained the same network for 60k iterations with 2cm voxel and achieved 72.1% mIoU on ScanNet after the deadline.
- **p. 7 / 7.4. Results and Analysis - extractive body cue:** We were able to achieve +19% mIOU on ScanNet, and +7% on Stanford compared with the bestpublished works by the CVPR deadline.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** 4D analysis The RueMongue dataset is a small dataset that ranges one section of a street, so with the smallest network, we were able to ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (7.4. Results and Analysis), p. 7 (7.4. Results and Analysis) |
| Embodiment/environment | In total, the train/val/test set contain 20k/815/1886 3D scenes respectively. | hardware/simulator version and reset protocol | p. 7 (7.3. Datasets), p. 7 (7.3. Datasets) |
| Dataset/benchmark | We use the Synthia datasets with and without noise for 3D and 4D analysis and results are presented in Tab. | role, split, size and leakage | p. 7 (7.3. Datasets), p. 7 (7.3. Datasets), p. 8 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis) |
| Metric | Per class IoU in the supplementary material. | definition, denominator, direction and uncertainty | p. 7 (7.3. Datasets), p. 7 (7.2. Training and Evaluation), p. 8 (Figure/Table caption) |
| Baseline/ablation | We were able to achieve +19% mIOU on ScanNet, and +7% on Stanford compared with the bestpublished works by the CVPR deadline. | fair input/data/compute/action matching | p. 7 (7.4. Results and Analysis), p. 7 (7. Experiments), p. 8 (7.4. Results and Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 7.4. Results and Analysis - extractive body cue:** Specifically, when we simulate noise in sensory inputs on the 4D Synthia dataset, we can observe that the 4D networks are more robust to noise.
- **p. 6 / 6. Trilateral Stationary-CRF - extractive body cue:** However, the loss does not enforce consistency as it does not have pair-wise terms.
- **p. 7 / 7.3. Datasets - extractive body cue:** We used elastic distortion, Gaussian noise, and chromatic shift in the color for the noisy 4D Synthia experiments.
- **p. 7 / 7.3. Datasets - extractive body cue:** Since the dataset is purely synthetic, we added various noise to the input point clouds to simulate noisy observations.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** As the input pointcloud coordinates are noisy, averaging along the temporal dimension introduces noise.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To resolve most, if not all, of the challenges in the highdimensional perception, we adopt a sparse tensor [8, 9] for our problem and propose the generalized sparse convolutions.를 문제로 두고, To overcome this challenge, we propose custom kernels with non-(hyper)-cubic shapes using the generalized sparse convolution.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 6 (6.3. Learning with 7D Sparse Convolution), p. 3 (4.1. Sparse Tensor Quantization) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
