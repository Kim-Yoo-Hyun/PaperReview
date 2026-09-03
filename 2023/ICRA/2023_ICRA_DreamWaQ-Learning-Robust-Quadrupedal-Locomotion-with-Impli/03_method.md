# Method - DreamWaQ: Learning Robust Quadrupedal Locomotion with Implicit Terrain Imagination via Deep Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2301.10602; PDF retrieval source: https://arxiv.org/pdf/2301.10602. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 1 (I. INTRODUCTION), p. 3 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 1 (I. INTRODUCTION)): The shared encoder is trained to provide a robust body state and context estimation jointly. of only explicitly estimating the robot's state, we propose a context-aided estimator network (CENet) architecture ...

## Method Body Digest

- **p. 3 / II. DREAMWAQ - extractive body cue:** The shared encoder is trained to provide a robust body state and context estimation jointly. of only explicitly estimating the robot's state, we propose a ...
- **p. 2 / II. DREAMWAQ - extractive body cue:** 1) Policy Network: The policy, πφ(at/ot, vt, zt) is a neural network parameterized by φ that infers an action at, given a proprioceptive observation ot, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Conventional model-based controllers often require a complex pipeline consisting of state estimation, trajectory optimization, gait optimization, and actuator control [1]-[3], [7]-[11].
- **p. 3 / II. DREAMWAQ - extractive body cue:** CENet consists of a single encoder and a multi-head decoder architecture as shown in Fig.
- **p. 2 / II. DREAMWAQ - extractive body cue:** In DreamWaQ, the policy (actor) receives temporal partial observations, oH t , as the input, while the value network (critic) receives the full state, st, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we proposed a framework called Dream Walking for Quadrupedal Robots (DreamWaQ), that trains a robust locomotion policy for quadrupedal robots with ...
- **p. 4 / II. DREAMWAQ - extractive body cue:** The key idea is that bootstrapping is required when the CV of m agents' rewards is small to make the policy more robust against inaccurate ...
- **p. 3 / II. DREAMWAQ - extractive body cue:** However, this reward minimizes the overall power without considering each motor's power usage balance.

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we proposed a framework called Dream Walking for Quadrupedal Robots (DreamWaQ), that trains a robust locomotion policy for quadrupedal robots with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, the contributions of this work are threefold:
- **p. 2 / II. DREAMWAQ - extractive body cue:** The reward function consists of task rewards for tracking the

## Source Evidence Cues

