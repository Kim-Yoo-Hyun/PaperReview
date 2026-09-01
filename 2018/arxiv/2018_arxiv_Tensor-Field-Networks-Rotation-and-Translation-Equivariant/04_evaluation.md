# Evaluation - Tensor Field Networks: Rotation- and Translation-Equivariant Neural Networks for 3D Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1802.08219; PDF retrieval source: https://arxiv.org/pdf/1802.08219. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 1 (Abstract), p. 9 (Figure/Table caption)): This capability has contributed significantly to their widespread success.

## Evaluation Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We demonstrate the capabilities of tensor field networks with tasks in geometry, physics, and chemistry.
- **p. 2 / Abstract - extractive PDF cue:** Finally, the network naturally encodes geometric tensors (such as scalars, vectors, and higher-rank geometric objects), mathematical objects that transform predictably under geometric transformations of rotation ...
- **p. 2 / Abstract - extractive PDF cue:** In this paper, we explain the mathematical conditions that such a 3D rotation- and translationequivariant network must satisfy, provide several examples of equivariant-compatible network components, ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Performance on missing point task Atoms Number of predictions Accuracy (%) (≤0.5 Å and atom type) Distance
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 2: 3D Tetris shapes. Blocks correspond to single points. The third and fourth shapes from the left are mirrored versions of each other. Rotation ...
- **p. 1 / Abstract - extractive PDF cue:** This capability has contributed significantly to their widespread success.
- **p. 2 / Abstract - extractive PDF cue:** Our network differs from a traditional convolutional neural network (CNN) in three ways: • We operate on point clouds using continuous convolutions.
- **p. 2 / Abstract - extractive PDF cue:** Equivariance confers three main benefits: First, this is more efficient than data augmentation to obtain 3D rotation-invariant output, making computation and training less expensive.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Abstract | SYSTEM / EVALUATION SCOPE UNRESOLVED | This capability has contributed significantly to their widespread success. | p. 1 (Abstract) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Table 1: Performance on missing point task Atoms Number of predictions Accuracy (%) (≤0.5 Å and atom type) Distance | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 1 / Abstract - extractive PDF cue:** We demonstrate the capabilities of tensor field networks with tasks in geometry, physics, and chemistry.
- **p. 2 / Abstract - extractive PDF cue:** Finally, the network naturally encodes geometric tensors (such as scalars, vectors, and higher-rank geometric objects), mathematical objects that transform predictably under geometric transformations of rotation ...
- **p. 2 / Abstract - extractive PDF cue:** In this paper, we explain the mathematical conditions that such a 3D rotation- and translationequivariant network must satisfy, provide several examples of equivariant-compatible network components, ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 1: Example of V (l) acm representing two point masses with velocities and accelerations. Colored brackets indicate the a (point), c (channel), and m ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Network diagrams for shape classification task showing how information flows between tensors of different order. Clebsch-Gordan tensors are implied in the arrows indicating ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 2: 3D Tetris shapes. Blocks correspond to single points. The third and fourth shapes from the left are mirrored versions of each other. Rotation ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: A hypothetical example input and out- put of the missing point network. (A) A benzene molecule with hydrogen removed (B) The relative output ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 1: Performance on missing point task Atoms Number of predictions Accuracy (%) (≤0.5 Å and atom type) Distance

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We demonstrate the capabilities of tensor field networks with tasks in geometry, physics, and chemistry. | embodiment, simulator version and control stack | p. 1 (Abstract), p. 2 (Abstract) |
| Task/environment | Finally, the network naturally encodes geometric tensors (such as scalars, vectors, and higher-rank geometric objects), mathematical objects that transform predictably under geometric transformations of ... | reset, timeout, object/scene variation | p. 2 (Abstract), p. 2 (Abstract) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (Abstract), p. 2 (Abstract) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (Abstract), p. 2 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 1: Performance on missing point task Atoms Number of predictions Accuracy (%) (≤0.5 Å and atom type) Distance | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 2: 3D Tetris shapes. Blocks correspond to single points. The third and fourth shapes from the left are mirrored versions of each other. ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| This capability has contributed significantly to their widespread success. | definition/direction/unit from same section | p. 1 (Abstract) |
| We demonstrate the capabilities of tensor field networks with tasks in geometry, physics, and chemistry. | definition/direction/unit from same section | p. 1 (Abstract) |
| Our network differs from a traditional convolutional neural network (CNN) in three ways: • We operate on point clouds using continuous convolutions. | definition/direction/unit from same section | p. 2 (Abstract) |
| Equivariance confers three main benefits: First, this is more efficient than data augmentation to obtain 3D rotation-invariant output, making computation and training less expensive. | definition/direction/unit from same section | p. 2 (Abstract) |
| Figure 3: Network diagrams for shape classification task showing how information flows between tensors of different order. Clebsch-Gordan tensors are implied in the arrows ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This is significantly more important in 3D than in 2D: Without equivariant filters like those in our design, achieving an angular resolution of δ ... | comparison identity and matched condition | p. 2 (Abstract) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This is significantly more important in 3D than in 2D: Without equivariant filters like those in our design, achieving an angular resolution of δ ... | component/input/data sensitivity | p. 2 (Abstract) |
| In this paper, we explain the mathematical conditions that such a 3D rotation- and translationequivariant network must satisfy, provide several examples of equivariant-compatible network ... | component/input/data sensitivity | p. 2 (Abstract) |
| 3D rotation equivariance removes the need for data augmentation to identify features in arbitrary orientations. | component/input/data sensitivity | p. 1 (Abstract) |
| 1 Motivation Convolutional neural networks are translation-equivariant, which means that features can be identified anywhere in a given input. | component/input/data sensitivity | p. 1 (Abstract) |
| Figure 4: A hypothetical example input and out- put of the missing point network. (A) A benzene molecule with hydrogen removed (B) The relative ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present a family of networks that enjoy richer equivariance: the symmetries of 3D Euclidean space. | This capability has contributed significantly to their widespread success. | PDF body cue; verify exact table/figure and matched conditions | p. 1 (Abstract), p. 9 (Figure/Table caption) |
| Primary metric/result | Table 1: Performance on missing point task Atoms Number of predictions Accuracy (%) (≤0.5 Å and atom type) Distance | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Any network that relies solely upon distances (such as SchNet [2]) or angles between points (such as ANI-1 [15]) cannot distinguish these shapes, but ... | p. 7 (2 Related work) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Finally, the network naturally encodes geometric tensors (such as scalars, vectors, and higher-rank geometric objects), mathematical objects that transform predictably under geometric transformations of ... | p. 2 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 2 Related work - extractive PDF cue:** Any network that relies solely upon distances (such as SchNet [2]) or angles between points (such as ANI-1 [15]) cannot distinguish these shapes, but ours ...

- **PDF anchors reviewed:** datasets p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), metrics p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract), p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), baselines p. 2 (Abstract), results p. 1 (Abstract), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
