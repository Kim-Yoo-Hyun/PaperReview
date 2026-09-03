# Method - Learning Memory-Based Control for Human-Scale Bipedal Locomotion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss16/p031.html; PDF retrieval source: https://www.roboticsproceedings.org/rss16/p031.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD)): Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end for During training, we used ...

## Method Body Digest

- **p. 4 / III. METHOD - extractive body cue:** Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end ...
- **p. 3 / III. METHOD - extractive body cue:** State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed ...
- **p. 4 / III. METHOD - extractive body cue:** Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm.
- **p. 3 / III. METHOD - extractive body cue:** Reward Design Our learning process makes use of a reference trajectory produced by an expert walking controller to help the policy learn in the initial ...
- **p. 3 / III. METHOD - extractive body cue:** All policies were trained to maximize the following reward function: R =0.20 · exp(-qerr) +0.20 · exp(-˙xerr) +0.05 · exp(-xerr) +0.20 · exp(-˙yerr) +0.30 · ...
- **p. 3 / III. METHOD - extractive body cue:** It is important to note that while the reward function is partially based on a reference motion, very similarly to Xie et al.
- **p. 4 / III. METHOD - extractive body cue:** However, correctly calculating the gradient of an RNN requires the use of the backpropagation through time (BPTT) algorithm, which necessitates special measures when sampling from ...
- **p. 4 / III. METHOD - extractive body cue:** The recurrent critic was also an LSTM network with two layers of 128 units each, with a single output representing the value function.

## Design Rationale

- **p. 3 / III. METHOD - extractive body cue:** State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** One of the main contributions of our work is to demonstrate that this approach is highly effective for training RNN controllers for the Cassie biped.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that by randomizing a small number of dynamics parameters over reasonable ranges, the RNNs can be consistently trained in simulation and successfully transferred ...

## Source Evidence Cues

