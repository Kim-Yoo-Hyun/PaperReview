# Method - ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=6bKEWevgSd; PDF retrieval source: https://arxiv.org/pdf/2412.13211. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 8 (5 METHODOLOGY), p. 8 (5 METHODOLOGY), p. 6 (5 METHODOLOGY), p. 6 (5 METHODOLOGY), p. 7 (5 METHODOLOGY), p. 7 (5 METHODOLOGY)): (2016), then concatenated with state observations.

## Method Body Digest

- **p. 8 / 5 METHODOLOGY - extractive PDF cue:** (2016), then concatenated with state observations.
- **p. 8 / 5 METHODOLOGY - extractive PDF cue:** First, we define "events" which occur at any timestep t: 1) Contact: nonzero robot/target pairwise force, 2) Grasped: object not grasped at step t-1 and ...
- **p. 6 / 5 METHODOLOGY - extractive PDF cue:** Furthermore, the policy must learn action sequences which can reach these grasp poses and retrieve the target object within the specified horizon while keeping the ...
- **p. 6 / 5 METHODOLOGY - extractive PDF cue:** 5.1 TRAINING REINFORCEMENT LEARNING POLICIES We choose Reinforcement Learning (RL) to learn our subtask policies as RL does not require prior demonstration data, and it ...
- **p. 7 / 5 METHODOLOGY - extractive PDF cue:** Visual observations are encoded by a NatureCNN (Mnih et al., 2015) and concatenated with state observations.
- **p. 7 / 5 METHODOLOGY - extractive PDF cue:** Algorithms and Hyperparameters: We stack 3 consecutive frames for image observations to handle partial observability.
- **p. 19 / A.4.3 SAC VS PPO FOR RL TRAINING - extractive PDF cue:** For consistency, we use the same RL algorithm across all Open and Close variants.
- **p. 6 / 5 METHODOLOGY - extractive PDF cue:** As a result, learning successful grasping for multiple objects with different geometries - in addition to whole body control with collision constraints - is difficult.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** We present MS-HAB1, a holistic, open-sourced, home-scale manipulation benchmark with four key features: (1) fast simulation with realistic physics and manipulation, including low-level control, for ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Summary of Contributions: The contributions of MS-HAB are summarized as follows: 1) GPUaccelerated HAB implementation which supports realistic low-level control and achieves over 4300 SPS ...

## Source Evidence Cues