- **p. 3 / II. DREAMWAQ - extractive body cue:** The shared encoder is trained to provide a robust body state and context estimation jointly. of only explicitly estimating the robot's state, we propose a ...
- **p. 2 / II. DREAMWAQ - extractive body cue:** 1) Policy Network: The policy, πφ(at/ot, vt, zt) is a neural network parameterized by φ that infers an action at, given a proprioceptive observation ot, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Conventional model-based controllers often require a complex pipeline consisting of state estimation, trajectory optimization, gait optimization, and actuator control [1]-[3], [7]-[11].
- **p. 3 / II. DREAMWAQ - extractive body cue:** CENet consists of a single encoder and a multi-head decoder architecture as shown in Fig.
- **p. 2 / II. DREAMWAQ - extractive body cue:** In DreamWaQ, the policy (actor) receives temporal partial observations, oH t , as the input, while the value network (critic) receives the full state, st, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we proposed a framework called Dream Walking for Quadrupedal Robots (DreamWaQ), that trains a robust locomotion policy for quadrupedal robots with ...
- **p. 4 / II. DREAMWAQ - extractive body cue:** The key idea is that bootstrapping is required when the CV of m agents' rewards is small to make the policy more robust against inaccurate ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | The shared encoder is trained to provide a robust body state and context estimation jointly. of only explicitly estimating the robot's state, ... | p. 3 (II. DREAMWAQ), p. 2 (II. DREAMWAQ) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | 1) Policy Network: The policy, πφ(at/ot, vt, zt) is a neural network parameterized by φ that infers an action at, given a ... | p. 2 (II. DREAMWAQ), p. 1 (I. INTRODUCTION) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | Conventional model-based controllers often require a complex pipeline consisting of state estimation, trajectory optimization, gait optimization, and actuator control [1]-[3], [7]-[11]. | p. 1 (I. INTRODUCTION), p. 3 (II. DREAMWAQ) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / II. DREAMWAQ - extractive body cue:** However, this reward minimizes the overall power without considering each motor's power usage balance.
- **p. 3 / II. DREAMWAQ - extractive body cue:** The complex reward function for learning a locomotion policy usually includes a motor power minimization term.
- **p. 2 / II. DREAMWAQ - extractive body cue:** The environment starts with an initial state distribution, d0(s0); progresses with a state transition probability p(st+1/st, at); and each transition is rewarded with a reward ...
- **p. 4 / II. DREAMWAQ - extractive body cue:** We define the bootstrapping probability for each learning iteration as follows: pboot = 1 -tanh(CV (R)), (8) where pboot ∈[0, 1] is the bootstrapping probability ...
- **p. 2 / II. DREAMWAQ - extractive body cue:** The reward function consists of task rewards for tracking the
- **p. 4 / II. DREAMWAQ - extractive body cue:** the standard deviation to the mean, of the episodic reward over m domain-randomized environments.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 3 (II. DREAMWAQ), p. 3 (II. DREAMWAQ).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Policy, Network, at/ot, neural, parameterized, infers, action, given, proprioceptive, observation, body, velocity, latent, state | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | Policy, Network, at/ot, neural, parameterized, infers, action, given, proprioceptive, observation | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | framework, called, Dream, Walking, Quadrupedal, Robots, DreamWaQ, trains, robust, locomotion | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | However, reward, minimizes, overall, power, without, considering, motor, usage, balance | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / II. DREAMWAQ - extractive body cue:** 1) Policy Network: The policy, πφ(at/ot, vt, zt) is a neural network parameterized by φ that infers an action at, given a proprioceptive observation ot, ...
- **p. 2 / II. DREAMWAQ - extractive body cue:** In DreamWaQ, the policy (actor) receives temporal partial observations, oH t , as the input, while the value network (critic) receives the full state, st, ...
- **p. 3 / II. DREAMWAQ - extractive body cue:** The total reward of the policy for taking an action at each state is given as: rt(st, at) = X riwi, (4) where i is ...
- **p. 3 / II. DREAMWAQ - extractive body cue:** Context-Aided Estimator Network The policy trained using the method described in Section II-B requires vt and zt as input, which can be estimated from proprioception.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Estimating the surrounding terrain's properties via proprioception while learning a locomotion policy requires an iterative process [19], [20], [23].
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recent works have shown that by combining different proprioception modalities, a quadrupedal robot can learn to estimate its surrounding terrain [19]-[23] and body state [24].
- **p. 4 / II. DREAMWAQ - extractive body cue:** The key idea is that bootstrapping is required when the CV of m agents' rewards is small to make the policy more robust against inaccurate ...
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | The robot's trajectory was measured using a real-time kinematic (RTK) GPS [39] with a frequency of 10 Hz, mounted on top of ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | Real-time experiment videos are available online1. | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | not recovered | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | The robot's trajectory was measured using a real-time kinematic (RTK) GPS [39] with a frequency of 10 Hz, mounted on top of ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / II. DREAMWAQ - extractive body cue:** The shared encoder is trained to provide a robust body state and context estimation jointly. of only explicitly estimating the robot's state, we propose a ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we proposed a framework called Dream Walking for Quadrupedal Robots (DreamWaQ), that trains a robust locomotion policy for quadrupedal robots with ...
- **p. 5 / III. EXPERIMENTS - extractive body cue:** We hypothesize that this is made possible by two factors: 1) the forward-backward dynamics learning provides more accurate estimation in all terrains, and 2) using ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** shared, encoder, trained, provide, robust, body, state, context, estimation, jointly, only, explicitly, estimating, robot, context-aided, estimator, network, CENet, architecture, learn.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | Real-World Experimental Setup Real-world experiments were conducted using a Unitree A1 [26] robot. | p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |
| Whole-body policy / controller | Compared Methods For a comparative evaluation, we compared the following algorithms with access to proprioceptions only: 1) Baseline [12]: The policy was ... | p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS) |
| Adaptation / recovery | Fig. 5: Estimation error of CENet and EstimatorNet. The superiority of CENet is highlighted when the robot's feet stumbled by stairs. barplot, ... | p. 5 (Figure/Table caption), p. 5 (III. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 4 / III. EXPERIMENTS - extractive body cue:** 4) DreamWaQ w/o AdaBoot: The proposed method without adaptive bootstrapping.
- **p. 4 / III. EXPERIMENTS - extractive body cue:** 3) EstimatorNet [24]: The policy was concurrently trained with an estimator network that explicitly estimates the body state without a context estimation.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** Moreover, the proposed AdaBoot method also increases robustness without sacrificing the base performance.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** Owing to the robust and accurate CENet, the robot had no problem in its body velocity estimation and could continue its journey without any performance ...
- **p. 6 / IV. CONCLUSION - extractive body cue:** DreamWaQ's limitation lies in its adaptation mechanism, where it must first hit the obstacles with its legs.
- **p. 5 / III. EXPERIMENTS - extractive body cue:** In severe cases, inaccurate estimation can lead to catastrophic failure.
- **p. 6 / III. EXPERIMENTS - extractive body cue:** (a) Foot stumble Foot slip Normal walk Normal walk Normal walk Climb upstairs Go downstairs Irregular foothold Adaptation Recovery (a) (b) Normal walk Fig.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 1 (I. INTRODUCTION), p. 3 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 1 (I. INTRODUCTION), objective p. 3 (II. DREAMWAQ), p. 3 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 4 (II. DREAMWAQ), p. 2 (II. DREAMWAQ), p. 4 (II. DREAMWAQ), temporal p. 5 (III. EXPERIMENTS), p. 6 (III. EXPERIMENTS), p. 4 (III. EXPERIMENTS), p. 4 (III. EXPERIMENTS), p. 5 (III. EXPERIMENTS), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
