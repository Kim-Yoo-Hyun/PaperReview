# Problem - Learning Memory-Based Control for Human-Scale Bipedal Locomotion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss16/p031.html; PDF retrieval source: https://www.roboticsproceedings.org/rss16/p031.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, when trained with dynamics randomization, are able to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Controlling a non-statically stable biped is a difficult problem largely due to the complex hybrid dynamics involved.
- **p. 1 / Abstract - extractive PDF cue:** Recent work has demonstrated the effectiveness of reinforcement learning (RL) for simulation-based training of neural network controllers that successfully transfer to real bipeds.
- **p. 1 / Abstract - extractive PDF cue:** The existing work, however, has primarily used simple memoryless network architectures, even though more sophisticated architectures, such as those including memory, often yield superior performance ...
- **p. 1 / Abstract - extractive PDF cue:** In this work, we consider recurrent neural networks (RNNs) for sim-to-real biped locomotion, allowing for policies that learn to use internal memory to model important ...
- **p. 1 / Abstract - extractive PDF cue:** We show that while RNNs are able to significantly outperform memoryless policies in simulation, they do not exhibit superior behavior on the real biped due ...
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, when trained with ...
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** A common way to help address this sim-to-real challenge is the use of dynamics randomization during simulation-based training.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, ... | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | State Space and Action Space The policy's input consists of: Xt =          fvel ... | proprioception, terrain/perception observation과 velocity command | exact sensor/frame/preprocessing from PDF |
| State / latent | State, Space, Action, policy, input, consists, fvel, desired, forward, speed | body/contact state, foothold 또는 behavior mode | notation and tensor shape require body check |
| Output / action | outputs, policy, simply, motor, targets, much, like, Xie | joint target, torque, footstep 또는 locomotion action | exact unit/frame/decoder require body check |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: State, Space, Action, policy, input, consists, fvel, desired, forward, speed | p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 3 (III. METHOD) |
| Decision / output variable | joint action/torque/footstep; body terms: State, Space, Action, policy, input, consists, fvel, desired | p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: policies, trained, maximize, following, reward, function, qerr, xerr | p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Success / guarantee | progress, balance and terrain robustness | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 4 (IV. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** A common way to help address this sim-to-real challenge is the use of dynamics randomization during simulation-based training.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** In particular, an expressive RNN controller may learn to exploit details of the simulation dynamics that are maladaptive in the real world, leading to failure.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** Memory-based controllers, such as recurrent neural networks (RNN), are a potentially powerful choice for solving highly dynamic nonlinear control problems due to their ability to ...

## What the Paper Changes

PDF contribution framing (p. 3 (III. METHOD), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): State Space and Action Space The policy's input consists of: Xt =          fvel desired forward speed sin( 2πω L ) clock ...

- **p. 2 / I. INTRODUCTION - extractive PDF cue:** One of the main contributions of our work is to demonstrate that this approach is highly effective for training RNN controllers for the Cassie biped.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** We show that by randomizing a small number of dynamics parameters over reasonable ranges, the RNNs can be consistently trained in simulation and successfully transferred ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 3 (III. METHOD), p. 4 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 3 (III. METHOD), p. 4 (III. METHOD), objective p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
