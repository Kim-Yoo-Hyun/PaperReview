# Method - ORB-SLAM: A Versatile and Accurate Monocular SLAM System

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1502.00956; PDF retrieval source: https://arxiv.org/pdf/1502.00956. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 5 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 5 (III. SYSTEM OVERVIEW), p. 6 (IV. AUTOMATIC MAP INITIALIZATION), p. 7 (V. TRACKING)): Nowadays we know that to achieve accurate results at non-prohibitive computational cost, a real time SLAM algorithm has to provide BA with: • Corresponding observations of scene features (map points) ...

## Method Body Digest

- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** Nowadays we know that to achieve accurate results at non-prohibitive computational cost, a real time SLAM algorithm has to provide BA with: • Corresponding observations ...
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** We use the Levenberg-Marquardt algorithm implemented in g2o [37] to carry out all optimizations.
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** We use ORB features [9] which allow real-time performance without GPUs, providing good invariance to changes in viewpoint and illumination. • Real time operation in ...
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** In order not to include all the edges provided by the covisibility graph, which can be very dense, we propose to build an Essential Graph ...
- **p. 6 / IV. AUTOMATIC MAP INITIALIZATION - extractive body cue:** We propose to compute in parallel two geometrical models, a homography assuming a planar scene and a fundamental matrix assuming a non-planar scene.
- **p. 7 / V. TRACKING - extractive body cue:** If not enough matches were found (i.e. motion model is clearly violated), we use a wider search of the map points around their position in ...
- **p. 7 / V. TRACKING - extractive body cue:** Initial Pose Estimation from Previous Frame If tracking was successful for last frame, we use a constant velocity motion model to predict the camera pose ...
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** In the Appendix we describe the error terms, cost functions, and variables involved in each optimization.

## Design Rationale

- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** In this work we build on the main ideas of PTAM, the place recognition work of G´alvez-L´opez and Tard´os [5], the scale-aware loop closing of ...
- **p. 2 / Abstract - extractive body cue:** We present an exhaustive evaluation in 27 sequences from the most popular datasets.
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** This allows to match them from wide baselines, boosting the accuracy of BA.

## Source Evidence Cues

- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** Nowadays we know that to achieve accurate results at non-prohibitive computational cost, a real time SLAM algorithm has to provide BA with: • Corresponding observations ...
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** We use the Levenberg-Marquardt algorithm implemented in g2o [37] to carry out all optimizations.
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** We use ORB features [9] which allow real-time performance without GPUs, providing good invariance to changes in viewpoint and illumination. • Real time operation in ...
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** In order not to include all the edges provided by the covisibility graph, which can be very dense, we propose to build an Essential Graph ...
- **p. 6 / IV. AUTOMATIC MAP INITIALIZATION - extractive body cue:** We propose to compute in parallel two geometrical models, a homography assuming a planar scene and a fundamental matrix assuming a non-planar scene.
- **p. 7 / V. TRACKING - extractive body cue:** If not enough matches were found (i.e. motion model is clearly violated), we use a wider search of the map points around their position in ...
- **p. 7 / V. TRACKING - extractive body cue:** Initial Pose Estimation from Previous Frame If tracking was successful for last frame, we use a constant velocity motion model to predict the camera pose ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Nowadays we know that to achieve accurate results at non-prohibitive computational cost, a real time SLAM algorithm has to provide BA with: ... | p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 5 (III. SYSTEM OVERVIEW) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We use the Levenberg-Marquardt algorithm implemented in g2o [37] to carry out all optimizations. | p. 5 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | We use ORB features [9] which allow real-time performance without GPUs, providing good invariance to changes in viewpoint and illumination. • Real ... | p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 5 (III. SYSTEM OVERVIEW) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** In the Appendix we describe the error terms, cost functions, and variables involved in each optimization.
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** Nowadays we know that to achieve accurate results at non-prohibitive computational cost, a real time SLAM algorithm has to provide BA with: • Corresponding observations ...
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** Finally a pose graph optimization over similarity constraints [6] is performed to achieve global consistency.
- **p. 6 / III. SYSTEM OVERVIEW - extractive body cue:** When we want to compute the correspondences between two sets of ORB features, we can constraint the brute force matching only to those features that ...
- **p. 8 / VI. LOCAL MAPPING - extractive body cue:** This matching is done as explained in Section III-E and discard those matches that do not fulfill the epipolar constraint.
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** Notably, we achieve better camera localization accuracy than the state of the art in direct methods [10], which optimize directly over pixel intensities instead of ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (III. SYSTEM OVERVIEW), p. 6 (III. SYSTEM OVERVIEW), p. 8 (VI. LOCAL MAPPING), p. 6 (III. SYSTEM OVERVIEW), p. 8 (VI. LOCAL MAPPING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | When, keyframe, inserted, included, tree, linked, shares, most, point, observations, erased, culling, policy, system | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | When, keyframe, inserted, included, tree, linked, shares, most, point, observations | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | build, main, ideas, PTAM, place, recognition, alvez-L, opez, Tard, scale-aware | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Appendix, describe, error, terms, cost, functions, variables, involved, optimization, Nowadays | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / III. SYSTEM OVERVIEW - extractive body cue:** When a new keyframe is inserted, it is included in the tree linked to the keyframe which shares most point observations, and when a keyframe ...
- **p. 2 / B UNDLE ADJUSTMENT (BA) is known to provide ac - extractive body cue:** Nowadays we know that to achieve accurate results at non-prohibitive computational cost, a real time SLAM algorithm has to provide BA with: • Corresponding observations ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** We requiere features that need for extraction much less than 33ms per image, which excludes the popular SIFT (∼300ms) [19], SURF (∼300ms) [18] or the ...
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** Each node is a keyframe and an edge between two keyframes exists if they share observations of the same map points (at least 15), being ...
- **p. 5 / III. SYSTEM OVERVIEW - extractive body cue:** Map points and keyframes are created with a generous policy, while a later very exigent culling mechanism is in charge of detecting redundant keyframes and ...
- **p. 6 / III. SYSTEM OVERVIEW - extractive body cue:** IEEE TRANSACTIONS ON ROBOTICS 5 accurate results.
- **p. 8 / VI. LOCAL MAPPING - extractive body cue:** This policy makes our map contain very few outliers.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Each horizontal line corresponds to a keyframe, from its creation frame until its destruction 0 10 20 30 40 50 60 70 ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | The sequence is recorded by a stereo camera at 20 fps and a resolution 512×382. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | The sequence is recorded by a stereo camera at 20 fps and a resolution 512×382. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Nowadays, know, achieve, accurate, non-prohibitive, computational, cost, real, time, SLAM, algorithm, provide, Corresponding, observations, scene, features, points, among, subset, selected.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We have performed an extensive experimental validation of our system in the large robot sequence of NewCollege [39], evaluating the general performance ... | p. 9 (VIII. EXPERIMENTS), p. 12 (VIII. EXPERIMENTS) |
| Global / local decision | We perform the same experiment with PTAM for comparison. | p. 11 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS) |
| Motion execution / recovery | In terms of accuracy ORB-SLAM and PTAM are similar in open trajectories, while ORB-SLAM achieves higher accuracy when detecting large loops as ... | p. 11 (VIII. EXPERIMENTS), p. 15 (VIII. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 15 / VIII. EXPERIMENTS - extractive body cue:** In table VI we show the keyframe trajectory RMSE and the time spent in the optimization in different cases: without loop closing, if we directly ...
- **p. 15 / VIII. EXPERIMENTS - extractive body cue:** 100 0 100 200 300 x [m] 200 100 0 100 200 300 400 500 600 y [m] Ground truth Estimated (a) Without Loop Closing ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 1. ORB-SLAM system overview, showing all the steps performed by the tracking, local mapping and loop closing threads. The main components of the place ...
- **p. 16 / IX. CONCLUSIONS AND DISCUSSION - extractive body cue:** However, direct methods have their own limitations.
- **p. 16 / IX. CONCLUSIONS AND DISCUSSION - extractive body cue:** Future Work The accuracy of our system can still be improved incorporating points at infinity in the tracking.
- **p. 15 / VIII. EXPERIMENTS - extractive body cue:** In sequence 08 there are no loops and drift cannot be corrected, which makes clear the need of loop closures to achieve accurate reconstructions.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** The big loop on the right does not perfectly align because it was traversed in opposite directions and the place recognizer was not able to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 5 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 5 (III. SYSTEM OVERVIEW), p. 6 (IV. AUTOMATIC MAP INITIALIZATION), p. 7 (V. TRACKING), objective p. 5 (III. SYSTEM OVERVIEW), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), p. 5 (III. SYSTEM OVERVIEW), p. 6 (III. SYSTEM OVERVIEW), p. 8 (VI. LOCAL MAPPING), p. 2 (B UNDLE ADJUSTMENT (BA) is known to provide ac), temporal p. 13 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS), p. 11 (VIII. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
