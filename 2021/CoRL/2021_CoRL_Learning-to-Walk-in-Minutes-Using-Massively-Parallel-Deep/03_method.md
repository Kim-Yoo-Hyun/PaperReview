# Method - Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v164/rudin22a.html; PDF retrieval source: https://proceedings.mlr.press/v164/rudin22a/rudin22a.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), p. 6 (1 Introduction)): Each step consists of policy inference, simulation, reward, and observation calculation.

## Method Body Digest

- **p. 2 / 1 Introduction - extractive body cue:** Each step consists of policy inference, simulation, reward, and observation calculation.
- **p. 3 / 1 Introduction - extractive body cue:** Since we increase nrobots by a few orders of magnitude, we must choose a small nsteps to keep B reasonable and hence optimize training times, ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we use NVIDIA's Isaac Gym simulation environment [8], which runs both the simulation and training on the GPU and is capable of ...
- **p. 1 / Abstract - extractive body cue:** We analyze and discuss the impact of different training algorithm components in the massively parallel regime on the final policy performance and training times.
- **p. 3 / 1 Introduction - extractive body cue:** We use mini-batches of tens of thousands of samples and observe that it stabilizes the learning process without increasing the total training time.
- **p. 6 / 1 Introduction - extractive body cue:** For this reason and following the methodology of previous work [1], we use a neural network to compute torques from joint position commands.
- **p. 5 / 1 Introduction - extractive body cue:** 3.2 Observations, Actions, and Rewards The policy receives proprioceptive measurements of the robot as well as terrain information around the robot's base.
- **p. 4 / 1 Introduction - extractive body cue:** In supplementary material, we show the effect of this solution on the total reward as well as the critic loss.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** Additionally, we present a novel game-inspired curriculum which automatically adapts the task difficulty to the performance of the policy.
- **p. 2 / 1 Introduction - extractive body cue:** Each step consists of policy inference, simulation, reward, and observation calculation.
- **p. 1 / Abstract - extractive body cue:** In addition, we present a novel game-inspired curriculum that is well suited for training with thousands of simulated robots in parallel.

## Source Evidence Cues

