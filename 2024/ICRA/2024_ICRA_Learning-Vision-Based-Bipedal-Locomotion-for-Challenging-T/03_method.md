# Method - Learning Vision-Based Bipedal Locomotion for Challenging Terrain

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2309.14594; PDF retrieval source: https://arxiv.org/pdf/2309.14594. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY)): We use a neural network to represent the policy for mapping observation sequences to actions.

## Method Body Digest

- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** We use a neural network to represent the policy for mapping observation sequences to actions.
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Below, we describe the observation space, action space, architecture of the policy, and training methods.
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The RL policy operates at 50Hz and outputs PD setpoints for all motors, which are provided to a PD controller operating at 2kHz.
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The model parameters are randomized per episode to simulate a range of robot models and also provide a wide range of state space that the ...
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Control Policy Design Observation Space.
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Parameters Range Unit Simulation Model Joint Damping [0.5, 2.5] % Mass [-0.25, 0.25] % Center of Mass Location [-0.01, 0.01] m Passive Spring Stiffness [-500, ...
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** However, due to the nature of RL, this term only acts as a soft constraint that the robot may violate in favor of not falling ...
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The main control objective is to follow speed and heading commands while maintaining balance over possibly challenging terrains.

## Design Rationale

- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The relative encoding means that the heights vary as the robot moves up and down during its gait, but enables us to avoid using global ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The key contribution of our work is the sim-to-real pipeline and the system integration for these components, which allows the overall locomotion controller to transfer ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The proposed approach enables bipedal robot Cassie traversing over challenging terrains, including random high blocks, stairs, 0.5m step up (∼60% leg length), with speed up ...

## Source Evidence Cues

- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** We use a neural network to represent the policy for mapping observation sequences to actions.
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Below, we describe the observation space, action space, architecture of the policy, and training methods.
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The RL policy operates at 50Hz and outputs PD setpoints for all motors, which are provided to a PD controller operating at 2kHz.
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The model parameters are randomized per episode to simulate a range of robot models and also provide a wide range of state space that the ...
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Control Policy Design Observation Space.
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Parameters Range Unit Simulation Model Joint Damping [0.5, 2.5] % Mass [-0.25, 0.25] % Center of Mass Location [-0.01, 0.01] m Passive Spring Stiffness [-500, ...
- **Detected method headings:** IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | We use a neural network to represent the policy for mapping observation sequences to actions. | p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Below, we describe the observation space, action space, architecture of the policy, and training methods. | p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | The RL policy operates at 50Hz and outputs PD setpoints for all motors, which are provided to a PD controller operating at ... | p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** However, due to the nature of RL, this term only acts as a soft constraint that the robot may violate in favor of not falling ...
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The main control objective is to follow speed and heading commands while maintaining balance over possibly challenging terrains.
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** First, we modified the PPO loss function to include a mirror loss over robot propriocepive inputs as well as visual inputs.
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The conditions correspond to undesirable robot behavior and implicitly punish the robot by causing it to not receive future rewards.
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** This reward helps prevent fast swing leg motions, which we found could arise during training on difficult terrain.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, vision-based, modulator, includes, available, observations, including, heightmap, addition, action, produced, blind, policy, particular | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | input, vision-based, modulator, includes, available, observations, including, heightmap, addition, action | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | relative, encoding, means, heights, vary, robot, moves, down, during, gait | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | However, nature, term, only, acts, soft, constraint, robot, violate, favor | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The input to the vision-based modulator includes all of the available observations, including the heightmap, in addition to the action produced by the blind policy.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In particular, our architecture is composed of two primary learned components: 1) a control policy whose input is proprioceptive information and a heightmap of a ...
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Below, we describe the observation space, action space, architecture of the policy, and training methods.
- **p. 3 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** We use a neural network to represent the policy for mapping observation sequences to actions.
- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The policy input includes: 1) proprioceptive information containing the orientation (in quaternion) and angular velocity of the floating base, and position and velocity for all ...
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Parameters Range Unit Simulation Model Joint Damping [0.5, 2.5] % Mass [-0.25, 0.25] % Center of Mass Location [-0.01, 0.01] m Passive Spring Stiffness [-500, ...
- **p. 4 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** The visual inputs are randomized to simulate noise from the heightmap estimator and prevent the policy from overfitting to the exact simulated heightmaps.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Each episode runs for a maximum of 400 timesteps, which is 8 seconds of simulated time. | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | After the initial command, once during each episode the command is randomly changed at a time randomly sampled from [200, 250] timesteps. | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | For each policy setup, we collect 1000 episodes per terrain mode and compute three metrics as shown in Figure 7-A. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY - extractive body cue:** Below, we describe the observation space, action space, architecture of the policy, and training methods.
- **p. 5 / VI. SIMULATION RESULTS - extractive body cue:** LSTM has implicit history, Transformer has a fixed window size of 0.6 seconds to allow reasonable inference during runtime, and MLP does not have history.
- **p. 6 / VI. SIMULATION RESULTS - extractive body cue:** Episodes with foot collision indicates the number of episodes that have one or more foot collision events occurred during rollouts, and such random collision events ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** neural, network, represent, policy, mapping, observation, sequences, actions, Below, describe, space, action, architecture, training, methods, operates, outputs, setpoints, motors, provided.
- **Relevant PDF headings:** IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Episodes with foot collision indicates the number of episodes that have one or more foot collision events occurred during rollouts, and such ... | p. 6 (VI. SIMULATION RESULTS), p. 5 (VI. SIMULATION RESULTS) |
| Whole-body policy / controller | Episodes with foot collision shows that, compared to Ours, other policies have significantly more foot collisions events. | p. 5 (VI. SIMULATION RESULTS), p. 6 (VI. SIMULATION RESULTS) |
| Adaptation / recovery | Fig. 6: Depth image from simulation and real world, with corre- sponding real predicted heightmap and simulation heightmap. mode of terrains. For ... | p. 5 (Figure/Table caption), p. 5 (VI. SIMULATION RESULTS) |

## Failure and Ablation Link

- **p. 5 / VI. SIMULATION RESULTS - extractive body cue:** Policy Performance We use the trained policy, along with a number of different policy setups, to evaluate the performance in simulation for the ablation study.
- **p. 5 / VI. SIMULATION RESULTS - extractive body cue:** We also implemented other architectures to use for ablations, including an MLP model and a transformer-based model, and they all have robot states and depth ...
- **p. 6 / VI. SIMULATION RESULTS - extractive body cue:** Ablation study on policy with different heightmap predictor architectures.
- **p. 6 / VI. SIMULATION RESULTS - extractive body cue:** Each ablation study uses data collected from a range of terrains defined in Table I.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of the locomotion policy with vision module. Figure 2 illustrates our overall system, which has two main components: 1) a locomotion policy, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Types of terrain used in training. a real robot. In particular, we use a three component reward function where all components are weighted ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 7: A. Ablation study on policy with simulation heightmap. B. Ablation study on policy with different heightmap predictor architectures. Each ablation study uses data ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), objective p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 2 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), temporal p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 3 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 4 (IV. LEARNING A TERRAIN-AWARE LOCOMOTION POLICY), p. 5 (V. HEIGHTMAP PREDICTION FROM EGOCENTRIC VISION), p. 6 (VI. SIMULATION RESULTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
