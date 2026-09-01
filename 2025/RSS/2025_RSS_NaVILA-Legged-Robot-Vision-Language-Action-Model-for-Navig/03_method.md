# Method - NaVILA: Legged Robot Vision-Language-Action Model for Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p018.html; PDF retrieval source: https://arxiv.org/pdf/2412.04453. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (II. METHOD), p. 3 (II. METHOD), p. 2 (II. METHOD), p. 5 (II. METHOD), p. 4 (II. METHOD), p. 4 (II. METHOD)): VILA undergoes a 3-stage training process: first, it pre-trains a connector between the frozen LLM and vision backbones using alignment data [20]; then it pre-trains both the connector and the ...

## Method Body Digest

- **p. 3 / II. METHOD - extractive body cue:** VILA undergoes a 3-stage training process: first, it pre-trains a connector between the frozen LLM and vision backbones using alignment data [20]; then it pre-trains ...
- **p. 3 / II. METHOD - extractive body cue:** Our VLA model processes single-view images to produce mid-level actions in natural language, which are then converted into precise joint movements by an advanced low-level ...
- **p. 2 / II. METHOD - extractive body cue:** We first describe how we tame VLMs for high-level VLN in Sec.II-A, then outline our robot configuration and locomotion policy in Sec.
- **p. 5 / II. METHOD - extractive body cue:** This control policy is trained in the Isaac Sim simulator using Isaac Lab [36] and then directly deployed to the real-world robot.
- **p. 4 / II. METHOD - extractive body cue:** For training, we use multi-view RGB images from the raw scans to support this task.
- **p. 4 / II. METHOD - extractive body cue:** Following [12], we use augmented instructions from EnvDrop [31] and introduce an auxiliary task of navigation trajectory summarization.
- **p. 5 / II. METHOD - extractive body cue:** The action space a of the control policy is defined as the desired joint position qd ∈R12, which is converted into torque input for the ...
- **p. 5 / II. METHOD - extractive body cue:** The right image shows a preprocessed height map with values clipped to sensor constraints; darker colors indicate higher heights.

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** To better simulate the challenges of locomotion navigation in VLN, we introduce a new benchmark, VLN-CE-Isaac, using Isaac Sim.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Inspired by the recent progress on VLM [10, 11] for spatial location and distance reasoning, we propose NaVILA, a twolevel framework for legged robot VLN: ...
- **p. 3 / II. METHOD - extractive body cue:** VILA consists of three main components: a vision encoder, a projector, and an LLM.

## Source Evidence Cues

