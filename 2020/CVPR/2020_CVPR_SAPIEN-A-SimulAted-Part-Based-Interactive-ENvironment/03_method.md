# Method - SAPIEN: A SimulAted Part-Based Interactive ENvironment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 8 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction)): Then we use velocity controller to pull it to the joint limit.

## Method Body Digest

- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** Then we use velocity controller to pull it to the joint limit.
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** In this way, we factor out the perception module and allow algorithms to focus on robotic control and interaction tasks; 2) using the raw image/point-cloud ...
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** We adopt Soft ActorCritic(SAC) [15], which is one of the SOTA reinforcement learning algorithms, trained on 2, 4, 8, 16 doors or drawers, and test ...
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** With the large-scale PartNet-Mobility dataset, SAPIEN also supports various robotic interaction tasks, including solving low-level control tasks, such as button pushing, handle grasping, and drawer ...
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** During training, agents receive positive rewards when the target part approaches the joint limit with the opening door/drawer, while obtaining negative rewards when the gripper ...
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** We provide three different state representations: 1) raw state of the whole scene (raw-exp), consisting of current positions and velocities of all the parts; 2) ...
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** The input of the agent consists of point clouds, normal maps and segmentation masks captured by three fixed cameras mounted on the left, right and ...
- **p. 1 / 1. Introduction - extractive body cue:** Researchers, therefore, Figure 1: Robot-object Interaction in SAPIEN.

## Design Rationale

- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** The input of the agent consists of point clouds, normal maps and segmentation masks captured by three fixed cameras mounted on the left, right and ...
- **p. 1 / 1. Introduction - extractive body cue:** We show the ray-traced scene (top) and robot camera views (bottom): RGB image, surface normals, depth and semantic segmentation of motion parts, while a robot ...
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** Also, this mode enables end-toend learning for perception and interactions (e.g., learning perception with a specific interaction target).

## Source Evidence Cues

- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** Then we use velocity controller to pull it to the joint limit.
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** In this way, we factor out the perception module and allow algorithms to focus on robotic control and interaction tasks; 2) using the raw image/point-cloud ...
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** We adopt Soft ActorCritic(SAC) [15], which is one of the SOTA reinforcement learning algorithms, trained on 2, 4, 8, 16 doors or drawers, and test ...
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** With the large-scale PartNet-Mobility dataset, SAPIEN also supports various robotic interaction tasks, including solving low-level control tasks, such as button pushing, handle grasping, and drawer ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | Then we use velocity controller to pull it to the joint limit. | p. 8 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | In this way, we factor out the perception module and allow algorithms to focus on robotic control and interaction tasks; 2) using ... | p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | We adopt Soft ActorCritic(SAC) [15], which is one of the SOTA reinforcement learning algorithms, trained on 2, 4, 8, 16 doors or ... | p. 8 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** During training, agents receive positive rewards when the target part approaches the joint limit with the opening door/drawer, while obtaining negative rewards when the gripper ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | factor, perception, module, allow, algorithms, focus, robotic, control, interaction, tasks, image/point-cloud, inputs, needs, develop | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | factor, perception, module, allow, algorithms, focus, robotic, control, interaction, tasks | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | input, agent, consists, point, clouds, normal, maps, segmentation, masks, captured | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | During, training, agents, receive, positive, rewards, when, target, part, approaches | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** In this way, we factor out the perception module and allow algorithms to focus on robotic control and interaction tasks; 2) using the raw image/point-cloud ...
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** We provide three different state representations: 1) raw state of the whole scene (raw-exp), consisting of current positions and velocities of all the parts; 2) ...
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** The input of the agent consists of point clouds, normal maps and segmentation masks captured by three fixed cameras mounted on the left, right and ...
- **p. 1 / 1. Introduction - extractive body cue:** Researchers, therefore, Figure 1: Robot-object Interaction in SAPIEN.
- **p. 1 / 1. Introduction - extractive body cue:** To achieve human-level perception and interaction with the 3D world, home-assistant robots must have the capability to use perception to interact with 3D objects [11, ...
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** Also, this mode enables end-toend learning for perception and interactions (e.g., learning perception with a specific interaction target).
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | This is because drawers are relatively easier to pull out, as the movement for the gripper almost follows the same pattern every ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | For drawer-opening, the visual features remain almost the same every time step from the front view, so it provides little information about ... | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | Tests were performed on a laptop with Ubuntu 18.04, on 2.2 GHz Intel i7-8750 CPU and an Nvidia GeForce RTX 2070 GPU. | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** We adopt Soft ActorCritic(SAC) [15], which is one of the SOTA reinforcement learning algorithms, trained on 2, 4, 8, 16 doors or drawers, and test ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Then, velocity, controller, pull, joint, limit, factor, perception, module, allow, algorithms, focus, robotic, control, interaction, tasks, image/point-cloud, inputs, needs, develop.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | SAPIEN simulator, equipped with the PartNet-Mobility dataset, provides a platform for several robotic perception tasks. | p. 5 (4.1. Robotic Perception), p. 7 (4.2. Robotic Interaction) |
| Baseline harness | We evaluate two baseline algorithms, ResNet-50 [17] and PointNet++ [39], that deals with the input RGB-D partial scans using either 2D or ... | p. 6 (4.1. Robotic Perception), p. 6 (4.1. Robotic Perception) |
| Metric / failure reporting | This method (PBVS) achieves an 81.8% success rate for door opening. | p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction) |

## Failure and Ablation Link

- **p. 6 / 4.1. Robotic Perception - extractive body cue:** Simple ambient and directional lighting without shadows are provided for RGB rendering.
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** With the large-scale PartNet-Mobility dataset, SAPIEN also supports various robotic interaction tasks, including solving low-level control tasks, such as button pushing, handle grasping, and drawer ...
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** If the agent cannot move the joint to the given threshold or move 11103
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** in the opposite direction, then it fails.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** During training, agents receive positive rewards when the target part approaches the joint limit with the opening door/drawer, while obtaining negative rewards when the gripper ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 8 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction), objective p. 8 (4.2. Robotic Interaction), temporal p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 1 (Abstract), p. 2 (3) The environment needs), p. 2 (3) The environment needs), p. 3 (2. Related Work).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
