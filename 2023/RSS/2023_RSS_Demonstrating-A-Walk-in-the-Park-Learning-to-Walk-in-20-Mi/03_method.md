# Method - Demonstrating A Walk in the Park: Learning to Walk in 20 Minutes With Model-Free Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss19/p056.html; PDF retrieval source: https://arxiv.org/pdf/2208.07860. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL)): Our choice of algorithm and implementation is aimed at enabling real-time synchronous training, which we expand on in Section V.

## Method Body Digest

- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Our choice of algorithm and implementation is aimed at enabling real-time synchronous training, which we expand on in Section V.
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Actor-critic methods have recently become significantly more sample-efficient by improving the training of the critic, thereby allowing more updates to the critic network for the ...
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** These algorithms use up to 20 times the number of critic updates to speed up learning with respect to the number of samples collected, but ...
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** What all of these works have in common is that they add some sort of regularization or normalization method (or both) to mitigate the tendency ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Reinforcement learning offers a promising alternative, acquiring effective control strategies directly through interaction with the real system, potentially right in the environment in which the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Experimental Design Training Statistics Simulation Real World Hardware Actions Resets Terrains Samples Hours Samples Hours Ours A1 PD targets Learned In/Outdoor 0 0 20 · ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** [29] Minitaur PMTG [26] parameters Unknown Indoor 0 0 45 · 103 0.16 Table I: Overview of experimental details (hardware platform used, the kinds of ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although large-scale robotic reinforcement learning experiments in the real world have been described in a number of prior works [1]-[5], many other researchers have sought ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our main contribution is an empirical demonstration that current deep RL methods can effectively learn quadrupedal locomotion directly in the real world in under 20 ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Crucially, this does not require novel algorithmic components or any other unexpected innovation, but rather careful implementation of one of several existing algorithmic frameworks (and ...
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** DroQ [60] similarly allows for a higher update to data ratio by regularizing the critic networks with dropout [61] and layer normalization [65].

## Source Evidence Cues

- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Our choice of algorithm and implementation is aimed at enabling real-time synchronous training, which we expand on in Section V.
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Actor-critic methods have recently become significantly more sample-efficient by improving the training of the critic, thereby allowing more updates to the critic network for the ...
- **Detected method headings:** B. Efficient Model-Free RL (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Our choice of algorithm and implementation is aimed at enabling real-time synchronous training, which we expand on in Section V. | p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | Actor-critic methods have recently become significantly more sample-efficient by improving the training of the critic, thereby allowing more updates to the critic ... | p. 4 (B. Efficient Model-Free RL) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | Our choice of algorithm and implementation is aimed at enabling real-time synchronous training, which we expand on in Section V. | p. 4 (B. Efficient Model-Free RL) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** These algorithms use up to 20 times the number of critic updates to speed up learning with respect to the number of samples collected, but ...
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** What all of these works have in common is that they add some sort of regularization or normalization method (or both) to mitigate the tendency ...
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Reinforcement, learning, offers, promising, alternative, acquiring, effective, control, strategies, directly, through, interaction, real, system | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | Reinforcement, learning, offers, promising, alternative, acquiring, effective, control, strategies, directly | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | main, contribution, empirical, demonstration, current, deep, methods, effectively, learn, quadrupedal | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | algorithms, times, number, critic, updates, speed, learning, respect, samples, collected | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / I. INTRODUCTION - extractive body cue:** Reinforcement learning offers a promising alternative, acquiring effective control strategies directly through interaction with the real system, potentially right in the environment in which the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Experimental Design Training Statistics Simulation Real World Hardware Actions Resets Terrains Samples Hours Samples Hours Ours A1 PD targets Learned In/Outdoor 0 0 20 · ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** [29] Minitaur PMTG [26] parameters Unknown Indoor 0 0 45 · 103 0.16 Table I: Overview of experimental details (hardware platform used, the kinds of ...
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** What all of these works have in common is that they add some sort of regularization or normalization method (or both) to mitigate the tendency ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Although large-scale robotic reinforcement learning experiments in the real world have been described in a number of prior works [1]-[5], many other researchers have sought ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | Standard SAC (purple) with an update-to-data (UTD) ratio of 1 takes one gradient step on the critic for every one time step ... | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | In contrast, for a baseline comparison, our best PyTorch implementation was not fast enough for synchronous training, only permitting an effective control ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Our choice of algorithm and implementation is aimed at enabling real-time synchronous training, which we expand on in Section V.
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Actor-critic methods have recently become significantly more sample-efficient by improving the training of the critic, thereby allowing more updates to the critic network for the ...
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Because of this, a na¨ıve implementation cannot train as fast as the samples are collected.
- **p. 4 / B. Efficient Model-Free RL - extractive body cue:** Prior work has addressed this either by performing asynchronous training [23], [28] or training in-between trials [24].
- **p. 5 / V. SIMULATION ANALYSIS - extractive body cue:** Since our goal is to run training on a real robot, we aim for design decisions and algorithms that lead to improved stability and sample ...
- **p. 6 / V. SIMULATION ANALYSIS - extractive body cue:** In order to facilitate this kind of training synchronously, the updates must be inexpensive enough to be able to perform them between time-steps (of which ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** choice, algorithm, implementation, aimed, enabling, real-time, synchronous, training, expand, Section, Actor-critic, methods, have, recently, become, significantly, more, sample-efficient, improving, critic.
- **Relevant PDF headings:** B. Efficient Model-Free RL (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various ... | p. 5 (V. SIMULATION ANALYSIS), p. 6 (V. SIMULATION ANALYSIS) |
| Whole-body policy / controller | Therefore, for the remaining ablations, we used the value of damping set to 10. | p. 5 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS) |
| Adaptation / recovery | From these results, we can conclude that a variety of regularization or normalization methods, if implemented and applied carefully, can all achieve ... | p. 6 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS) |

## Failure and Ablation Link

- **p. 5 / V. SIMULATION ANALYSIS - extractive body cue:** 3: Experimental evaluation of (a) performance for different value of the damping parameter for the position PD controller; (b) ablations of various task setup choices; ...
- **p. 5 / V. SIMULATION ANALYSIS - extractive body cue:** In particular, we confirm the efficacy of constraining the action space: we observe that the simulated agent cannot make any progress in the unconstrained action ...
- **p. 6 / V. SIMULATION ANALYSIS - extractive body cue:** As such, we favor using the less computationally expensive DroQ variants over others in the real world.
- **p. 6 / V. SIMULATION ANALYSIS - extractive body cue:** Left to right: flat, solid ground covered in dense foam mats; a 5cm memory foam mattress; loose ground comprised of eucalyptus bark; a grassy lawn; ...
- **p. 4 / IV. SYSTEM DESIGN - extractive body cue:** In the simulator, we used p = [0.05, 0.7, -1.4]; however, during the early experiments in the real world, we found that p = [0.05, ...
- **p. 4 / IV. SYSTEM DESIGN - extractive body cue:** As such, such policies cannot trivially be further trained in the real world.
- **p. 5 / IV. SYSTEM DESIGN - extractive body cue:** During early experiments with the real robot, we found that using the forward velocity in the robot's local frame caused it to dive forward as ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL), objective p. 4 (B. Efficient Model-Free RL), p. 4 (B. Efficient Model-Free RL), temporal p. 5 (V. SIMULATION ANALYSIS), p. 5 (V. SIMULATION ANALYSIS), p. 3 (III. FAST AND SIMPLE RL FOR REAL-WORLD ROBOTS), p. 6 (VI. LEARNING IN THE REAL WORLD), p. 6 (VI. LEARNING IN THE REAL WORLD), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
