# Method - LIT-GS: LiDAR-Inertial-Thermal Gaussian Splatting for Illumination-Robust Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2606.20424; PDF retrieval source: https://arxiv.org/pdf/2606.20424. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY)): LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 LiDAR-inertial-visual estimator as geometric anchors to est ...

## Method Body Digest

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 LiDAR-inertial-visual estimator as ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** 2) Thermal feature extraction and matching: For frameto-frame registration and scene-graph construction, we employ SuperPoint [15] for keypoint detection and description and SuperGlue [16] for ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Given synchronized LiDAR, inertial, and thermal measurements, it jointly estimates camera poses, 3D structure, and Gaussian parameters by minimizing a differentiable objective that couples thermal ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** In each frame, anchors are enforced to contribute a fraction αt of the total geometric weight, while the remaining weight is distributed to non-anchor points ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** (1) To adapt the anchor/non-anchor balance to the motion state of the current frame, we compute a normalized motion score from the linear and angular ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Reliance on visible imagery poses a fundamental limitation.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** This efficiency has rapidly motivated radiance-field mapping for robotics and large-scale environments, yet most existing 3DGS-based mapping pipelines still depend heavily on RGB imagery and ...

## Design Rationale

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Although LiDAR provides metric geometry, existing LiDAR-inertial-visual Gaus- * Equal contribution. † Corresponding Author.

## Source Evidence Cues

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 LiDAR-inertial-visual estimator as ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** 2) Thermal feature extraction and matching: For frameto-frame registration and scene-graph construction, we employ SuperPoint [15] for keypoint detection and description and SuperGlue [16] for ...
- **Detected method headings:** III. METHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 ... | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | 2) Thermal feature extraction and matching: For frameto-frame registration and scene-graph construction, we employ SuperPoint [15] for keypoint detection and description and ... | p. 3 (III. METHODOLOGY) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 ... | p. 3 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** Given synchronized LiDAR, inertial, and thermal measurements, it jointly estimates camera poses, 3D structure, and Gaussian parameters by minimizing a differentiable objective that couples thermal ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 LiDAR-inertial-visual estimator as ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | frame, anchors, enforced, contribute, fraction, total, geometric, weight, while, remaining, distributed, non-anchor, points, according | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | frame, anchors, enforced, contribute, fraction, total, geometric, weight, while, remaining | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Frame-wise, anchor-aware, geometric, weighting, improve, robustness, under, motion, introduce, anchor-non-anchor | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Given, synchronized, LiDAR, inertial, thermal, measurements, jointly, estimates, camera, poses | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** In each frame, anchors are enforced to contribute a fraction αt of the total geometric weight, while the remaining weight is distributed to non-anchor points ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** (1) To adapt the anchor/non-anchor balance to the motion state of the current frame, we compute a normalized motion score from the linear and angular ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Reliance on visible imagery poses a fundamental limitation.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** This efficiency has rapidly motivated radiance-field mapping for robotics and large-scale environments, yet most existing 3DGS-based mapping pipelines still depend heavily on RGB imagery and ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | LIT-GS is formulated as a unified geometry-aware optimization framework. | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHODOLOGY - extractive PDF cue:** LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 LiDAR-inertial-visual estimator as ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** LIT-GS, integrates, three, tightly, coupled, components, confidence-aware, cross-modal, anchoring, module, uses, uncertainty-tagged, visual, points, upstream, FAST-LIVO2, LiDAR-inertial-visual, estimator, geometric, anchors.
- **Relevant PDF headings:** III. METHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Preprocessing Prior to processing, PPS-based hardware synchronization is applied and the thermal camera-LiDAR intrinsics/extrinsics are calibrated. | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Global / local decision | Fig. 5. Omni-view ablation experiment demonstration. From the perspectives of front, back, left, and right, the refined perspectives (a1-a4) are compared with ... | p. 7 (Figure/Table caption), p. 5 (Figure/Table caption) |
| Motion execution / recovery | To improve global geometric accuracy and robustness in dynamic scenarios, we perform a LiDARplane-constrained bundle adjustment (BA) that jointly refines camera poses ... | p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5. Omni-view ablation experiment demonstration. From the perspectives of front, back, left, and right, the refined perspectives (a1-a4) are compared with the unrefined perspectives ...
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** LIT-GS integrates three tightly coupled components: • A confidence-aware cross-modal anchoring module that uses uncertainty-tagged visual map points from an upstream FAST-LIVO2 LiDAR-inertial-visual estimator as ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Reliance on visible imagery poses a fundamental limitation.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Under illumination changes or texture-deficient scenes, photometric cues become unstable, degrading correspondence quality and pose estimation [4].
- **p. 2 / II. RELATED WORKS - extractive PDF cue:** In contrast, LIT-GS combines illuminationrobust thermal supervision [8, 9] with persistent LiDAR
- **p. 2 / II. RELATED WORKS - extractive PDF cue:** Learning-based methods improve robustness by jointly learning detection and description, as exemplified by D2-Net [17].
- **p. 3 / III. METHODOLOGY - extractive PDF cue:** 1) Frame-wise anchor-aware geometric weighting.: To improve robustness under motion, we introduce frame-wise anchor-non-anchor geometric weighting.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), objective p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), temporal p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 1 (I. INTRODUCTION), p. 1 (Abstract), p. 2 (II. RELATED WORKS), p. 2 (II. RELATED WORKS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