- **p. 8 / 5 METHODOLOGY - extractive PDF cue:** (2016), then concatenated with state observations.
- **p. 8 / 5 METHODOLOGY - extractive PDF cue:** First, we define "events" which occur at any timestep t: 1) Contact: nonzero robot/target pairwise force, 2) Grasped: object not grasped at step t-1 and ...
- **p. 6 / 5 METHODOLOGY - extractive PDF cue:** Furthermore, the policy must learn action sequences which can reach these grasp poses and retrieve the target object within the specified horizon while keeping the ...
- **p. 6 / 5 METHODOLOGY - extractive PDF cue:** 5.1 TRAINING REINFORCEMENT LEARNING POLICIES We choose Reinforcement Learning (RL) to learn our subtask policies as RL does not require prior demonstration data, and it ...
- **p. 7 / 5 METHODOLOGY - extractive PDF cue:** Visual observations are encoded by a NatureCNN (Mnih et al., 2015) and concatenated with state observations.
- **p. 7 / 5 METHODOLOGY - extractive PDF cue:** Algorithms and Hyperparameters: We stack 3 consecutive frames for image observations to handle partial observability.
- **p. 19 / A.4.3 SAC VS PPO FOR RL TRAINING - extractive PDF cue:** For consistency, we use the same RL algorithm across all Open and Close variants.
- **Detected method headings:** 5 METHODOLOGY (p. 6); A.4.5 PER VS ALL-OBJECT POLICY LONG-HORIZON PERFORMANCE (p. 19); A.4.6 DIFFUSION POLICY BASELINES (p. 21)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | (2016), then concatenated with state observations. | p. 8 (5 METHODOLOGY), p. 8 (5 METHODOLOGY) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | First, we define "events" which occur at any timestep t: 1) Contact: nonzero robot/target pairwise force, 2) Grasped: object not grasped at ... | p. 8 (5 METHODOLOGY), p. 6 (5 METHODOLOGY) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | Furthermore, the policy must learn action sequences which can reach these grasp poses and retrieve the target object within the specified horizon ... | p. 6 (5 METHODOLOGY), p. 6 (5 METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 5 METHODOLOGY - extractive PDF cue:** As a result, learning successful grasping for multiple objects with different geometries - in addition to whole body control with collision constraints - is difficult.
- **p. 6 / 5 METHODOLOGY - extractive PDF cue:** Pick: Without magical grasp, our Pick policies must learn grasp poses which are valid, stable, and reachable within the kinematic constraints of the mobile Fetch ...
- **p. 8 / 5 METHODOLOGY - extractive PDF cue:** As the dataset generation code is publicly available, users have the flexibility to create their own datasets with custom constraints tailored to their specific requirements.
- **p. 7 / 5 METHODOLOGY - extractive PDF cue:** We evaluate long-horizon task success (TidyHouse, PrepareGroceries, SetTable) by Progressive Completion Rate (%).
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 6 (5 METHODOLOGY), p. 6 (5 METHODOLOGY), p. 8 (5 METHODOLOGY), p. 19 (A.4.3 SAC VS PPO FOR RL TRAINING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | provide, brief, descriptions, subtasks, below, Pick, optional, xpose, object, articulation, provided, Place, gpos, goal | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | provide, brief, descriptions, subtasks, below, Pick, optional, xpose, object, articulation | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | present, MS-HAB1, holistic, open-sourced, home-scale, manipulation, benchmark, four, features, fast | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | result, learning, successful, grasping, multiple, objects, different, geometries, addition, whole | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** We provide brief descriptions of the subtasks below: • Pick[a, optional](xpose): pick object x (from articulation a, if provided). • Place[a, optional](xpose , gpos): place ...
- **p. 6 / 5 METHODOLOGY - extractive PDF cue:** Furthermore, the policy must learn action sequences which can reach these grasp poses and retrieve the target object within the specified horizon while keeping the ...
- **p. 5 / 3 PRELIMINARIES - extractive PDF cue:** Observation Space: We include target object pose, goal position, and TCP pose relative to the base, an indicator of whether the target object is grasped, ...
- **p. 7 / 5 METHODOLOGY - extractive PDF cue:** Visual observations are encoded by a NatureCNN (Mnih et al., 2015) and concatenated with state observations.
- **p. 7 / 5 METHODOLOGY - extractive PDF cue:** Visual observations are encoded by D4PG's 4-layer CNN (Barth-Maron et al., 2018) and concatenated with state observations.
- **p. 8 / 5 METHODOLOGY - extractive PDF cue:** (2016), then concatenated with state observations.
- **p. 4 / 3 PRELIMINARIES - extractive PDF cue:** In this work, we study a partially observable variant of each task, where the policy must use 2 128x128 depth images to infer collisions and ...
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | We evaluate subtask policies (Pick, Place, Open, Close) by success once rate (%), which is the percentage of trajectories that achieve success ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | Furthermore, the policy must learn action sequences which can reach these grasp poses and retrieve the target object within the specified horizon ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | However, these models suffer from artifacts and long-term memory issues which rule out home-scale rearrangement, and low frame rates make training high-frequency ... | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | During training, we evaluate our policies every 10000 steps on 189 episodes. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 5 METHODOLOGY - extractive PDF cue:** 5.1 TRAINING REINFORCEMENT LEARNING POLICIES We choose Reinforcement Learning (RL) to learn our subtask policies as RL does not require prior demonstration data, and it ...
- **p. 17 / A.3 RL SUBTASK EVALUATION CURVES - extractive PDF cue:** During training, we evaluate our policies every 10000 steps on 189 episodes.
- **p. 19 / A.4.3 SAC VS PPO FOR RL TRAINING - extractive PDF cue:** 5.1, and we train SAC with 20 million samples per run.
- **p. 7 / 5 METHODOLOGY - extractive PDF cue:** We train Pick with 50M timesteps and Place with 25M timesteps.
- **p. 8 / 5 METHODOLOGY - extractive PDF cue:** As the dataset generation code is publicly available, users have the flexibility to create their own datasets with custom constraints tailored to their specific requirements.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** then, concatenated, state, observations, First, define, events, occur, timestep, Contact, nonzero, robot/target, pairwise, force, Grasped, object, step, Dropped, Excessive, Collisions.
- **Relevant PDF headings:** 5 METHODOLOGY (p. 6); A.4.5 PER VS ALL-OBJECT POLICY LONG-HORIZON PERFORMANCE (p. 19); A.4.6 DIFFUSION POLICY BASELINES (p. 21).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | This is not an issue with magical grasping (Gu et al., 2023a), indicating that low-level control may need more scene diversity. pick_0 ... | p. 9 (6 RESULTS), p. 18 (A.4.1 DATASET SIZE) |
| Baseline harness | Second, TidyHouse and SetTable RL baselines have some gap between upper bound and real completion rate, indicating potential handoff issues or disturbance ... | p. 8 (6 RESULTS), p. 8 (6 RESULTS) |
| Metric / failure reporting | Even with per-object RL policies, our low-level mobile manipulation subtasks are difficult to train on dense reward, and improving subtask success rate ... | p. 8 (6 RESULTS), p. 10 (6 RESULTS) |

## Failure and Ablation Link

- **p. 18 / A.3 RL SUBTASK EVALUATION CURVES - extractive PDF cue:** We remove all collision requirements, and allow placing on the full target receptacle surface.
- **p. 10 / 6 RESULTS - extractive PDF cue:** To verify this, we run two ablations.
- **p. 10 / 6 RESULTS - extractive PDF cue:** Although MS-HAB does not simulate state transitions like breaking, placing objects without dropping is a desirable, safe robot behavior to avoid excessive damage.
- **p. 22 / A.6.1 DATASET FILTERING AND GENERATION - extractive PDF cue:** For Pick, we require "straightforward success" demonstrations, where the agent successfully picks the object without dropping it while remaining within the cumulative collision threshold.
- **p. 22 / A.6.1 DATASET FILTERING AND GENERATION - extractive PDF cue:** For Open and Close, we require "open success" and "closed success" demonstrations, where the agent opens/closes the articulation without excessive collisions, and the articulation remains ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Trajectory labeling on Pick Cracker Box with all and per-object RL policies. We group the trajectories into four categories: success once (S-Once), excessive ...
- **p. 24 / A.6.2 DEFINITIONS - extractive PDF cue:** Eplace = () ∧eexcessive collisions̸ ∈Eplace viii Didn't reach goal failure: Agent grasps x, but cannot manipulate x to within 15cm of gpos. /Eplace/ > ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 8 (5 METHODOLOGY), p. 8 (5 METHODOLOGY), p. 6 (5 METHODOLOGY), p. 6 (5 METHODOLOGY), p. 7 (5 METHODOLOGY), p. 7 (5 METHODOLOGY), objective p. 6 (5 METHODOLOGY), p. 6 (5 METHODOLOGY), p. 8 (5 METHODOLOGY), p. 7 (5 METHODOLOGY), temporal p. 7 (5 METHODOLOGY), p. 6 (5 METHODOLOGY), p. 7 (5 METHODOLOGY), p. 8 (5 METHODOLOGY), p. 17 (A.3 RL SUBTASK EVALUATION CURVES), p. 3 (2 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
