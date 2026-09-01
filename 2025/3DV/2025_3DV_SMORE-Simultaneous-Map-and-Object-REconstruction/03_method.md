# Method - SMORE: Simultaneous Map and Object REconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=1NhnG9BvQB&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Decomposition), p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?), p. 5 (4.4. What is a LiDAR sweep?)): The first step of both derivations decomposes the objective across objects.

## Method Body Digest

- **p. 4 / 4.1. Decomposition - extractive PDF cue:** The first step of both derivations decomposes the objective across objects.
- **p. 4 / 4.1. Decomposition - extractive PDF cue:** In the following sections we derive the appropriate surface and pose optimization steps from the global objective.
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** However, our spacetime optimization can correctly model moving objects by applying the same insight; just as we assumed that the ego-vehicle obeys a constant velocity ...
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** Importantly, our global optimization Eq.
- **p. 4 / 4.1. Decomposition - extractive PDF cue:** Our approach consists of applying coordinate descent to Equation (2): alternating between fixing the poses to optimize surfaces and then fixing the surfaces to optimize ...
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** However, such constraints no longer hold after deskewing.
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** (7) Using these equations, points can be deskewed by transforming all of the points in a sweep to the coordinate frame e0.
- **p. 1 / 1. Introduction - extractive PDF cue:** In *Equal Contribution the context of depth sensors, this problem is posed as dynamic surface reconstruction, where the goal is to produce a time-varying surface ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** An example of the depth maps produced by our method is shown in Fig.
- **p. 2 / 1. Introduction - extractive PDF cue:** We introduce a global optimization that refines both ego and object poses so as to minimize a scan-to-surface reconstruction error, dramatically improving results (right).
- **p. 4 / 4.1. Decomposition - extractive PDF cue:** Our approach consists of applying coordinate descent to Equation (2): alternating between fixing the poses to optimize surfaces and then fixing the surfaces to optimize ...

## Source Evidence Cues

