# Method - Learning Agile and Dynamic Motor Skills for Legged Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1901.08652; PDF retrieval source: https://arxiv.org/pdf/1901.08652. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (Front matter), p. 9 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter)): We use the hybrid simulator for training controllers via reinforcement learning (Fig.

## Method Body Digest

- **p. 3 / Front matter - extractive PDF cue:** We use the hybrid simulator for training controllers via reinforcement learning (Fig.
- **p. 9 / Front matter - extractive PDF cue:** Thus we use the policy network as an impedance controller.
- **p. 1 / Front matter - extractive PDF cue:** In the present work, we report a new method for training a neural network policy in simulation and transferring it to a state-of-the-art legged system, ...
- **p. 2 / Front matter - extractive PDF cue:** In general, trajectory optimization for a complex rigid-body model with many unspecified contact points is beyond the capabilities of current optimization techniques.
- **p. 2 / Front matter - extractive PDF cue:** These methods can discover a gait pattern (i.e., contact sequence) with hard contact models and have demonstrated automatic motion generation for 2D robotic systems but, ...
- **p. 3 / Front matter - extractive PDF cue:** The controller is represented by a multi-layer perceptron that takes as input the history of the robot's states and produces as output the joint position ...
- **p. 8 / Front matter - extractive PDF cue:** To this end, we use supervised learning to obtain an actionto-torque relationship that includes all software and hardware dynamics within one control loop.
- **p. 2 / Front matter - extractive PDF cue:** The idea of RL is to collect data by trial and error and automatically tune the controller to optimize the given cost (or reward) function ...

## Design Rationale

- **p. 2 / Front matter - extractive PDF cue:** Furthermore, the system still consists of two independent modules that do not adapt to each other's performance characteristics.
- **p. 4 / Front matter - extractive PDF cue:** A command consists of three components: forward velocity, lateral velocity, and yaw rate.
- **p. 4 / Front matter - extractive PDF cue:** Next, we compare our method to ablated alternatives: training with an ideal actuator model and training with an analytical actuator model.

## Source Evidence Cues

- **p. 3 / Front matter - extractive PDF cue:** We use the hybrid simulator for training controllers via reinforcement learning (Fig.
- **p. 9 / Front matter - extractive PDF cue:** Thus we use the policy network as an impedance controller.
- **p. 1 / Front matter - extractive PDF cue:** In the present work, we report a new method for training a neural network policy in simulation and transferring it to a state-of-the-art legged system, ...
- **p. 2 / Front matter - extractive PDF cue:** In general, trajectory optimization for a complex rigid-body model with many unspecified contact points is beyond the capabilities of current optimization techniques.
- **p. 2 / Front matter - extractive PDF cue:** These methods can discover a gait pattern (i.e., contact sequence) with hard contact models and have demonstrated automatic motion generation for 2D robotic systems but, ...
- **p. 3 / Front matter - extractive PDF cue:** The controller is represented by a multi-layer perceptron that takes as input the history of the robot's states and produces as output the joint position ...
- **p. 8 / Front matter - extractive PDF cue:** To this end, we use supervised learning to obtain an actionto-torque relationship that includes all software and hardware dynamics within one control loop.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | We use the hybrid simulator for training controllers via reinforcement learning (Fig. | p. 3 (Front matter), p. 9 (Front matter) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Thus we use the policy network as an impedance controller. | p. 9 (Front matter), p. 1 (Front matter) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | In the present work, we report a new method for training a neural network policy in simulation and transferring it to a ... | p. 1 (Front matter), p. 2 (Front matter) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / Front matter - extractive PDF cue:** The idea of RL is to collect data by trial and error and automatically tune the controller to optimize the given cost (or reward) function ...
- **p. 9 / Front matter - extractive PDF cue:** We refer to reward and cost interchangeably, with cost being the negative of the reward.
- **p. 9 / Front matter - extractive PDF cue:** The aim is to find a policy that maximizes the discounted sum of rewards over an infinite horizon: π∗= argmax π Eτ(π) " ∞ ∑ ...
- **p. 11 / Front matter - extractive PDF cue:** This way, the robot first learns how to achieve the objective and then how to respect various constraints.
- **p. 11 / Front matter - extractive PDF cue:** All of cost terms are multiplied by this curriculum factor, except the cost terms related to the objective (i.e., base velocity error cost in the ...
- **p. 6 / Front matter - extractive PDF cue:** For applications to new tasks, our method only requires a task description, which consists of the cost function, the initial state distribution, and randomization.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 11 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 5 (Front matter), p. 6 (Front matter), p. 8 (Front matter).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | setting, observations, measurements, robot, states, provided, controller, actions, position, commands, actuators, rewards, specified, induce | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | setting, observations, measurements, robot, states, provided, controller, actions, position, commands | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | Furthermore, system, still, consists, independent, modules, adapt, other, performance, characteristics | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | idea, collect, data, trial, error, automatically, tune, controller, optimize, given | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 9 / Front matter - extractive PDF cue:** In our setting, the observations are the measurements of robot states provided to the controller, the actions are the position commands to the actuators, and ...
- **p. 9 / Front matter - extractive PDF cue:** The whole observation at t = tk is defined as ok = ⟨φg, rz, v, ω, φ, ˙φ, Θ, ak-1, C⟩, where rz, v, and ...
- **p. 3 / Front matter - extractive PDF cue:** The controller is represented by a multi-layer perceptron that takes as input the history of the robot's states and produces as output the joint position ...
- **p. 8 / Front matter - extractive PDF cue:** The policy network maps the current observation and the joint state history to the joint position targets.
- **p. 10 / Front matter - extractive PDF cue:** (A) Validation set (B,C) Data from a command-conditioned policy experiment with 0.75 m/s forward command velocity and its corresponding policy network output, respectively (D,E) Data ...
- **p. 7 / Front matter - extractive PDF cue:** Using a policy network that directly outputs a joint-level command brings another advantage to our method.
- **p. 8 / Front matter - extractive PDF cue:** The rigid-body simulator outputs the next state of the robot given the joint torques and the current state.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Crucially, the full hybrid simulator, including a rigidbody simulation and the actuator nets, runs at nearly 500K time steps per second, which ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | The solver is not only accurate but also fast, generating about 900,000 time steps per second for the simulated quadruped on an ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Note that too sparse input configuration might not effectively capture the dynamics at high frequency (> 100 Hz). | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / Front matter - extractive PDF cue:** We use the hybrid simulator for training controllers via reinforcement learning (Fig.
- **p. 1 / Front matter - extractive PDF cue:** In the present work, we report a new method for training a neural network policy in simulation and transferring it to a state-of-the-art legged system, ...
- **p. 3 / Front matter - extractive PDF cue:** Thanks to efficient software implementations, we did not need any special computing hardware, such as multi-CPU or multi-GPU servers, for training.
- **p. 3 / Front matter - extractive PDF cue:** All training sessions presented in this paper were done on a personal computer with one CPU and one GPU, and none lasted more than eleven ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** hybrid, simulator, training, controllers, reinforcement, learning, Fig, Thus, policy, network, impedance, controller, present, report, neural, simulation, transferring, state-of-the-art, legged, system.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Many hardware changes were introduced as well: different robot configurations, which roughly contribute 2.0 kg to the total weight, and a new ... | p. 7 (Front matter), p. 6 (Front matter) |
| Whole-body policy / controller | It outperformed the previous speed record by 25 % and learned to consistently restore the robot to an operational configuration by dynamically ... | p. 6 (Front matter), p. 9 (Front matter) |
| Adaptation / recovery | We then further improved the success rate to 100 % by relaxing the joint velocity constraints. | p. 6 (Front matter), p. 9 (Front matter) |

## Failure and Ablation Link

- **p. 6 / Front matter - extractive PDF cue:** DISCUSSION The learning-based control approach presented in this paper achieved a new level of locomotion skill based purely on training in simulation and without tedious ...
- **p. 7 / Front matter - extractive PDF cue:** All control policies have been tested for more than three months on the real robot without any modification.
- **p. 9 / Front matter - extractive PDF cue:** However, since this height estimator cannot be used when the robot is not on its feet, we removed the height observation when training for recovery ...
- **p. 11 / Front matter - extractive PDF cue:** Samples that result in unrealistic internal collisions are removed.
- **p. 7 / Front matter - extractive PDF cue:** Developing the recovery policy took about a week largely due to the fact that some safety concerns (i.e., high impacts, fast swing legs, collisions with ...
- **p. 8 / Front matter - extractive PDF cue:** In what follows we describe each component in detail.
- **p. 11 / Front matter - extractive PDF cue:** Interestingly, removing velocities from the observation altogether led to a complete failure to train, even though in theory the policy network could infer velocities as ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (Front matter), p. 9 (Front matter), p. 1 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter), objective p. 2 (Front matter), p. 9 (Front matter), p. 9 (Front matter), p. 11 (Front matter), p. 11 (Front matter), p. 6 (Front matter), temporal p. 3 (Front matter), p. 8 (Front matter), p. 9 (Front matter), p. 8 (Front matter), p. 9 (Front matter), p. 1 (Front matter).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
