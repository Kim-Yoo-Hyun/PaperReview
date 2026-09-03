# Method - Blind Bipedal Stair Traversal via Sim-to-Real Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss17/p061.html; PDF retrieval source: https://www.roboticsproceedings.org/rss17/p061.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION)): For sim-to-real training of the policy, we use Proximal Policy Optimization (PPO) [20], a model-free deep RL algorithm.

## Method Body Digest

- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** For sim-to-real training of the policy, we use Proximal Policy Optimization (PPO) [20], a model-free deep RL algorithm.
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Training is done completely in a simulation environment, with dynamics randomization (see below), and the resulting policy is then used in the realworld.
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Action Space The output action at of the control policy at each time step (running at 40Hz) is an 11 dimensional vector with the first ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Specifically, we use a KL-threshold-termination variant, wherein each time the policy is updated, the KL divergence between the updated policy and the former policy is ...
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** The RL optimization objective considered in this work is to learn a policy through interaction with the environment that maximizes the expected cumulative discounted reward ...
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** That is, find a policy π that maximizes: J(π) = E  ∑T t=0 γtRt  , where γ ∈[0,1] is the discount factor and ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** We add additional cost terms on top of these foundational reward terms, including a cost incentivizing the policy to match a translational velocity and orientation.
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** For a detailed explanation of the reward function used, see the Appendix.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** We present a training pipeline which produces policies capable of blindly ascending and descending stairs in the real world.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In this work, we show that robust proprioceptive bipedal control for complex stair-like terrain can be learned via an existing RL framework with surprisingly little ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These policies learn proprioceptive reflexes to reject significant disturbances in ground height, resulting in highly robust behavior to many realworld environments. start location or the ...

## Source Evidence Cues

- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** For sim-to-real training of the policy, we use Proximal Policy Optimization (PPO) [20], a model-free deep RL algorithm.
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Training is done completely in a simulation environment, with dynamics randomization (see below), and the resulting policy is then used in the realworld.
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Action Space The output action at of the control policy at each time step (running at 40Hz) is an 11 dimensional vector with the first ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Specifically, we use a KL-threshold-termination variant, wherein each time the policy is updated, the KL divergence between the updated policy and the former policy is ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | For sim-to-real training of the policy, we use Proximal Policy Optimization (PPO) [20], a model-free deep RL algorithm. | p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Training is done completely in a simulation environment, with dynamics randomization (see below), and the resulting policy is then used in the ... | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | Action Space The output action at of the control policy at each time step (running at 40Hz) is an 11 dimensional vector ... | p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** The RL optimization objective considered in this work is to learn a policy through interaction with the environment that maximizes the expected cumulative discounted reward ...
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** That is, find a policy π that maximizes: J(π) = E  ∑T t=0 γtRt  , where γ ∈[0,1] is the discount factor and ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** We add additional cost terms on top of these foundational reward terms, including a cost incentivizing the policy to match a translational velocity and orientation.
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** For a detailed explanation of the reward function used, see the Appendix.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | State, Space, input, control, policy, time, step, includes, three, main, components, general, setting, discrete | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | State, Space, input, control, policy, time, step, includes, three, main | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | present, training, pipeline, produces, policies, capable, blindly, ascending, descending, stairs | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | optimization, objective, considered, learn, policy, through, interaction, environment, maximizes, expected | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** State Space The state st that is input to the control policy at each time step includes three main components.
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** In the general RL setting, at each discrete time step t the robot control policy π receives the current state st and returns an action ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** While this component is included in the control policy action, it does not appear to have a large impact on performance and the learned policy ...
- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** We add additional cost terms on top of these foundational reward terms, including a cost incentivizing the policy to match a translational velocity and orientation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This goal is not compatible with a complete reliance on exteroceptive sensors such as RGB and depth cameras for accurate terrain estimation, which introduce fragility ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Further, integrating a state-ofthe-art computer vision system into a high-speed controller is technically difficult, especially on a computationally limited platform like a mobile robot.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Damping, mass, friction, and encoder offset are randomized at the beginning of each rollout, while execution rate is randomized at each timestep ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | Given that maximum episode length is 300 discrete timesteps, this means each command will change at least once on average per episode. | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | The starting position of the stairs are randomized at the beginning of each rollout, such that the episode can start with the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** For sim-to-real training of the policy, we use Proximal Policy Optimization (PPO) [20], a model-free deep RL algorithm.
- **p. 2 / II. REINFORCEMENT LEARNING FORMULATION - extractive body cue:** Training is done completely in a simulation environment, with dynamics randomization (see below), and the resulting policy is then used in the realworld.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** sim-to-real, training, policy, Proximal, Optimization, PPO, model-free, deep, algorithm, done, completely, simulation, environment, dynamics, randomization, below, resulting, then, realworld, Action.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Each policy was trained until 300 million timesteps were sampled from the virtual environment, simulated with MuJoCo [22]. | p. 4 (IV. RESULTS), p. 4 (Figure/Table caption) |
| Whole-body policy / controller | We also trained a group of policies without stair terrain randomization, and denote these Flat Ground LSTM, to investigate the importance of ... | p. 4 (IV. RESULTS), p. 5 (Figure/Table caption) |
| Adaptation / recovery | Fig. 3: The learned policies exhibit a high degree of blind robustness to a variety of stair-like terrain, and can reliably ascend ... | p. 4 (Figure/Table caption), p. 5 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and 1.5 ...
- **p. 4 / IV. RESULTS - extractive body cue:** We also trained a group of policies without stair terrain randomization, and denote these Flat Ground LSTM, to investigate the importance of the terrain randomization ...
- **p. 7 / V. CONCLUSION - extractive body cue:** In future work, it will be interesting to investigate how vision can be most effectively used to improve the efficiency and/or performance of a blind ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: We evaluate the probability of successfully climbing and descending stairs without falling as a function of commanded speed between 0.25 m/s and 1.5 ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: In this work, we investigate the limits of blind bipedal locomo- tion. We present a training pipeline which produces policies capable of blindly ...
- **p. 7 / V. CONCLUSION - extractive body cue:** In this work, we have motivated the desirability of a highly robust but blind walking controller, and demonstrated that such a blind bipedal walking controller ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: In order to ensure robustness over a variety of possible stair- like terrain, we randomize a number of parameters when generating stairs at ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), objective p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), temporal p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 3 (II. REINFORCEMENT LEARNING FORMULATION), p. 2 (II. REINFORCEMENT LEARNING FORMULATION), p. 4 (IV. RESULTS), p. 4 (III. TERRAIN RANDOMIZATION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
