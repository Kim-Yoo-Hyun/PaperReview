# Method - Bootstrapping Reinforcement Learning with Imitation for Vision-Based Agile Flight

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=bt0PX0e4rE; PDF retrieval source: https://arxiv.org/pdf/2403.12203. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3 Methodology), p. 4 (3 Methodology), p. 7 (3 Methodology), p. 7 (3 Methodology), p. 3 (3 Methodology), p. 8 (3 Methodology)): 2, our approach consists of three phases: (I) initial training of a teacher policy using state information, (II) distillation into a student policy via IL to transfer knowledge and create ...

## Method Body Digest

- **p. 4 / 3 Methodology - extractive PDF cue:** 2, our approach consists of three phases: (I) initial training of a teacher policy using state information, (II) distillation into a student policy via IL ...
- **p. 4 / 3 Methodology - extractive PDF cue:** In the case of BC, the state-based teacher policy is executed for a fixed number of steps, generating a dataset that encompasses corresponding perceptual observations ...
- **p. 7 / 3 Methodology - extractive PDF cue:** For (i) we train the RL policy using RGB images with 10M samples and our approach and baseline (ii) we use 5M data samples for ...
- **p. 7 / 3 Methodology - extractive PDF cue:** Training Effectiveness with different RL configurations To demonstrate the effectiveness of our visuomotor policy learning approach, we ablate the training performance of our approach with ...
- **p. 3 / 3 Methodology - extractive PDF cue:** In stage II, we use IL to learn a student distillation policy using visual inputs.
- **p. 8 / 3 Methodology - extractive PDF cue:** In this work, we introduced a novel approach by fusing the strengths of Reinforcement Learning (RL) and Imitation Learning (IL) for vision-based agile quadrotor flight, ...
- **p. 3 / 3 Methodology - extractive PDF cue:** The drone perceives the environment solely through a single RGB camera, and the learned policy network utilizes egocentric vision input op to output Collective Thrust ...
- **p. 3 / 3 Methodology - extractive PDF cue:** The drone racing task can be formulated as an optimization problem where the objective is to minimize the time required to navigate through a predefined ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** Contributions By leveraging the complementary advantages of IL and RL, we propose a framework that trains a policy capable of navigating through a sequence of ...
- **p. 4 / 3 Methodology - extractive PDF cue:** 2, our approach consists of three phases: (I) initial training of a teacher policy using state information, (II) distillation into a student policy via IL ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Although we validate our method using vision-based drone racing, our approach does not rely on task-specific adaptations that might limit its applicability to other robotic ...

## Source Evidence Cues

