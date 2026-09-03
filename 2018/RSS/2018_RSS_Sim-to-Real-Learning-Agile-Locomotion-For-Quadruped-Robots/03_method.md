# Method - Sim-to-Real: Learning Agile Locomotion For Quadruped Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss14/p10.html; PDF retrieval source: https://arxiv.org/pdf/1804.10332. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS)): Our problem is partially observable because certain states such as the position of the Minitaur's base and the foot contact forces are not accessible due to lack of corresponding sensors.

## Method Body Digest

- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** Our problem is partially observable because certain states such as the position of the Minitaur's base and the foot contact forces are not accessible due ...
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** We represent the feedback component π with a neural network and solve the above POMDP using Proximal Policy Optimization [5].
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** More importantly, a compact observation space helps to transfer the policy to the real robot.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** Policy Representation Although learning from scratch can eliminate the need of human expertise, and sometimes achieve better performance, having control of the learned policies is ...
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** Reinforcement learning optimizes a policy π : O 7→A that maximizes the expected return (accumulated rewards) R. π∗= arg maxπEs0∼D[Rπ(s0)] (1) B.
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** An MDP is a tuple (S, A, r, D, Psas′, γ), where S is the state space; A is the action space; r is the ...
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** During training, the rewards are accumulated at each episode.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** If we want a policy that is learned from scratch, we can set ¯a(t) = 0 and give the feedback component π(o) a wide output ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present a complete learning system for agile locomotion, in which control policies are learned in simulation and deployed on real robots.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that with deep RL, highly agile locomotion gaits can emerge automatically.

## Source Evidence Cues

- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** Our problem is partially observable because certain states such as the position of the Minitaur's base and the foot contact forces are not accessible due ...
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** We represent the feedback component π with a neural network and solve the above POMDP using Proximal Policy Optimization [5].
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** More importantly, a compact observation space helps to transfer the policy to the real robot.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** Policy Representation Although learning from scratch can eliminate the need of human expertise, and sometimes achieve better performance, having control of the learned policies is ...
- **Detected method headings:** IV. LEARNING LOCOMOTION CONTROLLERS (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Our problem is partially observable because certain states such as the position of the Minitaur's base and the foot contact forces are ... | p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | We represent the feedback component π with a neural network and solve the above POMDP using Proximal Policy Optimization [5]. | p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | More importantly, a compact observation space helps to transfer the policy to the real robot. | p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** Reinforcement learning optimizes a policy π : O 7→A that maximizes the expected return (accumulated rewards) R. π∗= arg maxπEs0∼D[Rπ(s0)] (1) B.
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** An MDP is a tuple (S, A, r, D, Psas′, γ), where S is the state space; A is the action space; r is the ...
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** During training, the rewards are accumulated at each episode.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** We represent the feedback component π with a neural network and solve the above POMDP using Proximal Policy Optimization [5].
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | want, policy, learned, scratch, give, feedback, component, wide, output, range, reason, decouple, locomotion, controller | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | want, policy, learned, scratch, give, feedback, component, wide, output, range | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | main, contributions, complete, learning, system, agile, locomotion, present, control, policies | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | Reinforcement, learning, optimizes, policy, maximizes, expected, return, accumulated, rewards, Es0 | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** If we want a policy that is learned from scratch, we can set ¯a(t) = 0 and give the feedback component π(o) a wide output ...
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** For this reason, we decouple the locomotion controller into two parts, an open loop component that allows a user to provide reference trajectories and a ...
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** More importantly, a compact observation space helps to transfer the policy to the real robot.
- **p. 3 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** At every control step, a partial observation o ∈O, rather than a complete state s ∈S, is observed.
- **p. 2 / I. INTRODUCTION - extractive body cue:** perturbation forces, and compact design of observation space.
- **p. 1 / I. INTRODUCTION - extractive body cue:** While learning from scratch can lead to better policies than incorporating human guidance [10], in robotics, having control of the learned policy sometimes is preferred.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recently, we have seen tremendous progress in deep reinforcement learning (deep RL) [4, 5, 6].
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | To model latency, we keep a history of observations and their measurement time {(ti, Oi)i=0,1,...,n-1}, where ti = i∆t and ∆t is ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | To measure the latency on the physical system, we send a spike of PWM signal that lasts for one time step, which ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | To model latency, we keep a history of observations and their measurement time {(ti, Oi)i=0,1,...,n-1}, where ti = i∆t and ∆t is ... | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | An episode terminates after 1000 steps or when the simulated Minitaur loses balance: its base tilts more than 0.5 radians. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** We repeated the training with different hyperparameters and random seeds, and found that the majority of the solutions converged to galloping.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** problem, partially, observable, because, certain, states, position, Minitaur, base, foot, contact, forces, accessible, lack, corresponding, sensors, represent, feedback, component, neural.
- **Relevant PDF headings:** IV. LEARNING LOCOMOTION CONTROLLERS (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | This time, we observed stable, comparable movements in both simulation and on the real robot. | p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION) |
| Whole-body policy / controller | We compared the learned gaits with the handcrafted ones from Ghost Robotics [3]. | p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption) |
| Adaptation / recovery | After we improved the simulation (Section V-A), an agile galloping gait emerged automatically. | p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION) |

## Failure and Ablation Link

- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** The controllers worked directly in the real world without additional fine tuning on the physical system.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found that ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 9: Comparison of controllers trained with different obser- vation spaces and randomization. The blue and red bars are the performance in simulation and in ...
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** Locomotion Tasks In the first experiment, we let the system learn from scratch: We set the open loop component ¯a(t) = 0 and gave the ...
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot.
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** Note that while this open loop controller expresses the user's preference of the locomotion style, by itself, it cannot produce any forward movement in the ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The simulated and the real Minitaurs learned to gallop using deep reinforcement learning. to locomotion tasks due to the difficulties of automatically resetting ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), objective p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), temporal p. 5 (V. NARROWING THE REALITY GAP), p. 5 (V. NARROWING THE REALITY GAP), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (V. NARROWING THE REALITY GAP), p. 4 (V. NARROWING THE REALITY GAP), p. 6 (VI. EVALUATION AND DISCUSSION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Our problem is partially observable because certain states such as the position of the Minitaur's base and the foot contact forces are not accessible due to lack of corresponding sensors. (p. 3, IV. LEARNING LOCOMOTION CONTROLLERS).
- **Objective/update evidence:** Reinforcement learning optimizes a policy π : O 7→A that maximizes the expected return (accumulated rewards) R. π∗= arg maxπEs0∼D[Rπ(s0)] (1) B. (p. 3, IV. LEARNING LOCOMOTION CONTROLLERS).
- **Temporal/runtime evidence:** To model latency, we keep a history of observations and their measurement time {(ti, Oi)i=0,1,...,n-1}, where ti = i∆t and ∆t is the time step. (p. 5, V. NARROWING THE REALITY GAP).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
