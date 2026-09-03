# Learning Memory-Based Control for Human-Scale Bipedal Locomotion

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss16/p031.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss16/p031.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2020 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, bipedal locomotion, recurrent policy, sim-to-real, online adaptation
- Official paper: https://www.roboticsproceedings.org/rss16/p031.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss16/p031.pdf
- Code/Project: https://www.roboticsproceedings.org/rss16/p031.html
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, when trained with dynamics randomization, are able to consistently transfer ...를 문제로 두고, State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed sin( 2πω L ) clock input cos( ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Controlling a non-statically stable biped is a difficult problem largely due to the complex hybrid dynamics involved.
- **p. 1 / Abstract - extractive body cue:** Recent work has demonstrated the effectiveness of reinforcement learning (RL) for simulation-based training of neural network controllers that successfully transfer to real bipeds.
- **p. 1 / Abstract - extractive body cue:** The existing work, however, has primarily used simple memoryless network architectures, even though more sophisticated architectures, such as those including memory, often yield superior performance ...
- **p. 1 / Abstract - extractive body cue:** In this work, we consider recurrent neural networks (RNNs) for sim-to-real biped locomotion, allowing for policies that learn to use internal memory to model important ...
- **p. 1 / Abstract - extractive body cue:** We show that while RNNs are able to significantly outperform memoryless policies in simulation, they do not exhibit superior behavior on the real biped due ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, when trained with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** A common way to help address this sim-to-real challenge is the use of dynamics randomization during simulation-based training.

## Core Idea

- **p. 3 / III. METHOD - extractive body cue:** State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** One of the main contributions of our work is to demonstrate that this approach is highly effective for training RNN controllers for the Cassie biped.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that by randomizing a small number of dynamics parameters over reasonable ranges, the RNNs can be consistently trained in simulation and successfully transferred ...
- **p. 4 / III. METHOD - extractive body cue:** Optimize surrogate L wrt θ, using ˆs, ˆa, ˆA if KL(πθ(ˆs, ˆa), πθold(ˆs, ˆa)) > klthresh then break end if end for end for end ...
- **p. 4 / III. METHOD - extractive body cue:** Recurrent Proximal Policy Optimization We trained all policies with PPO, a model-free reinforcement learning algorithm.
- **p. 3 / III. METHOD - extractive body cue:** Reward Design Our learning process makes use of a reference trajectory produced by an expert walking controller to help the policy learn in the initial ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed sin( 2πω L ) clock input cos( ... | proprioception, terrain/perception observation과 velocity command | p. 3 (III. METHOD), p. 2 (II. BACKGROUND) |
| State/latent | State, Space, Action, policy, input, consists, fvel, desired, forward, speed, clock, robot | body/contact state, foothold 또는 behavior mode | p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 3 (III. METHOD) |
| Output/action | The policy is often a stochastic policy, in which case it is a function π(a/s) which takes in a state s and outputs the parameters of a distribution, usually the mean and ... | joint target, torque, footstep 또는 locomotion action | p. 2 (II. BACKGROUND), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Objective/outcome | All policies were trained to maximize the following reward function: R =0.20 · exp(-qerr) +0.20 · exp(-˙xerr) +0.05 · exp(-xerr) +0.20 · exp(-˙yerr) +0.30 · exp(-orienterr) +0.05 · exp(-springerr) (1) qerr, ˙xerr, ... | velocity/progress, stability, energy와 terrain generalization | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 3 / III. METHOD - extractive body cue:** State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** One of the main contributions of our work is to demonstrate that this approach is highly effective for training RNN controllers for the Cassie biped.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that by randomizing a small number of dynamics parameters over reasonable ranges, the RNNs can be consistently trained in simulation and successfully transferred ...
- **p. 5 / IV. RESULTS - extractive body cue:** As can be seen, dynamics randomization improves performance of both policy types and LSTM with dynamics randomization performs the best.
- **p. 5 / IV. RESULTS - extractive body cue:** The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware.
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Embodiment/environment | The LSTM achieves a much higher reward with remarkably little variance, but both networks perform roughly the same on hardware. | hardware/simulator version and reset protocol | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Dataset/benchmark | Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, each with separate random seeds. | role, split, size and leakage | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 4 (IV. RESULTS) |
| Metric | Feedforward networks obtain a notably lower reward, with high variance. | definition, denominator, direction and uncertainty | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 4 (IV. RESULTS) |
| Baseline/ablation | Simulation We trained ten LSTM networks and ten FF networks with dynamics randomization, and ten LSTM networks and ten FF networks without dynamics randomization, each with separate random seeds. | fair input/data/compute/action matching | p. 4 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and demonstrate learned, memory-based control on the bipedal ...
- **p. 6 / V. CONCLUSION - extractive body cue:** The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and promise of this approach.
- **p. 5 / IV. RESULTS - extractive body cue:** We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in Table I.

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 locomotion 문제를 이해하기 위해 읽는다. 본문은 RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, when trained with dynamics randomization, are able to consistently transfer ...를 문제로 두고, State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed sin( 2πω L ) clock input cos( ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD), p. 3 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