- **p. 4 / 3 Methodology - extractive PDF cue:** 2, our approach consists of three phases: (I) initial training of a teacher policy using state information, (II) distillation into a student policy via IL ...
- **p. 4 / 3 Methodology - extractive PDF cue:** In the case of BC, the state-based teacher policy is executed for a fixed number of steps, generating a dataset that encompasses corresponding perceptual observations ...
- **p. 7 / 3 Methodology - extractive PDF cue:** For (i) we train the RL policy using RGB images with 10M samples and our approach and baseline (ii) we use 5M data samples for ...
- **p. 7 / 3 Methodology - extractive PDF cue:** Training Effectiveness with different RL configurations To demonstrate the effectiveness of our visuomotor policy learning approach, we ablate the training performance of our approach with ...
- **p. 3 / 3 Methodology - extractive PDF cue:** In stage II, we use IL to learn a student distillation policy using visual inputs.
- **p. 8 / 3 Methodology - extractive PDF cue:** In this work, we introduced a novel approach by fusing the strengths of Reinforcement Learning (RL) and Imitation Learning (IL) for vision-based agile quadrotor flight, ...
- **p. 3 / 3 Methodology - extractive PDF cue:** The drone perceives the environment solely through a single RGB camera, and the learned policy network utilizes egocentric vision input op to output Collective Thrust ...
- **Detected method headings:** 3 Methodology (p. 3); A.1 Quadrotor Dynamics for Policy Training (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | 2, our approach consists of three phases: (I) initial training of a teacher policy using state information, (II) distillation into a student ... | p. 4 (3 Methodology), p. 4 (3 Methodology) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | In the case of BC, the state-based teacher policy is executed for a fixed number of steps, generating a dataset that encompasses ... | p. 4 (3 Methodology), p. 7 (3 Methodology) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | For (i) we train the RL policy using RGB images with 10M samples and our approach and baseline (ii) we use 5M ... | p. 7 (3 Methodology), p. 7 (3 Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3 Methodology - extractive PDF cue:** The drone racing task can be formulated as an optimization problem where the objective is to minimize the time required to navigate through a predefined ...
- **p. 4 / 3 Methodology - extractive PDF cue:** The reward at time t, denoted as rt, is defined as the sum of various components rt = rprog t + rperc t + ract ...
- **p. 5 / 3 Methodology - extractive PDF cue:** Once the policy achieves high-reward action sequences, the policy update rate also increases.
- **p. 13 / A.3 Training Configurations - extractive PDF cue:** Reward Name Symbol Value Progress reward λ1 0.5 Perception-aware reward λ2 0.025 Command smoothness reward λ3 2e-4 Body rate penalty λ4 5e-4 Gate passing reward ...
- **p. 4 / 3 Methodology - extractive PDF cue:** The RL policy training rewards are adjusted based on [38].
- **p. 7 / 3 Methodology - extractive PDF cue:** It is evident that at 60%, the collected rewards achieve a peak (>100) in the curve representing the best performance.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 3 (3 Methodology), p. 4 (3 Methodology), p. 4 (3 Methodology), p. 8 (3 Methodology), p. 5 (3 Methodology), p. 5 (3 Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | case, state-based, teacher, policy, executed, fixed, number, steps, generating, dataset, encompasses, corresponding, perceptual, observations | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | case, state-based, teacher, policy, executed, fixed, number, steps, generating, dataset | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | Contributions, leveraging, complementary, advantages, framework, trains, policy, capable, navigating, through | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | drone, racing, task, formulated, optimization, problem, where, objective, minimize, time | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3 Methodology - extractive PDF cue:** In the case of BC, the state-based teacher policy is executed for a fixed number of steps, generating a dataset that encompasses corresponding perceptual observations ...
- **p. 3 / 3 Methodology - extractive PDF cue:** The drone perceives the environment solely through a single RGB camera, and the learned policy network utilizes egocentric vision input op to output Collective Thrust ...
- **p. 8 / 3 Methodology - extractive PDF cue:** In that work, the policy observation was an explicit state computed from images and an inertial sensor.
- **p. 4 / 3 Methodology - extractive PDF cue:** Phase I: State-based Teacher Policy Training The teacher policy πteacher processes state observations s = h p, ˜R, v, ω, i, d i , where ...
- **p. 1 / 1 Introduction - extractive PDF cue:** The intrinsic high dimensionality of visual input makes the policy exploration and learning process more inefficient than using low-dimensional input, such as robot states.
- **p. 12 / A.3 Training Configurations - extractive PDF cue:** For state-based teacher training, we employ a policy network consisting of a two-layer MLP, each layer containing 256 neurons, with a final layer outputting a ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The RL policy for state-of-the-art autonomous drone racing [7], which outperformed worldchampion pilots, still relies on explicit state estimates, including position, velocity, and orientation.
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | The vision-based student policy takes a sequence (history length H timesteps) of perceptual observations [ot-H+1, . . . , ot] as input. | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | The reward at time t, denoted as rt, is defined as the sum of various components rt = rprog t + rperc ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | The vision-based student policy takes a sequence (history length H timesteps) of perceptual observations [ot-H+1, . . . , ot] as input. | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | For imitation learning, we employ a batch size of 512, and convergence typically occurs after collecting 5M data samples over approximately 100 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3 Methodology - extractive PDF cue:** 2, our approach consists of three phases: (I) initial training of a teacher policy using state information, (II) distillation into a student policy via IL ...
- **p. 7 / 3 Methodology - extractive PDF cue:** For (i) we train the RL policy using RGB images with 10M samples and our approach and baseline (ii) we use 5M data samples for ...
- **p. 7 / 3 Methodology - extractive PDF cue:** Training Effectiveness with different RL configurations To demonstrate the effectiveness of our visuomotor policy learning approach, we ablate the training performance of our approach with ...
- **p. 3 / 3 Methodology - extractive PDF cue:** The drone perceives the environment solely through a single RGB camera, and the learned policy network utilizes egocentric vision input op to output Collective Thrust ...
- **p. 13 / A.3 Training Configurations - extractive PDF cue:** We incorporate a linear decay in the learning rate, starting at 1e-3 and decreasing to 1e-5 at 50 epochs, remaining unchanged for the remainder of ...
- **p. 12 / A.2 Reward Formulations for RL Trainings - extractive PDF cue:** In our experiments, we employ identical hyperparameters for both state-based teacher training and vision-based RL fine-tuning to ensure a fair comparison.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** consists, three, phases, initial, training, teacher, policy, state, information, distillation, student, transfer, knowledge, create, efficient, baseline, model, III, fine-tuning, through.
- **Relevant PDF headings:** 3 Methodology (p. 3); A.1 Quadrotor Dynamics for Policy Training (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | Realworld Experiments To demonstrate policy improvements, we validated our policy in real-world scenarios using Hardware-in-the-Loop (HIL) simulations, aided by a VICON motion ... | p. 8 (3 Methodology), p. 8 (3 Methodology) |
| Balance-aware whole-body execution | Table 5: Ablation study on history length of the policy observations using raw pixels. We could clearly find out by using more ... | p. 14 (Figure/Table caption), p. 7 (3 Methodology) |
| Recovery / adaptation | The quantitative results, shown in 6, clearly indicate that our approach greatly improves policy performance, achieving lap times within a difference of ... | p. 15 (A.8 Unobservable States Illustration), p. 13 (A.6 Performance w/ Diff. History Length) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Left: Reward comparison between our approach and the other RL configurations. Ours is the only approach that is able to learn to perform ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Table 6: Ablation study on history length of the policy observations using raw pixels. We could clearly find out by using more history observations, that ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Long exposure image of real-world flights shows a blue trajectory for our approach and a red one for the imitation policy. Training on ...
- **p. 6 / 3 Methodology - extractive PDF cue:** This limitation arises because the student policy is trained only on the explicit actions of the expert, without understanding the underlying context that the expert ...
- **p. 7 / 3 Methodology - extractive PDF cue:** This once again underscores the difficulty of RL exploration in high-dimensional time series without bootstrapping.
- **p. 15 / A.8 Unobservable States Illustration - extractive PDF cue:** Approach Slow IL policy Our Finetuned Policy Champion-level Policy LT [s] SR [%] LT [s] SR [%] LT [s] SR [%] Nominal Simulation 9.53 39 ...
- **p. 13 / A.5 Ablation study on Asymmetric Critic Formulation - extractive PDF cue:** In stage III of our approach, the visuomotor policy undergoes fine-tuning using an asymmetric critic setup.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3 Methodology), p. 4 (3 Methodology), p. 7 (3 Methodology), p. 7 (3 Methodology), p. 3 (3 Methodology), p. 8 (3 Methodology), objective p. 3 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 13 (A.3 Training Configurations), p. 4 (3 Methodology), p. 7 (3 Methodology), temporal p. 4 (3 Methodology), p. 4 (3 Methodology), p. 5 (3 Methodology), p. 7 (3 Methodology), p. 7 (3 Methodology), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