- **p. 2 / 1 Introduction - extractive body cue:** Each step consists of policy inference, simulation, reward, and observation calculation.
- **p. 3 / 1 Introduction - extractive body cue:** Since we increase nrobots by a few orders of magnitude, we must choose a small nsteps to keep B reasonable and hence optimize training times, ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we use NVIDIA's Isaac Gym simulation environment [8], which runs both the simulation and training on the GPU and is capable of ...
- **p. 1 / Abstract - extractive body cue:** We analyze and discuss the impact of different training algorithm components in the massively parallel regime on the final policy performance and training times.
- **p. 3 / 1 Introduction - extractive body cue:** We use mini-batches of tens of thousands of samples and observe that it stabilizes the learning process without increasing the total training time.
- **p. 6 / 1 Introduction - extractive body cue:** For this reason and following the methodology of previous work [1], we use a neural network to compute torques from joint position commands.
- **p. 5 / 1 Introduction - extractive body cue:** 3.2 Observations, Actions, and Rewards The policy receives proprioceptive measurements of the robot as well as terrain information around the robot's base.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Each step consists of policy inference, simulation, reward, and observation calculation. | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Since we increase nrobots by a few orders of magnitude, we must choose a small nsteps to keep B reasonable and hence ... | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | In this work, we use NVIDIA's Isaac Gym simulation environment [8], which runs both the simulation and training on the GPU and ... | p. 2 (1 Introduction), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 1 Introduction - extractive body cue:** In supplementary material, we show the effect of this solution on the total reward as well as the critic loss.
- **p. 3 / 1 Introduction - extractive body cue:** This can be explained by the fact that we use Generalized Advantage Estimation (GAE) [23], which requires rewards from multiple time steps to be effective.
- **p. 2 / 1 Introduction - extractive body cue:** Each step consists of policy inference, simulation, reward, and observation calculation.
- **p. 2 / 1 Introduction - extractive body cue:** The parallelization was achieved by averaging the gradients between the different workers without reducing the number of samples provided by each agent.
- **p. 3 / 1 Introduction - extractive body cue:** With too little data, the gradients will be too noisy, and the algorithm will not learn effectively.
- **p. 4 / 1 Introduction - extractive body cue:** (d) Randomized, discrete obstacles with heights of up to ±0.2 m. the two termination modes and augment the reward with the expected infinite sum of ...
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | observations, composed, base, linear, angular, velocities, measurement, gravity, vector, joint, positions, previous, actions, selected | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | observations, composed, base, linear, angular, velocities, measurement, gravity, vector, joint | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | Additionally, present, novel, game-inspired, curriculum, automatically, adapts, task, difficulty, performance | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | supplementary, material, effect, solution, total, reward, well, critic, loss, explained | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 1 Introduction - extractive body cue:** The observations are composed of: base linear and angular velocities, measurement of the gravity vector, joint positions and velocities, the previous actions selected by the ...
- **p. 5 / 1 Introduction - extractive body cue:** 3.2 Observations, Actions, and Rewards The policy receives proprioceptive measurements of the robot as well as terrain information around the robot's base.
- **p. 2 / 1 Introduction - extractive body cue:** Each step consists of policy inference, simulation, reward, and observation calculation.
- **p. 2 / 1 Introduction - extractive body cue:** Current popular pipelines have the simulation and reward/observation calculation computed on the CPU, making the GPU unsuitable for policy inference because of communication bottle-necks.
- **p. 3 / 1 Introduction - extractive body cue:** Since we increase nrobots by a few orders of magnitude, we must choose a small nsteps to keep B reasonable and hence optimize training times, ...
- **p. 1 / 1 Introduction - extractive body cue:** The amount of data required to train a policy increases with the task complexity.
- **p. 1 / 1 Introduction - extractive body cue:** For example, OpenAI's block reorientation task was trained for up to 14 days and their Rubik's cube solving policy took several months to train [4].
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | This can be explained by the fact that we use Generalized Advantage Estimation (GAE) [23], which requires rewards from multiple time steps ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | Instead of concatenating past measurements at fixed time steps and sending all of that information to a standard feed-forward network, we only ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | It is important to distinguish nsteps from the maximum episode length leading to a time-out and a reset, which we define as ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1 Introduction - extractive body cue:** Each step consists of policy inference, simulation, reward, and observation calculation.
- **p. 3 / 1 Introduction - extractive body cue:** Since we increase nrobots by a few orders of magnitude, we must choose a small nsteps to keep B reasonable and hence optimize training times, ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we use NVIDIA's Isaac Gym simulation environment [8], which runs both the simulation and training on the GPU and is capable of ...
- **p. 1 / Abstract - extractive body cue:** We analyze and discuss the impact of different training algorithm components in the massively parallel regime on the final policy performance and training times.
- **p. 3 / 1 Introduction - extractive body cue:** We use mini-batches of tens of thousands of samples and observe that it stabilizes the learning process without increasing the total training time.
- **p. 2 / 1 Introduction - extractive body cue:** Current popular pipelines have the simulation and reward/observation calculation computed on the CPU, making the GPU unsuitable for policy inference because of communication bottle-necks.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** step, consists, policy, inference, simulation, reward, observation, calculation, Since, increase, nrobots, orders, magnitude, must, choose, small, nsteps, keep, reasonable, hence.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | As such, we simplify the task by reducing the maximum step size of stairs and obstacles and directly train robots on the ... | p. 6 (4 Results), p. 6 (4 Results) |
| Whole-body policy / controller | We begin by setting a baseline with nrobots = 20000 and nsteps = 50, resulting in a batch size of 1M samples. | p. 6 (4 Results), p. 6 (4 Results) |
| Adaptation / recovery | (b) Success rate for climbing and descending sloped terrains. | p. 7 (4 Results), p. 7 (4 Results) |

## Failure and Ablation Link

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 7: Locomotion policy, trained in under 20min, deployed on the physical robot. weight, and the ANYmal B robot, which has comparable dimensions but modified ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: 4000 robots progressing through the terrains with automatic curriculum, after 500 (top) and 1000 (bottom) policy updates. The robots start the training session ...
- **p. 6 / 4 Results - extractive body cue:** In order to use the total reward as a single representative metric, we have to remove the curriculum, otherwise a more performant policy sees its ...
- **p. 7 / 4 Results - extractive body cue:** As such, we can conclude that increasing the number of robots is beneficial for both final performance and training time, but there is an upper ...
- **p. 8 / 5 Conclusion - extractive body cue:** The purpose of this work is not to obtain the absolute best-performing policy with the highest robustness.
- **p. 8 / 4 Results - extractive body cue:** As part of future work, we plan to merge the two approaches.
- **p. 7 / 4 Results - extractive body cue:** To that end, we perform robustness and traversability tests.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 3 (1 Introduction), p. 6 (1 Introduction), objective p. 4 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), temporal p. 3 (1 Introduction), p. 6 (1 Introduction), p. 7 (4 Results), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
