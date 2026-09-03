# Method - KinectFusion: Real-Time Dense Surface Mapping and Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.microsoft.com/en-us/research/publication/kinectfusion-real-time-dense-surface-mapping-and-tracking/; PDF retrieval source: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ismar2011.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (3.1 Preliminaries), p. 4 (3 METHOD), p. 6 (3.1 Preliminaries), p. 4 (3.1 Preliminaries), p. 5 (3.1 Preliminaries), p. 5 (3.1 Preliminaries)): The point-plane error metric in combination with correspondences obtained using projective data association was first demonstrated in a real time modelling system by [23] where frame-toframe tracking was used (with ...

## Method Body Digest

- **p. 6 / 3.1 Preliminaries - extractive body cue:** The point-plane error metric in combination with correspondences obtained using projective data association was first demonstrated in a real time modelling system by [23] where ...
- **p. 4 / 3 METHOD - extractive body cue:** Surface reconstruction update: The global scene fusion process, where given the pose determined by tracking the depth data from a new sensor frame, the surface ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** Many tracking algorithms use feature selection to improve speed by reducing the number of points for which data association need be performed.
- **p. 4 / 3.1 Preliminaries - extractive body cue:** We compute an L = 3 level multi-scale representation of the surface measurement in the form of a vertex and normal map pyramid.
- **p. 5 / 3.1 Preliminaries - extractive body cue:** Also, the support is increased linearly with distance from the sensor center to support correct representation of noisier measurements.
- **p. 5 / 3.1 Preliminaries - extractive body cue:** Although efficient algorithms exist for computing the true discrete SDF for a given set of point measurements (complexity is linear in the the number of ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** (21) An iteration is obtained by solving: min x∈R6 ∑ Ωk(u)̸=null ∥E∥2 2 (22) E = ˆNg k-1(ˆu)⊤ G(u)x+ eVg k(u)-ˆVg k-1(ˆu)  (23) By ...
- **p. 5 / 3.1 Preliminaries - extractive body cue:** Storing a weight Wk(p) with each value allows an important aspect of the global minimum of the convex L2 de-noising metric to be exploited for ...

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper we present a detailed method with analysis of what we believe is the first system which permits real-time, dense volumetric reconstruction of ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** Second, modern GPU hardware enables a fully parrallelised processing pipeline, so that the data association and point-plane optimisation can use all of the available surface ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** The symmetry of the system enables operations and memory to be saved and the final sum is obtained using a parallel tree-based reduction [13], to ...

## Source Evidence Cues

- **p. 6 / 3.1 Preliminaries - extractive body cue:** The point-plane error metric in combination with correspondences obtained using projective data association was first demonstrated in a real time modelling system by [23] where ...
- **p. 4 / 3 METHOD - extractive body cue:** Surface reconstruction update: The global scene fusion process, where given the pose determined by tracking the depth data from a new sensor frame, the surface ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** Many tracking algorithms use feature selection to improve speed by reducing the number of points for which data association need be performed.
- **p. 4 / 3.1 Preliminaries - extractive body cue:** We compute an L = 3 level multi-scale representation of the surface measurement in the form of a vertex and normal map pyramid.
- **p. 5 / 3.1 Preliminaries - extractive body cue:** Also, the support is increased linearly with distance from the sensor center to support correct representation of noisier measurements.
- **p. 5 / 3.1 Preliminaries - extractive body cue:** Although efficient algorithms exist for computing the true discrete SDF for a given set of point measurements (complexity is linear in the the number of ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** (21) An iteration is obtained by solving: min x∈R6 ∑ Ωk(u)̸=null ∥E∥2 2 (22) E = ˆNg k-1(ˆu)⊤ G(u)x+ eVg k(u)-ˆVg k-1(ˆu)  (23) By ...
- **Detected method headings:** 3 METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The point-plane error metric in combination with correspondences obtained using projective data association was first demonstrated in a real time modelling system ... | p. 6 (3.1 Preliminaries), p. 4 (3 METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Surface reconstruction update: The global scene fusion process, where given the pose determined by tracking the depth data from a new sensor ... | p. 4 (3 METHOD), p. 6 (3.1 Preliminaries) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Many tracking algorithms use feature selection to improve speed by reducing the number of points for which data association need be performed. | p. 6 (3.1 Preliminaries), p. 4 (3.1 Preliminaries) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.1 Preliminaries - extractive body cue:** Storing a weight Wk(p) with each value allows an important aspect of the global minimum of the convex L2 de-noising metric to be exploited for ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** Outliers from compatibility checks (Equation 17) using a surface measurement with (center) and without (right) bilateral filtering applied to the raw depth map. Ω(u) = ...
- **p. 4 / 3.1 Preliminaries - extractive body cue:** Subsequently each level in a vertex and normal map pyramid Vl∈[1...L], Nl∈[1...L] is computed with Equations 3 and 4 using the corresponding depth map level.
- **p. 5 / 3.1 Preliminaries - extractive body cue:** (5) A dense surface measurement (such as the raw depth map Rk) provides two important constraints on the surface being reconstructed.
- **p. 6 / 3.1 Preliminaries - extractive body cue:** 3.5 Sensor Pose Estimation Live camera localisation involves estimating the current camera pose Tw,k ∈SE3 (Equation 1) for each new depth image.
- **p. 7 / 3.1 Preliminaries - extractive body cue:** (21) An iteration is obtained by solving: min x∈R6 ∑ Ωk(u)̸=null ∥E∥2 2 (22) E = ˆNg k-1(ˆu)⊤ G(u)x+ eVg k(u)-ˆVg k-1(ˆu)  (23) By ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), p. 4 (3.1 Preliminaries), p. 5 (3.1 Preliminaries).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Later, discovered, practically, advantageous, abandon, propagation, full, probabilistic, state, instead, procedures, alternation, parallel, tracking | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Later, discovered, practically, advantageous, abandon, propagation, full, probabilistic, state, instead | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | present, detailed, analysis, what, believe, first, system, permits, real-time, dense | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Storing, weight, value, allows, important, aspect, global, minimum, convex, de-noising | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 2 BACKGROUND - extractive body cue:** Later, it was discovered to be practically advantageous to abandon the propagation of a full probabilistic state and instead to run two procedures in alternation ...
- **p. 4 / 3.1 Preliminaries - extractive body cue:** We will also use a dot notation to denote homogeneous vectors ˙u := (u⊤/1)⊤ 3.2 Surface Measurement At time k a measurement comprises a raw ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** 3.5 Sensor Pose Estimation Live camera localisation involves estimating the current camera pose Tw,k ∈SE3 (Equation 1) for each new depth image.
- **p. 4 / 3 METHOD - extractive body cue:** Rk Tg,k Rk Tg,k-1 Input Measurement Pose Estimation Update Reconstruction Surface Prediction Compute Surface Nertex and Normal Maps ICP of Predicted and Measured Surface Integrate ...
- **p. 5 / 3.1 Preliminaries - extractive body cue:** For a raw depth map Rk with a known pose Tg,k, its global frame projective TSDF [FRk,WRk] at a point p in the global frame ...
- **p. 6 / 3.1 Preliminaries - extractive body cue:** In this work, we take advantage of two factors to allow us instead to make use of all of the data in a depth image ...
- **p. 7 / 3.1 Preliminaries - extractive body cue:** Relocalisation Our current implementation uses an interactive re-localisation scheme, whereby if the sensor loses track, the last known sensor pose is used to provide a ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | For example, the ability to reason about changes in the scene, utilising outliers from ICP data association (see Figure 7), allows for ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | (10) Given that the focus of our work is on real-time sensor tracking and surface reconstruction we must maintain interactive frame-rates. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | For example, the ability to reason about changes in the scene, utilising outliers from ICP data association (see Figure 7), allows for ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** point-plane, error, metric, combination, correspondences, obtained, projective, data, association, first, demonstrated, real, time, modelling, system, where, frame-toframe, tracking, fixed, camera.
- **Relevant PDF headings:** 3 METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Finally, for comparison, a new longer dataset of MN frames was processed, where a user moved the sensor over the scene without ... | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Global / local decision | Note that this can be compared with the reconstruction from the same number of MN different frames of the same scene obtained ... | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Motion execution / recovery | Rapid accumulation of errors results in the non-circular trajectory and poor reconstruction is apparent (though see later Figure 11 where frame-skipping is ... | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.1 Metrically Consistent Reconstruction Our tracking and mapping system provides a constant time algorithm for a given area of reconstruction, and we are interested in ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Finally, for comparison, a new longer dataset of MN frames was processed, where a user moved the sensor over the scene without precise repetition.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** While the turntable experiments demonstrate interesting convergence of the system without an explicit global optimisation, the real power in integrating every frame of data is ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** But the frame-model tracking results in drift-free operation without explicit global optimisation.
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5: Reconstructed of a scene showing raycasting of the TSDF (left) without and (middle and right) with interpolation of the TSDF at the surface ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.2 Processing Time Figure 13 shows results from an experiment where timings were taken of the main system components and the reconstruction voxel resolution was ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 4.3 Observations and Failure Modes Our system is robust to a wide range of practical conditions in terms of scene structure and camera motion.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (3.1 Preliminaries), p. 4 (3 METHOD), p. 6 (3.1 Preliminaries), p. 4 (3.1 Preliminaries), p. 5 (3.1 Preliminaries), p. 5 (3.1 Preliminaries), objective p. 5 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), p. 4 (3.1 Preliminaries), p. 5 (3.1 Preliminaries), p. 6 (3.1 Preliminaries), p. 7 (3.1 Preliminaries), temporal p. 9 (4 EXPERIMENTS), p. 5 (3.1 Preliminaries), p. 5 (3.1 Preliminaries), p. 1 (ABSTRACT), p. 2 (2 BACKGROUND), p. 4 (3 METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