- **p. 4 / 4.1. Decomposition - extractive PDF cue:** The first step of both derivations decomposes the objective across objects.
- **p. 4 / 4.1. Decomposition - extractive PDF cue:** In the following sections we derive the appropriate surface and pose optimization steps from the global objective.
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** However, our spacetime optimization can correctly model moving objects by applying the same insight; just as we assumed that the ego-vehicle obeys a constant velocity ...
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** Importantly, our global optimization Eq.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The first step of both derivations decomposes the objective across objects. | p. 4 (4.1. Decomposition), p. 4 (4.1. Decomposition) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In the following sections we derive the appropriate surface and pose optimization steps from the global objective. | p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | However, our spacetime optimization can correctly model moving objects by applying the same insight; just as we assumed that the ego-vehicle obeys ... | p. 5 (4.4. What is a LiDAR sweep?), p. 5 (4.4. What is a LiDAR sweep?) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.1. Decomposition - extractive PDF cue:** In the following sections we derive the appropriate surface and pose optimization steps from the global objective.
- **p. 4 / 4.1. Decomposition - extractive PDF cue:** Our approach consists of applying coordinate descent to Equation (2): alternating between fixing the poses to optimize surfaces and then fixing the surfaces to optimize ...
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** However, such constraints no longer hold after deskewing.
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** (7) Using these equations, points can be deskewed by transforming all of the points in a sweep to the coordinate frame e0.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4. Objective), p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?), p. 5 (4.4. What is a LiDAR sweep?).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Equal, Contribution, context, depth, sensors, problem, posed, dynamic, surface, reconstruction, where, goal, produce, time-varying | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Equal, Contribution, context, depth, sensors, problem, posed, dynamic, surface, reconstruction | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | example, depth, maps, produced, Fig, introduce, global, optimization, refines, object | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | following, sections, derive, appropriate, surface, pose, optimization, steps, global, objective | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** In *Equal Contribution the context of depth sensors, this problem is posed as dynamic surface reconstruction, where the goal is to produce a time-varying surface ...
- **p. 3 / 3. Problem Statement - extractive PDF cue:** We assume as input a sequence of LiDAR sweeps measured at timestamps t ∈T , and coarse tracks of K objects.
- **p. 3 / 3. Problem Statement - extractive PDF cue:** Since we are using a compositional model of the scene, we will need a coordinate frame for each component. • Ego coordinates: This is the ...
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** To avoid this, we adopt a constant velocity model for poses between "keyframes" placed at the end of every complete sensor rotation.
- **p. 4 / 3. Problem Statement - extractive PDF cue:** Finally, we will measure the 3D distance between a surface and a point cloud using the nearest neighbor loss D(M, X) = X x∈X min ...
- **p. 5 / 4.4. What is a LiDAR sweep? - extractive PDF cue:** Ego-Motion Distortion: When the sensor moves during a sweep the resulting point cloud is distorted.
- **p. 1 / 1. Introduction - extractive PDF cue:** However, investment in autonomous driving has created a new mode of depth capture - spinning LiDAR sensors atop moving vehicles - which is largely unaddressed ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Then, we optimize the test poses to by running one pose step (ICP). | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For the mesh step, we use the default parameters of the publicly released Neural Kernel Surface Reconstruction model[12]. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Specifically, we compute the percent of points less than 10cm and 5cm for the relaxed and strict metrics, respectively Annotation Rate 1Hz ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 5.1. Lidar Novel View Synthesis - extractive PDF cue:** SMORE Details: We run the SMORE optimization on the training views to obtain reconstructed meshes for objects and the background.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** first, step, derivations, decomposes, objective, across, objects, following, sections, derive, appropriate, surface, pose, optimization, steps, global, However, spacetime, correctly, model.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Datasets: All of our experiments are conducted on nuScenes[3] and Argoverse 2.0[42]. | p. 5 (5. Experiments), p. 6 (5. Experiments) |
| Semantic / temporal fusion | However, the comparison is with a state-of-the-art LiDAR odometry method instead of the ground truth since we find odometry is generally superior. | p. 8 (6. Qualitative Results), p. 7 (5.1. Lidar Novel View Synthesis) |
| Robot query / planning handoff | Figure 2. Dynamic object reconstructions using human-annotated bounding-box annotations (top left) tend to be noisy. Optimizing over object pose (top right) improves ... | p. 2 (Figure/Table caption), p. 8 (6. Qualitative Results) |

## Failure and Ablation Link

- **p. 6 / 5.1. Lidar Novel View Synthesis - extractive PDF cue:** Iterations are stopped if the mean registration error for an object falls below 1 centimeter for three consecutive iterations.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1. NuScenes surface reconstruction produced by aggregating LiDAR scans using human-annotated ego-pose and dynamic object bounding boxes (left). We introduce a global optimization that ...
- **p. 6 / 5. Experiments - extractive PDF cue:** Interestingly, our approach is even more effective for recent AV datasets [30, 42] that employ multiple spinning lidars, which are often set to be out-of-phase ...
- **p. 7 / 5.1. Lidar Novel View Synthesis - extractive PDF cue:** For testing, however, the reference implementation does not support optimizing new poses that were not present at train time.
- **p. 5 / 5. Experiments - extractive PDF cue:** We focus primarily on nuScenes as its noisy annotations and sparse LiDAR present the greatest challenge to accurate geometry recovery.
- **p. 7 / 5.2. Pose Estimation - extractive PDF cue:** 1 further confirm the robustness of our method to input annotation errors.
- **p. 8 / 6. Qualitative Results - extractive PDF cue:** Evaluation of our method's robustness to actor annotation errors (subsampling or real tracks).

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.1. Decomposition), p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?), p. 5 (4.4. What is a LiDAR sweep?), objective p. 4 (4.1. Decomposition), p. 4 (4.1. Decomposition), p. 5 (4.4. What is a LiDAR sweep?), p. 5 (4.4. What is a LiDAR sweep?), temporal p. 6 (5.1. Lidar Novel View Synthesis), p. 6 (5.1. Lidar Novel View Synthesis), p. 7 (5.2. Pose Estimation), p. 7 (5.1. Lidar Novel View Synthesis), p. 1 (Abstract), p. 1 (1. Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
