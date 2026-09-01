# Method - Tensor Field Networks: Rotation- and Translation-Equivariant Neural Networks for 3D Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1802.08219; PDF retrieval source: https://arxiv.org/pdf/1802.08219. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract)): We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.

## Method Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.
- **p. 2 / Abstract - extractive PDF cue:** Equivariance confers three main benefits: First, this is more efficient than data augmentation to obtain 3D rotation-invariant output, making computation and training less expensive.
- **p. 2 / Abstract - extractive PDF cue:** We call these tensor field networks because every layer of our network inputs and outputs tensor fields: scalars, vectors, and higher-order tensors at every geometric ...
- **p. 1 / Abstract - extractive PDF cue:** 1 Motivation Convolutional neural networks are translation-equivariant, which means that features can be identified anywhere in a given input.
- **p. 1 / Abstract - extractive PDF cue:** Work in progress. arXiv:1802.08219v3 [cs.LG] 18 May 2018
- **p. 1 / Abstract - extractive PDF cue:** Our network uses filters built from spherical harmonics; due to the mathematical consequences of this filter choice, each layer accepts as input (and guarantees as ...

## Design Rationale

- **p. 1 / Abstract - extractive PDF cue:** In this paper, we present a family of networks that enjoy richer equivariance: the symmetries of 3D Euclidean space.
- **p. 1 / Abstract - extractive PDF cue:** We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.

## Source Evidence Cues

- **p. 1 / Abstract - extractive PDF cue:** We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.
- **p. 2 / Abstract - extractive PDF cue:** Equivariance confers three main benefits: First, this is more efficient than data augmentation to obtain 3D rotation-invariant output, making computation and training less expensive.
- **p. 2 / Abstract - extractive PDF cue:** We call these tensor field networks because every layer of our network inputs and outputs tensor fields: scalars, vectors, and higher-order tensors at every geometric ...
- **p. 1 / Abstract - extractive PDF cue:** 1 Motivation Convolutional neural networks are translation-equivariant, which means that features can be identified anywhere in a given input.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer. | p. 1 (Abstract), p. 2 (Abstract) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Equivariance confers three main benefits: First, this is more efficient than data augmentation to obtain 3D rotation-invariant output, making computation and training ... | p. 2 (Abstract), p. 2 (Abstract) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We call these tensor field networks because every layer of our network inputs and outputs tensor fields: scalars, vectors, and higher-order tensors ... | p. 2 (Abstract), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / Abstract - extractive PDF cue:** Work in progress. arXiv:1802.08219v3 [cs.LG] 18 May 2018
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | network, uses, filters, built, spherical, harmonics, mathematical, consequences, filter, choice, layer, accepts, input, guarantees | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | network, uses, filters, built, spherical, harmonics, mathematical, consequences, filter, choice | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, family, networks, enjoy, richer, equivariance, symmetries, Euclidean, space, introduce | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | progress, arXiv | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Abstract - extractive PDF cue:** Our network uses filters built from spherical harmonics; due to the mathematical consequences of this filter choice, each layer accepts as input (and guarantees as ...
- **p. 2 / Abstract - extractive PDF cue:** We call these tensor field networks because every layer of our network inputs and outputs tensor fields: scalars, vectors, and higher-order tensors at every geometric ...
- **p. 1 / Abstract - extractive PDF cue:** 1 Motivation Convolutional neural networks are translation-equivariant, which means that features can be identified anywhere in a given input.
- **p. 2 / Abstract - extractive PDF cue:** Equivariance confers three main benefits: First, this is more efficient than data augmentation to obtain 3D rotation-invariant output, making computation and training less expensive.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Our network uses filters built from spherical harmonics; due to the mathematical consequences of this filter choice, each layer accepts as input ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 2This is because the manifold of orthonormal frames at a point in 2D (the group O(2)) has dimension 1 and in 3D ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / Abstract - extractive PDF cue:** Equivariance confers three main benefits: First, this is more efficient than data augmentation to obtain 3D rotation-invariant output, making computation and training less expensive.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** introduce, tensor, field, neural, networks, locally, equivariant, rotations, translations, permutations, points, every, layer, Equivariance, confers, three, main, benefits, First, more.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We demonstrate the capabilities of tensor field networks with tasks in geometry, physics, and chemistry. | p. 1 (Abstract), p. 2 (Abstract) |
| Semantic / temporal fusion | This is significantly more important in 3D than in 2D: Without equivariant filters like those in our design, achieving an angular resolution ... | p. 2 (Abstract), p. 2 (Abstract) |
| Robot query / planning handoff | This capability has contributed significantly to their widespread success. | p. 1 (Abstract), p. 9 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 2 / Abstract - extractive PDF cue:** This is significantly more important in 3D than in 2D: Without equivariant filters like those in our design, achieving an angular resolution of δ would ...
- **p. 2 / Abstract - extractive PDF cue:** In this paper, we explain the mathematical conditions that such a 3D rotation- and translationequivariant network must satisfy, provide several examples of equivariant-compatible network components, ...
- **p. 1 / Abstract - extractive PDF cue:** 3D rotation equivariance removes the need for data augmentation to identify features in arbitrary orientations.
- **p. 1 / Abstract - extractive PDF cue:** 1 Motivation Convolutional neural networks are translation-equivariant, which means that features can be identified anywhere in a given input.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: A hypothetical example input and out- put of the missing point network. (A) A benzene molecule with hydrogen removed (B) The relative output ...
- **p. 7 / 2 Related work - extractive PDF cue:** Any network that relies solely upon distances (such as SchNet [2]) or angles between points (such as ANI-1 [15]) cannot distinguish these shapes, but ours ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 1 (Abstract), p. 2 (Abstract), p. 2 (Abstract), p. 1 (Abstract), objective p. 1 (Abstract), temporal p. 1 (Abstract), p. 2 (2 Related work), p. 3 (2 Related work), p. 6 (2 Related work), p. 6 (2 Related work), p. 7 (2 Related work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
