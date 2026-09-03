# Method - 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.08755; PDF retrieval source: https://arxiv.org/pdf/1904.08755. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (6.3. Learning with 7D Sparse Convolution), p. 3 (4.1. Sparse Tensor Quantization), p. 2 (1. Introduction), p. 5 (5. Minkowski Convolutional Neural Networks), p. 6 (6. Trilateral Stationary-CRF), p. 2 (1. Introduction)): Algorithm 5 Variational Inference of TS-CRF Require: Input: Logit scores φu for all xi; associated coordinate Ci, color Fi, time Ti Q0(X) = exp φu(X), Ccrf = [C, F, T] ...

## Method Body Digest

- **p. 6 / 6.3. Learning with 7D Sparse Convolution - extractive body cue:** Algorithm 5 Variational Inference of TS-CRF Require: Input: Logit scores φu for all xi; associated coordinate Ci, color Fi, time Ti Q0(X) = exp φu(X), ...
- **p. 3 / 4.1. Sparse Tensor Quantization - extractive body cue:** The first step in the sparse convolutional neural network is the data processing to generate a sparse tensor, which converts an input into unique coordinates, ...
- **p. 2 / 1. Introduction - extractive body cue:** We use variational inference to convert the conditional random field to differentiable recurrent layers which can be implemented in as a 7D generalized sparse convnet ...
- **p. 5 / 5. Minkowski Convolutional Neural Networks - extractive body cue:** Second, to enforce spatio-temporal consistency, we propose a high-dimensional conditional random field (7D space-time-color space) that filters network predictions.
- **p. 6 / 6. Trilateral Stationary-CRF - extractive body cue:** To find the global optima of the distribution, we use the variational inference and convert a series of fixed point update equations to a recurrent ...
- **p. 2 / 1. Introduction - extractive body cue:** Thus, we adopt the sparse representation for the our problem and create the first large-scale 3D/4D networks or Minkowski networks.3 We named them after the ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose 4-dimensional convolutional neural networks for spatio-temporal perception that can directly process such 3D-videos using high-dimensional convolutions.
- **p. 5 / 5. Minkowski Convolutional Neural Networks - extractive body cue:** Second, the networks do not have an incentive to make the prediction consistent throughout the space and time with conventional cross-entropy loss alone.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose custom kernels with non-(hyper)-cubic shapes using the generalized sparse convolution.
- **p. 2 / 1. Introduction - extractive body cue:** To enforce consistency, we propose high-dimensional conditional random fields defined in a 7D trilateral space (space-time-color) with a stationary pairwise consistency function.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose 4-dimensional convolutional neural networks for spatio-temporal perception that can directly process such 3D-videos using high-dimensional convolutions.

## Source Evidence Cues

