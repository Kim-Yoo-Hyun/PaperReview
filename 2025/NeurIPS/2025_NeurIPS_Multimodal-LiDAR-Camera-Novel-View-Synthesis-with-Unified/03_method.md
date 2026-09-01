# Method - Multimodal LiDAR-Camera Novel View Synthesis with Unified Pose-free Neural Fields

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=GQHUET0V6f; PDF retrieval source: https://openreview.net/pdf/81f57d1abb2e9779707b1274c08b3260d8f44d29.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (4 Methodology), p. 5 (4 Methodology), p. 7 (4 Methodology), p. 6 (4 Methodology), p. 7 (4 Methodology), p. 6 (4 Methodology)): Based on this observation, we propose a multimodal training method for optimizing the hash grid, which also stabilizes pose optimization and mitigates modality conflicts.

## Method Body Digest

- **p. 5 / 4 Methodology - extractive PDF cue:** Based on this observation, we propose a multimodal training method for optimizing the hash grid, which also stabilizes pose optimization and mitigates modality conflicts.
- **p. 5 / 4 Methodology - extractive PDF cue:** Then, we introduce our MMG module in Section 4.2, which provides explicit geometric guidance to avoid local optima.
- **p. 7 / 4 Methodology - extractive PDF cue:** Based on these correspondences, we introduce a point-to-image error using photometric loss, which serves as a regularization term.
- **p. 6 / 4 Methodology - extractive PDF cue:** In the Unified NeRF training, gradients are also propagated to pose from reconstruction loss.
- **p. 7 / 4 Methodology - extractive PDF cue:** Finally, the overall optimization loss for MMG is defined as: LMMG = LIRCD + LPoint2Image.
- **p. 6 / 4 Methodology - extractive PDF cue:** (4), the optimization of both hash-grid and pose follows a coarse-to-fine strategy.
- **p. 8 / 4 Methodology - extractive PDF cue:** 4.3 Overall Optimization Pipeline Consistency Constraint.
- **p. 5 / 4 Methodology - extractive PDF cue:** To explore how modality features are fused, we independently truncate the gradients of reconstruction loss LCamera and LLiDAR to hash grids and geo-MLP.

## Design Rationale

- **p. 3 / 1 Introduction - extractive PDF cue:** In summary, our primary contributions can be delineated as follows: (1) We propose MUP, a unified pose-free framework that combines the advantages of two modalities ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Moreover, to enhance color-depth consistency, we introduce a consistency constraint by projecting image pixels onto adjacent frames using depth derived from NeRF.
- **p. 2 / 1 Introduction - extractive PDF cue:** To alleviate modality conflicts [37] and address the uncoordinated convergence problem, we introduce a multimodal-specific coarse-to-fine training approach [16], facilitating the utilization of a singular ...

## Source Evidence Cues

