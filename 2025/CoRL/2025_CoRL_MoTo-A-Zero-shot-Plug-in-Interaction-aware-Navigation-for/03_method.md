# Method - MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/wu25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25c/wu25c.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (4 Approach), p. 5 (4 Approach), p. 5 (4 Approach), p. 7 (4 Approach), p. 4 (4 Approach), p. 4 (4 Approach)): Firstly, extracting the wrist keypoint from the RGB-D observation sw t , then projecting it to 3D space using Et.

## Method Body Digest

- **p. 6 / 4 Approach - extractive PDF cue:** Firstly, extracting the wrist keypoint from the RGB-D observation sw t , then projecting it to 3D space using Et.
- **p. 5 / 4 Approach - extractive PDF cue:** VLM(Tk, {Ik 1 , ..., Ik m}) generates target keypoint proposals in different images, which are then aggregated with a voting module V.
- **p. 5 / 4 Approach - extractive PDF cue:** Current segmentation models can only segment a laptop into screen and keyboard, and a table into surface and legs, which cannot provide detailed, actionable locations.
- **p. 7 / 4 Approach - extractive PDF cue:** Specifically, we generate initial solution proposals for the next time step from the search space and calculate the cost relative to the optimization objective for ...
- **p. 4 / 4 Approach - extractive PDF cue:** Similarly, the robot must choose context-specific interaction points.
- **p. 4 / 4 Approach - extractive PDF cue:** Determining how and where to move is a non-trivial problem that cannot be solved by a pure navigation policy.
- **p. 6 / 4 Approach - extractive PDF cue:** For dual-arm robots, both arms may output keypoints, which confuses the following optimization process.
- **p. 5 / 4 Approach - extractive PDF cue:** Therefore, the robot's action (abase t , {aarm t }) can be solved as an optimization problem, which aims to minimize the distance between TK ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- **p. 3 / 1 Introduction - extractive PDF cue:** Inspired by ReKep, we propose a multi-view voting strategy to generate scene-level interaction keypoints to fine-grain guide mobile manipulation trajectory generation.
- **p. 5 / 4 Approach - extractive PDF cue:** Therefore, we propose a two-stage VLM-based method to generate keypoints for an image, which is divided into keypoint proposal stage and keypoint selection stage.

## Source Evidence Cues

