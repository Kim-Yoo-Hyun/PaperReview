# Method - AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_AutoOcc_Automatic_Open-Ended_Semantic_Occupancy_Annotation_via_Vision-Language_Guided_Gaussian_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_AutoOcc_Automatic_Open-Ended_Semantic_Occupancy_Annotation_via_Vision-Language_Guided_Gaussian_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Vision-Language Guidance), p. 4 (3.1. Vision-Language Guidance), p. 5 (3.2. VL-GS), p. 5 (3.2. VL-GS)): Specifically, we use the attention map generation method [1, 29] to compute and aggregate the attentions from transformer decoder, with N output tokens S = s1, · · · , ...

## Method Body Digest

- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** Specifically, we use the attention map generation method [1, 29] to compute and aggregate the attentions from transformer decoder, with N output tokens S = ...
- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** We then rasterize the attention maps corresponding to these semantic categories into 2D feature maps, with each category represented by an aggregated attention map M.
- **p. 5 / 3.2. VL-GS - extractive body cue:** We then implement a geometry-aware loss to enforce the alignment of Gaussian ellipsoid distributions with the geometric 3371
- **p. 5 / 3.2. VL-GS - extractive body cue:** Thus, we introduce a self-estimated 3D flow module, which is used to capture and aggregate dynamic objects.
- **p. 5 / 3.2. VL-GS - extractive body cue:** Our pipeline also supports the use of LiDAR to obtain geometric constraints and continuously optimize the distribution of Gaussians.
- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** Human annotations are both costly and labor-intensive.
- **p. 4 / 3. Method - extractive body cue:** Concurrently, our method supports LiDAR input, serving as a robust geometric prior constraint.
- **p. 6 / 3.2. VL-GS - extractive body cue:** Finally, we cumulatively splat VL-GS onto the voxel grid at an arbitrary voxel size, with each voxel's semantic label determined by weighting the occupied range ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions include: • We present AutoOcc, a vision-centric automatic annotation pipeline that supports open-ended semantic 3D occupancy label generation, based on vision-language guided ...
- **p. 5 / 3.2. VL-GS - extractive body cue:** Unlike dense voxels or point clouds, our method allows for representing regions of interest with sparse Gaussians, aided by scalability and semantic attention maps.
- **p. 2 / 1. Introduction - extractive body cue:** Our method further exhibits excellent open-ended and zero-shot generalization capabilities, as evidenced by cross-dataset experiments.

## Source Evidence Cues

- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** Specifically, we use the attention map generation method [1, 29] to compute and aggregate the attentions from transformer decoder, with N output tokens S = ...
- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** We then rasterize the attention maps corresponding to these semantic categories into 2D feature maps, with each category represented by an aggregated attention map M.
- **p. 5 / 3.2. VL-GS - extractive body cue:** We then implement a geometry-aware loss to enforce the alignment of Gaussian ellipsoid distributions with the geometric 3371
- **p. 5 / 3.2. VL-GS - extractive body cue:** Thus, we introduce a self-estimated 3D flow module, which is used to capture and aggregate dynamic objects.
- **Detected method headings:** 3. Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Specifically, we use the attention map generation method [1, 29] to compute and aggregate the attentions from transformer decoder, with N output ... | p. 4 (3.1. Vision-Language Guidance), p. 4 (3.1. Vision-Language Guidance) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We then rasterize the attention maps corresponding to these semantic categories into 2D feature maps, with each category represented by an aggregated ... | p. 4 (3.1. Vision-Language Guidance), p. 5 (3.2. VL-GS) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We then implement a geometry-aware loss to enforce the alignment of Gaussian ellipsoid distributions with the geometric 3371 | p. 5 (3.2. VL-GS), p. 5 (3.2. VL-GS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.2. VL-GS - extractive body cue:** Our pipeline also supports the use of LiDAR to obtain geometric constraints and continuously optimize the distribution of Gaussians.
- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** Human annotations are both costly and labor-intensive.
- **p. 4 / 3. Method - extractive body cue:** Concurrently, our method supports LiDAR input, serving as a robust geometric prior constraint.
- **p. 5 / 3.2. VL-GS - extractive body cue:** We then implement a geometry-aware loss to enforce the alignment of Gaussian ellipsoid distributions with the geometric 3371
- **p. 6 / 3.2. VL-GS - extractive body cue:** Finally, we cumulatively splat VL-GS onto the voxel grid at an arbitrary voxel size, with each voxel's semantic label determined by weighting the occupied range ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3. Method), p. 4 (3.1. Vision-Language Guidance), p. 5 (3.2. VL-GS), p. 5 (3.2. VL-GS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, multi-view, image, sequence, input, employ, fixed, text, prompt, enumerate, possible, objects, within, scene | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Given, multi-view, image, sequence, input, employ, fixed, text, prompt, enumerate | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, include, present, AutoOcc, vision-centric, automatic, annotation, pipeline, supports | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | pipeline, supports, LiDAR, obtain, geometric, constraints, continuously, optimize, distribution, Gaussians | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3. Method - extractive body cue:** Given a multi-view image sequence as input, we employ a fixed text prompt to enumerate all possible objects within the scene.
- **p. 4 / 3.1. Vision-Language Guidance - extractive body cue:** Specifically, we use the attention map generation method [1, 29] to compute and aggregate the attentions from transformer decoder, with N output tokens S = ...
- **p. 6 / 3.2. VL-GS - extractive body cue:** AutoOcc-V uses only images as input, while AutoOcc-M integrates both camera and LiDAR data.
- **p. 2 / 1. Introduction - extractive body cue:** Recent self-supervised occupancy models [4, 13, 14, 17, 59] have eliminated the need for extensive labeled training data by leveraging 2D features from image inputs ...
- **p. 2 / 1. Introduction - extractive body cue:** These annotation methods heavily rely on LiDAR point clouds while overlooking semantic and geometric cues from multiview images.
- **p. 5 / 3.2. VL-GS - extractive body cue:** Unlike dense voxels or point clouds, our method allows for representing regions of interest with sparse Gaussians, aided by scalability and semantic attention maps.
- **p. 6 / 3.2. VL-GS - extractive body cue:** For fair comparisions, we replicate SurroundOcc* [51] and OpenOcc* [49] by replacing the manually annotated results with the semantic point clouds projected from VLMs.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | For a fair comparison, we extend existing self-supervised approaches by incorporating image sequences as historical frames and performing multi-frame feature aggregation. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Given a multi-view image sequence as input, we employ a fixed text prompt to enumerate all possible objects within the scene. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | The learning rate for the position parameters decays every 250 steps with a decay rate of 0.98. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Specifically, attention, generation, compute, aggregate, attentions, transformer, decoder, output, tokens, tensor, heads, layers, begi, frac, prime, aligned, where, n-th, semantic.
- **Relevant PDF headings:** 3. Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We use two benchmarks for evaluation: Occ3D-nuScenes, which is used to compare the performance of our method with other occupancy annotation methods ... | p. 6 (4.1. Implementation Details), p. 7 (4.2. Performance Evaluation and Analysis) |
| Global / local decision | We evaluate our method against the state-of-the-art (SOTA) methods for automatic semantic occupancy annotation, including offline methods [32, 49, 51] and self-supervised ... | p. 6 (4.2. Performance Evaluation and Analysis), p. 6 (4.2. Performance Evaluation and Analysis) |
| Motion execution / recovery | As shown in Table 2, our vision-centric method outperforms these pipelines that utilize LiDAR point clouds. | p. 6 (4.2. Performance Evaluation and Analysis), p. 7 (4.2. Performance Evaluation and Analysis) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. AutoOcc is a fully automatic, vision-centric pipeline for open-ended semantic 3D occupancy annotation. Our method achieves more efficient and effective semantic occupancy auto-labeling ...
- **p. 6 / 4.1. Implementation Details - extractive body cue:** Similar to [59, 66], we evaluate without the "other" and "other flat" classes.
- **p. 7 / 4.2. Performance Evaluation and Analysis - extractive body cue:** Selfsupervised methods enable occupancy estimation from image features without relying on manual annotations.
- **p. 8 / 4.3. Zero-shot and Generalization Ability - extractive body cue:** Label-free means training without any human-labeled annotations. † indicates the use of VLMs to obtain 2D semantics instead of human labeling.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. The effect of each module in our method. SFM is short for the self-estimated flow module, and SSG denotes the employ- ment of ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1. Comparisons between AutoOcc and existing semantic occupancy annotation pipelines. The definitions of closed-set, open- set, and open-ended are introduced in Section 2. Our ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overall pipeline of our method. AutoOcc is a vision-centric automated pipeline for semantic occupancy annotation. Our method starts with multi-view image inputs (optionally ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.1. Vision-Language Guidance), p. 4 (3.1. Vision-Language Guidance), p. 5 (3.2. VL-GS), p. 5 (3.2. VL-GS), objective p. 5 (3.2. VL-GS), p. 4 (3.1. Vision-Language Guidance), p. 4 (3. Method), p. 5 (3.2. VL-GS), p. 6 (3.2. VL-GS), temporal p. 7 (4.2. Performance Evaluation and Analysis), p. 4 (3. Method), p. 4 (3.1. Vision-Language Guidance), p. 5 (3.2. VL-GS), p. 5 (3.2. VL-GS), p. 6 (4.1. Implementation Details).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
