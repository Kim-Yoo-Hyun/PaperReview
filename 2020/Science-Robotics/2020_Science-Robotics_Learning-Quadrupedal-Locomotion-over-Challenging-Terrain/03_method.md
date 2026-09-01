# Method - Learning Quadrupedal Locomotion over Challenging Terrain

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.11251; PDF retrieval source: https://arxiv.org/pdf/2010.11251. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS), p. 7 (4. MATERIALS AND METHODS)): The model computes a latent embedding ¯lt that represents the current state, and an action ¯at.

## Method Body Digest

- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The model computes a latent embedding ¯lt that represents the current state, and an action ¯at.
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The student model is a temporal convolutional network (TCN) [22] that receives a sequence of N proprioceptive observations as input.
- **p. 7 / 4. MATERIALS AND METHODS - extractive body cue:** Research Article ETH Zurich and Intel 7 terrain traversability for the policy height map Automatic terrain curriculum
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The training objective rewards locomotion in prescribed directions.
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** Overview The main objective of the presented controller is to locomote over rough terrain following a command.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We have found that training a rough-terrain locomotion policy directly via reinforcement learning was not successful: the supervisory signal was sparse and the presented network ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Many rely on elaborate state machines that coordinate the execution of motion primitives and reflex controllers [1-5].
- **p. 1 / 1. INTRODUCTION - extractive body cue:** They can choose safe footholds within their kinematic reach and rapidly change their kinematic state in response to the environment.

## Design Rationale

- **p. 3 / 1. INTRODUCTION - extractive body cue:** Here we present a radically robust controller for blind quadrupedal locomotion on challenging terrain.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Our methodology and results open new frontiers for legged robotics and suggest that the extraordinary complexity of the physical world can be tamed without brittle ...
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** An overview of our method is given in Fig.

## Source Evidence Cues

- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The model computes a latent embedding ¯lt that represents the current state, and an action ¯at.
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The student model is a temporal convolutional network (TCN) [22] that receives a sequence of N proprioceptive observations as input.
- **p. 7 / 4. MATERIALS AND METHODS - extractive body cue:** Research Article ETH Zurich and Intel 7 terrain traversability for the policy height map Automatic terrain curriculum
- **Detected method headings:** 4. MATERIALS AND METHODS (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | The model computes a latent embedding ¯lt that represents the current state, and an action ¯at. | p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | The student model is a temporal convolutional network (TCN) [22] that receives a sequence of N proprioceptive observations as input. | p. 6 (4. MATERIALS AND METHODS), p. 7 (4. MATERIALS AND METHODS) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | Research Article ETH Zurich and Intel 7 terrain traversability for the policy height map Automatic terrain curriculum | p. 7 (4. MATERIALS AND METHODS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The training objective rewards locomotion in prescribed directions.
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** Overview The main objective of the presented controller is to locomote over rough terrain following a command.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | model, computes, latent, embedding, represents, current, state, action, student, temporal, convolutional, network, TCN, receives | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | model, computes, latent, embedding, represents, current, state, action, student, temporal | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | Here, present, radically, robust, controller, blind, quadrupedal, locomotion, challenging, terrain | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | training, objective, rewards, locomotion, prescribed, directions, Overview, main, presented, controller | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The model computes a latent embedding ¯lt that represents the current state, and an action ¯at.
- **p. 6 / 4. MATERIALS AND METHODS - extractive body cue:** The student model is a temporal convolutional network (TCN) [22] that receives a sequence of N proprioceptive observations as input.
- **p. 7 / 4. MATERIALS AND METHODS - extractive body cue:** Research Article ETH Zurich and Intel 7 terrain traversability for the policy height map Automatic terrain curriculum
- **p. 3 / 1. INTRODUCTION - extractive body cue:** We have found that training a rough-terrain locomotion policy directly via reinforcement learning was not successful: the supervisory signal was sparse and the presented network ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Many rely on elaborate state machines that coordinate the execution of motion primitives and reflex controllers [1-5].
- **p. 1 / 1. INTRODUCTION - extractive body cue:** They can choose safe footholds within their kinematic reach and rapidly change their kinematic state in response to the environment.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The first is a different policy architecture.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | The sample complexity of model-free RL algorithms, which commonly require millions of time steps for training, further exacerbates the challenge by precluding ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | At every time step t, φi = (φi,0 + ( f0 + fi)t) (mod 2π) where φi,0 is the initial phase, f0 ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | Rather than using a multi-layer perceptron (MLP) that operates on a snapshot of the robot's current state, as was common in prior ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | We conducted 10 trials for each step height and computed the success rate. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** model, computes, latent, embedding, represents, current, state, action, student, temporal, convolutional, network, TCN, receives, sequence, proprioceptive, observations, input, Research, Article.
- **Relevant PDF headings:** 4. MATERIALS AND METHODS (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | The objective of the competition is to develop robotic systems that rapidly map, navigate, and search complex underground environments, including tunnels, urban ... | p. 5 (2. RESULTS), p. 3 (2. RESULTS) |
| Whole-body policy / controller | We have compared the presented controller to a state-of-the-art baseline [1, 26] in the forest environment. | p. 5 (2. RESULTS), p. 5 (2. RESULTS) |
| Adaptation / recovery | (E) Success rates for different step heights. | p. 4 (2. RESULTS), p. 4 (2. RESULTS) |

## Failure and Ablation Link

- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5. Ablation studies. We trained each model 5 times using different random seeds. Error bars denote 95 % confidence intervals. (A) Test setups. The ...
- **p. 4 / 2. RESULTS - extractive body cue:** Our controller and a baseline [1, 26] are commanded to walk over a step with and without the 10 kg payload.
- **p. 5 / 2. RESULTS - extractive body cue:** The baseline showed high sensitivity to foot-trapping, which often led to a fall, as shown in Movie S3.
- **p. 5 / 2. RESULTS - extractive body cue:** Accordingly, the locomotion controller needs to perform without failure over extended mission durations.
- **p. 6 / 2. RESULTS - extractive body cue:** In contrast, the average heading error of the presented controller stays within 10 ◦with or without the payload.
- **p. 6 / 2. RESULTS - extractive body cue:** The heading error of the presented controller is consistently smaller than the baseline, both with and without the payload.
- **p. 6 / 3. DISCUSSION - extractive body cue:** We see a number of limitations and opportunities for future work.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS), p. 7 (4. MATERIALS AND METHODS), objective p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS), temporal p. 6 (3. DISCUSSION), p. 8 (50 Hz), p. 10 (50 N external force), p. 6 (4. MATERIALS AND METHODS), p. 3 (1. INTRODUCTION), p. 9 (50 Hz).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
