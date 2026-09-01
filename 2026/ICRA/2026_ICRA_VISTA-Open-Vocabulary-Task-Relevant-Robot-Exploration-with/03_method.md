# Method - VISTA: Open-Vocabulary, Task-Relevant Robot Exploration with Online Semantic Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html; PDF retrieval source: https://arxiv.org/pdf/2507.01125. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION)): The robot's motion is then modeled as a planar single integrator with a heading angle in the yaw direction.

## Method Body Digest

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** The robot's motion is then modeled as a planar single integrator with a heading angle in the yaw direction.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We consider a robotic exploration problem in which a robot has an onboard, forward-facing RGB-D camera with reliable state estimation.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** As the map updates, we assume that the motion of the robot is restricted in the z, ϕ, and θ axes.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** As the robot moves, it collects full pose odometry information along with RGB and depth images in order to train a 3DGS map of the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** the robot's environment online using a Gaussian Splatting (3DGS) representation [5].1 To enable open-vocabulary, taskrelevant robot exploration, VISTA distills semantic features from vision-language models, e.g., ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Once the robot receives the input query, it must then construct a map of its environment as it moves, while simultaneously searching for the query ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through an experimental campaign with a total of 36 hardware executions, we show that VISTA outperforms state-of-the-art baselines, achieving 6x better success rates in environments ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Real-time sensor data is gathered from a robot hardware platform to train a semantic 3DGS map.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present VISTA, an algorithm for Viewpoint-based Image Selection with Semantic Task Awareness.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We introduce: 1) an efficient information metric that combines view angle diversity and semantic task relevance stored on a voxel grid that can be recursively ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through an experimental campaign with a total of 36 hardware executions, we show that VISTA outperforms state-of-the-art baselines, achieving 6x better success rates in environments ...

## Source Evidence Cues

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** The robot's motion is then modeled as a planar single integrator with a heading angle in the yaw direction.
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** We consider a robotic exploration problem in which a robot has an onboard, forward-facing RGB-D camera with reliable state estimation.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The robot's motion is then modeled as a planar single integrator with a heading angle in the yaw direction. | p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We consider a robotic exploration problem in which a robot has an onboard, forward-facing RGB-D camera with reliable state estimation. | p. 3 (III. PROBLEM FORMULATION) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The robot's motion is then modeled as a planar single integrator with a heading angle in the yaw direction. | p. 3 (III. PROBLEM FORMULATION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** As the map updates, we assume that the motion of the robot is restricted in the z, ϕ, and θ axes.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (III. PROBLEM FORMULATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | robot, moves, collects, full, pose, odometry, information, along, RGB, depth, images, order, train, DGS | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | robot, moves, collects, full, pose, odometry, information, along, RGB, depth | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | present, VISTA, algorithm, Viewpoint-based, Image, Selection, Semantic, Task, Awareness, introduce | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | updates, assume, motion, robot, restricted, axes | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** As the robot moves, it collects full pose odometry information along with RGB and depth images in order to train a 3DGS map of the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** the robot's environment online using a Gaussian Splatting (3DGS) representation [5].1 To enable open-vocabulary, taskrelevant robot exploration, VISTA distills semantic features from vision-language models, e.g., ...
- **p. 3 / III. PROBLEM FORMULATION - extractive body cue:** Once the robot receives the input query, it must then construct a map of its environment as it moves, while simultaneously searching for the query ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Through an experimental campaign with a total of 36 hardware executions, we show that VISTA outperforms state-of-the-art baselines, achieving 6x better success rates in environments ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Real-time sensor data is gathered from a robot hardware platform to train a semantic 3DGS map.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The semantic and RGB information from the 3DGS map are transferred to a 3D Voxel Grid, and training poses are used to store geometric information ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The robot navigates its environment by planning receding-horizon trajectories that prioritize semantic similarity to the query and exploration of unseen regions of ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The trajectory with the highest semantic + geometric information gain is then executed in a receding horizon loop. semantic information that can ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In each voxel, the geometric uncertainty is the minimum angular separation between the test viewpoint and all view angles from which that ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | For pose feedback, we use an OptiTrack external motion capture system, and all 3DGS training and planning is done on a desktop ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / V. RESULTS - extractive body cue:** For pose feedback, we use an OptiTrack external motion capture system, and all 3DGS training and planning is done on a desktop computer that has ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** robot, motion, then, modeled, planar, single, integrator, heading, angle, direction, consider, robotic, exploration, problem, onboard, forward-facing, RGB-D, camera, reliable, state.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate each method across six scenes: three benchmark scenes in Nerfstudio (Plane, Kitchen, and Poster) and three additional datasets (Flight, Clutter, ... | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Semantic / temporal fusion | The results suggest that our method is able to outperform both baselines on both maps because we reason about both semantic and ... | p. 6 (V. RESULTS), p. 6 (V. RESULTS) |
| Robot query / planning handoff | On the more challenging map domain, we find that our method has a significant improvement over the baseline methods, where our method ... | p. 6 (V. RESULTS), p. 6 (V. RESULTS) |

## Failure and Ablation Link

- **p. 5 / V. RESULTS - extractive body cue:** We evaluate each method using the standard metrics: Peak-Signal-Noise-Ratio (PSNR), Learned Perceptuation Image Patch Similarity (LPIPS), and Structural Similarity Index Measure (SSIM).
- **p. 6 / V. RESULTS - extractive body cue:** Through these experiments, we find that all methods have some successes on the easy low-occlusion map domain.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. The top row shows our three environments and two robots, with the search object in a green circle. The second row shows an ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. PROBLEM FORMULATION), p. 3 (III. PROBLEM FORMULATION), objective p. 3 (III. PROBLEM FORMULATION), temporal p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (IV. VISTA), p. 2 (I. INTRODUCTION), p. 3 (IV. VISTA).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
