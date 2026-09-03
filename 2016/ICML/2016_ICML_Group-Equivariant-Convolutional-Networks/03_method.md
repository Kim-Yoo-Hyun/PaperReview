# Method - Group Equivariant Convolutional Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1602.07576; PDF retrieval source: https://arxiv.org/pdf/1602.07576. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (7. Efficient Implementation), p. 7 (7.2. Planar convolution), p. 7 (7.1. Filter transformation)): The computational cost of the algorithm presented here is roughly equal to that of a planar convolution with a filter bank that is the same size as the augmented filter ...

## Method Body Digest

- **p. 6 / 7. Efficient Implementation - extractive body cue:** The computational cost of the algorithm presented here is roughly equal to that of a planar convolution with a filter bank that is the same ...
- **p. 7 / 7.2. Planar convolution - extractive body cue:** The second part of the G-convolution algorithm is a planar convolution using the expanded filter bank F +.
- **p. 7 / 7.1. Filter transformation - extractive body cue:** Group Equivariant Convolutional Networks channels at layer l, Sl-1 denotes the number of transformations in G that leave the origin invariant (e.g.
- **p. 7 / 7.2. Planar convolution - extractive body cue:** The resulting array can be interpreted as a conventional filter bank with Sl-1Kl-1 planar input channels and SlKl planar output channels, which can be correlated ...
- **p. 7 / 7.1. Filter transformation - extractive body cue:** To precompute the indices, we define an invertible map g(s, u, v) that takes an input index (valid for an array of shape Sl-1 × ...
- **p. 1 / 1. Introduction - extractive body cue:** Deep convolutional neural networks (CNNs, convnets) have proven to be very powerful models of sensory data such as images, video, and audio.
- **p. 1 / 1. Introduction - extractive body cue:** By using the same weights to analyze or model each part of the image, a convolution layer uses far fewer parameters than a fully connected ...
- **p. 6 / 7. Efficient Implementation - extractive body cue:** A plane symmetry group G is called split if any transformation g ∈G can be decomposed into a translation t ∈Z2 and a transformation s ...

## Design Rationale

- **p. 6 / 7. Efficient Implementation - extractive body cue:** Here we present the details for a G-convolution implementation that can leverage recent advances in fast computation of planar convolutions (Mathieu et al., 2014; Vasilache ...

## Source Evidence Cues

- **p. 6 / 7. Efficient Implementation - extractive body cue:** The computational cost of the algorithm presented here is roughly equal to that of a planar convolution with a filter bank that is the same ...
- **p. 7 / 7.2. Planar convolution - extractive body cue:** The second part of the G-convolution algorithm is a planar convolution using the expanded filter bank F +.
- **p. 7 / 7.1. Filter transformation - extractive body cue:** Group Equivariant Convolutional Networks channels at layer l, Sl-1 denotes the number of transformations in G that leave the origin invariant (e.g.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The computational cost of the algorithm presented here is roughly equal to that of a planar convolution with a filter bank that ... | p. 6 (7. Efficient Implementation), p. 7 (7.2. Planar convolution) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The second part of the G-convolution algorithm is a planar convolution using the expanded filter bank F +. | p. 7 (7.2. Planar convolution), p. 7 (7.1. Filter transformation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Group Equivariant Convolutional Networks channels at layer l, Sl-1 denotes the number of transformations in G that leave the origin invariant (e.g. | p. 7 (7.1. Filter transformation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 7. Efficient Implementation - extractive body cue:** The computational cost of the algorithm presented here is roughly equal to that of a planar convolution with a filter bank that is the same ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | resulting, array, interpreted, conventional, filter, bank, Sl-1Kl-1, planar, input, channels, SlKl, output, correlated, feature | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | resulting, array, interpreted, conventional, filter, bank, Sl-1Kl-1, planar, input, channels | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Here, present, details, G-convolution, implementation, leverage, recent, advances, fast, computation | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | computational, cost, algorithm, presented, here, roughly, equal, planar, convolution, filter | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 7.2. Planar convolution - extractive body cue:** The resulting array can be interpreted as a conventional filter bank with Sl-1Kl-1 planar input channels and SlKl planar output channels, which can be correlated ...
- **p. 7 / 7.1. Filter transformation - extractive body cue:** To precompute the indices, we define an invertible map g(s, u, v) that takes an input index (valid for an array of shape Sl-1 × ...
- **p. 1 / 1. Introduction - extractive body cue:** Deep convolutional neural networks (CNNs, convnets) have proven to be very powerful models of sensory data such as images, video, and audio.
- **p. 1 / 1. Introduction - extractive body cue:** By using the same weights to analyze or model each part of the image, a convolution layer uses far fewer parameters than a fully connected ...
- **p. 6 / 7. Efficient Implementation - extractive body cue:** A plane symmetry group G is called split if any transformation g ∈G can be decomposed into a translation t ∈Z2 and a transformation s ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | (2015), which consists of a sequence of 9 strided and non-strided convolution layers, interspersed with rectified linear activation units, and nothing else. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The latter denotes moderate data augmentation with horizontal flips and small translations, following Goodfellow et al. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The learning rate was divided by 10 at epoch 50, 100 and 150, and training was continued for 300 epochs. | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 8.1. Rotated MNIST - extractive body cue:** The learning rate was divided by 10 at epoch 50, 100 and 150, and training was continued for 300 epochs.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** computational, cost, algorithm, presented, here, roughly, equal, planar, convolution, filter, bank, same, size, augmented, G-convolution, because, transformation, negligible, second, part.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The dataset is split into a training, validation and test sets of size 10000, 2000 and 50000, respectively. | p. 7 (8.1. Rotated MNIST), p. 7 (8.1. Rotated MNIST) |
| Semantic / temporal fusion | This baseline architecture outperforms the models tested by Larochelle et al. | p. 7 (8.1. Rotated MNIST), p. 7 (8.1. Rotated MNIST) |
| Robot query / planning handoff | This network (P4CNNRotationPooling) outperforms the baseline and the previous state of the art, but performs significantly worse than the P4CNN which does ... | p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST) |

## Failure and Ablation Link

- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** This architecture (P4CNN) was found to perform better without dropout, so we removed it.
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** The resulting feature maps consist of rotationinvariant features, and have the same transformation law as the input image.
- **p. 8 / 8.1. Rotated MNIST - extractive body cue:** Group Equivariant Convolutional Networks the baseline architectures by p4 or p4m convolutions.
- **p. 8 / 8.1. Rotated MNIST - extractive body cue:** This way, the number of parameters is left approximately invariant, while the size of the internal representation is increased.
- **p. 6 / 7. Efficient Implementation - extractive body cue:** A plane symmetry group G is called split if any transformation g ∈G can be decomposed into a translation t ∈Z2 and a transformation s ...
- **p. 8 / 9. Discussion & Future work - extractive body cue:** One limitation of the method as presented here is that it only works for discrete groups.
- **p. 8 / 9. Discussion & Future work - extractive body cue:** In future work, we want to implement G-CNNs that work on hexagonal lattices which have an increased number of symmetries relative to square grids, as ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (7. Efficient Implementation), p. 7 (7.2. Planar convolution), p. 7 (7.1. Filter transformation), objective p. 6 (7. Efficient Implementation), temporal p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST), p. 1 (48.
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
