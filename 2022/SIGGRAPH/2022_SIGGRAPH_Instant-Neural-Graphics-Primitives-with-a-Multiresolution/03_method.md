# Method - Instant Neural Graphics Primitives with a Multiresolution Hash Encoding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.05989; PDF retrieval source: https://arxiv.org/pdf/2201.05989. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 13 (B IMPLEMENTATION DETAILS OF NGLOD), p. 13 (B IMPLEMENTATION DETAILS OF NGLOD)): 2021] such that it closely resembles that of our hash encoding, only differing in the underlying data structure; i.e. using the vertices of an octree around ground-truth triangle mesh to ...

## Method Body Digest

- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive PDF cue:** 2021] such that it closely resembles that of our hash encoding, only differing in the underlying data structure; i.e. using the vertices of an octree ...
- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive PDF cue:** This results in a notable difference to the original NGLOD: the looked-up feature vectors are concatenated rather than summed, which in our implementation serendipitously resulted ...
- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive PDF cue:** The last point is important for two reasons: first, it matches the coarsest resolution of our hash tables 24 = 16 = 𝑁min, and second, ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** (4) Neural radiance and density fields (NeRF): the MLP learns the 3D density and 5D light field of a given scene from image observations and ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 2021], and to look-up and (optionally) interpolate these parameters depending on the input vector x ∈R𝑑.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** 2021] is trained to output dense feature grids in the leaf node around x.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** These are concatenated to form a 16-dimensional (same as (c)) input to the network.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** (4) we concatenate the result of each level, as well as auxiliary inputs 𝜉∈R𝐸, producing the encoded MLP input 𝑦∈R𝐿𝐹+𝐸, which (5) is evaluated last.

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** Our method-Figure 2 (e,f)-combines both ideas to reduce waste.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** To illustrate the trade-offs and to motivate our method, Figure 2 shows the effect on reconstruction quality of a neural radiance field for several different ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** This enables the use of smaller, more efficient MLPs.

## Source Evidence Cues

- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive PDF cue:** 2021] such that it closely resembles that of our hash encoding, only differing in the underlying data structure; i.e. using the vertices of an octree ...
- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive PDF cue:** This results in a notable difference to the original NGLOD: the looked-up feature vectors are concatenated rather than summed, which in our implementation serendipitously resulted ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | 2021] such that it closely resembles that of our hash encoding, only differing in the underlying data structure; i.e. using the vertices ... | p. 13 (B IMPLEMENTATION DETAILS OF NGLOD), p. 13 (B IMPLEMENTATION DETAILS OF NGLOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | This results in a notable difference to the original NGLOD: the looked-up feature vectors are concatenated rather than summed, which in our ... | p. 13 (B IMPLEMENTATION DETAILS OF NGLOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 2021] such that it closely resembles that of our hash encoding, only differing in the underlying data structure; i.e. using the vertices ... | p. 13 (B IMPLEMENTATION DETAILS OF NGLOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive PDF cue:** The last point is important for two reasons: first, it matches the coarsest resolution of our hash tables 24 = 16 = 𝑁min, and second, ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 13 (B IMPLEMENTATION DETAILS OF NGLOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Neural, radiance, density, fields, NeRF, MLP, learns, light, field, given, scene, image, observations, corresponding | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Neural, radiance, density, fields, NeRF, MLP, learns, light, field, given | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | method-Figure, combines, ideas, reduce, waste, illustrate, trade-offs, motivate, Figure, effect | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | last, point, important, reasons, first, matches, coarsest, resolution, hash, tables | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** (4) Neural radiance and density fields (NeRF): the MLP learns the 3D density and 5D light field of a given scene from image observations and ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 2021], and to look-up and (optionally) interpolate these parameters depending on the input vector x ∈R𝑑.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** 2021] is trained to output dense feature grids in the leaf node around x.
- **p. 3 / 1 INTRODUCTION - extractive PDF cue:** These are concatenated to form a 16-dimensional (same as (c)) input to the network.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** (4) we concatenate the result of each level, as well as auxiliary inputs 𝜉∈R𝐸, producing the encoded MLP input 𝑦∈R𝐿𝐹+𝐸, which (5) is evaluated last.
- **p. 4 / 1 INTRODUCTION - extractive PDF cue:** (1) for a given input coordinate x, we find the surrounding voxels at 𝐿resolution levels and assign indices to their corners by hashing their integer ...
- **p. 5 / 1 INTRODUCTION - extractive PDF cue:** The plot also shows model convergence over time leading up to the final state.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Neural radiance caching is a challenging application, because it is supervised online during real-time rendering. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Bearded Man ©Oliver Laric (CC BY-NC-SA 2.0) Feature buffers 𝑚 enc(𝑥;𝜃); Φ Predicted color Online supervised training Real-time sparse path tracer Fig. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | [2021]-our encoding results in sharper reconstruction while incurring only a mild performance overhead of 0.7 ms that reduces the frame rate from ... | hardware, batch and throughput |

## Training vs Inference

- **p. 13 / B IMPLEMENTATION DETAILS OF NGLOD - extractive PDF cue:** This results in a notable difference to the original NGLOD: the looked-up feature vectors are concatenated rather than summed, which in our implementation serendipitously resulted ...
- **p. 9 / 24.2 M - extractive PDF cue:** The effect of the MLP size on test error vs. training time (31 000 training steps) on the Lego scene.
- **p. 9 / 24.2 M - extractive PDF cue:** Informed by this analysis, we choose 𝑁layers = 2 and 𝑁neurons = 64. of the finest grid resolution, which is absent in NGLOD and does ...
- **p. 8 / 24.2 M - extractive PDF cue:** Neural signed distance functions trained for 11 000 steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** closely, resembles, hash, encoding, only, differing, underlying, data, structure, vertices, octree, around, ground-truth, triangle, mesh, store, collision-free, feature, vectors, rather.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | At HD resolutions, synthetic and even real-world scenes can be trained in seconds and rendered at 60 FPS, without the need of ... | p. 9 (24.2 M), p. 7 (5 EXPERIMENTS) |
| Semantic / temporal fusion | As baseline, we compare with NGLOD [Takikawa et al. | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Robot query / planning handoff | It approaches NeRF's quality after training for just ∼5 min, yet is outperformed by our full method after training for 5 s-15 ... | p. 10 (24.2 M), p. 9 (24.2 M) |

## Failure and Ablation Link

- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 12. NeRF reconstruction of a modular synthesizer and large natural 360 scene. The left image took 5 seconds to accumulate 128 samples at 1080p ...
- **p. 9 / 24.2 M - extractive PDF cue:** The effect of the MLP size on test error vs. training time (31 000 training steps) on the Lego scene.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** This sensitivity reveals undesired microstructure in our hash encoding on the scale 2IoU is the ratio of volumes of the interiors of the intersection and ...
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** However, even without such a dedicated data structure, our encoding approaches a similar fidelity to NGLOD in terms of the intersectionover-union metric (IoU2) with similar ...
- **p. 9 / 24.2 M - extractive PDF cue:** At HD resolutions, synthetic and even real-world scenes can be trained in seconds and rendered at 60 FPS, without the need of caching of the ...
- **p. 10 / 24.2 M - extractive PDF cue:** It could thus keep improving slightly if trained for extended periods of time, as in the offline NeRF variants that are often trained for several ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 2. A demonstration of the reconstruction quality of different encodings and parametric data structures for storing trainable feature embeddings. Each configuration was trained for ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 13 (B IMPLEMENTATION DETAILS OF NGLOD), p. 13 (B IMPLEMENTATION DETAILS OF NGLOD), objective p. 13 (B IMPLEMENTATION DETAILS OF NGLOD), temporal p. 8 (24.2 M), p. 8 (24.2 M), p. 9 (24.2 M), p. 10 (24.2 M), p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