- **p. 4 / III. METHOD - extractive body cue:** Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end ...
- **p. 3 / III. METHOD - extractive body cue:** State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed ...
- **p. 4 / III. METHOD - extractive body cue:** Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm.
- **p. 3 / III. METHOD - extractive body cue:** Reward Design Our learning process makes use of a reference trajectory produced by an expert walking controller to help the policy learn in the initial ...
- **Detected method headings:** III. METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Command / terrain state | body state와 terrain/task context를 표현한다 | proprioception, terrain/perception, velocity command | history encoder, reference, terrain latent 또는 behavior mode를 구성 | locomotion context | Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for ... | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| Whole-body policy / controller | context에서 joint target 또는 torque를 만든다 | context, body state, contact | RL policy, reference tracking, inverse dynamics 또는 whole-body control을 적용 | joint action/torque | State Space and Action Space The policy's input consists of: Xt =          fvel ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Adaptation / recovery | disturbance와 contact mismatch에 대응한다 | new observation/history와 failure signal | latent adaptation, foothold change, recovery 또는 replan을 수행 | updated command | Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm. | p. 4 (III. METHOD), p. 3 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** All policies were trained to maximize the following reward function: R =0.20 · exp(-qerr) +0.20 · exp(-˙xerr) +0.05 · exp(-xerr) +0.20 · exp(-˙yerr) +0.30 · ...
- **p. 3 / III. METHOD - extractive body cue:** It is important to note that while the reward function is partially based on a reference motion, very similarly to Xie et al.
- **p. 4 / III. METHOD - extractive body cue:** However, correctly calculating the gradient of an RNN requires the use of the backpropagation through time (BPTT) algorithm, which necessitates special measures when sampling from ...
- **p. 4 / III. METHOD - extractive body cue:** The recurrent critic was also an LSTM network with two layers of 128 units each, with a single output representing the value function.
- **Formal bridge:** body/proprioceptive/terrain state -> joint action/torque/footstep -> return, tracking or stability objective -> progress, balance and terrain robustness.
- **Equation/algorithm anchors:** p. 4 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | State, Space, Action, policy, input, consists, fvel, desired, forward, speed, clock, robot, Where, inputs | proprioception, terrain/perception observation과 velocity command | body cue; exact tensor/frame verify |
| State/latent | State, Space, Action, policy, input, consists, fvel, desired, forward, speed | body/contact state, foothold 또는 behavior mode | body cue; notation verify |
| Action/output | State, Space, Action, policy, input, consists, fvel, desired, forward, speed | joint target, torque, footstep 또는 locomotion action | body cue; unit/decoder verify |
| Objective/constraint | policies, trained, maximize, following, reward, function, qerr, xerr, yerr, orienterr | return, tracking or stability objective | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / III. METHOD - extractive body cue:** State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed ...
- **p. 2 / II. BACKGROUND - extractive body cue:** The policy is often a stochastic policy, in which case it is a function π(a/s) which takes in a state s and outputs the parameters ...
- **p. 3 / III. METHOD - extractive body cue:** The outputs of the policy are simply raw motor PD targets, much like Xie et al.
- **p. 4 / III. METHOD - extractive body cue:** Network Architecture All policies had an input dimension of length 49, and an output dimension of size 10.
- **p. 4 / III. METHOD - extractive body cue:** No information about the dynamics disturbances was provided to either the policy or the critic in the input space.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recent work in transferring these trained controllers from simulation onto real robots has also enjoyed encouraging results [1, 2, 3, 4, 5, 6], but many ...
- **p. 2 / II. BACKGROUND - extractive body cue:** The reward r = R(s, a) is a scalar signal that expresses how good a particular state-action pair is.
- **Normalized interface:** observation=proprioception, terrain/perception observation과 velocity command; state=body/contact state, foothold 또는 behavior mode; output/action=joint target, torque, footstep 또는 locomotion action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | gait/skill episode horizon과 short-horizon body control이 계층적으로 분리된다. | Though the reference contains the full robot state at each timestep, we only use the center of mass position, orientation, and velocity, ... | episode/sequence/action-chunk boundary |
| Rate / latency | high-level command, policy rate와 low-level torque rate를 구분; exact rate 확인 필요. | The recurrent policy has connections which loop back onto itself, so that information from previous timesteps is available. | Hz/fps, inference time and control rate |
| Memory | proprioceptive history, terrain latent와 contact/body state. | This produces a memory-like mechanism, allowing the RNN to encode things about the state history which may be useful for choosing actions. | window and reset |
| Compute | policy inference, adaptation encoder와 whole-body/control solve가 latency를 결정한다. | Dots become lighter as a function of time. batch size of 64 trajectories and a maximum trajectory length of 300 timesteps, equal ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / III. METHOD - extractive body cue:** Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end ...
- **p. 4 / III. METHOD - extractive body cue:** Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm.
- **p. 3 / III. METHOD - extractive body cue:** Reward Design Our learning process makes use of a reference trajectory produced by an expert walking controller to help the policy learn in the initial ...
- **p. 5 / IV. RESULTS - extractive body cue:** When training the feedforward policies, we used a batch size of 1024 timesteps.
- **p. 3 / III. METHOD - extractive body cue:** Though we believe that the recurrent policies do not have any theoretical reason for needing a clock input, we were not able to train any ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Optimize, surrogate, klthresh, then, break, During, training, fixed, action, standard, deviation, value, State, Space, policy, input, consists, fvel, desired, forward.
- **Relevant PDF headings:** III. METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Command / terrain state | The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware. | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Whole-body policy / controller | Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without ... | p. 4 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Adaptation / recovery | As can be seen, dynamics randomization improves performance of both policy types and LSTM with dynamics randomization performs the best. | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...
- **p. 4 / IV. RESULTS - extractive body cue:** Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, each ...
- **p. 5 / IV. RESULTS - extractive body cue:** 5: Reward curve of LSTM and FF networks during training without dynamics randomization.
- **p. 5 / IV. RESULTS - extractive body cue:** As can be seen in Figure 5, when trained without dynamics randomization, LSTM networks attain a significantly higher reward than feedforward networks, with surprisingly little ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...
- **p. 6 / V. CONCLUSION - extractive body cue:** The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and promise of this approach.
- **p. 5 / IV. RESULTS - extractive body cue:** We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in Table I.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), objective p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), temporal p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 1 (Abstract), p. 1 (I. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
