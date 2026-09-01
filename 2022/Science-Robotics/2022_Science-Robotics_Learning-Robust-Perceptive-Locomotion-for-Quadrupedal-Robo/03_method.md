# Method - Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.08117; PDF retrieval source: https://arxiv.org/pdf/2201.08117. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 8 (4. MATERIALS AND METHODS), p. 8 (4. MATERIALS AND METHODS), p. 10 (1. Teacher policy training)): Overview We train a neural network policy in simulation and then perform zeroshot sim-to-real transfer.

## Method Body Digest

- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** Overview We train a neural network policy in simulation and then perform zeroshot sim-to-real transfer.
- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** First, a teacher policy is trained with RL to follow a random target velocity over randomly generated terrain with random disturbances.
- **p. 10 / 1. Teacher policy training - extractive body cue:** Height scan Proprioception Privileged info Teacher Policy Action joint difference phase difference
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The controller gets onboard sensor observations and a desired velocity command, and outputs each joint's target position as the action.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The student policy learns to predict the teacher's optimal action given only partial and noisy observations of the environment.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Stereo camera based depth sensors, which most existing legged robots rely on [6, 9, 12], require texture to perform stereo matching and consequently struggle with ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** An elevation map is commonly used to represent geometric terrain information extracted from depth sensor measurements [14-17].

## Design Rationale

- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** Our method consists of three stages, illustrated in Figure 6.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Here we present a terrain-aware locomotion controller for quadrupedal robots that overcomes limitations of previous approaches and enables robust traversal of harsh natural terrain at ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The elevation map serves as an abstraction layer between sensors and the locomotion controller, making our method independent of depth sensor choices.

## Source Evidence Cues

- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** Overview We train a neural network policy in simulation and then perform zeroshot sim-to-real transfer.
- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** First, a teacher policy is trained with RL to follow a random target velocity over randomly generated terrain with random disturbances.
- **p. 10 / 1. Teacher policy training - extractive body cue:** Height scan Proprioception Privileged info Teacher Policy Action joint difference phase difference
- **Detected method headings:** 4. MATERIALS AND METHODS (p. 8); 1. Teacher policy training (p. 10); 2. Student policy training (p. 10)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Overview We train a neural network policy in simulation and then perform zeroshot sim-to-real transfer. | p. 8 (4. MATERIALS AND METHODS), p. 8 (4. MATERIALS AND METHODS) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | First, a teacher policy is trained with RL to follow a random target velocity over randomly generated terrain with random disturbances. | p. 8 (4. MATERIALS AND METHODS), p. 10 (1. Teacher policy training) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | Height scan Proprioception Privileged info Teacher Policy Action joint difference phase difference | p. 10 (1. Teacher policy training) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | controller, gets, onboard, sensor, observations, desired, velocity, command, outputs, joint, target, position, action, student | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | controller, gets, onboard, sensor, observations, desired, velocity, command, outputs, joint | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | consists, three, stages, illustrated, Figure, Here, present, terrain-aware, locomotion, controller | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | not recovered | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 1. INTRODUCTION - extractive body cue:** The controller gets onboard sensor observations and a desired velocity command, and outputs each joint's target position as the action.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** The student policy learns to predict the teacher's optimal action given only partial and noisy observations of the environment.
- **p. 10 / 1. Teacher policy training - extractive body cue:** Height scan Proprioception Privileged info Teacher Policy Action joint difference phase difference
- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** First, a teacher policy is trained with RL to follow a random target velocity over randomly generated terrain with random disturbances.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Stereo camera based depth sensors, which most existing legged robots rely on [6, 9, 12], require texture to perform stereo matching and consequently struggle with ...
- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** Overview We train a neural network policy in simulation and then perform zeroshot sim-to-real transfer.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** An elevation map is commonly used to represent geometric terrain information extracted from depth sensor measurements [14-17].
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Research Article ETH Zurich and Intel 13 Select with probability Height scan noise model Per point noise (sampled every timestep) Per foot ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | Problem formulation We formulate our control problem in discrete time dynamics, where the environment is fully defined by the state st at ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Wooden steps of various height (from 12 cm to 36.5 cm) were placed ahead of the robot, which performed 10 trials to ... | hardware, batch and throughput |

## Training vs Inference

- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** Overview We train a neural network policy in simulation and then perform zeroshot sim-to-real transfer.
- **p. 8 / 4. MATERIALS AND METHODS - extractive body cue:** First, a teacher policy is trained with RL to follow a random target velocity over randomly generated terrain with random disturbances.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Overview, train, neural, network, policy, simulation, then, perform, zeroshot, sim-to-real, transfer, First, teacher, trained, follow, random, target, velocity, over, randomly.
- **Relevant PDF headings:** 4. MATERIALS AND METHODS (p. 8); 1. Teacher policy training (p. 10); 2. Student policy training (p. 10).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | The robot perceives the environment in the form of height samples from an elevation map constructed from point cloud input, as seen ... | p. 5 (2. RESULTS), p. 3 (2. RESULTS) |
| Whole-body policy / controller | We compared our controller to a proprioceptive baseline [4] that does not use exteroception. | p. 5 (2. RESULTS), p. 5 (2. RESULTS) |
| Adaptation / recovery | First, we compared the success rate of overcoming fixed-height steps as shown in Figure 4A. | p. 5 (2. RESULTS), p. 5 (2. RESULTS) |

## Failure and Ablation Link

- **p. 5 / 2. RESULTS - extractive body cue:** The baseline, on the other hand, failed to track the path without human assistance.
- **p. 5 / 2. RESULTS - extractive body cue:** Our controller followed the given path smoothly without any assistance, as shown in Figure 4C.
- **p. 8 / 2. RESULTS - extractive body cue:** With an unobstructed sensor, the controller traversed the stairs gracefully, without any unintended contact with the stair risers, adjusting its footholds and body posture to ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 6. Details of robust terrain perception components. (A) During student training, random noise is added to the height samples. The noise is sampled from ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. Internal belief state inspection during perceptive failure using a learned belief decoder. Red dots indicate height samples given as input to the policy. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Robust locomotion in the wild. The presented locomotion controller was extensively tested in a variety of complex environments over multiple seasons. The controller ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 6. Details of robust terrain perception components. (A) During student training, random noise is added to the height samples. The noise is sampled from ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 8 (4. MATERIALS AND METHODS), p. 8 (4. MATERIALS AND METHODS), p. 10 (1. Teacher policy training), objective 본문 anchor 없음, temporal p. 13 (2. Perturbing the height values), p. 11 (3. Deployment), p. 12 (2. Perturbing the height values), p. 11 (3. Deployment), p. 12 (3. Deployment), p. 1 (1. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
