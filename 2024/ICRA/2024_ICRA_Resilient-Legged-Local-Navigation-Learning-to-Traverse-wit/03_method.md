# Method - Resilient Legged Local Navigation: Learning to Traverse with Compromised Perception End-to-End

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2310.03581; PDF retrieval source: https://arxiv.org/pdf/2310.03581. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. METHOD), p. 2 (III. METHOD), p. 2 (III. METHOD)): Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with Privileged Information Observations ...

## Method Body Digest

- **p. 3 / III. METHOD - extractive body cue:** Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with Privileged ...
- **p. 2 / III. METHOD - extractive body cue:** Overview The objective of our method is to guide the robot to a local target within the given time.
- **p. 2 / III. METHOD - extractive body cue:** Given a preestablished low-level locomotion policy [6], we train a navigation policy that generates velocity commands to be tracked in a hierarchical RL structure.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The learned navigation policy generates velocity commands to a pre-existing low-level locomotion policy, and takes low-level observations as part of its inputs.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Most of them construct an explicit map for path planning based on traversability [1], [8] or geometry information [10], [11] of the surroundings, and some ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** (C) Our proposed policy can react to perception failures and reach the target.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we propose to incorporate locomotion-level observations into navigation, contrasting existing methods that typically decouple navigation from locomotion.
- **p. 2 / III. METHOD - extractive body cue:** Overview The objective of our method is to guide the robot to a local target within the given time.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, such manually-designed rules cannot scale well to diverse situations.

## Source Evidence Cues

- **p. 3 / III. METHOD - extractive body cue:** Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with Privileged ...
- **p. 2 / III. METHOD - extractive body cue:** Overview The objective of our method is to guide the robot to a local target within the given time.
- **p. 2 / III. METHOD - extractive body cue:** Given a preestablished low-level locomotion policy [6], we train a navigation policy that generates velocity commands to be tracked in a hierarchical RL structure.
- **Detected method headings:** 1) The methodology to learn local navigation strategies (p. 2); 3) Experimental validation of our method both in simula (p. 2); III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values ... | p. 3 (III. METHOD), p. 2 (III. METHOD) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Overview The objective of our method is to guide the robot to a local target within the given time. | p. 2 (III. METHOD), p. 2 (III. METHOD) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | Given a preestablished low-level locomotion policy [6], we train a navigation policy that generates velocity commands to be tracked in a hierarchical ... | p. 2 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / III. METHOD - extractive body cue:** Overview The objective of our method is to guide the robot to a local target within the given time.
- **p. 3 / III. METHOD - extractive body cue:** Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with Privileged ...
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 2 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Actor, Critic, Low-Level, Exteroception, Proprioception, Previous, Action, Position, Command, Heading, Corrupted, Map, Navigation, Latent | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | Actor, Critic, Low-Level, Exteroception, Proprioception, Previous, Action, Position, Command, Heading | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | incorporate, locomotion-level, observations, navigation, contrasting, existing, methods, typically, decouple, locomotion | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | Overview, objective, guide, robot, local, target, within, given, time, Actor | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive body cue:** Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values Observations with Privileged ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The learned navigation policy generates velocity commands to a pre-existing low-level locomotion policy, and takes low-level observations as part of its inputs.
- **p. 2 / III. METHOD - extractive body cue:** Given a preestablished low-level locomotion policy [6], we train a navigation policy that generates velocity commands to be tracked in a hierarchical RL structure.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Most of them construct an explicit map for path planning based on traversability [1], [8] or geometry information [10], [11] of the surroundings, and some ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** (C) Our proposed policy can react to perception failures and reach the target.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | 5) No LSTM Memory (NoMem): This setting differs from Ours in that we replace the LSTM layer in the actor network with ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | Actor Critic Low-Level Exteroception Proprioception Previous Action Position Command Heading Command Corrupted Map Navigation Action Latent Features Feature Mixing LSTM Memory Values ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Proprioception: The proprioception consists of the base linear velocity vt, the base angular velocity ωt, the last five frames of the base ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / III. METHOD - extractive body cue:** Given a preestablished low-level locomotion policy [6], we train a navigation policy that generates velocity commands to be tracked in a hierarchical RL structure.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Actor, Critic, Low-Level, Exteroception, Proprioception, Previous, Action, Position, Command, Heading, Corrupted, Map, Navigation, Latent, Features, Feature, Mixing, LSTM, Memory, Values.
- **Relevant PDF headings:** 1) The methodology to learn local navigation strategies (p. 2); 3) Experimental validation of our method both in simula (p. 2); III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Environments We verify our methodology on the quadruped ANYmal robot both in simulation and in the real world. | p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP) |
| Whole-body policy / controller | Comparison Results We compare the proposed Ours with the baselines Oracle and Planner in simulation. | p. 5 (V. RESULTS AND ANALYSES), p. 4 (IV. EXPERIMENTAL SETUP) |
| Adaptation / recovery | According to the results, all of the policies perform well when the visibility is 100 %, and the Planner achieves a perfect ... | p. 5 (V. RESULTS AND ANALYSES), p. 5 (V. RESULTS AND ANALYSES) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. An illustration of what happens under perception failures, exem- plified by an invisible obstacle case. (A) Without perception failures, both classical planners and ...
- **p. 5 / V. RESULTS AND ANALYSES - extractive body cue:** Ablation Studies We evaluate different settings for ablation studies in simulation.
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 8. Results of ablation studies. Ours outperforms others in the metrics. commands directing away from the pit until the robot regains stability.
- **p. 4 / IV. EXPERIMENTAL SETUP - extractive body cue:** 5) No LSTM Memory (NoMem): This setting differs from Ours in that we replace the LSTM layer in the actor network with an MLP layer.
- **p. 6 / VI. LIMITATIONS AND FUTURE WORKS - extractive body cue:** Despite our policy's generalization to different collision geometries, we find it cannot handle out-of-distribution mapping noises.
- **p. 5 / V. RESULTS AND ANALYSES - extractive body cue:** These results indicate that the navigation policy cannot learn to react to perception failures without being exposed to them, and the locomotion policy cannot overcome ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2. Besides reaching the target in time, the robot should also reduce base collisions and avoid falls. An overview of our system is in ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHOD), p. 2 (III. METHOD), p. 2 (III. METHOD), objective p. 2 (III. METHOD), p. 3 (III. METHOD), temporal p. 3 (III. METHOD), p. 4 (IV. EXPERIMENTAL SETUP), p. 4 (IV. EXPERIMENTAL SETUP), p. 3 (10 Hz), p. 1 (Abstract), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
