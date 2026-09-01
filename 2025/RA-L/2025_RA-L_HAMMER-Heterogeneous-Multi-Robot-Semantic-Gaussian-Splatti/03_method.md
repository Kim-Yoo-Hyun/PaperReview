# Method - HAMMER: Heterogeneous, Multi-Robot Semantic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2501.14147; PDF retrieval source: https://arxiv.org/pdf/2501.14147. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD)): If the fraction of matched features exceeds a fixed ratio ξ = 0.25 then the image pair is accepted as a potential inter-robot correspondence.

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** If the fraction of matched features exceeds a fixed ratio ξ = 0.25 then the image pair is accepted as a potential inter-robot correspondence.
- **p. 3 / III. METHOD - extractive body cue:** To perform SfM, we use the COLMAP backend [18] with SuperPoint features and the SuperGlue matcher [28], which have exhibited robustness in aligning images from ...
- **p. 4 / III. METHOD - extractive body cue:** 1) Representation: 3DGS models the opacity and color of the environment using explicit Gaussian primitives, which are optimized based on a differentiable, tile-based rasterization process ...
- **p. 4 / III. METHOD - extractive body cue:** The point cloud is then directly used to supervise the feature field.
- **p. 5 / III. METHOD - extractive body cue:** To combat this deficiency, in addition to optimizing the scene parameters, HAMMER treats the SLAM pose and the localto-world transform T j →T g as ...
- **p. 5 / III. METHOD - extractive body cue:** When depth images are available, HAMMER adds depth-supervision to the existing color photometric loss.
- **p. 3 / III. METHOD - extractive body cue:** Equation (1) optimizes the scaling, rotation, and translation (s, R, t) between the two frames with a small regularization term on the rotation to address ...
- **p. 3 / III. METHOD - extractive body cue:** Therefore, although alignment is costly, it is a one-time cost to produce the transform T j →T g.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** A server-based architecture allows our method to be used with existing robot and edge device hardware without highpowered GPUs, while leveraging typical communication infrastructure (e.g.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose HAMMER, Heterogeneous Asynchronous Multi-robot Mapping of Environmental Radiance.
- **p. 1 / I. INTRODUCTION - extractive body cue:** HAMMER enables a server communicating with a team of robots to construct a joint 3DGS map of an unknown environment.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** If the fraction of matched features exceeds a fixed ratio ξ = 0.25 then the image pair is accepted as a potential inter-robot correspondence.
- **p. 3 / III. METHOD - extractive body cue:** To perform SfM, we use the COLMAP backend [18] with SuperPoint features and the SuperGlue matcher [28], which have exhibited robustness in aligning images from ...
- **p. 4 / III. METHOD - extractive body cue:** 1) Representation: 3DGS models the opacity and color of the environment using explicit Gaussian primitives, which are optimized based on a differentiable, tile-based rasterization process ...
- **p. 4 / III. METHOD - extractive body cue:** The point cloud is then directly used to supervise the feature field.
- **p. 5 / III. METHOD - extractive body cue:** To combat this deficiency, in addition to optimizing the scene parameters, HAMMER treats the SLAM pose and the localto-world transform T j →T g as ...
- **p. 5 / III. METHOD - extractive body cue:** When depth images are available, HAMMER adds depth-supervision to the existing color photometric loss.
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | If the fraction of matched features exceeds a fixed ratio ξ = 0.25 then the image pair is accepted as a potential ... | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To perform SfM, we use the COLMAP backend [18] with SuperPoint features and the SuperGlue matcher [28], which have exhibited robustness in ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 1) Representation: 3DGS models the opacity and color of the environment using explicit Gaussian primitives, which are optimized based on a differentiable, ... | p. 4 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** Equation (1) optimizes the scaling, rotation, and translation (s, R, t) between the two frames with a small regularization term on the rotation to address ...
- **p. 4 / III. METHOD - extractive body cue:** 1) Representation: 3DGS models the opacity and color of the environment using explicit Gaussian primitives, which are optimized based on a differentiable, tile-based rasterization process ...
- **p. 3 / III. METHOD - extractive body cue:** Therefore, although alignment is costly, it is a one-time cost to produce the transform T j →T g.
- **p. 4 / III. METHOD - extractive body cue:** Some works [34] augment the parameters of each Gaussian with a semantic channel and regress it directly from an image reconstruction loss.
- **p. 5 / III. METHOD - extractive body cue:** When depth images are available, HAMMER adds depth-supervision to the existing color photometric loss.
- **p. 5 / III. METHOD - extractive body cue:** The depth loss helps improve the geometry of the map in regions of visual ambiguity (e.g. monochromatic flat surfaces).
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | During, runtime, HAMMER, rejects, alignments, where, localized, SfM, fails, estimate, poses, input, images, have | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | During, runtime, HAMMER, rejects, alignments, where, localized, SfM, fails, estimate | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | server-based, architecture, allows, existing, robot, edge, device, hardware, without, highpowered | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Equation, optimizes, scaling, rotation, translation, between, frames, small, regularization, term | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive body cue:** During runtime, HAMMER rejects alignments where the localized SfM fails to estimate poses for all 2W input images or alignments that have high translation (0.1m ...
- **p. 2 / III. METHOD - extractive body cue:** Each robot produces color images, geometric information (e.g. depth images or point clouds), and camera pose estimates in SE(3) with respect to an arbitrary local ...
- **p. 3 / III. METHOD - extractive body cue:** Importantly, the process treats the onboard localization algorithms as black-boxes and only uses the resulting camera poses and color images as input.
- **p. 2 / I. INTRODUCTION - extractive body cue:** 1) are (1) a robust and metric inter-robot frame alignment using RGB images to align coordinate systems across devices with different image sensors and SLAM ...
- **p. 4 / III. METHOD - extractive body cue:** Specifically, if a depth image is received, then the camera intrinsics and pose are used to project random pixels into 3D to create a sparse ...
- **p. 4 / III. METHOD - extractive body cue:** For each message sent by aligned robots, HAMMER initializes the Gaussian geometric parameters (i.e. µk, Σk) based on the pose and geometric data (i.e. depth ...
- **p. 5 / III. METHOD - extractive body cue:** The attribution meshes show the part of the map contributed by each robot: Aria 1 (red), Aria 2 (green), GR 1 (orange), and GR 2 ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Their deployments can be asynchronous, potentially lacking any temporal overlap between individual robot deployments. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The goal is to continuously incorporate every robot's data into the 3DGS map within a consistent global coordinate frame T g. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The mapping server is a desktop computer with a NVIDIA RTX 4090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / III. METHOD - extractive body cue:** To combat this deficiency, in addition to optimizing the scene parameters, HAMMER treats the SLAM pose and the localto-world transform T j →T g as ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** fraction, matched, features, exceeds, fixed, ratio, then, image, pair, accepted, potential, inter-robot, correspondence, perform, SfM, COLMAP, backend, SuperPoint, SuperGlue, matcher.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | However, ReplicaMultiAgent only contains scenes from simulated environments, and lacks heterogeneous robots/sensing devices and challenging real-world scene conditions (e.g. motion blur, diverse ... | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Semantic / temporal fusion | Fig. 5: Map quality over time for HAMMER and baselines in two scenes. HAMMER outperforms Di-NeRF*, demonstrating the necessity of accurate robot ... | p. 7 (Figure/Table caption), p. 5 (IV. EXPERIMENTS) |
| Robot query / planning handoff | HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** 4) compared to Di-NeRF*, which fails to resolve robot alignments and therefore cannot accurately match the ground-truth images.
- **p. 5 / III. METHOD - extractive body cue:** 3) Pose Refinement: Although the alignment module produces robust estimates of the local-to-world transforms, it cannot account for gradual drift or other temporal noise.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** HAMMER dramatically outperforms Di-NeRF* which fails to converge to accurate inter-robot alignments.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), objective p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD), temporal p. 2 (III. METHOD), p. 2 (III. METHOD), p. 1 (Abstract), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