- **p. 6 / 4 Approach - extractive PDF cue:** Firstly, extracting the wrist keypoint from the RGB-D observation sw t , then projecting it to 3D space using Et.
- **p. 5 / 4 Approach - extractive PDF cue:** VLM(Tk, {Ik 1 , ..., Ik m}) generates target keypoint proposals in different images, which are then aggregated with a voting module V.
- **p. 5 / 4 Approach - extractive PDF cue:** Current segmentation models can only segment a laptop into screen and keyboard, and a table into surface and legs, which cannot provide detailed, actionable locations.
- **p. 7 / 4 Approach - extractive PDF cue:** Specifically, we generate initial solution proposals for the next time step from the search space and calculate the cost relative to the optimization objective for ...
- **p. 4 / 4 Approach - extractive PDF cue:** Similarly, the robot must choose context-specific interaction points.
- **p. 4 / 4 Approach - extractive PDF cue:** Determining how and where to move is a non-trivial problem that cannot be solved by a pure navigation policy.
- **p. 6 / 4 Approach - extractive PDF cue:** For dual-arm robots, both arms may output keypoints, which confuses the following optimization process.
- **Detected method headings:** 4 Approach (p. 4); C Optimization Algorithm (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | Firstly, extracting the wrist keypoint from the RGB-D observation sw t , then projecting it to 3D space using Et. | p. 6 (4 Approach), p. 5 (4 Approach) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | VLM(Tk, {Ik 1 , ..., Ik m}) generates target keypoint proposals in different images, which are then aggregated with a voting module ... | p. 5 (4 Approach), p. 5 (4 Approach) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | Current segmentation models can only segment a laptop into screen and keyboard, and a table into surface and legs, which cannot provide ... | p. 5 (4 Approach), p. 7 (4 Approach) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4 Approach - extractive PDF cue:** Therefore, the robot's action (abase t , {aarm t }) can be solved as an optimization problem, which aims to minimize the distance between TK ...
- **p. 7 / 4 Approach - extractive PDF cue:** Specifically, we generate initial solution proposals for the next time step from the search space and calculate the cost relative to the optimization objective for ...
- **p. 7 / 4 Approach - extractive PDF cue:** Method Partial Success Rates Overall SR Average SR FindObj (↑) Pick (↑) FindRec (↑) Cost w/o Collision 66.93% 60.95% 49.24% 18.50% 48.91% w/o Smoothness 66.76% ...
- **p. 13 / A.3 Training Details - extractive PDF cue:** We fine-tuned the model for 150,000 gradient steps on 8 NVIDIA RTX 4090 GPUs (total batch size 128) using the AdamW optimizer (learning rate 1×10-4, ...
- **p. 6 / 4 Approach - extractive PDF cue:** We formulate three cost functions to achieve this: Ct(θbase t , {θarm t }) = Fc t + Fs t + Fm t (7) Collision ...
- **p. 6 / 4 Approach - extractive PDF cue:** Otherwise, the collision cost will not influence the control of the robot.
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 5 (4 Approach), p. 6 (4 Approach), p. 6 (4 Approach), p. 7 (4 Approach), p. 7 (4 Approach), p. 13 (A.3 Training Details).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | robot, scanning, RGB-D, observation, scene, point, clouds, graphs, utilize, VLM, multi-view, consistency, voting, interaction | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | robot, scanning, RGB-D, observation, scene, point, clouds, graphs, utilize, VLM | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | solve, problem, mobile, manipulation, interaction-aware, navigation, policy, namely, Move, Touch | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | Therefore, robot, action, abase, aarm, solved, optimization, problem, aims, minimize | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 1 Introduction - extractive PDF cue:** Based on robot scanning RGB-D observation to get 3D scene point clouds and graphs, we utilize VLM and multi-view consistency voting to get interaction keypoints, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- **p. 2 / 1 Introduction - extractive PDF cue:** The proposed interaction-aware navigation policy generates suitable base docking points for the robot to successfully perform manipulation, which are inspired by the fact that the ...
- **p. 3 / 1 Introduction - extractive PDF cue:** 21, 22] directly map visual observations to the mobile manipulation action space.
- **p. 3 / 1 Introduction - extractive PDF cue:** At each time step t, the robot receives RGB-D observations (se t, {sw t }), and executes actions (abase t , {aarm t }), where ...
- **p. 5 / 4 Approach - extractive PDF cue:** Without any language information, we aim to find out all representative actionable points in an image as proposals.
- **p. 4 / 4 Approach - extractive PDF cue:** To accurately ground instruction T to objects in the scene, we first let the robot scan the whole scene and reconstruct a 3D point cloud ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | At each time step t, the robot receives RGB-D observations (se t, {sw t }), and executes actions (abase t , {aarm ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | Specifically, we generate initial solution proposals for the next time step from the search space and calculate the cost relative to the ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | We fine-tuned the model for 150,000 gradient steps on 8 NVIDIA RTX 4090 GPUs (total batch size 128) using the AdamW optimizer ... | hardware, batch and throughput |

## Training vs Inference

- **p. 13 / A.3 Training Details - extractive PDF cue:** We fine-tuned the model for 150,000 gradient steps on 8 NVIDIA RTX 4090 GPUs (total batch size 128) using the AdamW optimizer (learning rate 1×10-4, ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Firstly, extracting, wrist, keypoint, RGB-D, observation, then, projecting, space, VLM, generates, target, proposals, different, images, aggregated, voting, module, Current, segmentation.
- **Relevant PDF headings:** 4 Approach (p. 4); C Optimization Algorithm (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | The OVMM benchmark consists of 60 extensive indoor scenes and contains more than 18k 3D models of everyday objects.OVMM utilizes Hello Robot ... | p. 13 (A.1 Simulator Experiment), p. 13 (A.2 Real World Experiment) |
| Base-arm task decision | 5.1 Comparison with State-of-the-art Methods Table 1 demonstrates the performance of MoTo on the OVMM [18] validation set compared to the baseline, ... | p. 7 (5 Experiment), p. 7 (5 Experiment) |
| Execution / correction | All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each ... | p. 8 (5 Experiment), p. 7 (5 Experiment) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation experiments for optimization cost terms and keypoint generation variants.
- **p. 7 / 5 Experiment - extractive PDF cue:** The similar success rates in stages FindObj and Pick are due to MoTo's focus on interaction-aware navigation, which is invoked only after finding a container ...
- **p. 8 / 5 Experiment - extractive PDF cue:** We further investigated variants of the keypoint extraction and fusion pipeline.
- **p. 8 / 5 Experiment - extractive PDF cue:** 5.2 Ablation Study Table 2 reports a systematic ablation of our full MoTo pipeline in OVMM, isolating the contribution of each optimization cost term and ...
- **p. 13 / A.1 Simulator Experiment - extractive PDF cue:** We utilize an OVMM-heuristic baseline to collect manipulation expert trajectories that include robot proprioception, action, and visual observations to fine-tune off-the-shelf manipulation foundation models.
- **p. 13 / A.3 Training Details - extractive PDF cue:** To better fine-tune OpenVLA [11] to mitigate cross-robot ontology differences, we collected a total of 20k data and fine-tuned 10k epoch on 8 RTX 3090 ...
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into 3D space and votes to generate keypoints ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (4 Approach), p. 5 (4 Approach), p. 5 (4 Approach), p. 7 (4 Approach), p. 4 (4 Approach), p. 4 (4 Approach), objective p. 5 (4 Approach), p. 7 (4 Approach), p. 7 (4 Approach), p. 13 (A.3 Training Details), p. 6 (4 Approach), p. 6 (4 Approach), temporal p. 3 (1 Introduction), p. 7 (4 Approach), p. 8 (5 Experiment), p. 13 (A.2 Real World Experiment), p. 13 (A.3 Training Details), p. 1 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
