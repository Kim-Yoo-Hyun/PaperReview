# Method - DexterityGen: Foundation Controller for Unprecedented Dexterity

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (14 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://roboticsconference.org/2026/program/papers/103/; PDF retrieval source: https://roboticsconference.org/2026/program/papers/103/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (C. DexGen Model Architecture), p. 5 (C. DexGen Model Architecture), p. 6 (C. DexGen Model Architecture), p. 5 (C. DexGen Model Architecture), p. 4 (III. THE DEXGEN CONTROLLER), p. 4 (III. THE DEXGEN CONTROLLER)): The inverse dynamics model is a simple residual multilayer perceptron that outputs a normal distribution to model the actions conditioned on the current robot state and motion ‘command.

## Method Body Digest

- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The inverse dynamics model is a simple residual multilayer perceptron that outputs a normal distribution to model the actions conditioned on the current robot state ...
- **p. 5 / C. DexGen Model Architecture - extractive body cue:** The first module is a diffusion model that characterizes the distribution of robot finger keypoint motions given current observations.
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The generated finger keypoint ‘movement is then converted to action by the inverse dynamics model.
- **p. 5 / C. DexGen Model Architecture - extractive body cue:** Here we use 3D keypoint motions Ar € R™***% in the robot hand frame as an intermediate action representation, This representation is particularly advantageous for ...
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We propose to pretrain a generative behavior model po(o/0) ‘on the simulation dataset to model prior action distribution so that it can generate stable and ...
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We detail the dataset used for training the model in section II-B, the model architecture in section III-C, and the inference procedure in section IID.
- **p. 12 / B. Implementation of Anygrasp-to-Anygrasp - extractive body cue:** Grasp Generation To define this task, we first need to generate the grasp set for each object with the Grasp Generation Algorithm 2. ‘The algorithm ...
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** During inference, we can sample actions from this distribution and further aligned with extemal motion ‘commands using gradient guidance.

## Design Rationale

- **p. 2 / 1. INTRODUCTION - extractive body cue:** "Motivated by these observations, in this paper, we propose
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We propose to pretrain a generative behavior model po(o/0) ‘on the simulation dataset to model prior action distribution so that it can generate stable and ...
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The above function encourages the generated future fingertip position to closely match the commanded fingertip position Since the action of the robot hand has a ...

## Source Evidence Cues

- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The inverse dynamics model is a simple residual multilayer perceptron that outputs a normal distribution to model the actions conditioned on the current robot state ...
- **p. 5 / C. DexGen Model Architecture - extractive body cue:** The first module is a diffusion model that characterizes the distribution of robot finger keypoint motions given current observations.
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The generated finger keypoint ‘movement is then converted to action by the inverse dynamics model.
- **p. 5 / C. DexGen Model Architecture - extractive body cue:** Here we use 3D keypoint motions Ar € R™***% in the robot hand frame as an intermediate action representation, This representation is particularly advantageous for ...
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We propose to pretrain a generative behavior model po(o/0) ‘on the simulation dataset to model prior action distribution so that it can generate stable and ...
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We detail the dataset used for training the model in section II-B, the model architecture in section III-C, and the inference procedure in section IID.
- **p. 12 / B. Implementation of Anygrasp-to-Anygrasp - extractive body cue:** Grasp Generation To define this task, we first need to generate the grasp set for each object with the Grasp Generation Algorithm 2. ‘The algorithm ...
- **Detected method headings:** III. THE DEXGEN CONTROLLER (p. 4); C. DexGen Model Architecture (p. 5)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / affordance state | object와 contact-relevant scene을 표현한다 | RGB-D, point cloud, object/task observation | pose, affordance, grasp/contact graph 또는 SE(3) descriptor를 구성 | object/contact state | The inverse dynamics model is a simple residual multilayer perceptron that outputs a normal distribution to model the actions conditioned on the ... | p. 6 (C. DexGen Model Architecture), p. 5 (C. DexGen Model Architecture) |
| Grasp / trajectory generation | goal을 feasible manipulation candidate로 바꾼다 | geometry/contact state와 task goal | grasp sampling, pose planning, trajectory optimization 또는 policy decoding을 적용 | grasp, pose, force 또는 trajectory | The first module is a diffusion model that characterizes the distribution of robot finger keypoint motions given current observations. | p. 5 (C. DexGen Model Architecture), p. 6 (C. DexGen Model Architecture) |
| Contact execution / correction | interaction outcome으로 action을 닫힌 loop로 수정한다 | candidate와 visual/force/tactile feedback | tracking, regrasp, correction, termination 또는 recovery를 수행 | next action/task state | The generated finger keypoint ‘movement is then converted to action by the inverse dynamics model. | p. 6 (C. DexGen Model Architecture), p. 5 (C. DexGen Model Architecture) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** During inference, we can sample actions from this distribution and further aligned with extemal motion ‘commands using gradient guidance.
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** We train both the diffusion model and inverse dynamics model with our generated simulation dataset using the standard diffusion model loss function and the MSE ...
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The above function encourages the generated future fingertip position to closely match the commanded fingertip position Since the action of the robot hand has a ...
- **p. 5 / C. DexGen Model Architecture - extractive body cue:** Here we use 3D keypoint motions Ar € R™***% in the robot hand frame as an intermediate action representation, This representation is particularly advantageous for ...
- **Formal bridge:** object geometry/contact state -> grasp/pose/force/trajectory -> task/contact/pose objective -> completion, contact success and robustness.
- **Equation/algorithm anchors:** p. 4 (III. THE DEXGEN CONTROLLER), p. 6 (C. DexGen Model Architecture), p. 6 (C. DexGen Model Architecture).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | inverse, dynamics, model, simple, residual, multilayer, perceptron, outputs, normal, distribution, actions, conditioned, current, robot | RGB-D/point cloud, object state와 contact/task observation | body cue; exact tensor/frame verify |
| State/latent | inverse, dynamics, model, simple, residual, multilayer, perceptron, outputs, normal, distribution | object geometry, affordance, contact mode 또는 end-effector state | body cue; notation verify |
| Action/output | Motivated, observations, pretrain, generative, behavior, model, simulation, dataset, prior, action | grasp, pose, force 또는 end-effector trajectory | body cue; unit/decoder verify |
| Objective/constraint | During, inference, sample, actions, distribution, further, aligned, extemal, motion, commands | task/contact/pose objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The inverse dynamics model is a simple residual multilayer perceptron that outputs a normal distribution to model the actions conditioned on the current robot state ...
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The above function encourages the generated future fingertip position to closely match the commanded fingertip position Since the action of the robot hand has a ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** However, the external inputs in these studies are limited to a few discretized commands, lacking control over low-level interactions, such as finger movements and object ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** In simulation, we demonstrate that DexGen significantly enhances the robustness and per= formance of a highly perturbed noisy policy, extending its stable operation duration by ...
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We propose to pretrain a generative behavior model po(o/0) ‘on the simulation dataset to model prior action distribution so that it can generate stable and ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Additionally, existing discrete haptic feedback (e-. binary vibration) alone is often inadequate for conveying complex touch interactions and contact geometries.
- **p. 5 / A. Preliminaries - extractive body cue:** We can also specify Keypoints and actions for other robots to implement our proposed algorithm.
- **Normalized interface:** observation=RGB-D/point cloud, object state와 contact/task observation; state=object geometry, affordance, contact mode 또는 end-effector state; output/action=grasp, pose, force 또는 end-effector trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | grasp/pose proposal에서 contact episode까지의 task horizon; trajectory chunk 여부 확인 필요. | + Funetional Grasping Regrasping is a necessary step in tool manipulation. | episode/sequence/action-chunk boundary |
| Rate / latency | perception/planning rate와 low-level contact control rate가 분리된다. | The user is asked to perform a power grasp on the tool handle placed either horizontally (nor- ‘mal) or vertically in the ... | Hz/fps, inference time and control rate |
| Memory | object/contact state, current pose와 tactile/force history; exact window 확인 필요. | not recovered | window and reset |
| Compute | point/pose encoding, candidate sampling/optimization과 collision/contact checking이 결정한다. | Generating this dataset (by rolling out trained RL. policies) requires 300 GPU hours. | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We propose to pretrain a generative behavior model po(o/0) ‘on the simulation dataset to model prior action distribution so that it can generate stable and ...
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We detail the dataset used for training the model in section II-B, the model architecture in section III-C, and the inference procedure in section IID.
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** Generating this dataset (by rolling out trained RL. policies) requires 300 GPU hours.
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** We train these models with the AdamW optimizer (35, 29] for 15 epochs using 96 GPUs, which takes approximately 3 days.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** inverse, dynamics, model, simple, residual, multilayer, perceptron, outputs, normal, distribution, actions, conditioned, current, robot, state, motion, command, first, module, diffusion.
- **Relevant PDF headings:** III. THE DEXGEN CONTROLLER (p. 4); C. DexGen Model Architecture (p. 5).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / affordance state | ‘We have demonstrated that our system can provide effective assistance through simulated validation. ‘Then, we further design several tasks for benchmarking in ... | p. 7 (B. Simulated Experiments), p. 5 (B. Large-Scale Behavior Dataset Generation) |
| Grasp / trajectory generation | Compared to the baseline, our system can successfully help the user to solve many tasks in various challenging setups. | p. 8 (B. Simulated Experiments), p. 7 (IV. EXPERIMENTS) |
| Contact execution / correction | 4) Evaluation Protocol: We evaluate the performance of 1 teleoperation system by measuring the success rate a human user can achieve when ... | p. 8 (B. Simulated Experiments), p. 8 (B. Simulated Experiments) |

