# Method - ElasticFusion: Dense SLAM Without A Pose Graph

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss11/p01.html; PDF retrieval source: https://www.roboticsproceedings.org/rss11/p01.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment)): We adopt an architecture which is typically found in realtime dense visual SLAM systems that alternates between tracking and mapping [15, 25, 9, 8, 2, 16].

## Method Body Digest

- **p. 2 / II. APPROACH OVERVIEW - extractive PDF cue:** We adopt an architecture which is typically found in realtime dense visual SLAM systems that alternates between tracking and mapping [15, 25, 9, 8, 2, ...
- **p. 2 / 1) Estimate a fused surfel-based model of the environment - extractive PDF cue:** If registration is successful, a loop has been closed to the older inactive model and the entire model is non-rigidly deformed into place to reflect ...
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive PDF cue:** In the following section we describe our fused map representation and method for predictive tracking.
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive PDF cue:** If a match is detected, register the views together and check if the registration is globally consistent with the model's geometry.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** As we show in our evaluation of the system in Section VII, this approach to dense SLAM achieves state-of-the-art performance with trajectory estimation results on ...
- **p. 2 / II. APPROACH OVERVIEW - extractive PDF cue:** We mainly use CUDA to implement our tracking reduction process and the OpenGL Shading Language for view prediction and map management.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** After pose graph optimisation the final map is created by merging key surfel views [21].
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Pose graph SLAM systems primarily focus on optimising the camera trajectory, whereas our approach (utilising a deformation graph) instead focuses on optimising the map.

## Design Rationale

- **p. 2 / II. APPROACH OVERVIEW - extractive PDF cue:** In the following, we summarise the key elements of our method.
- **p. 2 / 1) Estimate a fused surfel-based model of the environment - extractive PDF cue:** This component of our method is inspired by the surfelbased fusion system of Keller et al.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Pose graph SLAM systems primarily focus on optimising the camera trajectory, whereas our approach (utilising a deformation graph) instead focuses on optimising the map.

## Source Evidence Cues

- **p. 2 / II. APPROACH OVERVIEW - extractive PDF cue:** We adopt an architecture which is typically found in realtime dense visual SLAM systems that alternates between tracking and mapping [15, 25, 9, 8, 2, ...
- **p. 2 / 1) Estimate a fused surfel-based model of the environment - extractive PDF cue:** If registration is successful, a loop has been closed to the older inactive model and the entire model is non-rigidly deformed into place to reflect ...
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive PDF cue:** In the following section we describe our fused map representation and method for predictive tracking.
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive PDF cue:** If a match is detected, register the views together and check if the registration is globally consistent with the model's geometry.
- **Detected method headings:** II. APPROACH OVERVIEW (p. 2); 1) Estimate a fused surfel-based model of the environment (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We adopt an architecture which is typically found in realtime dense visual SLAM systems that alternates between tracking and mapping [15, 25, ... | p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | If registration is successful, a loop has been closed to the older inactive model and the entire model is non-rigidly deformed into ... | p. 2 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | In the following section we describe our fused map representation and method for predictive tracking. | p. 3 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | evaluation, system, Section, VII, dense, SLAM, achieves, state-of-the-art, performance, trajectory, estimation, better, existing, systems | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | evaluation, system, Section, VII, dense, SLAM, achieves, state-of-the-art, performance, trajectory | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | following, summarise, elements, component, inspired, surfelbased, fusion, system, Keller, Pose | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | not recovered | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** As we show in our evaluation of the system in Section VII, this approach to dense SLAM achieves state-of-the-art performance with trajectory estimation results on ...
- **p. 2 / II. APPROACH OVERVIEW - extractive PDF cue:** We mainly use CUDA to implement our tracking reduction process and the OpenGL Shading Language for view prediction and map management.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** After pose graph optimisation the final map is created by merging key surfel views [21].
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Pose graph SLAM systems primarily focus on optimising the camera trajectory, whereas our approach (utilising a deformation graph) instead focuses on optimising the map.
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive PDF cue:** In the following section we describe our fused map representation and method for predictive tracking.
- **p. 3 / 1) Estimate a fused surfel-based model of the environment - extractive PDF cue:** tracking and surface fusion (including surfel culling) to take place between the registered areas of the map.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Geometric Pose Estimation Between the current live depth map Dl t and the predicted active model depth map from the last frame ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Computational Performance To analyse the computational performance of the system we provide a plot of the average frame processing time across the ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | As shown in Figure 6 the execution time of the system increases with the number of surfels in the map, with an ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** adopt, architecture, typically, found, realtime, dense, visual, SLAM, systems, alternates, between, tracking, mapping, registration, successful, loop, been, closed, older, inactive.
- **Relevant PDF headings:** II. APPROACH OVERVIEW (p. 2); 1) Estimate a fused surfel-based model of the environment (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | The Lab dataset contains a very loopy trajectory around a large office environment with many global and local loop closures. | p. 8 (VII. EVALUATION), p. 7 (VII. EVALUATION) |
| Global / local decision | These results show that our trajectory estimation performance is on par with or better than existing state-of-the-art systems that Fig. | p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION) |
| Motion execution / recovery | Interestingly our frame-to-model only results are also comparable in performance, whereas a uniform increase in accuracy is achieved when active to inactive ... | p. 7 (VII. EVALUATION), p. 7 (VII. EVALUATION) |

## Failure and Ablation Link

- **p. 7 / VII. EVALUATION - extractive PDF cue:** Points more than 0.1m from ground truth have been removed for visualisation purposes.
- **p. 8 / VIII. CONCLUSION - extractive PDF cue:** In future work we wish to address the problem of map scalability beyond whole rooms and also investigate the problem of dense globally consistent SLAM ...
- **p. 7 / VII. EVALUATION - extractive PDF cue:** We evaluate our approach on all four trajectories in the living room scene (including synthetic noise) providing surface reconstruction accuracy results in comparison to the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (II. APPROACH OVERVIEW), p. 2 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment), p. 3 (1) Estimate a fused surfel-based model of the environment), objective 본문 anchor 없음, temporal p. 3 (III. FUSED PREDICTED TRACKING), p. 8 (VII. EVALUATION), p. 8 (VII. EVALUATION), p. 1 (Abstract), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