- **p. 3 / II. METHOD - extractive body cue:** VILA undergoes a 3-stage training process: first, it pre-trains a connector between the frozen LLM and vision backbones using alignment data [20]; then it pre-trains ...
- **p. 3 / II. METHOD - extractive body cue:** Our VLA model processes single-view images to produce mid-level actions in natural language, which are then converted into precise joint movements by an advanced low-level ...
- **p. 2 / II. METHOD - extractive body cue:** We first describe how we tame VLMs for high-level VLN in Sec.II-A, then outline our robot configuration and locomotion policy in Sec.
- **p. 5 / II. METHOD - extractive body cue:** This control policy is trained in the Isaac Sim simulator using Isaac Lab [36] and then directly deployed to the real-world robot.
- **p. 4 / II. METHOD - extractive body cue:** For training, we use multi-view RGB images from the raw scans to support this task.
- **p. 4 / II. METHOD - extractive body cue:** Following [12], we use augmented instructions from EnvDrop [31] and introduce an auxiliary task of navigation trajectory summarization.
- **p. 5 / II. METHOD - extractive body cue:** The action space a of the control policy is defined as the desired joint position qd ∈R12, which is converted into torque input for the ...
- **Detected method headings:** II. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | VILA undergoes a 3-stage training process: first, it pre-trains a connector between the frozen LLM and vision backbones using alignment data [20]; ... | p. 3 (II. METHOD), p. 3 (II. METHOD) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Our VLA model processes single-view images to produce mid-level actions in natural language, which are then converted into precise joint movements by ... | p. 3 (II. METHOD), p. 2 (II. METHOD) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | We first describe how we tame VLMs for high-level VLN in Sec.II-A, then outline our robot configuration and locomotion policy in Sec. | p. 2 (II. METHOD), p. 5 (II. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / II. METHOD - extractive body cue:** The right image shows a preprocessed height map with values clipped to sensor constraints; darker colors indicate higher heights.
- **p. 5 / II. METHOD - extractive body cue:** During training, the critic observes the privileged environment and generates a value function to update the actor, while the actor only receives sensor data available ...
- **p. 3 / II. METHOD - extractive body cue:** However, recent progress in VLMs has largely been driven by the availability of imagetext data.
- **p. 3 / II. METHOD - extractive body cue:** On the other hand, frames before time step t are historical frames that function as a memory bank, helping the agent track overall progress (e.g., ...
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 5 (II. METHOD), p. 5 (II. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Inspired, recent, progress, VLM, spatial, location, distance, reasoning, NaVILA, twolevel, framework, legged, robot, VLN | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | Inspired, recent, progress, VLM, spatial, location, distance, reasoning, NaVILA, twolevel | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | better, simulate, challenges, locomotion, navigation, VLN, introduce, benchmark, VLN-CE-Isaac, Isaac | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | right, image, preprocessed, height, values, clipped, sensor, constraints, darker, colors | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / I. INTRODUCTION - extractive body cue:** Inspired by the recent progress on VLM [10, 11] for spatial location and distance reasoning, we propose NaVILA, a twolevel framework for legged robot VLN: ...
- **p. 3 / II. METHOD - extractive body cue:** Instruction Joint Positions Policy π VLA History Views Velocity Commands Proprioception Prior Actions Joint Pos. & Vel.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The advantages of this framework are three-fold: (i) By decoupling low-level execution from VLAs, the same VLA can be applied across different robots by swapping ...
- **p. 5 / II. METHOD - extractive body cue:** The action space a of the control policy is defined as the desired joint position qd ∈R12, which is converted into torque input for the ...
- **p. 5 / II. METHOD - extractive body cue:** As in our formulation, VLM outputs a fixed set of actionable words, such as {move forward, turn left, turn right, stop}, we casts these instructions ...
- **p. 3 / II. METHOD - extractive body cue:** Taming VLMs for Vision Language Navigation VLN requires processing video inputs as observations.
- **p. 4 / II. METHOD - extractive body cue:** Next, we estimate camera poses using MASt3R [27] to extract step-bystep actions, and we generate natural language instructions for each trajectory using VLM-based [13] captioning ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | On the other hand, frames before time step t are historical frames that function as a memory bank, helping the agent track ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | This results in step-wise navigation videos, where each sample comprises a (t + 1)-frame video and the corresponding oracle action at time ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | On the other hand, frames before time step t are historical frames that function as a memory bank, helping the agent track ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | With the support of ray-casting in Isaac Lab, our vision-based RL policy training achieves a high throughput over 60K FPS on an ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / II. METHOD - extractive body cue:** VILA undergoes a 3-stage training process: first, it pre-trains a connector between the frozen LLM and vision backbones using alignment data [20]; then it pre-trains ...
- **p. 5 / II. METHOD - extractive body cue:** This control policy is trained in the Isaac Sim simulator using Isaac Lab [36] and then directly deployed to the real-world robot.
- **p. 4 / II. METHOD - extractive body cue:** For training, we use multi-view RGB images from the raw scans to support this task.
- **p. 6 / III. EXPERIMENTS - extractive body cue:** In ROA training, the model first learns a privileged encoder that processes height scan points and other privileged observations.
- **p. 5 / II. METHOD - extractive body cue:** With the support of ray-casting in Isaac Lab, our vision-based RL policy training achieves a high throughput over 60K FPS on an RTX 4090 GPU.
- **p. 4 / II. METHOD - extractive body cue:** During this training, all three components-vision encoder, connector, and LLM-are unfrozen.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** VILA, undergoes, stage, training, process, first, pre-trains, connector, between, frozen, LLM, vision, backbones, alignment, data, then, text-image, interleaved, corpus, finally.
- **Relevant PDF headings:** II. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | To evaluate NaVILA's capabilities in scene understanding, we conduct evaluations on the ScanQA Validation benchmark, a widely used dataset for 3D Question ... | p. 6 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |
| Whole-body policy / controller | We also compare NaVILAs with a baseline using Oracle's low-level policy (assuming perfect command execution without realistic physics). | p. 7 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS) |
| Adaptation / recovery | Workspace Home Outdoor Simple Complex Simple Complex Simple Complex NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑NE↓SR↑ Unitree Go2 GPT-4o [28] 2.01 0.67 2.38 0.33 1.49 0.53 3.00 0.00 ... | p. 8 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 6 / III. EXPERIMENTS - extractive body cue:** All results are obtained without training on the RxRCE training set.
- **p. 7 / III. EXPERIMENTS - extractive body cue:** We also compare NaVILAs with a baseline using Oracle's low-level policy (assuming perfect command execution without realistic physics).
- **p. 7 / III. EXPERIMENTS - extractive body cue:** Existing benchmarks [29, 30] for vision-language navigation are based on the Habitat [69] simulator, which focuses on high-level planning without addressing precise low-level robotic control.
- **p. 8 / III. EXPERIMENTS - extractive body cue:** Note that † indicates models trained without human touring videos.
- **p. 8 / III. EXPERIMENTS - extractive body cue:** To demonstrate the flexibility of our two-level approach, we also evaluated it on a Booster Dynamics T1 humanoid robot, using the same VLA model without ...
- **p. 6 / III. EXPERIMENTS - extractive body cue:** Notably, this also marks the first time a VLN agent, trained solely on single-view RGB input, achieves comparable or superior results to models that use ...
- **p. 9 / V. CONCLUSION AND LIMITATIONS - extractive body cue:** While NaVILA demonstrates strong performance, it fails in some real-world cases (see Appx.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (II. METHOD), p. 3 (II. METHOD), p. 2 (II. METHOD), p. 5 (II. METHOD), p. 4 (II. METHOD), p. 4 (II. METHOD), objective p. 5 (II. METHOD), p. 5 (II. METHOD), p. 3 (II. METHOD), p. 3 (II. METHOD), temporal p. 3 (II. METHOD), p. 4 (II. METHOD), p. 3 (II. METHOD), p. 5 (II. METHOD), p. 4 (II. METHOD), p. 2 (II. METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
