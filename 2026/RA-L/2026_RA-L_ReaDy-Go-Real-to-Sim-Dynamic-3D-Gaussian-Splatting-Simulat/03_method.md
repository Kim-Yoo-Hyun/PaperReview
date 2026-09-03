# Method - ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.11575; PDF retrieval source: https://arxiv.org/pdf/2602.11575. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD)): The pipeline consists of three main components: (1) a real-to-sim dynamic 3D Gaussian Splatting (GS) simulator, (2) dynamic navigation dataset generation using the simulator and planners, and (3) navigation policy ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** The pipeline consists of three main components: (1) a real-to-sim dynamic 3D Gaussian Splatting (GS) simulator, (2) dynamic navigation dataset generation using the simulator and ...
- **p. 4 / III. METHOD - extractive body cue:** By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation policy.
- **p. 3 / III. METHOD - extractive body cue:** The human animation module places an animatable human GS model in the scene and then generates plausible human motion along a given obstacle trajectory.
- **p. 4 / III. METHOD - extractive body cue:** integrates our dynamic GS simulator, a robot expert planner designed for dynamic GS representations, and a human planner.
- **p. 3 / III. METHOD - extractive body cue:** Specifically, we employed PGSR [24] for 3D scene reconstruction, which achieves high-quality surface reconstruction and rendering by compressing 3D Gaussians into flat planes and using ...
- **p. 3 / III. METHOD - extractive body cue:** Given a video of a static target deployment environment, ReaDy-Go generates photorealistic navigation datasets with moving human obstacles and trains an environment-specific navigation policy, as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** RGB-only navigation models typically learn nonlinear visuomotor policies from high-dimensional monocular observations, where depth ambiguity complicates scene understanding.
- **p. 2 / I. INTRODUCTION - extractive body cue:** It unifies scene GS, animatable human GS avatars, and motion generation within a coherent dynamic simulator. • Photorealistic Dynamic Dataset Generation Pipeline: We propose a ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** The framework consists of three key components: (1) a dynamic GS simulator that integrates a static scene GS, an animatable human GS obstacle, and a ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** By reconstructing environments from RGB videos, GS enables high-fidelity rendering at fast frame rates, novel view synthesis, and simulation with an explicit 3D scene representation.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are threefold. • Dynamic GS Simulator: We develop a photorealistic realto-sim dynamic 3D Gaussian Splatting simulator with human GS obstacles.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** The pipeline consists of three main components: (1) a real-to-sim dynamic 3D Gaussian Splatting (GS) simulator, (2) dynamic navigation dataset generation using the simulator and ...
- **p. 4 / III. METHOD - extractive body cue:** By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation policy.
- **p. 3 / III. METHOD - extractive body cue:** The human animation module places an animatable human GS model in the scene and then generates plausible human motion along a given obstacle trajectory.
- **p. 4 / III. METHOD - extractive body cue:** integrates our dynamic GS simulator, a robot expert planner designed for dynamic GS representations, and a human planner.
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The pipeline consists of three main components: (1) a real-to-sim dynamic 3D Gaussian Splatting (GS) simulator, (2) dynamic navigation dataset generation using ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The human animation module places an animatable human GS model in the scene and then generates plausible human motion along a given ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** Specifically, we employed PGSR [24] for 3D scene reconstruction, which achieves high-quality surface reconstruction and rendering by compressing 3D Gaussians into flat planes and using ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | leveraging, simulator, planners, pipeline, collects, RGB, observations, actions, relative, goal, positions, training, samples, navigation | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | leveraging, simulator, planners, pipeline, collects, RGB, observations, actions, relative, goal | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | framework, consists, three, components, dynamic, simulator, integrates, static, scene, animatable | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Specifically, employed, PGSR, scene, reconstruction, achieves, high-quality, surface, rendering, compressing | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. METHOD - extractive body cue:** By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation policy.
- **p. 3 / III. METHOD - extractive body cue:** Given a video of a static target deployment environment, ReaDy-Go generates photorealistic navigation datasets with moving human obstacles and trains an environment-specific navigation policy, as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** RGB-only navigation models typically learn nonlinear visuomotor policies from high-dimensional monocular observations, where depth ambiguity complicates scene understanding.
- **p. 2 / I. INTRODUCTION - extractive body cue:** It unifies scene GS, animatable human GS avatars, and motion generation within a coherent dynamic simulator. • Photorealistic Dynamic Dataset Generation Pipeline: We propose a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The framework consists of three key components: (1) a dynamic GS simulator that integrates a static scene GS, an animatable human GS obstacle, and a ...
- **p. 3 / III. METHOD - extractive body cue:** Given a 2D trajectory, we convert it into body root linear and rotation velocities, normalize them to match the HumanML3D [29] representation as the model ...
- **p. 4 / III. METHOD - extractive body cue:** This data generation process does not require onerous procedures such as scene mesh extraction and physics engine integration.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | Then, the predicted 3D body joint positions are fitted to SMPL parameters through SMPLify [30] and transformed into the world coordinate frame ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | For each episode, the start/goal pairs are sampled randomly in the free space of the environment. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | For each task and environment, we evaluate 100 episodes in simulation and 10 episodes in real-world experiments. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. METHOD - extractive body cue:** The pipeline consists of three main components: (1) a real-to-sim dynamic 3D Gaussian Splatting (GS) simulator, (2) dynamic navigation dataset generation using the simulator and ...
- **p. 4 / III. METHOD - extractive body cue:** By leveraging the simulator and planners, the pipeline collects RGB observations, actions, and relative goal positions as training samples for a navigation policy.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** The policy predicts the action (v, w) and is trained with the Adam optimizer with a learning rate of 10-4.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** pipeline, consists, three, main, components, real-to-sim, dynamic, Gaussian, Splatting, simulator, navigation, dataset, generation, planners, policy, training, leveraging, collects, RGB, observations.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | For each task and environment, we evaluate 100 episodes in simulation and 10 episodes in real-world experiments. | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Global / local decision | For a fair comparison with image-goal navigation baselines (GNM, ViNT, and NoMaD), we provide them goal images captured at goal positions within ... | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Motion execution / recovery | As in simulation, ReaDy-Go and Vid2Sim achieve comparable success rates in Static, but their performance diverges in Dynamic. | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** 3) Baselines: We compare the following baselines against ReaDy-Go visual navigation policies to evaluate the effect of photorealistic dynamic GS simulation data for target deployment ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** To isolate the effect of photorealistic dynamic obstacles on navigation policies, we employ the same policy architecture, human trajectories, and expert planner for both Vid2Sim ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** First, the proposed human animation module generates plausible body motions for human GS avatars within static GS scenes along given 2D trajectories, without relying on ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: ReaDy-Go overview. The proposed photorealistic simulation pipeline for visual navigation in dynamic environments consists of three main components: (1) a real-to-sim dynamic 3D ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** ReaDy-Go yields fewer failures than the baselines, especially in failure modes related to dynamic obstacle avoidance, including Dynamic obstacle collision and Static collision during detour.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Second, while ReaDy-Go and Vid2Sim showed similar numbers of failures in cases unrelated to dynamic obstacle interactions, ReaDy-Go was more robust in situations involving dynamic ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Visualization of the robot expert planner. (a) The robot follows a collision-free path (red) from start (green) to goal (blue). (b) When a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), objective p. 3 (III. METHOD), temporal p. 3 (III. METHOD), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 4 (1) Static scene voxelization with opacity filtering for plan).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