- **p. 5 / 4 Methodology - extractive PDF cue:** Based on this observation, we propose a multimodal training method for optimizing the hash grid, which also stabilizes pose optimization and mitigates modality conflicts.
- **p. 5 / 4 Methodology - extractive PDF cue:** Then, we introduce our MMG module in Section 4.2, which provides explicit geometric guidance to avoid local optima.
- **p. 7 / 4 Methodology - extractive PDF cue:** Based on these correspondences, we introduce a point-to-image error using photometric loss, which serves as a regularization term.
- **p. 6 / 4 Methodology - extractive PDF cue:** In the Unified NeRF training, gradients are also propagated to pose from reconstruction loss.
- **p. 7 / 4 Methodology - extractive PDF cue:** Finally, the overall optimization loss for MMG is defined as: LMMG = LIRCD + LPoint2Image.
- **p. 6 / 4 Methodology - extractive PDF cue:** (4), the optimization of both hash-grid and pose follows a coarse-to-fine strategy.
- **p. 8 / 4 Methodology - extractive PDF cue:** 4.3 Overall Optimization Pipeline Consistency Constraint.
- **Detected method headings:** 4 Methodology (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Based on this observation, we propose a multimodal training method for optimizing the hash grid, which also stabilizes pose optimization and mitigates ... | p. 5 (4 Methodology), p. 5 (4 Methodology) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Then, we introduce our MMG module in Section 4.2, which provides explicit geometric guidance to avoid local optima. | p. 5 (4 Methodology), p. 7 (4 Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Based on these correspondences, we introduce a point-to-image error using photometric loss, which serves as a regularization term. | p. 7 (4 Methodology), p. 6 (4 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4 Methodology - extractive PDF cue:** To explore how modality features are fused, we independently truncate the gradients of reconstruction loss LCamera and LLiDAR to hash grids and geo-MLP.
- **p. 6 / 4 Methodology - extractive PDF cue:** In the Unified NeRF training, gradients are also propagated to pose from reconstruction loss.
- **p. 5 / 4 Methodology - extractive PDF cue:** Finally, we present the proposed consistency constraint and the overall optimization pipeline in Section 4.3.
- **p. 6 / 4 Methodology - extractive PDF cue:** In the early stages of optimization, only the gradients from the coarse resolution of the hash grids contribute to pose optimization, while the finer resolutions ...
- **p. 7 / 4 Methodology - extractive PDF cue:** Finally, the overall optimization loss for MMG is defined as: LMMG = LIRCD + LPoint2Image.
- **p. 7 / 4 Methodology - extractive PDF cue:** Based on these correspondences, we introduce a point-to-image error using photometric loss, which serves as a regularization term.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4 Methodology), p. 6 (4 Methodology), p. 5 (4 Methodology), p. 6 (4 Methodology), p. 7 (4 Methodology), p. 7 (4 Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | image, modality, lightweight, MLP, refine, geo-MLP, output, helping, reduce, conflicts, observation, multimodal, training, optimizing | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | image, modality, lightweight, MLP, refine, geo-MLP, output, helping, reduce, conflicts | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, primary, contributions, delineated, follows, MUP, unified, pose-free, framework, combines | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | explore, modality, features, fused, independently, truncate, gradients, reconstruction, loss, LCamera | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 4 Methodology - extractive PDF cue:** For the image modality, we use a lightweight MLP to refine the geo-MLP output, helping reduce modality conflicts.
- **p. 5 / 4 Methodology - extractive PDF cue:** Based on this observation, we propose a multimodal training method for optimizing the hash grid, which also stabilizes pose optimization and mitigates modality conflicts.
- **p. 7 / 4 Methodology - extractive PDF cue:** Leveraging the multimodal input, we exploit images to alleviate the impact of non-overlapping regions.
- **p. 2 / 1 Introduction - extractive PDF cue:** Nonetheless, when performing pose-free reconstruction and projecting discrete point clouds onto images for depth supervision, only a sparse set of pixels contains depth information, underutilizing ...
- **p. 4 / 3 Preliminaries - extractive PDF cue:** MUP is capable of performing NVS for both modalities, while also simultaneously recovering the vehicle poses P = {Ps/s = 0, 1, . . . ...
- **p. 4 / 3 Preliminaries - extractive PDF cue:** 𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈𝐈 Intensity Point Cloud World Coordinate System 𝑷𝑷𝟏𝟏 𝑷𝑷𝟐𝟐 𝑷𝑷𝟑𝟑 POSE Reconstruction Loss 𝐃𝐃𝐃𝐃𝐃𝐃𝐃𝐃𝐃𝐃 Ground Truth Unified Neural LiDAR-Camera Fields Camera-Mask LiDAR-Mask 𝐅𝐅𝐅𝐅𝐅𝐅𝐅𝐅𝐞𝐞𝟏𝟏 𝐅𝐅𝐅𝐅𝐅𝐅𝐅𝐅𝐞𝐞s𝟐𝟐 𝐅𝐅𝐅𝐅𝐅𝐅𝐅𝐅𝐞𝐞𝟑𝟑 ...
- **p. 6 / 4 Methodology - extractive PDF cue:** Consequently, we adopt point cloud-based loss at the early stages and later employ image-based photometric loss to refine the poses.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | However, it is primarily designed for sensor data within a sequence and relies on temporal correlations between frames. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Following prior pose-free NVS studies [16, 19, 47, 3, 10, 44], reconstruction is typically performed on short sequences without real-time constraints. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All experiments were conducted on a single NVIDIA GeForce RTX 3090 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4 Methodology - extractive PDF cue:** Based on this observation, we propose a multimodal training method for optimizing the hash grid, which also stabilizes pose optimization and mitigates modality conflicts.
- **p. 6 / 4 Methodology - extractive PDF cue:** In the Unified NeRF training, gradients are also propagated to pose from reconstruction loss.
- **p. 8 / 4 Methodology - extractive PDF cue:** 4.3 Overall Optimization Pipeline Consistency Constraint.
- **p. 6 / 4 Methodology - extractive PDF cue:** Pn+1 = Pn -(1 -w)lrGLiDAR -w · lrGCamera, (3) where G is the gradient of the corresponding modality, Pn denotes the pose at the n-th ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** observation, multimodal, training, optimizing, hash, grid, stabilizes, pose, optimization, mitigates, modality, conflicts, Then, introduce, MMG, module, Section, provides, explicit, geometric.
- **Relevant PDF headings:** 4 Methodology (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | For the NuScenes dataset, it includes six cameras and a LiDAR sensor, with keyframes that are typically used, which are time-synchronized based ... | p. 8 (5 Experiment), p. 8 (5 Experiment) |
| Semantic / temporal fusion | Figure 5: Qualitative comparison of NVS. We compared MUP with pose-free and registration-first methods. Nope-NeRF and Colored-ICP-assisted fail due to the large-scale ... | p. 7 (Figure/Table caption), p. 9 (5 Experiment) |
| Robot query / planning handoff | Figure 7: Qualitative NVS results with GT- poses. MUP outperforms single-modal meth- ods i-NGP w/ and w/o point clouds and LiDAR- NeRF. ... | p. 9 (Figure/Table caption), p. 9 (5 Experiment) |

## Failure and Ablation Link

- **p. 10 / 5 Experiment - extractive PDF cue:** Additionally, to further demonstrate the effectiveness of our multimodal approach, We conduct comparative experiments with the single-modality LiDAR-NeRF [36] and i-NGP [21], where i-NGP is ...
- **p. 9 / 5 Experiment - extractive PDF cue:** Ablation Study in pose-free setting.
- **p. 9 / 5 Experiment - extractive PDF cue:** All ablation studies are conducted on KITTI-360 [15].
- **p. 10 / 5 Experiment - extractive PDF cue:** Ablation of MSC2F and Consistency Loss.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: NVS results w/ and w/o accurate poses. Compared to continuous LiDAR-Camera Fields, projecting LiDAR point clouds onto images as discrete depth priors fails ...
- **p. 8 / 5 Experiment - extractive PDF cue:** For pose estimation, we follow [3], employing standard odometry metrics: Absolute Trajectory Error (ATE) and Relative Pose Error (RPE), with rotational (RPEr) and translational (RPEt) ...
- **p. 10 / 7 Conclusion - extractive PDF cue:** We revisit the limitations of single-modality pose-free methods in large-scale scenes.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (4 Methodology), p. 5 (4 Methodology), p. 7 (4 Methodology), p. 6 (4 Methodology), p. 7 (4 Methodology), p. 6 (4 Methodology), objective p. 5 (4 Methodology), p. 6 (4 Methodology), p. 5 (4 Methodology), p. 6 (4 Methodology), p. 7 (4 Methodology), p. 7 (4 Methodology), temporal p. 10 (5 Experiment), p. 9 (5 Experiment), p. 5 (4 Methodology), p. 5 (4 Methodology), p. 6 (4 Methodology), p. 6 (4 Methodology).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
