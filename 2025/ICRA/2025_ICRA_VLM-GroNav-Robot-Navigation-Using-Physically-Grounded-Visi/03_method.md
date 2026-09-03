# Method - VLM-GroNav: Robot Navigation Using Physically Grounded Vision-Language Models in Outdoor Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.proceedings.com/content/081/081087webtoc.pdf; PDF retrieval source: https://arxiv.org/pdf/2409.20445v1. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. OUR APPROACH), p. 5 (IV. OUR APPROACH), p. 6 (A method), p. 4 (IV. OUR APPROACH), p. 5 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH)): We propose a novel navigation method that integrates Vision-Language Models (VLMs) with proprioceptive sensing to enable adaptive and robust navigation across complex outdoor terrains.

## Method Body Digest

- **p. 3 / IV. OUR APPROACH - extractive body cue:** We propose a novel navigation method that integrates Vision-Language Models (VLMs) with proprioceptive sensing to enable adaptive and robust navigation across complex outdoor terrains.
- **p. 5 / IV. OUR APPROACH - extractive body cue:** To integrate terrain traversability into the planning process, we introduce a new cost term, the frontier cost, into the DWA's objective function.
- **p. 6 / A method - extractive body cue:** All metrics are averaged over both the successful and unsuccessful trails (reaching the goal). • ViNT [50]: A general-purpose foundation model for visual navigation that ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The VLM is then prompted with this marked image and a navigation objective Tobjective to select the optimal sequence of waypoints that lead to the ...
- **p. 5 / IV. OUR APPROACH - extractive body cue:** The updated waypoints Wnew are then passed to the local planner.
- **p. 3 / IV. OUR APPROACH - extractive body cue:** The core components of our method are: (a) Traversability Estimation using Proprioception-based sensing; (b) Physically Grounded Reasoning Module; (c) HighLevel Global Planner; (d) Adaptive Local ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The global planner uses these refined estimates to generate optimal waypoints visually marked on the aerial image to guide the robot toward the goal while ...
- **p. 5 / A method - extractive body cue:** that uses semantic segmentation-based terrain understanding to generate traversability costs for navigation. • CoNVOI [51]: A method that uses Vision Language Models (VLMs) to generate ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** Main contributions: We present VLM-GroNav, a novel navigation method that integrates Vision-Language Models (VLMs) with proprioception-based sensing.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This process allows for dynamic trajectory re-planning, informed by both visual cues and updated traversability estimates. • A real-time adaptive local planner: We introduce a ...
- **p. 3 / IV. OUR APPROACH - extractive body cue:** We propose a novel navigation method that integrates Vision-Language Models (VLMs) with proprioceptive sensing to enable adaptive and robust navigation across complex outdoor terrains.

## Source Evidence Cues

