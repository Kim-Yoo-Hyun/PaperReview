# Method - ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14874; PDF retrieval source: https://arxiv.org/pdf/2306.14874. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3) We develop a neural terrain reconstruction method that), p. 3 (3) We develop a neural terrain reconstruction method that), p. 14 (IV. MATERIALS AND METHODS), p. 3 (3) We develop a neural terrain reconstruction method that), p. 12 (IV. MATERIALS AND METHODS), p. 12 (IV. MATERIALS AND METHODS)): Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and robotics [18].

## Method Body Digest

- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and robotics [18].
- **p. 3 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** We also modify the network architecture to allow for efficient inference with large batch sizes during RL training.
- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** This leads to the natural progression where the policy first learns to climb using its knees and then starts using its feet instead when possible. ...
- **p. 3 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** In parallel, bipedal robots have also demonstrated their agile capabilities by walking blindly on rough terrain [20] and jumping on obstacles [21]. b) Navigation and ...
- **p. 12 / IV. MATERIALS AND METHODS - extractive body cue:** Due to the different formulation, we use a separate navigation policy for that scenario.
- **p. 12 / IV. MATERIALS AND METHODS - extractive body cue:** Pipeline The pipeline consists of three learning-based modules, which are described in the following subsections.
- **p. 4 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** The navigation module is given a target goal and uses the latent to plan a path and select the correct skill. of contacts that are ...
- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** The occupancy output is trained using a binary cross-entropy loss, while the centroids are trained using the Euclidean distance to the ground truth.

## Design Rationale

- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** Despite the promising results and the close similarity to our method, this work requires human-designed path and skill selection and is limited to a single ...
- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** To the best of our knowledge, we propose the first system that can perform agile navigation with a quadrupedal robot in such challenging scenarios without ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** We can summarize our contributions as follows:

## Source Evidence Cues

- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and robotics [18].
- **p. 3 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** We also modify the network architecture to allow for efficient inference with large batch sizes during RL training.
- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** This leads to the natural progression where the policy first learns to climb using its knees and then starts using its feet instead when possible. ...
- **p. 3 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** In parallel, bipedal robots have also demonstrated their agile capabilities by walking blindly on rough terrain [20] and jumping on obstacles [21]. b) Navigation and ...
- **p. 12 / IV. MATERIALS AND METHODS - extractive body cue:** Due to the different formulation, we use a separate navigation policy for that scenario.
- **p. 12 / IV. MATERIALS AND METHODS - extractive body cue:** Pipeline The pipeline consists of three learning-based modules, which are described in the following subsections.
- **p. 4 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** The navigation module is given a target goal and uses the latent to plan a path and select the correct skill. of contacts that are ...
- **Detected method headings:** 1) We propose a novel learned navigation approach that (p. 3); 3) We develop a neural terrain reconstruction method that (p. 3); IV. MATERIALS AND METHODS (p. 12)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and ... | p. 5 (3) We develop a neural terrain reconstruction method that), p. 3 (3) We develop a neural terrain reconstruction method that) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | We also modify the network architecture to allow for efficient inference with large batch sizes during RL training. | p. 3 (3) We develop a neural terrain reconstruction method that), p. 14 (IV. MATERIALS AND METHODS) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | This leads to the natural progression where the policy first learns to climb using its knees and then starts using its feet ... | p. 14 (IV. MATERIALS AND METHODS), p. 3 (3) We develop a neural terrain reconstruction method that) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** The occupancy output is trained using a binary cross-entropy loss, while the centroids are trained using the Euclidean distance to the ground truth.
- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** While the navigation module receives a full 3D representation of the map, it is impractical for the locomotion policies due to their high update rate ...
- **p. 4 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** For legged robots, the authors of [31] proposed to combine sampling-based planning with a learned motion cost for global path planning, resulting in a planner ...
- **p. 12 / IV. MATERIALS AND METHODS - extractive body cue:** Supplementary sections S1 and S2 define the observations, actions, and rewards of the locomotion and navigation policies and provide further implementation details.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 14 (IV. MATERIALS AND METHODS), p. 14 (IV. MATERIALS AND METHODS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, policies, receive, current, proprioceptive, state, local, surrounding, terrain, intermediate, command, output, position, commands | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | input, policies, receive, current, proprioceptive, state, local, surrounding, terrain, intermediate | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | Despite, promising, close, similarity, requires, human-designed, path, skill, selection, limited | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | occupancy, output, trained, binary, cross-entropy, loss, while, centroids, Euclidean, distance | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** As input, the policies receive the current proprioceptive state, a local map of the surrounding terrain, an intermediate command, and output position commands to the ...
- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** While these approaches produce a separate representation, the exteroceptive measurements can also be directly provided as input to the policy [8], [40].
- **p. 12 / IV. MATERIALS AND METHODS - extractive body cue:** The navigation and locomotion modules both use its output to make path planning, policy selection, foothold placement, and contact decisions.
- **p. 12 / IV. MATERIALS AND METHODS - extractive body cue:** Supplementary sections S1 and S2 define the observations, actions, and rewards of the locomotion and navigation policies and provide further implementation details.
- **p. 13 / IV. MATERIALS AND METHODS - extractive body cue:** Additionally, the coarse-resolution network benefits from an auto-regressive feedback, where the previous output is transformed into the current frame and concatenated with the measurement.
- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** Note that it does not use an autoregressive feedback, since temporal information is already contained in its input.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The complexity of the task exacerbates many of the challenges commonly faced by mobile robots: • The locomotion controller cannot rely on a stable and ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | We train these networks in an unsupervised fashion from simulated data on a total of 2000 trajectories with 100 timesteps each. | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | Despite the sparsity of the measurements on the top surface, the network remembers this region since it could be seen during the ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | We train these networks in an unsupervised fashion from simulated data on a total of 2000 trajectories with 100 timesteps each. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** Pre-training low-level skills with imitation learning and then controlling them through latent actions has been proposed for both character animation [33] and robotics [18].
- **p. 3 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** We also modify the network architecture to allow for efficient inference with large batch sizes during RL training.
- **p. 3 / 3) We develop a neural terrain reconstruction method that - extractive body cue:** We also modify the network architecture to allow for efficient inference with large batch sizes during RL training.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Pre-training, low-level, skills, imitation, learning, then, controlling, them, through, latent, actions, been, character, animation, robotics, modify, network, architecture, allow, efficient.
- **Relevant PDF headings:** 1) We propose a novel learned navigation approach that (p. 3); 3) We develop a neural terrain reconstruction method that (p. 3); IV. MATERIALS AND METHODS (p. 12).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot ... | p. 5 (II. RESULTS), p. 5 (II. RESULTS) |
| Whole-body policy / controller | The skill learns to turn on the spot in tight spaces and is more capable in such scenarios compared to other skills. | p. 5 (II. RESULTS), p. 11 (Figure/Table caption) |
| Adaptation / recovery | Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. ... | p. 8 (Figure/Table caption), p. 4 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / II. RESULTS - extractive body cue:** The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably reach ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Description of our approach. We decompose the problem into three components: The perception module receives the point cloud measurements to estimate the scene's ...
- **p. 12 / A. Current Limitations - extractive body cue:** Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires ...
- **p. 12 / A. Current Limitations - extractive body cue:** We develop a specific curriculum to overcome this limitation.
- **p. 5 / II. RESULTS - extractive body cue:** 3 (A2)), which is necessary for the leg to reach the other side of the gap and catch the fall of the robot during the ...
- **p. 5 / II. RESULTS - extractive body cue:** At this location, it has to perform precise foothold placement to pass the last step and prepare for the jump, despite the out-of-distribution scenario for ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3) We develop a neural terrain reconstruction method that), p. 3 (3) We develop a neural terrain reconstruction method that), p. 14 (IV. MATERIALS AND METHODS), p. 3 (3) We develop a neural terrain reconstruction method that), p. 12 (IV. MATERIALS AND METHODS), p. 12 (IV. MATERIALS AND METHODS), objective p. 14 (IV. MATERIALS AND METHODS), p. 14 (IV. MATERIALS AND METHODS), p. 4 (3) We develop a neural terrain reconstruction method that), p. 12 (IV. MATERIALS AND METHODS), temporal p. 14 (IV. MATERIALS AND METHODS), p. 10 (C B), p. 3 (3) We develop a neural terrain reconstruction method that), p. 3 (3) We develop a neural terrain reconstruction method that), p. 4 (3) We develop a neural terrain reconstruction method that), p. 5 (3) We develop a neural terrain reconstruction method that).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
