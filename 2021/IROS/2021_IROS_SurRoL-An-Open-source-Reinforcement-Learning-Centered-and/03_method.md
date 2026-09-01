# Method - SurRoL: An Open-source Reinforcement Learning Centered and dVRK Compatible Platform for Surgical Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/9635867; PDF retrieval source: https://arxiv.org/pdf/2108.13035. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (III. METHODS), p. 2 (III. METHODS)): Finally, ten surgical learning-based tasks are built for algorithm development and evaluation.

## Method Body Digest

- **p. 2 / III. METHODS - extractive PDF cue:** Finally, ten surgical learning-based tasks are built for algorithm development and evaluation.
- **p. 2 / III. METHODS - extractive PDF cue:** SurRoL builds on top of the open-source PyBullet because of its state-of-the-art physics simulation, wide adoption in the machine learning community, and removal of the ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** SurRoL provides dVRK compatible simulation environments for surgical robot learning (left), with Gym-like interfaces for reinforcement learning algorithm development and ranges of surgical contents with ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Moreover, the physical interactions supported by the current learning-based simulators are simplified.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Further, the designed SurRoL with carefully modeled assets can successfully deal with more realistic physical interactions.
- **p. 2 / III. METHODS - extractive PDF cue:** Finally, ten surgical learning-based tasks are built for algorithm development and evaluation.

## Source Evidence Cues

- **p. 2 / III. METHODS - extractive PDF cue:** Finally, ten surgical learning-based tasks are built for algorithm development and evaluation.
- **p. 2 / III. METHODS - extractive PDF cue:** SurRoL builds on top of the open-source PyBullet because of its state-of-the-art physics simulation, wide adoption in the machine learning community, and removal of the ...
- **Detected method headings:** III. METHODS (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Data schema / normalization | heterogeneous robot trajectory를 공통 sample로 만든다 | observation, action, task와 embodiment metadata | sensor/action schema alignment, filtering, normalization을 수행 | shared dataset representation | Finally, ten surgical learning-based tasks are built for algorithm development and evaluation. | p. 2 (III. METHODS), p. 2 (III. METHODS) |
| Coverage / augmentation | task·embodiment·failure variation을 확장한다 | dataset과 metadata | retargeting, relabeling, synthetic/teleoperation augmentation 또는 sampling을 적용 | expanded data support | SurRoL builds on top of the open-source PyBullet because of its state-of-the-art physics simulation, wide adoption in the machine learning community, and ... | p. 2 (III. METHODS) |
| Downstream learning interface | 정규화된 data를 policy/representation이 사용한다 | shared observations/actions | pretraining, BC, action-token 또는 representation learning을 수행 | checkpoint/policy action | Finally, ten surgical learning-based tasks are built for algorithm development and evaluation. | p. 2 (III. METHODS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** trajectory D with task/embodiment metadata -> normalized sample or downstream action -> coverage/data efficiency/transfer objective -> cross-domain transfer and task performance.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | SurRoL, builds, open-source, PyBullet, because, state-of-the-art, physics, simulation, wide, adoption, machine, learning, community, removal | multi-view observation, language/task label과 action trajectory | body cue; exact tensor/frame verify |
| State/latent | SurRoL, builds, open-source, PyBullet, because, state-of-the-art, physics, simulation, wide, adoption | shared representation, embodiment/task identity와 data distribution | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, design, open-source, surgical, robot, learning, simulation | dataset sample 또는 learned policy action | body cue; unit/decoder verify |
| Objective/constraint | not recovered | coverage/data efficiency/transfer objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. METHODS - extractive PDF cue:** SurRoL builds on top of the open-source PyBullet because of its state-of-the-art physics simulation, wide adoption in the machine learning community, and removal of the ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Our main contributions are summarized as follows: • We design an open-source surgical robot learning simulation platform centered on reinforcement learning for surgical skills, which ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** SurRoL provides dVRK compatible simulation environments for surgical robot learning (left), with Gym-like interfaces for reinforcement learning algorithm development and ranges of surgical contents with ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Moreover, the physical interactions supported by the current learning-based simulators are simplified.
- **Normalized interface:** observation=multi-view observation, language/task label과 action trajectory; state=shared representation, embodiment/task identity와 data distribution; output/action=dataset sample 또는 learned policy action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | trajectory demonstration horizon; training sample window와 deployment task horizon을 분리한다. | Each episode lasts for 50 timesteps for goalbased tasks and 500 timesteps for reward-based tasks. | episode/sequence/action-chunk boundary |
| Rate / latency | data recording/action sampling rate와 policy inference/control rate를 분리한다. | 2) Profiling Analysis: Our SurRoL can run at a real-time rate, at about 150Hz simulation in the reaching tasks with position control ... | Hz/fps, inference time and control rate |
| Memory | trajectory, embodiment/task metadata와 dataset index. | not recovered | window and reset |
| Compute | data decoding, normalization/augmentation과 downstream training budget이 결정한다. | 2) Profiling Analysis: Our SurRoL can run at a real-time rate, at about 150Hz simulation in the reaching tasks with position control ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** Most of the training and testing experiments are performed on a desktop with Ubuntu 18.04, Inter 3.6GHz CPU with 32GB RAM, and an Nvidia TITAN ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** After combining HER and demonstration (HER+DEMO) with Q-filtered behavior cloning [35], the agents manage to solve many challenging tasks with physicsrich simulation within 50 epochs ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Finally, surgical, learning-based, tasks, built, algorithm, development, evaluation, SurRoL, builds, open-source, PyBullet, because, state-of-the-art, physics, simulation, wide, adoption, machine, learning.
- **Relevant PDF headings:** III. METHODS (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Data schema / normalization | 1) Experiment Setup: In our RL environments, we set up the manipulation workspace for robots and objects to interact within. | p. 5 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Coverage / augmentation | 4) Evaluation Results: A summary of the evaluation results for RL baselines is shown in Fig. | p. 5 (IV. EXPERIMENTS), p. 3 (Figure/Table caption) |
| Downstream learning interface | By contrast, the policy trained in the Interact manner with improved physics simulation is more robust to environment changes with a high ... | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** We also observe that in StaticTrack, the learned policy can smoothly center the target object without the jittering effect, which is non-trivial for the visual ...
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** For ECM goalbased tasks without instrument-object physical interaction, the agent can successfully capture the complicated actionobservation relationship using HER, even for MisOrient and StaticTrack, which ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Epoch 30 40 50 10 20 0.0 0.2 0.4 0.6 0.8 1.0 Success Rate BiPegTransfer with Variants (1) Approach (2) Pick (3) Lift (4) Handover ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** We further analyze the most challenging long-range BiPegTransfer failed even with imitation learning by constructing several variants with different levels of simplification.
- **p. 5 / IV. EXPERIMENTS - extractive PDF cue:** By visually inspecting the training progress, we find that the agents can quickly learn to approach the object such as the needle and attempt to ...
- **p. 6 / IV. EXPERIMENTS - extractive PDF cue:** Meanwhile, the needle picking point is restricted to the jaw tip to avoid unsafe jaw collisions with the holding surface.
- **p. 7 / IV. EXPERIMENTS - extractive PDF cue:** Besides, we find some failure cases resulting from dynamics discrepancies between the simulation and the real world, also observed in [14].

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (III. METHODS), p. 2 (III. METHODS), objective 본문 anchor 없음, temporal p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 3 (A. SurRoL RL Library), p. 6 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
