# Method - SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2006.10503; PDF retrieval source: https://arxiv.org/pdf/2006.10503. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method)): These weights are SE(3)-invariant due to the invariance of inner products of features, transforming under the same representation. wℓℓ i,c′c = MLP  M c,c′ fℓ⊤ in,i,c′fℓ in,i,c   ...

## Method Body Digest

- **p. 6 / 3 Method - extractive body cue:** These weights are SE(3)-invariant due to the invariance of inner products of features, transforming under the same representation. wℓℓ i,c′c = MLP  M c,c′ ...
- **p. 6 / 3 Method - extractive body cue:** Channels, Self-interaction Layers, and Non-Linearities Analogous to conventional neural networks, the SE(3)-Transformer can straightforwardly be extended to multiple channels per representation degree ℓ, so far ...
- **p. 5 / 3 Method - extractive body cue:** 3.2 The SE(3)-Transformer The SE(3)-Transformer itself consists of three components.
- **p. 5 / 3 Method - extractive body cue:** If we remove the attention weights then we have a tensor field convolution, and if we instead remove the dependence of WV on (xj -xi), ...
- **p. 7 / 3 Method - extractive body cue:** Linear DeepSet [46] Tensor Field [28] Set Transformer [16] SE(3)-Transformer MSE x 0.0691 0.0639 0.0151 0.0139 0.0076 Position std - 0.0086 0.0011 0.0004 0.0002 ∆EQ ...
- **p. 1 / 1 Introduction - extractive body cue:** Furthermore, an important property is that these structures should be invariant to global changes in overall input pose; that is, 3D translations and rotations of ...
- **p. 6 / 3 Method - extractive body cue:** [25], output channels are a learned linear combination of input channels using one set of weights wℓℓ i,c′c = wℓℓ c′c per representation degree, shared ...
- **p. 5 / 3 Method - extractive body cue:** (7), and 3) a linear/attentive self-interaction layer.

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we propose the SE(3)-Transformer shown in Fig.
- **p. 5 / 3 Method - extractive body cue:** Here, we present the SE(3)-Transformer.
- **p. 5 / 3 Method - extractive body cue:** This mechanism consists of a normalised inner product between a query vector qi 5

## Source Evidence Cues

- **p. 6 / 3 Method - extractive body cue:** These weights are SE(3)-invariant due to the invariance of inner products of features, transforming under the same representation. wℓℓ i,c′c = MLP  M c,c′ ...
- **p. 6 / 3 Method - extractive body cue:** Channels, Self-interaction Layers, and Non-Linearities Analogous to conventional neural networks, the SE(3)-Transformer can straightforwardly be extended to multiple channels per representation degree ℓ, so far ...
- **p. 5 / 3 Method - extractive body cue:** 3.2 The SE(3)-Transformer The SE(3)-Transformer itself consists of three components.
- **p. 5 / 3 Method - extractive body cue:** If we remove the attention weights then we have a tensor field convolution, and if we instead remove the dependence of WV on (xj -xi), ...
- **p. 7 / 3 Method - extractive body cue:** Linear DeepSet [46] Tensor Field [28] Set Transformer [16] SE(3)-Transformer MSE x 0.0691 0.0639 0.0151 0.0139 0.0076 Position std - 0.0086 0.0011 0.0004 0.0002 ∆EQ ...
- **Detected method headings:** 3 Method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | These weights are SE(3)-invariant due to the invariance of inner products of features, transforming under the same representation. wℓℓ i,c′c = MLP ... | p. 6 (3 Method), p. 6 (3 Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Channels, Self-interaction Layers, and Non-Linearities Analogous to conventional neural networks, the SE(3)-Transformer can straightforwardly be extended to multiple channels per representation degree ... | p. 6 (3 Method), p. 5 (3 Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 3.2 The SE(3)-Transformer The SE(3)-Transformer itself consists of three components. | p. 5 (3 Method), p. 5 (3 Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Furthermore, important, property, structures, should, invariant, global, changes, overall, input, pose, translations, rotations, point | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Furthermore, important, property, structures, should, invariant, global, changes, overall, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Transformer, Fig, Here, present, mechanism, consists, normalised, inner, product, between | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | not recovered | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1 Introduction - extractive body cue:** Furthermore, an important property is that these structures should be invariant to global changes in overall input pose; that is, 3D translations and rotations of ...
- **p. 6 / 3 Method - extractive body cue:** [25], output channels are a learned linear combination of input channels using one set of weights wℓℓ i,c′c = wℓℓ c′c per representation degree, shared ...
- **p. 6 / 3 Method - extractive body cue:** These weights are SE(3)-invariant due to the invariance of inner products of features, transforming under the same representation. wℓℓ i,c′c = MLP  M c,c′ ...
- **p. 5 / 3 Method - extractive body cue:** (7), and 3) a linear/attentive self-interaction layer.
- **p. 5 / 3 Method - extractive body cue:** Attention is performed on a per-neighbourhood basis as follows: fℓ out,i = Wℓℓ V fℓ in,i / {z } 3 ⃝self-interaction + X k≥0 X ...
- **p. 1 / 1 Introduction - extractive body cue:** Finding neural structures which can adapt to the varying number of points in an input, while respecting the irregular sampling of point positions, is challenging.
- **p. 7 / 3 Method - extractive body cue:** Linear DeepSet [46] Tensor Field [28] Set Transformer [16] SE(3)-Transformer MSE x 0.0691 0.0639 0.0151 0.0139 0.0076 Position std - 0.0086 0.0011 0.0004 0.0002 ∆EQ ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The input to the network is the position of a particle in a specific time step, its velocity, and its charge. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The task of the algorithm is then to predict the relative location and velocity 500 time steps into the future. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The right-hand plots show predicted locations and velocities for rotations of the input in steps of 10 degrees. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** weights, invariant, invariance, inner, products, features, transforming, under, same, representation, MLP, Node, Edge, Point, cloud, data, often, information, attached, points.
- **Relevant PDF headings:** 3 Method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To test our method, we choose ScanObjectNN, a recently introduced dataset for real-world object classification. | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Semantic / temporal fusion | We compare to publicly available, state-of-the-art results as well as a set of our own baselines. | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Robot query / planning handoff | If both training and test set are not rotated (x = 0 in a), breaking the symmetry of the SE(3)-Transformer by providing ... | p. 8 (4 Experiments), p. 7 (4 Experiments) |

## Failure and Ablation Link

- **p. 8 / 4 Experiments - extractive body cue:** Our method sets itself apart by using roto-translation equivariant layers acting directly on the point cloud without prior projection onto a sphere [22, 45, 7].
- **p. 8 / 4 Experiments - extractive body cue:** We create an SO(2) invariant version of our algorithm by additionally feeding the z-component as an type-0 field and the x, y position as an ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: A) Each layer of the SE(3)-Transformer maps from a point cloud to a point cloud (or graph to graph) while guaranteeing equivariance. For ...
- **p. 7 / 4 Experiments - extractive body cue:** The dashed curves show the predicted locations of a perfectly equivariant model.
- **p. 7 / 4 Experiments - extractive body cue:** The N-body problem is an equivariant task: rotation of the input should result in rotated predictions of locations and velocities of the particles.
- **p. 9 / 4 Experiments - extractive body cue:** The table is split into non-equivariant (top) and equivariant models (bottom).
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Updating the node features using our equivariant attention mechanism in four steps. A more detailed description, especially of step 2, is provided in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3 Method), p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 7 (3 Method), objective 본문 anchor 없음, temporal p. 7 (4 Experiments), p. 7 (4 Experiments), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