- **p. 6 / 6.3. Learning with 7D Sparse Convolution - extractive body cue:** Algorithm 5 Variational Inference of TS-CRF Require: Input: Logit scores φu for all xi; associated coordinate Ci, color Fi, time Ti Q0(X) = exp φu(X), ...
- **p. 3 / 4.1. Sparse Tensor Quantization - extractive body cue:** The first step in the sparse convolutional neural network is the data processing to generate a sparse tensor, which converts an input into unique coordinates, ...
- **p. 2 / 1. Introduction - extractive body cue:** We use variational inference to convert the conditional random field to differentiable recurrent layers which can be implemented in as a 7D generalized sparse convnet ...
- **p. 5 / 5. Minkowski Convolutional Neural Networks - extractive body cue:** Second, to enforce spatio-temporal consistency, we propose a high-dimensional conditional random field (7D space-time-color space) that filters network predictions.
- **p. 6 / 6. Trilateral Stationary-CRF - extractive body cue:** To find the global optima of the distribution, we use the variational inference and convert a series of fixed point update equations to a recurrent ...
- **p. 2 / 1. Introduction - extractive body cue:** Thus, we adopt the sparse representation for the our problem and create the first large-scale 3D/4D networks or Minkowski networks.3 We named them after the ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose 4-dimensional convolutional neural networks for spatio-temporal perception that can directly process such 3D-videos using high-dimensional convolutions.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Algorithm 5 Variational Inference of TS-CRF Require: Input: Logit scores φu for all xi; associated coordinate Ci, color Fi, time Ti Q0(X) ... | p. 6 (6.3. Learning with 7D Sparse Convolution), p. 3 (4.1. Sparse Tensor Quantization) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The first step in the sparse convolutional neural network is the data processing to generate a sparse tensor, which converts an input ... | p. 3 (4.1. Sparse Tensor Quantization), p. 2 (1. Introduction) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We use variational inference to convert the conditional random field to differentiable recurrent layers which can be implemented in as a 7D ... | p. 2 (1. Introduction), p. 5 (5. Minkowski Convolutional Neural Networks) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 5. Minkowski Convolutional Neural Networks - extractive body cue:** Second, the networks do not have an incentive to make the prediction consistent throughout the space and time with conventional cross-entropy loss alone.
- **p. 6 / 6.3. Learning with 7D Sparse Convolution - extractive body cue:** Thus, we convert fixed point update equation Eq.
- **p. 6 / 6. Trilateral Stationary-CRF - extractive body cue:** For semantic segmentation, the cross-entropy loss is applied for each pixel or voxel.
- **p. 5 / 5. Minkowski Convolutional Neural Networks - extractive body cue:** First, the computational cost and the number of parameters in the networks increase exponentially as we increase the dimension.
- **p. 4 / 4.3. Max Pooling - extractive body cue:** We use a sparse matrix multiplication since it can be optimized on hardware or using a faster sparse BLAS library.
- **p. 4 / 4.3. Max Pooling - extractive body cue:** Sequence(n) generates a sequence of integers from 0 to n - 1 and the reduction function f((k1, v1), (k2, v2)) = min(v1, v2) which returns ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (6.3. Learning with 7D Sparse Convolution), p. 6 (6. Trilateral Stationary-CRF), p. 5 (5. Minkowski Convolutional Neural Networks), p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | reduces, input, features, same, output, coordinate, Similar, pooling, algorithm, input-tooutput, kernel, many, robotics, VR/AR | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | reduces, input, features, same, output, coordinate, Similar, pooling, algorithm, input-tooutput | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | overcome, challenge, custom, kernels, non-, hyper, cubic, shapes, generalized, sparse | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Second, networks, have, incentive, make, prediction, consistent, throughout, space, time | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.3. Max Pooling - extractive body cue:** 3 reduces the input features that map to the same output coordinate.
- **p. 4 / 4.3. Max Pooling - extractive body cue:** Similar to the max pooling algorithm, M is the (I, O) input-tooutput kernel map.
- **p. 1 / Abstract - extractive body cue:** In many robotics and VR/AR applications, 3D-videos are readily-available sources of input (a continuous sequence of depth images, or LIDAR scans).
- **p. 3 / 3.1. Generalized Sparse Convolution - extractive body cue:** Cin and Cout are predefined input and output coordinates of sparse tensors.
- **p. 3 / 3.1. Generalized Sparse Convolution - extractive body cue:** First, note that the input coordinates and output coordinates are not necessarily the same.
- **p. 1 / 1. Introduction - extractive body cue:** 1D: Line 2D: Square 3D: Cube 4D: Tesseract Figure 2: 2D projections of hypercubes in various dimensions more affordable and widely used for robotics applications, ...
- **p. 2 / 1. Introduction - extractive body cue:** It only computes outputs for predefined coordinates and saves them into a compact sparse tensor (Sec.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | To create a 4D dataset, we crop the 3D reconstruction on-the-fly to generate a temporal sequence. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Next, we create multiple 4D datasets from 3D datasets that have temporal sequences and analyze each of the proposed components for ablation ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Algorithm 4 GPU Sparse Tensor AvgPooling Input: mapping M = (I, O), features F, one vector 1 SM = coo2csr(row=O, col=I, val=1) ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 6.3. Learning with 7D Sparse Convolution - extractive body cue:** Algorithm 5 Variational Inference of TS-CRF Require: Input: Logit scores φu for all xi; associated coordinate Ci, color Fi, time Ti Q0(X) = exp φu(X), ...
- **p. 3 / 4.1. Sparse Tensor Quantization - extractive body cue:** The first step in the sparse convolutional neural network is the data processing to generate a sparse tensor, which converts an input into unique coordinates, ...
- **p. 2 / 1. Introduction - extractive body cue:** We use variational inference to convert the conditional random field to differentiable recurrent layers which can be implemented in as a 7D generalized sparse convnet ...
- **p. 6 / 6. Trilateral Stationary-CRF - extractive body cue:** To find the global optima of the distribution, we use the variational inference and convert a series of fixed point update equations to a recurrent ...
- **p. 7 / 7.2. Training and Evaluation - extractive body cue:** We use Momentum SGD with the Poly scheduler to train networks from learning rate 1e-1 and apply data augmentation including random scaling, rotation around the ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Algorithm, Variational, Inference, TS-CRF, Require, Input, Logit, scores, associated, coordinate, color, time, Ccrf, SparseConvolution, Qn-1, kernel, Softmax, return, Finally, predictions.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | In total, the train/val/test set contain 20k/815/1886 3D scenes respectively. | p. 7 (7.3. Datasets), p. 7 (7.3. Datasets) |
| Semantic / temporal fusion | We were able to achieve +19% mIOU on ScanNet, and +7% on Stanford compared with the bestpublished works by the CVPR deadline. | p. 7 (7.4. Results and Analysis), p. 7 (7. Experiments) |
| Robot query / planning handoff | We trained the same network for 60k iterations with 2cm voxel and achieved 72.1% mIoU on ScanNet after the deadline. | p. 7 (7.4. Results and Analysis), p. 7 (7.4. Results and Analysis) |

## Failure and Ablation Link

- **p. 7 / 7. Experiments - extractive body cue:** Next, we create multiple 4D datasets from 3D datasets that have temporal sequences and analyze each of the proposed components for ablation study.
- **p. 7 / 7.3. Datasets - extractive body cue:** We feed an entire room to a MinkowskiNet fully convolutionally without cropping.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** We use various 3D and 4D networks with and without TS-CRF.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** We use the Synthia datasets with and without noise for 3D and 4D analysis and results are presented in Tab.
- **p. 8 / 7.4. Results and Analysis - extractive body cue:** Specifically, when we simulate noise in sensory inputs on the 4D Synthia dataset, we can observe that the 4D networks are more robust to noise.
- **p. 6 / 6. Trilateral Stationary-CRF - extractive body cue:** However, the loss does not enforce consistency as it does not have pair-wise terms.
- **p. 7 / 7.3. Datasets - extractive body cue:** We used elastic distortion, Gaussian noise, and chromatic shift in the color for the noisy 4D Synthia experiments.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (6.3. Learning with 7D Sparse Convolution), p. 3 (4.1. Sparse Tensor Quantization), p. 2 (1. Introduction), p. 5 (5. Minkowski Convolutional Neural Networks), p. 6 (6. Trilateral Stationary-CRF), p. 2 (1. Introduction), objective p. 5 (5. Minkowski Convolutional Neural Networks), p. 6 (6.3. Learning with 7D Sparse Convolution), p. 6 (6. Trilateral Stationary-CRF), p. 5 (5. Minkowski Convolutional Neural Networks), p. 4 (4.3. Max Pooling), p. 4 (4.3. Max Pooling), temporal p. 7 (7.3. Datasets), p. 7 (7. Experiments), p. 1 (1. Introduction), p. 8 (7.4. Results and Analysis), p. 8 (7.4. Results and Analysis), p. 3 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
