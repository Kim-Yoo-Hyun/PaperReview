# Problem - Learning Memory-Based Control for Human-Scale Bipedal Locomotion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss16/p031.html; PDF retrieval source: https://www.roboticsproceedings.org/rss16/p031.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, when trained with dynamics randomization, are able to ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Controlling a non-statically stable biped is a difficult problem largely due to the complex hybrid dynamics involved.
- **p. 1 / Abstract - extractive body cue:** Recent work has demonstrated the effectiveness of reinforcement learning (RL) for simulation-based training of neural network controllers that successfully transfer to real bipeds.
- **p. 1 / Abstract - extractive body cue:** The existing work, however, has primarily used simple memoryless network architectures, even though more sophisticated architectures, such as those including memory, often yield superior performance ...
- **p. 1 / Abstract - extractive body cue:** In this work, we consider recurrent neural networks (RNNs) for sim-to-real biped locomotion, allowing for policies that learn to use internal memory to model important ...
- **p. 1 / Abstract - extractive body cue:** We show that while RNNs are able to significantly outperform memoryless policies in simulation, they do not exhibit superior behavior on the real biped due ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, when trained with ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** A common way to help address this sim-to-real challenge is the use of dynamics randomization during simulation-based training.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | RNNs trained without dynamics randomization are unable to consistently transfer to hardware (failures darkened and overlaid with X), while the same RNNs, ... | legged robot, terrain과 contact dynamics | body wording is the source claim |
| Observation / input | 목표 전진 속도, 보행 위상의 사인·코사인, 추정한 몸체 방향·관절 위치·속도 | 49차원 정책 입력 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| State / latent | LSTM의 순환 상태 | 기억 없는 정책과 비교 | [PDF 4쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=4) |
| Output / action | 중립 자세에 더할 모터 위치 목표 | 약 33 Hz 정책과 2 kHz 관절 PD 제어 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| Target outcome | progress, balance and terrain robustness | velocity/progress, stability, energy와 terrain generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | body/proprioceptive/terrain state; body terms: State, Space, Action, policy, input, consists, fvel, desired, forward, speed | p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 3 (III. METHOD) |
| Decision / output variable | 중립 자세에 더할 모터 위치 목표 | [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) |
| Objective / loss / cost | return, tracking or stability objective; cue terms: policies, trained, maximize, following, reward, function, qerr, xerr | p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Success / guarantee | progress, balance and terrain robustness | p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 4 (IV. RESULTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** A common way to help address this sim-to-real challenge is the use of dynamics randomization during simulation-based training.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In particular, an expressive RNN controller may learn to exploit details of the simulation dynamics that are maladaptive in the real world, leading to failure.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Memory-based controllers, such as recurrent neural networks (RNN), are a potentially powerful choice for solving highly dynamic nonlinear control problems due to their ability to ...

## What the Paper Changes

속도·위상·로봇 상태 입력을 공유하는 조건에서 순환 정책과 기억 없는 정책을 비교한다. [PDF 3쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss16/p031.pdf#page=4)

- **p. 2 / I. INTRODUCTION - extractive body cue:** One of the main contributions of our work is to demonstrate that this approach is highly effective for training RNN controllers for the Cassie biped.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We show that by randomizing a small number of dynamics parameters over reasonable ranges, the RNNs can be consistently trained in simulation and successfully transferred ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 1 | Fig. 1: We use recurrent neural networks and dynamics randomization to greatly improve the sim-to-real transfer rate and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | The policies were learned and tested first in simulation, then transferred to the robot, demonstrating the robustness and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | We conducted a robustness test in simulation across ten chosen sets of dynamics, taken from the range in ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

locomotion writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 3 (III. METHOD), p. 4 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 2 (II. BACKGROUND), p. 3 (III. METHOD), p. 4 (III. METHOD), objective p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
