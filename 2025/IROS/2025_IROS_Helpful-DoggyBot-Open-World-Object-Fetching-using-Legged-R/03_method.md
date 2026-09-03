# Method - Helpful DoggyBot: Open-World Object Fetching using Legged Robots and Vision-Language Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2410.00231; PDF retrieval source: https://arxiv.org/pdf/2410.00231. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER)): Phase 1: Training with Privileged Information We develop our agile visual whole-body control policy through a two-phase training process: In the first phase, we train a policy using PPO [79] ...

## Method Body Digest

- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Phase 1: Training with Privileged Information We develop our agile visual whole-body control policy through a two-phase training process: In the first phase, we train ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Our online estimator architecture consists of a convolutional neural network (CNN) followed by a gated recurrent unit (GRU) to process the temporal sequence of depth ...
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We use a two-phase framework to train a depth-based policy as the low-evel whole-body controller.
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** During deployment, we use VLMs for open-vocabulary detection, segmentation and tracking models to provide velocity commands and pitch commands for the controller. locomotion and precise ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We introduce auxiliary rewards for maintaining balance, minimizing energy consumption, and smooth transitions between different locomotion modes (e.g., walking, climbing, and tilting).
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** These include increased exploration burden and the potential for sub-optimal behaviors when optimizing for multiple objectives simultaneously [43].
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** The output of this estimator replaces the scandots input to the base policy learned in Phase 1.
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** VLM Velocity Commands VLM Pitch Commands Proprioception Exteroception Student Actions Deployment Training Depth Oracle Velocity Commands Phase 2 Depth Images Fig.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contributions of our system include (1) a simple yet effective 1-DoF gripper design that enables object grasping for quadrupeds, (2) a general-purpose low-level ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Helpful DoggyBot, a quadrupedal robot system that aims to overcome these limitations and enable helpful mobile manipulation skills that can ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Our online estimator architecture consists of a convolutional neural network (CNN) followed by a gated recurrent unit (GRU) to process the temporal sequence of depth ...

## Source Evidence Cues

- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Phase 1: Training with Privileged Information We develop our agile visual whole-body control policy through a two-phase training process: In the first phase, we train ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Our online estimator architecture consists of a convolutional neural network (CNN) followed by a gated recurrent unit (GRU) to process the temporal sequence of depth ...
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We use a two-phase framework to train a depth-based policy as the low-evel whole-body controller.
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** During deployment, we use VLMs for open-vocabulary detection, segmentation and tracking models to provide velocity commands and pitch commands for the controller. locomotion and precise ...
- **Detected method headings:** IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Phase 1: Training with Privileged Information We develop our agile visual whole-body control policy through a two-phase training process: In the first ... | p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Our online estimator architecture consists of a convolutional neural network (CNN) followed by a gated recurrent unit (GRU) to process the temporal ... | p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | We use a two-phase framework to train a depth-based policy as the low-evel whole-body controller. | p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We introduce auxiliary rewards for maintaining balance, minimizing energy consumption, and smooth transitions between different locomotion modes (e.g., walking, climbing, and tilting).
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** These include increased exploration burden and the potential for sub-optimal behaviors when optimizing for multiple objectives simultaneously [43].
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | output, estimator, replaces, scandots, input, base, policy, learned, Phase, VLM, Velocity, Commands, Pitch, Proprioception | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | output, estimator, replaces, scandots, input, base, policy, learned, Phase, VLM | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | contributions, system, include, simple, effective, DoF, gripper, design, enables, object | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | introduce, auxiliary, rewards, maintaining, balance, minimizing, energy, consumption, smooth, transitions | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** The output of this estimator replaces the scandots input to the base policy learned in Phase 1.
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** VLM Velocity Commands VLM Pitch Commands Proprioception Exteroception Student Actions Deployment Training Depth Oracle Velocity Commands Phase 2 Depth Images Fig.
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We convert ˆdwp into angular velocity command ωcmd as a policy input, which calculates the angular difference between robot's current direction and ˆdwp, removing dependency ...
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Phase 1 Teacher Actions Phase 1 Scandots Actor Student Actions Supervise Phase 2 MLP GRU Actor Pitch Commands Proprioception Florence 2 Open Vocabulary Detection Robot ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, their potential for assisting humans in everyday indoor environments remains largely untapped, like the ability to understand and follow language instructions to fetch a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The key contributions of our system include (1) a simple yet effective 1-DoF gripper design that enables object grasping for quadrupeds, (2) a general-purpose low-level ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To increase the traversability and reachability of quadrupeds compared to prior work [4], [5], we use reinforcement learning and simulation to train a general-purpose low-level ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Instead of using a GRU, it uses only the depth image and proprioception at the current time step without any memory to ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | These baselines allow us to assess the impact of various components in our approach, including the importance of visual input, temporal memory, ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | Instead of using a GRU, it uses only the depth image and proprioception at the current time step without any memory to ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Tracking: To maintain real-time performance, we employ SAM2 for object tracking at 10 Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Phase 1: Training with Privileged Information We develop our agile visual whole-body control policy through a two-phase training process: In the first phase, we train ...
- **p. 3 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** Our online estimator architecture consists of a convolutional neural network (CNN) followed by a gated recurrent unit (GRU) to process the temporal sequence of depth ...
- **p. 4 / IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER - extractive body cue:** We use a two-phase framework to train a depth-based policy as the low-evel whole-body controller.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Phase, Training, Privileged, Information, develop, agile, visual, whole-body, control, policy, through, two-phase, process, first, train, PPO, optimize, locomotion, objectives, online.
- **Relevant PDF headings:** IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Illustrated in Figure 1, we select three objects and three environments that represent realistic real-world scenarios: • Bed + Toy: The robot ... | p. 6 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS) |
| Whole-body policy / controller | In contrast, our approach achieves consistently higher performance, with nearperfect scores in most tasks, especially Climb Up and Climb Down, and outperforms ... | p. 5 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |
| Adaptation / recovery | In the task involving navigating to a toy on a bed, our system achieved a 60% total first-attempt success rate, significantly outperforming ... | p. 6 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / VI. EXPERIMENTS - extractive body cue:** Instead of using a GRU, it uses only the depth image and proprioception at the current time step without any memory to predict actions. • ...
- **p. 5 / VI. EXPERIMENTS - extractive body cue:** Without waypoints as guidance, the robot easily learns to walk pass the obstacle or turn around instead of trying to climb as a result of ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** We compare our system with three baselines including Go2 default controller instead of our learned controller, teleoperation using a remote controller instead of using VLMs, ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** In future work, we will focus on enhancing manipulation capabilities without compromising agility, developing navigation strategies using only onboard sensors, and future improving agility to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: System Overview. We use a two-phase framework to train a depth-based policy as the low-evel whole-body controller. During deployment, we use VLMs for ...
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** While our approach demonstrates progress, limitations include the gripper's restricted dexterity, reliance on ceiling-mounted cameras for navigation, and potential occlusion to the perception system.
- **p. 6 / VI. EXPERIMENTS - extractive body cue:** Go2 default controller fails to climb up high obstacles like beds and sofas, whereas No Tracking only generates an open-loop trajectory of commands and fails ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), objective p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), temporal p. 5 (VI. EXPERIMENTS), p. 5 (VI. EXPERIMENTS), p. 6 (VI. EXPERIMENTS), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 3 (IV. LEARNING A GENERAL WHOLE-BODY CONTROLLER), p. 4 (V. ZERO-SHOT DEPLOYMENT USING VLMS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