## Failure and Ablation Link

- **p. 7 / B. Simulated Experiments - extractive body cue:** We find that without our assistance, the noisy ‘expert has much more frequent failures.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Dataset: The Anygrasp-to-Anygrasp dataset generation pipeline is designed for the generative pretraining of DexGen. For a wide variety of objects, we extensively search ...
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** 5: Our large-scale, multi-task pretraining dataset covers diverse grasp to grasp transitions (arrows).
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** To achieve this, we require a large~ scale behavior dataset to pretrain our DexGen model, ensuring ‘comprehensive coverage of the state space.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: Part of our real world testing objects, which are rot present in our pretraining dataset. We include objects of different sizes, masses, and ...
- **p. 7 / B. Simulated Experiments - extractive body cue:** We find that without our assistance, the noisy ‘expert has much more frequent failures.
- **p. 7 / B. Simulated Experiments - extractive body cue:** We record the average number of critical failures (drop the object) and the number of goal achievements within a certain time of different policies

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (C. DexGen Model Architecture), p. 5 (C. DexGen Model Architecture), p. 6 (C. DexGen Model Architecture), p. 5 (C. DexGen Model Architecture), p. 4 (III. THE DEXGEN CONTROLLER), p. 4 (III. THE DEXGEN CONTROLLER), objective p. 4 (III. THE DEXGEN CONTROLLER), p. 6 (C. DexGen Model Architecture), p. 6 (C. DexGen Model Architecture), p. 5 (C. DexGen Model Architecture), temporal p. 7 (B. Simulated Experiments), p. 7 (B. Simulated Experiments), p. 8 (B. Simulated Experiments), p. 8 (B. Simulated Experiments), p. 4 (A. Preliminaries), p. 5 (A. Preliminaries).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