- **p. 3 / IV. OUR APPROACH - extractive body cue:** We propose a novel navigation method that integrates Vision-Language Models (VLMs) with proprioceptive sensing to enable adaptive and robust navigation across complex outdoor terrains.
- **p. 5 / IV. OUR APPROACH - extractive body cue:** To integrate terrain traversability into the planning process, we introduce a new cost term, the frontier cost, into the DWA's objective function.
- **p. 6 / A method - extractive body cue:** All metrics are averaged over both the successful and unsuccessful trails (reaching the goal). • ViNT [50]: A general-purpose foundation model for visual navigation that ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The VLM is then prompted with this marked image and a navigation objective Tobjective to select the optimal sequence of waypoints that lead to the ...
- **p. 5 / IV. OUR APPROACH - extractive body cue:** The updated waypoints Wnew are then passed to the local planner.
- **p. 3 / IV. OUR APPROACH - extractive body cue:** The core components of our method are: (a) Traversability Estimation using Proprioception-based sensing; (b) Physically Grounded Reasoning Module; (c) HighLevel Global Planner; (d) Adaptive Local ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The global planner uses these refined estimates to generate optimal waypoints visually marked on the aerial image to guide the robot toward the goal while ...
- **Detected method headings:** IV. OUR APPROACH (p. 3); A method (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | We propose a novel navigation method that integrates Vision-Language Models (VLMs) with proprioceptive sensing to enable adaptive and robust navigation across complex ... | p. 3 (IV. OUR APPROACH), p. 5 (IV. OUR APPROACH) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | To integrate terrain traversability into the planning process, we introduce a new cost term, the frontier cost, into the DWA's objective function. | p. 5 (IV. OUR APPROACH), p. 6 (A method) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | All metrics are averaged over both the successful and unsuccessful trails (reaching the goal). • ViNT [50]: A general-purpose foundation model for ... | p. 6 (A method), p. 4 (IV. OUR APPROACH) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / IV. OUR APPROACH - extractive body cue:** To integrate terrain traversability into the planning process, we introduce a new cost term, the frontier cost, into the DWA's objective function.
- **p. 5 / A method - extractive body cue:** that uses semantic segmentation-based terrain understanding to generate traversability costs for navigation. • CoNVOI [51]: A method that uses Vision Language Models (VLMs) to generate ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** (5) We use in-context learning [29] to refine terrain traversability and navigation cost estimates.
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The global planner uses these refined estimates to generate optimal waypoints visually marked on the aerial image to guide the robot toward the goal while ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 5 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH), p. 5 (IV. OUR APPROACH).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | leverages, VLMs, process, visual, inputs, aerial, imagery, front, camera, views, integrates, real-time, feedback, robot | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | leverages, VLMs, process, visual, inputs, aerial, imagery, front, camera, views | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Main, contributions, present, VLM-GroNav, novel, navigation, integrates, Vision-Language, Models, VLMs | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | integrate, terrain, traversability, planning, process, introduce, cost, term, frontier, DWA | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / IV. OUR APPROACH - extractive body cue:** It leverages VLMs to process visual inputs (aerial imagery and front camera views), and integrates real-time feedback from the robot's local sensors.
- **p. 3 / III. BACKGROUND - extractive body cue:** The global planner leverages aerial imagery and GPS to generate high-level global waypoints, while the local planner uses real-time sensory feedback, including proprioception to adjust ...
- **p. 4 / IV. OUR APPROACH - extractive body cue:** 2: The VLM-GroNav system employs a reasoning module that integrates visual inputs from aerial imagery, weather conditions, and proprioceptive data through a large VLM to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** This process allows for dynamic trajectory re-planning, informed by both visual cues and updated traversability estimates. • A real-time adaptive local planner: We introduce a ...
- **p. 5 / IV. OUR APPROACH - extractive body cue:** Adaptive Local Planner Our local planner adapts in real-time to changes in terrain traversability by integrating proprioceptive feedback with a light VLM (with low inference ...
- **p. 3 / IV. OUR APPROACH - extractive body cue:** We propose a novel navigation method that integrates Vision-Language Models (VLMs) with proprioceptive sensing to enable adaptive and robust navigation across complex outdoor terrains.
- **p. 6 / A method - extractive body cue:** All metrics are averaged over both the successful and unsuccessful trails (reaching the goal). • ViNT [50]: A general-purpose foundation model for visual navigation that ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At each time step, candidate trajectories are propagated over a fixed horizon ∆T, and each trajectory is evaluated by minimizing an objective ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | We use the updated traversability estimations to inform both the local and global planners for real-time trajectory replanning. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | The Ghost Vision 60 is equipped with a front-facing wide-angle camera, an OS1-32 LiDAR, GPS, and an onboard Intel NUC 11 system, ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / A method - extractive body cue:** All metrics are averaged over both the successful and unsuccessful trails (reaching the goal). • ViNT [50]: A general-purpose foundation model for visual navigation that ...
- **p. 5 / IV. OUR APPROACH - extractive body cue:** Adaptive Local Planner Our local planner adapts in real-time to changes in terrain traversability by integrating proprioceptive feedback with a light VLM (with low inference ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** novel, navigation, integrates, Vision-Language, Models, VLMs, proprioceptive, sensing, enable, adaptive, robust, across, complex, outdoor, terrains, integrate, terrain, traversability, planning, process.
- **Relevant PDF headings:** IV. OUR APPROACH (p. 3); A method (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Implementation For the real-world experiments, we utilize both the Ghost Vision 60 legged robot and the Clearpath Husky wheeled robot. | p. 5 (V. RESULTS AND ANALYSIS), p. 5 (V. RESULTS AND ANALYSIS) |
| Global / local decision | Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]: | p. 5 (V. RESULTS AND ANALYSIS), p. 5 (Figure/Table caption) |
| Motion execution / recovery | Fig. 1: Overview of our VLM-GroNav system: Our method uses the given information to achieve a navigation objective. We leverage VLMs and ... | p. 1 (Figure/Table caption), p. 6 (3. VLM-GroNav consistently achieves the highest success) |

## Failure and Ablation Link

- **p. 6 / 3. VLM-GroNav consistently achieves the highest success - extractive body cue:** We observe that this results in errors in predicting the terrain's traversbility while navigating, which in turn ill-informs the local and global planners, causing failures.
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The difference between these measurements reflects the degree of slippage experienced by the robot.
- **p. 4 / IV. OUR APPROACH - extractive body cue:** The traversability indicator (τsinkage and τslip) are time-shifted to match the visual inputs, τshifted(t) = τ(t -∆t).
- **p. 5 / V. RESULTS AND ANALYSIS - extractive body cue:** Comparison Methods • DWA [30]: A baseline motion planner that performs simple collision avoidance and goal-reaching behaviors. • GA-Nav [4]:
- **p. 6 / 3. VLM-GroNav consistently achieves the highest success - extractive body cue:** Scenarios 3 and 4 involve the wheeled robot navigating through unstructured and slippery terrains, VLM-GroNav excels at maintaining a high success rate and reduced IMU ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. OUR APPROACH), p. 5 (IV. OUR APPROACH), p. 6 (A method), p. 4 (IV. OUR APPROACH), p. 5 (IV. OUR APPROACH), p. 3 (IV. OUR APPROACH), objective p. 5 (IV. OUR APPROACH), p. 5 (A method), p. 4 (IV. OUR APPROACH), p. 4 (IV. OUR APPROACH), temporal p. 3 (III. BACKGROUND), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (II. RELATED WORK), p. 3 (II. RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
