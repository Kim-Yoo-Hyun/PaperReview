# Method - SplatFormer: Point Transformer for Robust 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=9NfHbWKqMF; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/111734. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 15 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS), p. 15 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS), p. 17 (B IMPLEMENTATION DETAILS), p. 17 (B IMPLEMENTATION DETAILS)): The feature decoder is composed of five separate MLP branches, which are responsible for predicting the residuals for the means, opacity, quaternion, scales, and spherical harmonics coefficients.

## Method Body Digest

- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** The feature decoder is composed of five separate MLP branches, which are responsible for predicting the residuals for the means, opacity, quaternion, scales, and spherical ...
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** For the training of our full model, we use 8 RTX4090s with one scene per GPU, set gradient accumulation steps as 4, and train for ...
- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** The point transformer encoder begins with an MLP embedding layer, followed by five down-pooling and four up-pooling stages, ultimately producing features with a dimensionality of ...
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** It takes 2 days to generate each training dataset.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive body cue:** The primary computational bottleneck still lies in the training stage.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive body cue:** Further improving the efficiency of point transformer for large-scale unbounded scenes remains an important direction for future work.
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** To reduce computational costs, we terminate the optimization early at 10k steps, where evaluation performance levels off.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** It outputs residuals that are added to the input Gaussian attributes.

## Design Rationale

- **p. 3 / 1 INTRODUCTION - extractive body cue:** In summary, we make the following contributions: • We introduce OOD-NVS, a new experimental protocol specifically designed to evaluate the performance of NVS methods when ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To meet these needs, we propose SplatFormer, a novel learning-based feed-forward 3D transformer designed to operate on Gaussian splats.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Existing NVS methods, including MipNeRF360 (Barron et al., 2022), and those designed for sparse inputs like LaRa (Chen et al., 2024a), face challenges in this ...

## Source Evidence Cues

- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** The feature decoder is composed of five separate MLP branches, which are responsible for predicting the residuals for the means, opacity, quaternion, scales, and spherical ...
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** For the training of our full model, we use 8 RTX4090s with one scene per GPU, set gradient accumulation steps as 4, and train for ...
- **p. 15 / B IMPLEMENTATION DETAILS - extractive body cue:** The point transformer encoder begins with an MLP embedding layer, followed by five down-pooling and four up-pooling stages, ultimately producing features with a dimensionality of ...
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** It takes 2 days to generate each training dataset.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive body cue:** The primary computational bottleneck still lies in the training stage.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive body cue:** Further improving the efficiency of point transformer for large-scale unbounded scenes remains an important direction for future work.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The feature decoder is composed of five separate MLP branches, which are responsible for predicting the residuals for the means, opacity, quaternion, ... | p. 15 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | For the training of our full model, we use 8 RTX4090s with one scene per GPU, set gradient accumulation steps as 4, ... | p. 16 (B IMPLEMENTATION DETAILS), p. 15 (B IMPLEMENTATION DETAILS) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The point transformer encoder begins with an MLP embedding layer, followed by five down-pooling and four up-pooling stages, ultimately producing features with ... | p. 15 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** To reduce computational costs, we terminate the optimization early at 10k steps, where evaluation performance levels off.
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** For the training of our full model, we use 8 RTX4090s with one scene per GPU, set gradient accumulation steps as 4, and train for ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 16 (B IMPLEMENTATION DETAILS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | outputs, residuals, added, input, Gaussian, attributes, While, initial, representation, effectively, integrates, multi-view, information, captured | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | outputs, residuals, added, input, Gaussian, attributes, While, initial, representation, effectively | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, make, following, contributions, introduce, OOD-NVS, experimental, protocol, specifically, designed | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | reduce, computational, costs, terminate, optimization, early, steps, where, evaluation, performance | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1 INTRODUCTION - extractive body cue:** It outputs residuals that are added to the input Gaussian attributes.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** While this initial 3D representation effectively integrates multi-view information from the captured images, we observe that the shapes, appearances, and spatial structure of the Gaussian ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Additionally, some feed-forward models predict 3D primitives from a few input views (Chen et al., 2024a;b; Yu et al., 2021), yet they handle no more ...
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** For each scene, we render 4 target images at each iteration, with 70% OOD views and 30% input views, for photometric supervision.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Traditionally, this problem has been approached using a standard novel view interpolation protocol, where test views are sampled at fixed intervals along the trajectory of ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, AR and VR applications require not only smooth transitions between input views but also the ability to explore novel regions of interest from viewing ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** This often results in elongated Gaussian splats that cover only the thin areas projected on the input views, leading to sparse surface coverage.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For LaRa, which is limited to four input views due to memory constraints, we chose four large-baseline views to maximize scene coverage. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The camera takes Nin photos from evenly spaced azimuths, with its elevation following a sinusoidal pattern defined by frequency f and maximal ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | For LaRa, which is limited to four input views due to memory constraints, we chose four large-baseline views to maximize scene coverage. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Regarding SplatFormer's inference efficiency, most input splats in our object-centric test sets contain 70k-100k gaussians, requiring only 900MB of GPU memory for ... | hardware, batch and throughput |

## Training vs Inference

- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** For the training of our full model, we use 8 RTX4090s with one scene per GPU, set gradient accumulation steps as 4, and train for ...
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** It takes 2 days to generate each training dataset.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive body cue:** The primary computational bottleneck still lies in the training stage.
- **p. 17 / B IMPLEMENTATION DETAILS - extractive body cue:** Regarding SplatFormer's inference efficiency, most input splats in our object-centric test sets contain 70k-100k gaussians, requiring only 900MB of GPU memory for one feed-forward inference ...
- **p. 16 / B IMPLEMENTATION DETAILS - extractive body cue:** For the training of our full model, we use 8 RTX4090s with one scene per GPU, set gradient accumulation steps as 4, and train for ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** feature, decoder, composed, five, separate, MLP, branches, responsible, predicting, residuals, means, opacity, quaternion, scales, spherical, harmonics, coefficients, training, full, model.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Following the OOD-NVS protocol, we rendered 20 objects from Google Scanned Objects (GSO) (Downs et al., 2022) and captured 4 real-world scenes. | p. 9 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS) |
| Semantic / temporal fusion | Our method also outperforms MipNeRF360 and 2DGS, the best-performing baselines in Objaverse-OOD (Tab. | p. 10 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |
| Robot query / planning handoff | While our method still faces challenges with high-frequency texture details, it outperforms previous approaches in terms of fidelity and consistency in out-of-distribution ... | p. 9 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Next, we examine regularized 3DGS variants without external priors, including 2DGS (Huang et al., 2024a) and SplatFields (Mihajlovic et al., 2024).
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** These improvements are reflected in the SSIM and LPIPS metrics, though we observed rather minimal improvements in PSNR, which we attribute to the pixelwise PSNR's ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** 4, we train a variant that directly predicts the full 3DGS attributes (direct component).
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Next, we present the results on OOD-NVS, crossdataset generalization, and ablation studies.
- **p. 10 / 6 CONCLUSION - extractive body cue:** In this work, we introduced a new out-of-distribution (OOD) novel view synthesis test scenario and demonstrated that most neural rendering methods, including those using regularization ...
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** Our method has several limitations that provide directions for future work.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Limitations of 3DGS in OOD-NVS setup. We observe that the quality of novel views obtained via 3DGS significantly deteriorates as the test camera ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 15 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS), p. 15 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS), p. 17 (B IMPLEMENTATION DETAILS), p. 17 (B IMPLEMENTATION DETAILS), objective p. 16 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS), temporal p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 16 (B IMPLEMENTATION DETAILS), p. 16 (B IMPLEMENTATION DETAILS), p. 17 (B IMPLEMENTATION DETAILS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
