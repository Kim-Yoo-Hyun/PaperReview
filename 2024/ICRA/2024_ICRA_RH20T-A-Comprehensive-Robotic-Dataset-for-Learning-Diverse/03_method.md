# Method - RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2307.00595; PDF retrieval source: https://arxiv.org/pdf/2307.00595. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (III. RH20T DATASET), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (Dataset), p. 4 (200 Hz), p. 4 (200 Hz)): To ensure applicability across different robot configurations, we used 4 popular robot arms, 4 different robotic grippers, and 3 types of force-torque sensors, resulting in 7 robot configurations.

## Method Body Digest

- **p. 3 / III. RH20T DATASET - extractive PDF cue:** To ensure applicability across different robot configurations, we used 4 popular robot arms, 4 different robotic grippers, and 3 types of force-torque sensors, resulting in ...
- **p. 1 / Abstract - extractive PDF cue:** Each sequence in the dataset includes visual, force, audio, and action information.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, these control methods are inefficient and pose safety risks when the robot engages in rich-contact interactions with the environment.
- **p. 3 / Dataset - extractive PDF cue:** #Traj. #Skills #Robots Human Demo Contact Rich Depth Sensing Camera Calib.
- **p. 4 / 200 Hz - extractive PDF cue:** Different force-torque sensors are tared carefully.
- **p. 4 / 200 Hz - extractive PDF cue:** The coordinate frame of all robots and force-torque sensors are aligned.
- **p. 5 / 200 Hz - extractive PDF cue:** RGBD cameras : robot arm force sensor microphone gripper - haptic device pedal 2 Fig.
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** Properties of RH20T RH20T is designed with the objective of enabling general robotic manipulation, which means that the robot can perform various skills based on ...

## Design Rationale

- **p. 3 / III. RH20T DATASET - extractive PDF cue:** We introduce our robotic manipulation dataset, RobotHuman demonstration in 20TB (RH20T), to the community.
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** [TM1 c) Scale: Our dataset consists of over 110,000 robot sequences and an equal number of human sequences, with more than 50 million images collected ...

## Source Evidence Cues

