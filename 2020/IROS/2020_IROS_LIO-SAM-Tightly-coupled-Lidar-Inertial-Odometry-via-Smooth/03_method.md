# Method - LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2007.00258; PDF retrieval source: https://arxiv.org/pdf/2007.00258. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (Abstract), p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA)): We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets.

## Method Body Digest

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets.
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Since we extract two types of features in the previous feature extraction step, Mi is composed of two subvoxel maps that are denoted Me i, ...
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Lidar Odometry Factor When a new lidar scan arrives, we first perform feature extraction.
- **p. 1 / Abstract - extractive body cue:** We propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIO-SAM, that achieves highly accurate, real-time mobile robot trajectory estimation and map-building.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We seek to estimate the state of the robot and its trajectory using the observations of these sensors.
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** each feature in ′Fe i+1 or ′Fp i+1, we then find its edge or planar correspondence in Me i or Mp i .
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** When a new state xi+1 is added to the factor graph, we first search the graph and find the prior states that are close to ...
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Note that without loss of generality, the proposed system can also incorporate measurements from other sensors, such as elevation from an altimeter or heading from ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Scan-matching at a local scale instead of a global scale significantly improves the real-time performance of the system, as does the selective introduction of keyframes, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIOSAM, to address the aforementioned problems.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We introduce four types of factors along with one variable type for factor graph construction.

## Source Evidence Cues

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets.
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Since we extract two types of features in the previous feature extraction step, Mi is composed of two subvoxel maps that are denoted Me i, ...
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Lidar Odometry Factor When a new lidar scan arrives, we first perform feature extraction.
- **p. 1 / Abstract - extractive body cue:** We propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIO-SAM, that achieves highly accurate, real-time mobile robot trajectory estimation and map-building.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We seek to estimate the state of the robot and its trajectory using the observations of these sensors.
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** each feature in ′Fe i+1 or ′Fp i+1, we then find its edge or planar correspondence in Me i or Mp i .
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** When a new state xi+1 is added to the factor graph, we first search the graph and find the prior states that are close to ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets. | p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Since we extract two types of features in the previous feature extraction step, Mi is composed of two subvoxel maps that are ... | p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Lidar Odometry Factor When a new lidar scan arrives, we first perform feature extraction. | p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Note that without loss of generality, the proposed system can also incorporate measurements from other sensors, such as elevation from an altimeter or heading from ...
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Besides its efficiency, applying IMU preintegration also naturally gives us one type of constraint for the factor graph - IMU preintegration factors.
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** The GaussNewton method is then used to solve for the optimal transformation by minimizing: min Ti+1  X pe i+1,k∈′Fe i+1 dek + X pp ...
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** 3) Relative transformation: The distance between a feature and its edge or planar patch correspondence can be computed using the following equations: dek =
- **p. 1 / I. INTRODUCTION - extractive body cue:** This collection of factors from various sources is used for joint optimization of the graph.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Its online optimization process becomes less efficient when this voxel map becomes dense in a feature-rich environment.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | seek, estimate, state, robot, trajectory, observations, sensors, estimation, localization, mapping, fundamental, prerequisites, successful, intelligent | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | seek, estimate, state, robot, trajectory, observations, sensors, estimation, localization, mapping | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Scan-matching, local, scale, instead, global, significantly, improves, real-time, performance, system | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Note, without, loss, generality, system, incorporate, measurements, other, sensors, elevation | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We seek to estimate the state of the robot and its trajectory using the observations of these sensors.
- **p. 1 / I. INTRODUCTION - extractive body cue:** State estimation, localization and mapping are fundamental prerequisites for a successful intelligent mobile robot, required for feedback control, obstacle avoidance, and planning, among many other ...
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Since we extract two types of features in the previous feature extraction step, Mi is composed of two subvoxel maps that are denoted Me i, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Many lidar-based state estimation and mapping methods have been proposed in the last two decades.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** This state estimation problem can be formulated as a maximum a posteriori (MAP) problem.
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** A new robot state node x is added to the graph when the change in robot pose exceeds a user-defined threshold.
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Throughout this paper, we choose the index m to be 12, and the search distance for loop closures is set to be 15m from a ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Adding keyframes in this way not only achieves a balance between map density and memory consumption but also helps maintain a relatively ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIO-SAM, that achieves highly accurate, real-time mobile robot trajectory ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | Adding keyframes in this way not only achieves a balance between map density and memory consumption but also helps maintain a relatively ... | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | In other words, some lidar frames are dropped if the runtime takes more than 100ms when the lidar rotation rate is 10Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** factor, graph, model, problem, better, suited, perform, inference, when, compared, Bayes, nets, Since, extract, types, features, previous, feature, extraction, step.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Similar to the problems encountered in the Park dataset, LIO-GPS is unable to close the loop when returning to the robot's initial ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Global / local decision | The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without ... | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Motion execution / recovery | The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without ... | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We note that only the CPU is used for computation, without parallel computing enabled.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Because LIOM uses the same initialization pipeline from [25], it inherits the same initialization sensitivity of visual-inertial SLAM and is not able to initialize properly ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Without the correction of GPS data, the trajectory of LIO-odom begins to visibly drift at the lower right corner of the map.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** LIO-SAM produces a map that is consistent with the Google Earth imagery, without using GPS. mapping area, GPS reception is rarely available and inaccurate most ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Results of various methods using the Campus dataset that is gathered on the MIT campus. The red dot indicates the start and end ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The results of LIOM are not shown due to its failure to initialize properly and produce meaningful results.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (Abstract), p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA), objective p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), temporal p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (Abstract), p. 1 (Abstract), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
