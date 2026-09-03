# Method - ManiSkill: Generalizable Manipulation Skill Benchmark with Large-Scale Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html; PDF retrieval source: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/eda80a3d5b344bc40f3bc04f65b7a357-Abstract-round2.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (Abstract), p. 8 (Abstract), p. 7 (Abstract), p. 3 (Abstract), p. 8 (Abstract), p. 1 (Abstract)): Here, s ∈S is an environment state that consists of robot states (e.g. joint angles of the robot) and object states (e.g. object pose and the joint angles); a ∈A ...

## Method Body Digest

- **p. 5 / Abstract - extractive body cue:** Here, s ∈S is an environment state that consists of robot states (e.g. joint angles of the robot) and object states (e.g. object pose and ...
- **p. 8 / Abstract - extractive body cue:** The global features from the PointNets are then fed into a Transformer [76], after which a final attention pooling layer extracts the final representations and ...
- **p. 7 / Abstract - extractive body cue:** In order to quickly verify the reward template (as our tasks are complicated and solving by RL takes hours), we use Model-Predictive Control (MPC) via ...
- **p. 3 / Abstract - extractive body cue:** ManiSkill has four main features: First, to support generalizable policy learning, ManiSkill provides objects of high topology and geometry variations, as shown in Fig 2.
- **p. 8 / Abstract - extractive body cue:** The first point cloud-based architecture uses one single PointNet [39], a very popular 3D deep learning backbone, to extract a global feature for the entire ...
- **p. 1 / Abstract - extractive body cue:** Here we propose SAPIEN Manipulation Skill Benchmark (ManiSkill) to benchmark manipulation skills over diverse objects in a full-physics simulator.
- **p. 3 / Abstract - extractive body cue:** Here we introduce the key features of the benchmark.
- **p. 3 / Abstract - extractive body cue:** We take significant efforts to select, fix, and re-model the original PartNet-Mobility data [62, 63, 64], as well as design the reward generation rules, so ...

## Design Rationale

- **p. 1 / Abstract - extractive body cue:** Here we propose SAPIEN Manipulation Skill Benchmark (ManiSkill) to benchmark manipulation skills over diverse objects in a full-physics simulator.
- **p. 3 / Abstract - extractive body cue:** Here we introduce the key features of the benchmark.
- **p. 3 / Abstract - extractive body cue:** Additionally, we present and evaluate 3D neural network-based policy learning baselines.

## Source Evidence Cues

- **p. 5 / Abstract - extractive body cue:** Here, s ∈S is an environment state that consists of robot states (e.g. joint angles of the robot) and object states (e.g. object pose and ...
- **p. 8 / Abstract - extractive body cue:** The global features from the PointNets are then fed into a Transformer [76], after which a final attention pooling layer extracts the final representations and ...
- **p. 7 / Abstract - extractive body cue:** In order to quickly verify the reward template (as our tasks are complicated and solving by RL takes hours), we use Model-Predictive Control (MPC) via ...
- **p. 3 / Abstract - extractive body cue:** ManiSkill has four main features: First, to support generalizable policy learning, ManiSkill provides objects of high topology and geometry variations, as shown in Fig 2.
- **p. 8 / Abstract - extractive body cue:** The first point cloud-based architecture uses one single PointNet [39], a very popular 3D deep learning backbone, to extract a global feature for the entire ...
- **p. 1 / Abstract - extractive body cue:** Here we propose SAPIEN Manipulation Skill Benchmark (ManiSkill) to benchmark manipulation skills over diverse objects in a full-physics simulator.
- **p. 3 / Abstract - extractive body cue:** Here we introduce the key features of the benchmark.
- **Detected method headings:** B.7 Controller Design (p. 16); B.7 Controller Design (p. 19)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Here, s ∈S is an environment state that consists of robot states (e.g. joint angles of the robot) and object states (e.g. ... | p. 5 (Abstract), p. 8 (Abstract) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | The global features from the PointNets are then fed into a Transformer [76], after which a final attention pooling layer extracts the ... | p. 8 (Abstract), p. 7 (Abstract) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | In order to quickly verify the reward template (as our tasks are complicated and solving by RL takes hours), we use Model-Predictive ... | p. 7 (Abstract), p. 3 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 7 / Abstract - extractive body cue:** In order to quickly verify the reward template (as our tasks are complicated and solving by RL takes hours), we use Model-Predictive Control (MPC) via ...
- **p. 3 / Abstract - extractive body cue:** We take significant efforts to select, fix, and re-model the original PartNet-Mobility data [62, 63, 64], as well as design the reward generation rules, so ...
- **p. 4 / Abstract - extractive body cue:** This RL plus divide-and-conquer approach is very scalable with respect to the number of object instances within a task, and we leave cross-task RL reward ...
- **p. 4 / Abstract - extractive body cue:** The demonstrations are collected by a scalable RL approach with dense rewards generated by a shared reward template within each task. • We provide several ...
- **p. 5 / Abstract - extractive body cue:** MoveBucket exemplifies motions without constraints.
- **p. 5 / Abstract - extractive body cue:** There are no constraints on the motions of the bucket.
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 4 (Abstract), p. 5 (Abstract), p. 5 (Abstract), p. 8 (Abstract).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | pointcloud, rgbd, modes, object, states, replaced, corresponding, point, cloud, RGB-D, visual, observations, captured, panoramic | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | pointcloud, rgbd, modes, object, states, replaced, corresponding, point, cloud, RGB-D | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | Here, SAPIEN, Manipulation, Skill, Benchmark, ManiSkill, skills, over, diverse, objects | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | order, quickly, verify, reward, template, tasks, complicated, solving, takes, hours | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / Abstract - extractive body cue:** In pointcloud and rgbd modes, the object states in s are replaced by the corresponding point cloud / RGB-D visual observations captured from a panoramic ...
- **p. 4 / Abstract - extractive body cue:** 2 ManiSkill Benchmark The goal of building ManiSkill benchmark can be best described as facilitating learning generalizable manipulation skills from 3D visual inputs with demonstrations. ...
- **p. 5 / Abstract - extractive body cue:** Here, s ∈S is an environment state that consists of robot states (e.g. joint angles of the robot) and object states (e.g. object pose and ...
- **p. 1 / Abstract - extractive body cue:** Object manipulation from 3D visual inputs poses many challenges on building generalizable perception and policy models.
- **p. 6 / Abstract - extractive body cue:** 2.3 Robots, Actions, Visual Observations, and Rewards All the tasks in ManiSkill use similar robots, which are composed of three parts: moving platform, Sciurus [65] ...
- **p. 3 / Abstract - extractive body cue:** For example, imitation learning [53, 54, 4] and offline RL [55, 56, 57] can learn a policy purely from demonstrations datasets [58, 59], but online ...
- **p. 6 / Abstract - extractive body cue:** As mentioned in Sec 2.1, ManiSkill supports three observation modes: state, pointcloud, and rgbd, where the latter two modes are suitable for studying object-level generalizability.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | Besides supporting the learning of policies from interactions, we also support learning-from-demonstrations (LfD) methods, by providing a large number of high-quality demonstrations ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | (For better view, we show point clouds obtained from cameras mounted in the world frame. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Third, to facilitate learning-from-demonstration methods, we have collected a large number of successful trajectories (~36,000 trajectories, ~1.5M 3D point cloud / RGB-D ... | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / Abstract - extractive body cue:** We train each model for 150k gradient steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Here, environment, state, consists, robot, states, joint, angles, object, pose, action, applied, target, velocity, controller, physical, dynamics, binary, variable, indicates.
- **Relevant PDF headings:** B.7 Controller Design (p. 16); B.7 Controller Design (p. 19).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | We plan to process more objects from the PartNet-Mobility dataset [62] and add them to our ManiSkill assets; 2) While the four ... | p. 9 (Abstract), p. 9 (Abstract) |
| Baseline harness | Therefore, we designed several baselines and open-sourced their implementations here to encourage future explorations in the field. | p. 8 (Abstract), p. 8 (Abstract) |
| Metric / failure reporting | We adopted pointcloud observation mode and designed point cloud-based vision architectures as our feature extractor since previous work [46] has achieved significant ... | p. 8 (Abstract), p. 9 (Abstract) |

## Failure and Ablation Link

- **p. 8 / Abstract - extractive body cue:** While network architectures and algorithms play an important role in the performance, learning manipulation skills from demonstrations is challenging without a large number of trajectories, ...
- **p. 8 / Abstract - extractive body cue:** Intuitively, this allows the extracted feature to not only contain geometric information of objects, but also contain the relation between the robot and each individual ...
- **p. 9 / Abstract - extractive body cue:** It is worth noting that our experiment results should not discourage benchmark users to include failure trajectories and find better usage of offline RL methods, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4: RGB-D (RGB/Depth) and point cloud observations in ManiSkill. Left two images: RGB-D image from one of the three cameras mounted on the robot. ...
- **p. 8 / Abstract - extractive body cue:** We fix issues if we cannot learn a policy to achieve the task.
- **p. 8 / Abstract - extractive body cue:** For example, certain cabinet drawers may be stuck due to inaccurate overlapping between collision shapes.
- **p. 9 / Abstract - extractive body cue:** 4 Conclusion and Limitations In this work, we propose ManiSkill, an articulated benchmark for generalizable physical object manipulation from 3D visual inputs with diverse object ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (Abstract), p. 8 (Abstract), p. 7 (Abstract), p. 3 (Abstract), p. 8 (Abstract), p. 1 (Abstract), objective p. 7 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract), p. 5 (Abstract), p. 5 (Abstract), temporal p. 1 (Abstract), p. 3 (Abstract), p. 3 (Abstract), p. 4 (Abstract), p. 4 (Abstract), p. 5 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