- **p. 3 / III. RH20T DATASET - extractive PDF cue:** To ensure applicability across different robot configurations, we used 4 popular robot arms, 4 different robotic grippers, and 3 types of force-torque sensors, resulting in ...
- **p. 1 / Abstract - extractive PDF cue:** Each sequence in the dataset includes visual, force, audio, and action information.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, these control methods are inefficient and pose safety risks when the robot engages in rich-contact interactions with the environment.
- **p. 3 / Dataset - extractive PDF cue:** #Traj. #Skills #Robots Human Demo Contact Rich Depth Sensing Camera Calib.
- **p. 4 / 200 Hz - extractive PDF cue:** Different force-torque sensors are tared carefully.
- **p. 4 / 200 Hz - extractive PDF cue:** The coordinate frame of all robots and force-torque sensors are aligned.
- **p. 5 / 200 Hz - extractive PDF cue:** RGBD cameras : robot arm force sensor microphone gripper - haptic device pedal 2 Fig.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | To ensure applicability across different robot configurations, we used 4 popular robot arms, 4 different robotic grippers, and 3 types of force-torque ... | p. 3 (III. RH20T DATASET), p. 1 (Abstract) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | Each sequence in the dataset includes visual, force, audio, and action information. | p. 1 (Abstract), p. 1 (I. INTRODUCTION) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | However, these control methods are inefficient and pose safety risks when the robot engages in rich-contact interactions with the environment. | p. 1 (I. INTRODUCTION), p. 3 (Dataset) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. RH20T DATASET - extractive PDF cue:** Properties of RH20T RH20T is designed with the objective of enabling general robotic manipulation, which means that the robot can perform various skills based on ...
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** The following properties are emphasized to fulfill this objective, and Tab.
- **p. 1 / Abstract - extractive PDF cue:** Recent progress in one-shot imitation learning and robotic foundation models have shown promise in transferring trained policies to new tasks based on demonstrations.
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** p. 3 (III. RH20T DATASET), p. 3 (III. RH20T DATASET).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Proprioception, encompasses, joint, angles/torques, end-effector, Cartesian, pose, gripper, states, sequence, dataset, includes, visual, force | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | Proprioception, encompasses, joint, angles/torques, end-effector, Cartesian, pose, gripper, states, sequence | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | introduce, robotic, manipulation, dataset, RobotHuman, demonstration, RH20T, community, TM1, Scale | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | Properties, RH20T, designed, objective, enabling, general, robotic, manipulation, means, robot | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. RH20T DATASET - extractive PDF cue:** Proprioception encompasses joint angles/torques, end-effector Cartesian pose and gripper states.
- **p. 1 / Abstract - extractive PDF cue:** Each sequence in the dataset includes visual, force, audio, and action information.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Additionally, tele-operation without force feedback degrades manipulation efficiency for humans.
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** To ensure applicability across different robot configurations, we used 4 popular robot arms, 4 different robotic grippers, and 3 types of force-torque sensors, resulting in ...
- **p. 4 / 200 Hz - extractive PDF cue:** Different force-torque sensors are tared carefully.
- **p. 4 / 200 Hz - extractive PDF cue:** The coordinate frame of all robots and force-torque sensors are aligned.
- **p. 5 / 200 Hz - extractive PDF cue:** RGBD cameras : robot arm force sensor microphone gripper - haptic device pedal 2 Fig.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | It is evident that all the cameras are calibrated with respect to the robot's base frame, and all the recorded data are ... | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | The chunk size is set to 20, which corresponds to 2 seconds with the frequency of 10Hz. | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | The chunk size is set to 20, which corresponds to 2 seconds with the frequency of 10Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** During pre-training phase, the model is trained with a learning rate of 2 x 10-5 for 10 epochs; while during fine-tuning phase, the model is ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Epochs Reach Pick Place 500 35 10 0 v 500 70 15 15 v 500 65 20 15 75 730 55 5 0 v 750 ...
- **p. 4 / 200 Hz - extractive PDF cue:** We make our tele-operation pretty intuitive and the average training time is less than 1 hour.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** ensure, applicability, across, different, robot, configurations, popular, arms, robotic, grippers, types, force-torque, sensors, resulting, sequence, dataset, includes, visual, force, audio.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | It is evident that all the cameras are calibrated with respect to the robot's base frame, and all the recorded data are ... | p. 5 (IV. EXPERIMENTS), p. 3 (III. RH20T DATASET) |
| Coverage / augmentation | With 40 robot demonstrations, the results of pretraining on our dataset outperform the counterpart trained with 75 demonstrations without pretraining. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Downstream learning interface | Additionally, the inclusion of data from different tasks during pretraining further improves the overall success rate. | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** With 40 robot demonstrations, the results of pretraining on our dataset outperform the counterpart trained with 75 demonstrations without pretraining.
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Comparing the results of training for 500 epochs with pretraining to training for 750 epochs without pretraining, we find that pretraining on our dataset also ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We evaluate the performance of the ACT model both with and without pre-training on our dataset.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Following pre-training, we fine-tune the ACT model on specific portions of the newly collected data, focusing on the task involving grasping and weight placement.
- **p. 3 / III. RH20T DATASET - extractive PDF cue:** To enhance environment diversity, we frequently replaced over 50 table covers with different textures and materials, and introduced irrelevant objects to create distractions.
- **p. 6 / V. DISCUSSION AND CONCLUSION - extractive PDF cue:** The current limitations of this paper are that (i) the cost of data collection is expensive and (ii) the potential of robotic foundation models is ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** These results demonstrate that leveraging the diverse training data from our dataset enhances the adaptability and robustness of the robotic manipulation model.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (III. RH20T DATASET), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 3 (Dataset), p. 4 (200 Hz), p. 4 (200 Hz), objective p. 3 (III. RH20T DATASET), p. 3 (III. RH20T DATASET), p. 1 (Abstract), temporal p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 1 (I. INTRODUCTION), p. 2 (II. RELATED WORKS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
